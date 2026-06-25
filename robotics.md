---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-25T00:14:21.825431+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** June 25, 2026 at 00:14 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Robotics for data centers](https://www.reddit.com/r/robotics/comments/1uerhc1/robotics_for_data_centers/)**

The scarce thing in a data center is not manpower, but instinct that only comes from years on the floor. Most robotics companies are focused on robots as a productivity amplifiers: 24/7 uptime, five days of work done in two. Few are focused on the potential of robots to change how people work altogether. We wanted to show what it looks like to rethink human-robot collaboration, using AI so a shrinking pool of experts can meet the increasing demands of future infrastructure. The obvious thing to automate is the rote physical work that consumes an expert's attention without needing critical judgment. Cabling tasks are the most common example of this. They're necessary when setting up any rack, but usually one-off, and labor is readily available to address this need. We think this is a good place to start, but the least interesting place to change how people work. Standard operating procedures (SOPs) are how critical infrastructure stays stable, and they're the work that scales worst. The video shows one common procedure: clearing the cables a technician leaves behind after testing, and reconciling the rack to a stable state for the next test. A robot that runs SOPs the same way every time, never skipping a step, keeps the system in a known, predictable state. This reduces the cognitive overhead on experts so they can solve harder problems. What most excites us is robots guiding where an expert's attention should go. In the video, the robot checks the switches with a thermal camera, then makes a judgment on whether the increase in temperature is a real problem or a spurious reading. This instinct requires an expert to synthesize all available background context and accumulated lessons from past failures. This is where we want to double down, and show how human-robot collaboration places scarce expert attention exactly where it matters. More to come.

2h ago

---

**[Beni, daily durability test.](https://www.reddit.com/r/robotics/comments/1ueauex/beni_daily_durability_test/)**

From Mondo Robotics on 𝕏: https://x.com/mondorobotics/status/2059305305553723725

12h ago

---

**[MuJoCo derived Simulator for High Fidelity Vision RL training natively on GPU](https://www.reddit.com/r/robotics/comments/1uel4j5/mujoco_derived_simulator_for_high_fidelity_vision/)**

Hi everyone, For the past couple of weeks I have been working on a simulator project considering the shortcomings of MuJoCo. There are things that people like and also don't like about MuJoCo, like the CPU dependency on MuJoCo which makes the simulation not parallelizable beyond a certain limit (depending on the hardware). I know there exists MJX which is GPU accelerated, however, it is not really made for vision based RL pipelines and training. There is also NVIDIA Isaac ecosystem, but that requires a powerful GPU, thus making it limited in terms of accessibility, let alone it requires license. This is why I worked out this new simulator (still working on it, so there will be significant bugs which require fixing). I call it MuJoFil => MuJoCo + Google's Filament Render Engine. Basically I used Nvidia's Newton Physics Engine (which itself is based on MuJoCo's physics engine but is GPU native), clubbed it with Google's Filament render engine (both of these are open-source), modified Filament significantly to support working natively on GPU to render multiple simulations in parallel, and worked on optimizing it for performance. So what is MuJoFil? It is supposed to be an open-source high visual fidelity simulator optimised for a highly parallelized RL training pipeline so that users can use it to train Vision based Policies. Besides, it offers PBR textures support and also a simple to use plug and play functionality, where you can use any environments available online and support formats such as GLB, OpenUSD, etc. for setting environments for your robots. Basically, now you aren't just limited to environments native to MuJoCo, but rather you can use any environments available online from sketchfab, polyhaven, etc. and use it as a practical robot simulation environment. Check it out for yourself in the video. I would really appreciate it if you guys could tell how you feel about it and suggest ideas for what all things I can incorporate into it as this is going to be a fully open-source and free to use simulator that I have been working on for weeks. PS: While I have a couple of published research papers at top RL and AI/ML venues in the field of RL, I still consider myself a learner in this field who is continuously trying, learning, and building stuff, so there will be things in this hugely ambitious project which I might have missed to work on, and that is where I want help from you people who understand this field well. Sorry for this lengthy post and thanks if you read it till here🙇🙇🙏, I would really appreciate if you could share your thoughts on it. Also, I will make its code repo public on GitHub, but till then you can definitely check it out on PyPI. There are 2 separate packages, one can be installed using: "pip install mujofil" This is the CPU based variant, whereas there is a CUDA supporting GPU native variant about which I mentioned above, you can currently install it using: "pip install mujofil-warp" I am planning on changing its name to mujofil-cuda instead of mujofil-warp as that apparently sounds more intuitive to my direct peers but you can suggest this name as well. Thank you for the support❤️.

6h ago

---

**[Simulation of a smartphone assembly line](https://www.reddit.com/r/robotics/comments/1ue7axb/simulation_of_a_smartphone_assembly_line/)**

Simulation of a smartphone assembly line that I recently made. Everything is physics-driven. All axes, including robots, are driven using PD-controllers. Parts collide using precise collision geometry with submillimeter tolerances. Disclaimer: I work for ProtoTwin.

16h ago

---

**[The LLVM for Robot Descriptions. A programmable IR engine to compose, validate, and compile URDF/XACRO/SRDF models from Python or Blender.](https://www.reddit.com/r/robotics/comments/1uepmdt/the_llvm_for_robot_descriptions_a_programmable_ir/)**

3h ago

---

**[Unitree Go1 unusable with jetson](https://www.reddit.com/r/robotics/comments/1ueuidv/unitree_go1_unusable_with_jetson/)**

I have to use a Unitree Go1 with a jetson AGX orin strapped to it for a university project. It's so hard to iterate because as soon as I get close to making progress, I have to power the whole thing off and replace the battery. Now I know you should run heavy processing offline and communicate with the robot over a network, but what I am doing is basically ROS2 troubleshooting for which I need the setup exactly as it will be during deployment. Exactly how is this "robotics revolution" powered by vision-language-action models supposed to work, when the most popular quadruped cannot even power a jetson for more than 15 minutes standing still??? I always thought VLA was an impractical idea, but now I am even less convinced.

3m ago

---

**[Using UWB for Real-Time Race Car Tracking in an Indoor Racing Arena](https://www.reddit.com/r/robotics/comments/1ue0w6n/using_uwb_for_realtime_race_car_tracking_in_an/)**

Recently, we worked on an indoor racing track project. We had to deploy a real-time tracking system for a fleet of miniature racing cars on an indoor track at an entertainment park. The goal was to display each car's position, trajectory, and race ranking on a large screen while maintaining smooth updates and reliable tracking performance. As we know, Ultra-wideband (UWB) is a technology that enables secure, reliable ranging and precision sensing, through wireless communication, but the main problem of UWB is the signal mutual conflicts/interference, that when multiple anchors&tags exists. That is why MaUWB, which is based on STM32 controller and DW3000, solves the signal mutual conflicts with TDMA, widely used in different positioning and tracking projects. (picture 1) The Hardware Deployment Anchors (Fixed Nodes):8 fixed Anchors installed around the racing track (picture 2) Tags (Mobile Nodes): A custom UWB Tag installed on each race car (picture 3) One of the key challenges was maintaining stable operation with multiple moving Tags within the same positioning area. To reduce signal conflicts and ranging interference, the system uses a TDMA-based scheduling mechanism. This approach significantly improves stability and eliminates signal mutual conflicts when the cars move together. Result By combining software and hardware architecture, Position data is updated in real time and rendered on a large display screen. (picture 4) · Real-time vehicle positions · Driving trajectories · Dynamic race rankings The deployment of the MaUWB project not only greatly improved the gaming experience and visual effects but also reduced the difficulty of using UWB technology, which provides great convenience and a solid foundation for project software development. I'd be interested to hear how you handle multi-tag UWB deployments, especially when scaling multiple moving devices. Let's discuss in the comments!

21h ago

---

**[Mister Mischief: The esp32 pet robot project using FREERTOS](https://www.reddit.com/r/robotics/comments/1ue7orv/mister_mischief_the_esp32_pet_robot_project_using/)**

Hello r/robotics. Greetings, this is my first post here. I Live alone. I get lonely sometimes. I cant own a dog. Then I thought, let me build one for myself (i've always been a tinkerer at heart) But then, reality hit like a freight train. I am not a good coder and I dont even work in the field of IT. So I looked at it as a passion project which I work on in my free time. Then I started searching the net for good quality hardware and settled with the esp32 s3 (n16r8) devkit-c1. Its a clone and not an official espressif board. But atleast it has USB-C. Then I thought of doing this the right way. I wanted to use Ardurover but its complicated with the esp32. So I resorted to FreeRTOS and code myself. Im using VSCode with the Platformio extension. Here are the details: Project: Mister Mischief the Robot 1. Hardware MCU: Esp32 s3 (n16r8) devkit-c1 working of a Mini560 buck converter (3.3v) soldered on a perfboard Sensors: GY-91 (clone, unfortunately) with an MPU6500 imu and a BMP280 barometer, HC-SR04 Sonar. Actuators: Dual GB-33 520 motors (350rpm, no encoders, yet!) paired to an XY-160D motor driver Battery: 2s Molicel P50B 21700 Li-ion cells 2. Architecture A central nervous system (GlobalDataBus) which holds all the data from sensors, actuators and tasks, event latches. All this happens inside FreeRTOS spinlocks (critical sections) to avoid memory tearing and random crashes. Tasks use this bus to process events and switch moods and modes (I have many of them currently) and set Event Latches (examples: "isLowering", "isTeasing", "hasExperiencedLift", etc.) 3. Features A fully fleshed out Bluetooth LE control and telemetry stream. Also, an Android App (working on Android Studio for this) which can read the realtime telemetry and display it in the dashboard. It can also control the robot in Manual Override mode (Yes! Remote control). Im not doing this with json but with raw bytes (both the telemetry and the control commands) so that its light weight on the BT LE. PID enabled drive, it holds its heading really well. Autotuning mode( Ardupilot style) which to my surprise perfectly tuned the robot in one attempt. A full fledged terminal which can take commands like "get <variable-name>", "set <variable-name>", "reset <variable-name>", "reset ALL", "reboot> (I am saving configurations in the non volatile storage of the esp32). This currently works over the serial terminal and I'm yet to flesh this out in the Android app. 4. Further additions Four bottom facing IR distance sensors mounted at the the four corners so that it can detect cliffs and dangerous situations. I need to get a lidar (its expensive!) so that I can enable true localization. Since the chassis lifts off when i place it with its "backside" on the floor, I think I can enable "self-balance" mode. Since the sonar will now be facing towards the ceiling, we can use it to interface with the robot in this mode. The event latches are not firing properly and the state (the Behaviour Engine) machine is inconsistent in switching modes. The Wifi keeps crashing and crashing. I've kept it off with the command "set WIFI_ACTIVE off". You can try and see by setting your wifi details by doing: set "WIFI_SSID "<your-ssid>" then set WIFI_PASSWORD "<your-wifi-password>" then connect WIFI (but it will crash I think). You need to enclose the SSID and Password in double quotes in the terminal. Tuning, Autotuning and mode triggers from the android app. Basically, I want it to be a mischiveous little companion that greets me when I get back from work, wanders around the house, topples things over, had mood swings, the lot. Whatever we can imagine! You might ask, Why did'nt you use ROS? Heres Why: Im not sure that I can incorporate these Moods and Modes that I have and MicroRos just doesnt cut it! I dont want to drag along a bulky SBC like a raspberry pi. There is networking feature but I want it to function entirely self-contained and standalone even when there's no internet or any connection of any sort. Battery Backup. I want it to have a good battery backup (another reason why I ditched JSON) I wouldnt have gotten to learn so much. I did extensively use AI (sorry in advance if its not allowed here, sincerely!) to build this much. I got to learn so much from this. But its getting out of my hand now and its hard to track the progress of my own work as I Have to work on both the Robot side and the Android App side. But I have tried to keep the code as modular as possible to the best of my abilities. Please feel free to have a look at my repository for both the robot side code and the Android App side code. If anyone is interested to work on this and wants a companion during those times of loneliness, Im inviting them to work on this like me, in their free time. So please feel free to notify me. But I dont even know how to allow anyone else to work on the same project on Github. You'll have to guide me I guess. P.s. I had also posted this over in r/esp32 but since I couldnt add images here, im posting it afresh here so that I can add images. Link to Mister Mischief Robot side repository: Mister Mischiev V1 Link to Mister Mischief Android App: Mister Mischief Android App

15h ago

---

**[GM-PHD in C++](https://www.reddit.com/r/robotics/comments/1ueb725/gmphd_in_c/)**

I just wanted to share my C++ implementation of GM-PHD filter: https://github.com/borodziejciesla/gm-phd For now only point objects implementation is working, but I am working on extended objects implementation.

12h ago

---

**[VLAs vs Nvidia world models vs all of that: where are we going?](https://www.reddit.com/r/robotics/comments/1udicvb/vlas_vs_nvidia_world_models_vs_all_of_that_where/)**

I'm reading the papers of Cosmos3 and Dreamzero and they looks very promising (compared to memoryless VLAs). And I am wondering where the filed will evolve. Based on your practical experience with new models, what's your bet between VLAs, WM, Jepa-style, WAM, RL approaches, and all of that? I worked so far with VLAs (eg pi05), and I don't have any experience in using the nvidia stack so far, of and other world action models. I am thinking if I should invest time in changing the base policy, and I'd appreciate some feedback form who has tested them (ie: the open source/weights model available, and capable of inference without one thousand gb of vram) On my side I'm a fan of model working planning latent space; video action models (which have more temporal coherence wrt vla), but I also feel that semantic power of a VLM should be present aswell. Ps: suggested survey reading in this topic: "World Model for Robot Learning: A Comprehensive Survey" Happy to discuss with you

1d ago

---

---

## Google News: "robotics"

**[Exclusive | Agility, Maker of Humanlike Robots, to Go Public in $2.5 Billion SPAC Deal](https://www.wsj.com/finance/agility-maker-of-humanlike-robots-to-go-public-in-2-5-billion-spac-deal-62c3cb32)**

WSJ • 20h ago

---

**[Lutnick privately warned top executives of possible action against imported Chinese robots](https://www.politico.com/news/2026/06/23/lutnick-china-robots-commerce-00972576)**

Politico • 1d ago

---

**[‘Who is going to pay us when we’re replaced by robots?’ The Indian factory workers told to film themselves for AI](https://www.theguardian.com/global-development/2026/jun/24/indian-factory-workers-told-film-themselves-for-ai-robots)**

When workers had cameras attached to them, they found it funny at first. But novelty soon turned to concern

The Guardian • 19h ago

---

**[Morgan Stanley doubles China humanoid robot shipment forecast as commercialization accelerates](https://www.cnbc.com/2026/06/24/morgan-stanley-china-humanoid-robot-market-forecast.html)**

Morgan Stanley has sharply raised its outlook for China's humanoid robotics market, as early commercial deployment in real-world scenarios accelerated.

CNBC • 17h ago

---

**[Boston Dynamics to build "advanced robotics and AI center" in Massachusetts, add over 1,000 jobs](https://www.cbsnews.com/boston/news/boston-dynamics-expansion-waltham-ai-center-jobs/)**

Boston Dynamics is expanding with a new robotics and AI center in Waltham, Massachusetts.

CBS News • 8h ago

---

**[Suppliers eye $5 trillion humanoid robot market despite value-capture concerns](https://www.autonews.com/manufacturing/suppliers/ane-supplier-target-humanoid-robot-market-0624/)**

Suppliers such as Bosch and Schaeffler are joining the humanoid robotics market with manufacturing expertise from electric vehicles and high-volume production.

Automotive News • 15h ago

---

**[NASA Announces Spacewalkers for Robotic Arm Repair Work](https://www.nasa.gov/blogs/spacestation/2026/06/23/nasa-announces-spacewalkers-for-robotic-arm-repair-work/)**

Spacewalk preparations filled the schedule aboard the International Space Station on Tuesday as a pair of astronauts gear up for next week’s external robotics repair job. CubeSat maintenance and eye checks rounded out the day for the Expedition 74 crew.

NASA (.gov) • 1d ago

---

**[Karl Storz laying off employees in North Carolina amid robotics strategy shift](https://www.medtechdive.com/news/karl-storz-laying-off-employees-in-north-carolina-amid-robotics-strategy-sh/823428/)**

The cuts come as Karl Storz plans to retire the Asensus brand and the Senhance robot as part of organizational changes.

MedTech Dive • 2d ago

---

**[NVIDIA Announces Halos for Robotics, the Industry’s First Full-Stack Safety System for Physical AI](https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai)**

NVIDIA today announced NVIDIA Halos for Robotics, the industry’s first full-stack, comprehensive safety system for robotics and physical AI that unifies AI compute and safety.

NVIDIA Newsroom • 2d ago

---

**[Nvidia Targets $200 Billion Humanoid Robotics Market](https://finance.yahoo.com/technology/ai/articles/nvidia-targets-200-billion-humanoid-193251306.html)**

Nvidia is offering Halos software and IGX Thor hardware to help robots operate more safely around people.

Yahoo Finance • 2d ago

---

---

## YouTube Videos: "robotics"

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 52K • 👍 949 • 💬 79 • ⏱️ 24:13 • 5d ago

---

**[Elon Musk&#39;s Scary Warning About Robots 🤖⚠️#elonmusk #shorts](https://www.youtube.com/watch?v=VCPff7vrBBs)**

Elon Musk's Scary Warning About Robots ⚠️#elonmusk #shorts Elon Musk explains a terrifying reality about the future of AI ...

📺 PodRavix

👁️ 477 • 👍 9 • ⏱️ 0:24 • 5h ago

---

**[GM lays off 1,000 workers and adds robots to its assembly line](https://www.youtube.com/watch?v=QPGQOivUt-g)**

General Motors has cut 1000 jobs at its Detroit facility, and it later installed about 50 robots on the assembly line. GM has faced ...

📺 NewsNation

👁️ 22K • 👍 330 • 💬 402 • ⏱️ 2:04 • 1d ago

---

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 57K • 👍 1K • 💬 209 • ⏱️ 13:45 • 3d ago

---

**[Prime Day Robot Vacuum Deals 2026 — What&#39;s Worth It and What to Skip](https://www.youtube.com/watch?v=F9m4Shls9-A)**

2026 Best Amazon Prime Sales on Robot Vacuums and Mop combo See Full Amazon Prime Robot Vacuum sales ...

📺 Just A Dad Approved

👁️ 10K • 👍 198 • 💬 126 • ⏱️ 18:57 • 1d ago

---

**[THIS Titan Buiold is STILL absolutely PUNISHING in War Robots](https://www.youtube.com/watch?v=j065lGeWEGY)**

War Robots Gameplay: Princeps going berserk - WR My War Robots Creator Link: https://wr.my.games/manni - Code: 'manni' ...

📺 Manni-Gaming

👁️ 5K • 👍 304 • 💬 107 • ⏱️ 11:36 • 12h ago

---

**[Inside the Warehouse Where Jobs Got DELETED 🤖📦](https://www.youtube.com/watch?v=vJYUmPVph0I)**

Welcome to the future of logistics. This fully automated warehouse in China operates 24/7 in complete darkness. Relying entirely ...

📺 Wealthy Capital

👁️ 100K • 👍 441 • 💬 47 • ⏱️ 0:09 • 1d ago

---

**[Ready, set, row: Humanoid robots partake in Dragon Boat Festival!](https://www.youtube.com/watch?v=IsLt7IdtcNo)**

At China's Dragon Boat Festival, everybody takes place – including the robots. In southwest China's Sichuan Province, ...

📺 CGTN Europe

👁️ 19K • 👍 92 • 💬 13 • ⏱️ 0:49 • 4d ago

---

**[$700K Robot Nanny Knows KUNG FU?! 😱🥋#shorts #funny #robot](https://www.youtube.com/watch?v=zv0PuRKDIWA)**

shorts #anime #fyp #recap #foryou 【Updated daily,welcome to subscribe!】

📺 RECAP Animation

👁️ 24K • 👍 332 • 💬 3 • ⏱️ 1:43 • 8h ago

---

**[Unitree R1  Affordable Humanoid Robot Does Backflips!](https://www.youtube.com/watch?v=O4aKWgQY1j8)**

The Unitree R1 humanoid robot is making headlines with a starting price of just $4900. Watch this robot show off impressive ...

📺 DPCcars

👁️ 547 • 👍 31 • 💬 1 • ⏱️ 1:43 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*

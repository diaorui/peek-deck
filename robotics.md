---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-25T08:23:20.567591+00:00'
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

**Last Updated:** June 25, 2026 at 08:23 UTC  
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

10h ago

---

**[Robotica arm 3d printed](https://www.reddit.com/r/robotics/comments/1uf0mf1/robotica_arm_3d_printed/)**

3h ago

---

**[Beni, daily durability test.](https://www.reddit.com/r/robotics/comments/1ueauex/beni_daily_durability_test/)**

From Mondo Robotics on 𝕏: https://x.com/mondorobotics/status/2059305305553723725

20h ago

---

**[Humanoid robot walking on its own across the room in sim.](https://www.reddit.com/r/robotics/comments/1uf3qd2/humanoid_robot_walking_on_its_own_across_the_room/)**

- chase: third-person view of the humanoid walking to the goal - POV cam: the robot's onboard RGB, with the planner overlay (🟢 global A* path, 🔴 immediate move) - metric depth: Depth-Anything 2's per-pixel depth - occupancy map: top-down log-odds grid being built live-> white=free, red=obstacle+inflation, green dot=robot, blue=goal, green line=A* path The robot starts with no map. It draws one as it walks, steering around furniture to reach a goal in the next room. This is a monocular-vision stack for perception, mapping, and navigation: Depth-Anything-V2 turns each RGB frame into metric depth, visual-inertial odometry (VIO) fuses that depth with the IMU for pose, the two build a live occupancy map, and an A*/DWA planner walks the robot to the goal. What would make this more close to reality? Curious to know what tends to break first when a stack like this moves onto hardware.

23m ago

---

**[Unitree Go1 unusable with jetson](https://www.reddit.com/r/robotics/comments/1ueuidv/unitree_go1_unusable_with_jetson/)**

I have to use a Unitree Go1 with a jetson AGX orin strapped to it for a university project. It's so hard to iterate because as soon as I get close to making progress, I have to power the whole thing off and replace the battery. Now I know you should run heavy processing offline and communicate with the robot over a network, but what I am doing is basically ROS2 troubleshooting for which I need the setup exactly as it will be during deployment. Exactly how is this "robotics revolution" powered by vision-language-action models supposed to work, when the most popular quadruped cannot even power a jetson for more than 15 minutes standing still??? I always thought VLA was an impractical idea, but now I am even less convinced.

8h ago

---

**[Sorting bolts and screws. The location and size of screws is detected with a camera. A robotic gripper picks them up and puts them in a drop-off cart.](https://www.reddit.com/r/robotics/comments/1uf363x/sorting_bolts_and_screws_the_location_and_size_of/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/XQdOJ0K_NJU) • 57m ago

---

**[MuJoCo derived Simulator for High Fidelity Vision RL training natively on GPU](https://www.reddit.com/r/robotics/comments/1uel4j5/mujoco_derived_simulator_for_high_fidelity_vision/)**

Hi everyone, For the past couple of weeks I have been working on a simulator project considering the shortcomings of MuJoCo. There are things that people like and also don't like about MuJoCo, like the CPU dependency on MuJoCo which makes the simulation not parallelizable beyond a certain limit (depending on the hardware). I know there exists MJX which is GPU accelerated, however, it is not really made for vision based RL pipelines and training. There is also NVIDIA Isaac ecosystem, but that requires a powerful GPU, thus making it limited in terms of accessibility, let alone it requires license. This is why I worked out this new simulator (still working on it, so there will be significant bugs which require fixing). I call it MuJoFil => MuJoCo + Google's Filament Render Engine. Basically I used Nvidia's Newton Physics Engine (which itself is based on MuJoCo's physics engine but is GPU native), clubbed it with Google's Filament render engine (both of these are open-source), modified Filament significantly to support working natively on GPU to render multiple simulations in parallel, and worked on optimizing it for performance. So what is MuJoFil? It is supposed to be an open-source high visual fidelity simulator optimised for a highly parallelized RL training pipeline so that users can use it to train Vision based Policies. Besides, it offers PBR textures support and also a simple to use plug and play functionality, where you can use any environments available online and support formats such as GLB, OpenUSD, etc. for setting environments for your robots. Basically, now you aren't just limited to environments native to MuJoCo, but rather you can use any environments available online from sketchfab, polyhaven, etc. and use it as a practical robot simulation environment. Check it out for yourself in the video. I would really appreciate it if you guys could tell how you feel about it and suggest ideas for what all things I can incorporate into it as this is going to be a fully open-source and free to use simulator that I have been working on for weeks. PS: While I have a couple of published research papers at top RL and AI/ML venues in the field of RL, I still consider myself a learner in this field who is continuously trying, learning, and building stuff, so there will be things in this hugely ambitious project which I might have missed to work on, and that is where I want help from you people who understand this field well. Sorry for this lengthy post and thanks if you read it till here🙇🙇🙏, I would really appreciate if you could share your thoughts on it. Also, I will make its code repo public on GitHub, but till then you can definitely check it out on PyPI. There are 2 separate packages, one can be installed using: "pip install mujofil" This is the CPU based variant, whereas there is a CUDA supporting GPU native variant about which I mentioned above, you can currently install it using: "pip install mujofil-warp" I am planning on changing its name to mujofil-cuda instead of mujofil-warp as that apparently sounds more intuitive to my direct peers but you can suggest this name as well. Thank you for the support❤️.

14h ago

---

**[I mean chat only helped a little 🫪](https://www.reddit.com/r/robotics/comments/1uf1o8e/i_mean_chat_only_helped_a_little/)**

2h ago

---

**[I never thought a robot would replace me one day..what’s my purpose then.](https://www.reddit.com/r/robotics/comments/1uf40aa/i_never_thought_a_robot_would_replace_me_one/)**

Is this the Move-37 moment for flooring? I know, this machine is engineered for this job and probably needs close to perfect conditions to work, hence lacking the "creativity" of AlphaGo. But still, don't look where we are today, but 2 more machines down the line. Seems frightening for flooring installers at least.

7m ago

---

**[Controlling the posture of the robot dog 'Mini Pupper' with BNO055](https://www.reddit.com/r/robotics/comments/1ueygi9/controlling_the_posture_of_the_robot_dog_mini/)**

（Translating this interesting Japanese post into English for the community! [Repost/Translation] Original link provided at the end.） We are diving right into microcontroller-based control today to explore some new IMU sensors for the Mini Pupper. Here is the breakdown: Table of contents BNO055 Integrating the BNO055 into Mini Pupper Key Notes Party Trick Time! Conclusion BNO055 Previously, I used the ATOM Matrix for control and had fun experimenting with attitude control using its built-in MPU6886 IMU sensor. My goal was to track the Yaw angle (rotation around the gravity axis) so the robot could keep facing the same direction even when the floor beneath it rotated. However, the MPU6886 suffered from significant Yaw drift, forcing me to abandon that approach. In this post, I’m switching to a different IMU sensor to finally achieve accurate Yaw control. To be fair, it's no surprise that a 6-axis IMU like the MPU6886 struggles with Yaw. That said, even with another 6-axis sensor like the MPU6050, you can actually get a relatively low-drift Yaw angle after a proper offset calibration. I could have gone with the MPU6050, but I decided to try out the BNO055 9-axis IMU sensor instead. Honestly, while the internal processing of the BNO055 is a bit of a black box, it delivers highly accurate attitude angles. You can get precise orientation data right out of the box without any tedious calibration or manual compensation using this sample code. Integrating the BNO055 into Mini Pupper I could have simply added the BNO055 to my previous ATOM Matrix setup. However, adding an extra IMU to a board that already integrates an MPU6886 felt way too redundant, and I just couldn't accept it. So, I opted for the ATOM Lite as the controller instead. BNO055 Circuit Board Key Notes While the BNO055 communicates via I2C, I ran into an issue where using M5Atom.h from the M5Stack Arduino library prevented me from mapping custom I2C pins for the Adafruit_BNO055 library. https://preview.redd.it/obc4fr764r8h1.png?width=1196&format=png&auto=webp&s=72d581213069e44203c269b73a8353f036312c93 To bypass this, I skipped the M5Stack library entirely and programmed the ATOM Lite using the standard ESP32 Arduino framework instead. This allowed me to freely specify the I2C pins, and communication with the BNO055 worked flawlessly. In this setup, I assigned Wire.begin(25, 21) for the BNO055 and Wire1.begin(22, 19) for the PCA9685 servo driver. I can confirm that everything runs perfectly without any issues! Reading attitude data with the BNO055, controlling the servos with the PCA9685, and lighting up the NeoPixels —— I've finally built my ideal board! Party trick Time! Thanks to the BNO055, I can now get highly accurate orientation angles. No Kalman filtering or complex algorithms needed—I just used the raw angle data straight from the sensor. The BNO055 is a beast and made this incredibly easy. I tested out the Yaw-based turn control to keep the robot locked onto a single heading while rotating. The longed-for Mini Pupper party trick Looks great! The walking gaits I programmed earlier are also working perfectly. ATOM Lite version Mini Pupper is also doing very well Even when the floor is tilted, parallel control based on foot height is smoothly achieved using only the attitude angle P control of BNO055. Conclusion I had a blast using the BNO055 9-axis IMU sensor to control the Mini Pupper. The BNO055 is honestly a game-changer—it finally allowed me to bring my dream Mini Pupper party trick to life! It's incredibly rewarding to watch this little robot get smarter and smarter. I'll definitely keep learning and experimenting! Original Japanese Post Original X Post #1 (Media) Original X Post #2 (Media) Original X Post #3 (Media) Original X Post #4 (Media)

5h ago

---

---

## Google News: "robotics"

**[Exclusive | Agility, Maker of Humanlike Robots, to Go Public in $2.5 Billion SPAC Deal](https://www.wsj.com/finance/agility-maker-of-humanlike-robots-to-go-public-in-2-5-billion-spac-deal-62c3cb32)**

WSJ • 22h ago

---

**[Lutnick privately warned top executives of possible action against imported Chinese robots](https://www.politico.com/news/2026/06/23/lutnick-china-robots-commerce-00972576)**

Politico • 1d ago

---

**[Inside India newsletter: Meet the humans teaching robots to perform routine tasks, as India finds a way to enter the AI race](https://www.cnbc.com/2026/06/25/inside-india-newsletter-humans-are-teaching-robots-to-do-ai.html)**

Several companies have cropped up in India providing video training data made by humans that is being used to teach robots in the U.S. and China.

CNBC • 8h ago

---

**[‘Who is going to pay us when we’re replaced by robots?’ The Indian factory workers told to film themselves for AI](https://www.theguardian.com/global-development/2026/jun/24/indian-factory-workers-told-film-themselves-for-ai-robots)**

When workers had cameras attached to them, they found it funny at first. But novelty soon turned to concern

The Guardian • 1d ago

---

**[Suppliers eye $5 trillion humanoid robot market despite value-capture concerns](https://www.autonews.com/manufacturing/suppliers/ane-supplier-target-humanoid-robot-market-0624/)**

Suppliers such as Bosch and Schaeffler are joining the humanoid robotics market with manufacturing expertise from electric vehicles and high-volume production.

Automotive News • 23h ago

---

**[NASA Announces Spacewalkers for Robotic Arm Repair Work](https://www.nasa.gov/blogs/spacestation/2026/06/23/nasa-announces-spacewalkers-for-robotic-arm-repair-work/)**

Spacewalk preparations filled the schedule aboard the International Space Station on Tuesday as a pair of astronauts gear up for next week’s external robotics repair job. CubeSat maintenance and eye checks rounded out the day for the Expedition 74 crew.

NASA (.gov) • 1d ago

---

**[Boston Dynamics to build "advanced robotics and AI center" in Massachusetts, add over 1,000 jobs](https://www.cbsnews.com/boston/news/boston-dynamics-expansion-waltham-ai-center-jobs/)**

Boston Dynamics is expanding with a new robotics and AI center in Waltham, Massachusetts.

CBS News • 16h ago

---

**[Hyundai workers in South Korea vote to strike over fears of robots replacing them](https://www.ft.com/content/e5f2892a-d3b1-4779-88db-8d3b034b078a?syn-25a6b1a6=1)**

Union at country’s largest carmaker wants greater say over how AI and automation are introduced

Financial Times • 22h ago

---

**[Karl Storz laying off employees in North Carolina amid robotics strategy shift](https://www.medtechdive.com/news/karl-storz-laying-off-employees-in-north-carolina-amid-robotics-strategy-sh/823428/)**

The cuts come as Karl Storz plans to retire the Asensus brand and the Senhance robot as part of organizational changes.

MedTech Dive • 2d ago

---

**[After Successfully Selling Over 15 Cars, Faraday Future Would Now Like You To Buy Its Robots](https://www.engadget.com/2201189/after-successfully-selling-over-15-cars-faraday-future-would-now-like-you-to-buy-its-robots/)**

Faraday Future recently showed off a lineup of robots as part of the electric car maker's latest pivot.

Engadget • 9h ago

---

---

## YouTube Videos: "robotics"

**[New Chinese Humanoid Robots at ICRA 2026](https://www.youtube.com/watch?v=pn69HUvg8_M)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: pro_robots The International Conference on Robotics and ...

📺 PRO ROBOTS

👁️ 53K • 👍 954 • 💬 80 • ⏱️ 24:13 • 5d ago

---

**[Unitree R1 | Price from $4,900, Ready Stock](https://www.youtube.com/watch?v=mTMYfVD4zCw)**

Your Smart Robot Companion.

📺 Unitree Robotics

👁️ 326K • 👍 920 • 💬 269 • ⏱️ 0:31 • 20h ago

---

**[Prime Day Robot Vacuum Deals 2026 — What&#39;s Worth It and What to Skip](https://www.youtube.com/watch?v=F9m4Shls9-A)**

2026 Best Amazon Prime Sales on Robot Vacuums and Mop combo See Full Amazon Prime Robot Vacuum sales ...

📺 Just A Dad Approved

👁️ 12K • 👍 224 • 💬 132 • ⏱️ 18:57 • 1d ago

---

**[China&#39;s New AI Robot MOYA Feels Too Real (92% Human)](https://www.youtube.com/watch?v=KdeO-D0tZD0)**

China's new AI robot MOYA just shocked the internet with warm skin, camera eyes, human-like reactions, and a walking claim that ...

📺 AI Revolution

👁️ 59K • 👍 1K • 💬 214 • ⏱️ 13:45 • 3d ago

---

**[Ready, set, row: Humanoid robots partake in Dragon Boat Festival!](https://www.youtube.com/watch?v=IsLt7IdtcNo)**

At China's Dragon Boat Festival, everybody takes place – including the robots. In southwest China's Sichuan Province, ...

📺 CGTN Europe

👁️ 19K • 👍 92 • 💬 13 • ⏱️ 0:49 • 4d ago

---

**[Kawasaki’s New Hydrogen-Powered Robot Horse Will Blow Your Mind!](https://www.youtube.com/watch?v=7AQHBuj30LQ)**

Kawasaki's New Hydrogen-Powered Robot Horse Will Blow Your Mind! #kawasaki #corleo #transport #hydrogen.

📺 Nova Discovery

👁️ 29K • 👍 924 • 💬 92 • ⏱️ 21:28 • 4d ago

---

**[Inside the Warehouse Where Jobs Got DELETED 🤖📦](https://www.youtube.com/watch?v=vJYUmPVph0I)**

Welcome to the future of logistics. This fully automated warehouse in China operates 24/7 in complete darkness. Relying entirely ...

📺 Wealthy Capital

👁️ 128K • 👍 465 • 💬 48 • ⏱️ 0:09 • 1d ago

---

**[Inside look at Amazon&#39;s robotics lab in Massachusetts](https://www.youtube.com/watch?v=r98fdSJ9lfw)**

Look inside Amazon's robotics lab in Massachusetts, where a fleet of robots keeps packages moving swiftly. (AP video: Sydney ...

📺 Associated Press

👁️ 1K • 👍 30 • 💬 10 • ⏱️ 1:23 • 13h ago

---

**[$700K Robot Nanny Knows KUNG FU?! 😱🥋#shorts #funny #robot](https://www.youtube.com/watch?v=zv0PuRKDIWA)**

shorts #anime #fyp #recap #foryou 【Updated daily,welcome to subscribe!】

📺 RECAP Animation

👁️ 54K • 👍 460 • 💬 5 • ⏱️ 1:43 • 16h ago

---

**[This Robot Changed How I Vlog](https://www.youtube.com/watch?v=YxJIHbHXVrs)**

If you want to buy this camera use this link so i get a commission - https://bit.ly/4v2s1cH Music ...

📺 CaseyNeistat

👁️ 514K • 👍 23K • 💬 879 • ⏱️ 8:33 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

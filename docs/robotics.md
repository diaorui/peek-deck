---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-27T23:33:16.292145+00:00'
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

**Last Updated:** October 27, 2026 at 23:33 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[CBR-II update (V3): smoother gait + trying to stand on one leg](https://www.reddit.com/r/robotics/comments/1xf3s92/cbrii_update_v3_smoother_gait_trying_to_stand_on/)**

Hey all, here's a small update on CBR-II, my DIY biped. This is the third iteration. Clip 1 (V3): It walks a lot more confidently now, with much less jitter. The only harsh moment left is when a "stop" comes right after "forward". It plants its front foot and slams it into the floor pretty loudly. Clip 2 (V1): The original version, for comparison. Clip 3 (V3): Attempting to balance on one leg :) In sim it nails this every time. In real life it's far from perfect, but you can definitely tell what it's trying to do. I think this is the end of the road for this project (at least for this year). I was thinking about jumps (and secretly dreaming of a backflip), but the hardware is just too fragile. Today alone it broke a joint three times and snapped a GT2 belt. And not where it bends around the pulley, it just snapped from tension in the middle of a straight run. Thanks to everyone who followed along and gave feedback on the previous posts!

2d ago

---

**[Meet the star of #NVIDIAGTC Berlin ... Microduck.](https://www.reddit.com/r/robotics/comments/1xfagiq/meet_the_star_of_nvidiagtc_berlin_microduck/)**

Microduck from Pollen Robotics. I had the opportunity to meet up with the team here to learn about this, and it's not only a cute little robot, it's one very impressive development tool 👏 "A tiny biped for reinforcement learning" I attended NVIDIA GTC Berlin as a guest of NVIDIA EMEA.

2d ago

---

**[Used an Octopus Pro + 6x TMC2209 to drive a 6-axis 3D-printed robot arm (not a 3D printer!)](https://www.reddit.com/r/robotics/comments/1xfbmjt/used_an_octopus_pro_6x_tmc2209_to_drive_a_6axis/)**

2d ago

---

**[Two months to prepare for humanoid robotics research .. your feedback matters :)](https://www.reddit.com/r/robotics/comments/1xf5mww/two_months_to_prepare_for_humanoid_robotics/)**

I’m starting a master’s in two months, working on vision-guided grasping and end-effector integration for humanoid robots. I have experience in Mechanical Design mainly .. have worked with ROS, and computer vision in college but want a better understanding of humanoids as a complete system. My rough plan is below: start with anatomy and hardware, then arm movement and control, then some simulation. I learn best through practical examples rather than heavy maths. Any recommendations for accessible resources, or changes you’d make to the plan? Also happy to connect with anyone interested in studying together.

2d ago

---

**[Cubic Doggo update: Wouf's first steps](https://www.reddit.com/r/robotics/comments/1xey15u/cubic_doggo_update_woufs_first_steps/)**

Took me a while to work up the nerve to dig into the sloth-speed-servo bug since my last post. Firmware debugging never fails to scare the heck out of me, phew... Turns out the culprit was the latency from reading servo position/velocity/effort values, technically the trademark of smart servos like ST3215. Each read took like 3–5 ms for three servos, and it looks like synchronous read isn't supported yet in the ST3215 C++ SMS_STS library. Does anyone know if it already exists somewhere? For now, feedback reading is disabled on Wouf. With ST3215 servos, although the servo speed is still lower than the Dynamixels used in Doggo, Wouf is walking much faster than expected! And yeah, I think I messed up the turning algorithm again somehow, lol Still, I think this is a good sign that the ST3215-based design can work for a walking robot, and I really like their mechanical sound. Will work on summarizing the build in the next few days. May not have the read function (basically input for reinforcement learning) at the moment though, depending on how difficult it is to develop the sync read firmware. GitHub: https://github.com/SphericalCowww/CubicDoggo_07B

2d ago

---

**[Raspberry Pi Pico Driving a robot arm](https://www.reddit.com/r/robotics/comments/1xfa5qz/raspberry_pi_pico_driving_a_robot_arm/)**

Source code and more info here: https://github.com/AdrianCX/picohive-robotarm Controlled via internal web page (gamepad, keyboard), LLMs, MQTT, with an openGL visualizer

2d ago

---

**[RealMan ECO65 bring-up: a shared MCP backend, MuJoCo twin, and a 5° hardware test](https://www.reddit.com/r/robotics/comments/1xf9oo0/realman_eco65_bringup_a_shared_mcp_backend_mujoco/)**

I’m building a robot lab in a Gaussian-splat reconstruction of my office. Today the RealMan ECO65 (on loan) finally moved: J1 +5° at 5% speed and back. Then I switched its Wi-Fi to client mode, lost access, and discovered I had no Ethernet cable. The software side has one shared backend for Codex and Claude, revision-checked edits, a MuJoCo twin and link/desk collision checks. The MCP motion interface is still simulation-only; the physical move was a separate controller session. The twin is a nominal model, not validated hardware behaviour. EP19 shows the build and the failures. The J1 visual is a labelled replay of the logged command. https://www.youtube.com/watch?v=1ZrYGwZJQto For those running an arm in a home lab: what was the first mismatch you found between your twin and the hardware?

2d ago

---

**[Four-legged robot solves giant Rubik's Cube without using hands](https://www.reddit.com/r/robotics/comments/1xf218z/fourlegged_robot_solves_giant_rubiks_cube_without/)**

ETH Zurich’s ANYmal solved a 10-pound Rubik’s Cube three times using only its feet, taking around eight to nine minutes per attempt. The trick combined computer vision and a traditional cube-solving algorithm with reinforcement learning that taught the robot how to balance, apply force, and correct mistakes. Beyond the fun demo, could “pedipulation” make future robots more useful by letting them open doors, turn valves, or move obstacles without needing hands?

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/four-legged-robot-solves-rubik-cube) • 2d ago

---

**[Day 363 of building Asimov 1. Testing new grippers so it can pick things up and work with them!](https://www.reddit.com/r/robotics/comments/1xeabg7/day_363_of_building_asimov_1_testing_new_grippers/)**

Adding grippers to Asimov 1. The arms have been strong enough for a while. Now it’s time to use them for manipulation! Quick note, if you’re seeing Asimov 1 for the first time, it's a fully open-source humanoid robot built from off-the-shelf parts, so you can build one yourself. https://github.com/menloresearch/asimov-1/

3d ago

---

**[Cycloidal Drive Help](https://www.reddit.com/r/robotics/comments/1xf4aqe/cycloidal_drive_help/)**

Hello everyone, I would like to know some good sites and guides on how to design cycloidal drives for stepper motors (NEMA 17). I have been looking on YouTube and some sites but mostly i didn't learn anything about what is needed from my side and what I need to calculate. I have made few attempts at printing these drives and all of them are off by some millimeters, and they are getting stuck after few turns.

2d ago

---

---

## Google News: "robotics"

**[Robotics Lab Physical Intelligence in Talks for a $20 Billion Valuation](https://www.bloomberg.com/news/articles/2026-10-27/robotics-lab-physical-intelligence-in-talks-for-a-20-billion-valuation)**

Bloomberg.com • 3h ago

---

**[Doctor performs surgery on patient at hospital 35 miles away using robotics - ABC News](https://abcnews.com/GMA/Wellness/doctor-performs-surgery-patient-hospital-35-miles-robotics/story?id=137576330)**

A doctor in Florida performed a medical first on Sunday, using a robotic telesurgery system to perform a surgery at a hospital located 35 miles away.

ABC News - Breaking News, Latest News and Videos • 1d ago

---

**[In the A.I. ‘Robogym,’ Machines Train to Be More Like Humans](https://www.nytimes.com/2026/10/27/business/neura-robotics-germany-china-ai.html)**

The New York Times • 14h ago

---

**[Spacewalk Preps, Robotics Jobs, and Science Duties Fill Tuesday Schedule](https://www.nasa.gov/blogs/spacestation/2026/10/27/spacewalk-preps-robotics-jobs-and-science-duties-fill-tuesday-schedule/)**

Spacewalking tools and a pair of robotics jobs topped Tuesday’s schedule aboard the International Space Station. The Expedition 75 crew members also kept up their scientific duties configuring botany research hardware and setting up advanced Earth observation gear.

NASA (.gov) • 3h ago

---

**[BlackBerry reinvented: CEO sees big opportunities AI-powered robots](https://www.cnbc.com/2026/10/26/blackberry-qnx-physical-ai-robots.html)**

BlackBerry CEO John Giamatteo sees AI-powered robots as a major growth opportunity.

CNBC • 1d ago

---

**[AI factory designer Foundry Robotics makes massive expansion into East Bay](https://www.bizjournals.com/sanfrancisco/news/2026/10/26/foundry-robotics-emeryville-expansion.html)**

The Business Journals • 1d ago

---

**[Ukraine Develops Drone-Carrying Ground Robots to Fight Aerial Threats, With Millions More in Funding Needed](https://www.kyivpost.com/post/88325)**

A UGV would carry interceptor drones to a designated position and launch them to engage enemy aerial targets.

Kyiv Post • 9h ago

---

**[This AI Stock Catapults 58% Amid Robotics Spinoff; Nears Pivot As Earnings Loom](https://www.investors.com/research/ai-stock-zebra-technologies-zbra-earnings/)**

AI stock Zebra Technologies is near a pivot after a 58% gain year-to-date. Third-quarter earnings are due Nov. 3.

Investor's Business Daily • 5h ago

---

**[Companion humanoid robots combine lifelike silicone skin with 39 degrees of freedom](https://interestingengineering.com/ai-robotics/companion-robots-silicone-skin-100-languages)**

Realbotix's Echo humanoid robots start at $11,950, with 39 degrees of freedom, optional on-device vision, and deliveries planned for 2027.

Interesting Engineering • 20h ago

---

**[Sterling Anderson doesn’t think humanoid robots should be building cars](https://www.theverge.com/transportation/1018625/gm-sterling-anderson-interview-robots-ai-autonomous-data-privacy)**

GM is placing a high-stakes bet on AI and centralized software to fight off Tesla and Chinese rivals.

The Verge • 12h ago

---

---

## YouTube Videos: "robotics"

**[This Cute Robot Stole the Show at NVIDIA 🤖🥹#jensenhuang #nvidia #shorts](https://www.youtube.com/watch?v=DBOKSJYANgk)**

Meet Grek, the adorable robot that stole the show on stage with NVIDIA's CEO! From learning to walk in a virtual world to ...

📺 VisionX Lab

👁️ 226K • 👍 6K • 💬 357 • ⏱️ 0:59 • 2d ago

---

**[From Prompt to Walking Robot With NVIDIA RTX Spark](https://www.youtube.com/watch?v=VvJai6HGfyE)**

AI agents on NVIDIA RTX Spark help developers turn ideas into real-world robots. Astra connects FreeCAD, Blender, and ...

📺 NVIDIA

👁️ 260K • 👍 4K • 💬 175 • ⏱️ 2:40 • 6d ago

---

**[NVIDIA Isaac GR00T Reference Humanoid Robot First Look](https://www.youtube.com/watch?v=P_VFdI1Yaq0)**

NVIDIA's Isaac GR00T Reference Humanoid Robot brings advanced artificial intelligence, 75 degrees of freedom, and ...

📺 DPCcars

👁️ 85K • 👍 333 • 💬 80 • ⏱️ 4:22 • 1d ago

---

**[NEW Unitree H2-X Kung Fu Robot Shows Incredible Power](https://www.youtube.com/watch?v=Z3_7Bmf6CqE)**

The NEW Unitree H2-X Kung Fu Legend Guardian humanoid robot is showing incredible strength, martial arts skills, and ...

📺 DPCcars

👁️ 61K • 👍 542 • 💬 166 • ⏱️ 2:30 • 6d ago

---

**[Meet Unitree’s latest security robot: martial arts skills &amp; car-lifting strength](https://www.youtube.com/watch?v=Vez_mlGo7gE)**

📺 ShanghaiEye魔都眼

👁️ 112K • 👍 738 • 💬 329 • ⏱️ 1:01 • 3d ago

---

**[Robots Going Completely Wrong Caught on Camera - Part 3](https://www.youtube.com/watch?v=wcOZklEXzd8)**

Robots going completely wrong caught on camera return in Part 3 with more shocking malfunctions, unexpected behavior, and ...

📺 MostAmazingTop10

👁️ 78K • 👍 546 • 💬 37 • ⏱️ 10:29 • 3d ago

---

**[Jensen Huang&#39;s Tiny Microduck Robots Steal the Show at NVIDIA GTC 2026](https://www.youtube.com/watch?v=Nt6d62vN7CU)**

NVIDIA CEO Jensen Huang introduces 4 tiny Microduck robots during the NVIDIA GTC Berlin 2026 keynote, demonstrating the ...

📺 DPCcars

👁️ 2.1M • 👍 14K • 💬 2K • ⏱️ 4:06 • 6d ago

---

**[Microduck robots go viral at NVIDIA GTC 2026 #robots #microduck #nvidia](https://www.youtube.com/watch?v=tYROJBVwt5M)**

Hugging Face says it's sold more than 4000 of its Microducks since their viral appearance during Jensen Huang's NVIDIA GTC ...

📺 Kalil 4.0

👁️ 111K • 👍 805 • 💬 27 • ⏱️ 0:34 • 4d ago

---

**[AI agent builds itself a robot body, does exactly what experts warned](https://www.youtube.com/watch?v=QRVz697rEx0)**

AI Robot. Is AI dangerous? Can we trust AI? AI Agents and AGI. Use code insideai at https://incogni.com/insideai to get an ...

📺 InsideAI

👁️ 2.0M • 👍 37K • 💬 4K • ⏱️ 15:05 • 2d ago

---

**[China&#39;s Hidden Giant Building Thousands of Humanoid Robot Heads #robotics #robots #tech](https://www.youtube.com/watch?v=naoHeKPg21A)**

China's Joyson Electronics may be the world's largest supplier of humanoid robot heads. Founded in 2004, the Ningbo-based ...

📺 Kalil 4.0

👁️ 172 • 👍 3 • ⏱️ 0:49 • 25m ago

---

---

*Generated by PeekDeck - A glance is all you need*

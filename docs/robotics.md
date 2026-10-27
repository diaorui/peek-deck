---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-27T19:51:58.499627+00:00'
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

**Last Updated:** October 27, 2026 at 19:51 UTC  
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

**[Doctor performs surgery on patient at hospital 35 miles away using robotics - ABC News](https://abcnews.com/GMA/Wellness/doctor-performs-surgery-patient-hospital-35-miles-robotics/story?id=137576330)**

A doctor in Florida performed a medical first on Sunday, using a robotic telesurgery system to perform a surgery at a hospital located 35 miles away.

ABC News - Breaking News, Latest News and Videos • 22h ago

---

**[BlackBerry reinvented: CEO sees big opportunities AI-powered robots](https://www.cnbc.com/2026/10/26/blackberry-qnx-physical-ai-robots.html)**

BlackBerry CEO John Giamatteo sees AI-powered robots as a major growth opportunity.

CNBC • 21h ago

---

**[Toyota takes on Tesla and China in humanoid robot race](https://www.ft.com/content/8bf93407-6b93-4ebb-b54b-f290ebd563e3?syn-25a6b1a6=1)**

Financial Times • 1d ago

---

**[China unveils 13-foot robot that can lift a cow](https://malaysia.news.yahoo.com/china-unveils-13-foot-robot-174401927.html)**

‘Robots should not merely replicate human forms but surpass human physical limits,’ says NeodraDynamics founder

Yahoo • 2h ago

---

**[Sterling Anderson doesn’t think humanoid robots should be building cars](https://www.theverge.com/transportation/1018625/gm-sterling-anderson-interview-robots-ai-autonomous-data-privacy)**

GM is placing a high-stakes bet on AI and centralized software to fight off Tesla and Chinese rivals.

The Verge • 8h ago

---

**[In the A.I. ‘Robogym,’ Machines Train to Be More Like Humans](https://www.nytimes.com/2026/10/27/business/neura-robotics-germany-china-ai.html)**

The New York Times • 10h ago

---

**[Week Begins with Robotics Prep for Spacewalk and Advanced Research](https://www.nasa.gov/blogs/spacestation/2026/10/26/week-begins-with-robotics-prep-for-spacewalk-and-advanced-research/)**

Expedition 75 began the week gearing up for a spacewalk to upgrade the International Space Station’s power generation system. Research into bioprinted blood vessels and relaxation techniques, as well cargo operations rounded out Monday’s schedule.

NASA (.gov) • 1d ago

---

**[An 11-person startup raised $40 million to challenge robotics' data-hungry giants](https://www.businessinsider.com/this-11-person-startup-raised-40-million-train-robots-virtual-worlds-2026-10)**

Machenta, founded by Imperial College London researchers, raised $40 million to build AI that teaches robots new tasks from one demonstration.

Business Insider • 8h ago

---

**[ICE plan to buy robot dogs spurs protest from hundreds of Boston Dynamics employees](https://arstechnica.com/ai/2026/10/boston-dynamics-employees-want-to-block-sale-of-robot-dogs-to-ice/)**

US robotics company stands by ICE deal as more than 300 employees warn of risk.

Ars Technica • 1d ago

---

**[Ukraine Develops Drone-Carrying Ground Robots to Fight Aerial Threats, With Millions More in Funding Needed](https://www.kyivpost.com/post/88325)**

A UGV would carry interceptor drones to a designated position and launch them to engage enemy aerial targets.

Kyiv Post • 6h ago

---

---

## YouTube Videos: "robotics"

**[AI agent builds itself a robot body, does exactly what experts warned](https://www.youtube.com/watch?v=QRVz697rEx0)**

AI Robot. Is AI dangerous? Can we trust AI? AI Agents and AGI. Use code insideai at https://incogni.com/insideai to get an ...

📺 InsideAI

👁️ 1.9M • 👍 36K • 💬 4K • ⏱️ 15:05 • 2d ago

---

**[This Cute Robot Stole the Show at NVIDIA 🤖🥹#jensenhuang #nvidia #shorts](https://www.youtube.com/watch?v=DBOKSJYANgk)**

Meet Grek, the adorable robot that stole the show on stage with NVIDIA's CEO! From learning to walk in a virtual world to ...

📺 VisionX Lab

👁️ 210K • 👍 6K • 💬 342 • ⏱️ 0:59 • 2d ago

---

**[NVIDIA Isaac GR00T Reference Humanoid Robot First Look](https://www.youtube.com/watch?v=P_VFdI1Yaq0)**

NVIDIA's Isaac GR00T Reference Humanoid Robot brings advanced artificial intelligence, 75 degrees of freedom, and ...

📺 DPCcars

👁️ 85K • 👍 329 • 💬 80 • ⏱️ 4:22 • 1d ago

---

**[From Prompt to Walking Robot With NVIDIA RTX Spark](https://www.youtube.com/watch?v=VvJai6HGfyE)**

AI agents on NVIDIA RTX Spark help developers turn ideas into real-world robots. Astra connects FreeCAD, Blender, and ...

📺 NVIDIA

👁️ 258K • 👍 4K • 💬 175 • ⏱️ 2:40 • 6d ago

---

**[China Sets New Guinness World Record as 110 Humanoid Robots Dance in Perfect Synchronization | AI1B](https://www.youtube.com/watch?v=y-Iy1AsIM9I)**

China has set a new Guinness World Record as 110 full-size humanoid robots performed synchronized dance routines in Jinan, ...

📺 DRM News

👁️ 35K • 👍 91 • 💬 47 • ⏱️ 1:21 • 1d ago

---

**[New NVIDIA Isaac GR00T humanoid AI Robot is mind blowing - World Premiere](https://www.youtube.com/watch?v=C3CeYOOYzXw)**

Take a look at the all new NVIDIA Isaac GR00T humanoid AI robot. NVIDIA is accelerating the future of humanoid robotics with ...

📺 REC Anything

👁️ 70K • 👍 412 • 💬 73 • ⏱️ 9:37 • 22h ago

---

**[NEW Unitree H2-X Kung Fu Robot Shows Incredible Power](https://www.youtube.com/watch?v=Z3_7Bmf6CqE)**

The NEW Unitree H2-X Kung Fu Legend Guardian humanoid robot is showing incredible strength, martial arts skills, and ...

📺 DPCcars

👁️ 60K • 👍 541 • 💬 165 • ⏱️ 2:30 • 6d ago

---

**[Robots Going Completely Wrong Caught on Camera - Part 3](https://www.youtube.com/watch?v=wcOZklEXzd8)**

Robots going completely wrong caught on camera return in Part 3 with more shocking malfunctions, unexpected behavior, and ...

📺 MostAmazingTop10

👁️ 77K • 👍 542 • 💬 37 • ⏱️ 10:29 • 3d ago

---

**[Meet Unitree’s latest security robot: martial arts skills &amp; car-lifting strength](https://www.youtube.com/watch?v=Vez_mlGo7gE)**

📺 ShanghaiEye魔都眼

👁️ 111K • 👍 730 • 💬 329 • ⏱️ 1:01 • 3d ago

---

**[Jensen Huang&#39;s Tiny Microduck Robots Steal the Show at NVIDIA GTC 2026](https://www.youtube.com/watch?v=Nt6d62vN7CU)**

NVIDIA CEO Jensen Huang introduces 4 tiny Microduck robots during the NVIDIA GTC Berlin 2026 keynote, demonstrating the ...

📺 DPCcars

👁️ 2.1M • 👍 14K • 💬 2K • ⏱️ 4:06 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

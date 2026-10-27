---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-27T02:18:51.369247+00:00'
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

**Last Updated:** October 27, 2026 at 02:18 UTC  
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

1d ago

---

**[Meet the star of #NVIDIAGTC Berlin ... Microduck.](https://www.reddit.com/r/robotics/comments/1xfagiq/meet_the_star_of_nvidiagtc_berlin_microduck/)**

Microduck from Pollen Robotics. I had the opportunity to meet up with the team here to learn about this, and it's not only a cute little robot, it's one very impressive development tool 👏 "A tiny biped for reinforcement learning" I attended NVIDIA GTC Berlin as a guest of NVIDIA EMEA.

1d ago

---

**[Used an Octopus Pro + 6x TMC2209 to drive a 6-axis 3D-printed robot arm (not a 3D printer!)](https://www.reddit.com/r/robotics/comments/1xfbmjt/used_an_octopus_pro_6x_tmc2209_to_drive_a_6axis/)**

1d ago

---

**[Two months to prepare for humanoid robotics research .. your feedback matters :)](https://www.reddit.com/r/robotics/comments/1xf5mww/two_months_to_prepare_for_humanoid_robotics/)**

I’m starting a master’s in two months, working on vision-guided grasping and end-effector integration for humanoid robots. I have experience in Mechanical Design mainly .. have worked with ROS, and computer vision in college but want a better understanding of humanoids as a complete system. My rough plan is below: start with anatomy and hardware, then arm movement and control, then some simulation. I learn best through practical examples rather than heavy maths. Any recommendations for accessible resources, or changes you’d make to the plan? Also happy to connect with anyone interested in studying together.

1d ago

---

**[Cubic Doggo update: Wouf's first steps](https://www.reddit.com/r/robotics/comments/1xey15u/cubic_doggo_update_woufs_first_steps/)**

Took me a while to work up the nerve to dig into the sloth-speed-servo bug since my last post. Firmware debugging never fails to scare the heck out of me, phew... Turns out the culprit was the latency from reading servo position/velocity/effort values, technically the trademark of smart servos like ST3215. Each read took like 3–5 ms for three servos, and it looks like synchronous read isn't supported yet in the ST3215 C++ SMS_STS library. Does anyone know if it already exists somewhere? For now, feedback reading is disabled on Wouf. With ST3215 servos, although the servo speed is still lower than the Dynamixels used in Doggo, Wouf is walking much faster than expected! And yeah, I think I messed up the turning algorithm again somehow, lol Still, I think this is a good sign that the ST3215-based design can work for a walking robot, and I really like their mechanical sound. Will work on summarizing the build in the next few days. May not have the read function (basically input for reinforcement learning) at the moment though, depending on how difficult it is to develop the sync read firmware. GitHub: https://github.com/SphericalCowww/CubicDoggo_07B

1d ago

---

**[Raspberry Pi Pico Driving a robot arm](https://www.reddit.com/r/robotics/comments/1xfa5qz/raspberry_pi_pico_driving_a_robot_arm/)**

Source code and more info here: https://github.com/AdrianCX/picohive-robotarm Controlled via internal web page (gamepad, keyboard), LLMs, MQTT, with an openGL visualizer

1d ago

---

**[RealMan ECO65 bring-up: a shared MCP backend, MuJoCo twin, and a 5° hardware test](https://www.reddit.com/r/robotics/comments/1xf9oo0/realman_eco65_bringup_a_shared_mcp_backend_mujoco/)**

I’m building a robot lab in a Gaussian-splat reconstruction of my office. Today the RealMan ECO65 (on loan) finally moved: J1 +5° at 5% speed and back. Then I switched its Wi-Fi to client mode, lost access, and discovered I had no Ethernet cable. The software side has one shared backend for Codex and Claude, revision-checked edits, a MuJoCo twin and link/desk collision checks. The MCP motion interface is still simulation-only; the physical move was a separate controller session. The twin is a nominal model, not validated hardware behaviour. EP19 shows the build and the failures. The J1 visual is a labelled replay of the logged command. https://www.youtube.com/watch?v=1ZrYGwZJQto For those running an arm in a home lab: what was the first mismatch you found between your twin and the hardware?

1d ago

---

**[Four-legged robot solves giant Rubik's Cube without using hands](https://www.reddit.com/r/robotics/comments/1xf218z/fourlegged_robot_solves_giant_rubiks_cube_without/)**

ETH Zurich’s ANYmal solved a 10-pound Rubik’s Cube three times using only its feet, taking around eight to nine minutes per attempt. The trick combined computer vision and a traditional cube-solving algorithm with reinforcement learning that taught the robot how to balance, apply force, and correct mistakes. Beyond the fun demo, could “pedipulation” make future robots more useful by letting them open doors, turn valves, or move obstacles without needing hands?

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/four-legged-robot-solves-rubik-cube) • 1d ago

---

**[Day 363 of building Asimov 1. Testing new grippers so it can pick things up and work with them!](https://www.reddit.com/r/robotics/comments/1xeabg7/day_363_of_building_asimov_1_testing_new_grippers/)**

Adding grippers to Asimov 1. The arms have been strong enough for a while. Now it’s time to use them for manipulation! Quick note, if you’re seeing Asimov 1 for the first time, it's a fully open-source humanoid robot built from off-the-shelf parts, so you can build one yourself. https://github.com/menloresearch/asimov-1/

2d ago

---

**[Cycloidal Drive Help](https://www.reddit.com/r/robotics/comments/1xf4aqe/cycloidal_drive_help/)**

Hello everyone, I would like to know some good sites and guides on how to design cycloidal drives for stepper motors (NEMA 17). I have been looking on YouTube and some sites but mostly i didn't learn anything about what is needed from my side and what I need to calculate. I have made few attempts at printing these drives and all of them are off by some millimeters, and they are getting stuck after few turns.

1d ago

---

---

## Google News: "robotics"

**[Doctor performs surgery on patient at hospital 35 miles away using robotics - ABC News](https://abcnews.com/GMA/Wellness/doctor-performs-surgery-patient-hospital-35-miles-robotics/story?id=137576330)**

A doctor in Florida performed a medical first on Sunday, using a robotic telesurgery system to perform a surgery at a hospital located 35 miles away.

ABC News - Breaking News, Latest News and Videos • 4h ago

---

**[Using AI Agents to Teach Robots Like Microduck to Walk in Simulation | NVIDIA Technical Blog](https://developer.nvidia.com/blog/using-ai-agents-to-teach-robots-like-microduck-to-walk-in-simulation/)**

Teaching a robot to navigate an obstacle course requires more than a walking policy. It must perceive its surroundings, maintain balance, and adjust its actions when obstacles block the path ahead.

NVIDIA Developer • 3d ago

---

**[Emerson-Hubbard robotics team granted money to compete](https://www.yahoo.com/news/articles/emerson-hubbard-robotics-team-granted-004652004.html)**

For the last three years, Emerson-Hubbard High School students have been getting hands-on experience building robots as part of their robotics programs.

Yahoo • 1h ago

---

**[This startup’s self-driving excavators help dig up $600M in new funding](https://techcrunch.com/2026/10/26/this-startups-self-driving-excavators-help-dig-up-600m-in-new-funding/)**

Bedrock Robotics, which is now valued at $4.1 billion, is particularly focused on autonomous excavators, in part because of a growing shortage of skilled operators.

TechCrunch • 8h ago

---

**[BlackBerry reinvented: CEO sees big opportunities AI-powered robots](https://www.cnbc.com/2026/10/26/blackberry-qnx-physical-ai-robots.html)**

BlackBerry CEO John Giamatteo sees AI-powered robots as a major growth opportunity.

CNBC • 3h ago

---

**[Week Begins with Robotics Prep for Spacewalk and Advanced Research](https://www.nasa.gov/blogs/spacestation/2026/10/26/week-begins-with-robotics-prep-for-spacewalk-and-advanced-research/)**

Expedition 75 began the week gearing up for a spacewalk to upgrade the International Space Station’s power generation system. Research into bioprinted blood vessels and relaxation techniques, as well cargo operations rounded out Monday’s schedule.

NASA (.gov) • 10h ago

---

**[Autonomous Construction Firm Bedrock Hits $4.1 Billion Valuation](https://www.bloomberg.com/news/articles/2026-10-26/autonomous-construction-firm-bedrock-hits-4-1-billion-valuation)**

Bloomberg.com • 14h ago

---

**[Move Over, Tesla: This Robotics Stock Is the Better Buy](https://www.fool.com/investing/2026/10/26/move-over-tesla-this-robotics-stock-is-better/)**

Tesla is looking to start manufacturing its Optimus robots, but this industrial giant has been helping factories automate for decades.

The Motley Fool • 6h ago

---

**[Are Delivery Robots Scanning You Into a Database Scarier Than Flock?](https://futurism.com/robots-and-machines/delivery-robots-database-flock)**

A pair of lawsuits from Chicago residents allege that delivery robots recorded and stored people's data without their consent.

Futurism • 1d ago

---

**[AI factory designer Foundry Robotics makes massive expansion into East Bay](https://www.bizjournals.com/sanfrancisco/news/2026/10/26/foundry-robotics-emeryville-expansion.html)**

The Business Journals • 4h ago

---

---

## YouTube Videos: "robotics"

**[This Cute Robot Stole the Show at NVIDIA 🤖🥹#jensenhuang #nvidia #shorts](https://www.youtube.com/watch?v=DBOKSJYANgk)**

Meet Grek, the adorable robot that stole the show on stage with NVIDIA's CEO! From learning to walk in a virtual world to ...

📺 VisionX Lab

👁️ 116K • 👍 3K • 💬 236 • ⏱️ 0:59 • 1d ago

---

**[NVIDIA Isaac GR00T Reference Humanoid Robot First Look](https://www.youtube.com/watch?v=P_VFdI1Yaq0)**

NVIDIA's Isaac GR00T Reference Humanoid Robot brings advanced artificial intelligence, 75 degrees of freedom, and ...

📺 DPCcars

👁️ 77K • 👍 298 • 💬 70 • ⏱️ 4:22 • 11h ago

---

**[AI agent builds itself a robot body, does exactly what experts warned](https://www.youtube.com/watch?v=QRVz697rEx0)**

AI Robot. Is AI dangerous? Can we trust AI? AI Agents and AGI. Use code insideai at https://incogni.com/insideai to get an ...

📺 InsideAI

👁️ 1.7M • 👍 32K • 💬 4K • ⏱️ 15:05 • 1d ago

---

**[NEW Unitree H2-X Kung Fu Robot Shows Incredible Power](https://www.youtube.com/watch?v=Z3_7Bmf6CqE)**

The NEW Unitree H2-X Kung Fu Legend Guardian humanoid robot is showing incredible strength, martial arts skills, and ...

📺 DPCcars

👁️ 59K • 👍 530 • 💬 162 • ⏱️ 2:30 • 5d ago

---

**[China&#39;s New Giant AI Robot Is Absolutely Terrifying (Stronger Than 10 Men)](https://www.youtube.com/watch?v=vD4YWPo9a-I)**

China's new giant AI robot Neo1 is absolutely terrifying. Standing 13 feet tall and weighing 1.2 tons, this massive humanoid from ...

📺 MACHINEKIND

👁️ 131K • 👍 1K • 💬 117 • ⏱️ 13:57 • 6d ago

---

**[Jensen Huang&#39;s Tiny Microduck Robots Steal the Show at NVIDIA GTC 2026](https://www.youtube.com/watch?v=Nt6d62vN7CU)**

NVIDIA CEO Jensen Huang introduces 4 tiny Microduck robots during the NVIDIA GTC Berlin 2026 keynote, demonstrating the ...

📺 DPCcars

👁️ 2.1M • 👍 13K • 💬 2K • ⏱️ 4:06 • 5d ago

---

**[Why all robots should be crabs](https://www.youtube.com/watch?v=eUGL5QYxzE0)**

Thank you to Quince for sponsoring this video! Elevate your wardrobe essentials with Quince. Download the Quince app for ...

📺 Xyla Foxlin

👁️ 213K • 👍 6K • 💬 447 • ⏱️ 14:36 • 2d ago

---

**[DIY AI Lockpicking Robot: ESP32 + Claude AI Opens Any Lock!](https://www.youtube.com/watch?v=o4AUKGdScNI)**

I built an ESP32 and AI-powered lockpicking machine capable of opening locks automatically. The entire frame and mechanics ...

📺 Dr.Kun Dániel

👁️ 126K • 👍 1K • 💬 177 • ⏱️ 3:28 • 2d ago

---

**[Are robots taking over? I ranked every humanoid robot - only one gets SSS](https://www.youtube.com/watch?v=Eta625JJKqc)**

Robots just learned kung fu. I ranked the best humanoid robots on the market, with real footage of every one. Only one gets SSS.

📺 AI BROS

👁️ 21K • 👍 691 • 💬 73 • ⏱️ 2:54 • 2d ago

---

**[Nvidia Microduck AI Robots are mind blowing - World Premiere and First Look](https://www.youtube.com/watch?v=ac6pspFbPsI)**

Have a look at the new Nvidia Microduck AI robots. NVIDIA CEO Jensen Huang was joined onstage at GTC Berlin 2026 by four ...

📺 REC Anything

👁️ 1.7M • 👍 11K • 💬 1K • ⏱️ 8:29 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

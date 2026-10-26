---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-26T05:48:57.861848+00:00'
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

**Last Updated:** October 26, 2026 at 05:48 UTC  
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

15h ago

---

**[Meet the star of #NVIDIAGTC Berlin ... Microduck.](https://www.reddit.com/r/robotics/comments/1xfagiq/meet_the_star_of_nvidiagtc_berlin_microduck/)**

Microduck from Pollen Robotics. I had the opportunity to meet up with the team here to learn about this, and it's not only a cute little robot, it's one very impressive development tool 👏 "A tiny biped for reinforcement learning" I attended NVIDIA GTC Berlin as a guest of NVIDIA EMEA.

10h ago

---

**[Used an Octopus Pro + 6x TMC2209 to drive a 6-axis 3D-printed robot arm (not a 3D printer!)](https://www.reddit.com/r/robotics/comments/1xfbmjt/used_an_octopus_pro_6x_tmc2209_to_drive_a_6axis/)**

10h ago

---

**[Two months to prepare for humanoid robotics research .. your feedback matters :)](https://www.reddit.com/r/robotics/comments/1xf5mww/two_months_to_prepare_for_humanoid_robotics/)**

I’m starting a master’s in two months, working on vision-guided grasping and end-effector integration for humanoid robots. I have experience in Mechanical Design mainly .. have worked with ROS, and computer vision in college but want a better understanding of humanoids as a complete system. My rough plan is below: start with anatomy and hardware, then arm movement and control, then some simulation. I learn best through practical examples rather than heavy maths. Any recommendations for accessible resources, or changes you’d make to the plan? Also happy to connect with anyone interested in studying together.

14h ago

---

**[Cubic Doggo update: Wouf's first steps](https://www.reddit.com/r/robotics/comments/1xey15u/cubic_doggo_update_woufs_first_steps/)**

Took me a while to work up the nerve to dig into the sloth-speed-servo bug since my last post. Firmware debugging never fails to scare the heck out of me, phew... Turns out the culprit was the latency from reading servo position/velocity/effort values, technically the trademark of smart servos like ST3215. Each read took like 3–5 ms for three servos, and it looks like synchronous read isn't supported yet in the ST3215 C++ SMS_STS library. Does anyone know if it already exists somewhere? For now, feedback reading is disabled on Wouf. With ST3215 servos, although the servo speed is still lower than the Dynamixels used in Doggo, Wouf is walking much faster than expected! And yeah, I think I messed up the turning algorithm again somehow, lol Still, I think this is a good sign that the ST3215-based design can work for a walking robot, and I really like their mechanical sound. Will work on summarizing the build in the next few days. May not have the read function (basically input for reinforcement learning) at the moment though, depending on how difficult it is to develop the sync read firmware. GitHub: https://github.com/SphericalCowww/CubicDoggo_07B

20h ago

---

**[Raspberry Pi Pico Driving a robot arm](https://www.reddit.com/r/robotics/comments/1xfa5qz/raspberry_pi_pico_driving_a_robot_arm/)**

Source code and more info here: https://github.com/AdrianCX/picohive-robotarm Controlled via internal web page (gamepad, keyboard), LLMs, MQTT, with an openGL visualizer

11h ago

---

**[RealMan ECO65 bring-up: a shared MCP backend, MuJoCo twin, and a 5° hardware test](https://www.reddit.com/r/robotics/comments/1xf9oo0/realman_eco65_bringup_a_shared_mcp_backend_mujoco/)**

I’m building a robot lab in a Gaussian-splat reconstruction of my office. Today the RealMan ECO65 (on loan) finally moved: J1 +5° at 5% speed and back. Then I switched its Wi-Fi to client mode, lost access, and discovered I had no Ethernet cable. The software side has one shared backend for Codex and Claude, revision-checked edits, a MuJoCo twin and link/desk collision checks. The MCP motion interface is still simulation-only; the physical move was a separate controller session. The twin is a nominal model, not validated hardware behaviour. EP19 shows the build and the failures. The J1 visual is a labelled replay of the logged command. https://www.youtube.com/watch?v=1ZrYGwZJQto For those running an arm in a home lab: what was the first mismatch you found between your twin and the hardware?

11h ago

---

**[Four-legged robot solves giant Rubik's Cube without using hands](https://www.reddit.com/r/robotics/comments/1xf218z/fourlegged_robot_solves_giant_rubiks_cube_without/)**

ETH Zurich’s ANYmal solved a 10-pound Rubik’s Cube three times using only its feet, taking around eight to nine minutes per attempt. The trick combined computer vision and a traditional cube-solving algorithm with reinforcement learning that taught the robot how to balance, apply force, and correct mistakes. Beyond the fun demo, could “pedipulation” make future robots more useful by letting them open doors, turn valves, or move obstacles without needing hands?

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/four-legged-robot-solves-rubik-cube) • 16h ago

---

**[Day 363 of building Asimov 1. Testing new grippers so it can pick things up and work with them!](https://www.reddit.com/r/robotics/comments/1xeabg7/day_363_of_building_asimov_1_testing_new_grippers/)**

Adding grippers to Asimov 1. The arms have been strong enough for a while. Now it’s time to use them for manipulation! Quick note, if you’re seeing Asimov 1 for the first time, it's a fully open-source humanoid robot built from off-the-shelf parts, so you can build one yourself. https://github.com/menloresearch/asimov-1/

1d ago

---

**[Cycloidal Drive Help](https://www.reddit.com/r/robotics/comments/1xf4aqe/cycloidal_drive_help/)**

Hello everyone, I would like to know some good sites and guides on how to design cycloidal drives for stepper motors (NEMA 17). I have been looking on YouTube and some sites but mostly i didn't learn anything about what is needed from my side and what I need to calculate. I have made few attempts at printing these drives and all of them are off by some millimeters, and they are getting stuck after few turns.

14h ago

---

---

## Google News: "robotics"

**[110 humanoid robots set Guinness world record for synchronized dancing in China, eyeing large-scale deployment](https://www.globaltimes.cn/page/202610/1372888.shtml)**

China's humanoid robot industry is moving from single-machine demonstration toward large-scale deployment, as 110 humanoid robots set a Guinness World Records title for the most humanoid robots dancing simultaneously in Jinan, East China's Shandong Province, on October 24.

Global Times • 1d ago

---

**[Toyota takes on Tesla and China in humanoid robot race](https://www.ft.com/content/8bf93407-6b93-4ebb-b54b-f290ebd563e3?syn-25a6b1a6=1)**

Financial Times • 8h ago

---

**[Agile ONE SN Humanoid Robot Bundles Nvidia’s Robotics Stack](https://www.techrepublic.com/article/news-nvidia-agile-one-sn-humanoid-robot/)**

Nvidia and Agile Robots unveiled Agile ONE SN, a compact humanoid with AI training tools. Explore its features, specifications, and planned 2027 release.

TechRepublic • 2d ago

---

**['The beginning of The Matrix': Unitree is developing an AI system that will let humanoid robots self-improve — and Tesla should be worried](https://tech.yahoo.com/ai/meta-ai/articles/beginning-matrix-unitree-developing-ai-110000127.html)**

We've got robotics updates from Unitree, Tesla, and Figure, as the companies announce their latest progress.

Yahoo Tech • 1d ago

---

**[Unitree Founder Now Expects Robots Breakthrough as Soon as 2028](https://www.bloomberg.com/news/articles/2026-10-23/unitree-founder-now-expects-robots-breakthrough-as-soon-as-2028)**

Bloomberg.com • 2d ago

---

**[Figure AI's Robot Endures 13-Day Walk, 200-Hour Sorting Test](https://www.chosun.com/english/industry-en/2026/10/26/PWEXG3OIKVAM7N2O7YP6O6T5II/)**

Figure AIs Robot Endures 13-Day Walk, 200-Hour Sorting Test Extreme tests identify faults, prove reliability for factories and logistics customers

조선일보 • 16m ago

---

**[Intel gets waiver after worries fuzzy US ban on foreign-made robots may hit fabs](https://arstechnica.com/ai/2026/10/intel-gets-waiver-after-worries-fuzzy-us-ban-on-foreign-made-robots-may-hit-fabs/)**

Company says foreign-made robotic vehicles are crucial to US chip production.

Ars Technica • 2d ago

---

**[Using AI Agents to Teach Robots Like Microduck to Walk in Simulation | NVIDIA Technical Blog](https://developer.nvidia.com/blog/using-ai-agents-to-teach-robots-like-microduck-to-walk-in-simulation/)**

Teaching a robot to navigate an obstacle course requires more than a walking policy. It must perceive its surroundings, maintain balance, and adjust its actions when obstacles block the path ahead.

NVIDIA Developer • 2d ago

---

**[Finger-controlled robo beetle sports artificial muscles & two-way feedback](https://newatlas.com/robotics/beetlebot-robotic-beetle/)**

Insects have long been a source of inspiration for robotics engineers. They are small, agile, and can squeeze into spaces where people can’t. Such robots are very useful for space exploration, inspecting industrial equipment, and even carrying out search-and-rescue operations. For certain purposes,…

New Atlas • 20h ago

---

**[Hottest toy for Christmas? Nvidia CEO plays with adorable Microduck robots, 20,000 sell](https://techcrunch.com/2026/10/23/hottest-toy-for-christmas-nvidia-ceo-plays-with-adorable-microduck-robots-20000-sell/)**

The robots, stomping their little feet and making tiny R2-D2 noises, sat, fell down dead for a "nap," and summersaulted on voice command.

TechCrunch • 2d ago

---

---

## YouTube Videos: "robotics"

**[This Cute Robot Stole the Show at NVIDIA 🤖🥹#jensenhuang #nvidia #shorts](https://www.youtube.com/watch?v=DBOKSJYANgk)**

Meet Grek, the adorable robot that stole the show on stage with NVIDIA's CEO! From learning to walk in a virtual world to ...

📺 VisionX Lab

👁️ 30K • 👍 1K • 💬 96 • ⏱️ 0:59 • 11h ago

---

**[Elon Musk&#39;s Humanoid Robot Bodyguard 👀 #elonmusk #shorts](https://www.youtube.com/watch?v=svFO2f6mXc4)**

Subscribe to VisionX Lab for more fascinating moments from Elon Musk, cutting-edge technology, AI, and the future. Disclaimer: ...

📺 VisionX Lab

👁️ 63K • 👍 1K • 💬 129 • ⏱️ 0:11 • 10h ago

---

**[China&#39;s New Giant AI Robot Is Absolutely Terrifying (Stronger Than 10 Men)](https://www.youtube.com/watch?v=vD4YWPo9a-I)**

China's new giant AI robot Neo1 is absolutely terrifying. Standing 13 feet tall and weighing 1.2 tons, this massive humanoid from ...

📺 MACHINEKIND

👁️ 116K • 👍 1K • 💬 103 • ⏱️ 13:57 • 5d ago

---

**[Nvidia Microduck AI Robots are mind blowing - World Premiere and First Look](https://www.youtube.com/watch?v=ac6pspFbPsI)**

Have a look at the new Nvidia Microduck AI robots. NVIDIA CEO Jensen Huang was joined onstage at GTC Berlin 2026 by four ...

📺 REC Anything

👁️ 1.5M • 👍 10K • 💬 1K • ⏱️ 8:29 • 3d ago

---

**[Microducks Stole NVIDIA’s Show](https://www.youtube.com/watch?v=cgOZPijdl7w)**

Four tiny Microducks walked onto Jensen Huang's GTC Berlin stage, followed his commands... mostly Microduck is a ...

📺 Techy or Not

👁️ 13K • 👍 366 • 💬 3 • ⏱️ 1:46 • 23h ago

---

**[Why all robots should be crabs](https://www.youtube.com/watch?v=eUGL5QYxzE0)**

Thank you to Quince for sponsoring this video! Elevate your wardrobe essentials with Quince. Download the Quince app for ...

📺 Xyla Foxlin

👁️ 169K • 👍 6K • 💬 398 • ⏱️ 14:36 • 1d ago

---

**[This robot is India&#39;s answer to Boston Dynamics](https://www.youtube.com/watch?v=HgmaxBWkk5w)**

xTerra Robotics is quickly establishing itself as one of India's most advanced robotics startups, transitioning from an academic ...

📺 RuntimeBRT

👁️ 369K • 👍 14K • 💬 388 • ⏱️ 2:55 • 6d ago

---

**[Inside the Robot Data Factory: Mecka&#39;s Josh Gao on Sensorizing Humans to Train Robots](https://www.youtube.com/watch?v=0idrTKCDhuE)**

Robotics never got the internet's gift of free training data, so someone has to manufacture it. Josh Gao, founder and CEO of Mecka ...

📺 Sequoia Capital

👁️ 18K • 👍 113 • 💬 11 • ⏱️ 45:12 • 5d ago

---

**[Jensen Huang&#39;s Tiny Microduck Robots Steal the Show at NVIDIA GTC 2026](https://www.youtube.com/watch?v=Nt6d62vN7CU)**

NVIDIA CEO Jensen Huang introduces 4 tiny Microduck robots during the NVIDIA GTC Berlin 2026 keynote, demonstrating the ...

📺 DPCcars

👁️ 1.9M • 👍 13K • 💬 2K • ⏱️ 4:06 • 4d ago

---

**[NEW Unitree H2-X Kung Fu Robot Shows Incredible Power](https://www.youtube.com/watch?v=Z3_7Bmf6CqE)**

The NEW Unitree H2-X Kung Fu Legend Guardian humanoid robot is showing incredible strength, martial arts skills, and ...

📺 DPCcars

👁️ 56K • 👍 521 • 💬 174 • ⏱️ 2:30 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

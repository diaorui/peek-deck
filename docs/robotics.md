---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-28T17:01:02.192666+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- news
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** October 28, 2026 at 17:01 UTC  
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

3d ago

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

3d ago

---

**[Cubic Doggo update: Wouf's first steps](https://www.reddit.com/r/robotics/comments/1xey15u/cubic_doggo_update_woufs_first_steps/)**

Took me a while to work up the nerve to dig into the sloth-speed-servo bug since my last post. Firmware debugging never fails to scare the heck out of me, phew... Turns out the culprit was the latency from reading servo position/velocity/effort values, technically the trademark of smart servos like ST3215. Each read took like 3–5 ms for three servos, and it looks like synchronous read isn't supported yet in the ST3215 C++ SMS_STS library. Does anyone know if it already exists somewhere? For now, feedback reading is disabled on Wouf. With ST3215 servos, although the servo speed is still lower than the Dynamixels used in Doggo, Wouf is walking much faster than expected! And yeah, I think I messed up the turning algorithm again somehow, lol Still, I think this is a good sign that the ST3215-based design can work for a walking robot, and I really like their mechanical sound. Will work on summarizing the build in the next few days. May not have the read function (basically input for reinforcement learning) at the moment though, depending on how difficult it is to develop the sync read firmware. GitHub: https://github.com/SphericalCowww/CubicDoggo_07B

3d ago

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

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/four-legged-robot-solves-rubik-cube) • 3d ago

---

**[Day 363 of building Asimov 1. Testing new grippers so it can pick things up and work with them!](https://www.reddit.com/r/robotics/comments/1xeabg7/day_363_of_building_asimov_1_testing_new_grippers/)**

Adding grippers to Asimov 1. The arms have been strong enough for a while. Now it’s time to use them for manipulation! Quick note, if you’re seeing Asimov 1 for the first time, it's a fully open-source humanoid robot built from off-the-shelf parts, so you can build one yourself. https://github.com/menloresearch/asimov-1/

4d ago

---

**[Cycloidal Drive Help](https://www.reddit.com/r/robotics/comments/1xf4aqe/cycloidal_drive_help/)**

Hello everyone, I would like to know some good sites and guides on how to design cycloidal drives for stepper motors (NEMA 17). I have been looking on YouTube and some sites but mostly i didn't learn anything about what is needed from my side and what I need to calculate. I have made few attempts at printing these drives and all of them are off by some millimeters, and they are getting stuck after few turns.

3d ago

---

---

## Google News: "robotics"

**[Robotics Lab Physical Intelligence in Talks for a $20 Billion Valuation](https://www.bloomberg.com/news/articles/2026-10-27/robotics-lab-physical-intelligence-in-talks-for-a-20-billion-valuation)**

Bloomberg.com • 21h ago

---

**[Doctor performs surgery on patient at hospital 35 miles away using robotics - ABC News](https://abcnews.com/GMA/Wellness/doctor-performs-surgery-patient-hospital-35-miles-robotics/story?id=137576330)**

A doctor in Florida performed a medical first on Sunday, using a robotic telesurgery system to perform a surgery at a hospital located 35 miles away.

ABC News - Breaking News, Latest News and Videos • 1d ago

---

**[Foundry Robotics Raises $100 Million Series A to Build America’s First Autonomous Factory for Assembly](https://www.businesswire.com/news/home/20261028508802/en/Foundry-Robotics-Raises-%24100-Million-Series-A-to-Build-Americas-First-Autonomous-Factory-for-Assembly)**

Business Wire • 2h ago

---

**[Amazon warehouse workers tell us what they think about their new robot coworkers](https://www.businessinsider.com/amazon-robot-warehouse-where-jobs-changing-ai-robotics-workers-2026-9)**

Inside Amazon's robotic warehouse in Tracy, California, workers explain how automation is transforming their jobs.

Business Insider • 7h ago

---

**[Unitree's quarterly revenue surges 70% in test for China's robotics sector](https://www.reuters.com/world/asia-pacific/unitrees-q3-profit-down-174-on-year-test-chinas-robotics-sector-2026-10-28/)**

Reuters • 4h ago

---

**[Spacewalk Preps, Robotics Jobs, and Science Duties Fill Tuesday Schedule](https://www.nasa.gov/blogs/spacestation/2026/10/27/spacewalk-preps-robotics-jobs-and-science-duties-fill-tuesday-schedule/)**

Spacewalking tools and a pair of robotics jobs topped Tuesday’s schedule aboard the International Space Station. The Expedition 75 crew members also kept up their scientific duties configuring botany research hardware and setting up advanced Earth observation gear.

NASA (.gov) • 21h ago

---

**[Could humanoid robots replace soldiers on the battlefield?](https://theconversation.com/could-humanoid-robots-replace-soldiers-on-the-battlefield-292913)**

Militaries around the world are testing the newest generation of machines.

The Conversation • 1d ago

---

**[China unveils 13-foot robot that can lift a cow](https://uk.finance.yahoo.com/news/china-unveils-13-foot-robot-174401927.html)**

‘Robots should not merely replicate human forms but surpass human physical limits,’ says NeodraDynamics founder

Yahoo Finance UK • 23h ago

---

**[ByteDance goes on a hiring spree to move its robots from lab to factory floor](https://www.scmp.com/tech/big-tech/article/3372295/bytedance-accelerates-robotics-commercialisation-new-recruitment-drive)**

South China Morning Post • 14h ago

---

**[Japan experiments with autonomous AI chainsaw-wielding robots — video shows rail truck-mounted metal humanoid cutting down tree branches](https://www.tomshardware.com/tech-industry/robotics/japan-experiments-with-autonomous-ai-chainsaw-wielding-robots-video-shows-rail-truck-mounted-metal-humanoid-cutting-down-tree-branches)**

The frightening-looking mech in the demo still has a human operator, for now.

Tom's Hardware • 7h ago

---

---

## YouTube Videos: "robotics"

**[This Cute Robot Stole the Show at NVIDIA 🤖🥹#jensenhuang #nvidia #shorts](https://www.youtube.com/watch?v=DBOKSJYANgk)**

Meet Grek, the adorable robot that stole the show on stage with NVIDIA's CEO! From learning to walk in a virtual world to ...

📺 VisionX Lab

👁️ 377K • 👍 10K • 💬 502 • ⏱️ 0:59 • 2d ago

---

**[OpenAI&#39;s First AI Robot Is Finally Happening (ChatGPT Gets a Body)](https://www.youtube.com/watch?v=BhdPuzza7i0)**

OpenAI is officially building its first humanoid robot, and Sam Altman has confirmed a major demonstration planned for 2027.

📺 MACHINEKIND

👁️ 20K • 👍 353 • 💬 31 • ⏱️ 13:33 • 17h ago

---

**[AI agent builds itself a robot body, does exactly what experts warned](https://www.youtube.com/watch?v=QRVz697rEx0)**

AI Robot. Is AI dangerous? Can we trust AI? AI Agents and AGI. Use code insideai at https://incogni.com/insideai to get an ...

📺 InsideAI

👁️ 2.2M • 👍 40K • 💬 4K • ⏱️ 15:05 • 2d ago

---

**[Toyota’s 400,000-Robot Plan: Is It Taking on Tesla and China? | Firstpost Explains](https://www.youtube.com/watch?v=Egf4fBLfRk4)**

In this video, Firstpost explains Toyota's ambitious plan to enter the humanoid robot race against Tesla and Chinese ...

📺 Firstpost

👁️ 5K • 👍 16 • 💬 2 • ⏱️ 7:48 • 5h ago

---

**[Tesla Leaked Optimus 3 At Earnings Call | It&#39;s As Good As They Say](https://www.youtube.com/watch?v=gS1iOU_JnkA)**

Tesla has started production of Optimus on a line in Fremont, and on their third quarter earnings call Elon Musk said "there is no ...

📺 Ryan Shaw

👁️ 115K • 👍 2K • 💬 166 • ⏱️ 37:43 • 4d ago

---

**[Elon Musk&#39;s Humanoid Robot Bodyguard 👀 #elonmusk #shorts](https://www.youtube.com/watch?v=svFO2f6mXc4)**

Subscribe to VisionX Lab for more fascinating moments from Elon Musk, cutting-edge technology, AI, and the future. Disclaimer: ...

📺 VisionX Lab

👁️ 254K • 👍 3K • 💬 295 • ⏱️ 0:11 • 2d ago

---

**[Robot Dog Entered the Lion&#39;s Territory... Big Mistake?!](https://www.youtube.com/watch?v=eZQo7KqJy8c)**

What happens when a robot dog walks into the world of lions? In today's episode of Wild Clash, the mightiest and most curious ...

📺 Wild Clash

👁️ 1.1M • 👍 8K • 💬 603 • ⏱️ 8:40 • 4d ago

---

**[New Unitree H2X AI Robot Shocks The World With Superhuman Strength](https://www.youtube.com/watch?v=Uz5ktECdg6M)**

Unitree just dropped the H2X AI robot, and its terrifying strength is shocking the world. This humanoid bodyguard fights knife ...

📺 MACHINEKIND

👁️ 19K • 👍 220 • 💬 34 • ⏱️ 13:25 • 4d ago

---

**[New NVIDIA Isaac GR00T humanoid AI Robot is mind blowing - World Premiere](https://www.youtube.com/watch?v=C3CeYOOYzXw)**

Take a look at the all new NVIDIA Isaac GR00T humanoid AI robot. NVIDIA is accelerating the future of humanoid robotics with ...

📺 REC Anything

👁️ 118K • 👍 740 • 💬 103 • ⏱️ 9:37 • 1d ago

---

**[Jensen Huang&#39;s Tiny Microduck Robots Steal the Show at NVIDIA GTC 2026](https://www.youtube.com/watch?v=Nt6d62vN7CU)**

NVIDIA CEO Jensen Huang introduces 4 tiny Microduck robots during the NVIDIA GTC Berlin 2026 keynote, demonstrating the ...

📺 DPCcars

👁️ 2.2M • 👍 14K • 💬 2K • ⏱️ 4:06 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

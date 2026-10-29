---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-29T01:36:00.575056+00:00'
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

**Last Updated:** October 29, 2026 at 01:36 UTC  
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

3d ago

---

**[Used an Octopus Pro + 6x TMC2209 to drive a 6-axis 3D-printed robot arm (not a 3D printer!)](https://www.reddit.com/r/robotics/comments/1xfbmjt/used_an_octopus_pro_6x_tmc2209_to_drive_a_6axis/)**

3d ago

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

3d ago

---

**[RealMan ECO65 bring-up: a shared MCP backend, MuJoCo twin, and a 5° hardware test](https://www.reddit.com/r/robotics/comments/1xf9oo0/realman_eco65_bringup_a_shared_mcp_backend_mujoco/)**

I’m building a robot lab in a Gaussian-splat reconstruction of my office. Today the RealMan ECO65 (on loan) finally moved: J1 +5° at 5% speed and back. Then I switched its Wi-Fi to client mode, lost access, and discovered I had no Ethernet cable. The software side has one shared backend for Codex and Claude, revision-checked edits, a MuJoCo twin and link/desk collision checks. The MCP motion interface is still simulation-only; the physical move was a separate controller session. The twin is a nominal model, not validated hardware behaviour. EP19 shows the build and the failures. The J1 visual is a labelled replay of the logged command. https://www.youtube.com/watch?v=1ZrYGwZJQto For those running an arm in a home lab: what was the first mismatch you found between your twin and the hardware?

3d ago

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

Bloomberg • 1d ago

---

**[Foundry Robotics Raises $100 Million Series A to Build America’s First Autonomous Factory for Assembly](https://www.businesswire.com/news/home/20261028508802/en/Foundry-Robotics-Raises-%24100-Million-Series-A-to-Build-Americas-First-Autonomous-Factory-for-Assembly)**

Business Wire • 10h ago

---

**[We went inside Amazon's robot-powered warehouse to see if machines are taking jobs. What we found surprised us.](https://www.businessinsider.com/amazon-robot-warehouse-where-jobs-changing-ai-robotics-workers-2026-9)**

Inside Amazon's robotic warehouse in Tracy, California, workers explain how automation is transforming their jobs.

Business Insider • 16h ago

---

**[Spacewalk Preps, Robotics Jobs, and Science Duties Fill Tuesday Schedule](https://www.nasa.gov/blogs/spacestation/2026/10/27/spacewalk-preps-robotics-jobs-and-science-duties-fill-tuesday-schedule/)**

Spacewalking tools and a pair of robotics jobs topped Tuesday’s schedule aboard the International Space Station. The Expedition 75 crew members also kept up their scientific duties configuring botany research hardware and setting up advanced Earth observation gear.

NASA (.gov) • 1d ago

---

**[Unitree's quarterly revenue surges 70% in test for China's robotics sector](https://www.reuters.com/world/asia-pacific/unitrees-q3-profit-down-174-on-year-test-chinas-robotics-sector-2026-10-28/)**

Reuters • 12h ago

---

**[Robots roaming grocery stores could put millions of retail jobs at risk](https://www.newsnationnow.com/business/your-money/robots-grocery-stores-retail-jobs/)**

NewsNation • 3h ago

---

**[Doctor performs surgery on patient at hospital 35 miles away using robotics - ABC News](https://abcnews.com/GMA/Wellness/doctor-performs-surgery-patient-hospital-35-miles-robotics/story?id=137576330)**

A doctor in Florida performed a medical first on Sunday, using a robotic telesurgery system to perform a surgery at a hospital located 35 miles away.

ABC News - Breaking News, Latest News and Videos • 2d ago

---

**[San Francisco startup offered $20 an hour to walk robot dogs for AI training: report](https://www.foxbusiness.com/technology/san-francisco-startup-offered-20-hour-walk-robot-dogs-ai-training-report)**

The $20-an-hour job posting sought workers to operate four-legged robots on outdoor testing routes through San Francisco with no robotics experience required.

Fox Business • 2h ago

---

**[Arizona Robotics League](https://www.mlb.com/dbacks/video/arizona-robotics-league)**

The Arizona Diamondbacks and Honeywell Aerospace are proud to support the Arizona Robotics League

MLB.com • 3h ago

---

**[Exclusive: Rendezvous Robotics Raises $20M to Develop Self-Assembling Spacecraft](https://payloadspace.com/exclusive-rendezvous-robotics-raises-20m-to-develop-self-assembling-spacecraft/)**

Rendezvous Robotics is developing technology to allow future satellites to launch in pieces that can self-assemble in space.

Payload Space • 12h ago

---

---

## YouTube Videos: "robotics"

**[Robot Dog Entered the Lion&#39;s Territory... Big Mistake?!](https://www.youtube.com/watch?v=eZQo7KqJy8c)**

What happens when a robot dog walks into the world of lions? In today's episode of Wild Clash, the mightiest and most curious ...

📺 Wild Clash

👁️ 1.1M • 👍 9K • 💬 607 • ⏱️ 8:40 • 4d ago

---

**[AI agent builds itself a robot body, does exactly what experts warned](https://www.youtube.com/watch?v=QRVz697rEx0)**

AI Robot. Is AI dangerous? Can we trust AI? AI Agents and AGI. Use code insideai at https://incogni.com/insideai to get an ...

📺 InsideAI

👁️ 2.3M • 👍 41K • 💬 4K • ⏱️ 15:05 • 3d ago

---

**[Tesla Leaked Optimus 3 At Earnings Call | It&#39;s As Good As They Say](https://www.youtube.com/watch?v=gS1iOU_JnkA)**

Tesla has started production of Optimus on a line in Fremont, and on their third quarter earnings call Elon Musk said "there is no ...

📺 Ryan Shaw

👁️ 118K • 👍 2K • 💬 171 • ⏱️ 37:43 • 4d ago

---

**[New Unitree H2X AI Robot Shocks The World With Superhuman Strength](https://www.youtube.com/watch?v=Uz5ktECdg6M)**

Unitree just dropped the H2X AI robot, and its terrifying strength is shocking the world. This humanoid bodyguard fights knife ...

📺 MACHINEKIND

👁️ 19K • 👍 222 • 💬 34 • ⏱️ 13:25 • 5d ago

---

**[Nvidia Microduck AI Robots are mind blowing - World Premiere and First Look](https://www.youtube.com/watch?v=ac6pspFbPsI)**

Have a look at the new Nvidia Microduck AI robots. NVIDIA CEO Jensen Huang was joined onstage at GTC Berlin 2026 by four ...

📺 REC Anything

👁️ 1.8M • 👍 11K • 💬 1K • ⏱️ 8:29 • 6d ago

---

**[Microduck robots go viral at NVIDIA GTC 2026 #robots #microduck #nvidia](https://www.youtube.com/watch?v=tYROJBVwt5M)**

Hugging Face says it's sold more than 4000 of its Microducks since their viral appearance during Jensen Huang's NVIDIA GTC ...

📺 Kalil 4.0

👁️ 121K • 👍 905 • 💬 38 • ⏱️ 0:34 • 5d ago

---

**[Meet Unitree’s latest security robot: martial arts skills &amp; car-lifting strength](https://www.youtube.com/watch?v=Vez_mlGo7gE)**

📺 ShanghaiEye魔都眼

👁️ 113K • 👍 741 • 💬 337 • ⏱️ 1:01 • 4d ago

---

**[Unitree&#39;s New Guard Robot Comes With a Warning](https://www.youtube.com/watch?v=oq1Ia8zlXNQ)**

Unitree posted the H2-X on Oct 21 and pitches it as a guardian. The knife scene is labeled a security demonstration, and the last ...

📺 The Humanoid Files

👁️ 77K • 👍 993 • 💬 119 • ⏱️ 0:39 • 6d ago

---

**[Ai is Dropping. The Robotics Stack is Just Starting ($2.5T Opportunity)](https://www.youtube.com/watch?v=OMDj6el4AbY)**

I'm Kuran Francis, and in this video I'll be mapping the full 8-layer robotics stack for physical AI. Get a free $55 when you trade $25 ...

📺 Fin Tek

👁️ 56K • 👍 827 • 💬 40 • ⏱️ 22:57 • 5d ago

---

**[Meet the AI Robots Built with NVIDIA RTX Spark #shorts](https://www.youtube.com/watch?v=ERQPIELdV4Y)**

Engineered on Nvidia supercomputers and trained within a high-fidelity Omniverse digital twin, these robots are the next evolution ...

📺 Eco Life

👁️ 5K • 👍 51 • 💬 3 • ⏱️ 0:38 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

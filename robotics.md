---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-11T23:59:32.122627+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- videos
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 11, 2026 at 23:59 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I Built Disney’s BD-X Star Wars Robot](https://www.reddit.com/r/robotics/comments/1ta3ynw/i_built_disneys_bdx_star_wars_robot/)**

Over the past year, I’ve been recreating Disney’s BD-X Star Wars Robot :) it’s hard itself to walk using reinforcement learning in mjlab and then was able to walk in the real world. I recently uploaded a video on my YouTube explaining the full build process and how I brought it to life :) Feel free to ask me anything!

10h ago

---

**[A few weeks running an end to end VLA on a real arm and some things I did not expect](https://www.reddit.com/r/robotics/comments/1tae37w/a_few_weeks_running_an_end_to_end_vla_on_a_real/)**

Been quietly swapping our usual perception/planning/control stack for an end to end VLA model on a UR style arm + parallel gripper setup. Mostly because my advisor wanted to see if the hype was real, and because two of the open weights releases this spring (pi0.6 and the WALL OSS drop from X Square Robot) actually run on a single 4090 without too much pain. Some stuff that genuinely caught me off guard, in no particular order. The good. Recovery behavior is weirdly fluent. With our old stack, if the grasp slipped we hit a planning re-call and the arm would just stop for ~400ms and then redo the whole motion. The VLA just adjusts mid trajectory the way a person would, it doesnt look like a state machine recovering, it looks like a hand. I have no good explanation for why this is the part that surprised me most, but it is. The annoying. Latency variance is awful at the start. First few hundred episodes of fine tuning, we were seeing 80 to 240 ms inference jitter on the same hardware. Turns out a lot of that was us still feeding it preprocessed depth from our old pipeline, which the model didnt want. Once we just gave it raw RGB and proprio it stabilized. The unexpected. Language conditioning is not magic. "pick up the red one" works. "pick up the red one and put it on the cloth, not the plate" is a coin flip in our setup. Multi clause instructions still fall apart in ways that feel very 2022. I think people see the demos and assume natural langauge is solved, it is very much not, at least not at our scale. The philosophical one. After a while it becomes hard to tell what the model is "doing wrong". With a modular stack, when something fails you can point at it: localization drifted, the planner chose a bad pose, the controller overshot. With end to end you just get a worse rollout and a vague feeling. The interpretability story for VLAs is going to be a real problem for anyone shipping this in safety critical contexts. Not selling anything, not affiliated with the labs releasing these weights. Honestly the main reason I am writing this up is because all the public discourse is either "lab demo of the century" or "it is all teleop", and the actual day to day experience of running one of these things is much more boring and much more interesting than either. If you have run pi0.6, WALL OSS, OpenVLA or anything in that family on real hardware (not sim), drop your weirdest observation. I will collect them and post a follow up if there is enough material.

4h ago

---

**[Live 'Violence' Testing: Little Guy Has a Good Temper – Doesn’t Get Mad No Matter How Many Times He’s Kicked, Just Dusts Himself Off and Gets Back Up. #Reinforcement Learning.](https://www.reddit.com/r/robotics/comments/1ta6h64/live_violence_testing_little_guy_has_a_good/)**

8h ago

---

**[Just finished HW of my Bimanual wheeled robot](https://www.reddit.com/r/robotics/comments/1t9xfyj/just_finished_hw_of_my_bimanual_wheeled_robot/)**

ROS 2 based Two LeRobot arms Pan & Tilt with Realsense depth camera Diff drive with ros2_control Next I want to pick socks and put them into washing machine, or open 3D printer and take out finished prints. Let me know if you have some cool ideas! I want to make a sim either in Gazebo or Isaac so people can try it out and/or do something useful in simulation.

15h ago

---

**[Assistive Robotics Prototype - Preparing a salad](https://www.reddit.com/r/robotics/comments/1taaj9x/assistive_robotics_prototype_preparing_a_salad/)**

6h ago

---

**[RLDX-1 just dropped, claims dexterity needs missing modalities not more scale](https://www.reddit.com/r/robotics/comments/1ta4eik/rldx1_just_dropped_claims_dexterity_needs_missing/)**

RLWRLD dropped RLDX-1 last week (https://www.rlwrld.ai/en/rldx-1). Their pitch goes against the current GR00T/π₀ consensus that scaling VLAs eventually gives you dexterity. Their argument: scale can't recover a modality the model was never given. So they built MSAT, each modality (tactile, torque, vision, memory) gets its own stream and fuses late. Sympathetic to the thesis. We've all watched robots fail at basic physical intuition from vision alone. But the way they scale data is via Cosmos-Predict2, which is itself a video world model, so the synthetic pipeline only stretches the vision modality. Tactile and torque still depend on real teleop, which is the actual bottleneck. Wonder how they're handling data curation for the modalities that synthetic can't easily reach. Architecture intuition checks out. Forcing torque and 4-frame video through one trunk means whichever has stronger gradients eats the capacity. But one thing nags me: humans use vision to predict touch before contact. If you train each modality as its own stream, do you lose the cross-modal priors that would help on vision-only hardware? Or does the joint self-attention recover that? The 3DGS-based human data pipeline is the part I'd actually push more people to read. Reconstruct the workspace with Gaussian Splatting, track bare human hands, retarget onto robot hands, roll out in sim. 200+ demos per hour and no awkward DexUMI-style hand-strap rigs. This is where the data engine for dexterity quietly wins or loses. On the "SOTA at 20% of GR00T's compute" claim, grain of salt. Different data mixes, different VLM backbones, tech report not a controlled ablation. Still, 87.5 vs 50 on real conveyor pick-and-place is hard to wave away.

🔗 [youtu.be](https://youtu.be/xh8UaGT4J5s) • 9h ago

---

**[CUDA Kernel + Quantization for VLA Training/RL](https://www.reddit.com/r/robotics/comments/1tad18b/cuda_kernel_quantization_for_vla_trainingrl/)**

Recently started experimenting with using custom CUDA kernels + quantization paths to accelerate VLA fine-tuning and RL workloads. Current Pi0.5 results: ~2.2x faster training/fine-tuning VRAM reduced from ~26GB → ~10GB Faster RL iteration cycles Much easier to run on consumer GPUs / smaller robotics labs Most optimization work in embodied AI currently focuses on inference. But after working on real deployments, I’m increasingly convinced that robotics training/RL infrastructure is also massively bottlenecked by: memory bandwidth launch overhead small-batch inefficiency fragmented runtime stacks There’s still a huge amount of unexplored optimization space at the kernel/runtime layer for embodied AI. Welcome to check it out!! https://github.com/LiangSu8899/FlashRT

4h ago

---

**[A custom lego robot taking a beer up some stairs without spilling](https://www.reddit.com/r/robotics/comments/1t9cmc4/a_custom_lego_robot_taking_a_beer_up_some_stairs/)**

1d ago

---

**[Update on the robot game thing... actually help me name this.](https://www.reddit.com/r/robotics/comments/1tab1pu/update_on_the_robot_game_thing_actually_help_me/)**

It needs a name, somebody help me make a name for this thing. When it's all said and done , the robotic arm will pick up the ball and put it into a launcher that will then launch it to hit a target and then collect it in the funnel and bring it back to the original point. What would you name something like that? Also,The theme is that you're going to be on the moon.

6h ago

---

**[3 months ago I launched a ROS2 practice platform. Here's what 3,100 engineers taught me.](https://www.reddit.com/r/robotics/comments/1tacboq/3_months_ago_i_launched_a_ros2_practice_platform/)**

In February I launched SimuCode — a browser-based ROS2 practice platform. No setup, real Docker containers, runtime-verified grading. Three months and 3,100+ users later, here's what I've learned: What people actually struggle with: TF2 and transform trees — by far the most failed problem category Understanding why their node graph looks wrong at runtime vs what they expected Debugging from runtime behavior rather than reading their own code What we built because of that: Runtime introspector that captures actual ROS2 graph behavior — topic Hz, TF frames, node lifecycle states — not just stdout AI reviewer that analyzes your failed run using the full runtime context, not just your code Problems designed around runtime debugging, not implementation Numbers: 3,130 users, 40+ countries US is the biggest market (729 users), India #2 (580) Pro tier live If you're preparing for robotics interviews or just want to practice ROS2 without the environment headache. Still free to start.

5h ago

---

---

## Google News: "robotics"

**[China wants more robots but not fewer workers](https://www.economist.com/finance-and-economics/2026/05/11/china-wants-more-robots-but-not-fewer-workers)**

The Economist • 6h ago

---

**[Japan: World-first fully automated medicine lab with humanoids, robots and no humans](https://interestingengineering.com/ai-robotics/japan-unmanned-lab-robots-ai-automation-aist)**

A Japanese lab deploys humanoid robots and AI to automate medical experiments with no human staff on site.

Interesting Engineering • 10h ago

---

**[Are humanoid robots all hype?](https://www.vox.com/podcasts/488050/humanoid-robots-ai-us-china-tesla-hype)**

﻿AI is making them better — but they’re not going to be doing your chores anytime soon.

vox.com • 12h ago

---

**[Figure’s Humanoid Robots Tidy a Bedroom, Hinting at Bigger Home Automation Leap](https://www.eweek.com/news/figure-ai-humanoid-robots-bedroom-demo/)**

Figure AI’s latest humanoid robot demo shows two machines tidying a bedroom and making a bed without direct communication.

eWeek • 7h ago

---

**[Robots for America Launches National Coalition to Advance U.S. Robotics Deployment Policy](https://www.businesswire.com/news/home/20260511908908/en/Robots-for-America-Launches-National-Coalition-to-Advance-U.S.-Robotics-Deployment-Policy)**

In a move to strengthen long-term manufacturing productivity, U.S. government officials asked the robotics industry to organize and deliver a unified plan to...

Business Wire • 9h ago

---

**[What Serve Robotics (SERV)'s Rapid Q1 Revenue Surge And Wider Losses Mean For Shareholders](https://finance.yahoo.com/markets/stocks/articles/serve-robotics-serv-rapid-q1-200754214.html)**

In early May 2026, Serve Robotics Inc. reported first-quarter 2026 revenue of about US$2.98 million versus US$0.44 million a year earlier, while its net loss widened to roughly US$49.0 million from US$13.22 million and it reaffirmed full-year 2026 revenue guidance of approximately US$26.0 million. The quarter also marked a step change in scale and scope, as Serve expanded to 44 cities across 14 states, grew its robot fleet to around 2,000 units, and moved into healthcare robotics through the...

Yahoo Finance • 1d ago

---

**[Korea’s biggest manufacturers back Config, the TSMC of robot data](https://techcrunch.com/2026/05/11/koreas-biggest-manufacturers-back-config-the-tsmc-of-robot-data/)**

Samsung, Hyundai and LG just bet on the startup that wants to be robotics' data backbone.

TechCrunch • 13h ago

---

**[South Korea Exploring Using Hyundai Robots as Army Numbers Fall](https://www.bloomberg.com/news/articles/2026-05-11/south-korea-exploring-using-hyundai-robots-as-army-numbers-fall)**

Bloomberg.com • 19h ago

---

**[Humanoid robots enter the classroom in Classover’s new K-12 AI program](https://www.stocktitan.net/news/KIDZ/classover-launches-embodied-ai-robotics-education-platform-featuring-mt6iq5bqgao9.html)**

Humanoid and robotic dog systems from Unitree power Classover’s proprietary K-12 AI curriculum, aimed at hands-on coding and robotics training for classrooms.

Stock Titan • 12h ago

---

**[Artificial muscle merges sensing and movement in one structure for humanoid robots](https://techxplore.com/news/2026-05-artificial-muscle-merges-movement-humanoid.html)**

Tech Xplore • 23h ago

---

---

## YouTube Videos: "robotics"

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 545K • 👍 48K • 💬 4K • ⏱️ 23:53 • 1d ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 8K • 👍 141 • 💬 61 • ⏱️ 2:19 • 3d ago

---

**[Atlas&#39; Balancing Act | Boston Dynamics](https://www.youtube.com/watch?v=UoHfGhLHRkg)**

Balancing commercial goals and robotics research can be tricky, but with Atlas we're making it work.

📺 Boston Dynamics

👁️ 377K • 👍 21K • 💬 1K • ⏱️ 0:44 • 6d ago

---

**[Humanoid robots engage in full tea-making process](https://www.youtube.com/watch?v=73dGNetDtj4)**

Robots that ran a half-marathon in Beijing in April have swapped the track for a tea production base in Fujian Province — picking ...

📺 CGTN Europe

👁️ 2K • 👍 113 • 💬 10 • ⏱️ 0:56 • 13h ago

---

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 3K • 👍 80 • 💬 14 • ⏱️ 8:07 • 6d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=A8sENgAxZbw)**

📺 Robot Julie 

👁️ 403K • 👍 3K • 💬 74 • ⏱️ 0:27 • 2d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=2UUaZy4cWHw)**

📺 Robot Julie 

👁️ 30K • 👍 202 • 💬 2 • ⏱️ 0:26 • 2d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 31K • 👍 263 • 💬 96 • ⏱️ 2:14 • 6d ago

---

**[🤖 Control a Robot Arm with Joystick!](https://www.youtube.com/watch?v=Z3UCTCq5OJ8)**

Control a Robot Arm with One Joystick using Arduino! code link ...

📺 MW Electronics Lab

👁️ 214K • 👍 1K • 💬 35 • ⏱️ 0:05 • 5d ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 5K • 👍 141 • 💬 19 • ⏱️ 20:22 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

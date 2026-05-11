---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-11T19:49:03.101641+00:00'
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

**Last Updated:** May 11, 2026 at 19:49 UTC  
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

5h ago

---

**[Live 'Violence' Testing: Little Guy Has a Good Temper – Doesn’t Get Mad No Matter How Many Times He’s Kicked, Just Dusts Himself Off and Gets Back Up. #Reinforcement Learning.](https://www.reddit.com/r/robotics/comments/1ta6h64/live_violence_testing_little_guy_has_a_good/)**

4h ago

---

**[Just finished HW of my Bimanual wheeled robot](https://www.reddit.com/r/robotics/comments/1t9xfyj/just_finished_hw_of_my_bimanual_wheeled_robot/)**

ROS 2 based Two LeRobot arms Pan & Tilt with Realsense depth camera Diff drive with ros2_control Next I want to pick socks and put them into washing machine, or open 3D printer and take out finished prints. Let me know if you have some cool ideas! I want to make a sim either in Gazebo or Isaac so people can try it out and/or do something useful in simulation.

11h ago

---

**[A custom lego robot taking a beer up some stairs without spilling](https://www.reddit.com/r/robotics/comments/1t9cmc4/a_custom_lego_robot_taking_a_beer_up_some_stairs/)**

1d ago

---

**[RLDX-1 just dropped, claims dexterity needs missing modalities not more scale](https://www.reddit.com/r/robotics/comments/1ta4eik/rldx1_just_dropped_claims_dexterity_needs_missing/)**

RLWRLD dropped RLDX-1 last week (https://www.rlwrld.ai/en/rldx-1). Their pitch goes against the current GR00T/π₀ consensus that scaling VLAs eventually gives you dexterity. Their argument: scale can't recover a modality the model was never given. So they built MSAT, each modality (tactile, torque, vision, memory) gets its own stream and fuses late. Sympathetic to the thesis. We've all watched robots fail at basic physical intuition from vision alone. But the way they scale data is via Cosmos-Predict2, which is itself a video world model, so the synthetic pipeline only stretches the vision modality. Tactile and torque still depend on real teleop, which is the actual bottleneck. Wonder how they're handling data curation for the modalities that synthetic can't easily reach. Architecture intuition checks out. Forcing torque and 4-frame video through one trunk means whichever has stronger gradients eats the capacity. But one thing nags me: humans use vision to predict touch before contact. If you train each modality as its own stream, do you lose the cross-modal priors that would help on vision-only hardware? Or does the joint self-attention recover that? The 3DGS-based human data pipeline is the part I'd actually push more people to read. Reconstruct the workspace with Gaussian Splatting, track bare human hands, retarget onto robot hands, roll out in sim. 200+ demos per hour and no awkward DexUMI-style hand-strap rigs. This is where the data engine for dexterity quietly wins or loses. On the "SOTA at 20% of GR00T's compute" claim, grain of salt. Different data mixes, different VLM backbones, tech report not a controlled ablation. Still, 87.5 vs 50 on real conveyor pick-and-place is hard to wave away.

🔗 [youtu.be](https://youtu.be/xh8UaGT4J5s) • 5h ago

---

**[Assistive Robotics Prototype - Preparing a salad](https://www.reddit.com/r/robotics/comments/1taaj9x/assistive_robotics_prototype_preparing_a_salad/)**

2h ago

---

**[Update on the robot game thing... actually help me name this.](https://www.reddit.com/r/robotics/comments/1tab1pu/update_on_the_robot_game_thing_actually_help_me/)**

It needs a name, somebody help me make a name for this thing. When it's all said and done , the robotic arm will pick up the ball and put it into a launcher that will then launch it to hit a target and then collect it in the funnel and bring it back to the original point. What would you name something like that? Also,The theme is that you're going to be on the moon.

1h ago

---

**[Spatial VLM : Projecting 2D reasoning into 3D output (open source demo)](https://www.reddit.com/r/robotics/comments/1t9tkko/spatial_vlm_projecting_2d_reasoning_into_3d/)**

So I've always argued that Physical AI for robotics need actionable outputs like 3D coordinates, not bullet points or nice paragraphs. So decided to experiment by combining a VLM with Monocular Depth Estimation, essentially projecting 2D reasoning into 3D, I called it Odyseus - Spatial VLM Tech Stack: - VLM: Qwen 3.6 - Depth Estimation: Depth Anything 3 - Metric Large Worked pretty well, figured to share, check repo: https://github.com/MercuriusTech/Odyseus-Spatial-VLM

14h ago

---

**[CUDA Kernel + Quantization for VLA Training/RL](https://www.reddit.com/r/robotics/comments/1tad18b/cuda_kernel_quantization_for_vla_trainingrl/)**

Recently started experimenting with using custom CUDA kernels + quantization paths to accelerate VLA fine-tuning and RL workloads. Current Pi0.5 results: ~2.2x faster training/fine-tuning VRAM reduced from ~26GB → ~10GB Faster RL iteration cycles Much easier to run on consumer GPUs / smaller robotics labs Most optimization work in embodied AI currently focuses on inference. But after working on real deployments, I’m increasingly convinced that robotics training/RL infrastructure is also massively bottlenecked by: memory bandwidth launch overhead small-batch inefficiency fragmented runtime stacks There’s still a huge amount of unexplored optimization space at the kernel/runtime layer for embodied AI. Welcome to check it out!! https://github.com/LiangSu8899/FlashRT

43m ago

---

**[Bimo’s walking model now runs natively on a Raspberry Pi Pico at 5ms inference time!](https://www.reddit.com/r/robotics/comments/1t968vj/bimos_walking_model_now_runs_natively_on_a/)**

This is Bimo walking completely standalone: no data cable, no external compute, just a battery and an RP2040 (custom board) running the walking policy natively at ~5.2ms inference time. The main walking model trains on thousands of parallel environments in Isaac Lab. That policy gets distilled down to a tiny student network and compiled directly into the MCU firmware. Here's the pipeline: Train a standard 256×128×64 teacher model in Isaac Lab (~5min on an RTX 4080) Distill it into a 64×32 student network (~30s, yep, I was surprised too) Export as pure C using onnx2c Compile into the RP2040 firmware via Arduino IDE Inference runs at 5.0-5.2ms, comfortably within the 50ms control loop The full distillation pipeline, the standalone MCU inference code, and the Bimo API ported to ROS2 nodes are all coming in the next update (v1.1). ROS2 was a direct request from the last Reddit post, so that's in. Has anyone else run RL locomotion policies natively on an MCU? How small have you made the student network before significantly degrading performance? If you want to follow the development, join the Discord server, all updates go there first. Code update to v1.1 will be available on GitHub soon.

1d ago

---

---

## Google News: "robotics"

---

## YouTube Videos: "robotics"

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 502K • 👍 46K • 💬 4K • ⏱️ 23:53 • 1d ago

---

**[Humanoid robots engage in full tea-making process](https://www.youtube.com/watch?v=73dGNetDtj4)**

Robots that ran a half-marathon in Beijing in April have swapped the track for a tea production base in Fujian Province — picking ...

📺 CGTN Europe

👁️ 2K • 👍 96 • 💬 10 • ⏱️ 0:56 • 9h ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 8K • 👍 140 • 💬 61 • ⏱️ 2:19 • 2d ago

---

**[Atlas&#39; Balancing Act | Boston Dynamics](https://www.youtube.com/watch?v=UoHfGhLHRkg)**

Balancing commercial goals and robotics research can be tricky, but with Atlas we're making it work.

📺 Boston Dynamics

👁️ 376K • 👍 21K • 💬 1K • ⏱️ 0:44 • 6d ago

---

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 3K • 👍 80 • 💬 14 • ⏱️ 8:07 • 6d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=A8sENgAxZbw)**

📺 Robot Julie 

👁️ 334K • 👍 3K • 💬 64 • ⏱️ 0:27 • 2d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=2UUaZy4cWHw)**

📺 Robot Julie 

👁️ 30K • 👍 201 • 💬 2 • ⏱️ 0:26 • 2d ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 5K • 👍 140 • 💬 19 • ⏱️ 20:22 • 6d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 31K • 👍 263 • 💬 96 • ⏱️ 2:14 • 6d ago

---

**[Mender REBUILT Getting Swarmed | Ridiculous Healing Waves | War Robots](https://www.youtube.com/watch?v=qXpzp0DWSXc)**

Mender returns to face the meta. We need to make the most powerful Mender possible. The Menders have pretty much become ...

📺 PREDATOR WR

👁️ 12K • 👍 484 • 💬 69 • ⏱️ 14:24 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

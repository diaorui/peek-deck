---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-10T23:09:08.523499+00:00'
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

**Last Updated:** February 10, 2026 at 23:09 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[K-bot](https://www.reddit.com/r/robotics/comments/1r18pvw/kbot/)**

Hello everyone, since K-Scale Labs (https://kscale.ai) shut down and they still kept everything open-source on their GitHub page, I was wondering if anyone has actually tried to build their humanoid robot on their own. Do you guys think it would be worth it or not and why?

4h ago

---

**[The world's first 'biomimetic AI robot' just strolled in from the uncanny valley - and yes, it's super-creepy](https://www.reddit.com/r/robotics/comments/1r0zrzk/the_worlds_first_biomimetic_ai_robot_just/)**

A Shanghai startup, DroidUp, has unveiled Moya, a biomimetic AI robot designed to cross the uncanny valley. Unlike plastic and metal droids, Moya features silicone skin that is heated to human body temperature and mimics subtle facial expressions like eyebrow raises. Standing 5'5" and weighing 70 lbs, Moya is built on a modular platform that allows for swapping between male and female presentations. With a price tag of ~$173k, DroidUp aims to deploy these warm companions in healthcare and business by late 2026.

🔗 [TechRadar](https://www.techradar.com/computing/the-worlds-first-biomimetic-ai-robot-just-strolled-in-from-the-uncanny-valley-and-yes-its-super-creepy) • 10h ago

---

**[G1 kicks mother and child when performing](https://www.reddit.com/r/robotics/comments/1r0awur/g1_kicks_mother_and_child_when_performing/)**

1d ago

---

**[I built URDFViewer.com, a robotic workcell analysis and visualization tool](https://www.reddit.com/r/robotics/comments/1r1f3dp/i_built_urdfviewercom_a_robotic_workcell_analysis/)**

While developing ROS2 applications for robotic arm projects, we found it was difficult to guarantee that a robot would execute a full sequence of motion without failure. In pick-and-place applications, the challenge was reaching a pose and approaching along a defined direction. In welding or surface finishing applications, the difficulty was selecting a suitable start pose without discovering failure midway through execution. Many early iterations involved trial and error to find a working set of joint configurations that could serve as good “seeds” for further IK and motion planning. Over time, we built internal offline utilities to nearly guarantee that our configurations and workspace designs would work. These relied heavily on open-source libraries like TRAC-IK, along with extracting meaningful metrics such as manipulability. Eventually, we decided to package the internal tool we were using and open it up to anyone working on robotic application setup or pre-deployment validation. What the platform offers: a. Select from a list of supported robots, or upload your own. Any serial chain in standard robot_description format should work. b. Move the robot using interactive markers, direct joint control, or by setting a target pose. If you only need FK/IK exploration, you can stop here. The tool continuously displays end-effector pose and joint states. c. Insert obstacles to resemble your working scene. d. Create regions of interest and add orientation constraints, such as holding a glass upright or maintaining a welding direction. e. Run analysis to determine: Whether a single IK branch can serve the entire region Whether all poses within the region are reachable Whether the region is reachable but discontinuous in joint space How we hope it helps users: a. Select a suitable robot for an application by comparing results across platforms. b. Help robotics professionals, including non-engineers, create and validate workcells early. c. Create, share, and collaborate on scenes with colleagues or clients. We’re planning to add much more to this tool, and we hope user feedback helps shape its future development. Give it a try.

🔗 [urdfviewer.com](https://urdfviewer.com) • 51m ago

---

**[r/c sumo bots?](https://www.reddit.com/r/robotics/comments/1r1c87b/rc_sumo_bots/)**

Hello! Our makerspace for kids 11-18 is hosting a three week summer camp this summer. Most of the kids will likely be 11-13 who come. The kids we know will come have indicated they would like to build and program sumo bots. The kids will have wide varieties of experience. Some will have no coding experience at all, so I am thinking rather than autonomous sumo bots they should make remote controlled ones. Which I realize now makes them not robots so maybe y'all can't help. We have here several Creality HI 3d printers and a large Omtech laser, as well as basic woodshop and electronics things like soldering irons and breadboards and all kinds of electronical bits and bobs. I am thinking if we have a premade chassis that the kids can add on to, they still get to design stuff and print it or cut it out but the basics are already there, then they can do the electronics and whatever coding needs to go between the rc stuff and the electronics and maybe they can conceivably do all that in 15 days/three weeks? I think trying to make it autonomous will be too challenging for all, but we can always suggest/challenge the kids who are good coders already to do so. Have any of y'all done something like this? Does it seem feasible? Thanks!

2h ago

---

**[Design process advice for robotic arm](https://www.reddit.com/r/robotics/comments/1r1c3ce/design_process_advice_for_robotic_arm/)**

2h ago

---

**[Opensource IoT/Robotics ESP32 Controller](https://www.reddit.com/r/robotics/comments/1r19o5v/opensource_iotrobotics_esp32_controller/)**

Board I designed a custom board called ESP PowerDeck, based on the ESP32-S3. It’s meant for experimenting with robotics and IoT where you need real power handling, not just a breadboard setup. Would love feedback from the community — especially on features that might make it more useful for robotics work. (edit moved photo up so it could be seen ;p)

4h ago

---

**[Yet another Onshape robot exporter, but this one (hopefully) saves your API credits.](https://www.reddit.com/r/robotics/comments/1r18zed/yet_another_onshape_robot_exporter_but_this_one/)**

4h ago

---

**[OEM LiDAR](https://www.reddit.com/r/robotics/comments/1r17mgn/oem_lidar/)**

Hello guys A quick question am looking for OEM 2D lidar Sensor I want to flash them and deploy my own software into it. Where can I get such lidar sensor? Let me know if you know any vendors or any websites where can I buy.

5h ago

---

**[We trained a VLA model on 20,000 hours of real robot data across 9 embodiments, then tested it on 100 tasks. Here's what actually worked and what didn't.](https://www.reddit.com/r/robotics/comments/1r0au80/we_trained_a_vla_model_on_20000_hours_of_real/)**

Over the past year our team built LingBot-VLA, a Vision-Language-Action foundation model for dual-arm manipulation. We just released everything: code, base model, and benchmark data (paper: arXiv:2601.18692, code: github.com/robbyant/lingbot-vla, weights on HuggingFace). I wanted to share what we learned deploying this across real hardware because the results tell an honest and, I think, useful story for anyone working on generalist robot policies. The setup: ~20,000 hours of teleoperated manipulation data from 9 mainstream dual-arm configs (Agibot G1, AgileX, Galaxea R1Pro, Realman, Leju KUAVO, and others). We evaluated on 3 physical platforms, 100 tasks each, 130 post-training demos per task, 15 trials per task per model. That's 22,500 total real-world trials comparing us against π0.5, GR00T N1.6, and WALL-OSS under identical conditions. The honest numbers: our best variant (with depth distillation) hit 17.30% average success rate and 35.41% progress score across all 300 task-platform pairs. π0.5 got 13.02% SR / 27.65% PS. WALL-OSS landed at 4.05% SR. Before anyone says "17% is low," I want to contextualize this. These are 100 diverse bimanual tasks, many requiring multi-step fine-grained manipulation (cleaning tableware, stacking, arranging objects), tested across three physically different robots. Some individual tasks hit 80%+ SR, others are near zero. Real-world bimanual manipulation across this breadth of tasks is genuinely hard, and I think the field benefits from reporting these numbers honestly rather than cherry-picking the best 5 tasks for a demo reel. What actually worked well: Scaling laws are real and not saturating. We ran a systematic study scaling pre-training data from 3K to 6K to 13K to 18K to 20K hours. Success rates climbed consistently across all three platforms with no sign of plateau at 20K. This was the most exciting finding for us because it suggests the path forward is clear: more diverse, high-quality real-world data keeps helping. Depth distillation made a meaningful difference. We use learnable queries aligned with depth embeddings from our LingBot-Depth model via cross-attention. This bumped average SR from 15.74% to 17.30% in real-world and from 85.34% to 86.68% in randomized simulation scenes. The gain was most visible on transparent object manipulation (glass vases, clear containers) where RGB alone struggles. Data-efficient adaptation. With only 80 demos per task, LingBot-VLA outperformed π0.5 trained on the full 130 demos, in both SR and progress score. The gap widened as we added more post-training data, which suggests the pre-training is providing genuinely useful priors rather than just memorizing. Training efficiency. We built a custom codebase with FSDP2, mixed-precision, FlexAttention, and operator fusion via torch.compile. On 8 GPUs we get 261 samples/sec/GPU for the Qwen2.5-VL-3B backbone, which is 1.5x to 2.8x faster than StarVLA, Dexbotic, and OpenPI depending on the VLM. Scaling to 256 GPUs tracks near-linear throughput. This matters practically because iterating on 20K hours of data is brutal without an efficient pipeline. What didn't work or remains unsolved: Plenty of tasks are still near 0% SR across all models. Tasks requiring very precise spatial reasoning in cluttered scenes, long-horizon multi-step sequences, or unusual object geometries remain extremely challenging. The depth distillation helps but doesn't solve spatial reasoning completely. Also, the model currently only covers dual-arm tabletop manipulation. Single-arm, mobile manipulation, and non-tabletop scenarios are future work. The architecture uses a Mixture-of-Transformers design (similar to BAGEL) where the VLM and action expert share self-attention but have separate feedforward pathways. Action generation uses flow matching with 50-step action chunks. We found the shared attention critical for letting semantic understanding guide action prediction without the modalities interfering with each other's representations. One thing I'd love to hear from this community: for those of you working with real dual-arm setups, what task categories do you find most important for practical deployment? Our GM-100 benchmark covers 100 tasks but we're always thinking about what's missing. Also curious if anyone has experimented with alternative spatial representations beyond depth for VLA models. All code, model weights, and the benchmark data are public. We wanted to make sure anyone can reproduce these results and build on them.

1d ago

---

---

## Google News: "robotics"

**[Haply Robotics raises $16 million to build the “steering wheels” for physical AI](https://betakit.com/haply-robotics-raises-16-million-to-build-the-steering-wheels-for-physical-ai/)**

How the Montréal startup plans to own the touch layer of robotics.

BetaKit • 1d ago

---

**[China: Humanoid robots perform kung fu moves with Shaolin monks in a viral video](https://interestingengineering.com/ai-robotics/humanoid-robots-kung-fu-with-shaolin-monks)**

A group of humanoid robots made by Agibot performed kung fu moves at the Shaolin Temple in China, captivating viewers with their capabilities.

Interesting Engineering • 1d ago

---

**[VC-backed startups show off robots at Manifest 2026](https://www.axios.com/pro/supply-chain-deals/2026/02/10/robot-startups-demonstrations-manifest-2026)**

The warehouse has become a focus area for startups and investors alike looking to modernize logistics operations.

Axios • 35m ago

---

**[Investor Stephanie Link likes this robotics play, a 'sleeper name for 2026'](https://www.cnbc.com/2026/02/10/investor-stephanie-link-likes-this-robotics-play-a-sleeper-name-for-2026.html)**

Stephanie Link scooped up shares of Rockwell Automation following the robotics firm's latest earnings beat.

CNBC • 3h ago

---

**[Symbotic acquires autonomous forklift maker Fox Robotics](https://www.therobotreport.com/symbotic-acquires-autonomous-forklift-maker-fox-robotics/)**

Symbotic has acquired autonomous forklift developer Fox Robotics in a move that broadens its logistics robotics offerings.

The Robot Report • 1h ago

---

**[Elon Musk warns the U.S. is '1,000% going to go bankrupt' unless AI and robotics save the economy from crushing debt](https://fortune.com/2026/02/07/elon-musk-us-bankruptcy-ai-robotics-economic-growth-national-debt-crisis/)**

"We just need enough time to build the AI and robots to not go bankrupt before then."

Fortune • 3d ago

---

**[China's Alibaba launches AI model to power robots as tech giants talk up 'physical AI'](https://www.cnbc.com/2026/02/10/alibaba-ai-model-robotics-rynnbrain-china.html)**

Nvidia and Google are among a handful of major tech giants developing models for robotics and so-called "phyiscal AI."

CNBC • 12h ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://www.bloomberg.com/news/articles/2026-02-10/alibaba-pushes-into-robotics-ai-with-open-source-rynnbrain)**

Bloomberg.com • 16h ago

---

**[New ‘RynnBrain’ Lifts Alibaba Stock (BABA) as It Enters Robotics AI Race With Nvidia and Google](https://www.tipranks.com/news/new-rynnbrain-lifts-alibaba-stock-baba-as-it-enters-robotics-ai-race-with-nvidia-and-google)**

Alibaba ($BABA) is broadening its AI strategy with a new robotics-focused project. The Chinese e-commerce giant introduced a new AI system called “RynnBrain,” desig...

TipRanks • 12h ago

---

**[AI In Robotics - New Position Paper](https://ifr.org/ifr-press-releases/news/ai-in-robotics-new-position-paper)**

A new generation of AI-powered robots moving from research labs into the real world is fueled by AI tech companies and analysts forecasting a multitrillion-dollar market. The vision is to give artificial intelligence its own robot body. What are the trends, challenges, and commercial applications?

IFR International Federation of Robotics • 16h ago

---

---

## YouTube Videos: "robotics"

**[Atlas Airborne Robot Shows the Final Evolution of Boston Dynamics](https://www.youtube.com/watch?v=IjRjKwZhYCQ)**

The Atlas Airborne Robot takes one final research run as Boston Dynamics pushes humanoid robot control to its absolute limit.

📺 DPCcars

👁️ 72K • 👍 493 • 💬 87 • ⏱️ 2:45 • 3d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 1.2M • 👍 38K • 💬 4K • ⏱️ 1:38 • 3d ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 249K • 👍 4K • 💬 958 • ⏱️ 13:31 • 5d ago

---

**[SHOCKING: XPeng’s New IRON Robot COLLAPSES in Public...](https://www.youtube.com/watch?v=4MNfUBZNRFU)**

XPeng's brand-new IRON humanoid robot just collapsed in public, and the footage has taken the internet by storm. In this video ...

📺 The AI Nexus

👁️ 8K • 👍 141 • 💬 35 • ⏱️ 19:22 • 5d ago

---

**[Elon Musk on Why Everyone Will Want an Optimus Robot by 2027](https://www.youtube.com/watch?v=dWRqUdVBKjE)**

Will a robot soon be watching your children or caring for your parents? Elon Musk predicts a future where billions of humanoid ...

📺 SpaceTakers

👁️ 42K • 👍 858 • 💬 79 • ⏱️ 0:29 • 5d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=HInDqhlzVd4)**

📺 Lin of Brant robot 

👁️ 28K • 👍 69 • 💬 2 • ⏱️ 0:20 • 4d ago

---

**[Boston Dynamics Tests the Limits of Atlas Robot&#39;s Full-Body Control and Mobility](https://www.youtube.com/watch?v=h-pNWy7v_qc)**

Boston Dynamics and the RAI Institute release a video demonstrating the All-Electric Atlas Robot's evolution away from a scripted ...

📺 CNET

👁️ 12K • 👍 284 • 💬 56 • ⏱️ 1:25 • 22h ago

---

**[How They&#39;re Building Robot Hands Like Human Muscles #robotics #innovation #engineering](https://www.youtube.com/watch?v=zcbY5VW4BYc)**

A Hungarian startup is generating buzz with its automated manufacturing system for building robots that's straight out of Westworld ...

📺 Kalil 4.0

👁️ 423 • 👍 14 • ⏱️ 0:45 • 2h ago

---

**[Tesla Was Never a Car Company #teslaoptimus  #elonmusk  #teslarobot  #teslabotgen3 #humanoidrobots](https://www.youtube.com/watch?v=slqW7zBA6Oc)**

They laughed when Elon Musk brought a man in a spandex suit on stage. But in 2026, nobody is laughing. Tesla was never a car ...

📺 By 2050

👁️ 455K • 👍 7K • 💬 170 • ⏱️ 1:00 • 2d ago

---

**[This Is How Warfare Becomes Fully Automated](https://www.youtube.com/watch?v=wrWDnuWlKDs)**

Autonomous micro drones like the Stinger demonstrate how AI can independently identify, track, and eliminate targets using live ...

📺 Deepen

👁️ 129K • 👍 2K • 💬 92 • ⏱️ 0:40 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

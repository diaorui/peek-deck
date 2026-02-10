---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-10T22:06:43.271468+00:00'
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

**Last Updated:** February 10, 2026 at 22:06 UTC  
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

3h ago

---

**[G1 kicks mother and child when performing](https://www.reddit.com/r/robotics/comments/1r0awur/g1_kicks_mother_and_child_when_performing/)**

1d ago

---

**[The world's first 'biomimetic AI robot' just strolled in from the uncanny valley - and yes, it's super-creepy](https://www.reddit.com/r/robotics/comments/1r0zrzk/the_worlds_first_biomimetic_ai_robot_just/)**

A Shanghai startup, DroidUp, has unveiled Moya, a biomimetic AI robot designed to cross the uncanny valley. Unlike plastic and metal droids, Moya features silicone skin that is heated to human body temperature and mimics subtle facial expressions like eyebrow raises. Standing 5'5" and weighing 70 lbs, Moya is built on a modular platform that allows for swapping between male and female presentations. With a price tag of ~$173k, DroidUp aims to deploy these warm companions in healthcare and business by late 2026.

🔗 [TechRadar](https://www.techradar.com/computing/the-worlds-first-biomimetic-ai-robot-just-strolled-in-from-the-uncanny-valley-and-yes-its-super-creepy) • 9h ago

---

**[r/c sumo bots?](https://www.reddit.com/r/robotics/comments/1r1c87b/rc_sumo_bots/)**

Hello! Our makerspace for kids 11-18 is hosting a three week summer camp this summer. Most of the kids will likely be 11-13 who come. The kids we know will come have indicated they would like to build and program sumo bots. The kids will have wide varieties of experience. Some will have no coding experience at all, so I am thinking rather than autonomous sumo bots they should make remote controlled ones. Which I realize now makes them not robots so maybe y'all can't help. We have here several Creality HI 3d printers and a large Omtech laser, as well as basic woodshop and electronics things like soldering irons and breadboards and all kinds of electronical bits and bobs. I am thinking if we have a premade chassis that the kids can add on to, they still get to design stuff and print it or cut it out but the basics are already there, then they can do the electronics and whatever coding needs to go between the rc stuff and the electronics and maybe they can conceivably do all that in 15 days/three weeks? I think trying to make it autonomous will be too challenging for all, but we can always suggest/challenge the kids who are good coders already to do so. Have any of y'all done something like this? Does it seem feasible? Thanks!

1h ago

---

**[Design process advice for robotic arm](https://www.reddit.com/r/robotics/comments/1r1c3ce/design_process_advice_for_robotic_arm/)**

1h ago

---

**[Opensource IoT/Robotics ESP32 Controller](https://www.reddit.com/r/robotics/comments/1r19o5v/opensource_iotrobotics_esp32_controller/)**

Board I designed a custom board called ESP PowerDeck, based on the ESP32-S3. It’s meant for experimenting with robotics and IoT where you need real power handling, not just a breadboard setup. Would love feedback from the community — especially on features that might make it more useful for robotics work. (edit moved photo up so it could be seen ;p)

3h ago

---

**[Yet another Onshape robot exporter, but this one (hopefully) saves your API credits.](https://www.reddit.com/r/robotics/comments/1r18zed/yet_another_onshape_robot_exporter_but_this_one/)**

3h ago

---

**[OEM LiDAR](https://www.reddit.com/r/robotics/comments/1r17mgn/oem_lidar/)**

Hello guys A quick question am looking for OEM 2D lidar Sensor I want to flash them and deploy my own software into it. Where can I get such lidar sensor? Let me know if you know any vendors or any websites where can I buy.

4h ago

---

**[We trained a VLA model on 20,000 hours of real robot data across 9 embodiments, then tested it on 100 tasks. Here's what actually worked and what didn't.](https://www.reddit.com/r/robotics/comments/1r0au80/we_trained_a_vla_model_on_20000_hours_of_real/)**

Over the past year our team built LingBot-VLA, a Vision-Language-Action foundation model for dual-arm manipulation. We just released everything: code, base model, and benchmark data (paper: arXiv:2601.18692, code: github.com/robbyant/lingbot-vla, weights on HuggingFace). I wanted to share what we learned deploying this across real hardware because the results tell an honest and, I think, useful story for anyone working on generalist robot policies. The setup: ~20,000 hours of teleoperated manipulation data from 9 mainstream dual-arm configs (Agibot G1, AgileX, Galaxea R1Pro, Realman, Leju KUAVO, and others). We evaluated on 3 physical platforms, 100 tasks each, 130 post-training demos per task, 15 trials per task per model. That's 22,500 total real-world trials comparing us against π0.5, GR00T N1.6, and WALL-OSS under identical conditions. The honest numbers: our best variant (with depth distillation) hit 17.30% average success rate and 35.41% progress score across all 300 task-platform pairs. π0.5 got 13.02% SR / 27.65% PS. WALL-OSS landed at 4.05% SR. Before anyone says "17% is low," I want to contextualize this. These are 100 diverse bimanual tasks, many requiring multi-step fine-grained manipulation (cleaning tableware, stacking, arranging objects), tested across three physically different robots. Some individual tasks hit 80%+ SR, others are near zero. Real-world bimanual manipulation across this breadth of tasks is genuinely hard, and I think the field benefits from reporting these numbers honestly rather than cherry-picking the best 5 tasks for a demo reel. What actually worked well: Scaling laws are real and not saturating. We ran a systematic study scaling pre-training data from 3K to 6K to 13K to 18K to 20K hours. Success rates climbed consistently across all three platforms with no sign of plateau at 20K. This was the most exciting finding for us because it suggests the path forward is clear: more diverse, high-quality real-world data keeps helping. Depth distillation made a meaningful difference. We use learnable queries aligned with depth embeddings from our LingBot-Depth model via cross-attention. This bumped average SR from 15.74% to 17.30% in real-world and from 85.34% to 86.68% in randomized simulation scenes. The gain was most visible on transparent object manipulation (glass vases, clear containers) where RGB alone struggles. Data-efficient adaptation. With only 80 demos per task, LingBot-VLA outperformed π0.5 trained on the full 130 demos, in both SR and progress score. The gap widened as we added more post-training data, which suggests the pre-training is providing genuinely useful priors rather than just memorizing. Training efficiency. We built a custom codebase with FSDP2, mixed-precision, FlexAttention, and operator fusion via torch.compile. On 8 GPUs we get 261 samples/sec/GPU for the Qwen2.5-VL-3B backbone, which is 1.5x to 2.8x faster than StarVLA, Dexbotic, and OpenPI depending on the VLM. Scaling to 256 GPUs tracks near-linear throughput. This matters practically because iterating on 20K hours of data is brutal without an efficient pipeline. What didn't work or remains unsolved: Plenty of tasks are still near 0% SR across all models. Tasks requiring very precise spatial reasoning in cluttered scenes, long-horizon multi-step sequences, or unusual object geometries remain extremely challenging. The depth distillation helps but doesn't solve spatial reasoning completely. Also, the model currently only covers dual-arm tabletop manipulation. Single-arm, mobile manipulation, and non-tabletop scenarios are future work. The architecture uses a Mixture-of-Transformers design (similar to BAGEL) where the VLM and action expert share self-attention but have separate feedforward pathways. Action generation uses flow matching with 50-step action chunks. We found the shared attention critical for letting semantic understanding guide action prediction without the modalities interfering with each other's representations. One thing I'd love to hear from this community: for those of you working with real dual-arm setups, what task categories do you find most important for practical deployment? Our GM-100 benchmark covers 100 tasks but we're always thinking about what's missing. Also curious if anyone has experimented with alternative spatial representations beyond depth for VLA models. All code, model weights, and the benchmark data are public. We wanted to make sure anyone can reproduce these results and build on them.

1d ago

---

**[Building a robot](https://www.reddit.com/r/robotics/comments/1r0len2/building_a_robot/)**

Hi guys! Im 17 and Have NO prior experience to ths. As you can see in the caption, i wanna build a robot. Its Supposed to be a Mining robot, one they could perhaps use instead of Human workers in very Dangerous Enviroments (Deadly Gasses in the Mine or Radioactive material or similar stuff.) Im Currently still drawing the blueprint. Its more jst a suggestion currently but anyways. (I will attach a picture of the current status, most of it will probably Change, also sorry if the handwriting is bad). So. My rough ideas: it will use something like tank tracks to move around (in drawing too). Because its easier to maintain than legs, cheaper and less complicated. Im still somewhat stuck on the arms, where they meet the upper hull i will probably use an electric servo motor so its more detailed, the arms themselves will probably use hydraulics because they are POWAH (as far as i know). Which in this case is very much needed. At the peak of the arm (where normally hands are) i wanna make a motor slot, so you can easily take out motors and/or change them according to tbe tool (Drill or Hammer for example). Im thinking of maybe screwing it in or using a few screws to hold it in, for easy maintenance. I have not yet though about how its gonna see around (head) or what its upper body would look like yet. As for energy supply?..probably changeable batteries (big ones) so you dont have to charge it, and can more or less let it continously work. Would you guys have any idea what could be changed on the CURRENT design?

21h ago

---

---

## Google News: "robotics"

**[Haply Robotics raises $16 million to build the “steering wheels” for physical AI](https://betakit.com/haply-robotics-raises-16-million-to-build-the-steering-wheels-for-physical-ai/)**

How the Montréal startup plans to own the touch layer of robotics.

BetaKit • 1d ago

---

**[China's Alibaba launches AI model to power robots as tech giants talk up 'physical AI'](https://www.cnbc.com/2026/02/10/alibaba-ai-model-robotics-rynnbrain-china.html)**

Nvidia and Google are among a handful of major tech giants developing models for robotics and so-called "phyiscal AI."

CNBC • 11h ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://www.bloomberg.com/news/articles/2026-02-10/alibaba-pushes-into-robotics-ai-with-open-source-rynnbrain)**

Bloomberg.com • 15h ago

---

**[New ‘RynnBrain’ Lifts Alibaba Stock (BABA) as It Enters Robotics AI Race With Nvidia and Google](https://www.tipranks.com/news/new-rynnbrain-lifts-alibaba-stock-baba-as-it-enters-robotics-ai-race-with-nvidia-and-google)**

Alibaba ($BABA) is broadening its AI strategy with a new robotics-focused project. The Chinese e-commerce giant introduced a new AI system called “RynnBrain,” desig...

TipRanks • 11h ago

---

**[Elon Musk warns the U.S. is '1,000% going to go bankrupt' unless AI and robotics save the economy from crushing debt](https://fortune.com/2026/02/07/elon-musk-us-bankruptcy-ai-robotics-economic-growth-national-debt-crisis/)**

"We just need enough time to build the AI and robots to not go bankrupt before then."

Fortune • 3d ago

---

**[AI In Robotics - New Position Paper](https://ifr.org/ifr-press-releases/news/ai-in-robotics-new-position-paper)**

A new generation of AI-powered robots moving from research labs into the real world is fueled by AI tech companies and analysts forecasting a multitrillion-dollar market. The vision is to give artificial intelligence its own robot body. What are the trends, challenges, and commercial applications?

IFR International Federation of Robotics • 15h ago

---

**[Exclusive: Trener Robotics raises $32M to scale AI robot skills](https://www.axios.com/pro/all-deals/2026/02/10/trener-robotics-32m-ai-robot-skills)**

Robotics funding rebounded in 2025.

Axios • 9h ago

---

**[The Autonomous Robotics Stock Wall Street Insiders Are Quietly Buying (Hint: It's Not Tesla)](https://finance.yahoo.com/news/autonomous-robotics-stock-wall-street-195000880.html)**

This high-flying stock is about more than just military drones.

Yahoo Finance • 2d ago

---

**[Humanoid robots are getting smaller, safer and closer](https://www.foxnews.com/tech/humanoid-robots-getting-smaller-safer-closer)**

Fauna Robotics is launching Sprout as a developer platform for humanoid robots. The robot features 29 degrees of freedom and NVIDIA compute power.

Fox News • 4h ago

---

**[Why This VC Says AI and Robotics Will Put Every Human Job at Risk](https://www.wsj.com/video/series/wsj-take-on-the-week/why-this-vc-says-ai-and-robotics-will-put-every-human-job-at-risk/546BD698-2E82-484A-8364-61B5B20A66E4?gaa_at=eafs&gaa_n=AWEtsqc0ek-MEoT0O09ba0Mt38onPLBK4IQgyWdumwNU-d14QvJjYdEV1k_8&gaa_ts=698ba24a&gaa_sig=9Ye43EFAXqbnX4hbSVc2GUMlYnQ4Q8kZFRCBNLsYgVuLpfC30qZqm1NSYE2uC43pgrViPvwsbof3U59UGF_paw%3D%3D)**

The Wall Street Journal • 2d ago

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

👁️ 12K • 👍 284 • 💬 56 • ⏱️ 1:25 • 21h ago

---

**[How They&#39;re Building Robot Hands Like Human Muscles #robotics #innovation #engineering](https://www.youtube.com/watch?v=zcbY5VW4BYc)**

A Hungarian startup is generating buzz with its automated manufacturing system for building robots that's straight out of Westworld ...

📺 Kalil 4.0

👁️ 423 • 👍 14 • ⏱️ 0:45 • 1h ago

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

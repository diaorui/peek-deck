---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-09T18:11:05.910399+00:00'
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

**Last Updated:** February 09, 2026 at 18:11 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[We trained a VLA model on 20,000 hours of real robot data across 9 embodiments, then tested it on 100 tasks. Here's what actually worked and what didn't.](https://www.reddit.com/r/robotics/comments/1r0au80/we_trained_a_vla_model_on_20000_hours_of_real/)**

Over the past year our team built LingBot-VLA, a Vision-Language-Action foundation model for dual-arm manipulation. We just released everything: code, base model, and benchmark data (paper: arXiv:2601.18692, code: github.com/robbyant/lingbot-vla, weights on HuggingFace). I wanted to share what we learned deploying this across real hardware because the results tell an honest and, I think, useful story for anyone working on generalist robot policies. The setup: ~20,000 hours of teleoperated manipulation data from 9 mainstream dual-arm configs (Agibot G1, AgileX, Galaxea R1Pro, Realman, Leju KUAVO, and others). We evaluated on 3 physical platforms, 100 tasks each, 130 post-training demos per task, 15 trials per task per model. That's 22,500 total real-world trials comparing us against π0.5, GR00T N1.6, and WALL-OSS under identical conditions. The honest numbers: our best variant (with depth distillation) hit 17.30% average success rate and 35.41% progress score across all 300 task-platform pairs. π0.5 got 13.02% SR / 27.65% PS. WALL-OSS landed at 4.05% SR. Before anyone says "17% is low," I want to contextualize this. These are 100 diverse bimanual tasks, many requiring multi-step fine-grained manipulation (cleaning tableware, stacking, arranging objects), tested across three physically different robots. Some individual tasks hit 80%+ SR, others are near zero. Real-world bimanual manipulation across this breadth of tasks is genuinely hard, and I think the field benefits from reporting these numbers honestly rather than cherry-picking the best 5 tasks for a demo reel. What actually worked well: Scaling laws are real and not saturating. We ran a systematic study scaling pre-training data from 3K to 6K to 13K to 18K to 20K hours. Success rates climbed consistently across all three platforms with no sign of plateau at 20K. This was the most exciting finding for us because it suggests the path forward is clear: more diverse, high-quality real-world data keeps helping. Depth distillation made a meaningful difference. We use learnable queries aligned with depth embeddings from our LingBot-Depth model via cross-attention. This bumped average SR from 15.74% to 17.30% in real-world and from 85.34% to 86.68% in randomized simulation scenes. The gain was most visible on transparent object manipulation (glass vases, clear containers) where RGB alone struggles. Data-efficient adaptation. With only 80 demos per task, LingBot-VLA outperformed π0.5 trained on the full 130 demos, in both SR and progress score. The gap widened as we added more post-training data, which suggests the pre-training is providing genuinely useful priors rather than just memorizing. Training efficiency. We built a custom codebase with FSDP2, mixed-precision, FlexAttention, and operator fusion via torch.compile. On 8 GPUs we get 261 samples/sec/GPU for the Qwen2.5-VL-3B backbone, which is 1.5x to 2.8x faster than StarVLA, Dexbotic, and OpenPI depending on the VLM. Scaling to 256 GPUs tracks near-linear throughput. This matters practically because iterating on 20K hours of data is brutal without an efficient pipeline. What didn't work or remains unsolved: Plenty of tasks are still near 0% SR across all models. Tasks requiring very precise spatial reasoning in cluttered scenes, long-horizon multi-step sequences, or unusual object geometries remain extremely challenging. The depth distillation helps but doesn't solve spatial reasoning completely. Also, the model currently only covers dual-arm tabletop manipulation. Single-arm, mobile manipulation, and non-tabletop scenarios are future work. The architecture uses a Mixture-of-Transformers design (similar to BAGEL) where the VLM and action expert share self-attention but have separate feedforward pathways. Action generation uses flow matching with 50-step action chunks. We found the shared attention critical for letting semantic understanding guide action prediction without the modalities interfering with each other's representations. One thing I'd love to hear from this community: for those of you working with real dual-arm setups, what task categories do you find most important for practical deployment? Our GM-100 benchmark covers 100 tasks but we're always thinking about what's missing. Also curious if anyone has experimented with alternative spatial representations beyond depth for VLA models. All code, model weights, and the benchmark data are public. We wanted to make sure anyone can reproduce these results and build on them.

29m ago

---

**[Robot](https://www.reddit.com/r/robotics/comments/1qzw7nc/robot/)**

12h ago

---

**[Brian Gerkey on open source and commercialization](https://www.reddit.com/r/robotics/comments/1r08txo/brian_gerkey_on_open_source_and_commercialization/)**

When asked about tension around open source in robotics, Brian Gerkey, CTO of Intrinsic, pushes back on the idea that it was ever a problem. His point is that open source was designed from the start to be used by industry, not kept separate from it. Permissive licensing was intentional. Companies were meant to take the software, ship products with it, and build businesses on top, without being forced to contribute back. From that perspective, corporate involvement isn’t a betrayal of open source. What matters is whether the software stays open, maintained, and widely usable over time, not who adopts it or commercializes it.

1h ago

---

**[Lego strandbeest (Part 1)](https://www.reddit.com/r/robotics/comments/1r09da6/lego_strandbeest_part_1/)**

1h ago

---

**[Autonomous Navigation in Dynamic Environments as a Persistent Robotics Challenge](https://www.reddit.com/r/robotics/comments/1r087bz/autonomous_navigation_in_dynamic_environments_as/)**

🔗 [gazetemakina.com](https://gazetemakina.com/en/dinamik-robotik/) • 2h ago

---

**[G1 kicks mother and child when performing](https://www.reddit.com/r/robotics/comments/1r0awur/g1_kicks_mother_and_child_when_performing/)**

26m ago

---

**[Distance measuring sensor](https://www.reddit.com/r/robotics/comments/1r03rwp/distance_measuring_sensor/)**

Hi everyone I've stumbled across this sub reddit while searching for some kind of distance measuring sensor. Edit: i need it for 15 meters up to i need it for a school project so a cheaper would be good enough. accuracy is not too important because up to 5cm accuracy is already good enough for me and I need it outdoors. i have found one for cheap but I'm interested in your opinion's too.

5h ago

---

**[LeRobot's ACT running on my robotic arm](https://www.reddit.com/r/robotics/comments/1qz65ru/lerobots_act_running_on_my_robotic_arm/)**

1d ago

---

**[Is Tesla a Buy?](https://www.reddit.com/r/robotics/comments/1r0bbpm/is_tesla_a_buy/)**

12m ago

---

**[Everbot Demo: Home gym bot, Factory QA, Fitness and AirBnb App](https://www.reddit.com/r/robotics/comments/1qzt9y0/everbot_demo_home_gym_bot_factory_qa_fitness_and/)**

14h ago

---

---

## Google News: "robotics"

**[Stryker introduces Mako Handheld Robotics with the limited market release of Mako RPS](https://finance.yahoo.com/news/stryker-introduces-mako-handheld-robotics-152900144.html)**

Stryker (NYSE: SYK), a global leader in medical technologies, announced the limited market release of Mako RPS (Robotic Power System) for Total Knee, an intuitive handheld robotic system that combines Stryker's proven robotics and power tool legacies and represents Mako's expansion into a new robotics platform. Mako now includes Mako SmartRobotics™ – Stryker's multi-specialty, robotic-arm assisted platform featuring Mako 4 – and Mako Handheld Robotics with Mako RPS, which is designed to reach a

Yahoo Finance • 2h ago

---

**[Flipping the script: How ‘upside-down’ AutoPallet robots solve palletizing density](https://www.therobotreport.com/flipping-autopalleet-script-how-upside-down-autopallet-robots-solve-palletizing-density/)**

AutoPallet debuts magnetic, ceiling-mounted AMRs at Manifest 2026, providing high-density palletizing through a suspended swarm architecture.

The Robot Report • 4h ago

---

**[Machine Vision Systems (MVS) Research Report 2026: Rising Demand for Zero-Defect Manufacturing and Increasing Adoption of Vision-Guided Robotics - Market Trends, Statistics, Growth Forecasts 2025-2031](https://uk.finance.yahoo.com/news/machine-vision-systems-mvs-research-140000658.html)**

Yahoo Finance UK • 4h ago

---

**[Elon Musk warns the U.S. is '1,000% going to go bankrupt' unless AI and robotics save the economy from crushing debt](https://fortune.com/2026/02/07/elon-musk-us-bankruptcy-ai-robotics-economic-growth-national-debt-crisis/)**

"We just need enough time to build the AI and robots to not go bankrupt before then."

Fortune • 1d ago

---

**[Robots for daily life: Mint and Rice Robotics plan HK$10M AI venture](https://www.stocktitan.net/news/MIMI/mint-signed-mo-u-with-robotics-leader-rice-robotics-to-pioneer-1ae1uax2xl9b.html)**

HK$10M JV MoU targets localized robotics R&D in Hong Kong, combining Mint’s Southeast Asia reach with Rice Robotics’ Japan presence around 'physical AI'.

stocktitan.net • 5h ago

---

**[Tesla's Robotics Revolution Won't Save It (NASDAQ:TSLA)](https://seekingalpha.com/article/4867567-teslas-robotics-revolution-would-not-save-it)**

Seeking Alpha • 11h ago

---

**[China Is Going All-In to Beat the U.S. on Humanoid Robots](https://www.wsj.com/tech/china-is-going-all-in-to-beat-the-u-s-on-humanoid-robots-b9c434d2?gaa_at=eafs&gaa_n=AWEtsqdsVT-GxeGJCOmwI3e08cx49C0z4ttVNoM1TGyvX8jPGaGofr-uRb2j&gaa_ts=698a26a1&gaa_sig=V2e8FqYNCRnqFXa23bwp-InCPaQGR5Tn9ED6EFl86bWKf67xFTWHDrQaP_zZm3klTcyhTXnN2RgFcWLW9gmNXQ%3D%3D)**

The Wall Street Journal • 2d ago

---

**[The Autonomous Robotics Stock Wall Street Insiders Are Quietly Buying (Hint: It's Not Tesla)](https://www.fool.com/investing/2026/02/08/the-autonomous-robotics-stock-wall-street-insiders/)**

This high-flying stock is about more than just military drones.

The Motley Fool • 22h ago

---

**[Swarmbotics Wins US Army Contract for Swarming Ground Robots](https://thedefensepost.com/2026/02/09/swarmbotics-us-army/)**

Swarmbotics AI has won a US Army contract to build swarming, attritable small unmanned ground vehicles for the 1st Cavalry Division.

The Defense Post • 9h ago

---

**[Convenient ordering option or ‘sidewalk hog’? Food delivery robots get mixed reception in Chicago.](https://www.chicagotribune.com/2026/02/09/food-delivery-robots-safety-chicago/)**

Robotic food delivery carts are now a familiar sight on the streets of Chicago. But not everyone has rolled out the welcome wagon for the army of AI-driven meals on wheels.

Chicago Tribune • 7h ago

---

---

## YouTube Videos: "robotics"

**[Atlas Airborne Robot Shows the Final Evolution of Boston Dynamics](https://www.youtube.com/watch?v=IjRjKwZhYCQ)**

The Atlas Airborne Robot takes one final research run as Boston Dynamics pushes humanoid robot control to its absolute limit.

📺 DPCcars

👁️ 52K • 👍 377 • 💬 70 • ⏱️ 2:45 • 1d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 780K • 👍 30K • 💬 3K • ⏱️ 1:38 • 2d ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 230K • 👍 4K • 💬 910 • ⏱️ 13:31 • 4d ago

---

**[Elon Musk on Why Everyone Will Want an Optimus Robot by 2027](https://www.youtube.com/watch?v=dWRqUdVBKjE)**

Will a robot soon be watching your children or caring for your parents? Elon Musk predicts a future where billions of humanoid ...

📺 SpaceTakers

👁️ 36K • 👍 750 • 💬 71 • ⏱️ 0:29 • 3d ago

---

**[Tony Stark would hate this! 😂 #engineering #ironman #revrobotics #3dprinting](https://www.youtube.com/watch?v=13fah4TQXhw)**

📺 Concept Bytes

👁️ 28K • 👍 2K • 💬 33 • ⏱️ 1:24 • 3d ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 27K • 👍 456 • 💬 12 • ⏱️ 0:19 • 1d ago

---

**[Tesla Robot handles upside down popcorn. It’s crazy how much these will change everything.](https://www.youtube.com/watch?v=PlEGwoJmon8)**

📺 Tesla Owners Silicon Valley

👁️ 173K • 👍 3K • 💬 157 • ⏱️ 0:40 • 3d ago

---

**[The world of robotics is advancing](https://www.youtube.com/watch?v=O-IPeboeXGI)**

📺 Fredo on TV

👁️ 199K • 👍 20K • 💬 546 • ⏱️ 0:34 • 1d ago

---

**[헬로카봇 빅포트 탱크 변신 합체 모음 Hello Carbot Robot Toys Transformation](https://www.youtube.com/watch?v=JL45MHCxjvw)**

헬로카봇 빅포트 탱크 변신 합체 모음 Hello Carbot Robot Toys Transformation 헬로카봇 용사 시즌2 첫 메카는 강력한 탱크 빅포트 빅 ...

📺 Rainbow Play

👁️ 3K • 👍 38 • 💬 14 • ⏱️ 6:57 • 10h ago

---

**[Robots That Move Without a Brain? Sea Star Locomotion Is Changing Robotics Forever #robot #shorts](https://www.youtube.com/watch?v=Q7doiqBMz-k)**

Robots That Move Without a Brain? Sea Star Locomotion Is Changing Robotics Forever What if robots could keep moving even ...

📺 Future Lens Pi

👁️ 28K • 💬 10 • ⏱️ 0:08 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

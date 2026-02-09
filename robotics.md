---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-09T23:38:29.678282+00:00'
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

**Last Updated:** February 09, 2026 at 23:38 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[G1 kicks mother and child when performing](https://www.reddit.com/r/robotics/comments/1r0awur/g1_kicks_mother_and_child_when_performing/)**

5h ago

---

**[We trained a VLA model on 20,000 hours of real robot data across 9 embodiments, then tested it on 100 tasks. Here's what actually worked and what didn't.](https://www.reddit.com/r/robotics/comments/1r0au80/we_trained_a_vla_model_on_20000_hours_of_real/)**

Over the past year our team built LingBot-VLA, a Vision-Language-Action foundation model for dual-arm manipulation. We just released everything: code, base model, and benchmark data (paper: arXiv:2601.18692, code: github.com/robbyant/lingbot-vla, weights on HuggingFace). I wanted to share what we learned deploying this across real hardware because the results tell an honest and, I think, useful story for anyone working on generalist robot policies. The setup: ~20,000 hours of teleoperated manipulation data from 9 mainstream dual-arm configs (Agibot G1, AgileX, Galaxea R1Pro, Realman, Leju KUAVO, and others). We evaluated on 3 physical platforms, 100 tasks each, 130 post-training demos per task, 15 trials per task per model. That's 22,500 total real-world trials comparing us against π0.5, GR00T N1.6, and WALL-OSS under identical conditions. The honest numbers: our best variant (with depth distillation) hit 17.30% average success rate and 35.41% progress score across all 300 task-platform pairs. π0.5 got 13.02% SR / 27.65% PS. WALL-OSS landed at 4.05% SR. Before anyone says "17% is low," I want to contextualize this. These are 100 diverse bimanual tasks, many requiring multi-step fine-grained manipulation (cleaning tableware, stacking, arranging objects), tested across three physically different robots. Some individual tasks hit 80%+ SR, others are near zero. Real-world bimanual manipulation across this breadth of tasks is genuinely hard, and I think the field benefits from reporting these numbers honestly rather than cherry-picking the best 5 tasks for a demo reel. What actually worked well: Scaling laws are real and not saturating. We ran a systematic study scaling pre-training data from 3K to 6K to 13K to 18K to 20K hours. Success rates climbed consistently across all three platforms with no sign of plateau at 20K. This was the most exciting finding for us because it suggests the path forward is clear: more diverse, high-quality real-world data keeps helping. Depth distillation made a meaningful difference. We use learnable queries aligned with depth embeddings from our LingBot-Depth model via cross-attention. This bumped average SR from 15.74% to 17.30% in real-world and from 85.34% to 86.68% in randomized simulation scenes. The gain was most visible on transparent object manipulation (glass vases, clear containers) where RGB alone struggles. Data-efficient adaptation. With only 80 demos per task, LingBot-VLA outperformed π0.5 trained on the full 130 demos, in both SR and progress score. The gap widened as we added more post-training data, which suggests the pre-training is providing genuinely useful priors rather than just memorizing. Training efficiency. We built a custom codebase with FSDP2, mixed-precision, FlexAttention, and operator fusion via torch.compile. On 8 GPUs we get 261 samples/sec/GPU for the Qwen2.5-VL-3B backbone, which is 1.5x to 2.8x faster than StarVLA, Dexbotic, and OpenPI depending on the VLM. Scaling to 256 GPUs tracks near-linear throughput. This matters practically because iterating on 20K hours of data is brutal without an efficient pipeline. What didn't work or remains unsolved: Plenty of tasks are still near 0% SR across all models. Tasks requiring very precise spatial reasoning in cluttered scenes, long-horizon multi-step sequences, or unusual object geometries remain extremely challenging. The depth distillation helps but doesn't solve spatial reasoning completely. Also, the model currently only covers dual-arm tabletop manipulation. Single-arm, mobile manipulation, and non-tabletop scenarios are future work. The architecture uses a Mixture-of-Transformers design (similar to BAGEL) where the VLM and action expert share self-attention but have separate feedforward pathways. Action generation uses flow matching with 50-step action chunks. We found the shared attention critical for letting semantic understanding guide action prediction without the modalities interfering with each other's representations. One thing I'd love to hear from this community: for those of you working with real dual-arm setups, what task categories do you find most important for practical deployment? Our GM-100 benchmark covers 100 tasks but we're always thinking about what's missing. Also curious if anyone has experimented with alternative spatial representations beyond depth for VLA models. All code, model weights, and the benchmark data are public. We wanted to make sure anyone can reproduce these results and build on them.

5h ago

---

**[Lego strandbeest (Part 1)](https://www.reddit.com/r/robotics/comments/1r09da6/lego_strandbeest_part_1/)**

6h ago

---

**[Robot](https://www.reddit.com/r/robotics/comments/1qzw7nc/robot/)**

17h ago

---

**[Brian Gerkey on open source and commercialization](https://www.reddit.com/r/robotics/comments/1r08txo/brian_gerkey_on_open_source_and_commercialization/)**

When asked about tension around open source in robotics, Brian Gerkey, CTO of Intrinsic, pushes back on the idea that it was ever a problem. His point is that open source was designed from the start to be used by industry, not kept separate from it. Permissive licensing was intentional. Companies were meant to take the software, ship products with it, and build businesses on top, without being forced to contribute back. From that perspective, corporate involvement isn’t a betrayal of open source. What matters is whether the software stays open, maintained, and widely usable over time, not who adopts it or commercializes it.

7h ago

---

**[Built a browser-based teleoperation platform for quadrupeds, and drones. Looking for beta testers to try remote piloting](https://www.reddit.com/r/robotics/comments/1r0cib6/built_a_browserbased_teleoperation_platform_for/)**

https://preview.redd.it/lrhwvdgtjiig1.png?width=2880&format=png&auto=webp&s=8bd95c1e3352d027ab5574c0b9e17850b45186b3 Hey r/robotics, I've been working on a teleoperation platform that lets you control robots remotely through a browser with low-latency video (~150ms). Currently testing with a Unitree Go2 EDU Plus XT16. The setup: - WebRTC video/audio streaming from the robot - Real-time controls via WebSocket - HUD overlay with telemetry (battery, signal, heading) - Works on laptop/desktop with Chrome, Brave, and safari. - Mobile Bonding System I'm looking for a few people to beta test the pilot experience and give feedback on: - Control responsiveness - Video quality/latency - UI/UX of the operator interface - What features you'd want to see No hardware needed on your end , you'd be remotely controlling an actual robot in my lab. If you're interested, drop a comment or DM with: - Your timezone - Any relevant background (gaming, drones, robotics, etc - not required) - What interests you about remote robot operation Happy to answer questions about the technical stack too (WebRTC, Janus, aiortc, etc). Thanks!

4h ago

---

**[Realsense D455f: Drone-to-drone distancing](https://www.reddit.com/r/robotics/comments/1r0k8z0/realsense_d455f_dronetodrone_distancing/)**

Hello, I can't find any information on this online anywhere. But I am considering purchasing the D455f for my Orin Nano to do drone-to-drone ranging for formation. In my specific case, I wish to ensure that a drone (Mavic-like) "in front" of my drone (the ego) is 5m +/- 1xcm or less away. I will use YOLOv11 to determine the bounding box of which pixels the drones occupy and then take the median range of this. The thing is, that the drones will be flown outside in mostly clear conditions and high up enough that the sky would in many cases be the background. I was wondering if anyone has footage of such or a similar scenario they can share? Or whether they can estimate how accurate the depth map of the D455f will be in such conditions? I just need to know whether the median (or a smarter algorithm) will let me reliably say whether the drone is about 5m away. 4m is also okay, worst case. I am not looking for suggestions into the underlying aim, but specifically related to the viability of utilizing D455f.

12m ago

---

**[North American robot orders rose again in 2025, driven mostly by non-automotive industries](https://www.reddit.com/r/robotics/comments/1r0iyy9/north_american_robot_orders_rose_again_in_2025/)**

New industry data shows robot orders in North America increased in 2025, reaching 36,766 units worth $2.25B, up 6.6% in units and 10.1% in revenue compared to 2024. Food and consumer goods, semiconductors and electronics, and life sciences accounted for the majority of orders. Automotive suppliers lagged 2024 levels, but OEM activity picked up later in the year. Q4 was the strongest quarter with 10,325 robots ordered in Q4 alone, marking the sixth straight quarter of year-over-year growth and the highest annual total since 2022. Cobots made up 28.6% of Q4 units and nearly 20% of all robots ordered in 2025, with their highest quarterly volume since being tracked as a separate category.

🔗 [Automate](https://www.automate.org/robotics/news/robot-orders-grow-6-6-in-2025-as-general-industries-drive-broader-automation-adoption) • 1h ago

---

**[Autonomous Navigation in Dynamic Environments as a Persistent Robotics Challenge](https://www.reddit.com/r/robotics/comments/1r087bz/autonomous_navigation_in_dynamic_environments_as/)**

🔗 [gazetemakina.com](https://gazetemakina.com/en/dinamik-robotik/) • 7h ago

---

**[LeRobot's ACT running on my robotic arm](https://www.reddit.com/r/robotics/comments/1qz65ru/lerobots_act_running_on_my_robotic_arm/)**

1d ago

---

---

## Google News: "robotics"

**[Haply Robotics raises $16 million to build the “steering wheels” for physical AI](https://betakit.com/haply-robotics-raises-16-million-to-build-the-steering-wheels-for-physical-ai/)**

How the Montréal startup plans to own the touch layer of robotics.

BetaKit • 7h ago

---

**[Tesla Retools For Robotics And AI As Rich Valuation Faces Test](https://finance.yahoo.com/news/tesla-retools-robotics-ai-rich-221526827.html)**

Tesla (NasdaqGS:TSLA) is shifting resources away from its Model S and X lines to prepare production capacity for its humanoid robot program, Optimus. The company is increasing U.S. solar cell manufacturing as part of Elon Musk's 100-gigawatt energy vision. Tesla is directing more investment toward AI and robotics infrastructure across its operations. Market speculation is growing around a potential merger between Tesla, SpaceX and/or xAI that could create a combined AI and robotics...

Yahoo Finance • 1h ago

---

**[Elon Musk warns the U.S. is '1,000% going to go bankrupt' unless AI and robotics save the economy from crushing debt](https://fortune.com/2026/02/07/elon-musk-us-bankruptcy-ai-robotics-economic-growth-national-debt-crisis/)**

"We just need enough time to build the AI and robots to not go bankrupt before then."

Fortune • 2d ago

---

**[China Is Going All-In to Beat the U.S. on Humanoid Robots](https://www.wsj.com/tech/china-is-going-all-in-to-beat-the-u-s-on-humanoid-robots-b9c434d2?gaa_at=eafs&gaa_n=AWEtsqfrptzlpm9S-nzEx138UYMshI_dFVo7Izib8e6A1fEhKuZGon7G1-YE&gaa_ts=698a735d&gaa_sig=Q4_bxO2PLjbcvycLOqSDdLY64YljkE_x_-Mi5yAybxFEh0ydP-pt8pPktgCIxjUiYnRdugPOMVthPlqKwfYsDQ%3D%3D)**

The Wall Street Journal • 2d ago

---

**[China: Humanoid robots perform kung fu moves with Shaolin monks in a viral video](https://interestingengineering.com/ai-robotics/humanoid-robots-kung-fu-with-shaolin-monks)**

A group of humanoid robots made by Agibot performed kung fu moves at the Shaolin Temple in China, captivating viewers with their capabilities.

Interesting Engineering • 12h ago

---

**[The Rapid Rise of Humanoid Robots](https://oilprice.com/Energy/Energy-General/The-Rapid-Rise-of-Humanoid-Robots.html)**

Automakers including Tesla and Hyundai are investing heavily in humanoid robots as a long-term cost-saving strategy, even as questions remain over productivity, technical feasibility, and the risk of widespread job losses.

Crude Oil Prices Today | OilPrice.com • 2d ago

---

**[Tesla's Robotics Revolution Won't Save It (NASDAQ:TSLA)](https://seekingalpha.com/article/4867567-teslas-robotics-revolution-would-not-save-it)**

Seeking Alpha • 16h ago

---

**[Insect-inspired adaptive behavioral compensation strategy against olfactory sensory deficiency for robotic odor source localization](https://www.nature.com/articles/s44182-026-00080-5)**

npj Robotics - Insect-inspired adaptive behavioral compensation strategy against olfactory sensory deficiency for robotic odor source localization

Nature • 8m ago

---

**[Robots for daily life: Mint and Rice Robotics plan HK$10M AI venture](https://www.stocktitan.net/news/MIMI/mint-signed-mo-u-with-robotics-leader-rice-robotics-to-pioneer-1ae1uax2xl9b.html)**

HK$10M JV MoU targets localized robotics R&D in Hong Kong, combining Mint’s Southeast Asia reach with Rice Robotics’ Japan presence around 'physical AI'.

stocktitan.net • 10h ago

---

**[Swarmbotics Wins US Army Contract for Swarming Ground Robots](https://thedefensepost.com/2026/02/09/swarmbotics-us-army/)**

Swarmbotics AI has won a US Army contract to build swarming, attritable small unmanned ground vehicles for the 1st Cavalry Division.

The Defense Post • 15h ago

---

---

## YouTube Videos: "robotics"

**[Atlas Airborne Robot Shows the Final Evolution of Boston Dynamics](https://www.youtube.com/watch?v=IjRjKwZhYCQ)**

The Atlas Airborne Robot takes one final research run as Boston Dynamics pushes humanoid robot control to its absolute limit.

📺 DPCcars

👁️ 61K • 👍 411 • 💬 76 • ⏱️ 2:45 • 2d ago

---

**[Elon Musk on Why Everyone Will Want an Optimus Robot by 2027](https://www.youtube.com/watch?v=dWRqUdVBKjE)**

Will a robot soon be watching your children or caring for your parents? Elon Musk predicts a future where billions of humanoid ...

📺 SpaceTakers

👁️ 39K • 👍 782 • 💬 72 • ⏱️ 0:29 • 4d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 872K • 👍 33K • 💬 3K • ⏱️ 1:38 • 2d ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 234K • 👍 4K • 💬 918 • ⏱️ 13:31 • 5d ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 27K • 👍 451 • 💬 12 • ⏱️ 0:19 • 1d ago

---

**[Tony Stark would hate this! 😂 #engineering #ironman #revrobotics #3dprinting](https://www.youtube.com/watch?v=13fah4TQXhw)**

📺 Concept Bytes

👁️ 29K • 👍 2K • 💬 34 • ⏱️ 1:24 • 4d ago

---

**[Tesla Robot handles upside down popcorn. It’s crazy how much these will change everything.](https://www.youtube.com/watch?v=PlEGwoJmon8)**

📺 Tesla Owners Silicon Valley

👁️ 193K • 👍 3K • 💬 177 • ⏱️ 0:40 • 4d ago

---

**[This Is How Warfare Becomes Fully Automated](https://www.youtube.com/watch?v=wrWDnuWlKDs)**

Autonomous micro drones like the Stinger demonstrate how AI can independently identify, track, and eliminate targets using live ...

📺 Deepen

👁️ 128K • 👍 2K • 💬 92 • ⏱️ 0:40 • 3d ago

---

**[The world of robotics is advancing](https://www.youtube.com/watch?v=O-IPeboeXGI)**

📺 Fredo on TV

👁️ 203K • 👍 20K • 💬 554 • ⏱️ 0:34 • 2d ago

---

**[헬로카봇 빅포트 탱크 변신 합체 모음 Hello Carbot Robot Toys Transformation](https://www.youtube.com/watch?v=JL45MHCxjvw)**

헬로카봇 빅포트 탱크 변신 합체 모음 Hello Carbot Robot Toys Transformation 헬로카봇 용사 시즌2 첫 메카는 강력한 탱크 빅포트 빅 ...

📺 Rainbow Play

👁️ 4K • 👍 41 • 💬 14 • ⏱️ 6:57 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*

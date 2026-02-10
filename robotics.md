---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-10T10:30:47.183370+00:00'
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

**Last Updated:** February 10, 2026 at 10:30 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[G1 kicks mother and child when performing](https://www.reddit.com/r/robotics/comments/1r0awur/g1_kicks_mother_and_child_when_performing/)**

16h ago

---

**[We trained a VLA model on 20,000 hours of real robot data across 9 embodiments, then tested it on 100 tasks. Here's what actually worked and what didn't.](https://www.reddit.com/r/robotics/comments/1r0au80/we_trained_a_vla_model_on_20000_hours_of_real/)**

Over the past year our team built LingBot-VLA, a Vision-Language-Action foundation model for dual-arm manipulation. We just released everything: code, base model, and benchmark data (paper: arXiv:2601.18692, code: github.com/robbyant/lingbot-vla, weights on HuggingFace). I wanted to share what we learned deploying this across real hardware because the results tell an honest and, I think, useful story for anyone working on generalist robot policies. The setup: ~20,000 hours of teleoperated manipulation data from 9 mainstream dual-arm configs (Agibot G1, AgileX, Galaxea R1Pro, Realman, Leju KUAVO, and others). We evaluated on 3 physical platforms, 100 tasks each, 130 post-training demos per task, 15 trials per task per model. That's 22,500 total real-world trials comparing us against π0.5, GR00T N1.6, and WALL-OSS under identical conditions. The honest numbers: our best variant (with depth distillation) hit 17.30% average success rate and 35.41% progress score across all 300 task-platform pairs. π0.5 got 13.02% SR / 27.65% PS. WALL-OSS landed at 4.05% SR. Before anyone says "17% is low," I want to contextualize this. These are 100 diverse bimanual tasks, many requiring multi-step fine-grained manipulation (cleaning tableware, stacking, arranging objects), tested across three physically different robots. Some individual tasks hit 80%+ SR, others are near zero. Real-world bimanual manipulation across this breadth of tasks is genuinely hard, and I think the field benefits from reporting these numbers honestly rather than cherry-picking the best 5 tasks for a demo reel. What actually worked well: Scaling laws are real and not saturating. We ran a systematic study scaling pre-training data from 3K to 6K to 13K to 18K to 20K hours. Success rates climbed consistently across all three platforms with no sign of plateau at 20K. This was the most exciting finding for us because it suggests the path forward is clear: more diverse, high-quality real-world data keeps helping. Depth distillation made a meaningful difference. We use learnable queries aligned with depth embeddings from our LingBot-Depth model via cross-attention. This bumped average SR from 15.74% to 17.30% in real-world and from 85.34% to 86.68% in randomized simulation scenes. The gain was most visible on transparent object manipulation (glass vases, clear containers) where RGB alone struggles. Data-efficient adaptation. With only 80 demos per task, LingBot-VLA outperformed π0.5 trained on the full 130 demos, in both SR and progress score. The gap widened as we added more post-training data, which suggests the pre-training is providing genuinely useful priors rather than just memorizing. Training efficiency. We built a custom codebase with FSDP2, mixed-precision, FlexAttention, and operator fusion via torch.compile. On 8 GPUs we get 261 samples/sec/GPU for the Qwen2.5-VL-3B backbone, which is 1.5x to 2.8x faster than StarVLA, Dexbotic, and OpenPI depending on the VLM. Scaling to 256 GPUs tracks near-linear throughput. This matters practically because iterating on 20K hours of data is brutal without an efficient pipeline. What didn't work or remains unsolved: Plenty of tasks are still near 0% SR across all models. Tasks requiring very precise spatial reasoning in cluttered scenes, long-horizon multi-step sequences, or unusual object geometries remain extremely challenging. The depth distillation helps but doesn't solve spatial reasoning completely. Also, the model currently only covers dual-arm tabletop manipulation. Single-arm, mobile manipulation, and non-tabletop scenarios are future work. The architecture uses a Mixture-of-Transformers design (similar to BAGEL) where the VLM and action expert share self-attention but have separate feedforward pathways. Action generation uses flow matching with 50-step action chunks. We found the shared attention critical for letting semantic understanding guide action prediction without the modalities interfering with each other's representations. One thing I'd love to hear from this community: for those of you working with real dual-arm setups, what task categories do you find most important for practical deployment? Our GM-100 benchmark covers 100 tasks but we're always thinking about what's missing. Also curious if anyone has experimented with alternative spatial representations beyond depth for VLA models. All code, model weights, and the benchmark data are public. We wanted to make sure anyone can reproduce these results and build on them.

16h ago

---

**[Building a robot](https://www.reddit.com/r/robotics/comments/1r0len2/building_a_robot/)**

Hi guys! Im 17 and Have NO prior experience to ths. As you can see in the caption, i wanna build a robot. Its Supposed to be a Mining robot, one they could perhaps use instead of Human workers in very Dangerous Enviroments (Deadly Gasses in the Mine or Radioactive material or similar stuff.) Im Currently still drawing the blueprint. Its more jst a suggestion currently but anyways. (I will attach a picture of the current status, most of it will probably Change, also sorry if the handwriting is bad). So. My rough ideas: it will use something like tank tracks to move around (in drawing too). Because its easier to maintain than legs, cheaper and less complicated. Im still somewhat stuck on the arms, where they meet the upper hull i will probably use an electric servo motor so its more detailed, the arms themselves will probably use hydraulics because they are POWAH (as far as i know). Which in this case is very much needed. At the peak of the arm (where normally hands are) i wanna make a motor slot, so you can easily take out motors and/or change them according to tbe tool (Drill or Hammer for example). Im thinking of maybe screwing it in or using a few screws to hold it in, for easy maintenance. I have not yet though about how its gonna see around (head) or what its upper body would look like yet. As for energy supply?..probably changeable batteries (big ones) so you dont have to charge it, and can more or less let it continously work. Would you guys have any idea what could be changed on the CURRENT design?

10h ago

---

**[Humanoid Robotics Oversight and Blocking of Obtainment from Totalitarians Act of 2025](https://www.reddit.com/r/robotics/comments/1r0ritl/humanoid_robotics_oversight_and_blocking_of/)**

https://www.congress.gov/bill/119th-congress/senate-bill/3275/text It seems now US is banning Chinese EVS, drones and finally humanoid robots. Will they ban chinese actuators as well?

5h ago

---

**[Connection for ball balancing robot?](https://www.reddit.com/r/robotics/comments/1r0x02z/connection_for_ball_balancing_robot/)**

Hey , I'm in the connection for ball balancing robot I don't know how to do it , it's an imu sensors bot with arduino uno i have no Idea what connection is needed for connection the body is bulid. Only the connections and code is required.... I hope you guys will help me I have only 1 week time .:)

16m ago

---

**[Biometric Access System with Dual Authentication using Arduino Uno](https://www.reddit.com/r/robotics/comments/1r0wpx9/biometric_access_system_with_dual_authentication/)**

33m ago

---

**[Does anyone have an experience running SmolVLA simulations?](https://www.reddit.com/r/robotics/comments/1r0whaj/does_anyone_have_an_experience_running_smolvla/)**

49m ago

---

**[Alve-x robot arm](https://www.reddit.com/r/robotics/comments/1r0kt4u/alvex_robot_arm/)**

10h ago

---

**[Quantum-Assisted Path-Planning for Robotic Quality Inspection in Industry 4.0 | Qubits26](https://www.reddit.com/r/robotics/comments/1r0v5xf/quantumassisted_pathplanning_for_robotic_quality/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/ZvxcdFsGxRI?si=lOf37bVvi6sUnUWo) • 2h ago

---

**[Lego strandbeest (Part 1)](https://www.reddit.com/r/robotics/comments/1r09da6/lego_strandbeest_part_1/)**

17h ago

---

---

## Google News: "robotics"

**[Haply Robotics raises $16 million to build the “steering wheels” for physical AI](https://betakit.com/haply-robotics-raises-16-million-to-build-the-steering-wheels-for-physical-ai/)**

How the Montréal startup plans to own the touch layer of robotics.

BetaKit • 17h ago

---

**[China: Humanoid robots perform kung fu moves with Shaolin monks in a viral video](https://interestingengineering.com/ai-robotics/humanoid-robots-kung-fu-with-shaolin-monks)**

A group of humanoid robots made by Agibot performed kung fu moves at the Shaolin Temple in China, captivating viewers with their capabilities.

Interesting Engineering • 23h ago

---

**[China Is Going All-In to Beat the U.S. on Humanoid Robots](https://www.wsj.com/tech/china-is-going-all-in-to-beat-the-u-s-on-humanoid-robots-b9c434d2?gaa_at=eafs&gaa_n=AWEtsqdSjo5dINZIZ4IBxdS-Urm416OZjH1hmtSJAO6yTntyMzqXuoTkL7Vv&gaa_ts=698b0c3c&gaa_sig=thTPG221qaxdvcApO-FnpNSn2LR0fnZ0DI5xpcX5nwencdNCr-k9oO00zQJbehhuptLSL1zo1Kty2rl4asduIw%3D%3D)**

The Wall Street Journal • 3d ago

---

**[What happens if robots learn to feel physical harm?](https://newatlas.com/ai-humanoids/robots-learn-feel-physical-harm/)**

In a groundbreaking new study, researchers have developed an electronic skin that allows humanoid robots to distinguish everyday touch from damaging force. That ability, once reserved for living nervous systems, could reshape how robots interact with the physical world and with humans in particular.

New Atlas • 1d ago

---

**[Dreame Pool Debuts Award-Winning Robotic Cleaner During the Game Day with NBC Commercial](https://sg.finance.yahoo.com/news/dreame-pool-debuts-award-winning-085400939.html)**

On February 8, Dreame Pool announced that its flagship pool-cleaning robot, the Zircon 2 Ultra, made its U.S. primetime debut in a nationwide commercial that aired on NBC during Championship Sunday — reaching millions of viewers across the network's extensive footprint. The campaign introduced Dreame Pool's cutting-edge technology to a mass audience, signaling a new era of intelligent pool maintenance on one of the biggest days in sports and entertainment.

Yahoo Finance Singapore • 1h ago

---

**[Alibaba Pushes Into Robotics AI With Open-Source ‘RynnBrain’](https://www.bloomberg.com/news/articles/2026-02-10/alibaba-pushes-into-robotics-ai-with-open-source-rynnbrain)**

bloomberg.com • 3h ago

---

**[Robots for daily life: Mint and Rice Robotics plan HK$10M AI venture](https://www.stocktitan.net/news/MIMI/mint-signed-mo-u-with-robotics-leader-rice-robotics-to-pioneer-1ae1uax2xl9b.html)**

HK$10M JV MoU targets localized robotics R&D in Hong Kong, combining Mint’s Southeast Asia reach with Rice Robotics’ Japan presence around 'physical AI'.

stocktitan.net • 21h ago

---

**[Tesla's Robotics Revolution Won't Save It (NASDAQ:TSLA)](https://seekingalpha.com/article/4867567-teslas-robotics-revolution-would-not-save-it)**

Seeking Alpha • 1d ago

---

**[AI, Robotaxis, and Robotics: Why Elon Musk and Tesla Are Set to Join "Magnificent Seven" Peers on a Massive Spending Spree](https://www.fool.com/investing/2026/02/09/ai-robotaxis-robotics-elon-musk-tesla-mag-7/)**

The once-thriving electric vehicle leader is investing in a new future.

The Motley Fool • 17h ago

---

**[Swarmbotics Wins US Army Contract for Swarming Ground Robots](https://thedefensepost.com/2026/02/09/swarmbotics-us-army/)**

Swarmbotics AI has won a US Army contract to build swarming, attritable small unmanned ground vehicles for the 1st Cavalry Division.

The Defense Post • 1d ago

---

---

## YouTube Videos: "robotics"

**[Atlas Airborne Robot Shows the Final Evolution of Boston Dynamics](https://www.youtube.com/watch?v=IjRjKwZhYCQ)**

The Atlas Airborne Robot takes one final research run as Boston Dynamics pushes humanoid robot control to its absolute limit.

📺 DPCcars

👁️ 68K • 👍 463 • 💬 82 • ⏱️ 2:45 • 2d ago

---

**[Elon Musk on Why Everyone Will Want an Optimus Robot by 2027](https://www.youtube.com/watch?v=dWRqUdVBKjE)**

Will a robot soon be watching your children or caring for your parents? Elon Musk predicts a future where billions of humanoid ...

📺 SpaceTakers

👁️ 41K • 👍 821 • 💬 74 • ⏱️ 0:29 • 4d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=HInDqhlzVd4)**

📺 Lin of Brant robot 

👁️ 28K • 👍 69 • 💬 2 • ⏱️ 0:20 • 4d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 1.1M • 👍 36K • 💬 4K • ⏱️ 1:38 • 2d ago

---

**[SHOCKING: XPeng’s New IRON Robot COLLAPSES in Public...](https://www.youtube.com/watch?v=4MNfUBZNRFU)**

XPeng's brand-new IRON humanoid robot just collapsed in public, and the footage has taken the internet by storm. In this video ...

📺 The AI Nexus

👁️ 8K • 👍 140 • 💬 35 • ⏱️ 19:22 • 5d ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 241K • 👍 4K • 💬 934 • ⏱️ 13:31 • 5d ago

---

**[Tony Stark would hate this! 😂 #engineering #ironman #revrobotics #3dprinting](https://www.youtube.com/watch?v=13fah4TQXhw)**

📺 Concept Bytes

👁️ 29K • 👍 2K • 💬 34 • ⏱️ 1:24 • 4d ago

---

**[This Is How Warfare Becomes Fully Automated](https://www.youtube.com/watch?v=wrWDnuWlKDs)**

Autonomous micro drones like the Stinger demonstrate how AI can independently identify, track, and eliminate targets using live ...

📺 Deepen

👁️ 129K • 👍 2K • 💬 92 • ⏱️ 0:40 • 4d ago

---

**[War Robots - Trolling With The Ravager Ballista | This Shouldn’t Work… But It Did!](https://www.youtube.com/watch?v=GcXahFeSPIE)**

War Robots - Trolling with the Ravager Ballista setup. This is definitely not a setup I would personally recommend but somehow in ...

📺 Adrian Chong

👁️ 4K • 👍 261 • 💬 34 • ⏱️ 19:12 • 20h ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 28K • 👍 458 • 💬 12 • ⏱️ 0:19 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-10T06:43:13.641105+00:00'
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

**Last Updated:** February 10, 2026 at 06:43 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[G1 kicks mother and child when performing](https://www.reddit.com/r/robotics/comments/1r0awur/g1_kicks_mother_and_child_when_performing/)**

12h ago

---

**[We trained a VLA model on 20,000 hours of real robot data across 9 embodiments, then tested it on 100 tasks. Here's what actually worked and what didn't.](https://www.reddit.com/r/robotics/comments/1r0au80/we_trained_a_vla_model_on_20000_hours_of_real/)**

Over the past year our team built LingBot-VLA, a Vision-Language-Action foundation model for dual-arm manipulation. We just released everything: code, base model, and benchmark data (paper: arXiv:2601.18692, code: github.com/robbyant/lingbot-vla, weights on HuggingFace). I wanted to share what we learned deploying this across real hardware because the results tell an honest and, I think, useful story for anyone working on generalist robot policies. The setup: ~20,000 hours of teleoperated manipulation data from 9 mainstream dual-arm configs (Agibot G1, AgileX, Galaxea R1Pro, Realman, Leju KUAVO, and others). We evaluated on 3 physical platforms, 100 tasks each, 130 post-training demos per task, 15 trials per task per model. That's 22,500 total real-world trials comparing us against π0.5, GR00T N1.6, and WALL-OSS under identical conditions. The honest numbers: our best variant (with depth distillation) hit 17.30% average success rate and 35.41% progress score across all 300 task-platform pairs. π0.5 got 13.02% SR / 27.65% PS. WALL-OSS landed at 4.05% SR. Before anyone says "17% is low," I want to contextualize this. These are 100 diverse bimanual tasks, many requiring multi-step fine-grained manipulation (cleaning tableware, stacking, arranging objects), tested across three physically different robots. Some individual tasks hit 80%+ SR, others are near zero. Real-world bimanual manipulation across this breadth of tasks is genuinely hard, and I think the field benefits from reporting these numbers honestly rather than cherry-picking the best 5 tasks for a demo reel. What actually worked well: Scaling laws are real and not saturating. We ran a systematic study scaling pre-training data from 3K to 6K to 13K to 18K to 20K hours. Success rates climbed consistently across all three platforms with no sign of plateau at 20K. This was the most exciting finding for us because it suggests the path forward is clear: more diverse, high-quality real-world data keeps helping. Depth distillation made a meaningful difference. We use learnable queries aligned with depth embeddings from our LingBot-Depth model via cross-attention. This bumped average SR from 15.74% to 17.30% in real-world and from 85.34% to 86.68% in randomized simulation scenes. The gain was most visible on transparent object manipulation (glass vases, clear containers) where RGB alone struggles. Data-efficient adaptation. With only 80 demos per task, LingBot-VLA outperformed π0.5 trained on the full 130 demos, in both SR and progress score. The gap widened as we added more post-training data, which suggests the pre-training is providing genuinely useful priors rather than just memorizing. Training efficiency. We built a custom codebase with FSDP2, mixed-precision, FlexAttention, and operator fusion via torch.compile. On 8 GPUs we get 261 samples/sec/GPU for the Qwen2.5-VL-3B backbone, which is 1.5x to 2.8x faster than StarVLA, Dexbotic, and OpenPI depending on the VLM. Scaling to 256 GPUs tracks near-linear throughput. This matters practically because iterating on 20K hours of data is brutal without an efficient pipeline. What didn't work or remains unsolved: Plenty of tasks are still near 0% SR across all models. Tasks requiring very precise spatial reasoning in cluttered scenes, long-horizon multi-step sequences, or unusual object geometries remain extremely challenging. The depth distillation helps but doesn't solve spatial reasoning completely. Also, the model currently only covers dual-arm tabletop manipulation. Single-arm, mobile manipulation, and non-tabletop scenarios are future work. The architecture uses a Mixture-of-Transformers design (similar to BAGEL) where the VLM and action expert share self-attention but have separate feedforward pathways. Action generation uses flow matching with 50-step action chunks. We found the shared attention critical for letting semantic understanding guide action prediction without the modalities interfering with each other's representations. One thing I'd love to hear from this community: for those of you working with real dual-arm setups, what task categories do you find most important for practical deployment? Our GM-100 benchmark covers 100 tasks but we're always thinking about what's missing. Also curious if anyone has experimented with alternative spatial representations beyond depth for VLA models. All code, model weights, and the benchmark data are public. We wanted to make sure anyone can reproduce these results and build on them.

13h ago

---

**[Building a robot](https://www.reddit.com/r/robotics/comments/1r0len2/building_a_robot/)**

Hi guys! Im 17 and Have NO prior experience to ths. As you can see in the caption, i wanna build a robot. Its Supposed to be a Mining robot, one they could perhaps use instead of Human workers in very Dangerous Enviroments (Deadly Gasses in the Mine or Radioactive material or similar stuff.) Im Currently still drawing the blueprint. Its more jst a suggestion currently but anyways. (I will attach a picture of the current status, most of it will probably Change, also sorry if the handwriting is bad). So. My rough ideas: it will use something like tank tracks to move around (in drawing too). Because its easier to maintain than legs, cheaper and less complicated. Im still somewhat stuck on the arms, where they meet the upper hull i will probably use an electric servo motor so its more detailed, the arms themselves will probably use hydraulics because they are POWAH (as far as i know). Which in this case is very much needed. At the peak of the arm (where normally hands are) i wanna make a motor slot, so you can easily take out motors and/or change them according to tbe tool (Drill or Hammer for example). Im thinking of maybe screwing it in or using a few screws to hold it in, for easy maintenance. I have not yet though about how its gonna see around (head) or what its upper body would look like yet. As for energy supply?..probably changeable batteries (big ones) so you dont have to charge it, and can more or less let it continously work. Would you guys have any idea what could be changed on the CURRENT design?

6h ago

---

**[Humanoid Robotics Oversight and Blocking of Obtainment from Totalitarians Act of 2025](https://www.reddit.com/r/robotics/comments/1r0ritl/humanoid_robotics_oversight_and_blocking_of/)**

https://www.congress.gov/bill/119th-congress/senate-bill/3275/text It seems now US is banning Chinese EVS, drones and finally humanoid robots. Will they ban chinese actuators as well?

1h ago

---

**[Alve-x robot arm](https://www.reddit.com/r/robotics/comments/1r0kt4u/alvex_robot_arm/)**

6h ago

---

**[Lego strandbeest (Part 1)](https://www.reddit.com/r/robotics/comments/1r09da6/lego_strandbeest_part_1/)**

13h ago

---

**[Robot](https://www.reddit.com/r/robotics/comments/1qzw7nc/robot/)**

1d ago

---

**[Brian Gerkey on open source and commercialization](https://www.reddit.com/r/robotics/comments/1r08txo/brian_gerkey_on_open_source_and_commercialization/)**

When asked about tension around open source in robotics, Brian Gerkey, CTO of Intrinsic, pushes back on the idea that it was ever a problem. His point is that open source was designed from the start to be used by industry, not kept separate from it. Permissive licensing was intentional. Companies were meant to take the software, ship products with it, and build businesses on top, without being forced to contribute back. From that perspective, corporate involvement isn’t a betrayal of open source. What matters is whether the software stays open, maintained, and widely usable over time, not who adopts it or commercializes it.

14h ago

---

**[Built a browser-based teleoperation platform for quadrupeds, and drones. Looking for beta testers to try remote piloting](https://www.reddit.com/r/robotics/comments/1r0cib6/built_a_browserbased_teleoperation_platform_for/)**

https://preview.redd.it/lrhwvdgtjiig1.png?width=2880&format=png&auto=webp&s=8bd95c1e3352d027ab5574c0b9e17850b45186b3 Hey r/robotics, I've been working on a teleoperation platform that lets you control robots remotely through a browser with low-latency video (~150ms). Currently testing with a Unitree Go2 EDU Plus XT16. The setup: - WebRTC video/audio streaming from the robot - Real-time controls via WebSocket - HUD overlay with telemetry (battery, signal, heading) - Works on laptop/desktop with Chrome, Brave, and safari. - Mobile Bonding System I'm looking for a few people to beta test the pilot experience and give feedback on: - Control responsiveness - Video quality/latency - UI/UX of the operator interface - What features you'd want to see No hardware needed on your end , you'd be remotely controlling an actual robot in my lab. If you're interested, drop a comment or DM with: - Your timezone - Any relevant background (gaming, drones, robotics, etc - not required) - What interests you about remote robot operation Happy to answer questions about the technical stack too (WebRTC, Janus, aiortc, etc). Thanks!

12h ago

---

**[North American robot orders rose again in 2025, driven mostly by non-automotive industries](https://www.reddit.com/r/robotics/comments/1r0iyy9/north_american_robot_orders_rose_again_in_2025/)**

New industry data shows robot orders in North America increased in 2025, reaching 36,766 units worth $2.25B, up 6.6% in units and 10.1% in revenue compared to 2024. Food and consumer goods, semiconductors and electronics, and life sciences accounted for the majority of orders. Automotive suppliers lagged 2024 levels, but OEM activity picked up later in the year. Q4 was the strongest quarter with 10,325 robots ordered in Q4 alone, marking the sixth straight quarter of year-over-year growth and the highest annual total since 2022. Cobots made up 28.6% of Q4 units and nearly 20% of all robots ordered in 2025, with their highest quarterly volume since being tracked as a separate category.

🔗 [Automate](https://www.automate.org/robotics/news/robot-orders-grow-6-6-in-2025-as-general-industries-drive-broader-automation-adoption) • 8h ago

---

---

## Google News: "robotics"

**[AI In Robotics - New Position Paper](https://ifr.org/ifr-press-releases/news/ai-in-robotics-new-position-paper)**

A new generation of AI-powered robots moving from research labs into the real world is fueled by AI tech companies and analysts forecasting a multitrillion-dollar market. The vision is to give artificial intelligence its own robot body. What are the trends, challenges, and commercial applications?

IFR International Federation of Robotics • 32m ago

---

**[Elon Musk warns the U.S. is '1,000% going to go bankrupt' unless AI and robotics save the economy from crushing debt](https://fortune.com/2026/02/07/elon-musk-us-bankruptcy-ai-robotics-economic-growth-national-debt-crisis/)**

"We just need enough time to build the AI and robots to not go bankrupt before then."

Fortune • 2d ago

---

**[The Autonomous Robotics Stock Wall Street Insiders Are Quietly Buying (Hint: It's Not Tesla)](https://finance.yahoo.com/news/autonomous-robotics-stock-wall-street-195000880.html)**

This high-flying stock is about more than just military drones.

Yahoo Finance • 1d ago

---

**[China Is Going All-In to Beat the U.S. on Humanoid Robots](https://www.wsj.com/tech/china-is-going-all-in-to-beat-the-u-s-on-humanoid-robots-b9c434d2?gaa_at=eafs&gaa_n=AWEtsqch3HfurA6FOnY4r-3p-8DhArgXWaMCbsFmjRvMzVgB4jB3QwadWX7U&gaa_ts=698ad6ea&gaa_sig=rWU_Dluh1taSihav9lI9KmrhZN-3lEEe7BSCtRR6m7MYLkG_Yf3ZlcjIUGi5mmJD053BrvWH5YdF-fQ1Jerfig%3D%3D)**

The Wall Street Journal • 2d ago

---

**[Idaho robotics team gears up for national competition in Washington D.C.](https://idahonews.com/news/local/idaho-robotics-team-gears-up-for-national-competition-in-washington-dc)**

The Project Impact STEM Academy robotics team, known as The Quackens, is set to represent Idaho on a national stage in Washington, D.C.

KBOI • 1h ago

---

**[China: Humanoid robots perform kung fu moves with Shaolin monks in a viral video](https://interestingengineering.com/ai-robotics/humanoid-robots-kung-fu-with-shaolin-monks)**

A group of humanoid robots made by Agibot performed kung fu moves at the Shaolin Temple in China, captivating viewers with their capabilities.

Interesting Engineering • 19h ago

---

**[Companies shouldn't rush to replace workers with robots. Here's why](https://qz.com/human-workers-ai-robots-automation-risks)**

Companies that replace humans with robots "risk losing their competitive edge," researchers say, as collaboration is the real key

qz.com • 14h ago

---

**[AI, Robotaxis, and Robotics: Why Elon Musk and Tesla Are Set to Join "Magnificent Seven" Peers on a Massive Spending Spree](https://www.fool.com/investing/2026/02/09/ai-robotaxis-robotics-elon-musk-tesla-mag-7/)**

The once-thriving electric vehicle leader is investing in a new future.

The Motley Fool • 13h ago

---

**[Tesla's Robotics Revolution Won't Save It (NASDAQ:TSLA)](https://seekingalpha.com/article/4867567-teslas-robotics-revolution-would-not-save-it)**

Seeking Alpha • 23h ago

---

**[Robots for daily life: Mint and Rice Robotics plan HK$10M AI venture](https://www.stocktitan.net/news/MIMI/mint-signed-mo-u-with-robotics-leader-rice-robotics-to-pioneer-1ae1uax2xl9b.html)**

HK$10M JV MoU targets localized robotics R&D in Hong Kong, combining Mint’s Southeast Asia reach with Rice Robotics’ Japan presence around 'physical AI'.

stocktitan.net • 17h ago

---

---

## YouTube Videos: "robotics"

**[Atlas Airborne Robot Shows the Final Evolution of Boston Dynamics](https://www.youtube.com/watch?v=IjRjKwZhYCQ)**

The Atlas Airborne Robot takes one final research run as Boston Dynamics pushes humanoid robot control to its absolute limit.

📺 DPCcars

👁️ 66K • 👍 447 • 💬 81 • ⏱️ 2:45 • 2d ago

---

**[The real test for humanoid robots isn’t performance.](https://www.youtube.com/watch?v=4iU9kfIZnhs)**

Humanoid robots don't fail at tasks. They fail at presence. The hardest part of building humanoid robots isn't hardware.

📺 Slidebean

👁️ 2K • 👍 151 • 💬 9 • ⏱️ 1:21 • 6h ago

---

**[Elon Musk on Why Everyone Will Want an Optimus Robot by 2027](https://www.youtube.com/watch?v=dWRqUdVBKjE)**

Will a robot soon be watching your children or caring for your parents? Elon Musk predicts a future where billions of humanoid ...

📺 SpaceTakers

👁️ 40K • 👍 801 • 💬 73 • ⏱️ 0:29 • 4d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=HInDqhlzVd4)**

📺 Lin of Brant robot 

👁️ 28K • 👍 69 • 💬 2 • ⏱️ 0:20 • 4d ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 238K • 👍 4K • 💬 931 • ⏱️ 13:31 • 5d ago

---

**[SHOCKING: XPeng’s New IRON Robot COLLAPSES in Public...](https://www.youtube.com/watch?v=4MNfUBZNRFU)**

XPeng's brand-new IRON humanoid robot just collapsed in public, and the footage has taken the internet by storm. In this video ...

📺 The AI Nexus

👁️ 8K • 👍 140 • 💬 35 • ⏱️ 19:22 • 5d ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 28K • 👍 454 • 💬 12 • ⏱️ 0:19 • 2d ago

---

**[Tesla Robot handles upside down popcorn. It’s crazy how much these will change everything.](https://www.youtube.com/watch?v=PlEGwoJmon8)**

📺 Tesla Owners Silicon Valley

👁️ 206K • 👍 3K • 💬 181 • ⏱️ 0:40 • 4d ago

---

**[Humanoid Robot Falls in Front of Everyone](https://www.youtube.com/watch?v=4M0y26U_FRk)**

XPeng's humanoid robot IRON went viral after it fell during its first offline public demo at MixC Shenzhen Bay in Shenzhen on ...

📺 Game of Tomorrow

👁️ 3K • 👍 122 • 💬 9 • ⏱️ 0:48 • 4h ago

---

**[Robots That Move Without a Brain? Sea Star Locomotion Is Changing Robotics Forever #robot #shorts](https://www.youtube.com/watch?v=Q7doiqBMz-k)**

Robots That Move Without a Brain? Sea Star Locomotion Is Changing Robotics Forever What if robots could keep moving even ...

📺 Future Lens Pi

👁️ 28K • 💬 10 • ⏱️ 0:08 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

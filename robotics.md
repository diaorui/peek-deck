---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-22T20:55:30.074082+00:00'
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

**Last Updated:** December 22, 2025 at 20:55 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Physical Intelligence (π) launches the "Robot Olympics": 5 autonomous events demonstrating the new π0.6 generalist model](https://www.reddit.com/r/robotics/comments/1pt6ouz/physical_intelligence_π_launches_the_robot/)**

Physical Intelligence just released a series of "Robot Olympics" events to showcase their latest π0.6 model. Unlike standard benchmarks, these tasks are designed to illustrate Moravec’s Paradox which are everyday physical actions that are trivial for humans but represent the "gold standard" of difficulty for modern robotics. All tasks shown are fully autonomous, demonstrating high-level task decomposition and fine motor control. The 5 Olympic Events: Event 1 (Gold) - Door Entry: The robot successfully navigates a self-closing lever-handle door. This is technically challenging because it requires the model to apply force to keep the door open while simultaneously moving its base through the frame. Event 2 (Silver) - Textile Manipulation: The model successfully turns a sock right-side-out. They attempted the Gold medal task (hanging an inside-out dress shirt), but the current hardware gripper was too wide for the sleeves. Event 3 (Gold) - Fine Tool Use: A major win here,the robot used a small key to unlock a padlock. This requires extreme precision to align the key and enough torque to turn the tumbler. (Silver was making a peanut butter sandwich, involving long-horizon steps like spreading and cutting triangles). Event 4 (Silver) - Deformable Objects: The robot successfully opened a dog poop bag. This is notoriously difficult because the thin plastic blinds the wrist cameras during manipulation. They attempted to peel an orange for Gold but were "disqualified" for needing a sharper tool. Event 5 (Gold) - Complex Cleaning: The robot washed a frying pan in a sink using soap and water, scrubbing both sides. They also cleared the Silver (cleaning the grippers) and Bronze (wiping the counter) tasks for this category. The Tech Behind It: The π0.6 model is a Vision-Language-Action (VLA) generalist policy. It moves away from simple "behavior cloning" and instead focuses on agentic coding and task completion, allowing it to recover from errors and handle diverse, "messy" real-world environments. Official Blog: pi.website/blog/olympics Source Video: Physical Intelligence on X

2h ago

---

**[GITAI's rovers and robotic arms deploy solar panels and weld in a construction field test](https://www.reddit.com/r/robotics/comments/1pswpjv/gitais_rovers_and_robotic_arms_deploy_solar/)**

Website: https://gitai.tech/ On 𝕏: https://x.com/GITAI_HQ Previous post: https://www.reddit.com/r/robotics/comments/1pd2kbm/gitai_is_designing_robots_that_can_maintain/ https://www.reddit.com/r/robotics/comments/1pgfvku/gitai_robots_cooperatively_assemble_a_5meter/

10h ago

---

**[Logan Kilpatrick, lead AI product for Google: "2026 is going to be a huge year for embodied AI" - "We are going to see a lot more robots in the real world soon"](https://www.reddit.com/r/robotics/comments/1psydvl/logan_kilpatrick_lead_ai_product_for_google_2026/)**

Logan Kilpatrick on 𝕏: https://x.com/OfficialLoganK/status/2002831811823763639

8h ago

---

**[[OS] SPIDER: A General Physics-Informed Retargeting Framework for Humanoids & Dexterous Hands](https://www.reddit.com/r/robotics/comments/1pt4uxn/os_spider_a_general_physicsinformed_retargeting/)**

Hi everyone, we’re open-sourcing SPIDER, a general framework for retargeting human motion to diverse robot embodiments. Most retargeting methods suffer from physical inconsistencies. SPIDER is physics-informed, ensuring dynamically feasible motions without artifacts like ghosting or floating. Key Features: General: Supports both humanoids (G1, H1, etc.) and dexterous hands (Allegro, Shadow, etc.). Physics-Based: GPU-accelerated optimization for clean, stable motion. Sim2Real-ready: Ready for deployment, from human video to real-world robot actions. Links: 📦 Code: https://github.com/facebookresearch/spider 📓 Tutorial: Notebook 🌐 Project Page: http://jc-bao.github.io/spider-project/ Would love to hear your feedback or help with any integration questions!

3h ago

---

**[Why don’t we have a small home robot that just… exists?](https://www.reddit.com/r/robotics/comments/1pswx2g/why_dont_we_have_a_small_home_robot_that_just/)**

I keep coming back to this thought, especially when I look at how much home robotics has progressed over the last few years. We’ve had social robots like Jibo and Anki Vector. We’ve seen Amazon Astro. None of them really stuck. And it doesn’t feel like they failed because the tech was bad. More like… they never found a natural place in daily life. What still feels missing to me is a very specific kind of robot. Not a humanoid. Not another appliance on wheels. I’m thinking about something small, maybe pet-sized, that just lives in the house with you. It moves between rooms. Goes upstairs and downstairs. Checks on the cat napping in the sun. Notices when the toddler is too quiet, or suddenly way too loud. Maybe it picks up small stuff, fetches things, or just keeps an eye on what’s going on. Not built around one killer feature. More around presence. The weird part is that most of the building blocks feel… good enough now. Indoor navigation mostly works. Cameras are cheap. Perception models are way better than they used to be. Small mobile robots aren’t exactly new tech. And yet, this category basically doesn’t exist. Which makes me think the blocker isn’t really technical anymore. It’s more about how people are supposed to relate to a thing like this. A few reasons that might explain it: Nobody can quite agree on what a “non-task” home robot is actually for A moving thing in your house feels stranger than a fixed device, even if it does less It’s hard to sell something that doesn’t replace a clear chore Homes are messy, emotional, and inconsistent in very human ways If it’s too capable, people get uneasy; if it’s too dumb, it feels pointless So we’re kind of stuck without a mental model for a robot that’s somewhere between an appliance, a pet, and a background presence. Maybe personal robots don’t fail because they’re not useful enough, but because we keep trying to frame them as tools. Maybe they need to be framed more like ambient companions that adapt to the rhythms of people, kids, and pets, instead of optimizing a single task. Feels like the tech is close. We just don’t know what role this thing is supposed to play yet.

9h ago

---

**[Tilt gimbal](https://www.reddit.com/r/robotics/comments/1pso6qv/tilt_gimbal/)**

This setup uses two single-axis (pitch-only) gimbals stacked in series. When combined, could this configuration serve as an alternative to a robotic arm in certain applications? I’d welcome discussion and insights from the community.

18h ago

---

**[watchdog using roborock](https://www.reddit.com/r/robotics/comments/1pt14lc/watchdog_using_roborock/)**

new modified version with a better camera. Patrolling on demand or on schedule. record video at move forward. excellent navigation avoiding obstacles. no vacuum brushes removed. Just video patrolling.

6h ago

---

**[Tesla Optimus Controversy | Teleoperated!](https://www.reddit.com/r/robotics/comments/1pt33xm/tesla_optimus_controversy_teleoperated/)**

Found an interesting video on Tesla's Optimus Robot.

🔗 [youtu.be](https://youtu.be/J_y5ni5mihI) • 4h ago

---

**[In China, robots are now handling the solar panels, making installation faster and safer](https://www.reddit.com/r/robotics/comments/1ps2aw1/in_china_robots_are_now_handling_the_solar_panels/)**

From Lukas Ziegler on 𝕏: https://x.com/lukas_m_ziegler/status/2002328813548589126

1d ago

---

**[3d printed automatic tool-changer update](https://www.reddit.com/r/robotics/comments/1pt4jb8/3d_printed_automatic_toolchanger_update/)**

Making some good progress on the automatic tool-changing mechanism for my SCARA arm. I got it wired and assembled to the Z-compensation module and made it grip and release when pushing against the tool. I made a tool pocket that fits on a 2020 extrusion so I can stack a few of them in a row once I make more tools and added a little magnet to have it sit in a fixed position. The tools are connected by a magnetic pogo pin connector to power and control them and I want one of the pins to serve as a connection verification signal, and later, tool identification. I am still considering what is the best and simplest method to do it. I am considering wiring different resistors or capacitors in each tool and measuring the voltage/charge time when connected. If anyone has tried these methods before or has a better one I would really appreciate your advice. For more details on this project check out my hackaday page: https://hackaday.io/project/204557-pr3-scara

4h ago

---

---

## Google News: "robotics"

**[Humanoid Robots Are Coming, As Soon As They Learn to Fold Clothes](https://www.bloomberg.com/news/articles/2025-12-19/humanoid-robots-are-emerging-as-the-next-big-ai-breakthrough)**

Bloomberg.com • 3d ago

---

**[Elon Musk shares video of Unitree G1 humanoid robots pulling off backflips at concert](https://technode.com/2025/12/20/elon-musk-shares-video-of-unitree-g1-humanoid-robots-pulling-off-backflips-at-concert/)**

Tesla CEO Elon Musk today reposted a video of a Chinese concert performance on social media platform X, captioning it “Impressive,” a move that quickly

TechNode • 2d ago

---

**[Humanoid robots head to chip factories in global deal with Oversonic](https://www.stocktitan.net/news/STM/oversonic-robotics-signs-humanoid-robots-supply-agreement-with-st-yc3ygdinwizf.html)**

In 2025, STMicroelectronics will deploy Oversonic RoBee humanoids across plants, starting at its Malta fab, and show collaboration with live demos at CES.

Stock Titan • 12h ago

---

**[Humanoid robots are coming. Eventually?](https://www.theverge.com/column/843418/humanoid-robot-hype)**

China sees humanoids as an economic engine and Musk wants a ‘robot army.’

The Verge • 1d ago

---

**[Hyundai Motor Group to Unveil AI Robotics Strategy at CES 2026](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001093)**

Hyundai Motor Group released a teaser image previewing its upcoming participation at CES 2026

hyundai.com • 14h ago

---

**[iRobot founder says company's bankruptcy revealed a new kind of competitor: 'the Chinese fast follower'](https://www.businessinsider.com/irobot-ceo-bankruptcy-china-fast-followers-competition-2025-12)**

As iRobot's founder Colin Angle looks back on its path to bankruptcy, he says it was hard to overcome competitors in China.

Business Insider • 21h ago

---

**[Solo GP Kevin Costa closes $20m fund to invest in AI, robotics and infrastructure](https://sifted.eu/articles/belief-capital-kevin-costa-solo-gp)**

Solo GP Kevin Costa has raised his $20m fund from LPs including general partners at VC firms Point Nine, Hummingbird and Adjacent

Sifted • 15h ago

---

**[‘World’s most advanced’ robotic hand enters mass production with 22 motion freedoms](https://interestingengineering.com/ai-robotics/sharpas-advanced-robotic-hand-enters-mass-production)**

Sharpa Robotics moves its SharpaWave dexterous hand into mass production, scaling human-level robotic manipulation ahead of CES 2026.

Interesting Engineering • 3d ago

---

**[NVIDIA's Quest For A "Safe" Linux Kernel For Automobiles, Robotics](https://www.phoronix.com/news/NVIDIA-ASIL-B-Linux-Kernel)**

NVIDIA engineer Igor Stoppa presented at the Linux Plumbers Conference (LPC) earlier this month around using Linux in safety-critical environments like automobiles and the current shortcomings of the upstream Linux kernel and the challenges on achieving Automotive Safety Integrity Level (ASIL) certifications around the Linux kernel

Phoronix • 9h ago

---

**[China’s humanoid arms race: start-ups debut robots for stores, offices and factories](https://www.scmp.com/tech/big-tech/article/3337098/chinas-humanoid-arms-race-start-ups-debut-robots-stores-offices-and-factories)**

China’s latest venture-backed robotics contenders are unveiling ever more humanlike machines for reception desks, stores and factory floors.

South China Morning Post • 2d ago

---

---

## YouTube Videos: "robotics"

**[AI ROBOTS Are Now TOO REAL! - Shocking AI &amp; Robotics 2025 Updates](https://www.youtube.com/watch?v=a4Y_VVuqYyk)**

The world of AI and robotics accelerated faster this year than almost anyone expected. Humanoid robots became cheaper, faster, ...

📺 AI Revolution

👁️ 36K • 👍 727 • 💬 76 • ⏱️ 2:08:46 • 2d ago

---

**[How STRONG Are Humanoid Robots Really? (And Why It&#39;s Hard to Tell)](https://www.youtube.com/watch?v=PGRJg5eExO4)**

China's got a new Terminator robot and Figure is facing a lawsuit alleging its robots are strong enough to "fracture a human skull.

📺 CNET

👁️ 22K • 👍 502 • 💬 110 • ⏱️ 5:25 • 1d ago

---

**[This Rolling Robot Could Replace Police in the Future](https://www.youtube.com/watch?v=wKWUTIHGQZk)**

FutureTech #Robotics #LawEnforcement.

📺 Skye Ocean Girl

👁️ 30K • 👍 145 • 💬 6 • ⏱️ 0:19 • 1d ago

---

**[TRON 2 Officially Launched | Redefining the Foundation of Embodied Robotics](https://www.youtube.com/watch?v=Ut3QFPr7hyo)**

Cutting-edge Algorithms, At Your Fingertips. Explore More: https://www.limxdynamics.com/en/tron2 #limxdynamics #limxtron2 ...

📺 LimX Dynamics

👁️ 918K • 👍 10K • 💬 600 • ⏱️ 2:43 • 4d ago

---

**[I Made a Self Aware Robot - EXPLAINED](https://www.youtube.com/watch?v=EQEkwqvkyFI)**

LIGHTSAREOFF AZFK MERCH! https://azfk-shop.fourthwall.com/ Donate to the Cult for exclusive behind the Scenes Access ...

📺 AZFK

👁️ 128K • 👍 7K • 💬 520 • ⏱️ 13:43 • 4d ago

---

**[INSANE AI Curling Robot in Dubai😱💇🏼‍♀️Automatic Perm Tach From the Future!](https://www.youtube.com/watch?v=aaHeKdH4ILc)**

ai #beauty #hair #curling #coloring #robot #tachnology #viral #dubai #future #hairstyle #salon #trnding #shorts #transformation ...

📺 Ai BOOF

👁️ 10K • 👍 158 • 💬 6 • ⏱️ 0:11 • 12h ago

---

**[His Self-Aware Robot Escaped ...](https://www.youtube.com/watch?v=e7fkeontbaE)**

I got a little bit bored so His Self-Aware Robot Escaped SUBSCRIBE TO OG @LIGHTSAREOFF New Merch https://socks.store/ ...

📺 SocksReact

👁️ 487K • 👍 9K • 💬 1K • ⏱️ 18:35 • 1d ago

---

**[MY TYLER ROBOT ESCAPED..](https://www.youtube.com/watch?v=JML9u9OlIKE)**

MERCH NOW 50% OFF! ✨ https://tylerandsnowi.store/ For a Limited Time ⏰ Today Tyler and Snowi meet ELBERR THE ...

📺 Tyler & Snowi

👁️ 1.0M • 👍 39K • 💬 642 • ⏱️ 21:05 • 21h ago

---

**[Introduction to Physical AI &amp; Robotics at NVIDIA](https://www.youtube.com/watch?v=p8yhD0JnScM)**

This session will provide a high-level overview of NVIDIA's comprehensive approach to robotics, emphasizing how our open ...

📺 NVIDIA Developer

👁️ 2K • 👍 91 • 💬 1 • ⏱️ 55:42 • 2d ago

---

**[China Just Crossed The Line With 6 Arm AI Robot (Works All At Once)](https://www.youtube.com/watch?v=ppoFxgp0PJI)**

Factories, streets, and physical reality just crossed a line. China unveiled a six-armed industrial robot built to outwork humans on ...

📺 AI Revolution

👁️ 76K • 👍 1K • 💬 146 • ⏱️ 11:23 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

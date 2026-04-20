---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-20T16:40:31.751839+00:00'
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

**Last Updated:** April 20, 2026 at 16:40 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Little Robots Join the Half-Marathon. Some even run decked out in costumes .](https://www.reddit.com/r/robotics/comments/1sqo9f0/little_robots_join_the_halfmarathon_some_even_run/)**

T.Yamazaki on 𝕏: https://x.com/ZappyZappy7/status/2046192595802656933 High Torque Robotics on YouTube: https://www.youtube.com/watch?v=aBe_ceuesEA

3h ago

---

**[2026 robot half marathon fail & fun compilation](https://www.reddit.com/r/robotics/comments/1sqd2ag/2026_robot_half_marathon_fail_fun_compilation/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2045896309765288179

13h ago

---

**[Many of the finish times have been revised upward (by 10–15 seconds) – Maintenance and battery replacement like F1](https://www.reddit.com/r/robotics/comments/1spq0zh/many_of_the_finish_times_have_been_revised_upward/)**

From 小互 on 𝕏: "Feels a bit like F1": https://x.com/xiaohu/status/2045786816213815411

1d ago

---

**[Newton 1.0 is 100% open source. GPU-accelerated physics engine from NVIDIA, DeepMind, and Disney Research, now under the Linux Foundation](https://www.reddit.com/r/robotics/comments/1squlyf/newton_10_is_100_open_source_gpuaccelerated/)**

Repo: https://github.com/newton-physics/newton Been digging into this over the weekend. Quick rundown for anyone who hasn't seen it yet: Built on NVIDIA Warp, Apache 2.0, now governed by the Linux Foundation (vendor-neutral) MuJoCo Warp is integrated as a solver, plus Disney's Kamino solver for closed-loop mechanisms (parallel linkages, robotic hands) Reported 475x faster than MJX on manipulation tasks on RTX PRO 6000 Blackwell. Massive parallel throughput per GPU means more room for aggressive domain randomization, which is usually where sim-to-real actually breaks OpenUSD native. So assets from Omniverse and Isaac Lab can be dropped in directly. Embedded OpenGL viewer + USD viewer for debugging I know this isn't brand new, but wanted to share as I am genuinely excited about where physics engines are heading, especially with this kind of collaboration behind it.

3m ago

---

**[Update on Cubic Doggo: man, walking is hard](https://www.reddit.com/r/robotics/comments/1sq4rip/update_on_cubic_doggo_man_walking_is_hard/)**

Update from the previous post: https://www.reddit.com/r/robotics/comments/1rouerc/first_time_building_a_hobbyist_robot_from_scratch/ Added control since last time, which is actually the easy part with ROS2. I am also surprised by how versatile Dynamixel XL430-W250-T servos are; they even offer current-based position control that mimics the torque control. Hope their higher torque variants get cheaper over time. Made several iterations of the servos and battery arrangement to center the mass (redoing all the urdf is really quite something). Tried a few different walking gaits with IK calculated by ROS2, which I believe is oriented around position control, so a bit difficult to define arbitrary trajectories. Put on kitchen sponge clothes to increase friction on the feet. The previous attempt on all four feet twisted and broke off one leg, so now it sticks with only the two front legs. I think that is also why the back legs felt limp as a few screws went loose in that incident. Anyways, have a few things in mind to fix/try, and always welcome any recommendation: https://github.com/SphericalCowww/CubicDoggo

19h ago

---

**[How did so many Chinese robot manufacturers catch up to Boston Dynamics?](https://www.reddit.com/r/robotics/comments/1sq2bzn/how_did_so_many_chinese_robot_manufacturers_catch/)**

They had been working on their designs for years and I don't think they publish proprietary information so how is it that there are so many manufacturers with humanoid and 'Spot-form' robots that seem to be equal or outperform Boston Dynamics?

21h ago

---

**[Everyone saw the Honour robot win… but nobody noticed what it did right after](https://www.reddit.com/r/robotics/comments/1spy9lg/everyone_saw_the_honour_robot_win_but_nobody/)**

23h ago

---

**[Robots I saw at MODEX 2026](https://www.reddit.com/r/robotics/comments/1sqspjf/robots_i_saw_at_modex_2026/)**

1h ago

---

**[Real-World Deployment as a Core Strategy in Robotics Development](https://www.reddit.com/r/robotics/comments/1sq3s5m/realworld_deployment_as_a_core_strategy_in/)**

Ali Kashani, founder and CEO of Serve Robotics and former head of robotics at Postmates X, has spent years deploying autonomous delivery robots in active urban environments. He mentions systems built only in controlled settings are based on assumptions. Once robots operate in public, those assumptions are tested immediately. People behave unpredictably, environments change, and situations come up that were never accounted for during development. Those conditions shape what actually needs to be solved. They expose gaps that do not appear in lab testing and force teams to prioritize what matters in real use.

20h ago

---

**[What's your take on AI-generated environments for sim-to-real? HY-World 2.0 skips the video→3DGS→mesh chain entirely](https://www.reddit.com/r/robotics/comments/1sqivfr/whats_your_take_on_aigenerated_environments_for/)**

Tencent just open-sourced HY-World 2.0 (https://github.com/Tencent-Hunyuan/HY-World-2.0). The key difference from video world models like Genie 3 or Cosmos is that it outputs real 3D assets (meshes, 3DGS) that you can import into Isaac Sim, Unity, Unreal, not just pixel videos. I've spent time trying to go from video world models → 3DGS → meshes and the information loss along the way is brutal. You end up with hole-y environments full of weird artifacts. WorldLabs' Marble was better because it generates 3DGS directly, but then the mesh conversion still sucked. I built my own conversion pipeline for their outputs and still wasn't happy with it. HY-World 2.0 skipping that whole chain and outputting usable 3D directly is a big deal if the quality holds up. For robotics sim specifically: this could be solid for fast environment generation and domain randomization. If you need a bunch of varied training environments quickly, this kind of tool gets you there. It won't replace handcrafted digital twins for teams that need hyperrealistic sim-to-real fidelity, but for the "I need 200 warehouse variations for my policy to generalize" use case, it could be a real speedup. Anyone else tried running the WorldMirror 2.0 reconstruction yet? Curious how the outputs actually look in a sim engine.

8h ago

---

---

## Google News: "robotics"

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 1d ago

---

**[NVIDIA and QNX target safer robots and medical devices with edge AI](https://www.stocktitan.net/news/BB/qnx-and-nvidia-deepen-collaboration-to-advance-safety-critical-edge-2fpnzowdrzx3.html)**

Using IGX Thor and Halos Safety Stack, the platform combines real-time control with AI, supporting safety certification. Early access is now open.

Stock Titan • 10h ago

---

**[Tools for Your To Do List with Spot and Gemini Robotics](https://bostondynamics.com/blog/tools-for-your-to-do-list-with-spot-and-gemini-robotics/)**

A recent demo shows Boston Dynamics Spot in a residential home, using Google’s visual-language model (VLM) Gemini Robotics-ER 1.5 for embodied reasoning.

Boston Dynamics • 10h ago

---

**[Video Friday: Digit Learns to Dead-lift](https://spectrum.ieee.org/robot-learning)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 42m ago

---

**[Coco Robotics and BlindSquare Partner to Make City Sidewalks Safer and More Accessible for All](https://www.prnewswire.com/news-releases/coco-robotics-and-blindsquare-partner-to-make-city-sidewalks-safer-and-more-accessible-for-all-302747192.html)**

/PRNewswire/ -- Coco Robotics, the world's largest urban robot delivery platform, and BlindSquare, the world's most widely used accessible GPS app for the...

PR Newswire • 1h ago

---

**[Ferris State hosts FIRST Robotics contest in the Jim Wink Arena](https://www.bigrapidsnews.com/news/article/ferris-state-first-robotics-22215837.php)**

Big Rapids Pioneer • 58m ago

---

**[Pudu Robotics debuts commercial cleaning and delivery robots](https://www.dcvelocity.com/material-handling/pudu-robotics-debuts-commercial-cleaning-and-delivery-robots)**

The manufacturer's intelligent scrubber and sweeper robot & PUDU D5 quadruped delivery robot put on a show at Modex 2026 last week, wowing attendees with their capabilities.

DC Velocity • 24m ago

---

**[Embodied AI Company Booster Robotics Completes Nearly 1 Billion Yuan Financing](https://autonews.gasgoo.com/articles/news/embodied-ai-company-booster-robotics-completes-nearly-1-billion-yuan-financing-2046225660790435840)**

body { font-size: 16px; line-height: 34px; ...

Gasgoo • 2h ago

---

**[Robotics bring the future of surgery to Southern New Hampshire](https://nashua.inklink.news/robotics-bring-the-future-of-surgery-to-southern-new-hampshire/)**

Nashua Ink Link • 1h ago

---

**[🎥 AgriPass on ag robotics 2.0: ‘We’re replicating the human weeding process but making it affordable at scale’](https://agfundernews.com/agripass-on-ag-robotics-2-0-were-replicating-the-human-weeding-process-but-making-it-affordable-at-scale)**

Israeli startup AgriPass pulls weeds out of the ground with what it claims is the precision of a human hand.

AgFunderNews • 46m ago

---

---

## YouTube Videos: "robotics"

**[The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ)**

Physical Intelligence is building a foundation model that can control any robot to do any task — what the team describes as the ...

📺 Y Combinator

👁️ 46K • 👍 1K • 💬 58 • ⏱️ 49:27 • 4d ago

---

**[A humanoid robot is seen chasing a group of wild boars off the street](https://www.youtube.com/watch?v=yyCmTL-wC-w)**

For more context and news coverage of the most important stories of our day, click here: https://www.nbcnews.com » Subscribe to ...

📺 NBC News

👁️ 231K • 👍 4K • 💬 309 • ⏱️ 0:25 • 5d ago

---

**[Robot in Poland scares off wild boars](https://www.youtube.com/watch?v=BmwTEOGb88k)**

A humanoid robot named Edward Warchocki chased away a herd of wild boars in Warsaw, shouting "Go away!" in Polish as the ...

📺 Reuters

👁️ 46K • 👍 685 • 💬 77 • ⏱️ 0:26 • 6d ago

---

**[The Future is Mass-Produced: Inside the Canton Fair Robotics Hall](https://www.youtube.com/watch?v=S0eEXTn3zX4)**

You think robots are still sci-fi? Think again. I'm at the this year's Canton Fair to show you the reality of the Chinese automation ...

📺 Eric Cracks China

👁️ 97K • 👍 3K • 💬 152 • ⏱️ 1:54 • 2d ago

---

**[Humanoid Robot Beats Human Record in Beijing](https://www.youtube.com/watch?v=XWmVqXpF84A)**

Bloomberg's Minmin Low highlights a half marathon held in Beijing, where autonomous robots showcased significant ...

📺 Bloomberg Television

👁️ 20K • 👍 413 • 💬 130 • ⏱️ 5:51 • 11h ago

---

**[Should You Kill Robots With Liquid Nitrogen?](https://www.youtube.com/watch?v=1uNHprtb1Ik)**

See the full video here https://www.youtube.com/watch?v=A0gB3trtxkU.

📺 Action Lab Shorts

👁️ 59K • 👍 3K • 💬 107 • ⏱️ 1:26 • 2d ago

---

**[Boston Dynamics Won The AI Robot Race With This One Move](https://www.youtube.com/watch?v=7bPZJhhDQU4)**

Boston Dynamics just did what most people thought would take years longer. Atlas is now entering real serial production, the ...

📺 AI Revolution

👁️ 145K • 👍 3K • 💬 218 • ⏱️ 21:49 • 6d ago

---

**[weldingRobot #Robot #WeldingRobot #robot #robotfactory #lndustrialrobot](https://www.youtube.com/watch?v=BtdwdjAFP1o)**

📺 RobotMiketwo

👁️ 33K • 👍 286 • 💬 10 • ⏱️ 0:29 • 3d ago

---

**[The humanoid robot, known as Edward Warchocki, was filmed chasing boars in Warsaw, Poland. #BBCNews](https://www.youtube.com/watch?v=AmLPpSx8OMQ)**

📺 BBC News

👁️ 219K • 👍 2K • 💬 297 • ⏱️ 0:25 • 5d ago

---

**[Humanoid robot chases wild boar herd in Poland](https://www.youtube.com/watch?v=u8-l_NHUTEk)**

On the streets of Warsaw, Poland, a humanoid robot named Edward Warchocki was filmed chasing away a herd of wild boars.

📺 CGTN America

👁️ 35K • 👍 341 • 💬 59 • ⏱️ 0:30 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

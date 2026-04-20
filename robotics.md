---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-20T08:09:54.656093+00:00'
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

**Last Updated:** April 20, 2026 at 08:09 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[2026 robot half marathon fail & fun compilation](https://www.reddit.com/r/robotics/comments/1sqd2ag/2026_robot_half_marathon_fail_fun_compilation/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2045896309765288179

5h ago

---

**[Many of the finish times have been revised upward (by 10–15 seconds) – Maintenance and battery replacement like F1](https://www.reddit.com/r/robotics/comments/1spq0zh/many_of_the_finish_times_have_been_revised_upward/)**

From 小互 on 𝕏: "Feels a bit like F1": https://x.com/xiaohu/status/2045786816213815411

21h ago

---

**[How did so many Chinese robot manufacturers catch up to Boston Dynamics?](https://www.reddit.com/r/robotics/comments/1sq2bzn/how_did_so_many_chinese_robot_manufacturers_catch/)**

They had been working on their designs for years and I don't think they publish proprietary information so how is it that there are so many manufacturers with humanoid and 'Spot-form' robots that seem to be equal or outperform Boston Dynamics?

12h ago

---

**[Update on Cubic Doggo: man, walking is hard](https://www.reddit.com/r/robotics/comments/1sq4rip/update_on_cubic_doggo_man_walking_is_hard/)**

Update from the previous post: https://www.reddit.com/r/robotics/comments/1rouerc/first_time_building_a_hobbyist_robot_from_scratch/ Added control since last time, which is actually the easy part with ROS2. I am also surprised by how versatile Dynamixel XL430-W250-T servos are; they even offer current-based position control that mimics the torque control. Hope their higher torque variants get cheaper over time. Made several iterations of the servos and battery arrangement to center the mass (redoing all the urdf is really quite something). Tried a few different walking gaits with IK calculated by ROS2, which I believe is oriented around position control, so a bit difficult to define arbitrary trajectories. Put on kitchen sponge clothes to increase friction on the feet. The previous attempt on all four feet twisted and broke off one leg, so now it sticks with only the two front legs. I think that is also why the back legs felt limp as a few screws went loose in that incident. Anyways, have a few things in mind to fix/try, and always welcome any recommendation: https://github.com/SphericalCowww/CubicDoggo

11h ago

---

**[Everyone saw the Honour robot win… but nobody noticed what it did right after](https://www.reddit.com/r/robotics/comments/1spy9lg/everyone_saw_the_honour_robot_win_but_nobody/)**

15h ago

---

**[Real-World Deployment as a Core Strategy in Robotics Development](https://www.reddit.com/r/robotics/comments/1sq3s5m/realworld_deployment_as_a_core_strategy_in/)**

Ali Kashani, founder and CEO of Serve Robotics and former head of robotics at Postmates X, has spent years deploying autonomous delivery robots in active urban environments. He mentions systems built only in controlled settings are based on assumptions. Once robots operate in public, those assumptions are tested immediately. People behave unpredictably, environments change, and situations come up that were never accounted for during development. Those conditions shape what actually needs to be solved. They expose gaps that do not appear in lab testing and force teams to prioritize what matters in real use.

11h ago

---

**[Honor’s humanoid fully autonomous robot "Lightning" from the Monkey King team won the 2026 Beijing Humanoid Robot Half Marathon on April 19. Among over 100 teams, it finished first with a net time of 50m26s.](https://www.reddit.com/r/robotics/comments/1sphe3h/honors_humanoid_fully_autonomous_robot_lightning/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2045678855638405436 https://x.com/XRoboHub/status/2045695900434276501

1d ago

---

**[What's your take on AI-generated environments for sim-to-real? HY-World 2.0 skips the video→3DGS→mesh chain entirely](https://www.reddit.com/r/robotics/comments/1sqivfr/whats_your_take_on_aigenerated_environments_for/)**

Tencent just open-sourced HY-World 2.0 (https://github.com/Tencent-Hunyuan/HY-World-2.0). The key difference from video world models like Genie 3 or Cosmos is that it outputs real 3D assets (meshes, 3DGS) that you can import into Isaac Sim, Unity, Unreal, not just pixel videos. I've spent time trying to go from video world models → 3DGS → meshes and the information loss along the way is brutal. You end up with hole-y environments full of weird artifacts. WorldLabs' Marble was better because it generates 3DGS directly, but then the mesh conversion still sucked. I built my own conversion pipeline for their outputs and still wasn't happy with it. HY-World 2.0 skipping that whole chain and outputting usable 3D directly is a big deal if the quality holds up. For robotics sim specifically: this could be solid for fast environment generation and domain randomization. If you need a bunch of varied training environments quickly, this kind of tool gets you there. It won't replace handcrafted digital twins for teams that need hyperrealistic sim-to-real fidelity, but for the "I need 200 warehouse variations for my policy to generalize" use case, it could be a real speedup. Anyone else tried running the WorldMirror 2.0 reconstruction yet? Curious how the outputs actually look in a sim engine.

9m ago

---

**[New Robotis Humanoid](https://www.reddit.com/r/robotics/comments/1spuiai/new_robotis_humanoid/)**

Robotis just revealed their new QDD actuators and their new open source humanoid robot. This robot very closely resembles Unitree G1, but it is totally open source in both hardware and software. I heard that the pricing will be competitive as well.

🔗 [LinkedIn](https://www.linkedin.com/posts/yoonseokpyo_this-is-robotiss-open-source-entry-level-activity-7451595734975557632-eLLl/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEP9kBABMMZZVzJTJhId4-134XyBuXENZws) • 17h ago

---

**[Reprogrammable artificial muscle can change its shape, recover from damage, and even be reused](https://www.reddit.com/r/robotics/comments/1sq1mki/reprogrammable_artificial_muscle_can_change_its/)**

A research team in South Korea created an artificial muscle that can be reshaped during use, recover after damage, and even have part of its material reused in another device.

🔗 [The Brighter Side of News](http://thebrighterside.news/post/reprogrammable-artificial-muscle-can-change-its-shape-recover-from-damage-and-even-be-reused) • 13h ago

---

---

## Google News: "robotics"

**[Humanoid robots race past humans in Beijing half-marathon, showing rapid advances](https://www.reuters.com/sports/humanoid-robots-race-past-humans-beijing-half-marathon-showing-rapid-advances-2026-04-19/)**

Reuters • 1d ago

---

**[Exclusive: Your delivery robot will now offer the blind real-time, on-the-ground eyes around sidewalk hazards](https://fortune.com/2026/04/20/coco-delivery-robots-blind-users-blindsquare-hazards-sidewalk/)**

Coco Robotics is partnering with BlindSquare, the world's most popular GPS app for the blind, to turn data from delivery robots into spoken alerts.

Fortune • 1h ago

---

**[Tools for Your To Do List with Spot and Gemini Robotics](https://bostondynamics.com/blog/tools-for-your-to-do-list-with-spot-and-gemini-robotics/)**

A recent demo shows Boston Dynamics Spot in a residential home, using Google’s visual-language model (VLM) Gemini Robotics-ER 1.5 for embodied reasoning.

Boston Dynamics • 2h ago

---

**[Alabama Considers Robotics to Augment Rural Obstetrics Care](https://dailyyonder.com/alabama-considers-robotics-to-augment-rural-obstetrics-care/2026/04/20/)**

The Daily Yonder • 43m ago

---

**[NVIDIA and QNX target safer robots and medical devices with edge AI](https://www.stocktitan.net/news/BB/qnx-and-nvidia-deepen-collaboration-to-advance-safety-critical-edge-2fpnzowdrzx3.html)**

Using IGX Thor and Halos Safety Stack, the platform combines real-time control with AI, supporting safety certification. Early access is now open.

Stock Titan • 2h ago

---

**[FAMU Hosted Global High School Stem Athletes Who Competed To Qualify For First® International Robotics Championship - Florida A&M University](https://news.famu.edu/2025/famu-hosted-global-high-school-stem-athletes-who-competed-to-qualify-for-first-international-robotics-championship.php)**

Florida A&M University - FAMU • 13h ago

---

**[Neptune Robotics Invests US$12mn in New Singapore Factory to Drive Five-Fold Increase in Autonomous Ship Hull Cleanings](https://www.prnewswire.com/apac/news-releases/neptune-robotics-invests-us12mn-in-new-singapore-factory-to-drive-five-fold-increase-in-autonomous-ship-hull-cleanings-302746872.html)**

/PRNewswire/ -- Neptune Robotics ("Neptune"), a pioneer in AI-powered robotic hull cleaning services with a presence in 61 ports across Singapore and China,...

PR Newswire • 3h ago

---

**[Chinese robotics stocks mixed after Beijing half-marathon showcases humanoid tech](https://www.investing.com/news/stock-market-news/chinese-robotics-stocks-mixed-after-beijing-halfmarathon-showcases-humanoid-tech-4622298)**

Investing.com • 4h ago

---

**[Hutto ISD sending two teams to robotics world championship](https://www.kxan.com/news/hutto-isd-sending-two-teams-to-robotics-world-championship/)**

KXAN Austin • 11h ago

---

**[Northwest Arkansas teams gearing up for VEX Robotics World Championship in St. Louis](https://www.arkansasonline.com/news/2026/apr/19/northwest-arkansas-teams-gearing-up-for-vex/)**

Robotics students across Northwest Arkansas are getting ready to compete on the world stage this week.

The Arkansas Democrat-Gazette • 6h ago

---

---

## YouTube Videos: "robotics"

**[The GPT Moment for Robotics Is Here](https://www.youtube.com/watch?v=4EsUaur0nsQ)**

Physical Intelligence is building a foundation model that can control any robot to do any task — what the team describes as the ...

📺 Y Combinator

👁️ 44K • 👍 1K • 💬 57 • ⏱️ 49:27 • 3d ago

---

**[A humanoid robot is seen chasing a group of wild boars off the street](https://www.youtube.com/watch?v=yyCmTL-wC-w)**

For more context and news coverage of the most important stories of our day, click here: https://www.nbcnews.com » Subscribe to ...

📺 NBC News

👁️ 231K • 👍 4K • 💬 309 • ⏱️ 0:25 • 5d ago

---

**[The Future is Mass-Produced: Inside the Canton Fair Robotics Hall](https://www.youtube.com/watch?v=S0eEXTn3zX4)**

You think robots are still sci-fi? Think again. I'm at the this year's Canton Fair to show you the reality of the Chinese automation ...

📺 Eric Cracks China

👁️ 95K • 👍 3K • 💬 150 • ⏱️ 1:54 • 2d ago

---

**[Robot in Poland scares off wild boars](https://www.youtube.com/watch?v=BmwTEOGb88k)**

A humanoid robot named Edward Warchocki chased away a herd of wild boars in Warsaw, shouting "Go away!" in Polish as the ...

📺 Reuters

👁️ 45K • 👍 680 • 💬 77 • ⏱️ 0:26 • 5d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=v45_LCDH6gk)**

📺 Robot Julie 

👁️ 10K • 👍 72 • 💬 5 • ⏱️ 0:21 • 7h ago

---

**[Tesla Just Started Mass Producing Humanoid Robots — And Nobody Is Ready](https://www.youtube.com/watch?v=2sHaQffX0w0)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *Tesla ...

📺 Julia McCoy

👁️ 84K • 👍 2K • 💬 321 • ⏱️ 4:16 • 5d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 72K • 👍 1K • 💬 140 • ⏱️ 16:14 • 3d ago

---

**[I Made a 3D Printed Gearbox. #3dprinting #gearbox #robotics #steppermotor](https://www.youtube.com/watch?v=vYnedIup1Nk)**

I made a 3D printed gearbox for a Nema 17 stepper motor. I released the 3D files on Printables.com. Checkout the full video for ...

📺 Advanced Hobby Lab

👁️ 96K • 👍 1K • 💬 12 • ⏱️ 0:27 • 2d ago

---

**[Drag-and-drop welding robot.#welding #industry #stamping #robot #polish](https://www.youtube.com/watch?v=ZMOHebvddcY)**

📺 Robot Linda 

👁️ 24K • 👍 163 • 💬 3 • ⏱️ 0:30 • 2d ago

---

**[The humanoid robot, known as Edward Warchocki, was filmed chasing boars in Warsaw, Poland. #BBCNews](https://www.youtube.com/watch?v=AmLPpSx8OMQ)**

📺 BBC News

👁️ 215K • 👍 2K • 💬 291 • ⏱️ 0:25 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

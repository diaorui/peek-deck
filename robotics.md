---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-24T05:56:34.119376+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** December 24, 2025 at 05:56 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Disney: Olaf: Bringing an Animated Character to Life in the Physical World (Demo - Paper)](https://www.reddit.com/r/robotics/comments/1pts3ka/disney_olaf_bringing_an_animated_character_to/)**

Paper: Olaf: Bringing an Animated Character to Life in the Physical World arXiv:2512.16705 [cs.RO]: https://arxiv.org/abs/2512.16705

18h ago

---

**[Deep dive into Disney’s Self-Roaming Olaf Robot](https://www.reddit.com/r/robotics/comments/1pu4xx9/deep_dive_into_disneys_selfroaming_olaf_robot/)**

8h ago

---

**[Bio-hybrid Robots: Turns Food waste into High-Performance Functional Machines](https://www.reddit.com/r/robotics/comments/1ptqsal/biohybrid_robots_turns_food_waste_into/)**

Researchers at EPFL’s CREATE Lab are now repurposing langoustine exoskeletons to build high-performance, biodegradable robots. By combining these natural shells with artificial tendons and soft rubber, they have created a new class of sustainable bio-hybrid machines. Extreme Strength: These actuators can lift over 100 times their own mass without structural failure. High Frequency: The shells function as high-speed bending actuators operating at up to 8 Hz. Versatile Locomotion: Testing includes robotic grippers for delicate tasks (like cherries) and swimming robots that reach speeds of 11 cm/s. This approach solves the difficulty of replicating complex biological joints with synthetic materials while using waste from the food industry to create fully biodegradable components. Sources: Full Article: https://robohub.org/bio-hybrid-robots-turn-food-waste-into-functional-machines/ Demonstration: https://youtu.be/VfTn-1KY61Q

19h ago

---

**[Will humanoid robots outshine the alternatives?](https://www.reddit.com/r/robotics/comments/1pu6h78/will_humanoid_robots_outshine_the_alternatives/)**

The great revelation I had at the beginning of my robotics career (circa 1982) was that roboticists were loving robots to death. “General-purpose” was the watchword of the day and most roboticists aimed to achieve it by lovingly lashing as much technology onto their platforms as they could. The result was no-purpose robots. In controlled situations designers could conduct cool demonstrations but their robots offered no real-world utility, and none succeeded in the marketplace. The Roomba team (I was a member) stood that conventional idea on its head. We deliberately built a robot that had just one function and we stripped out every nonessential bit of technology so we could achieve a price comparable to manual vacuum cleaners. That strategy worked pretty well. Today there seems to be a great resurgence in the quest for general-purpose robots. This time it’s different, or so enthusiasts say, because of AI. But to my ancient sensibilities, focusing on technology and leaving the actual tasks to AI magic sets alarm bells ringing. The critical question isn’t whether a humanoid robot can perform a particular task or set of tasks. Rather, it’s what solution or set of solutions will the marketplace reward? When thinking (and investment) is limited to the solution space of humanoids, creators may find themselves blindsided by bespoke robots or multi-purpose robots that don’t resemble humans. I’m wondering how current practitioners in the field see things. Should humanoids be receiving the lion’s share of effort and cash or do you think their chief talent their ability to seduce money from investors?

7h ago

---

**[Most days building a humanoid robot look like this](https://www.reddit.com/r/robotics/comments/1ptqfy6/most_days_building_a_humanoid_robot_look_like_this/)**

Emre from Menlo Research here. What you're seeing is how we learn to make humanoids walk. It's called Asimov and will be an open-source humanoid. We're building a pair of humanoid legs from scratch, no upper body yet. Only enough structure to explore balance, control, and motion, and to see where things break. Some days they work, some days don't. We iterate quickly, change policies, play with the hardware and watch how it behaves. Each version is a little different. Over time, those differences add up. We'll be sharing docs soon once the website is ready. We're documenting the journey day by day on. If you're curious to follow along, please join our community to be part of it: https://discord.gg/HzDfGN7kUw

19h ago

---

**[Sunday Robotics Memo: "Pick Up Anything" test](https://www.reddit.com/r/robotics/comments/1ptkti2/sunday_robotics_memo_pick_up_anything_test/)**

From Sunday on 𝕏: https://x.com/sundayrobotics/status/2003294087236190623 Website: https://www.sunday.ai/

1d ago

---

**[Built a tool that uses AI to catch URDF errors visually - looking for honest feedback](https://www.reddit.com/r/robotics/comments/1pu9cke/built_a_tool_that_uses_ai_to_catch_urdf_errors/)**

I've been working on a desktop app called Artifex for generating robot descriptions from natural language. The part I'm most interested in feedback on is the visual verification loop: **How it works:** 1. User describes a robot in plain English 2. AI generates the URDF (using structured output with Zod schemas for validation) 3. The 3D viewport renders the robot using React Three Fiber 4. AI takes a screenshot of the render via MCP tool call 5. AI analyzes the image for errors - wrong joint axes, scale mismatches, parts facing the wrong way 6. AI fixes what it finds and re-renders 7. Export to a colcon-ready ROS2 package The "AI looking at its own output" loop is the part I'm genuinely unsure about. In my testing it catches things like cameras mounted upside-down or wheel axes pointing the wrong direction. But I don't know if this is solving a real problem or just a gimmick. **Questions for this community:** - Does the visual verification seem useful, or is it solving a problem that doesn't really exist? - What URDF errors do you actually run into that are hard to catch? - Any obvious gaps in this workflow? **Disclosure:** I'm the developer. This is a commercial project but the tool is free to download. Happy to share a link if anyone wants to try it, but mainly here because I don't know if I'm building something people actually need. Roast away - honest feedback is more valuable than polite encouragement.

5h ago

---

**[Physical Intelligence (π) launches the "Robot Olympics": 5 autonomous events demonstrating the new π0.6 generalist model](https://www.reddit.com/r/robotics/comments/1pt6ouz/physical_intelligence_π_launches_the_robot/)**

Physical Intelligence just released a series of "Robot Olympics" events to showcase their latest π0.6 model. Unlike standard benchmarks, these tasks are designed to illustrate Moravec’s Paradox which are everyday physical actions that are trivial for humans but represent the "gold standard" of difficulty for modern robotics. All tasks shown are fully autonomous, demonstrating high-level task decomposition and fine motor control. The 5 Olympic Events: Event 1 (Gold) - Door Entry: The robot successfully navigates a self-closing lever-handle door. This is technically challenging because it requires the model to apply force to keep the door open while simultaneously moving its base through the frame. Event 2 (Silver) - Textile Manipulation: The model successfully turns a sock right-side-out. They attempted the Gold medal task (hanging an inside-out dress shirt), but the current hardware gripper was too wide for the sleeves. Event 3 (Gold) - Fine Tool Use: A major win here,the robot used a small key to unlock a padlock. This requires extreme precision to align the key and enough torque to turn the tumbler. (Silver was making a peanut butter sandwich, involving long-horizon steps like spreading and cutting triangles). Event 4 (Silver) - Deformable Objects: The robot successfully opened a dog poop bag. This is notoriously difficult because the thin plastic blinds the wrist cameras during manipulation. They attempted to peel an orange for Gold but were "disqualified" for needing a sharper tool. Event 5 (Gold) - Complex Cleaning: The robot washed a frying pan in a sink using soap and water, scrubbing both sides. They also cleared the Silver (cleaning the grippers) and Bronze (wiping the counter) tasks for this category. The Tech Behind It: The π0.6 model is a Vision-Language-Action (VLA) generalist policy. It moves away from simple "behavior cloning" and instead focuses on agentic coding and task completion, allowing it to recover from errors and handle diverse, "messy" real-world environments. Official Blog: pi.website/blog/olympics Source Video: Physical Intelligence on X

1d ago

---

**[Resources to get ready for an Undergraduate Researcher Interview](https://www.reddit.com/r/robotics/comments/1pu4xp0/resources_to_get_ready_for_an_undergraduate/)**

8h ago

---

**[I built the MVP for the block-based ROS2 IDE. Here is the Rviz integration in action!](https://www.reddit.com/r/robotics/comments/1pu1dco/i_built_the_mvp_for_the_blockbased_ros2_ide_here/)**

11h ago

---

---

## Google News: "robotics"

**[Hyundai Motor Group to Unveil AI Robotics Strategy at CES 2026](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001093)**

Hyundai Motor Group released a teaser image previewing its upcoming participation at CES 2026

hyundai.com • 1d ago

---

**[Eve Energy breaks ground on sodium battery headquarters and robotics center](https://cnevpost.com/2025/12/23/eve-energy-breaks-ground-sodium-battery-headquarters-robotics-center/)**

Eve Energy will invest about RMB 1 billion ($140 million) in this sodium-ion battery project, with an annual production capacity planned at 2 GWh.

CnEVPost • 1d ago

---

**[Wilton Dominates State Championship in Robotics, Again Ascends to World Competition](https://goodmorningwilton.com/wilton-robotics-teams-win-state-championship-dec-2025/)**

Wilton teams shine at the FIRST Lego League Robotics State Championships. Allied Algorithms won the championship and Singularity Technology Juniors earning the Motivate Award.

Good Morning Wilton • 2d ago

---

**[Robotics in review: Editors look back at 2025](https://www.therobotreport.com/robotics-in-review-editors-look-back-at-2025/)**

The editorial team reviews 2025’s top robotics stories, including iRobot’s bankruptcy, the humanoid boom, and Waymo’s scaling.

The Robot Report • 9h ago

---

**[Robotic system synthesizes hundreds of metal complexes to find potential new antibiotic](https://phys.org/news/2025-12-robotic-hundreds-metal-complexes-potential.html)**

Phys.org • 19h ago

---

**[Top 5 Viral Humanoid Moments That Made 2025 The Year Of Robotics](https://seekingalpha.com/article/4855343-top-5-viral-humanoid-moments-made-2025-year-of-robotics)**

The KOID ETF is designed to capture the broad opportunity in the robotics and embodied intelligence ecosystem. Read more here.

Seeking Alpha • 18h ago

---

**[European firm to deploy humanoid robots in semiconductor production for first time](https://interestingengineering.com/ai-robotics/humanoid-robots-to-join-chip-production-factories)**

Swiss semiconductor firm STMicroelectronics has signed an agreement with Oversonic Robotics to deploy cognitive robots in factories.

Interesting Engineering • 17h ago

---

**[Scientists built a robotic claw using shrimp — and it outperforms synthetic versions](https://www.futura-sciences.com/en/scientists-built-a-robotic-claw-using-shrimp-and-it-outperforms-synthetic-versions_22465/)**

Swiss scientists have done something truly unexpected: they’ve created robotic fingers using leftover crustacean shells. The result is a robotic claw that’s not only efficient but also eco-friendly and cheap — a sustainable twist in ... Read more

Futura, Le média qui explore le monde • 17h ago

---

**[It's official—China deploys humanoid robots at border crossings and commits to round-the-clock surveillance and logistics](https://eladelantado.com/en/humanoid-robot-china/)**

China has been teaching humanoid robots in its country's decision-making rooms for years. Now they have been taken to a much more practical, albeit dystopian,

El Adelantado • 1d ago

---

**[The Tech Review 2025: China sees breakthroughs in AI and robotics](https://news.cgtn.com/news/2025-12-23/The-Tech-Review-2025-China-sees-breakthroughs-in-AI-and-robotics-1JkPp0QUWl2/p.html)**

The year 2025 has been defined by a wave of transformative advances in China's artificial intelligence (AI) and robotics sectors, marking a decisive shift from laboratory research toward deep industrial integration and real-world application.The year

news.cgtn.com • 20h ago

---

---

## YouTube Videos: "robotics"

**[AI ROBOTS Are Now TOO REAL! - Shocking AI &amp; Robotics 2025 Updates](https://www.youtube.com/watch?v=a4Y_VVuqYyk)**

The world of AI and robotics accelerated faster this year than almost anyone expected. Humanoid robots became cheaper, faster, ...

📺 AI Revolution

👁️ 44K • 👍 799 • 💬 80 • ⏱️ 2:08:46 • 4d ago

---

**[How STRONG Are Humanoid Robots Really? (And Why It&#39;s Hard to Tell)](https://www.youtube.com/watch?v=PGRJg5eExO4)**

China's got a new Terminator robot and Figure is facing a lawsuit alleging its robots are strong enough to "fracture a human skull.

📺 CNET

👁️ 36K • 👍 610 • 💬 148 • ⏱️ 5:25 • 2d ago

---

**[This Rolling Robot Could Replace Police in the Future](https://www.youtube.com/watch?v=wKWUTIHGQZk)**

FutureTech #Robotics #LawEnforcement.

📺 Skye Ocean Girl

👁️ 30K • 👍 147 • 💬 6 • ⏱️ 0:19 • 2d ago

---

**[Robotics Could Actually HELP End Poverty?  | Episode #117](https://www.youtube.com/watch?v=jS_wekM_Zvs)**

Waking Up | 30 Day FREE TRIAL- wakingup.com/drmike Dr. Mike chats about all things progress, especially technology, futurism, ...

📺 Mike Israetel

👁️ 4K • 👍 232 • 💬 70 • ⏱️ 49:59 • 1d ago

---

**[INSANE AI Curling Robot in Dubai😱💇🏼‍♀️Automatic Perm Tach From the Future!](https://www.youtube.com/watch?v=eFeyyTAyxMI)**

ai #beauty #hair #curling #coloring #robot #tachnology #viral #dubai #future #hairstyle #salon #trnding #shorts #transformation ...

📺 Ai BOOF

👁️ 21K • 👍 241 • 💬 4 • ⏱️ 0:11 • 20h ago

---

**[TRON 2 Officially Launched | Redefining the Foundation of Embodied Robotics](https://www.youtube.com/watch?v=Ut3QFPr7hyo)**

Cutting-edge Algorithms, At Your Fingertips. Explore More: https://www.limxdynamics.com/en/tron2 #limxdynamics #limxtron2 ...

📺 LimX Dynamics

👁️ 1.1M • 👍 11K • 💬 655 • ⏱️ 2:43 • 5d ago

---

**[His Self-Aware Robot Escaped ...](https://www.youtube.com/watch?v=e7fkeontbaE)**

I got a little bit bored so His Self-Aware Robot Escaped SUBSCRIBE TO OG @LIGHTSAREOFF New Merch https://socks.store/ ...

📺 SocksReact

👁️ 579K • 👍 10K • 💬 1K • ⏱️ 18:35 • 3d ago

---

**[Futuristic dancing robot&#39;s in china.....#dance](https://www.youtube.com/watch?v=7drSENm6rpQ)**

future stick dancing robots in China robots can dance like a human robots dance leke better than human China's robots that ...

📺 Santoshgian

👁️ 42K • 💬 4 • ⏱️ 0:26 • 1d ago

---

**[INSANE AI Curling Robot in Dubai😱💇🏼‍♀️Automatic Perm Tach From the Future!](https://www.youtube.com/watch?v=8PfHGA1Rjt8)**

ai #beauty #hair #curling #coloring #robot #tachnology #viral #dubai #future #hairstyle #salon #trnding #shorts #transformation ...

📺 Ai BOOF

👁️ 4K • 👍 49 • 💬 2 • ⏱️ 0:11 • 13h ago

---

**[The Robot That ESCAPED...](https://www.youtube.com/watch?v=eYAprc8mGvQ)**

Disturbing Robot Thinks It's Human.. Hope yall enjoyed the vid! If you did consider liking and subscribing for more ...

📺 Aimin

👁️ 1.1M • 👍 21K • 💬 4K • ⏱️ 14:27 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

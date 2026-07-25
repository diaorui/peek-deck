---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-25T07:17:25.977282+00:00'
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

**Last Updated:** July 25, 2026 at 07:17 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Unitree “Super Athlete" AS2-W (wheeled-leg variant of the AS2)](https://www.reddit.com/r/robotics/comments/1v582o5/unitree_super_athlete_as2w_wheeledleg_variant_of/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2080549171661295907 - Weight: ~25 kg with battery. - Speed: Over 6 m/s (higher than the pure-legged As2). - Payload: Continuous ~16 kg; higher static capacity. - Endurance: Unloaded >3 hours / 30+ km; loaded (>16 kg) >2 hours / >16 km. Same 648 Wh (15,000 mAh) battery class as the As2. - Mobility: Up to ~80 cm obstacles, 45° slopes, 30 cm stairs; strong on gravel, rocky, and uneven outdoor terrain. https://www.unitree.com/As2-W

20h ago

---

**[Bob (my robot) died 😢 I tried consolidating 2 LiPo batteries into a 1 larger one and fried its Raspberry Pi brains. I'm gonna rebuild him with a Nvidia Jetson brain and RealSense D457 GMSL camera.](https://www.reddit.com/r/robotics/comments/1v5faas/bob_my_robot_died_i_tried_consolidating_2_lipo/)**

15h ago

---

**[Embodied AI is getting scary cheap. We just got our sub-$1,000 open-source robot (AlohaMini2) to do autonomous mobile manipulation trained on a consumer 8GB GPU.](https://www.reddit.com/r/robotics/comments/1v535b3/embodied_ai_is_getting_scary_cheap_we_just_got/)**

Hey everyone, A while back, I posted here asking for advice on my $149 metal cycloidal actuator project. A lot of folks asked me why I was so obsessed with pushing the hardware BOM cost down so aggressively. Well, this video is exactly why. My co-founder Yiteng and I just released AlohaMini2. To our knowledge, it's the first sub-$1,000 self-build BOM robot capable of end-to-end, long-horizon autonomous tasks (like this grocery manipulation). Here is the technical takeaway that I think will interest this community: The Compute Barrier is Gone: This wasn't trained on a server farm. The AM-ACT policy was trained and deployed entirely on a standard 8GB consumer GPU. Data Efficiency: It only took 50 human demonstration episodes to reach a 50% end-to-end success rate on this specific long-horizon task. We are open-sourcing the entire repo (hardware files & codebase) because we want to prove that you don't need a multi-million-dollar lab to play with cutting-edge Embodied AI anymore. The Real Bottleneck Now? Hardware Reliability. While the software/policy side is moving at lightspeed, keeping a $1,000 robot mechanically alive during 24/7 RL training is a nightmare. 3D printed gears strip, cheap servos overheat. That’s exactly what drove me to start designing metal actuators in the first place. Repo link for anyone who wants to build one or dive into the code:https://github.com/liyiteng/AlohaMini I’m curious—if the software barrier is this low now, what tasks would you guys train a cheap $1k robot to do at home?

1d ago

---

**[[Project] Reproducing NVIDIA’s Isaac Lab-to-VLA pipeline with 50 remotely collected VR demonstrations](https://www.reddit.com/r/robotics/comments/1v5ewia/project_reproducing_nvidias_isaac_labtovla/)**

I’m part of the team that ran this experiment at Sim XR. Sharing it here as a technical project rather than a product announcement. We started by reproducing NVIDIA’s published Isaac Lab → LeRobot → VLA fine-tuning → Arena evaluation workflow for the Unitree G1 apple task. In our matched simulation evaluation: checkpoint trained on 208 usable released demonstrations: 93/100 checkpoint trained on 50 demonstrations we collected remotely through VR: 84/100 We then moved the task to the other side of the workspace. Both existing policies scored 0/20. After collecting targeted demonstrations for the new layout, the best result reached 74/100. Finally, we replaced the apple task with a cross-body mustard-bottle-to-bowl task: released apple checkpoint: 0/30 checkpoint fine-tuned on 50 new VR demonstrations: 27/30 These are simulation results, not a real-robot or sim-to-real claim. The interesting part for us was how sensitive the policies remained to layout changes—and how quickly targeted demonstrations could recover useful behavior. I’d be interested to hear how others are evaluating layout shifts and deciding where additional demonstrations are most useful.

15h ago

---

**[Claude Code skills for ROS 2 Jazzy that route to official docs instead of guessing APIs (measured before/after included)](https://www.reddit.com/r/robotics/comments/1v5h7ud/claude_code_skills_for_ros_2_jazzy_that_route_to/)**

14h ago

---

**[Human Fall Detection By 3D Dtof LIDAR HM-LD1](https://www.reddit.com/r/robotics/comments/1v5crci/human_fall_detection_by_3d_dtof_lidar_hmld1/)**

16h ago

---

**[New AMD Robotics SoC: X100 - 128GB Unified Memory](https://www.reddit.com/r/robotics/comments/1v57zsa/new_amd_robotics_soc_x100_128gb_unified_memory/)**

Saw on blog by Steve Macenski: https://opennav.org/news/opennav-robotics-workload-benchmark/ running extended ROS 2 workloads. Pretty cool HW-wise, especially with recent Jetson 50-100% price increase. Hopefully AMD won't price it same as new Thor price 👀 Also vote if you can what HW you use to run ROS (if you use ROS)

🔗 [AMD](https://www.amd.com/en/products/system-on-modules/kria/ai.html) • 20h ago

---

**[I built a real Wall-E](https://www.reddit.com/r/robotics/comments/1v5dvxn/i_built_a_real_walle/)**

I made this real life Wall-E robot from scratch and am really proud of it so check my youtube video about it out if you would like

🔗 [youtu.be](https://youtu.be/zddu86VGEX0?si=zm1kSBUPQm3cokhk) • 16h ago

---

**[[Collab] Anyone in Houston wants to team up on a robot project](https://www.reddit.com/r/robotics/comments/1v5lcnb/collab_anyone_in_houston_wants_to_team_up_on_a/)**

Hey everyone, I’m currently working on a robot project and was wondering if anyone in the Houston, Texas area would like to join forces. The idea is to combine skills, share knowledge, and build something awesome together. I have the engineering background and some parts already, but I’d love to connect with people who are into robotics, coding, AI, electronics, or even just tinkering and learning. Whether you’re a student, hobbyist, or professional, collaboration makes projects way more fun (and productive). If you’re interested in teaming up or just want to chat about robots, feel free to DM me or drop a comment

11h ago

---

**[ROS News for the Week of July 20th, 2026 - Community News](https://www.reddit.com/r/robotics/comments/1v5l6a5/ros_news_for_the_week_of_july_20th_2026_community/)**

ROS News for the week of July 20th, 2026                      I’ve had quite the week! In the past seven days, I’ve been to Open Sauce, AMD’s developer conference, and now I’m at Teardown in Portland. It might have also been my birthday this week. 🎂  I’ve run into so many fantastic people building wonderful ROS robots, including a working Johnny 5 replica, a giant art robot with cast aluminum components, a hexapod with a 25 kg payload, a room full of SO-101s, a controllable robot t...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-july-20th-2026/56937) • 11h ago

---

---

## Google News: "robotics"

**[The Robots Cometh](https://time.com/article/2026/07/23/unitree-china-human-robotics/)**

The humanoid revolution is coming—and the Chinese firm Unitree is leading the charge.

Time Magazine • 1d ago

---

**[What's Next for Humanoids After This Week's Cage Match and Cowboying?](https://spectrum.ieee.org/video-friday-physical-ai-robotics)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 11h ago

---

**[This Silicon Valley city is quietly becoming Robot Row. Here's who's clanking around.](https://www.businessinsider.com/robot-row-humanoid-hub-location-fremont-silicon-valley-agility-tesla-2026-7)**

A growing number of robotics companies now have a footprint in Fremont, which sits at the intersection of Silicon Valley talent and manufacturing.

Business Insider • 23h ago

---

**[US eyes ban on Chinese humanoid robots as US-China tech rivalry intensifies](https://www.scmp.com/tech/policy/article/3361622/us-eyes-ban-chinese-humanoid-robots-us-china-tech-rivalry-intensifies)**

South China Morning Post • 1d ago

---

**[Eric Trump-backed Foundation partners with AMD to develop humanoid robots](https://www.reuters.com/business/eric-trump-backed-foundation-partners-with-amd-develop-humanoid-robots-2026-07-23/)**

Reuters • 1d ago

---

**[U.S. Robotics Leadership Is Not Guaranteed](https://www.piratewires.com/p/us-robotics-leadership-is-not-guaranteed)**

Pirate Wires • 1d ago

---

**[For The First Time Ever, Humanoid Robots Perform Surgery on Live Animals](https://www.sciencealert.com/world-first-humanoid-robots-perform-surgery-on-live-animals-this-could-prove-useful-in-space)**

For the first time ever, humanoid robots operated by surgeons have successfully performed laparoscopic gallbladder removal in pigs.

ScienceAlert • 2d ago

---

**[A spider-inspired robotic boat could track and rescue people in water](https://techxplore.com/news/2026-07-spider-robotic-boat-track-people.html)**

Tech Xplore • 18h ago

---

**[Tech Moves: Agility Robotics gets CFO; Microsoft security departure; Zap's legal officer; new KEXP CPTO](https://www.geekwire.com/2026/tech-moves-agility-robotics-gets-cfo-microsoft-security-departure-zaps-legal-officer-new-kexp-cto/)**

Agility Robotics names a CFO ahead of its plans to go public, moving its current CFO/COO into an operations-focused role. Microsoft loses another security leader while Zap Energy gets a chief legal officer.

GeekWire • 1d ago

---

**[This is the world’s most advanced robotic servicing satellite—that we know about](https://arstechnica.com/space/2026/07/this-is-the-worlds-most-advanced-robotic-servicing-satellite-that-we-know-about/)**

These are things that tend to be really hard."

Ars Technica • 15h ago

---

---

## YouTube Videos: "robotics"

**[A Silicon Valley company with Eric Trump as an advisor is making robot soldiers](https://www.youtube.com/watch?v=9O2iIZt25p4)**

One Silicon Valley company thinks that robot soldiers are the future of warfare. Eric Trump is an advisor and they've already got a ...

📺 NBC News

👁️ 15K • 👍 158 • 💬 90 • ⏱️ 5:29 • 2d ago

---

**[Real-Time Omni-Modal Interaction Driven Whole-Body Mobile Manipulation](https://www.youtube.com/watch?v=IiNbFPOUrz8)**

Unitree UnifoLM-OminiA-0.3 — a single model handling diverse home-care and wellness tasks, with omni-modal interactive ...

📺 Unitree Robotics

👁️ 2.7M • 👍 2K • 💬 422 • ⏱️ 2:15 • 4d ago

---

**[America Is Now Building Humanoid AI Robot Soldiers for War](https://www.youtube.com/watch?v=Qm64Vm-lf80)**

An American robotics startup is preparing humanoid AI robots for war. Its Phantom machines have already been tested in Ukraine, ...

📺 AI Revolution

👁️ 28K • 👍 759 • 💬 107 • ⏱️ 13:15 • 6d ago

---

**[World&#39;s First Robot Fighting Tournament Is Insane](https://www.youtube.com/watch?v=aZ6o3SrzCWo)**

Humanoid robots have officially stepped into the ring. Watch the world's first robot fighting tournament and see how artificial ...

📺 DPCcars

👁️ 49K • 👍 513 • 💬 191 • ⏱️ 4:18 • 6d ago

---

**[America Doesn&#39;t Know What&#39;s Coming...China&#39;s Robot Factories](https://www.youtube.com/watch?v=3UEfc0XqJJ0)**

America Doesn't Know What's Coming | China's Robot Factories Chengdu is usually known for pandas, hotpot, teahouses, old ...

📺 Living in China

👁️ 61K • 👍 2K • 💬 177 • ⏱️ 12:28 • 3d ago

---

**[Losing a Head Doesn&#39;t Stop This Robot From Battling Another in the Ring](https://www.youtube.com/watch?v=FEcPelBd9t0)**

Humanoid robots fought inside a cage at a tournament in China. The two exchange a fury of blows before the black robot loses it's ...

📺 New York Post

👁️ 43K • 👍 872 • 💬 389 • ⏱️ 2:02 • 2d ago

---

**[China’s T800 Robots Fight Just SHOCKED the World!](https://www.youtube.com/watch?v=QbnCPSLDkpw)**

A humanoid robot named Matador took a brutal high kick to the head, and its head rolled across the cage floor. Then Matador ...

📺 NextGen Humanoids

👁️ 19K • 👍 412 • 💬 81 • ⏱️ 8:56 • 5d ago

---

**[The Brothers Betting Their Robots Can Solve America&#39;s Welding Crisis | Path Robotics](https://www.youtube.com/watch?v=cI1XawnfEJE)**

America is running out of welders. By 2035, we'll lose 43% of America's welding workforce. @path_robotics is building robots to ...

📺 S3 | Science, Startups, & Stories

👁️ 38K • 👍 1K • 💬 98 • ⏱️ 14:37 • 6d ago

---

**[A Chinese Robot Just Decapitated Another Robot In Public. Nobody Asked What Comes Next](https://www.youtube.com/watch?v=rUjlFRok3qk)**

Everyone is asking if killer robots are coming. Wrong question. One already knocked another robot's head clean off, on camera ...

📺 Ambrose In China

👁️ 610K • 👍 22K • 💬 4K • ⏱️ 2:25 • 4d ago

---

**[Why China is dominating the humanoid robot race - Asia Specific podcast, BBC World Service](https://www.youtube.com/watch?v=8jXScBvrEJ0)**

Humanoid robots are suddenly everywhere - dancing, boxing, running marathons and even attempting surgery. China leads the ...

📺 BBC World Service

👁️ 18K • 👍 311 • 💬 97 • ⏱️ 18:15 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

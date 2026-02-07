---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-07T02:05:22.951754+00:00'
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

**Last Updated:** February 07, 2026 at 02:05 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Atlas, from Boston Dynamics, does gymnastics, lands on its toes, then performs a backflip.](https://www.reddit.com/r/robotics/comments/1qxdo57/atlas_from_boston_dynamics_does_gymnastics_lands/)**

From CyberRobo on 𝕏: https://x.com/CyberRobooo/status/2019598569909743755

16h ago

---

**[CasADi → native GPU kernels → Pytorch / Cupy / C++ [Batch 100K + evaluations in ms]](https://www.reddit.com/r/robotics/comments/1qxy5p7/casadi_native_gpu_kernels_pytorch_cupy_c_batch/)**

Just pushed an update to casadi-on-gpu that lets you generate CUDA kernels directly from CasADi and call them from C++, PyTorch, or CuPy. Useful for MPC, sampling, system ID, and robotics pipelines at scale.

2h ago

---

**[Would some of you guys here can help us with your workflows ??](https://www.reddit.com/r/robotics/comments/1qxyn1d/would_some_of_you_guys_here_can_help_us_with_your/)**

Hey guys, I'm not a robotics engineer. just a guy who got tired of watching some friends (robotics & mechatronics engineers) fight their own compute setups more than their actual problems. everyone’s on different ubuntu versions. ROS breaks. rviz crashes. Isaac sim won’t launch unless your gpu speaks fluent cuda and your drivers were blessed by a wizard. onboarding = 3 days of setup and maybe it works. so we built infinity. you open a browser ➜ you pick what you need- ros 2 humble + gazebo + rviz, or isaac sim + ros bridge, or whatever ➜ each app runs in its own gpu-accelerated container- clean, isolated, zero conflict But they’re networked together so you can stream data between them like they’re on your laptop. Also you can also toggle compute resources per application with just one click. It has a latency of <20ms (only in California). No install. No local config. what you could do with it: spin up isaac sim + ros 2 in separate containers, link them with a bridge, stream rviz in real-time -- no gpu needed on your side run two nav stacks (say, nav2 + custom planner) side by side and test them without touching your machine hand off a full ros + gazebo sim mid-debug -- your teammate clicks a link, jumps into the same exact setup test a vision pipeline on galactic, then instantly switch to humble and rerun -- no reboots, no docker give someone a link to a full robotics workspace -- it launches in their browser, and lidar + rviz just work this is for dev, sim, prototyping, tuning, testing- the part of robotics that usually breaks first nothing runs local. if it crashes, you refresh. if you mess up a config, you reset. we’re testing it with a couple of YC robotics teams in the bay, would love it , if some of you guys here can help us with your workflows :)

1h ago

---

**[Ball-and-Socket… But for Locomotion, Enchanted Tools](https://www.reddit.com/r/robotics/comments/1qx3nuo/ballandsocket_but_for_locomotion_enchanted_tools/)**

1d ago

---

**[Does anyone have experience with finetuning Huggingface's SmolVLA model on SO-101?](https://www.reddit.com/r/robotics/comments/1qxm907/does_anyone_have_experience_with_finetuning/)**

Hello everyone! Recently I tried to test the SmolVLA model from a paper that HuggingFace published, that uses relatively small VLA model for Imitation Learning on a SO-101 arm. They have a library called LeRobot that has a lot of stuff to handle robots. First I tried to run a pretrained model, which didn't work. Then I tried finetuning the model on a dataset that I collected. I gradually moved from 30 episodes to 120 with a simple task of picking up a cube and putting it in the designated place. The robot still can't solve the task at all and frankly does not improve with the increase in data amount. So my question is the following: have anybody experimented with LeRobot + smolvla + SO-101? What is your experience? Did you manage to run it? Basically, how much more time can I expect to sink into this or should I switch to another model, or from a robot to a simulator first, or something else?

9h ago

---

**[Cartwheel Robotics Shutdown- What Do You Think?](https://www.reddit.com/r/robotics/comments/1qxf32f/cartwheel_robotics_shutdown_what_do_you_think/)**

Cartwheel Robotics shutting down is a reminder of how misaligned capital can be. Great teams struggle for funding while massive checks keep flowing elsewhere. Scott’s advice hits home: “No money is better than the wrong money.” https://preview.redd.it/ov7omrf40vhg1.png?width=716&format=png&auto=webp&s=b0ce7c7ceaa4607cfdc5de89775cfcddf883c3fe

14h ago

---

**[Robotics engineer meets UX problems](https://www.reddit.com/r/robotics/comments/1qwo57d/robotics_engineer_meets_ux_problems/)**

Felt so excited to see the robot I've been working on getting this much attention. Guess I need to step up my UX game though :/

1d ago

---

**[Open-source CI gate + offline debug packets (seeking pilot teams or hobbyist creators)](https://www.reddit.com/r/robotics/comments/1qxt7da/opensource_ci_gate_offline_debug_packets_seeking/)**

Hey everyone — I’m a CS student working on an open-source tool called PF Gate that is supposed to be a supplement to the process of robotics debugging. If you run sims/log replays and deal with “it worked yesterday / what changed?” regressions, PF Gate sits in CI and turns a run into: deterministic PASS / WARN / FAIL / QUARANTINE (CI-friendly exit codes) JUnit output so results show up directly in CI UI an offline report.html “debug packet” auditable receipts explaining exactly why it flagged a run (plus policy + artifact hashes for provenance) diff-as-gate mode so CI failures include regression context vs a baseline It runs locally/in CI (no log upload). If you already have your own logs (rosbags/MCAP/custom), the idea is to adapt them into a canonical trace.jsonl (adapter guide included). This is just a fun project to me. I hope that this can be of help to anyone. Thank you in advance for checking it out, and if you have any questions feel free to DM me. If you do use it, I would love feedback on what worked and what didn’t. Thank y’all!

🔗 [GitHub](https://github.com/QPFAI/PF-Gate) • 5h ago

---

**[ROS News for the Week of February 2nd, 2026](https://www.reddit.com/r/robotics/comments/1qxs0dx/ros_news_for_the_week_of_february_2nd_2026/)**

ROS News for the Week of February 2nd, 2026            Big news, ROSCon Croatia is go! The event is scheduled for late March. Reach out to @destogl for more information. Our friends at InOrbit have an event tonight in Mountain view and our SG ROS Meetup will happen on the 10th. Towards the end of the month we have a very special joint PX4 / ROS By-The-Bay Meetup sheduled.             URDF Kitchen is a GUI-based tool that allows you to load mesh files for robot parts, mark connection points, and ...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-february-2nd-2026/52379) • 6h ago

---

**[Humanoid Robotics Market in 2026 Transformative Trends and Technological Advancements](https://www.reddit.com/r/robotics/comments/1qxe7rq/humanoid_robotics_market_in_2026_transformative/)**

A new 2026 market report highlights a massive shift toward mass production, led by giants like Tesla (aiming for 1 million Optimus units), Boston Dynamics, and Figure AI. From logistics and healthcare to customer-facing retail, general-purpose humanoids are becoming an operational reality.

🔗 [GlobeNewswire News Room](https://www.globenewswire.com/news-release/2026/02/04/3232234/0/en/Humanoid-Robotics-Market-in-2026-Transformative-Trends-and-Technological-Advancements.html) • 15h ago

---

---

## Google News: "robotics"

**[China is running the EV playbook on humanoid robots — and it’s working](https://restofworld.org/2026/china-humanoid-robots-unitree-agibot-tesla-optimus/)**

Rest of World • 1d ago

---

**[If it’s good enough for Tesla: Faraday Future pivots to humanoid robots](https://electrek.co/2026/02/06/if-its-good-enough-for-tesla-faraday-future-pivots-to-humanoid-robots/)**

After failing to deliver its promised "Tesla killer" EV, Faraday Future is hoping it's robot has what it takes to finally pull ahead of Elon.

Electrek • 13h ago

---

**[I'm a 25-year-old founder who loves robots but too many humanoids are militant and creepy-looking. Things need to change—just look at Elon Musk](https://fortune.com/2026/02/05/25-year-old-robotics-founder-says-too-many-creepy-militant-look-at-elon-musk/)**

Who’s raising our robots? Teaching social norms in the age of humanoid robots.

Fortune • 1d ago

---

**[ETM brings its transverse flux motor technology to robotics](https://www.therobotreport.com/etm-brings-its-transverse-flux-motor-technology-to-robotics/)**

ETM said its TFM technology enables OEMs to simplify mechanical designs, reduce costs, and achieve performance benchmarks.

The Robot Report • 2d ago

---

**[Robot development, from actuators to AI](https://www.therobotreport.com/robot-development-from-actuators-ai-mauerer/)**

The Robot Report Podcast's guests this week are Marco Mauerer from maxon motor and David Koelle of Charles River Analytics.

The Robot Report • 4h ago

---

**[Walmart to add automation, robotics to Louisiana distribution center](https://www.supplychaindive.com/news/walmart-automation-robotics-opelousas-louisiana-distribution-center/811025/)**

The retailer’s $330 million investment, slated to start this year, is part of a larger effort to upgrade all 42 of its regional distribution facilities.

Supply Chain Dive • 1d ago

---

**[Hail our new robot overlords! Amazon warehouse tour offers glimpse of future](https://www.theguardian.com/technology/2026/feb/06/amazon-georgia-warehouse-tour-robots)**

At its new Stone Mountain, Georgia, facility, Roomba-like robots shuffle between stacks, another adds shipping labels while another arranges packages in pallets

The Guardian • 14h ago

---

**[Making robots useful and affordable will need better motors](https://www.bbc.com/news/articles/c5y46356zzyo)**

Firms are working to make the motors that drive robots more efficient and cheaper.

BBC • 1d ago

---

**[Apple Teaching Swift and Robotics Across Its India Supply Chain](https://www.macrumors.com/2026/02/04/apple-teaching-swift-and-robotics-in-india/)**

Apple today announced a new Education Hub in Bengaluru as part of an expanded effort to provide technical training and skills development for employees across its supply chain in India. Apple said the new Apple Education Hub in Bengaluru will serve as a centralized training and coordination facility for supplier employees in India, marking the company's first education hub of its kind in the country.

MacRumors • 2d ago

---

**[Sam Altman On Elon Musk, Donald Trump, Robotics, Fatherhood And More](https://www.forbes.com/sites/richardnieva/2026/02/04/sam-altman-on-elon-musk-donald-trump-robotics-fatherhood-and-more/)**

Forbes • 2d ago

---

---

## YouTube Videos: "robotics"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 149K • 👍 3K • 💬 666 • ⏱️ 13:31 • 2d ago

---

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 22K • 👍 190 • 💬 41 • ⏱️ 1:21 • 6d ago

---

**[He Tried to Troll a Tesla Robot. The Robot Trolled Him Back 🤯🍿](https://www.youtube.com/watch?v=8sw7pOaOkik)**

Tesla's Optimus Gen 2 demonstrates its advanced low-latency tracking and tactile precision by playfully interacting with a person ...

📺 Batya Feuer

👁️ 6K • 👍 116 • 💬 10 • ⏱️ 0:25 • 2d ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 36K • 👍 150 • 💬 50 • ⏱️ 2:06 • 5d ago

---

**[ROBOT FAILS AT CES 2026 When the robot had one job... #RobotFail #funny](https://www.youtube.com/watch?v=uWeL84NvWXw)**

Not all the robots at CES were behaving this year. In this video, witness a hilarious robotics fail with an AI robot and a casino robot ...

📺 Tinker Forward

👁️ 850 • 👍 23 • ⏱️ 1:30 • 3h ago

---

**[ChatGPT in a kids robot does exactly what experts warned.](https://www.youtube.com/watch?v=LF4o4Z01Q0I)**

AI in a kids toy does what experts warned. Can we trust AI? Get Inside AI's exclusive Nord VPN deal here: ...

📺 InsideAI

👁️ 758K • 👍 32K • 💬 5K • ⏱️ 15:47 • 6d ago

---

**[IShowSpeed Started Beefing with an AI Robot on Stream 😂](https://www.youtube.com/watch?v=8ga7WPMN6GE)**

Credits: IShowSpeed Live ishowspeed started beefing with an ai robot on stream after the robot responded back with ...

📺 WClipMedia

👁️ 622K • 👍 4K • 💬 24 • ⏱️ 0:26 • 3d ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 75K • 👍 500 • 💬 36 • ⏱️ 0:06 • 3d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=lsVNGP4LfPA)**

📺 Lin of Brant robot 

👁️ 30K • 👍 93 • 💬 1 • ⏱️ 0:22 • 4d ago

---

**[This Robot Produces Speech the Human Way 😮](https://www.youtube.com/watch?v=L0M5fs_phpA)**

This Robot Produces Speech the Human Way This system generates speech using physical movement rather than digital ...

📺 MrScoopz

👁️ 5.4M • 👍 30K • 💬 1K • ⏱️ 0:05 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

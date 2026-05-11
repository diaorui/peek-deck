---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-11T05:33:17.557847+00:00'
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

**Last Updated:** May 11, 2026 at 05:33 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A custom lego robot taking a beer up some stairs without spilling](https://www.reddit.com/r/robotics/comments/1t9cmc4/a_custom_lego_robot_taking_a_beer_up_some_stairs/)**

12h ago

---

**[Bimo’s walking model now runs natively on a Raspberry Pi Pico at 5ms inference time!](https://www.reddit.com/r/robotics/comments/1t968vj/bimos_walking_model_now_runs_natively_on_a/)**

This is Bimo walking completely standalone: no data cable, no external compute, just a battery and an RP2040 (custom board) running the walking policy natively at ~5.2ms inference time. The main walking model trains on thousands of parallel environments in Isaac Lab. That policy gets distilled down to a tiny student network and compiled directly into the MCU firmware. Here's the pipeline: Train a standard 256×128×64 teacher model in Isaac Lab (~5min on an RTX 4080) Distill it into a 64×32 student network (~30s, yep, I was surprised too) Export as pure C using onnx2c Compile into the RP2040 firmware via Arduino IDE Inference runs at 5.0-5.2ms, comfortably within the 50ms control loop The full distillation pipeline, the standalone MCU inference code, and the Bimo API ported to ROS2 nodes are all coming in the next update (v1.1). ROS2 was a direct request from the last Reddit post, so that's in. Has anyone else run RL locomotion policies natively on an MCU? How small have you made the student network before significantly degrading performance? If you want to follow the development, join the Discord server, all updates go there first. Code update to v1.1 will be available on GitHub soon.

16h ago

---

**[Harvesting Robot prototype](https://www.reddit.com/r/robotics/comments/1t9op9f/harvesting_robot_prototype/)**

Been building this harvesting robot (made for glasshouses with pipe rails) for the last 2 years. Prototype almost ready

4h ago

---

**[Spatial VLM : Projecting 2D reasoning into 3D output (open source demo)](https://www.reddit.com/r/robotics/comments/1t9tkko/spatial_vlm_projecting_2d_reasoning_into_3d/)**

So I've always argued that Physical AI for robotics need actionable outputs like 3D coordinates, not bullet points or nice paragraphs. So decided to experiment by combining a VLM with Monocular Depth Estimation, essentially projecting 2D reasoning into 3D, I called it Odyseus - Spatial VLM Tech Stack: - VLM: Qwen 3.6 - Depth Estimation: Depth Anything 3 - Metric Large Worked pretty well, figured to share, check repo: https://github.com/MercuriusTech/Odyseus-Spatial-VLM

22m ago

---

**[look at this neat little feature in development for humanoid robots](https://www.reddit.com/r/robotics/comments/1t9a67c/look_at_this_neat_little_feature_in_development/)**

13h ago

---

**[Police Robots Are a Security Nightmare- YouTube](https://www.reddit.com/r/robotics/comments/1t9b3bx/police_robots_are_a_security_nightmare_youtube/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=lA8WuXDXfcI) • 13h ago

---

**[PID control](https://www.reddit.com/r/robotics/comments/1t9ohfy/pid_control/)**

These days I've been trying to do some projects with PID control, but I just haven't been able to get it right. At first, I made the hardware for a maze-solving mouse, but I couldn't program it appropriately, so I decided to perhaps start doing some related projects to later implement everything in the mouse maze solver; I've been working on an inverted pendulum I'm trying to practice with PID control, but I can't get it to work no matter how hard I try. Any advice on how to learn about this type of control?

4h ago

---

**[Gabi the robot was ordained as a monk in a special ceremony in South Korea](https://www.reddit.com/r/robotics/comments/1t9t5np/gabi_the_robot_was_ordained_as_a_monk_in_a/)**

43m ago

---

**[Custom Robotics Simulator focused on a drag-and-drop prefab workflow.](https://www.reddit.com/r/robotics/comments/1t8ycyd/custom_robotics_simulator_focused_on_a/)**

Check it out:: https://github.com/alfaiajanon/RoboticsStudio The problem: When I first got into robotics, the biggest frustration I faced was that I couldn't just test real hardware in a simulation. Most simulators aren't built around prefabs, and the ones that are usually just give you 3D visual assets with zero actual behavior attached to them. So.... I built this simulator as a proof of concept to fix that. The focus here is strictly on beginners and creating an educational sandbox. You just drag and drop parts to build the robot, and then jump straight into scripting. The features: Prefab Assembly Built-in JS Editor (arduino like) Live Telemetry Note: As i was the only dev, to speed up, I leaned heavily on AI for coding assistance (used as a copilot, no autonomous agents were used).

23h ago

---

**[[Competition] LoRR 2026: Robust multi-robot coordination under execution uncertainty](https://www.reddit.com/r/robotics/comments/1t9nvpb/competition_lorr_2026_robust_multirobot/)**

Hello r/robotics! This is an invitation to join the 2026 League of Robot Runners! https://www.leagueofrobotrunners.org Co-located with AAMAS 2026, LoRR is a research competition that tackles large-scale coordination for a fleet of robots. Our problem is inspired by modern logistics automation, where robots operate continuously, tasks arrive online, and you must keep throughput high while staying safe. Solving this problem requires full-stack robotics expertise: Task and motion planning: decide which robot performs which task and how they reach their destinations Safe execution: robots must avoid collisions during the entirety of each motion! 🛠️ Planning + execution gap: actions don’t always proceed exactly as planned (there are delays), so robust control matters. 🤖 Real-time operation: strict timing budgets (mirroring real application settings). ⏱️ Coordination at scale: manage queueing, congestion and coordination for thousands of robots (small mistakes amplify, dynamics show up at scale). 🚀 Work with an integrated development system: we provide tools and testbeds that let you focus on your interests and expertise: task scheduling, execution management and/or holistic fleet orchestration. ⚙️ Participate for fame, glory and cash prizes across three distinct tracks: Task Scheduling Track Execution Track Combined Track We provide a start kit (C++/Python), example instances, validators, and a visualiser Submissions are evaluated automatically with live leaderboard feedback Timeline: 16th April 2026: Main Round Begin 22nd May 2026: AAMAS prize deadline AAMAS 2026: AAMAS Prize Announcement 22nd July 2026: Main Round End Early August: Winner Announcement Visit our website for more details or post here if you have questions!

4h ago

---

---

## Google News: "robotics"

**[South Korea Exploring Using Hyundai Robots as Army Numbers Fall](https://www.bloomberg.com/news/articles/2026-05-11/south-korea-exploring-using-hyundai-robots-as-army-numbers-fall)**

Bloomberg.com • 1h ago

---

**[MDA Space continues work on Gateway robotic arm](https://spacenews.com/mda-space-continues-work-on-gateway-robotic-arm/)**

SpaceNews • 1d ago

---

**[Video Friday: AI Gives Robot Hands Human-Like Dexterity](https://spectrum.ieee.org/video-friday-robotic-hand-dexterity)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[A Look At Richtech Robotics (RR) Valuation After SoundHound AI Partnership And Hospitality Robot Showcases](https://finance.yahoo.com/markets/stocks/articles/look-richtech-robotics-rr-valuation-152228053.html)**

Richtech Robotics (RR) stock is back in focus after the company signed a non binding letter of intent with SoundHound AI to integrate voice AI into its service robots for upcoming hospitality focused demonstrations. See our latest analysis for Richtech Robotics. Those upcoming hospitality demos and recent high profile showcases, such as ADAM serving fans at Vegas Golden Knights games, come after a 30 day share price return of 39.58% and a 1 year total shareholder return of 30.73%, even though...

Yahoo Finance • 2d ago

---

**[Man Who Invented Roomba Moves Into Household Demon Market](https://futurism.com/robots-and-machines/roomba-inventor-moves-into-demon-market)**

Colin Angle, the inventor of the Roomba, is creating a furry AI robot companion that walks a fine line between cute and horrifically uncanny.

Futurism • 18h ago

---

**[Warrenton students gear up for another run at the world championships in underwater robotics - Oregon Public Broadcasting](https://www.opb.org/article/2026/05/09/warrenton-oregon-aquatic-robotics-team-mate-rov-competition/)**

Regional qualifying competition in Newport this weekend could send an Oregon underwater robots team to the world championships.

Oregon Public Broadcasting - OPB • 1d ago

---

**[Falling prices, broad use scenarios fuel Chinese adoption of humanoid robots](https://www.globaltimes.cn/page/202605/1360578.shtml)**

Driven by constant tech breakthroughs and growing market adoption, humanoid robots in China are undergoing a notable wave of price cuts this year.

Global Times • 2d ago

---

**[WATCH: Surprise robotics team wins international award for expanding STEM access](https://www.abc15.com/news/uplifting-arizona/watch-surprise-robotics-team-wins-international-award-for-expanding-stem-access)**

Launch Team Robotics, founded by former Paradise Honors student Stephen Robertson, was created to remove barriers and give kids across the Valley free access to hands-on STEM education.

ABC15 Arizona • 2d ago

---

**[Figure AI's robots can make a bed faster than you](https://www.businessinsider.com/figure-ai-robots-humanoids-make-a-bed-video-2026-5)**

Figure AI release a video of two humanoid robots making a bed together — a deceptively hard task that tests coordination, vision, and dexterity.

Business Insider • 1d ago

---

**[China unveils 220-pound robot ‘construction worker’ to use human tools on moon](https://interestingengineering.com/ai-robotics/china-unveils-robot-construction-worker)**

The upcoming Chang’e-8 mission may showcase China’s first AI-assisted humanoid-style robot on the lunar surface.

Interesting Engineering • 16h ago

---

---

## YouTube Videos: "robotics"

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 320K • 👍 32K • 💬 3K • ⏱️ 23:53 • 15h ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 7K • 👍 117 • 💬 51 • ⏱️ 2:19 • 2d ago

---

**[Atlas&#39; Balancing Act | Boston Dynamics](https://www.youtube.com/watch?v=UoHfGhLHRkg)**

Balancing commercial goals and robotics research can be tricky, but with Atlas we're making it work.

📺 Boston Dynamics

👁️ 369K • 👍 20K • 💬 1K • ⏱️ 0:44 • 5d ago

---

**[Mender REBUILT Getting Swarmed | Ridiculous Healing Waves | War Robots](https://www.youtube.com/watch?v=qXpzp0DWSXc)**

Mender returns to face the meta. We need to make the most powerful Mender possible. The Menders have pretty much become ...

📺 PREDATOR WR

👁️ 9K • 👍 424 • 💬 58 • ⏱️ 14:24 • 17h ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=2UUaZy4cWHw)**

📺 Robot Julie 

👁️ 27K • 👍 198 • 💬 2 • ⏱️ 0:26 • 2d ago

---

**[🤖 Control a Robot Arm with Joystick!](https://www.youtube.com/watch?v=Z3UCTCq5OJ8)**

Control a Robot Arm with One Joystick using Arduino! code link ...

📺 MW Electronics Lab

👁️ 204K • 👍 1K • 💬 34 • ⏱️ 0:05 • 4d ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 5K • 👍 136 • 💬 17 • ⏱️ 20:22 • 6d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 30K • 👍 262 • 💬 96 • ⏱️ 2:14 • 5d ago

---

**[Kai Cenat bought a $70,000 robot, and it keeps shocking them 💀😭 #kaicenat #kaicenatstream #shorts](https://www.youtube.com/watch?v=xy5p1EimPXc)**

kaicenat #kaicenatstream #fanum #robot.

📺 StreamGenius

👁️ 284K • 💬 59 • ⏱️ 0:44 • 2d ago

---

**[Self-evolving AI, robot fights, new GPT voice, new local image model, Gemma upgrade: AI NEWS](https://www.youtube.com/watch?v=quxnhOeRz7I)**

HUGE AI NEWS: HiDream-O1 Image, Bach 1.0, Zaya1, LabOS, PhysForge & more #ai #ainews #aitools #aivideo #agi Thanks to ...

📺 AI Search

👁️ 71K • 👍 3K • 💬 287 • ⏱️ 48:10 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

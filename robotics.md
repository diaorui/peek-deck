---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-14T11:15:37.753353+00:00'
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

**Last Updated:** August 14, 2026 at 11:15 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Revamp & Retry](https://www.reddit.com/r/robotics/comments/1vnlzp7/revamp_retry/)**

​ 🎉拔蘑菇验证通过，但离“实战”还差一截。 下一版直接上狭窄空间模拟——相机怼近了有盲区，所以末端执行器改方案：从底下横着“抄”菌柄，夹得稳还不伤菇。 小伙伴有没有更骚的操作？欢迎砸我脑洞，在线等！🍄🔧 ✅ Mushroom-pulling works—now time for the real squeeze. Next up: tight spaces, closer camera (blind spots, ugh), so we’re redesigning the end-effector to slide in sideways from below and grip the stipe—no more crushed caps. Any brighter ideas? Throw ’em at me! 🍄🤖

15h ago

---

**[Avancée](https://www.reddit.com/r/robotics/comments/1vninq2/avancée/)**

16h ago

---

**[Hexapod Spider Robot (Half-finished)](https://www.reddit.com/r/robotics/comments/1vn17c3/hexapod_spider_robot_halffinished/)**

(Note: Every component is made from scratch in Fusion). I originally planned to add a lightweight robot arm at the top center of the robot, after the calculations... (Inspiration comes from MakeYourPets)

1d ago

---

**[Robotic Actuator Comparison Almanac](https://www.reddit.com/r/robotics/comments/1vnjby8/robotic_actuator_comparison_almanac/)**

Spec the right actuator without clicking through 20 Chinese websites. This is V1 - what else would make this more useful? Other brands or specs you'd add? https://pendulumrobotics.com/pages/robotic-actuators

16h ago

---

**[I added remote motor, camera, and skills control to AgenticROS for controlling ROS robots remotely!](https://www.reddit.com/r/robotics/comments/1vnhqas/i_added_remote_motor_camera_and_skills_control_to/)**

17h ago

---

**[AcadosCpp: plug-and-play integration of acados NMPC controllers into C++ robotics applications](https://www.reddit.com/r/robotics/comments/1vnjscg/acadoscpp_plugandplay_integration_of_acados_nmpc/)**

Hi everyone, I’ve been developing a project called AcadosCpp. https://github.com/amaldevh/AcadosCpp acados is excellent for generating fast C code for nonlinear MPC. However, bringing that generated API into a bigger robotics codebase often means writing model-specific code to connect everything. If you change the robot model or OCP, you usually have to update solver symbols, dimensions, lifecycle management, references, parameters, and warm-start logic. AcadosCpp gives you a unified C++ and Python interface for the generated solver. The idea is to keep your workflow simple: if you change the model or control problem, just regenerate, recompile, and keep using the same controller interface. Here’s what a typical control loop looks like: while (running) { const auto& u = controller.solve(measured_state, state_refs, input_refs); robot.apply(u); } The wrapper takes care of: Applying the measurement only at stage 0 Updating the complete reference horizon Separate running and terminal references Time-varying model parameters Shifted warm starts from the previous solution Predicted state and control trajectories Solver timing and convergence diagnostics Split SQP-RTI preparation and feedback Python bindings for prototyping You’ll find a 13-state quadrotor example in the repository, available in both C++ and Python. I’d love to know what other models, middleware integrations, or real-robot examples would help make this tool more useful for your projects.

16h ago

---

**[A 4-servo quadruped that reconfigures into 5 different locomotion modes (biped, tricycle, bar-spin, 4WD, water-paddle)](https://www.reddit.com/r/robotics/comments/1vns8sf/a_4servo_quadruped_that_reconfigures_into_5/)**

Been testing how much mechanical diversity I can get out of Quaddle robot by changing the attachment instead of adding more actuators. Same 4 servos and the same OpenCat firmware the whole time — what changes is the attachment (3D-printed, mostly) and which gait is loaded for it: - Biped: printed base clips on, switches to two-legged walking - Tricycle: printed wheel mount + a bearing wheel, front legs go passive and drag - Bar-spin: printed grippers clip onto a bar, full 360° rotation gait - 4WD: wheel kit replaces all 4 legs, standard car driving - Water-paddle: printed footpads, paddling gait (works, though we've sunk it twice) This is pre-release — not in production yet, but I wanted to share this fun experiment since keeping the servo count fixed while switching locomotion modes was a fun constraint to design around. The gait codes and the 3D-printed parts will be open sourced. Happy to go into Quaddle's gait/kinematics details in the comments if anyone's curious.

🔗 [youtube.com](https://www.youtube.com/watch?v=YfREsyasRe8) • 10h ago

---

**[AUXON: A First Look](https://www.reddit.com/r/robotics/comments/1vn96n6/auxon_a_first_look/)**

It is an absolute pleasure to present after 18 months, a working version of AUXON v2! AUXON is an ultrasonic communications system which transmits data through frequencies way above the human range of hearing. Today I successfully transmitted and reconstructed a full passage of text. I initially sent in a simple repeating binary sequence, to test the BFSK(the way the system recognises frequencies and recovers bits post-transmission). Then, of course I had too, I transmitted the string "Hello World" and success again. I decided to ramp it up and transmit a longer passage - a far cry from the initial repeating sequence. Absolutely flawless at approximately 1kb/s. As you can understand, this was absolutely surreal seeing results after the better part of two years of learning the skills, design and development all amongst other work.

22h ago

---

**[[Project] ROS2 full conversion of the freenove big hexapod kit (open source)](https://www.reddit.com/r/robotics/comments/1vnovff/project_ros2_full_conversion_of_the_freenove_big/)**

13h ago

---

**[Folding a towel: hands vs code, and the hands still win](https://www.reddit.com/r/robotics/comments/1vn4r8r/folding_a_towel_hands_vs_code_and_the_hands_still/)**

This week a student came by and tried our teaching arms, both hands on two of them, teleoperating our control arms. First try, the arms folded the towel. That's exactly why we still keep teleoperation around. You don't write a line of code. You just move. The teaching arms are linked to the control arms, so your motion gets copied onto them in real time. Which means someone with zero experience can do the kind of thing that would otherwise take ages to hand-program. Watching him work, two things hit me. One: this is still the fastest way we have to pull real manipulation data. Fabric is the hardest to deal with. No fixed grasp point, and it keeps sliding off to the side. A human hand just knows how to teach it the right move. Two: it's a straight check on whether the motion actually holds up. If a person can't move the arm cleanly themselves, all the algorithm and programming in the world probably won't fix it. That's why the towel became our test. Soft. Slippery. Never the same twice. And honestly, if you want a robot to fold a towel, the fastest way I know is still a human on the teaching arms. The models haven't beaten that trick yet.

1d ago

---

---

## Google News: "robotics"

**[America Wants to Make Its Own Humanoid Robots. That Won’t Be Easy.](https://www.nytimes.com/2026/08/13/business/humanoid-robot-us-china.html)**

The New York Times • 1d ago

---

**[Workers Are Teaching AI-Powered Robots to Take Over Their Jobs](https://www.bloomberg.com/news/features/2026-08-12/thousands-of-india-workers-are-helping-ai-firms-train-robots-to-replace-them)**

Robotics companies are competing to collect videos of humans stitching shoes and welding steel to give their machines new skills.

Bloomberg • 1d ago

---

**[Path Robotics CEO: Physical AI can help U.S. manufacturing produce more](https://www.cnbc.com/video/2026/08/14/path-robotics-ceo-physical-ai-can-help-us-manufacturing-produce-more.html)**

Andrew Lonsberry, Chief Executive Officer of Path Robotics, said physical AI can address welding labor shortages by augmenting workers and helping U.S. manufacturers produce more, faster.

CNBC • 14m ago

---

**[Watch Making 'Significant' Progress on Robotics: Deepmind's Parada](https://www.bloomberg.com/news/videos/2026-08-14/humanoid-robots-will-become-useful-deepmind-s-parada-video)**

Bloomberg • 1h ago

---

**[Canadian-based robotics company opens 1st U.S. facility in Lexington, bringing 111 jobs](https://www.lex18.com/news/covering-kentucky/canadian-based-robotics-company-opens-1st-u-s-facility-in-lexington-bringing-111-jobs)**

A Canadian-based automation and robotics company has officially opened its first U.S. manufacturing operation in Lexington.

LEX 18 News • 1d ago

---

**[China built robots that can do backflips – but can they make money?](https://www.cnbc.com/2026/08/14/china-humanoid-robots-unitree-ipo-tesla-optimus.html)**

Unitree’s IPO will gauge investors’ appetite for a technology that has yet to prove its commercial viability amid intensifying geopolitical tensions.

CNBC • 7h ago

---

**[Chinese humanoid robot maker Unitree powers up for stellar Shanghai debut](https://www.reuters.com/world/asia-pacific/chinese-humanoid-robot-maker-unitree-powers-up-stellar-shanghai-debut-2026-08-14/)**

Reuters • 5h ago

---

**[The Latest Robotics IPO is 8000X Oversubscribed. These ETFs Could Take Off if Humanoid Robotics Are The Next Big Thing.](https://finance.yahoo.com/markets/stocks/articles/latest-robotics-ipo-8000x-oversubscribed-225120337.html)**

A Chinese humanoid robotics IPO just shattered demand records, and the shockwave is already hitting a handful of niche ETFs built exactly for this moment. Whether that momentum holds depends on two wildcards most investors are not watching closely enough.

Yahoo Finance • 1d ago

---

**[Naval Academy Integrates Robotics, Autonomous Systems Into Summer Training](https://www.war.gov/News/News-Stories/Article/Article/4569991/naval-academy-integrates-robotics-autonomous-systems-into-summer-training/)**

The Department of War provides the military forces needed to deter war and ensure our nation's security.

U.S. Department of War (.gov) • 1d ago

---

**[Uber surprised robotics company Serve by selling its entire stake](https://techcrunch.com/2026/08/11/uber-surprised-robotics-company-serve-by-selling-its-entire-stake/)**

The divesture comes comes as the two once-tight companies have started to diverge on the business side.

TechCrunch • 2d ago

---

---

## YouTube Videos: "robotics"

**[I spent 3 days at MIT... the robot hype is worse than you think](https://www.youtube.com/watch?v=aB5LGrHISqY)**

Omnigent is an open source meta-harness to run all your AI agents in one place. Try it free - https://bit.ly/4fXzeo8 I spent last week ...

📺 Fireship

👁️ 907K • 👍 22K • 💬 2K • ⏱️ 7:02 • 2d ago

---

**[MASSIVE robotics deal pushes physical AI into US shipbuilding](https://www.youtube.com/watch?v=fhzTrAfskQk)**

GrayMatter Robotics CEO Ariyan Kabir explains how AI-powered robots could supercharge U.S. shipbuilding, boost American ...

📺 Fox Business Clips

👁️ 39K • 👍 541 • 💬 108 • ⏱️ 7:05 • 2d ago

---

**[$1.4 Billion Robot &quot;Died&quot; on Stage](https://www.youtube.com/watch?v=7KTiXWvw7mc)**

FREE GUIDE: The Content Creator's AI Blueprint – https://FirstMovers.ai/blueprint/ A robot just raised its fist at a Qualcomm ...

📺 Julia McCoy

👁️ 60K • 👍 2K • 💬 238 • ⏱️ 9:02 • 5d ago

---

**[I Spent a Year Building a Robot Actuator](https://www.youtube.com/watch?v=qKkivaZwqTo)**

Huge thanks to PCBWay for supporting this project! Checkout their CNC and metal 3D printing services. If you use my link when ...

📺 Food For Robots (The 5439 Workshop)

👁️ 16K • 👍 881 • 💬 87 • ⏱️ 18:39 • 2d ago

---

**[So… this is how Skynet starts? 👀🤖](https://www.youtube.com/watch?v=zAXjAyJ07bM)**

Spotted a humanoid robot outside Figure AI headquarters in Silicon Valley. The future is already here… and honestly, I'm a little ...

📺 Страна Возможностей

👁️ 1K • 👍 25 • 💬 3 • ⏱️ 0:22 • 5h ago

---

**[So Nosey The Robot Has A New Enemy](https://www.youtube.com/watch?v=nF2YCyuwABE)**

📺 Tyrecordslol

👁️ 3.6M • 👍 142K • 💬 9K • ⏱️ 0:58 • 7d ago

---

**[Chelsea Finn: This is the State of the Art in Robotics](https://www.youtube.com/watch?v=cRZNwgvcWUg)**

Robots can already fold laundry, make espresso, clean kitchens, and assemble things. The harder problem is getting them to do ...

📺 Y Combinator

👁️ 21K • 👍 579 • 💬 17 • ⏱️ 58:18 • 1d ago

---

**[Chris Camillo &amp; Amit Kukreja: The Humanoid Robot Boom Is Just Getting Started](https://www.youtube.com/watch?v=FpAh425b_SY)**

Chris Camillo calls humanoid robotics the biggest market we've ever seen. Not AI, not the internet, this. He and Amit Kukreja join ...

📺 WOLF Financial

👁️ 44K • 👍 1K • 💬 236 • ⏱️ 48:23 • 5d ago

---

**[Why the US government is trying to ban this Chinese dancing robot | Explainer](https://www.youtube.com/watch?v=RzqtTunpXlE)**

The Federal Communications Commission on 28 July announced a ban on humanoid robots from China including the popular ...

📺 Guardian News

👁️ 37K • 👍 437 • 💬 112 • ⏱️ 3:48 • 2d ago

---

**[Python for Engineers &amp; Robotics – Master NumPy, Pandas, and ChatGPT Automation](https://www.youtube.com/watch?v=eDqVqVyCo6k)**

In this comprehensive course, you will learn Python programming from scratch specifically tailored for mechanical engineering ...

📺 freeCodeCamp.org

👁️ 33K • 👍 1K • 💬 42 • ⏱️ 6:49:12 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

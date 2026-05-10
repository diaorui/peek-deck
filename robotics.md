---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-10T15:55:23.914267+00:00'
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

**Last Updated:** May 10, 2026 at 15:55 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Bimo’s walking model now runs natively on a Raspberry Pi Pico at 5ms inference time!](https://www.reddit.com/r/robotics/comments/1t968vj/bimos_walking_model_now_runs_natively_on_a/)**

This is Bimo walking completely standalone: no data cable, no external compute, just a battery and an RP2040 (custom board) running the walking policy natively at ~5.2ms inference time. The main walking model trains on thousands of parallel environments in Isaac Lab. That policy gets distilled down to a tiny student network and compiled directly into the MCU firmware. Here's the pipeline: Train a standard 256×128×64 teacher model in Isaac Lab (~5min on an RTX 4080) Distill it into a 64×32 student network (~30s, yep, I was surprised too) Export as pure C using onnx2c Compile into the RP2040 firmware via Arduino IDE Inference runs at 5.0-5.2ms, comfortably within the 50ms control loop The full distillation pipeline, the standalone MCU inference code, and the Bimo API ported to ROS2 nodes are all coming in the next update (v1.1). ROS2 was a direct request from the last Reddit post, so that's in. Has anyone else run RL locomotion policies natively on an MCU? How small have you made the student network before significantly degrading performance? If you want to follow the development, join the Discord server, all updates go there first. Code update to v1.1 will be available on GitHub soon.

2h ago

---

**[Custom Robotics Simulator focused on a drag-and-drop prefab workflow.](https://www.reddit.com/r/robotics/comments/1t8ycyd/custom_robotics_simulator_focused_on_a/)**

Check it out:: https://github.com/alfaiajanon/RoboticsStudio The problem: When I first got into robotics, the biggest frustration I faced was that I couldn't just test real hardware in a simulation. Most simulators aren't built around prefabs, and the ones that are usually just give you 3D visual assets with zero actual behavior attached to them. So.... I built this simulator as a proof of concept to fix that. The focus here is strictly on beginners and creating an educational sandbox. You just drag and drop parts to build the robot, and then jump straight into scripting. The features: Prefab Assembly Built-in JS Editor (arduino like) Live Telemetry Note: As i was the only dev, to speed up, I leaned heavily on AI for coding assistance (used as a copilot, no autonomous agents were used).

10h ago

---

**[Someone here bought Stackchan on Kickstarter](https://www.reddit.com/r/robotics/comments/1t98ws0/someone_here_bought_stackchan_on_kickstarter/)**

Someone else has received them Stackchan? I received this week. It is a pretty funny robot. Not too useful and a bit slowly sometimes but for 75 dollars is a good starting point in robotics. And open source too. When I have some time I would try to make some coding with claude code. Lets see if it works.

1h ago

---

**[Glavenus 3d printed robot arm](https://www.reddit.com/r/robotics/comments/1t88tba/glavenus_3d_printed_robot_arm/)**

I’ve made a few posts of my arm while it was still in development, though that account was banned/deleted for unknown reasons. Here is my finished build, the arm design was made in freecad and uses nema17 and nema28 motors with some high precision planetary and a few harmonic drives for the joints. Firmware and software is custom and I can freely control the arm then place points to make joint, continuous joint, and linear moves then play through them like a very crude version of pendant software. I can’t take too much credit for the firmware/software as ChatGPT was a huge crutch but regardless of I’m very happy with the end results. I still want to implement a gripper and possibly figure out controlling it through a vr controller but I’m glad to have brought this project to a finished state after such a long time.

23h ago

---

**[look at this neat little feature in development for humanoid robots](https://www.reddit.com/r/robotics/comments/1t9a67c/look_at_this_neat_little_feature_in_development/)**

20m ago

---

**[Cubic Doggo Update: phew, it finally walks like it's walking](https://www.reddit.com/r/robotics/comments/1t8gf5q/cubic_doggo_update_phew_it_finally_walks_like_its/)**

Update since: https://www.reddit.com/r/robotics/comments/1sq4rip/comment/oioxsel/ Actually inspired by the walking gait in this post :D https://www.reddit.com/r/robotics/comments/1t0o42c/dax_robotics_just_unveiled_qiji_t1000_a_tonclass/ Next up will be implementing direction control (yes yes, still manual gait. AI told me to do manual ones first before using AI), and hopefully tidying up the GitHub page for those who are interested. Full ROS2 + all commercial/3D-print part: https://github.com/SphericalCowww/CubicDoggo

20h ago

---

**[Convex MPC for humanoid locomotion](https://www.reddit.com/r/robotics/comments/1t8wteh/convex_mpc_for_humanoid_locomotion/)**

11h ago

---

**[Industrial Robotics in Action at Volkswagen’s EV Factory](https://www.reddit.com/r/robotics/comments/1t8b1dp/industrial_robotics_in_action_at_volkswagens_ev/)**

22h ago

---

**[Air Gesture Control, Zero Touch ✋🤖](https://www.reddit.com/r/robotics/comments/1t86tif/air_gesture_control_zero_touch/)**

Our AI quadruped robot now understands your hand movements. 👏 Command, navigate, interact—wireless, effortless, extraordinary. Perfect for education, research, and showcasing cutting-edge robotics.

1d ago

---

**[A hobby engineer builds a fully automated wheelchair for his wife](https://www.reddit.com/r/robotics/comments/1t7tyw5/a_hobby_engineer_builds_a_fully_automated/)**

The project video is sourced from Magic Smoke Engineer. The creator is a photographer whose wife has a congenital condition and is unable to walk. He built a remote-controlled wheelchair for her, with over 10 km range and fast charging. The video shows how he designed and built it step by step.

1d ago

---

---

## Google News: "robotics"

**[Opinion | An American industrial revolution is brewing. I saw it in Pittsburgh.](https://www.washingtonpost.com/opinions/2026/05/07/us-robotics-firm-tech-innovators-modernize-manufacturing-defense/)**

America isn't ready for "Day 30." Companies like Pittsburgh's Gecko Robotics are working to change that.

The Washington Post • 2d ago

---

**[Video Friday: AI Gives Robot Hands Human-Like Dexterity](https://spectrum.ieee.org/video-friday-robotic-hand-dexterity)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 23h ago

---

**[Warrenton students gear up for another run at the world championships in underwater robotics - Oregon Public Broadcasting](https://www.opb.org/article/2026/05/09/warrenton-oregon-aquatic-robotics-team-mate-rov-competition/)**

Regional qualifying competition in Newport this weekend could send an Oregon underwater robots team to the world championships.

Oregon Public Broadcasting - OPB • 1d ago

---

**[Western Pennsylvania School for the Deaf wins national robotics championship](https://www.wtae.com/article/western-pennsylvania-school-for-deaf-robotics-championship/71257710)**

Western Pennsylvania School for the Deaf is celebrating a big win: A national title for the school's robotics team.

WTAE • 1d ago

---

**[MDA Space continues work on Gateway robotic arm](https://spacenews.com/mda-space-continues-work-on-gateway-robotic-arm/)**

SpaceNews • 16h ago

---

**[A Look At Richtech Robotics (RR) Valuation After SoundHound AI Partnership And Hospitality Robot Showcases](https://finance.yahoo.com/markets/stocks/articles/look-richtech-robotics-rr-valuation-152228053.html)**

Richtech Robotics (RR) stock is back in focus after the company signed a non binding letter of intent with SoundHound AI to integrate voice AI into its service robots for upcoming hospitality focused demonstrations. See our latest analysis for Richtech Robotics. Those upcoming hospitality demos and recent high profile showcases, such as ADAM serving fans at Vegas Golden Knights games, come after a 30 day share price return of 39.58% and a 1 year total shareholder return of 30.73%, even though...

Yahoo Finance • 2d ago

---

**[Falling prices, broad use scenarios fuel Chinese adoption of humanoid robots](https://www.globaltimes.cn/page/202605/1360578.shtml)**

Driven by constant tech breakthroughs and growing market adoption, humanoid robots in China are undergoing a notable wave of price cuts this year.

Global Times • 2d ago

---

**[Rocket Lab To Acquire Robotics Leader Motiv Space Systems](https://rocketlabcorp.com/updates/rocket-lab-to-acquire-robotics-leader-motiv-space-systems/)**

The acquisition will add proven robotics technology used in Mars rovers and also insources precision space mechanisms such as solar array drive assemblies, one of the critical components needed for satellite constellation manufacturing.

Rocket Lab • 2d ago

---

**[Nanoleaf bets its future on robots, red light therapy, and AI](https://www.theverge.com/tech/926342/nanoleaf-smart-lighting-ai-robotics-red-light-wellness)**

“The smart home is getting kind of boring.”

The Verge • 2d ago

---

**[Hacker Takes Over Robot Lawnmower, Runs Over Innocent Man](https://futurism.com/robots-and-machines/hacker-robot-lawnmower-runs-over-man)**

A reporter for The Verge was thankfully unharmed after a white hat hacker seized control of a Yarbo lawnmower robot.

Futurism • 1d ago

---

---

## YouTube Videos: "robotics"

**[Bot Shovel by CPSLO Cal Poly Gear Slingers](https://www.youtube.com/watch?v=DSJB1q0wJK0)**

Pits & Parts full robot explanation: https://youtu.be/Ed37xibjqNE @calpolygearslingers Check out our robotics game and FUN ...

📺 FUN Robotics Network

👁️ 6K • 👍 65 • 💬 4 • ⏱️ 0:14 • 18h ago

---

**[Figure Helix 02 Humanoid Robot Cleans Bedroom Like a Human](https://www.youtube.com/watch?v=xsLOYZxIUqc)**

Figure AI just revealed one of the most realistic humanoid robot demonstrations yet. The new Helix 02 robot cleaned and ...

📺 DPCcars

👁️ 5K • 👍 87 • 💬 47 • ⏱️ 2:19 • 1d ago

---

**[Atlas&#39; Balancing Act | Boston Dynamics](https://www.youtube.com/watch?v=UoHfGhLHRkg)**

Balancing commercial goals and robotics research can be tricky, but with Atlas we're making it work.

📺 Boston Dynamics

👁️ 359K • 👍 20K • 💬 1K • ⏱️ 0:44 • 5d ago

---

**[Elon Musk Reveals Tesla Optimus Gen 3 Upgrade: AI5 Thinks Alone, 1M Ships in 2027!](https://www.youtube.com/watch?v=Nvo30-29QMc)**

Tesla AI5 and Optimus Gen 3 are changing robotics forever. A self-learning robot powered by an AI chip rivaling Nvidia could ...

📺 Tech Revolution

👁️ 78K • 👍 1K • 💬 162 • ⏱️ 18:23 • 4d ago

---

**[🤖 Control a Robot Arm with Hand Gesture](https://www.youtube.com/watch?v=FXRmCmsIXwI)**

Control a Robot Arm using just hand movement! In this project, I used an Arduino UNO, MPU6050 gyroscope sensor, and servo ...

📺 MW Electronics Lab

👁️ 7K • 💬 7 • ⏱️ 0:05 • 3h ago

---

**[VEX OVERRIDE MEGA TOWER #robotics #vex #vexrobotics #robot #override #pushback](https://www.youtube.com/watch?v=JmpESyBlXps)**

📺 Hawks Robotics

👁️ 15K • 👍 84 • 💬 7 • ⏱️ 0:05 • 1d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=2UUaZy4cWHw)**

📺 Robot Julie 

👁️ 20K • 👍 172 • 💬 1 • ⏱️ 0:26 • 1d ago

---

**[Forget About Any Job Forever With This $5,000 AI Robot - It Will Do Everything For You](https://www.youtube.com/watch?v=GBlCDrN7t2s)**

A new generation of AI robots is being designed to handle everyday tasks with minimal human involvement, from communication ...

📺 Carros Show

👁️ 4K • 👍 52 • 💬 10 • ⏱️ 20:56 • 1d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 27K • 👍 250 • 💬 94 • ⏱️ 2:14 • 4d ago

---

**[This vacuum has an ARM?! #robotics #shorts #innovation](https://www.youtube.com/watch?v=XawvaJ9A4eM)**

This video showcases a sophisticated robot vacuum cleaner equipped with a functional robotic arm. Witness its precise navigation ...

📺 Just A Dad Approved

👁️ 594 • 👍 16 • 💬 3 • ⏱️ 1:10 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*

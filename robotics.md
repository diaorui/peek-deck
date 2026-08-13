---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-13T07:40:39.328435+00:00'
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

**Last Updated:** August 13, 2026 at 07:40 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Hexapod Spider Robot (Half-finished)](https://www.reddit.com/r/robotics/comments/1vn17c3/hexapod_spider_robot_halffinished/)**

(Note: Every component is made from scratch in Fusion). I originally planned to add a lightweight robot arm at the top center of the robot, after the calculations... (Inspiration comes from MakeYourPets)

2h ago

---

**[SLAM Camera Board + Obstacle Mapping](https://www.reddit.com/r/robotics/comments/1vmfavq/slam_camera_board_obstacle_mapping/)**

This is yet another update from my project. Mighty Camera runs VIO on-device realtime in a tiny package. This gives us accurate camera motion. Using that + the camera feed, the SDK estimates depth and builds a 3D map of obstacles around it. This means a robot or drone can use Mighty for things like: - Collision avoidance - Motion planning - Autonomous navigation No stereo camera or depth sensor needed. Just Mighty’s global shutter camera + IMU.

17h ago

---

**[Looking for study partners — robotics software engineering (ROS2, C++, SLAM)](https://www.reddit.com/r/robotics/comments/1vmd52w/looking_for_study_partners_robotics_software/)**

Recent CS/BCA grad here, actively job hunting for robotics SWE roles. Been building a TurtleBot + ROS2 Humble project (Docker, React dashboard, Nav2, Gazebo sim) and want to go deeper on C++, Linux, and SLAM with people who are serious about it. Thinking a small group (Discord/weekly calls) where we: Work through ROS2 concepts and share resources Review each other's projects/code Mock interview each other for robotics SWE roles Keep each other accountable If you're learning robotics software (student, self-taught, or between jobs), drop a comment or DM. Open to remote/India-based folks especially, but anyone's welcome.

18h ago

---

**[Why Real-World Movement Is So Hard for Exoskeletons](https://www.reddit.com/r/robotics/comments/1vmhsz8/why_realworld_movement_is_so_hard_for_exoskeletons/)**

Exoskeletons can handle predictable movements pretty well. Everyday movement is a lot messier. Kathryn Zealand of Skip explains why something as simple as bending down can create a control problem, and how the company is using machine learning to better understand what a person is actually trying to do. Full ep: https://www.youtube.com/watch?v=jDR8xeU-GFQ

15h ago

---

**[Has anyone deployed VLA-based robots in production?](https://www.reddit.com/r/robotics/comments/1vmeaqq/has_anyone_deployed_vlabased_robots_in_production/)**

There's of course a lot of hype around the new robot foundation models, but seems that there are not many real deployments. Has anyone tried making this things work in production? Which tasks did you try? Did you have to end up collecting a lot of data to fine tune the model?

18h ago

---

**[I built a Raspberry Pi and ESP32-based USV — first system integration and field test](https://www.reddit.com/r/robotics/comments/1vmekgh/i_built_a_raspberry_pi_and_esp32based_usv_first/)**

Hi everyone, I’ve been developing a small unmanned surface vehicle called BN-USV, and I recently completed its first system integration and field test. The hull was designed in FreeCAD and 3D-printed in PETG. The onboard system uses a Raspberry Pi 5 for navigation, sensor processing, data logging, and mission-level control, while an ESP32-S3 handles real-time thruster control and safety-related functions. The vehicle uses two independently controlled thrusters and steers through differential thrust. It collects navigation data from GPS, IMU, and magnetometer sensors. Waypoint-based autonomous navigation is planned for the next stage of development. The main goals of this first field test were to evaluate: Hull buoyancy and stability Manual RC control and steering response Communication between the Raspberry Pi and ESP32 Navigation sensor data collection Power, vibration, and other system issues under real operating conditions This was not yet a polished autonomous-navigation demonstration. It was an early system integration test conducted before implementing and validating waypoint navigation. The vehicle also behaved quite differently on the water than I had expected from indoor testing. However, the test provided useful data and revealed several areas that need improvement, particularly sensor calibration, heading estimation, control response, and the onboard electronics. I put together a video showing both the development process and the vehicle’s first field test: https://youtu.be/Lz2eOEANyZo I’m now developing a more modular second version of the platform, together with improved navigation and waypoint control. The long-term goal is to develop BN-USV into a practical modular platform for marine research, education, environmental monitoring, and autonomous-navigation experiments. Full disclosure: I’m developing BN-USV as part of BrillNova, with the long-term goal of turning it into a commercial modular hardware platform. The software and development process will remain open and publicly documented. I’d be very interested to hear feedback, especially from anyone who has worked with small USVs, autonomous boats, marine robotics, sensor fusion, or differential-thrust control. Thanks!

17h ago

---

**[Do humanoid robots need to be general-purpose to actually scale?](https://www.reddit.com/r/robotics/comments/1vmiwaj/do_humanoid_robots_need_to_be_generalpurpose_to/)**

Humanoid pilots are starting to focus on narrower tasks and simpler deployment models. Toyota Research Institute is testing a progression from vision systems to specialized mobile manipulation before moving toward more complex humanoid systems. Other companies are also focusing on specific tasks, operational KPIs and collecting real-world data through deployment.

🔗 [Automate](https://www.automate.org/robotics/industry-insights/are-simple-tasks-and-simpler-hardware-the-secret-to-scaling-humanoids) • 15h ago

---

**[ros2_control With Closed-Loop Feedback](https://www.reddit.com/r/robotics/comments/1vm9v04/ros2_control_with_closedloop_feedback/)**

If you want to see how ros2_control works WITH feedback from encoders, take a look at my latest blog post and video in the Autonomously Exploring Viam Rover series! I talk through how the motors are driven, show how encoders work and how they're read, and most importantly, how they're linked together by ros2_control using chained PID controllers with a differential drive controller. Blog post: https://mikelikesrobots.github.io/blog/rover-ros2-control Video: https://youtu.be/FyVvHbA4nBs

21h ago

---

**[The data scaling law for physical AI is real](https://www.reddit.com/r/robotics/comments/1vmrw4d/the_data_scaling_law_for_physical_ai_is_real/)**

Two results dropped this week that I think together paint a clearer picture than either one alone. Dyna-2 (Aug 10): World-action model pretrained on 1M hours of egocentric human video. Power law holds across 4 orders of magnitude (1K to 1M hours). Cross-embodiment transfer to robots never seen in pretraining. Task success from 20% to 80-90% purely from scaling data. No architecture changes. PI0.7 (Chelsea Finn's talk, today): Single generalist model trained on highly heterogeneous data matches or outperforms fine-tuned specialists. Key ablation: removing the most diverse subset of training data causes a dramatic drop in held-out task performance. Removing a random 20% barely moves the needle. The common thread: scaling works, but what you scale matters. Dyna-2 proves the law holds to 1M hours with no plateau. PI proves that within that data, diversity (different environments, objects, tasks) is what actually drives compositional generalization, not repetition of the same scenes. Both results converge on the same conclusion: physical AI foundation models need scale AND breadth. 1M hours of kitchens won't get you construction site generalization. But 1M hours across 100+ work domains apparently will.

9h ago

---

**[Collision-avoidant admittance control via marker-free localisation](https://www.reddit.com/r/robotics/comments/1vld63g/collisionavoidant_admittance_control_via/)**

We recently explored integrating marker-free robot localisation into a collision-aware admittance controller. roboreg estimates the poses of both robots. OpTaS constructs and continuously solves the admittance task subject to spherical collision constraints (visualised as red spheres in RViz). It can't really be "felt" by watching the video, but sliding along these virtual spheres creates quite the surreal sensation. roboreg: github.com/lbr-stack/roboreg OpTaS: github.com/cmower/optas

1d ago

---

---

## Google News: "robotics"

**[Uber surprised robotics company Serve by selling its entire stake](https://techcrunch.com/2026/08/11/uber-surprised-robotics-company-serve-by-selling-its-entire-stake/)**

The divesture comes comes as the two once-tight companies have started to diverge on the business side.

TechCrunch • 1d ago

---

**[Uber Exits Serve Robotics Stake as Delivery Alliance Unravels](https://www.bloomberg.com/news/articles/2026-08-11/uber-exits-serve-robotics-stake-as-delivery-alliance-unravels)**

Uber Technologies Inc. has divested from long-time partner Serve Robotics Inc. as the two companies clash over how to deploy delivery robots, the latest setback in Uber’s push to facilitate autonomous services on its platform.

Bloomberg • 1d ago

---

**[The Latest Robotics IPO is 8000X Oversubscribed. These ETFs Could Take Off if Humanoid Robotics Are The Next Big Thing.](https://finance.yahoo.com/markets/stocks/articles/latest-robotics-ipo-8000x-oversubscribed-225120337.html)**

A Chinese humanoid robotics IPO just shattered demand records, and the shockwave is already hitting a handful of niche ETFs built exactly for this moment. Whether that momentum holds depends on two wildcards most investors are not watching closely enough.

Yahoo Finance • 8h ago

---

**[Robots That Walk and Talk Are Coming to Car Factories](https://www.nytimes.com/2026/08/11/business/humanoid-robots-car-factories.html)**

The New York Times • 1d ago

---

**[San Mateo County Could Be First to Regulate Humanoid Robots for Commercial Use](https://www.kqed.org/news/12094873/san-mateo-county-could-be-first-to-regulate-humanoid-robots-for-commercial-use)**

Researchers say that humanoid robots have a long way to go before they are officially ready for work.

kqed.org • 17h ago

---

**[Are humanoid robots ready to scrub your kitchen and take out the trash? Not quite.](https://www.cbsnews.com/news/tau-robotics-humanoid-ai-cleaning-robots-san-francisco/)**

Startup companies are now starting to test their humanoid robots for home use, but experts said wider adoption will take years.

CBS News • 1d ago

---

**[AMD’s Ryzen AI X100 Takes On GPU-Centric AI](https://www.eetimes.com/amd-challenges-gpu-centric-architectures-as-it-takes-aim-at-nvidia-in-robotics/)**

AMD launches Ryzen AI X100, betting that heterogeneous SoCs with CPU, GPU, and NPU will outperform big GPUs in physical AI and robotics.

EE Times • 1d ago

---

**[Clinical translation and engineering challenges of soft robotic cardiac sleeves for heart failure](https://www.nature.com/articles/s41467-026-76596-z)**

Nature • 1d ago

---

**[How Smart Disassembly Bots Could Power a Real Circular Economy](https://spectrum.ieee.org/recycling-robot)**

This system is getting the automated circular economy rolling

IEEE Spectrum • 2d ago

---

**[Canadian-based robotics company opens 1st U.S. facility in Lexington, bringing 111 jobs](https://www.lex18.com/news/covering-kentucky/canadian-based-robotics-company-opens-1st-u-s-facility-in-lexington-bringing-111-jobs)**

A Canadian-based automation and robotics company has officially opened its first U.S. manufacturing operation in Lexington.

LEX 18 News • 14mo ago

---

---

## YouTube Videos: "robotics"

**[I spent 3 days at MIT... the robot hype is worse than you think](https://www.youtube.com/watch?v=aB5LGrHISqY)**

Omnigent is an open source meta-harness to run all your AI agents in one place. Try it free - https://bit.ly/4fXzeo8 I spent last week ...

📺 Fireship

👁️ 800K • 👍 20K • 💬 2K • ⏱️ 7:02 • 1d ago

---

**[Why the US government is trying to ban this Chinese dancing robot | Explainer](https://www.youtube.com/watch?v=RzqtTunpXlE)**

The Federal Communications Commission on 28 July announced a ban on humanoid robots from China including the popular ...

📺 Guardian News

👁️ 32K • 👍 377 • 💬 92 • ⏱️ 3:48 • 1d ago

---

**[MASSIVE robotics deal pushes physical AI into US shipbuilding](https://www.youtube.com/watch?v=fhzTrAfskQk)**

GrayMatter Robotics CEO Ariyan Kabir explains how AI-powered robots could supercharge U.S. shipbuilding, boost American ...

📺 Fox Business Clips

👁️ 35K • 👍 501 • 💬 100 • ⏱️ 7:05 • 1d ago

---

**[Robot Teachers are Canceled.](https://www.youtube.com/watch?v=eTCfPsC1yN4)**

📺 Ben Esherick

👁️ 630K • 👍 30K • 💬 775 • ⏱️ 0:35 • 6d ago

---

**[$1.4 Billion Robot &quot;Died&quot; on Stage](https://www.youtube.com/watch?v=7KTiXWvw7mc)**

FREE GUIDE: The Content Creator's AI Blueprint – https://FirstMovers.ai/blueprint/ A robot just raised its fist at a Qualcomm ...

📺 Julia McCoy

👁️ 60K • 👍 2K • 💬 236 • ⏱️ 9:02 • 4d ago

---

**[Satyress Threehalves Is the Most Terrifying Robot Yet #Robotics #AI #Tech](https://www.youtube.com/watch?v=LLuFDQV7Js0)**

The Satyress Threehalves robot looks absolutely terrifying. This seven-foot-tall centaur robot has four legs, a humanoid body, and ...

📺 Custom Adventurist

👁️ 49K • 👍 3K • 💬 212 • ⏱️ 1:02 • 6d ago

---

**[This Transformer Robot Went To The Moon](https://www.youtube.com/watch?v=uargNhK22vs)**

This tiny transformer robot was built for the moon… It's about the size of a baseball, BUT INSIDE…are cameras, two wheels, and a ...

📺 Cleo Abram

👁️ 981K • 👍 51K • 💬 662 • ⏱️ 0:32 • 1d ago

---

**[Robots serve coke? An autonomous mobile freezer powered by VLA](https://www.youtube.com/watch?v=En7jfhGMqCI)**

In a hackathon we sponsored, builders created an autonomous mobile freezer powered by our RANGER MINI 3.0 mobile robot ...

📺 AgileX Robotics

👁️ 1K • 👍 9 • ⏱️ 0:13 • 8h ago

---

**[Beni Camera Robot: It Replaced My $5,000 Camera Rig 🤯](https://www.youtube.com/watch?v=ufoDSiEjRHU)**

Beni is an all-terrain Camera Robot designed to follow you and capture smooth, hands-free footage. In this video, I take Beni ...

📺 KhanFlicks

👁️ 23K • 💬 57 • ⏱️ 8:34 • 1d ago

---

**[So Nosey The Robot Has A New Enemy](https://www.youtube.com/watch?v=nF2YCyuwABE)**

📺 Tyrecordslol

👁️ 3.5M • 👍 139K • 💬 8K • ⏱️ 0:58 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

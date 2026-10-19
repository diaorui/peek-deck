---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-19T03:34:42.149301+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** October 19, 2026 at 03:34 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I Built a Drone With Only One Motor – And a Poor Man's High Speed Camera](https://www.reddit.com/r/robotics/comments/1x8zyvp/i_built_a_drone_with_only_one_motor_and_a_poor/)**

I've been working on an under-actuated drone that can fly with only one motor for the last few months. The propeller hub is 3D printed out of PPA-CF and has a hinge, so when the motor accelerates the blades lag behind and one pitches up while the other pitches down. By pulsing the motor torque 300 times a second, timed to the rotor angle, the drone controls its pitch and roll with the same motor that produces its thrust. Along the way I also built a "poor man's high speed camera" - a camera flash synced to my camera and motor controller, so I could take images of the propeller at precise angles to analyze its behavior. The mechanical simplicity hides a lot of software. At almost 20,000 RPM, a 0.2 ms control loop is already 20 degrees of rotation late, so I wrote custom firmware for the motor controller to compute the torque pulses on board. The body also slowly spins, so the drone gets its heading from an infrared "lighthouse" beacon in the corner of the room that it sees once per revolution. The full video explaining how it all works is available on youtube: https://www.youtube.com/watch?v=Ndftcft6XhU The code and CAD are open source on github: https://github.com/jyjblrd/single-propeller-drone

17h ago

---

**[Development over 8 months yay](https://www.reddit.com/r/robotics/comments/1x90h84/development_over_8_months_yay/)**

I posted here 8 months ago and am only now posting again, haha. This is how I've improved over the past 8 months: MK5 V1: The appearance was impressive, but... Yes, I lacked torque. MK5 V2: Hmm... MK6 V1: it walks!! it walks!! it walks!! 🐕🐕 MK6 V2: Laser cut leg Hell yeah😎😎 Two-arm guy Two-leg guy : w.i.p DMs are welcome, and those who really want to see them can do so in Seoul😎 T h a n k y o u !

16h ago

---

**[Spot stepped on it.](https://www.reddit.com/r/robotics/comments/1x93wc2/spot_stepped_on_it/)**

MK6 got stepped on by Spot. It said it didn't hurt much lol. I think this was the evening of the day I developed the MK6 V2 and participated in the Maker Faire. 2026.09.19 😎👍

13h ago

---

**[3D Printed Rocker-Bogie Mars Rover | ESP32-CAM | 6-Wheel Robotic Platform](https://www.reddit.com/r/robotics/comments/1x9666z/3d_printed_rockerbogie_mars_rover_esp32cam_6wheel/)**

More info about cad and STL https://cults3d.com/en/3d-model/game/3d-printed-rocker-bogie-mars-rover-esp32-cam-6-wheel-robotic-platform

11h ago

---

**[AI lab offers free plumbing and HVAC repairs across three cities to train AI robots](https://www.reddit.com/r/robotics/comments/1x9bqtf/ai_lab_offers_free_plumbing_and_hvac_repairs/)**

HUMXN wants to pay for maintenance and repair services for homes in Minneapolis, Chicago, and Miami to gather data to train AI models and robots.

🔗 [Yahoo Tech](https://tech.yahoo.com/ai/articles/ai-lab-offers-free-plumbing-132120755.html) • 8h ago

---

**[Humanoid robot Digit 5 targets 20-hour workdays with 9-minute charging](https://www.reddit.com/r/robotics/comments/1x90sfg/humanoid_robot_digit_5_targets_20hour_workdays/)**

Agility Robotics says its upcoming Digit 5 humanoid will use Nyobolt batteries to deliver 90 minutes of operation after a nine-minute charge. The targeted 10:1 run-to-charge ratio could support more than 20 productive hours per day in warehouses and manufacturing facilities. Early-access deployment is planned for the first half of 2027, but the company has not yet disclosed the battery capacity, cycle-life rating, or independent real-world test results.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/humanoid-robot-digit-5-workdays) • 16h ago

---

**[The Landscape of Humanoids - 2,351 products, 788 companies](https://www.reddit.com/r/robotics/comments/1x9c0ss/the_landscape_of_humanoids_2351_products_788/)**

Who builds each part of a humanoid robot: 2,351 products from 788 organizations in 46 technology boxes, as of October 2026.

🔗 [Airfold](https://www.airfold.co/humanoid-technology-map/) • 8h ago

---

**[Build a robot](https://www.reddit.com/r/robotics/comments/1x9dg0e/build_a_robot/)**

Hi my name is deemco From saudi arabia Like u see the title I have proplem with my robot I’m running into some issues building my robot. As everyone knows, robots are divided into a cloud-based component and a physical one; let’s set the cloud part aside—the problem lies in the physical side. Actually, the truth is I don’t even know how to build a robot in the first place—but that’s not your problem! Anyway, I’m working on that. My specific issue right now is the connectivity—how do I get everything to come together so that, in the end, my robot functions as one perfectly orchestrated symphony? ,,, by the way my robot is so coplex! Its like the that dude hows follow the main character in sci-fi ! . Actually everything is expensive dunno why but if u have short list i would like to see it! [ i forgot to say but hes fly tipe of robots(use fly for something very imprortant) in my brain hes super intelegent and hes gonna be my companion and help me and a friendly tipe! Haha i feel exited !!] I think i gonna put motors and cameras and in the middle theres a screen and rasberri pi and a lot! But absolute dunno . How u guys past that proplem ? I enjoyed typing that !

7h ago

---

**[Come to enjoy whit us in a Drone section](https://www.reddit.com/r/robotics/comments/1x9bu87/come_to_enjoy_whit_us_in_a_drone_section/)**

Drones are the next section Online tools that run sample by sample on a flight controller's data, on a Raspberry Pi or an NVIDIA Jetson next to it. This issue splits the work into small points. Pick one, say so in a comment, and open a PR. Every point has a question it answers, a data source and a way to check it, so a first contribution fits in an afternoon. How to take a point: comment "I take N", fork, work on a branch, open a PR that mentions this issue. One point per PR. Questions in the comments are welcome. Ground rules for every point - Each number on a page comes from a script of the repository that was run before the sentence was written. - Synthetic data are labelled "synthetic" everywhere they appear. - "Tested on a Raspberry Pi / a Jetson" is written only when the command ran on that board; otherwise "written, not run on the board". - Sources are the papers named below, with page numbers. ## Data and adapters **PX4 ULog reader.** Yield one dict per sample (time, gyro, accelerometer, GPS velocity, motor outputs, battery voltage) with `pyulog`. Check: a tiny ULog written by the test round-trips. **MAVLink tlog reader.** The same fields with `pymavlink`. Source: the MAVLink survey, arXiv:1906.10641 (Koubaa et al., IEEE Access 2019). **Synthetic flight generator.** Hover plus a circle, noise, one fault at a stated sample, labelled. The single source of data for tests and smoke runs. **ALFA loader.** Load the fixed-wing fault dataset (arXiv:1907.06268, Keipour et al., IJRR 2021; data DOI 10.1184/R1/12707963) and its ground-truth fault times. Check: the 47 processed flights load and the fault time of each is read. ## Pipelines (each answers one question) **Which part broke, and how many seconds after?** Residual of commanded against measured rate, a CUSUM detector with `reset_on_alarm=True`, a robust Mahalanobis score. Metrics: detection delay and alarm episodes per hour of normal flight. Data: ALFA (point 4). Related: Garg and Fan, arXiv:2309.09108. **Is the GPS telling the truth?** Online comparison of GPS velocity with the integrated IMU. Inject an offset ramp into normal flights and say so on the page. Motivation: SemperFi arXiv:2105.01860 and Kim et al. arXiv:2407.15003. **Is a propeller damaged?** Online spectrum of the gyro or accelerometer and a distance of the band energies from the healthy baseline. Related: Zhang et al., arXiv:2302.04410. **How many minutes of flight are left, and how sure are we?** Online fit of voltage against current and time with an interval; the remaining time as a distribution. Source for the energy model: Alyassi et al., arXiv:1703.10049. **Is the next move safe?** Distance to a geofence and to obstacles from the simulated lidar of `benchmarks/lidar_sim.py`, with the protection tools already in the library. **Where is the landing pad, and is the camera moving?** `GlobalMotion`, `MotionMask` and `FrameAnomaly` on synthetic frames of a pad. Metrics: pixel error against the planted position and time per frame at 640x360. **Is the radio link about to fail?** A drift detector on packet inter-arrival time and RSSI of a synthetic MQTT stream. **Static against online.** The same fault data with a scikit-learn batch model and the online one; median of 20 seeds, time per sample, memory. The page follows `docs/finance/static_vs_online.md`. ## Boards **Raspberry Pi to Pixhawk page.** Serial wiring, the PX4 parameters and the Pi settings, with each step checked against the PX4 documentation page (https://docs.px4.io/main/en/companion\_computer/pixhawk\_rpi.html). Mark every step you ran yourself. **Jetson power modes page.** The `nvpmodel` modes of each Orin module and the time per sample of a pipeline in each mode, measured on the board you own. **`edge_bench.py`.** Time per sample (median and interquartile range), 99th percentile, resident memory and CPU temperature for each pipeline on a given board, written to a JSON file named after the host. Include your board model in the file name. Results from a board you own are the most valuable contribution here. **Dockerfiles for arm64 and Jetson, `install.sh`, a systemd unit and an MQTT bridge** publishing the score and the alarm episodes. Base image names come from the vendor documentation, with the URL. ## Also open **ArduPilot.** The same adapters against an ArduPilot log, with the differences written down. **A flight log of your own.** Run a pipeline on a log from your drone and tell us what it found, as a comment or a page. **Spotted something in the plan?** A missing pipeline, a better source paper, a wrong sentence. Open a comment and it becomes a numbered point. A new contributor can start with point 3, 13 or 18. The folder with the instructions, rules and papers is kept by the maintainer; ask here if you want a copy. ## Papers to read (one per area) - **MAVLink, the protocol every point 1-2 and 16 talks to:** A. Koubaa et al., "Micro Air Vehicle Link (MAVLink) in a Nutshell: A Survey", IEEE Access 2019, arXiv:1906.10641. - **Fault data and metrics (points 4-5):** A. Keipour, M. Mousaei, S. Scherer, "ALFA: A Dataset for UAV Fault and Anomaly Detection", IJRR 2021, arXiv:1907.06268. - **Actuator faults (point 5):** K. Garg, C. Fan, "Neural Network-based Fault Detection and Identification for Quadrotors using Dynamic Symmetry", arXiv:2309.09108. - **GPS and state-estimator attacks (point 6):** H. Sathaye et al., "SemperFi: A Spoofer Eliminating GPS Receiver for UAVs", arXiv:2105.01860; K. H. Kim et al., "Predictable by Design, Vulnerable by Nature: Security Consequences of Learnability in UAV State Estimators", arXiv:2407.15003. - **Propeller faults (point 7):** W. Zhang et al., "Simulation-to-reality UAV Fault Diagnosis with Deep Learning", arXiv:2302.04410. - **Battery and energy (point 8):** R. Alyassi et al., "Autonomous Recharging and Flight Mission Planning for Battery-operated Autonomous Drones", IEEE T-ASE 2023, arXiv:1703.10049. - **Boards (points 13-16):** PX4 documentation, "Companion Computers", https://docs.px4.io/main/en/companion\_computer/ and "Raspberry Pi to Pixhawk", https://docs.px4.io/main/en/companion\_computer/pixhawk\_rpi.html; NVIDIA Jetson Orin power modes, https://docs.nvidia.com/jetson/archives/r36.4/DeveloperGuide/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html. Know a better paper for one of these areas? Add it in a comment with the arXiv number. link : https://github.com/tatopenn-cell/Dense-Evolution-Discovery/issues/266

8h ago

---

**[Collaboration Request: Space inspired robotics/rover for a show!](https://www.reddit.com/r/robotics/comments/1x9b6e8/collaboration_request_space_inspired/)**

Hi everyone! Not sure if this is the right flair or subreddit for this inquiry but I am trying my luck! Looking for a collaboration with someone who has made a fully functioning robotics machine (example: like the mars rover or something in that general field) that they would like to showcase next year. CONTEXT: I am hosting a NYFW show in NYC next year showcasing my cyber/steampunk space inspired collection. I would like to showcase and collaborate with someone who would like to share their work on a stage. I am no where near well versed to make and create my own robotics, so I was hoping someone would be open to connecting the bridge of couture (high fashion) and science with me. It would be a demonstration on the catwalk or simply stationary in the middle while the audience could see the functions in person. The models would maneuver around the displayed robotics making sure your work is also being carefully considered and safe. i’m happy to share concepts (think dystopian, commentary on space tourism and the implications of it and what that looks like for the future, etc) and the collection or any other context privately. if this is something you or someone you know would be interested in please comment or message me! If there is a better sub to post this I would be grateful for the recs! Thank you!!

8h ago

---

---

## Google News: "robotics"

**[Amazon Has Now Deployed Over 1 Million Robots, Which Is Bad News for Its 1.5 Million Workers](https://futurism.com/future-society/amazon-robotics-automation-warehouse-labor-safety)**

Amazon's record-breaking robotics deployment is squeezing its human warehouse workers in more ways than one.

Futurism • 1d ago

---

**[Germany's New Robot Billionaire Is Betting Big On Humanoid Gyms](https://www.forbes.com/sites/ninabambysheva/2026/10/18/germanys-new-robot-billionaire-is-betting-big-on-humanoid-gyms/)**

Forbes • 17h ago

---

**[Video: Are These Workers Training Robots to Replace Them?](https://www.nytimes.com/video/technology/100000011193946/robots-training-work.html)**

The New York Times • 2d ago

---

**[Robots could boost US manufacturing as America races to keep pace with China, expert says](https://www.foxbusiness.com/technology/robots-could-boost-us-manufacturing-america-races-keep-pace-china-expert-says)**

A Path Robotics executive told FOX Business that automation will be critical to expanding U.S. manufacturing as worker shortages persist and China moves faster to adopt robotics.

Fox Business • 2d ago

---

**[Team develops embodied robotic arm 'EmArm' with human-like touch sensing](https://techxplore.com/news/2026-10-team-embodied-robotic-arm-emarm.html)**

Tech Xplore • 1d ago

---

**[Jeff Bezos Predicts Millions Could Live In Space By 2045, Robots To Do The Work](https://www.ndtv.com/feature/jeff-bezos-predicts-millions-could-live-in-space-by-2045-robots-to-do-the-work-12202504)**

Bezos said rapid advances in AI, robotics and space technology could make life beyond Earth a reality in the coming decades.

NDTV • 17h ago

---

**[Chinese robotics firms race to roll out components and data systems, helping robots perceive, understand, interact with real world](https://www.globaltimes.cn/page/202610/1372460.shtml)**

At the Humanoid Robot Data Training Center in Beijing's western Shijingshan District, dozens of robots stood in their workrooms, learning how to pick up an object steadily and quickly. This is not a simple task - the robot must

Global Times • 22h ago

---

**[Delivery Robots Accused Of Scanning Customers’ Faces, Sharing Biometric Data](https://blockclubchicago.org/2026/10/16/delivery-robots-accused-of-scanning-customers-faces-sharing-biometric-data/)**

Block Club Chicago • 2d ago

---

**[Fincantieri to invest $100 million in robotics, artificial intelligence at shipyards](https://www.masoncountypress.com/2026/10/17/fincantieri-to-invest-100-million-in-robotics-artificial-intelligence-at-shipyards/)**

MARINETTE, Wis. — Fincantieri, one of the world’s largest shipbuilders, announced plans to invest nearly $100 million in robotics, artificial intelligence and advanced automation at its shipyards around the world, including its three facilities in Wisconsin. The Italian-based company announced Oct. 15 that it was expanding its BOOST² — The Shipyard of the Future program, an initiative launched three years ago to develop and introduce new technologies into shipbuilding operations. The investment is part of the company’s 2026-2030 industrial plan. More than 450 employees at 13 shipyards worldwide have participated in the program, including employees at Fincantieri Marinette Marine and the company’s Wisconsin System of Shipyards. Fincantieri operates three Wisconsin facilities: Marinette Marine in Marinette, Bay Shipbuilding in Sturgeon Bay and ACE Marine in Green Bay. Marinette Marine specializes in military shipbuilding, including vessels for the U.S. Navy. Bay Shipbuilding constructs, repairs and converts commercial vessels, including Great Lakes freighters. ACE Marine specializes in aluminum vessels for military and commercial applications. The modernization program focuses on integrating artificial intelligence with robotics to improve production efficiency, workplace safety and construction quality. One of the technologies being developed is known as Physical AI, which allows intelligent robotic systems to interact with their […]

MasonCountyPress.com • 1d ago

---

**[A Nvidia insider-turned-VC on why robotics hasn’t hit its ChatGPT moment, yet](https://finance.yahoo.com/technology/ai/articles/nvidia-insider-turned-vc-why-163000883.html)**

Amulya Vishwanath, who spent seven years leading product marketing for NVIDIA’s robotics platforms, says robotics is currently in its “Lego era,” with the basic building blocks like actuators, robotic hands, software, and safety standards still being rebuilt. This view runs counter to those who believe that robotics, powered by a general foundation model, is about to have […]

Yahoo Finance • 2d ago

---

---

## YouTube Videos: "robotics"

**[This Is Where the Robot Takeover Actually Began](https://www.youtube.com/watch?v=SYWsUwFxApE)**

Bringing the iconic Boston Dynamics robot dog to life through 3D modeling and animation. From advanced robotics to brick-built ...

📺 LEGO Ksunder Cage | Puzzleksu 

👁️ 16K • 👍 369 • 💬 3 • ⏱️ 0:09 • 15h ago

---

**[Ichhapur Underrated Robotics Durga Puja Pandal 2026| Most Unique Durga Puja Theme in Kolkata #shorts](https://www.youtube.com/watch?v=GHXoP4bl44Q)**

Ichhapur Underrated Robotics Durga Puja Pandal 2026 | Most Unique Durga Puja Theme in Kolkata | AI & Robotics Theme ...

📺 Little Rakhi

👁️ 25K • 👍 331 • ⏱️ 0:17 • 15h ago

---

**[These AI Robots Are Getting OUT OF CONTROL… Here’s What’s Actually Real](https://www.youtube.com/watch?v=NjcCxL9zcQQ)**

AI robots are advancing faster than ever, but how much of what we see online is actually real? From humanoid robot fights to ...

📺 The AI Nexus

👁️ 11K • 👍 75 • 💬 17 • ⏱️ 1:21:36 • 6d ago

---

**[Physical Vocal Tract Acoustic Robotic Mouth](https://www.youtube.com/watch?v=4oVij1Sdw94)**

This mechanical vocal tract mechanism utilizes forced airflow through a flexible silicone mouth and movable vocal tract ...

📺 Retrolix1

👁️ 115K • 👍 985 • 💬 93 • ⏱️ 0:07 • 1d ago

---

**[Vir The Robot Boy : Robo Vir Ki Flying Mode On | Best Scenes Robot Cartoon for kids](https://www.youtube.com/watch?v=PvxlGkbmq00)**

Vir The Robot Boy : Robo Vir Ki Flying Mode On | Best Scenes Robot Cartoon for kids #VirTheRobotBoy #HindiCartoon ...

📺 Vir - The Robot Boy

👁️ 59K • 👍 333 • ⏱️ 17:00 • 1d ago

---

**[Top 10 Arduino Projects #arduinoproject #arduino #top10 #top10ardujnoprojects #iot #robot](https://www.youtube.com/watch?v=6Q0wqK_zfEk)**

Top 10 Arduino Projects #arduinoproject #arduino #top10 #top10ardujnoprojects #iot #robot.

📺 Robotos

👁️ 3.3M • 👍 63K • 💬 109 • ⏱️ 0:58 • 6d ago

---

**[Robots Will Frame 1,250 Homes for America&#39;s Biggest Homebuilder](https://www.youtube.com/watch?v=SzzaIEKv8Ec)**

Date: October 17, 2026 Sources Promise Robotics partners with D.R. Horton on physical AI for homebuilding ...

📺 Jason Lowe on AI

👁️ 106K • 👍 2K • 💬 921 • ⏱️ 2:15 • 1d ago

---

**[I Built a Robot to Replace My Rabbit’s Best Friend #3DPrinting #Robotics #Engineering](https://www.youtube.com/watch?v=vIKYRi4GDXA)**

📺 It's on my MIND

👁️ 115K • 👍 5K • 💬 151 • ⏱️ 1:53 • 1d ago

---

**[This Robot Does Interior Work 3X Faster | Origin Company OG-1 Robot](https://www.youtube.com/watch?v=uEJPV-7EgAE)**

An Indian-founded startup called Origin has emerged with $20M in funding and robots designed to automate wall-finishing work ...

📺 Nimish Prabhu

👁️ 4K • 👍 77 • 💬 11 • ⏱️ 1:13 • 13h ago

---

**[Teaching a humanoid robot to play cornhole with Gemini 4 Argon](https://www.youtube.com/watch?v=9PICEmtfpWU)**

In an internal test, Google DeepMind robotics researchers instructed Gemini 4 Argon to watch a video of a human playing ...

📺 Google DeepMind

👁️ 926K • 👍 5K • 💬 379 • ⏱️ 1:44 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

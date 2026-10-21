---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-21T01:25:44.343495+00:00'
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

**Last Updated:** October 21, 2026 at 01:25 UTC  
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

2d ago

---

**[Development over 8 months yay](https://www.reddit.com/r/robotics/comments/1x90h84/development_over_8_months_yay/)**

I posted here 8 months ago and am only now posting again, haha. This is how I've improved over the past 8 months: MK5 V1: The appearance was impressive, but... Yes, I lacked torque. MK5 V2: Hmm... MK6 V1: it walks!! it walks!! it walks!! 🐕🐕 MK6 V2: Laser cut leg Hell yeah😎😎 Two-arm guy Two-leg guy : w.i.p DMs are welcome, and those who really want to see them can do so in Seoul😎 T h a n k y o u !

2d ago

---

**[Spot stepped on it.](https://www.reddit.com/r/robotics/comments/1x93wc2/spot_stepped_on_it/)**

MK6 got stepped on by Spot. It said it didn't hurt much lol. I think this was the evening of the day I developed the MK6 V2 and participated in the Maker Faire. 2026.09.19 😎👍

2d ago

---

**[3D Printed Rocker-Bogie Mars Rover | ESP32-CAM | 6-Wheel Robotic Platform](https://www.reddit.com/r/robotics/comments/1x9666z/3d_printed_rockerbogie_mars_rover_esp32cam_6wheel/)**

More info about cad and STL https://cults3d.com/en/3d-model/game/3d-printed-rocker-bogie-mars-rover-esp32-cam-6-wheel-robotic-platform

2d ago

---

**[AI lab offers free plumbing and HVAC repairs across three cities to train AI robots](https://www.reddit.com/r/robotics/comments/1x9bqtf/ai_lab_offers_free_plumbing_and_hvac_repairs/)**

HUMXN wants to pay for maintenance and repair services for homes in Minneapolis, Chicago, and Miami to gather data to train AI models and robots.

🔗 [Yahoo Tech](https://tech.yahoo.com/ai/articles/ai-lab-offers-free-plumbing-132120755.html) • 2d ago

---

**[Humanoid robot Digit 5 targets 20-hour workdays with 9-minute charging](https://www.reddit.com/r/robotics/comments/1x90sfg/humanoid_robot_digit_5_targets_20hour_workdays/)**

Agility Robotics says its upcoming Digit 5 humanoid will use Nyobolt batteries to deliver 90 minutes of operation after a nine-minute charge. The targeted 10:1 run-to-charge ratio could support more than 20 productive hours per day in warehouses and manufacturing facilities. Early-access deployment is planned for the first half of 2027, but the company has not yet disclosed the battery capacity, cycle-life rating, or independent real-world test results.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/humanoid-robot-digit-5-workdays) • 2d ago

---

**[The Landscape of Humanoids - 2,351 products, 788 companies](https://www.reddit.com/r/robotics/comments/1x9c0ss/the_landscape_of_humanoids_2351_products_788/)**

Who builds each part of a humanoid robot: 2,351 products from 788 organizations in 46 technology boxes, as of October 2026.

🔗 [Airfold](https://www.airfold.co/humanoid-technology-map/) • 2d ago

---

**[Build a robot](https://www.reddit.com/r/robotics/comments/1x9dg0e/build_a_robot/)**

Hi my name is deemco From saudi arabia Like u see the title I have proplem with my robot I’m running into some issues building my robot. As everyone knows, robots are divided into a cloud-based component and a physical one; let’s set the cloud part aside—the problem lies in the physical side. Actually, the truth is I don’t even know how to build a robot in the first place—but that’s not your problem! Anyway, I’m working on that. My specific issue right now is the connectivity—how do I get everything to come together so that, in the end, my robot functions as one perfectly orchestrated symphony? ,,, by the way my robot is so coplex! Its like the that dude hows follow the main character in sci-fi ! . Actually everything is expensive dunno why but if u have short list i would like to see it! [ i forgot to say but hes fly tipe of robots(use fly for something very imprortant) in my brain hes super intelegent and hes gonna be my companion and help me and a friendly tipe! Haha i feel exited !!] I think i gonna put motors and cameras and in the middle theres a screen and rasberri pi and a lot! But absolute dunno . How u guys past that proplem ? I enjoyed typing that !

2d ago

---

**[Come to enjoy whit us in a Drone section](https://www.reddit.com/r/robotics/comments/1x9bu87/come_to_enjoy_whit_us_in_a_drone_section/)**

Drones are the next section Online tools that run sample by sample on a flight controller's data, on a Raspberry Pi or an NVIDIA Jetson next to it. This issue splits the work into small points. Pick one, say so in a comment, and open a PR. Every point has a question it answers, a data source and a way to check it, so a first contribution fits in an afternoon. How to take a point: comment "I take N", fork, work on a branch, open a PR that mentions this issue. One point per PR. Questions in the comments are welcome. Ground rules for every point - Each number on a page comes from a script of the repository that was run before the sentence was written. - Synthetic data are labelled "synthetic" everywhere they appear. - "Tested on a Raspberry Pi / a Jetson" is written only when the command ran on that board; otherwise "written, not run on the board". - Sources are the papers named below, with page numbers. ## Data and adapters **PX4 ULog reader.** Yield one dict per sample (time, gyro, accelerometer, GPS velocity, motor outputs, battery voltage) with `pyulog`. Check: a tiny ULog written by the test round-trips. **MAVLink tlog reader.** The same fields with `pymavlink`. Source: the MAVLink survey, arXiv:1906.10641 (Koubaa et al., IEEE Access 2019). **Synthetic flight generator.** Hover plus a circle, noise, one fault at a stated sample, labelled. The single source of data for tests and smoke runs. **ALFA loader.** Load the fixed-wing fault dataset (arXiv:1907.06268, Keipour et al., IJRR 2021; data DOI 10.1184/R1/12707963) and its ground-truth fault times. Check: the 47 processed flights load and the fault time of each is read. ## Pipelines (each answers one question) **Which part broke, and how many seconds after?** Residual of commanded against measured rate, a CUSUM detector with `reset_on_alarm=True`, a robust Mahalanobis score. Metrics: detection delay and alarm episodes per hour of normal flight. Data: ALFA (point 4). Related: Garg and Fan, arXiv:2309.09108. **Is the GPS telling the truth?** Online comparison of GPS velocity with the integrated IMU. Inject an offset ramp into normal flights and say so on the page. Motivation: SemperFi arXiv:2105.01860 and Kim et al. arXiv:2407.15003. **Is a propeller damaged?** Online spectrum of the gyro or accelerometer and a distance of the band energies from the healthy baseline. Related: Zhang et al., arXiv:2302.04410. **How many minutes of flight are left, and how sure are we?** Online fit of voltage against current and time with an interval; the remaining time as a distribution. Source for the energy model: Alyassi et al., arXiv:1703.10049. **Is the next move safe?** Distance to a geofence and to obstacles from the simulated lidar of `benchmarks/lidar_sim.py`, with the protection tools already in the library. **Where is the landing pad, and is the camera moving?** `GlobalMotion`, `MotionMask` and `FrameAnomaly` on synthetic frames of a pad. Metrics: pixel error against the planted position and time per frame at 640x360. **Is the radio link about to fail?** A drift detector on packet inter-arrival time and RSSI of a synthetic MQTT stream. **Static against online.** The same fault data with a scikit-learn batch model and the online one; median of 20 seeds, time per sample, memory. The page follows `docs/finance/static_vs_online.md`. ## Boards **Raspberry Pi to Pixhawk page.** Serial wiring, the PX4 parameters and the Pi settings, with each step checked against the PX4 documentation page (https://docs.px4.io/main/en/companion\_computer/pixhawk\_rpi.html). Mark every step you ran yourself. **Jetson power modes page.** The `nvpmodel` modes of each Orin module and the time per sample of a pipeline in each mode, measured on the board you own. **`edge_bench.py`.** Time per sample (median and interquartile range), 99th percentile, resident memory and CPU temperature for each pipeline on a given board, written to a JSON file named after the host. Include your board model in the file name. Results from a board you own are the most valuable contribution here. **Dockerfiles for arm64 and Jetson, `install.sh`, a systemd unit and an MQTT bridge** publishing the score and the alarm episodes. Base image names come from the vendor documentation, with the URL. ## Also open **ArduPilot.** The same adapters against an ArduPilot log, with the differences written down. **A flight log of your own.** Run a pipeline on a log from your drone and tell us what it found, as a comment or a page. **Spotted something in the plan?** A missing pipeline, a better source paper, a wrong sentence. Open a comment and it becomes a numbered point. A new contributor can start with point 3, 13 or 18. The folder with the instructions, rules and papers is kept by the maintainer; ask here if you want a copy. ## Papers to read (one per area) - **MAVLink, the protocol every point 1-2 and 16 talks to:** A. Koubaa et al., "Micro Air Vehicle Link (MAVLink) in a Nutshell: A Survey", IEEE Access 2019, arXiv:1906.10641. - **Fault data and metrics (points 4-5):** A. Keipour, M. Mousaei, S. Scherer, "ALFA: A Dataset for UAV Fault and Anomaly Detection", IJRR 2021, arXiv:1907.06268. - **Actuator faults (point 5):** K. Garg, C. Fan, "Neural Network-based Fault Detection and Identification for Quadrotors using Dynamic Symmetry", arXiv:2309.09108. - **GPS and state-estimator attacks (point 6):** H. Sathaye et al., "SemperFi: A Spoofer Eliminating GPS Receiver for UAVs", arXiv:2105.01860; K. H. Kim et al., "Predictable by Design, Vulnerable by Nature: Security Consequences of Learnability in UAV State Estimators", arXiv:2407.15003. - **Propeller faults (point 7):** W. Zhang et al., "Simulation-to-reality UAV Fault Diagnosis with Deep Learning", arXiv:2302.04410. - **Battery and energy (point 8):** R. Alyassi et al., "Autonomous Recharging and Flight Mission Planning for Battery-operated Autonomous Drones", IEEE T-ASE 2023, arXiv:1703.10049. - **Boards (points 13-16):** PX4 documentation, "Companion Computers", https://docs.px4.io/main/en/companion\_computer/ and "Raspberry Pi to Pixhawk", https://docs.px4.io/main/en/companion\_computer/pixhawk\_rpi.html; NVIDIA Jetson Orin power modes, https://docs.nvidia.com/jetson/archives/r36.4/DeveloperGuide/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html. Know a better paper for one of these areas? Add it in a comment with the arXiv number. link : https://github.com/tatopenn-cell/Dense-Evolution-Discovery/issues/266

2d ago

---

**[Collaboration Request: Space inspired robotics/rover for a show!](https://www.reddit.com/r/robotics/comments/1x9b6e8/collaboration_request_space_inspired/)**

Hi everyone! Not sure if this is the right flair or subreddit for this inquiry but I am trying my luck! Looking for a collaboration with someone who has made a fully functioning robotics machine (example: like the mars rover or something in that general field) that they would like to showcase next year. CONTEXT: I am hosting a NYFW show in NYC next year showcasing my cyber/steampunk space inspired collection. I would like to showcase and collaborate with someone who would like to share their work on a stage. I am no where near well versed to make and create my own robotics, so I was hoping someone would be open to connecting the bridge of couture (high fashion) and science with me. It would be a demonstration on the catwalk or simply stationary in the middle while the audience could see the functions in person. The models would maneuver around the displayed robotics making sure your work is also being carefully considered and safe. i’m happy to share concepts (think dystopian, commentary on space tourism and the implications of it and what that looks like for the future, etc) and the collection or any other context privately. if this is something you or someone you know would be interested in please comment or message me! If there is a better sub to post this I would be grateful for the recs! Thank you!!

2d ago

---

---

## Google News: "robotics"

**[Eka is worth $1.45B thanks to a physical AI model that has experts raving](https://techcrunch.com/2026/10/20/eka-is-worth-1-45-billion-thanks-to-a-physical-ai-model-that-has-experts-raving/)**

Eka Robotics may be the first robotic arm that is actually good at picking a wide range of objects up, and it is so smooth and human-like, it is wowing the industry.

TechCrunch • 12h ago

---

**[Robot Wars How China Has the Robotics Industry in Its Grip](https://oilprice.com/Energy/Energy-General/Robot-Wars-How-China-Has-the-Robotics-Industry-in-Its-Grip.html)**

Goldman Sachs now expects about 6.5 million humanoid robots a year by 2035, and every one of them runs on rare earth magnets that China makes nearly all of.

Crude Oil Prices Today | OilPrice.com • 1d ago

---

**[Seattle ag-tech startup Carbon Robotics reduces workforce, citing economic conditions](https://www.geekwire.com/2026/seattle-ag-tech-startup-carbon-robotics-reduces-workforce-citing-economic-conditions/)**

The company did not disclose the total number of layoffs, but confirmed that the cuts affected employees across multiple departments both in the U.S. and internationally.

GeekWire • 23h ago

---

**[US Army competition explores military uses for humanoid robots](https://www.defensenews.com/industry/techwatch/2026/10/16/us-army-competition-explores-military-uses-for-humanoid-robots/)**

They're still a long way off from mass-producing Terminators.

Defense News • 1d ago

---

**[The Robot I Didn’t Expect to Build](https://spectrum.ieee.org/agility-robotics-digit-5-redesign)**

Agility Robotics’ first practical robotic worker is nothing like I dreamed

IEEE Spectrum • 1d ago

---

**[In a Second Robotics Contract, Nyobolt Will Power Agility’s Latest Humanoid](https://www.theinformation.com/newsletters/the-electric/second-robotics-contract-nyobolt-will-power-agilitys-latest-humanoid)**

In the latest bullish sign for the previously troubled battery industry, Agility Robotics said it would power the latest version of its humanoid robot, Digit, with next-generation batteries manufactured by Nyobolt.

The Information • 2d ago

---

**[Daimon Robotics building the infrastructure layer for tactile intelligence](https://www.therobotreport.com/daimon-robotics-building-the-infrastructure-layer-for-tactile-intelligence/)**

Daimon Robotics is connecting tactile sensing, real-world data collection, simulation, and AI models to help robots perform more reliably.

The Robot Report • 1d ago

---

**[U.S. clients are co-developing an AI-powered station to wash and groom dogs.](https://www.stocktitan.net/news/GMEX/gmex-robotics-announces-media-meta-s-u-s-ai-powered-autonomous-zk829ekey1np.html)**

MediaMeta submitted a U.S. patent application; the grooming station remains in development, with commercialization subject to testing and client acceptance.

Stock Titan • 6d ago

---

**[Stanford researchers develop robots that could soon do all your housework](https://www.newsnationnow.com/business/tech/robotics-robots-housework-stanford-researchers/)**

NewsNation • 7h ago

---

**[Elon Musk: Only Way to Solve U.S. Debt Is AI and Robots](https://www.chosun.com/english/industry-en/2026/10/18/NMUZPXHAGVHYDFG6GRKRPUE5LI/)**

Elon Musk: Only Way to Solve U.S. Debt Is AI and Robots Musk regrets political role, stresses AI focus after failed government spending cuts

조선일보 • 2d ago

---

---

## YouTube Videos: "robotics"

**[10,000 People Just Bought a Home Robot. Nobody Saw It Coming](https://www.youtube.com/watch?v=jDyswxYxArY)**

robot #artificialintelligence #robotics #ai 10000 People Just Bought a Home Robot. Nobody Saw It Coming For More Content ...

📺 AI Unfiltered

👁️ 41K • 👍 463 • 💬 59 • ⏱️ 8:52 • 4d ago

---

**[Tesla Reveals Major New Optimus Robot Update](https://www.youtube.com/watch?v=oy8mzP_y2H4)**

Remove your personal information online with Delete Me using my link https://joindeleteme.com/TESLASPACE20 - And enter ...

📺 The Tesla Space

👁️ 93K • 👍 3K • 💬 154 • ⏱️ 13:59 • 6d ago

---

**[Robots Going Completely Wrong Caught on Camera - Part 2](https://www.youtube.com/watch?v=b6xZtNV5ggg)**

Robots going completely wrong caught on camera return in Part 2 with more shocking malfunctions, unexpected behavior, and ...

📺 MostAmazingTop10

👁️ 80K • 👍 715 • 💬 40 • ⏱️ 9:03 • 2d ago

---

**[Robots Going Completely Wrong Caught On Camera](https://www.youtube.com/watch?v=L_W9K1q9X3o)**

Original Video https://youtu.be/rMLr5CLd1jY?is=bBzpQD81EdehBnFp.

📺 Jamel_AKA_Jamal

👁️ 109K • 👍 3K • 💬 704 • ⏱️ 13:05 • 2d ago

---

**[Are These Workers Training Robots to Replace Them?](https://www.youtube.com/watch?v=H7_KofwTsXw)**

More American workers are strapping cameras to their bodies to collect data in order to help train robots. The New York Times met ...

📺 The New York Times

👁️ 152K • 👍 1K • 💬 435 • ⏱️ 4:07 • 3d ago

---

**[This robot is India&#39;s answer to Boston Dynamics](https://www.youtube.com/watch?v=HgmaxBWkk5w)**

xTerra Robotics is quickly establishing itself as one of India's most advanced robotics startups, transitioning from an academic ...

📺 RuntimeBRT

👁️ 146K • 👍 6K • 💬 190 • ⏱️ 2:55 • 1d ago

---

**[😳 China’s 13-Foot Robot Titan Is Real — And It’s Not AI‼️ 🤯  #fyp #share #china #robots #bigduke13](https://www.youtube.com/watch?v=LlUa_jJSeIk)**

📺 Big Duke13

👁️ 368K • 👍 12K • 💬 1K • ⏱️ 2:35 • 4d ago

---

**[The Weirdest Robots to Ever Fight at NHRL](https://www.youtube.com/watch?v=eVI9Ig3lq_o)**

Not your average fighting robots. From bizarre designs to completely unconventional engineering, these robots prove there's ...

📺 NHRL

👁️ 132K • 👍 1K • 💬 86 • ⏱️ 12:13 • 5d ago

---

**[China Just Unleashed AI Robot Police on Its Streets](https://www.youtube.com/watch?v=oxStFRgyLuw)**

China's new AI robots are taking on real human jobs, and things are getting seriously weird. DEEP Robotics sent its DR02 ...

📺 MACHINEKIND

👁️ 43K • 👍 597 • 💬 63 • ⏱️ 12:40 • 4d ago

---

**[Elon Musk’s $299/Month Tesla Robot Leak Is INSANE — Cooks, Cleans &amp; Ends Nursing Home Bills?](https://www.youtube.com/watch?v=oL8z3mfQzBA)**

Elon Musk's $299/Month Tesla Robot Leak Is INSANE — Cooks, Cleans & Ends Nursing Home Bills? New patent filings and ...

📺 Tesla Insider News

👁️ 326K • 👍 2K • 💬 503 • ⏱️ 21:44 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

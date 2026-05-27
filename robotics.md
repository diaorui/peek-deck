---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-27T03:55:31.192600+00:00'
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

**Last Updated:** May 27, 2026 at 03:55 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[As China’s humanoid robot boom fades, Unitree reports profit drop.](https://www.reddit.com/r/robotics/comments/1tohvif/as_chinas_humanoid_robot_boom_fades_unitree/)**

🔗 [scmp.com](https://www.scmp.com/tech/tech-trends/article/3354855/unitree-robotics-reports-plunge-first-quarter-profits-days-crucial-ipo-hearing) • 8h ago

---

**[Beni from Mondo Robotics](https://www.reddit.com/r/robotics/comments/1to4yiv/beni_from_mondo_robotics/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2058707244703773003 Website (Kickstarter campaign: Your First Camera Robot) : https://mondorobotics.com/

15h ago

---

**[For robotic hands, what more demanding tasks can I perform with an RTX 3060 12GB? To fully utilize its potential, what can I do? Run multiple sensors in parallel? Estimate hand pose? Predict grip types? Generate finger commands?](https://www.reddit.com/r/robotics/comments/1tolnot/for_robotic_hands_what_more_demanding_tasks_can_i/)**

I used a webcam to track an Xbox controller, smartphone, and mouse, and then used the YOLO library and PyTorch to have the hand perform actions such as opening or closing certain fingers. Using my RTX 3060 12GB, I believe we can take this further by: running multiple sensors in parallel, estimating hand pose, predicting grip types, generating finger commands, and performing segmentation.

5h ago

---

**[Autonomous underwater robot uses cameras and hydrophones to map coral reef biodiversity hotspots](https://www.reddit.com/r/robotics/comments/1togr6x/autonomous_underwater_robot_uses_cameras_and/)**

Researchers at Woods Hole Oceanographic Institution developed CUREE, an autonomous underwater vehicle designed to monitor coral reef ecosystems using both visual and acoustic sensing. The robot combines cameras, hydrophones, and onboard computing to identify areas of high biological activity in real time. In field tests in the U.S. Virgin Islands, it repeatedly identified a hotspot near pillar coral where fish density was around 25 times higher than the rest of the reef. The goal is to make reef monitoring more scalable than diver-based surveys alone, especially across larger or less-explored reef systems.

🔗 [Automate](https://www.automate.org/robotics/industry-insights/scientists-utilize-underwater-drones-to-monitor-life-in-coral-reefs) • 8h ago

---

**[I built a lightweight ROS 2 observer that turns wheel slip, localization jumps, and telemetry jitter into standard diagnostics](https://www.reddit.com/r/robotics/comments/1toqkim/i_built_a_lightweight_ros_2_observer_that_turns/)**

I released a small ROS 2 runtime observer called runtime_integrity v0.3-alpha. The goal is to turn command-to-physical execution consistency into a standard ROS diagnostic signal. It currently detects / surfaces: wheel slip localization jumps timing or command-stream disturbance missing or stale command/odom streams Example wheel slip diagnostic: message: "ERROR | RESYNCING: WHEEL_SLIP" diagnosticLevelName: "ERROR" status: "RESYNCING" dominantCause: "WHEEL_SLIP" totalResidual: "1.730000" cmdOdomResidual: "1.462117" Example hard localization jump diagnostic: message: "ERROR | RESYNCING: LOCALIZATION_JUMP" dominantCause: "LOCALIZATION_JUMP" totalResidual: "50.757462" localizationJumpMetric: "1.349308" cmdOdomResidual: "42.897885" One interesting detail: localization jumps are harder than wheel slip because EKF / SLAM systems often smooth pose corrections. A hard pose discontinuity can be detected as LOCALIZATION_JUMP, but a smoothed correction may appear as sustained command/odom mismatch instead. Most robot diagnostics answer: Is the node alive? Is the topic publishing? Did a timeout happen? But on mobile robots, I often care about a different question: The stack commanded velocity X. Did the robot physically execute motion consistent with X? runtime_integrity passively observes: /cmd_vel + /odom and publishes to: /diagnostics runtime_integrity/execution_integrity No controller modification. No Nav2 BT modification. No base-driver modification. No command interception. I would love feedback from people working on AMRs, Nav2, SLAM, sensor fusion, and field robotics. Repo: https://github.com/ZC502/runtime_integrity navigation2 Discussion： https://github.com/orgs/ros-navigation/discussions/6156#discussioncomment-17064880 Open Source Robotics Projects： https://discourse.openrobotics.org/t/release-runtime-integrity-v0-3-alpha-turning-command-to-physical-execution-consistency-into-standard-ros-diagnostics/55095?u=zc_liu

2h ago

---

**[Watney Robotics.](https://www.reddit.com/r/robotics/comments/1topt95/watney_robotics/)**

Anyone have any information on this company, good or bad? Located in SF. I’ve been offered a position there and would like any firsthand information that you may have. Thanks.

3h ago

---

**[Robot servos 3d printed](https://www.reddit.com/r/robotics/comments/1tnwesd/robot_servos_3d_printed/)**

23h ago

---

**[We can have up to four 4-lane MIPI cameras fully synchronized with all AI compute offloaded from Jetson, but not sure it's worth the cost](https://www.reddit.com/r/robotics/comments/1to6rmy/we_can_have_up_to_four_4lane_mipi_cameras_fully/)**

Is there a robotics or autonomous systems use case where this is actually worth it? Thinking high-speed inspection, multi-camera SLAM, perception pipelines. Or is it over-engineered for most applications?

14h ago

---

**[Building a Tiny CAN-Enabled Zone Controller for Mobile Robotics & Automation.](https://www.reddit.com/r/robotics/comments/1tnrdqs/building_a_tiny_canenabled_zone_controller_for/)**

In 2024 I designed a device to use as a localized body control module for a project car. It has a CAN transceiver, a microcontroller, and 2 high-side switches. The goal was to take "dumb" peripherals (lights, solenoids, etc.) and make them controllable via CAN events for automotive, robotics, or industrial projects. I found the device to be pretty useful since (have several of them in my car and use them to control test jigs, robot arms, and other projects in my garage). TLDR they are useful to quickly add CAN to projects. I’m thinking about completely redesigning this from the ground up as an open-source tool for a larger audience (leaning toward launching it on Crowd Supply). I’d really appreciate your feedback on what specs I should focus on: Power: Right now it supports up to 24V. Do mobile robotics or AGV applications realistically need 48V capability nowadays, or is 24V plenty? Also, what's a typical continuous current per channel you'd expect out of something this size? Microcontroller: Currently uses an old ATmega328p. I want to upgrade this to an STM32 or RP2040 (with integrated CAN). Any preferences or code ecosystems you'd rather see native support for? Connectors/Form Factor: Because of the car environment, I used spring terminals for critical connections, plus reverse polarity protection on power and ESD on the CAN lines. Any connector suggestions? Software Stack: Right now it's just programmed via the Arduino IDE. My plan for the new version is to build a simple web-based configuration GUI (similar to an IFTTT style, where a specific CAN ID/message triggers a specific output action). Would this approach be useful, or would you still prefer just flashing your own custom C code? I’ve attached some photos of the 2024 version. Let me know what you think, or if I’m missing anything useful. Thanks!

1d ago

---

**[I’m Building Small Robot Arm](https://www.reddit.com/r/robotics/comments/1tobjiu/im_building_small_robot_arm/)**

I’m building small robot arm as leader for bimanual ROS2 robot: https://youtube.com/shorts/\_GdOdmXE9-8?is=UEOfTip8ZGyxvGn6 Or can be for small tabletop robo dog or cat 🐈

🔗 [youtu.be](https://youtu.be/aeDEz6oKb74) • 11h ago

---

---

## Google News: "robotics"

**[Delivery robots are spreading across LA. Residents ‘both pity and hate them’](https://www.theguardian.com/us-news/2026/may/25/los-angeles-delivery-robots)**

A region known for its lack of walkability now has more obstacles for pedestrians to contend with

The Guardian • 1d ago

---

**[3D-printable humanoid legs let robotics experiments run wild](https://arstechnica.com/ai/2026/05/3d-printable-humanoid-legs-let-robotics-experiments-run-wild/)**

Hugging Face debuts $2,500 bipedal robot project for builders and researchers.

Ars Technica • 10h ago

---

**[Humanoid robots work nonstop in package test](https://www.foxnews.com/tech/humanoid-robots-work-nonstop-package-test)**

Figure AI claims its three humanoid robots completed over 24 hours of continuous autonomous package sorting without any human control in a warehouse test.

Fox News • 2d ago

---

**[As China’s humanoid-robot hype cools, Unitree sees profit plunge](https://www.scmp.com/tech/tech-trends/article/3354855/unitree-robotics-reports-plunge-first-quarter-profits-days-crucial-ipo-hearing)**

South China Morning Post • 22h ago

---

**[Robotics, Science Underway as Cosmonauts Prep for Wednesday Spacewalk](https://www.nasa.gov/blogs/spacestation/2026/05/26/robotics-science-underway-as-cosmonauts-prep-for-wednesday-spacewalk/)**

Robotics controllers wrapped up a weekend of swapping scientific hardware packed inside the SpaceX Dragon cargo spacecraft’s trunk for installation on the International Space Station. Meanwhile, the Expedition 74 crew is continuing its biotechnology and botany research while getting ready for a spacewalk scheduled for Wednesday, May 27.

NASA (.gov) • 9h ago

---

**[Jury finds Palo Alto robotics teacher was harassed – but not by the district](https://www.paloaltoonline.com/palo-alto-schools/2026/05/26/jury-finds-palo-alto-robotics-teacher-was-harassed-but-not-by-the-district/)**

Palo Alto Online • 7h ago

---

**[Amazon robotic facilities could quadruple tech giant’s Middletown footprint](https://spotlightdelaware.org/2026/05/26/amazon-robotic-facilities-could-quadruple-the-tech-giants-footprint-in-middletown/)**

Spotlight Delaware • 17h ago

---

**[Popular robotics company shuts down and liquidates all assets](https://www.thestreet.com/technology/popular-robotics-company-shuts-down-and-liquidates-all-assets)**

thestreet.com • 13h ago

---

**[Moorhead High School robotics team helps empower first grade student with new device](https://www.kare11.com/article/news/local/kare11-extras/moorhead-high-school-robotics-team-helps-empower-first-grade-student/89-df02a72c-a129-460f-9711-fadfc5d671d2)**

A young girl with disabilities at Ellen Hopkins Elementary gains new independence and confidence thanks to a device engineered by the Moorhead High School robotics.

kare11.com • 1h ago

---

**[Blair Robotics Team Delivers Best-Ever Finish at World Championship](https://mocoshow.com/2026/05/25/blair-robotics-team-delivers-best-ever-finish-at-world-championship/)**

Montgomery Blair High School’s robotics team delivered its best-ever performance at the FIRST Robotics Competition World Championship, capping off a dominant season for the Silver Spring program. The Blair Robot […]

The MoCo Show - • 1d ago

---

---

## YouTube Videos: "robotics"

**[4 Robotics Stocks (ALREADY Making Money)](https://www.youtube.com/watch?v=19SrFEBkK8s)**

Physical AI isn't coming. It's already performing surgeries, sorting packages at warehouse speeds, running factory floors, and ...

📺 MarketBeat

👁️ 4K • 👍 165 • 💬 1 • ⏱️ 3:00 • 3h ago

---

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 9K • 👍 193 • 💬 45 • ⏱️ 18:21 • 3d ago

---

**[Shaq surprises Kenny and Chuck with ROBOTS 🤖😂 | Inside the NBA](https://www.youtube.com/watch?v=nIPenYETLtI)**

Subscribe to ESPN Unlimited: https://plus.espn.com/ #ESPN.

📺 ESPN

👁️ 175K • 👍 4K • 💬 378 • ⏱️ 4:57 • 23h ago

---

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 78K • 👍 920 • 💬 347 • ⏱️ 5:15 • 4d ago

---

**[Unique PTO and Middle Goal Mech | 8995H Habanero | V5RC Push Back Robot Rundown](https://www.youtube.com/watch?v=CiJpfdxfPl0)**

Unique PTO and Middle Goal Mech | 8995H Habanero | V5RC Push Back Robot Rundown This video is presented in partnership ...

📺 FUN Robotics Network

👁️ 920 • 👍 14 • 💬 4 • ⏱️ 1:17 • 4h ago

---

**[Shoggoth 👾 Robot Spotlight — War Robots](https://www.youtube.com/watch?v=Csn_o89Y3Fg)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 69K • 👍 2K • 💬 178 • ⏱️ 1:55 • 16h ago

---

**[This Robotic Finger Changed People&#39;s Brains Forever](https://www.youtube.com/watch?v=XwN-LBBHDAc)**

Scientists gave people a robotic sixth finger. After 5 days, their brains permanently rewired to accept a machine as a real body part ...

📺 AzlanX

👁️ 534K • 💬 56 • ⏱️ 0:31 • 1d ago

---

**[8 Robotic Transformation Machines Tested in 63 Seconds ⚙️ #shorts](https://www.youtube.com/watch?v=YfPxolAz3V8)**

Prototype concept demo: eight robot transformation machines tested hair, hairline, braids, and tattoo tech back-to-back.

📺 Prototype Leaked

👁️ 528K • 👍 7K • 💬 228 • ⏱️ 1:04 • 6d ago

---

**[When Bots enter your server (RoBoTs x TF2)  #3danimation](https://www.youtube.com/watch?v=iZoTzpdO0HU)**

I always thought... this was brilliant adaptation for her evil robots... massive bot army. :)) Also, this is a smaller portion of what was ...

📺 Bunny Hop Development

👁️ 491K • 👍 12K • 💬 74 • ⏱️ 0:19 • 17h ago

---

**[Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!](https://www.youtube.com/watch?v=faBkVCEEEHQ)**

Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry! Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!

📺 TESLA CAR WORLD

👁️ 31K • 👍 591 • 💬 56 • ⏱️ 15:32 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

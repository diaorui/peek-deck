---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-27T08:05:32.330270+00:00'
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

**Last Updated:** May 27, 2026 at 08:05 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Spider robot, two legs](https://www.reddit.com/r/robotics/comments/1tov0vf/spider_robot_two_legs/)**

3h ago

---

**[As China’s humanoid robot boom fades, Unitree reports profit drop.](https://www.reddit.com/r/robotics/comments/1tohvif/as_chinas_humanoid_robot_boom_fades_unitree/)**

🔗 [scmp.com](https://www.scmp.com/tech/tech-trends/article/3354855/unitree-robotics-reports-plunge-first-quarter-profits-days-crucial-ipo-hearing) • 12h ago

---

**[Beni from Mondo Robotics](https://www.reddit.com/r/robotics/comments/1to4yiv/beni_from_mondo_robotics/)**

From Eren Chen on 𝕏: https://x.com/ErenChenAI/status/2058707244703773003 Website (Kickstarter campaign: Your First Camera Robot) : https://mondorobotics.com/

19h ago

---

**[I built a lightweight mechanical arm digital twin demo with ESP32 and servos](https://www.reddit.com/r/robotics/comments/1tow5nf/i_built_a_lightweight_mechanical_arm_digital_twin/)**

Hi, I recently joined a new company and started experimenting with lightweight bidirectional communication between virtual and physical systems. To keep things simple, I built a small mechanical arm setup using three SG90 servos and an ESP32. The virtual control side is already working and I turned it into a small demo project. Right now the system has two modes: continuous data streaming servo synchronization control The main goal is to explore lightweight digital twin workflows, real-time interaction, and physical-virtual synchronization. https://reddit.com/link/1tow5nf/video/tijqxpaham3h1/player

2h ago

---

**[I finally upgraded my 1-arm keyboard automation project to a dual-arm system powered by a Raspberry Pi Pico.](https://www.reddit.com/r/robotics/comments/1toywlj/i_finally_upgraded_my_1arm_keyboard_automation/)**

3m ago

---

**[For robotic hands, what more demanding tasks can I perform with an RTX 3060 12GB? To fully utilize its potential, what can I do? Run multiple sensors in parallel? Estimate hand pose? Predict grip types? Generate finger commands?](https://www.reddit.com/r/robotics/comments/1tolnot/for_robotic_hands_what_more_demanding_tasks_can_i/)**

I used a webcam to track an Xbox controller, smartphone, and mouse, and then used the YOLO library and PyTorch to have the hand perform actions such as opening or closing certain fingers. Using my RTX 3060 12GB, I believe we can take this further by: running multiple sensors in parallel, estimating hand pose, predicting grip types, generating finger commands, and performing segmentation.

10h ago

---

**[Autonomous underwater robot uses cameras and hydrophones to map coral reef biodiversity hotspots](https://www.reddit.com/r/robotics/comments/1togr6x/autonomous_underwater_robot_uses_cameras_and/)**

Researchers at Woods Hole Oceanographic Institution developed CUREE, an autonomous underwater vehicle designed to monitor coral reef ecosystems using both visual and acoustic sensing. The robot combines cameras, hydrophones, and onboard computing to identify areas of high biological activity in real time. In field tests in the U.S. Virgin Islands, it repeatedly identified a hotspot near pillar coral where fish density was around 25 times higher than the rest of the reef. The goal is to make reef monitoring more scalable than diver-based surveys alone, especially across larger or less-explored reef systems.

🔗 [Automate](https://www.automate.org/robotics/industry-insights/scientists-utilize-underwater-drones-to-monitor-life-in-coral-reefs) • 13h ago

---

**[I built a lightweight ROS 2 observer that turns wheel slip, localization jumps, and telemetry jitter into standard diagnostics](https://www.reddit.com/r/robotics/comments/1toqkim/i_built_a_lightweight_ros_2_observer_that_turns/)**

I released a small ROS 2 runtime observer called runtime_integrity v0.3-alpha. The goal is to turn command-to-physical execution consistency into a standard ROS diagnostic signal. It currently detects / surfaces: wheel slip localization jumps timing or command-stream disturbance missing or stale command/odom streams Example wheel slip diagnostic: message: "ERROR | RESYNCING: WHEEL_SLIP" diagnosticLevelName: "ERROR" status: "RESYNCING" dominantCause: "WHEEL_SLIP" totalResidual: "1.730000" cmdOdomResidual: "1.462117" Example hard localization jump diagnostic: message: "ERROR | RESYNCING: LOCALIZATION_JUMP" dominantCause: "LOCALIZATION_JUMP" totalResidual: "50.757462" localizationJumpMetric: "1.349308" cmdOdomResidual: "42.897885" One interesting detail: localization jumps are harder than wheel slip because EKF / SLAM systems often smooth pose corrections. A hard pose discontinuity can be detected as LOCALIZATION_JUMP, but a smoothed correction may appear as sustained command/odom mismatch instead. Most robot diagnostics answer: Is the node alive? Is the topic publishing? Did a timeout happen? But on mobile robots, I often care about a different question: The stack commanded velocity X. Did the robot physically execute motion consistent with X? runtime_integrity passively observes: /cmd_vel + /odom and publishes to: /diagnostics runtime_integrity/execution_integrity No controller modification. No Nav2 BT modification. No base-driver modification. No command interception. I would love feedback from people working on AMRs, Nav2, SLAM, sensor fusion, and field robotics. Repo: https://github.com/ZC502/runtime_integrity navigation2 Discussion： https://github.com/orgs/ros-navigation/discussions/6156#discussioncomment-17064880 Open Source Robotics Projects： https://discourse.openrobotics.org/t/release-runtime-integrity-v0-3-alpha-turning-command-to-physical-execution-consistency-into-standard-ros-diagnostics/55095?u=zc_liu

6h ago

---

**[Robot servos 3d printed](https://www.reddit.com/r/robotics/comments/1tnwesd/robot_servos_3d_printed/)**

1d ago

---

**[Building a Tiny CAN-Enabled Zone Controller for Mobile Robotics & Automation.](https://www.reddit.com/r/robotics/comments/1tnrdqs/building_a_tiny_canenabled_zone_controller_for/)**

In 2024 I designed a device to use as a localized body control module for a project car. It has a CAN transceiver, a microcontroller, and 2 high-side switches. The goal was to take "dumb" peripherals (lights, solenoids, etc.) and make them controllable via CAN events for automotive, robotics, or industrial projects. I found the device to be pretty useful since (have several of them in my car and use them to control test jigs, robot arms, and other projects in my garage). TLDR they are useful to quickly add CAN to projects. I’m thinking about completely redesigning this from the ground up as an open-source tool for a larger audience (leaning toward launching it on Crowd Supply). I’d really appreciate your feedback on what specs I should focus on: Power: Right now it supports up to 24V. Do mobile robotics or AGV applications realistically need 48V capability nowadays, or is 24V plenty? Also, what's a typical continuous current per channel you'd expect out of something this size? Microcontroller: Currently uses an old ATmega328p. I want to upgrade this to an STM32 or RP2040 (with integrated CAN). Any preferences or code ecosystems you'd rather see native support for? Connectors/Form Factor: Because of the car environment, I used spring terminals for critical connections, plus reverse polarity protection on power and ESD on the CAN lines. Any connector suggestions? Software Stack: Right now it's just programmed via the Arduino IDE. My plan for the new version is to build a simple web-based configuration GUI (similar to an IFTTT style, where a specific CAN ID/message triggers a specific output action). Would this approach be useful, or would you still prefer just flashing your own custom C code? I’ve attached some photos of the 2024 version. Let me know what you think, or if I’m missing anything useful. Thanks!

1d ago

---

---

## Google News: "robotics"

**[Delivery robots are spreading across LA. Residents ‘both pity and hate them’](https://www.theguardian.com/us-news/2026/may/25/los-angeles-delivery-robots)**

A region known for its lack of walkability now has more obstacles for pedestrians to contend with

The Guardian • 1d ago

---

**[3D-printable humanoid legs let robotics experiments run wild](https://arstechnica.com/ai/2026/05/3d-printable-humanoid-legs-let-robotics-experiments-run-wild/)**

Hugging Face debuts $2,500 bipedal robot project for builders and researchers.

Ars Technica • 14h ago

---

**[Humanoid robots work nonstop in package test](https://www.foxnews.com/tech/humanoid-robots-work-nonstop-package-test)**

Figure AI claims its three humanoid robots completed over 24 hours of continuous autonomous package sorting without any human control in a warehouse test.

Fox News • 2d ago

---

**[Need help at home? Israel’s first consumer humanoid robot will cost NIS 150,000](https://www.ynetnews.com/tech-and-digital/article/sygmb3glgx)**

Electra Consumer Products’ Mahsanei Hashmal chain will sell WANDA, a semi-humanoid robot designed to perform household tasks, alongside a robotic emotional-support puppy and an AI-powered exoskeleton for walking and climbing stairs

ynetnews • 3h ago

---

**[Jury finds Palo Alto robotics teacher was harassed – but not by the district](https://www.paloaltoonline.com/palo-alto-schools/2026/05/26/jury-finds-palo-alto-robotics-teacher-was-harassed-but-not-by-the-district/)**

Palo Alto Online • 11h ago

---

**[Robotics, Science Underway as Cosmonauts Prep for Wednesday Spacewalk](https://www.nasa.gov/blogs/spacestation/2026/05/26/robotics-science-underway-as-cosmonauts-prep-for-wednesday-spacewalk/)**

Robotics controllers wrapped up a weekend of swapping scientific hardware packed inside the SpaceX Dragon cargo spacecraft’s trunk for installation on the International Space Station. Meanwhile, the Expedition 74 crew is continuing its biotechnology and botany research while getting ready for a spacewalk scheduled for Wednesday, May 27.

NASA (.gov) • 13h ago

---

**[Oops! Domino's-Partnered Robotics Startup That Was Supposed to Put Human Pizza Chefs Out of a Job Just Shut Down](https://futurism.com/robots-and-machines/dominos-robotics-startup-pizza-shuts-down)**

A startup that developed a robot capable of putting human restaurant workers out of a job and partnered with Domino's, has shut down.

Futurism • 14h ago

---

**[Amazon celebrates opening of Virginia Beach robotics facility](https://www.pilotonline.com/2026/05/24/amazon-robotics-facility-virginia-beach/)**

It’s Amazon’s third robotics fulfillment center in Virginia.

The Virginian-Pilot • 2d ago

---

**[Amazon robotic facilities could quadruple tech giant’s Middletown footprint](https://spotlightdelaware.org/2026/05/26/amazon-robotic-facilities-could-quadruple-the-tech-giants-footprint-in-middletown/)**

Spotlight Delaware • 22h ago

---

**[Rocket Lab Adds Mars-Proven Robotics Capabilities with Completion of Motiv Space Systems Acquisition](https://www.globenewswire.com/news-release/2026/05/26/3301487/0/en/rocket-lab-adds-mars-proven-robotics-capabilities-with-completion-of-motiv-space-systems-acquisition.html)**

Rocket Lab has acquired Motiv Space Systems, adding Mars heritage for complex planetary missions, plus precision mechanisms for space infrastructure....

GlobeNewswire • 11h ago

---

---

## YouTube Videos: "robotics"

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 9K • 👍 193 • 💬 46 • ⏱️ 18:21 • 3d ago

---

**[Nexi AiBot V2.0 by HD Robotics is Ready just need a new Design . read Description](https://www.youtube.com/watch?v=GTDt0VFqXFc)**

Nexi is almost complete After a long time of building, programming, testing, and improving, my AI robot project is finally ...

📺 HD Robotics

👁️ 650 • 👍 1 • ⏱️ 0:38 • 14h ago

---

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 79K • 👍 933 • 💬 349 • ⏱️ 5:15 • 4d ago

---

**[Shaq surprises Kenny and Chuck with ROBOTS 🤖😂 | Inside the NBA](https://www.youtube.com/watch?v=nIPenYETLtI)**

Subscribe to ESPN Unlimited: https://plus.espn.com/ #ESPN.

📺 ESPN

👁️ 192K • 👍 4K • 💬 398 • ⏱️ 4:57 • 1d ago

---

**[War Robots: HUGE REBALANCE 12.2 ruins EVERYTHING (again)...](https://www.youtube.com/watch?v=7Gyr40hifwk)**

War Robots News Vlog REBALANCE 12.2 ruins everything again - WR My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 12K • 👍 863 • 💬 349 • ⏱️ 37:56 • 19h ago

---

**[This Robotic Finger Changed People&#39;s Brains Forever](https://www.youtube.com/watch?v=XwN-LBBHDAc)**

Scientists gave people a robotic sixth finger. After 5 days, their brains permanently rewired to accept a machine as a real body part ...

📺 AzlanX

👁️ 543K • 💬 56 • ⏱️ 0:31 • 1d ago

---

**[NEW Shoggoth BREAKS The Live Server… Massive Titan Slaying Firepower +200% Damage | War Robots](https://www.youtube.com/watch?v=KkMiHouuRI0)**

New Shoggoth robot is here with the new update and event. This robot does have a unique ability but i dont think anyone ...

📺 PREDATOR WR

👁️ 12K • 👍 496 • 💬 94 • ⏱️ 14:24 • 15h ago

---

**[SPIDER-MAN ROBOT! This Logistics Bot Climbs 12-Meter Shelves Directly 🤖](https://www.youtube.com/watch?v=sz6hEdNSoTc)**

Inside a high-density, automated smart fulfillment fulfillment center, a groundbreaking category of logistics robotics showcases its ...

📺 Peace Working Shorts

👁️ 671K • 👍 2K • 💬 15 • ⏱️ 0:06 • 1d ago

---

**[Shoggoth 👾 Robot Spotlight — War Robots](https://www.youtube.com/watch?v=Csn_o89Y3Fg)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 77K • 👍 3K • 💬 194 • ⏱️ 1:55 • 20h ago

---

**[JUST LIKE A HUMAN! Watch This Humanoid Robot Stand Up From Its Box 🤖](https://www.youtube.com/watch?v=iBgxKU3bi7w)**

Inside a futuristic, brightly lit robotics research facility, a cutting-edge humanoid robot executes a highly coordinated autonomous ...

📺 Peace Working Shorts

👁️ 26K • 👍 135 • 💬 4 • ⏱️ 0:06 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

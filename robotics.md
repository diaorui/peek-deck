---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-28T16:19:54.955658+00:00'
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

**Last Updated:** May 28, 2026 at 16:19 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Atlas takes on the Rabona](https://www.reddit.com/r/robotics/comments/1tpym4u/atlas_takes_on_the_rabona/)**

From Hyundai Worldwide on 𝕏: https://x.com/Hyundai_Global/status/2059620640815034466

6h ago

---

**[Built a 6DOF robotic arm from scratch in India — raw movement test, no editing](https://www.reddit.com/r/robotics/comments/1tpzdmz/built_a_6dof_robotic_arm_from_scratch_in_india/)**

Been building this for 6 months. Original mechanical design, no open source blueprints. Current specs: — DS5160 60kg digital servo at core — GT2 belt drive transmission — Bearing mounted output shafts — 3D printed housing — Ender 3 — Core, shoulder, bicep assembled Moving like butter. Full demo coming soon. Happy to answer any questions.

6h ago

---

**[Standalone, high-performance 2D & 3D visualization in C++ / Python / MATLAB](https://www.reddit.com/r/robotics/comments/1tq0lw6/standalone_highperformance_2d_3d_visualization_in/)**

Hi! We've often run into performance and deployment issues with existing visualization tools, so we created HEBI Charts, a custom library for 2D and 3D robotics visualization that is in-process, standalone, cross-platform, and has idiomatic 100% type-hinted bindings for Python, MATLAB, and C++. Decoupled Rendering In order to play well with Python's GIL and MATLAB's single-threaded nature, data ingestion is completely isolated from the UI thread. Telemetry is pushed into an internally double-buffered state that gets swapped at the start of every frame. This means that a Python or MATLAB script can update data from a busy-loop running at > 10 kHz, and the internal UI thread continuously renders the latest state at 60fps. Performance The rendering is fully hardware accelerated and automatically handles multi-instancing of 3D models. The linked video shows a few demos: Updating a complex UI at 50 kHz 100 subplots 1000 random lines 1 line with 1 million points updating at 5 MHz 1000 simultaneous robot displays w/ kinematics Cross-Platform It exposes a stable C ABI with zero-configuration installation (headers automatically fetch the binaries into a local cache). It runs natively with hardware GPU acceleration on Windows (amd64), Linux (amd64), and macOS (x86_64/arm64). Examples Standalone examples and test scripts are fully accessible in the example repository: https://github.com/HebiRobotics/hebi-charts-examples Let me know in case you have questions or suggestions. I'll also be at ICRA next week in case anyone wants to have a deeper discussion.

🔗 [youtube.com](https://www.youtube.com/watch?v=TlaJmlVQf98) • 5h ago

---

**[Please keep sharing progress. Inspires us Newbies](https://www.reddit.com/r/robotics/comments/1tq48y5/please_keep_sharing_progress_inspires_us_newbies/)**

Newbie here, looking to get into Robotics. It is very inspiring to see partially working robotics videos that people post. There are a lot of videos on YT but they are generally finished work by experts which seem to be way out of reach. When I see working prototype videos here it gives me hope and inspiration. Thank you all for sharing.

2h ago

---

**[How could we make our bots talk to each other?](https://www.reddit.com/r/robotics/comments/1tpq9cy/how_could_we_make_our_bots_talk_to_each_other/)**

We are considering getting our bots to have a battle mode and are exploring comms between bots. What are some lightweight ways to implement this that might have already been explored and standardized? I have considered a wifi based basic comms (kinda like ROS Topics) that can allow us to have impact, health and scoring data be shared between bots that can allow us to really have a screen free battling experience.

13h ago

---

**[Testing pure pursuit for omni-directional robot](https://www.reddit.com/r/robotics/comments/1tq5h3f/testing_pure_pursuit_for_omnidirectional_robot/)**

Just a little showcase on my implementation of pure pursuit for omni-directional robots. The original project was made back in late 2024 for the then upcoming ABU Robocon 2025 competition. Ended up not using it in the real competition due to mechanical oopsie with the lidar. And a year later I decided to revisit it and do some more tweaking. It is still not perfect as I need to implement the feed forward control to help the robot slow down smoothly when entering the curve. I also tested the combination of Google Cartographer with 2D Lidar + odom + IMU, which is something that Japan, China and Cambodia teams have done and able to somehow break the 2D flat word assumption on elevated competition field (with slope) while still maintaining accurate localization.

1h ago

---

**[Trained a SO101 robot to flip a tube upright and balance it on a tiny platform.](https://www.reddit.com/r/robotics/comments/1tpampg/trained_a_so101_robot_to_flip_a_tube_upright_and/)**

trained a diffusion policy on the so-101 using @LeRobotHF to flip a tube upright and place it on a small platform the balancing is the part that surprised me. platform’s barely wider than the tube but the policy lands it cleanly and lets go without tipping it 150 episodes across 30 cells, 12 hr training on a g5.16xlarge works really well inside cells, weaker on interpolation between them Write more about it here https://x.com/pbshgthm/status/2059654080134529082?s=46 what’s a good way to handle inter-cell interpolation without just collecting more data?

23h ago

---

**[Robots learning manipulation through “imagination” instead of endless real-world trial and error](https://www.reddit.com/r/robotics/comments/1tpppqg/robots_learning_manipulation_through_imagination/)**

RISE is an interesting robot learning project from CUHK, HKU, Tsinghua, and collaborators. Instead of relying only on costly real-world trial and error, it uses a compositional world model to let the policy improve through imagined rollouts, then tests on tasks like dynamic brick sorting, backpack packing, and box closing with a PiPER 6-DOF arm. Interesting example of how world models are being applied to real-world robot manipulation.

14h ago

---

**[Spider robot, leg test](https://www.reddit.com/r/robotics/comments/1tpt60s/spider_robot_leg_test/)**

11h ago

---

**[Student Built an Omni-Wheel Robotic Car Using ESP32](https://www.reddit.com/r/robotics/comments/1tpzg7w/student_built_an_omniwheel_robotic_car_using_esp32/)**

5h ago

---

---

## Google News: "robotics"

**[3D-printable humanoid legs let robotics experiments run wild](https://arstechnica.com/ai/2026/05/3d-printable-humanoid-legs-let-robotics-experiments-run-wild/)**

Hugging Face debuts $2,500 bipedal robot project for builders and researchers.

Ars Technica • 1d ago

---

**[Oops! Domino's-Partnered Robotics Startup That Was Supposed to Put Human Pizza Chefs Out of a Job Just Shut Down](https://futurism.com/robots-and-machines/dominos-robotics-startup-pizza-shuts-down)**

A startup that developed a robot capable of putting human restaurant workers out of a job and partnered with Domino's, has shut down.

Futurism • 1d ago

---

**[Robotics team looks at its creation as a new species, not copy of humans or animals](https://apnews.com/video/robotics-team-looks-at-its-creation-as-a-new-species-not-copy-of-humans-or-animals-3b7aafa7ea5e40afb98fac619bdeebd8)**

Argus looks more like a virus than a robot, and that's the point. The team at Duke University's General Robotics Lab says they're out to create a new species, not just more copies of humans, dogs or birds.

AP News • 22h ago

---

**[Alibaba, Tencent lead pivot from chatbots to embodied AI for robotics](https://www.scmp.com/tech/tech-trends/article/3355178/alibaba-tencent-lead-pivot-chatbots-embodied-ai-robotics)**

South China Morning Post • 5h ago

---

**[American Rheinmetall and Harbinger partnership in the field of robotics](https://www.rheinmetall.com/en/media/news-watch/news/2026/05/2026-05-27-american-rheinmetall-and-harbinger-partnership-in-the-field-of-robotics)**

American Rheinmetall and Harbinger partner to develop hybrid robotic and unmanned ground vehicles in support of U.S. Department of War modernization priorities.

Rheinmetall • 1d ago

---

**[Inside a Millersville lab, interns collaborate on real-world robotics projects](https://lancasteronline.com/news/local/inside-a-millersville-lab-interns-collaborate-on-real-world-robotics-projects/article_475df3c7-7621-4391-9884-06dfdd733c70.html)**

Wheel.Me hummed and hugged the ground as the autonomous mobile robot careened around corners, working its way through the aisles of Millersville University’s Automation and Robotics Lab.

LancasterOnline • 1d ago

---

**[Delivery robots are spreading across LA. Residents ‘both pity and hate them’](https://www.theguardian.com/us-news/2026/may/25/los-angeles-delivery-robots)**

A region known for its lack of walkability now has more obstacles for pedestrians to contend with

The Guardian • 3d ago

---

**[Elbit acquires Bluewhite as it deepens push into AI robotics](https://www.calcalistech.com/ctechnews/article/hy9w5znlfl)**

Deal adds AI-powered ground autonomy platform with 100,000 hours of operational use, strengthening Elbit’s efforts to integrate unmanned systems across air and land domains.

CTech • 1d ago

---

**[Seattle teens to take on real-world ocean science challenges in underwater robotics championship](https://www.geekwire.com/2026/seattle-teens-to-take-on-real-world-ocean-science-challenges-in-underwater-robotics-championship/)**

This year's tasks include mapping cold-water coral ecosystems, deploying ocean observatory instrumentation, modeling offshore wind turbines, and operating profiling floats beneath sea ice.

GeekWire • 23h ago

---

**[Robotics, Science Underway as Cosmonauts Prep for Wednesday Spacewalk](https://www.nasa.gov/blogs/spacestation/2026/05/26/robotics-science-underway-as-cosmonauts-prep-for-wednesday-spacewalk/)**

Robotics controllers wrapped up a weekend of swapping scientific hardware packed inside the SpaceX Dragon cargo spacecraft’s trunk for installation on the International Space Station. Meanwhile, the Expedition 74 crew is continuing its biotechnology and botany research while getting ready for a spacewalk scheduled for Wednesday, May 27.

NASA (.gov) • 1d ago

---

---

## YouTube Videos: "robotics"

**[Inside The $440 Million Startup Building The Brain For Physical AI](https://www.youtube.com/watch?v=PyGkn9DYm9s)**

Meet Generalist, the startup that says the next big leap in robotics won't come from fancier humanoid hardware. It will come from ...

📺 Forbes

👁️ 15K • 👍 436 • 💬 22 • ⏱️ 10:21 • 23h ago

---

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 10K • 👍 196 • 💬 46 • ⏱️ 18:21 • 4d ago

---

**[War Robots - New Robot Shoggoth Unlocked In Update 12.1 WR Shoggoth Gameplay](https://www.youtube.com/watch?v=kfHnflcURI0)**

War Robots - New robot Shoggoth unlocked in update 12.1. In this video, I run a maxed out MK3 Shoggoth with new weapons ...

📺 Adrian Chong

👁️ 6K • 👍 265 • 💬 54 • ⏱️ 18:23 • 1d ago

---

**[Shoggoth 👾 Robot Spotlight — War Robots](https://www.youtube.com/watch?v=Csn_o89Y3Fg)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 111K • 👍 3K • 💬 230 • ⏱️ 1:55 • 2d ago

---

**[Why the F.03 Robot’s 200-Hour Run is Terrifying 🤖](https://www.youtube.com/watch?v=LOrV7WK8C4w)**

The gap between human and machine just closed. What started as a standard 8-hour engineering challenge turned into a ...

📺 Singular Podcast

👁️ 83K • 👍 1K • 💬 154 • ⏱️ 0:32 • 6d ago

---

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 86K • 👍 1K • 💬 378 • ⏱️ 5:15 • 5d ago

---

**[&quot;Not Sure This Is a Good Idea...&quot; NEO&#39;s AI Robot Will be Shipping This Year, Anton Orders Prototype](https://www.youtube.com/watch?v=pLgnzQ21HqM)**

Tiege Hanley: Get your first box 40% off (+ FREE gift), and 20% off for life, at https://tiege.com/morningshow Join the Bag Chasers ...

📺 The Millionaire Morning Show w/ Anton Daniels

👁️ 13K • 👍 509 • 💬 220 • ⏱️ 22:52 • 1d ago

---

**[Shaq surprises Kenny and Chuck with ROBOTS 🤖😂 | Inside the NBA](https://www.youtube.com/watch?v=nIPenYETLtI)**

On Inside the NBA, Shaquille O'Neal surprises Kenny "The Jet" Smith and Charles Barkley with his robots. ✔️ Subscribe to ...

📺 ESPN

👁️ 252K • 👍 5K • 💬 485 • ⏱️ 4:57 • 2d ago

---

**[4 Robotics Stocks (ALREADY Making Money)](https://www.youtube.com/watch?v=19SrFEBkK8s)**

Physical AI isn't coming. It's already performing surgeries, sorting packages at warehouse speeds, running factory floors, and ...

📺 MarketBeat

👁️ 23K • 👍 620 • 💬 8 • ⏱️ 3:00 • 1d ago

---

**[Extreme Dynamic Symmetry EnablesOmnidirectional and Multifunctional Robots](https://www.youtube.com/watch?v=Nd-I4YNQEuY)**

Project website (paper, code, video): http://generalroboticslab.com/Argus Abstract: Symmetry is a central organizing principle in ...

📺 General Robotics Lab

👁️ 8K • 👍 670 • 💬 129 • ⏱️ 3:03 • 22h ago

---

---

*Generated by PeekDeck - A glance is all you need*

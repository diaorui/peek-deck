---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-20T19:12:20.400573+00:00'
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

**Last Updated:** March 20, 2026 at 19:12 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Range of motion evaluation test for my homemade robotic hand & wrist](https://www.reddit.com/r/robotics/comments/1ryzwte/range_of_motion_evaluation_test_for_my_homemade/)**

Showcasing the newest version (v20) of my hand & wrist combo! Same as the last version, it's a combination of direct- and tendon-driven actuation, still with 19 joints and 10 active DOFs. It has independent finger flexion, a 3-DOF thumb, linked finger splay, and a 2-DOF wrist. There's an onboard ESP32-S3 in the wrist which measures joint position (at the motor output), current, and temperature. And all the movements were programmed with custom C#/C++ software. Improved from the last version, the base thumb joints were switched to direct drive and much beefier motors were swapped in for the wrist joints - improving strength and repeatability under heavier loads. Despite these new motors though, the form factor remains nearly identical to v19, spare a few millimeters of thickness and height. Some more minor changes: (1) ASA and carbon fiber filaments replaced basic PLA to improve rigidity and strength, (2) the power input was switched to an XT30 connector to accommodate the more power-hungry motors, and (3) better filtering and chips to reduce current and position signal noise. Still making incremental improvements here and there, but happy to answer any questions and hear your thoughts!

3h ago

---

**[Humanoid robots on the streets at midnight training for their half-marathon!](https://www.reddit.com/r/robotics/comments/1rz19uy/humanoid_robots_on_the_streets_at_midnight/)**

Don't be surprised if you meet humanoid robots on the streets of Beijing at midnight. They are training for their half-marathon! Over 20 teams joined the first trial run. The official race will be held on April 19.

2h ago

---

**[Physical Intelligence developed an RL method for fine-tuning their models for precise tasks in just a few hours or even minutes](https://www.reddit.com/r/robotics/comments/1ryt963/physical_intelligence_developed_an_rl_method_for/)**

From Physical Intelligence on 𝕏 (thread with multiple videos): https://x.com/physical_int/status/2034728220818641363 Technical Blog post: https://www.pi.website/research/rlt

8h ago

---

**[The Robotics team from Wissahickon High School in Ambler, Pennsylvania built a robot Miss Daisy XXIV that picks up balls and shoots them into a container.](https://www.reddit.com/r/robotics/comments/1ry3haa/the_robotics_team_from_wissahickon_high_school_in/)**

1d ago

---

**[copper-rs v0.14: deterministic robotics runtime in Rust now supports Python tasks](https://www.reddit.com/r/robotics/comments/1ryznc2/copperrs_v014_deterministic_robotics_runtime_in/)**

Copper is an open-source robotics runtime in Rust for building deterministic, observable systems. Until now, it was very much geared toward production. With v0.14, we’re opening that system up to earlier-stage work as well. In robotics, you typically prototype quickly in Python, then rebuild the system to meet determinism, safety, and observability requirements. You can validate algorithms on real logs or simulation, inspect them in a running system, and iterate without rebuilding the surrounding infrastructure. When it’s time to move to Rust, only the task needs to change, and LLMs are quite effective at helping with that step. This release also also introduces: - composable monitoring, including a dedicated safety monitors - a new Webassembly target! After CPUs and MCUs targets, Copper can now fully run in a browser for shareable demos, check out the links in the article. - The ROS2 bridge is now bidirectional, helping the gradual migrations from ROS2 from both sides of the stack The focus is continuity from early experimentation to deployment. If you’re a Python roboticist looking for a smooth path into a Rust-based production system, come talk to us on Discord, we’re happy to help.

🔗 [Copper Robotics](https://www.copper-robotics.com/whats-new/copper-rs-v014-from-prototype-to-production-without-changing-systems) • 3h ago

---

**[Robot does Flying Kick into Arcade Machines 🤦‍♂️](https://www.reddit.com/r/robotics/comments/1ry601x/robot_does_flying_kick_into_arcade_machines/)**

Why can’t robots use their lidar to scan the room and confirm there is enough space to perform an action? 🤔 Obviously I learned the hard way but it’s a good question. What do you guys think?

1d ago

---

**[Amazon acquires Rivr, maker of a stair-climbing delivery robot - TechCrunch](https://www.reddit.com/r/robotics/comments/1ryisz3/amazon_acquires_rivr_maker_of_a_stairclimbing/)**

Amazon and Jeff Bezos had previously invested in the startup. The deal signals the e-commerce giant's interest in doorstep delivery.

🔗 [TechCrunch](https://techcrunch.com/2026/03/19/amazon-acquires-rivr-maker-of-a-stair-climbing-delivery-robot/) • 17h ago

---

**[Disney Research's Lab Director on Free Range Robots](https://www.reddit.com/r/robotics/comments/1rysn71/disney_researchs_lab_director_on_free_range_robots/)**

During NVIDIA's GTC event this week attendees had the chance to see our favorite come to life snowman walking around the show floor. Disney research designer Moritz Baecher describes the technology behind creating Robot Olaf and the future of free range robots.

🔗 [Automate](https://www.automate.org/vision/industry-insights/letting-it-go-disney-researchs-lab-director-on-free-range-robots) • 8h ago

---

**[Building an A.I. navigation software that will only require a camera, a raspberry pi and a WiFi connection (DAY 6)](https://www.reddit.com/r/robotics/comments/1ryfrmu/building_an_ai_navigation_software_that_will_only/)**

Been seeing a lot of people building robots that use the ChatGPT API to give them autonomy, but that's like asking a writer to be a gymnast, so I'm building a software that makes better use of VLMs, Depth Estimation and World Models, to give autonomy to your robot. Building this in public. (skipped DAY 5 bc there was no much progress really) Today: > Tested out different visual odometry algorithms > Turns out DA3 is also pretty good for pose estimation/odometry > Was struggling for a bit generating a reasonable occupancy grid > Reused some old code from my robotics research in college > Turns out Bayesian Log-Odds Mapping yielded some kinda good results at least > Pretty low definition voxels for now, but pretty good for SLAM that just uses a camera and no IMU or other odometry methods Working towards releasing this as an API alongside a Python SDK repo, for any builder to be able to add autonomy to their robot as long as it has a camera

19h ago

---

**[Need help for the 3 DOF SCARA Plotter](https://www.reddit.com/r/robotics/comments/1rylxr3/need_help_for_the_3_dof_scara_plotter/)**

I badly need help for our problem in the plotting output of the plotter. It seems that the square is tilted at a certain angle. Can somebody help solving this problem.

15h ago

---

---

## Google News: "robotics"

**[Inside China’s robotics revolution](https://www.theguardian.com/technology/2026/mar/19/inside-chinas-robotics-revolution)**

The long read: How close are we to the sci-fi vision of autonomous humanoid robots? I visited 11 companies in five Chinese cities to find out

The Guardian • 1d ago

---

**[Mark Cuban says the future of robotics isn't humanoids, but robots and homes that are co-designed](https://www.businessinsider.com/mark-cuban-humanoid-robotics-will-fail-robots-houses-codesigned-2026-3)**

Mark Cuban said the push for humanoid robots will fail and that instead robots and spaces will be co-designed.

Business Insider • 13h ago

---

**[Amazon acquires startup Rivr to test robots for 'doorstep delivery'](https://www.cnbc.com/2026/03/19/amazon-acquires-startup-rivr-to-test-robots-for-doorstep-delivery.html)**

The company expects to test ways it can use Rivr's robots to help with "doorstep delivery" and to "improve safety outcomes" for delivery drivers.

CNBC • 21h ago

---

**[Amazon Acquires Robotics Startup, Boosting Efforts to Streamline Deliveries](https://www.theinformation.com/articles/amazon-acquires-robotics-startup-boosting-efforts-streamline-deliveries)**

Amazon has acquired autonomous robotics startup Rivr, an Amazon spokesperson confirmed, a deal that could help the commerce and logistics giant deliver packages to shoppers’ doors more efficiently. Based in Zurich and formerly known as Swiss-Mile, Rivr was valued at $110 million in an August ...

The Information • 22h ago

---

**[Amazon acquires autonomous robotics startup Rivr](https://www.engadget.com/big-tech/amazon-acquires-autonomous-robotics-startup-rivr-212839750.html)**

Amazon has acquired Rivr, a startup focused on autonomous robotics that could further the tech giant's capabilities in package deliveries.

Engadget • 21h ago

---

**[Robotics giant plans massive $90M plant in metro Detroit, 225 jobs](https://www.crainsdetroit.com/manufacturing-logistics/cdb-fanuc-robots-investment-michigan-20260319/)**

Japanese manufacturer Fanuc is plotting a large expansion in Michigan in response to demand from automakers and other customers.

Crain's Detroit • 9h ago

---

**[Chinese Robot Maker Unitree Seeks $610 Million in Shanghai IPO](https://www.bloomberg.com/news/articles/2026-03-20/chinese-robot-maker-unitree-seeks-610-million-in-shanghai-ipo)**

Bloomberg.com • 7h ago

---

**[Smarter, faster, and more human: AI system helps robots outpace their human teachers](https://techxplore.com/news/2026-03-smarter-faster-human-ai-robots.html)**

Tech Xplore • 1d ago

---

**[Techman’s Humanoid Robot Astonishes GTC 2026 Crowd, Redefining Industrial Robotics](https://www.eweek.com/news/techman-tm-xplore-i-humanoid-robot-nvidia-gtc-2026/)**

Techman unveils its TM Xplore I humanoid robot at Nvidia GTC 2026, showcasing AI-powered automation designed for real-world industrial work.

eWeek • 21h ago

---

**[Wall-climbing robots swarm US Navy warships](https://www.foxnews.com/tech/ai-newsletter-wall-climbing-robots-swarm-us-navy-warships)**

The Fox News AI Newsletter gives readers the latest AI technology advancements, covering the challenges and opportunities AI presents.

Fox News • 1d ago

---

---

## YouTube Videos: "robotics"

**[NVIDIA GTC Demo Stuns Audience With Real Olaf Robot Next To Jensen Huang](https://www.youtube.com/watch?v=pPnVsRPFWV8)**

The NVIDIA GTC keynote delivered one of the most unexpected robotics demonstrations when Jensen Huang introduced a real ...

📺 DPCcars

👁️ 141K • 👍 1K • 💬 152 • ⏱️ 2:02 • 3d ago

---

**[The Future of Flooring: Automated Sand-Cement Screeding Robot #ConstructionTech #Robotics #Flooring](https://www.youtube.com/watch?v=QK7Y1-O5koE)**

"Efficiency meets precision! Watch this automated floor screeding robot transform a rough sand-cement mix into a perfectly level ...

📺 MachineWorks Studio

👁️ 1.4M • 👍 1K • 💬 14 • ⏱️ 0:06 • 4d ago

---

**[EXCLUSIVE: This Robot Video Changed The Conversation](https://www.youtube.com/watch?v=t7BI3Z1THz4)**

Humanoid Robot Race Just Heated Up! Buying a Tesla? Use this referral link and get $500 to $1K off. My daughter: ...

📺 Brighter with Herbert

👁️ 101K • 👍 2K • 💬 319 • ⏱️ 49:45 • 6d ago

---

**[This wearable robot adds two mechanical legs behind you](https://www.youtube.com/watch?v=y1Jh2BtO-Ow)**

CENTAUR ROBOT - wearable robot adds two legs behind people to help distribute the load ...

📺 Unstoppable Gadgets

👁️ 27K • 👍 332 • 💬 21 • ⏱️ 0:17 • 1d ago

---

**[Dancing robot goes rogue in hot pot restaurant](https://www.youtube.com/watch?v=DfnIEWpbMU8)**

Video shows restaurant employees struggling to restrain a dancing robot that went rogue in a hot pot restaurant in California.

📺 NBC News

👁️ 126K • 👍 2K • 💬 464 • ⏱️ 3:38 • 1d ago

---

**[Out of control robot smashes up restaurant as waitress desperately attempts to drag it away](https://www.youtube.com/watch?v=ZyohmMJA5Ao)**

THIS is the hilarious moment a boogying robot dances too hard and sends food and cutlery flying in a high end restaurant.

📺 The Sun

👁️ 78K • 👍 1K • 💬 877 • ⏱️ 2:07 • 1d ago

---

**[Gecko Robotics Inks $71 Million Deal With US Navy](https://www.youtube.com/watch?v=82_585LieQY)**

Gecko Robotics announced a $71 million partnership with the US Navy, deploying its AI-powered robots to assess the condition ...

📺 Bloomberg Technology

👁️ 4K • 👍 121 • 💬 3 • ⏱️ 4:39 • 3d ago

---

**[AI Robot Snaps And Attacks Woman On Street (Then Gets Arrested)](https://www.youtube.com/watch?v=ZZrR7rIIPmc)**

Try the full AI cinematic workflow here: https://higgsfield.ai/s/cinema-studio-2-0-airevolutionx-pekSSk Researchers in China just ...

📺 AI Revolution

👁️ 20K • 👍 484 • 💬 42 • ⏱️ 13:18 • 4d ago

---

**[China’s New CENTAUR AI ROBOT Gives Humans Super Strength](https://www.youtube.com/watch?v=HxUhW1zIrbw)**

China just revealed a robotic system that can turn a human into something that moves like a centaur, helping people carry heavy ...

📺 AI Revolution

👁️ 49K • 👍 681 • 💬 81 • ⏱️ 14:52 • 6d ago

---

**[I Built The World&#39;s Smallest Robot Dog!](https://www.youtube.com/watch?v=nmmopQ1EEs0)**

Sesame Micro is a tangent project to the Sesame Robot Project, an open-source mini quadruped robot. This video is an insight ...

📺 Dorian Todd

👁️ 24K • 👍 2K • 💬 109 • ⏱️ 11:03 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

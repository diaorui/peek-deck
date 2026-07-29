---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-29T21:29:21.081415+00:00'
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

**Last Updated:** July 29, 2026 at 21:29 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Trump administration bans new Chinese humanoid robots, to protect US AI buildout](https://www.reddit.com/r/robotics/comments/1v9jexw/trump_administration_bans_new_chinese_humanoid/)**

🔗 [reuters.com](https://www.reuters.com/world/trump-administration-ban-new-chinese-robots-inverters-protecting-us-ai-buildout-2026-07-28/) • 18h ago

---

**[Foreign-produced mobile ground robots added to the FCC Covered List (DA 26-786)](https://www.reddit.com/r/robotics/comments/1va1i3g/foreignproduced_mobile_ground_robots_added_to_the/)**

🔗 [docs.fcc.gov](https://docs.fcc.gov/public/attachments/DA-26-786A1.pdf) • 4h ago

---

**[The depth and point cloud of 3D DTOF LIDAR HM-LD1 in dark environment](https://www.reddit.com/r/robotics/comments/1va1gi3/the_depth_and_point_cloud_of_3d_dtof_lidar_hmld1/)**

4h ago

---

**[Robot Walking](https://www.reddit.com/r/robotics/comments/1v8yonh/robot_walking/)**

Legs I built for a humanoid robot I’m building. It uses mg996R servos. Currently the angles are hardcoded but I plan on either using reinforcement learning or inverse kinematics. 3D Files: https://cad.onshape.com/documents/70f01b8e5ad7f6e6f53bece6/w/0018e339e6e08e5dc7b59583/e/d5ff5e55fff463878f55d670

1d ago

---

**[My robotics project so far and let's discuss](https://www.reddit.com/r/robotics/comments/1v8qink/my_robotics_project_so_far_and_lets_discuss/)**

After weeks of CAD and 3D printing, I realized that the motors I chose - Feetech S3215, wouldn't be able to handle the weights of a full body humanoid so it ended up with something like what's in the images a legs-only. The next step will be installing some electronics on top of the pelvis and let it walk. What's your ideas? I've long been into robotics and physical AI, but this process makes me realize that the hardware is too harsh to compete with existing giants, and my long term dream is full body with intelligence. There are two paths after this project in my mind, one is sticking with hardware but focus instead on dexterous hand with AI controlling/policy, second is go to build general AI brain, some thing like a OS can be installed in any body, with proper interface set up, the system automatically detects what can be controlled like motors id 1-x and what's peak torque of each, and the 3D body file for the brain to understand what it's controlling, and then it can do general task within the new body, with image/vision as major sensor type. what do you folks think?

1d ago

---

**[Community PR fixes two teleoperation bugs in LeRobot v6.1.1-beta — Alicia-D Leader support & duplicate command prevention](https://www.reddit.com/r/robotics/comments/1v9r132/community_pr_fixes_two_teleoperation_bugs_in/)**

Hey everyone, Just wanted to highlight a community pull request we received on our LeRobot fork (v6.1.1-beta branch). A user identified and fixed two issues in lerobot-teleoperate: Bug 1 — Missing alicia_d_leader in teleop.type: When trying to teleoperate with an Alicia-D Leader + Alicia-M Follower pair, the CLI would reject alicia_d_leader as an invalid choice. The fix adds it back to the valid options list in lerobot_teleoperate.py. Bug 2 — Missing teleop.directly_controls_robot support: When the teleoperator directly controls the robot via hardware (e.g., the leader arm is physically connected to the follower), the computer shouldn't re-send the action command — otherwise it duplicates. The flag existed in config but wasn't actually implemented in the teleoperate script. The PR adds the skip logic. PR here: https://github.com/Synria-Robotics/lerobot/pull/10 Big thanks to the contributor for the clean, well-documented fix. If you're running v6.1.1-beta with Alicia hardware, this PR is worth watching. And as always, issues and PRs are welcome!

12h ago

---

**[My robot project so far](https://www.reddit.com/r/robotics/comments/1v8eivl/my_robot_project_so_far/)**

Working to make a fun open source STEM robot for begginers. Uses a custom edge impulse object detection model to play "fetch". Extras are the animated eyes, "ears", voice, and programmed character behavior. Currently testing the model but looking forward to releasing it for everyone soon.

1d ago

---

**[Progress Update: Testing Éloi’s Reflexes.](https://www.reddit.com/r/robotics/comments/1v8oul6/progress_update_testing_élois_reflexes/)**

Éloi is the non-functional companion robot currently being developed by Animotion Robotics. With its dreamy violet eyes, we’re now testing one of its core reflex mechanisms. When an object suddenly approaches its eyes, Éloi instinctively reacts with fear—blinking, twitching its mouth, and even furrowing its brows. These subtle expressions are designed to make its responses feel more lifelike and emotionally believable, rather than simply programmed. Éloi will feature at least 42 degrees of facial actuation, enabling a rich range of nuanced expressions and emotional reactions.

1d ago

---

**[Fun demos and findings: a decoupled parallel wrist](https://www.reddit.com/r/robotics/comments/1v8m15d/fun_demos_and_findings_a_decoupled_parallel_wrist/)**

Came across the recent DexWrist paper out of MIT and some fun demos. Researchers point out an interesting mechanical issue: standard serial wrists (like the ones on a UR3e or Franka) are often too stiff and bulky. In tight spaces, they force human operators into awkward, large arm movements just to reorient the gripper, which makes teleoperation slow and messy. They built a compact, decoupled parallel wrist using QDD actuators (integrated onto an AgileX Robotics PiPER base) that co-locates the pitch and yaw axes, much like a human wrist. Because it moves so much more intuitively, human teleoperation time dropped by up to 2.2x. The models trained on this cleaner data then saw a 50-76% relative improvement in success rates for contact-rich tasks. So to what extent hardware choices quietly shape robot learning data quality?

1d ago

---

**[We open-sourced our training setup for VLA / world-action models — Pi0.5, GR00T, DreamZero, up to 2.67x over the official repos](https://www.reddit.com/r/robotics/comments/1v94cik/we_opensourced_our_training_setup_for_vla/)**

If you train VLA / world-action models, you've probably noticed the training side is kind of underbaked compared to LLMs. Usually you're stuck on each model's official repo, and throughput was never really the point there. We open-sourced LoongForge to scratch that itch. It has ready-to-run configs for Pi0.5, GR00T N1.6&N1.7, X-VLA, FastWAM, DreamZero, Lingbot-VA and a couple more. On those, we measured up to 2.67x higher training throughput over the official implementations (DreamZero 2.67x, GR00T 2.31x, Pi0.5 2.23x; the weaker cases are around 1.6x). The numbers and the setups behind them are all in the repo. Honestly I'm mostly posting because I want to know what actually breaks for you when you train these — that's what we'll work on next. github：https://github.com/baidu-baige/LoongForge

1d ago

---

---

## Google News: "robotics"

**[How Brian Klos and Darragh de Stonndún Built Automated Industrial Robotics (AIR) Into an Engineering-Led Approach to American Manufacturing](https://www.usatoday.com/story/special/contributor-content/2026/07/29/how-brian-klos-and-darragh-de-stonndn-built-automated-industrial-robotics-air-into-an-engineering-le/91095756007/)**

The company operates in pharmaceutical production, precision assembly, and complex systems integration, sectors where the requirements for accuracy and consistency are unforgiving and where the relationship between an automation provider and a facility operator needs to be sustained and genuinely co

USA Today • 2h ago

---

**[$6M innovation center, robotics credentials and new hires signal big year at Indian Creek](https://wtov9.com/news/local/6m-innovation-center-robotics-credentials-and-new-hires-signal-big-year-at-indian-creek-indian-creek-robotics-program-fanuc-certification-innovation-center-jefferson-county-new-teachers-new-coaches-workforce-skills)**

Students in the Indian Creek Local School District will be heading back to the classroom in about a month, and Superintendent T.C. Chappelear said the coming sc

WTOV • 1h ago

---

**[Robotics startup Generalist AI is in talks to raise a new funding round at a $3 billion valuation](https://www.businessinsider.com/startup-generalist-ai-in-talks-to-raise-at-billion-valuation-2026-7)**

Venture firm 8VC is expected to lead the round as investors pour money into physical AI.

Business Insider • 4h ago

---

**[US bans foreign-made humanoid robots, targeting China over national security - ABC News](https://abcnews.com/Business/wireStory/us-bans-foreign-made-humanoid-robots-targeting-china-135179676)**

The U.S. Federal Communications Commission has announced a ban on new foreign-made humanoid robots, citing national security concerns

ABC News - Breaking News, Latest News and Videos • 14h ago

---

**[XYZ Robotics Advances Physical AI Through Real-World Data and Robot Learning](https://www.wboc.com/online_features/press_releases/xyz-robotics-advances-physical-ai-through-real-world-data-and-robot-learning/article_501dfdf3-a9c5-5518-94c3-ec31efec6a75.html)**

Company Secures 3,000 Real-World Data Points Daily at Café Locations South Korean AI robotics company XYZ Robotics Inc.

WBOC TV • 11h ago

---

**[Developing Healthcare Robotics with GPU-Native Medical Physics Simulation](https://developer.nvidia.com/blog/developing-healthcare-robotics-with-gpu-native-medical-physics-simulation/)**

Unlike autonomous driving or industrial robotics, healthcare robotics can’t rely on internet-scale data collection or unlimited real-world experimentation. Every demonstration requires specialized…

NVIDIA Developer • 1d ago

---

**[Making robots faster by helping them think ahead](https://news.mit.edu/2026/making-robots-faster-helping-them-think-ahead-0728)**

The VLASH technique, developed by MIT researchers, helps robots think ahead while moving, eliminating lags that occur between different chunks of action. This smooths and streamlines robot motion, accelerating performance on tasks like pick-and-place, sorting, and stacking.

MIT News • 1d ago

---

**[Israeli AI robotics startup Enigma emerges from stealth with $71 million Seed round](https://www.calcalistech.com/ctechnews/article/h1tdxjhrgx)**

Founded by former Unit 8200 researchers, Enigma is developing foundation AI models designed to make robots more intelligent and easier to deploy.

calcalistech.com • 2d ago

---

**[China's Unitree Robotics eyes capacity boost to meet humanoid demand](https://asia.nikkei.com/editor-s-picks/interview/china-s-unitree-robotics-eyes-capacity-boost-to-meet-humanoid-demand)**

Senior executive sees Japan as potential engineering hub

Nikkei Asia • 1d ago

---

**[Robotics Startup Tacta Shows Its Hand (and Glove)](https://www.theinformation.com/newsletters/ai-agenda/robotics-startup-tacta-shows-hand-glove)**

As robotics companies explore new ways to collect the massive volumes of data needed to train the physical AI models that will power humanoid robots, one approach is gaining steam. Some robotics companies are relying on specialized gloves that people can wear while they carry out tasks at work ...

The Information • 2d ago

---

---

## YouTube Videos: "robotics"

**[US bans imports of new Chinese robots and power inverters in latest tech crackdown](https://www.youtube.com/watch?v=qZsrLRxlauU)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Citing threats to US national security, the Trump ...

📺 South China Morning Post

👁️ 16K • 👍 738 • 💬 183 • ⏱️ 1:48 • 10h ago

---

**[Viral video of new robot released by Chinese Unitree freaks out social media](https://www.youtube.com/watch?v=GHbywXK2NMo)**

Chinese robotics company Unitree released a new video of its "super athlete" model. It's going viral for its impressive all-terrain ...

📺 NBC News

👁️ 341K • 👍 4K • 💬 2K • ⏱️ 2:15 • 1d ago

---

**[China will soon be leading in Robotics Worldwide...](https://www.youtube.com/watch?v=zPgq4fIYDSE)**

📺 Tech OverWatch

👁️ 6K • 👍 542 • 💬 35 • ⏱️ 1:03 • 5h ago

---

**[Tech News 2216 || AI Open Weight, Galaxy AI Glasses, WhatsApp, Tau Robotics, Infosys, PS 5 Sale.Etc.](https://www.youtube.com/watch?v=8Tds9CH6gos)**

Tech News 2216 || AI Open Weight, Galaxy AI Glasses, WhatsApp, Tau Robotics, Infosys, PS 5 Price Hike.Etc... Deal Of The Day ...

📺 Prasadtechintelugu

👁️ 89K • 👍 6K • 💬 246 • ⏱️ 9:12 • 7h ago

---

**[Inside the Inspire RH56DFQ Robotic Hand | Complete Teardown](https://www.youtube.com/watch?v=nhOiGu9qqzY)**

In this episode of Munro Live, we perform a complete teardown of the Inspire Robots RH56DFQ robotic hand to examine the ...

📺 Munro Live

👁️ 19K • 👍 180 • 💬 14 • ⏱️ 20:04 • 1d ago

---

**[Solving the Hardest Problem in Robotics | Fei-Fei Li with a16z](https://www.youtube.com/watch?v=-tabaM5l3s0)**

Last week, World Labs announced its acquisition of SceniX, bringing together two teams working on one of AI's biggest unsolved ...

📺 a16z

👁️ 12K • 💬 20 • ⏱️ 42:21 • 1d ago

---

**[America&#39;s first robot security force? Company aims to make country safest in world](https://www.youtube.com/watch?v=r_SstYY9STc)**

A tech company that specializes in building autonomous robots wants to make Americans safer by creating the country's first ...

📺 NewsNation

👁️ 6K • 👍 168 • 💬 98 • ⏱️ 3:10 • 2d ago

---

**[Why is the FCC banning new human-like robots from China?](https://www.youtube.com/watch?v=rao2KMyxH_0)**

The Trump administration said it's banning new Chinese humanoid robots, topped with AI-enabled "brains," as part of an attempt ...

📺 Reuters

👁️ 7K • 👍 155 • 💬 64 • ⏱️ 1:27 • 20h ago

---

**[Jared Isaacman: NASA&#39;s Moon Base by 2028, Optimus Robots on the Moon, and 15 Years to Mars | Ep #274](https://www.youtube.com/watch?v=nV_lyWrkBs8)**

The mates chat with Jared Isaacman on NASA's plan for a Moon base by 2028, Optimus Robots on the Moon, and exploring UAPs ...

📺 Peter H. Diamandis

👁️ 103K • 👍 3K • 💬 461 • ⏱️ 1:27:17 • 2d ago

---

**[What Should We Call This? 😳 #engineering #technology #robot](https://www.youtube.com/watch?v=vLtOhVjhReE)**

One of the strangest kinematic designs you'll ever see This is a Parallel Axis Tripteron concept. Instead of stacking heavy ...

📺 mechdesign98

👁️ 9K • 👍 96 • 💬 11 • ⏱️ 0:10 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*

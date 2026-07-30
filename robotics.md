---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-30T09:13:35.200011+00:00'
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

**Last Updated:** July 30, 2026 at 09:13 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Foreign-produced mobile ground robots added to the FCC Covered List (DA 26-786)](https://www.reddit.com/r/robotics/comments/1va1i3g/foreignproduced_mobile_ground_robots_added_to_the/)**

🔗 [docs.fcc.gov](https://docs.fcc.gov/public/attachments/DA-26-786A1.pdf) • 16h ago

---

**[The depth and point cloud of 3D DTOF LIDAR HM-LD1 in dark environment](https://www.reddit.com/r/robotics/comments/1va1gi3/the_depth_and_point_cloud_of_3d_dtof_lidar_hmld1/)**

16h ago

---

**[Trump administration bans new Chinese humanoid robots, to protect US AI buildout](https://www.reddit.com/r/robotics/comments/1v9jexw/trump_administration_bans_new_chinese_humanoid/)**

🔗 [reuters.com](https://www.reuters.com/world/trump-administration-ban-new-chinese-robots-inverters-protecting-us-ai-buildout-2026-07-28/) • 1d ago

---

**[3D model prototype of Capstan drive robotic arm. Ideas?](https://www.reddit.com/r/robotics/comments/1vacaqw/3d_model_prototype_of_capstan_drive_robotic_arm/)**

-This is a really rough 3d model of a capstan drive robot arm I am trying to build. My plan is to use fast and high RPM motors high gear reductions to get high precision and torque. -My goal is to use capstan drives as the end speed reducer because they are low backlash and precise, and then use belt drives and maybe planetary gear boxes to get the higher gear reduction in the earlier stages. This way if there is a little bit of backlash in the planetary gear box, that backlash gets divided by 1/8th. -For the first prototype I am printing I plan to use Aaed Musa capstan design, but later when I make the final product I will design my own. -Any ideas how to improve the deign or improve the robotic arm in general? -Dimensions: 3ft ish

10h ago

---

**[Robot Walking](https://www.reddit.com/r/robotics/comments/1v8yonh/robot_walking/)**

Legs I built for a humanoid robot I’m building. It uses mg996R servos. Currently the angles are hardcoded but I plan on either using reinforcement learning or inverse kinematics. 3D Files: https://cad.onshape.com/documents/70f01b8e5ad7f6e6f53bece6/w/0018e339e6e08e5dc7b59583/e/d5ff5e55fff463878f55d670

1d ago

---

**[My robotics project so far and let's discuss](https://www.reddit.com/r/robotics/comments/1v8qink/my_robotics_project_so_far_and_lets_discuss/)**

After weeks of CAD and 3D printing, I realized that the motors I chose - Feetech S3215, wouldn't be able to handle the weights of a full body humanoid so it ended up with something like what's in the images a legs-only. The next step will be installing some electronics on top of the pelvis and let it walk. What's your ideas? I've long been into robotics and physical AI, but this process makes me realize that the hardware is too harsh to compete with existing giants, and my long term dream is full body with intelligence. There are two paths after this project in my mind, one is sticking with hardware but focus instead on dexterous hand with AI controlling/policy, second is go to build general AI brain, some thing like a OS can be installed in any body, with proper interface set up, the system automatically detects what can be controlled like motors id 1-x and what's peak torque of each, and the 3D body file for the brain to understand what it's controlling, and then it can do general task within the new body, with image/vision as major sensor type. what do you folks think?

2d ago

---

**[Community PR fixes two teleoperation bugs in LeRobot v6.1.1-beta — Alicia-D Leader support & duplicate command prevention](https://www.reddit.com/r/robotics/comments/1v9r132/community_pr_fixes_two_teleoperation_bugs_in/)**

Hey everyone, Just wanted to highlight a community pull request we received on our LeRobot fork (v6.1.1-beta branch). A user identified and fixed two issues in lerobot-teleoperate: Bug 1 — Missing alicia_d_leader in teleop.type: When trying to teleoperate with an Alicia-D Leader + Alicia-M Follower pair, the CLI would reject alicia_d_leader as an invalid choice. The fix adds it back to the valid options list in lerobot_teleoperate.py. Bug 2 — Missing teleop.directly_controls_robot support: When the teleoperator directly controls the robot via hardware (e.g., the leader arm is physically connected to the follower), the computer shouldn't re-send the action command — otherwise it duplicates. The flag existed in config but wasn't actually implemented in the teleoperate script. The PR adds the skip logic. PR here: https://github.com/Synria-Robotics/lerobot/pull/10 Big thanks to the contributor for the clean, well-documented fix. If you're running v6.1.1-beta with Alicia hardware, this PR is worth watching. And as always, issues and PRs are welcome!

23h ago

---

**[My robot project so far](https://www.reddit.com/r/robotics/comments/1v8eivl/my_robot_project_so_far/)**

Working to make a fun open source STEM robot for begginers. Uses a custom edge impulse object detection model to play "fetch". Extras are the animated eyes, "ears", voice, and programmed character behavior. Currently testing the model but looking forward to releasing it for everyone soon.

2d ago

---

**[Progress Update: Testing Éloi’s Reflexes.](https://www.reddit.com/r/robotics/comments/1v8oul6/progress_update_testing_élois_reflexes/)**

Éloi is the non-functional companion robot currently being developed by Animotion Robotics. With its dreamy violet eyes, we’re now testing one of its core reflex mechanisms. When an object suddenly approaches its eyes, Éloi instinctively reacts with fear—blinking, twitching its mouth, and even furrowing its brows. These subtle expressions are designed to make its responses feel more lifelike and emotionally believable, rather than simply programmed. Éloi will feature at least 42 degrees of facial actuation, enabling a rich range of nuanced expressions and emotional reactions.

2d ago

---

**[Fun demos and findings: a decoupled parallel wrist](https://www.reddit.com/r/robotics/comments/1v8m15d/fun_demos_and_findings_a_decoupled_parallel_wrist/)**

Came across the recent DexWrist paper out of MIT and some fun demos. Researchers point out an interesting mechanical issue: standard serial wrists (like the ones on a UR3e or Franka) are often too stiff and bulky. In tight spaces, they force human operators into awkward, large arm movements just to reorient the gripper, which makes teleoperation slow and messy. They built a compact, decoupled parallel wrist using QDD actuators (integrated onto an AgileX Robotics PiPER base) that co-locates the pitch and yaw axes, much like a human wrist. Because it moves so much more intuitively, human teleoperation time dropped by up to 2.2x. The models trained on this cleaner data then saw a 50-76% relative improvement in success rates for contact-rich tasks. So to what extent hardware choices quietly shape robot learning data quality?

2d ago

---

---

## Google News: "robotics"

**[The Chinese robot army transforming the UK's retail industry](https://www.bbc.com/news/articles/c0jl8v23qwgo)**

Britain's weak productivity growth and labour shortages are creating an opportunity for China's robotics firms.

BBC • 11h ago

---

**[Trump administration bans new Chinese humanoid robots, to protect US AI buildout](https://www.reuters.com/world/trump-administration-ban-new-chinese-robots-inverters-protecting-us-ai-buildout-2026-07-28/)**

Reuters • 1d ago

---

**[Developing Healthcare Robotics with GPU-Native Medical Physics Simulation](https://developer.nvidia.com/blog/developing-healthcare-robotics-with-gpu-native-medical-physics-simulation/)**

Unlike autonomous driving or industrial robotics, healthcare robotics can’t rely on internet-scale data collection or unlimited real-world experimentation. Every demonstration requires specialized…

NVIDIA Developer • 1d ago

---

**[Robotics startup Generalist AI is in talks to raise a new funding round at a $3 billion valuation](https://www.businessinsider.com/startup-generalist-ai-in-talks-to-raise-at-billion-valuation-2026-7)**

Venture firm 8VC is expected to lead the round as investors pour money into physical AI.

Business Insider • 16h ago

---

**[Robotics giant plans major expansion in Michigan](https://www.mlive.com/news/detroit/2026/07/robotics-giant-plans-major-expansion-in-michigan.html)**

MLive.com • 1d ago

---

**[Denham Springs robotics team wins Indiana Robotics Invitational](https://www.wbrz.com/news/denham-springs-robotics-team-wins-indiana-robotics-invitational/)**

The Denham Springs High School robotics team won the Indiana Robotics Invitational on July 18 in Indianapolis, beating the event's top-seeded alliance in the finals.

WBRZ • 1d ago

---

**[How Brian Klos and Darragh de Stonndún Built Automated Industrial Robotics (AIR) Into an Engineering-Led Approach to American Manufacturing](https://www.usatoday.com/story/special/contributor-content/2026/07/29/how-brian-klos-and-darragh-de-stonndn-built-automated-industrial-robotics-air-into-an-engineering-le/91095756007/)**

The company operates in pharmaceutical production, precision assembly, and complex systems integration, sectors where the requirements for accuracy and consistency are unforgiving and where the relationship between an automation provider and a facility operator needs to be sustained and genuinely co

USA Today • 14h ago

---

**[Making robots faster by helping them think ahead](https://news.mit.edu/2026/making-robots-faster-helping-them-think-ahead-0728)**

The VLASH technique, developed by MIT researchers, helps robots think ahead while moving, eliminating lags that occur between different chunks of action. This smooths and streamlines robot motion, accelerating performance on tasks like pick-and-place, sorting, and stacking.

MIT News • 2d ago

---

**[SoftBank eyes $500M Gravis Robotics deal after completing its Boston Dynamics exit](https://techfundingnews.com/softbank-eyes-500m-gravis-robotics-deal-after-completing-its-boston-dynamics-exit/)**

Tech Funding News • 2d ago

---

**[Israeli AI robotics startup Enigma emerges from stealth with $71 million Seed round](https://www.calcalistech.com/ctechnews/article/h1tdxjhrgx)**

Founded by former Unit 8200 researchers, Enigma is developing foundation AI models designed to make robots more intelligent and easier to deploy.

calcalistech.com • 2d ago

---

---

## YouTube Videos: "robotics"

**[FCC chair Carr defends new ban on foreign-made humanoid robots](https://www.youtube.com/watch?v=kTeCO57t9cs)**

The Trump administration will ban foreign-made humanoid robots in the U.S. as China seeks to dominate the emerging high-tech ...

📺 NBC News

👁️ 13K • 👍 125 • 💬 167 • ⏱️ 6:04 • 9h ago

---

**[The U.S. Just Banned Chinese Humanoid Robots… I Own Two](https://www.youtube.com/watch?v=wNaohV4eY0A)**

The U.S. just banned Chinese humanoid robots… or did it? I own the Unitree G1 and Agibot X2, so here's what the new U.S. ...

📺 KhanFlicks

👁️ 973 • 💬 27 • ⏱️ 3:45 • 12h ago

---

**[USA Banning Chinese Humanoid Robots - America Can&#39;t Compete with China](https://www.youtube.com/watch?v=QZLrwIAYiZU)**

Spotify - https://open.spotify.com/show/1KkKuQe82tf1bW78ReQ0wM Apple Podcasts ...

📺 Eli the Computer Guy

👁️ 6K • 👍 425 • 💬 214 • ⏱️ 20:17 • 9h ago

---

**[Viral video of new robot released by Chinese Unitree freaks out social media](https://www.youtube.com/watch?v=GHbywXK2NMo)**

Chinese robotics company Unitree released a new video of its "super athlete" model. It's going viral for its impressive all-terrain ...

📺 NBC News

👁️ 487K • 👍 5K • 💬 2K • ⏱️ 2:15 • 2d ago

---

**[Solving the Hardest Problem in Robotics | Fei-Fei Li with a16z](https://www.youtube.com/watch?v=-tabaM5l3s0)**

Last week, World Labs announced its acquisition of SceniX, bringing together two teams working on one of AI's biggest unsolved ...

📺 a16z

👁️ 15K • 💬 24 • ⏱️ 42:21 • 1d ago

---

**[The FDA Just Changed Robotics Forever... Everyone Bought the Wrong Stock](https://www.youtube.com/watch?v=_6iqP7hdsk8)**

The FDA just changed the future of surgical robotics and almost everyone is watching the WRONG stock. While headlines focused ...

📺 Ross Givens

👁️ 11K • 👍 617 • 💬 148 • ⏱️ 11:31 • 16h ago

---

**[America&#39;s first robot security force? Company aims to make country safest in world](https://www.youtube.com/watch?v=r_SstYY9STc)**

A tech company that specializes in building autonomous robots wants to make Americans safer by creating the country's first ...

📺 NewsNation

👁️ 7K • 👍 185 • 💬 102 • ⏱️ 3:10 • 2d ago

---

**[Meet the Humanoid Robot with &#39;Smart Skin&#39; (I Touched It)](https://www.youtube.com/watch?v=3vGWIPIDpB4)**

Gene.01 is the new humanoid robot from Generative Bionics, featuring "smart skin" embedded with touch sensors and proximity ...

📺 CNET

👁️ 20K • 👍 548 • 💬 33 • ⏱️ 4:23 • 3d ago

---

**[US bans imports of new Chinese robots and power inverters in latest tech crackdown](https://www.youtube.com/watch?v=qZsrLRxlauU)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Citing threats to US national security, the Trump ...

📺 South China Morning Post

👁️ 26K • 👍 1K • 💬 343 • ⏱️ 1:48 • 22h ago

---

**[Jared Isaacman: NASA&#39;s Moon Base by 2028, Optimus Robots on the Moon, and 15 Years to Mars | Ep #274](https://www.youtube.com/watch?v=nV_lyWrkBs8)**

The mates chat with Jared Isaacman on NASA's plan for a Moon base by 2028, Optimus Robots on the Moon, and exploring UAPs ...

📺 Peter H. Diamandis

👁️ 108K • 👍 3K • 💬 473 • ⏱️ 1:27:17 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-22T12:05:01.395721+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 22, 2026 at 12:05 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Hand taxonomy tests with my robotic hand & wrist](https://www.reddit.com/r/robotics/comments/1tkgco6/hand_taxonomy_tests_with_my_robotic_hand_wrist/)**

Evaluating some hand grip patterns following the https://www.eng.yale.edu/grablab/pubs/Feix_THMS2016.pdf paper. I didn't do all of them because I'm lazy and some of them are pretty similar. But I'm confident my hand can achieve all of them EXCEPT the disks grips and the inferior pinch since I lack independent intermediate phalanx actuation. I chose some random objects I could find lying around that fit each grip type to see how well the hand could actually hold real household items. Overall, I think it was quite successful, what do you think?

28m ago

---

**[We made airsoft tank robots for our online video game](https://www.reddit.com/r/robotics/comments/1tk7tib/we_made_airsoft_tank_robots_for_our_online_video/)**

The real robot airsoft battles will be integrated with virtual battles seamlessly within the same matchmaking queue. We're using digital FPV equipment for the video link to a receiver pc, and then we send that to players over the internet via a custom UDP streaming protocol that also handles our normal game data. Virtual battles are standard video game servers. If you want to help with testing, we're looking for some people.

🔗 [youtube.com](https://www.youtube.com/watch?v=Nj5QkNiJvaU) • 7h ago

---

**[Meet Xhand a dexterous hand for real world task](https://www.reddit.com/r/robotics/comments/1tjuztp/meet_xhand_a_dexterous_hand_for_real_world_task/)**

Meet XHand ✋ — precision, dexterity, and adaptability for real-world tasks. For building embodied AI solutions that bridge perception and action. XHand is just the beginning. #PhysicalAI #EmbodiedAI #Robotics #XHand #PNProbotics

16h ago

---

**[My color classification robot arm (repurpose tofu frying robot)](https://www.reddit.com/r/robotics/comments/1tjt0e0/my_color_classification_robot_arm_repurpose_tofu/)**

17h ago

---

**[Remote Teleop for Evals](https://www.reddit.com/r/robotics/comments/1tk4l8b/remote_teleop_for_evals/)**

Would love feedback on such an eval setup for robotic policies. Currently looking for people who are training policies and who would be interested to try something like this out.

10h ago

---

**[BLDC motor controller](https://www.reddit.com/r/robotics/comments/1tjqfz1/bldc_motor_controller/)**

For those of you running BLDC motors — what controller are you using and what frustrates you most about it? I’m trying to build something and want to understand your needs. What is the unreliable part of it?

19h ago

---

**[Battling severe voltage sag on a 48V AMR under peak torque. How do you stop your servo drives from throttling?](https://www.reddit.com/r/robotics/comments/1tjw9hg/battling_severe_voltage_sag_on_a_48v_amr_under/)**

Hey everyone, looking for a sanity check on a heavy-payload AMR project (~700kg payload) running on a 48V LiFePO4 pack. Whenever the robot hits rough terrain or accelerates suddenly, the transient current draw causes our battery bus to sag hard, dipping down to 35V-36V for a few hundred milliseconds. Our current "industrial-grade" servo drives are losing their minds under this sag. We are hitting under-voltage faults that trigger random emergency stops, massive thermal spikes inside our sealed IP65 wheel hubs as the drives draw more current to compensate, and mushy velocity control right when we need tight torque response. We’ve debated adding a bulky buck-boost regulator just to keep the drive logic stable, but it kills our payload-to-weight ratio. For those building battery-powered platforms that survive high-torque transients, are you over-specifying the battery pack to stop the sag, or switching to drives with ultra-wide input voltage ranges? Also, how do you handle the thermal overhead in a sealed housing? Do GaN-based or ultra-high-efficiency drives actually solve the heat issue at the source? Trying to avoid a massive chassis redesign just to fit a bulkier cooling system. Any advice?

15h ago

---

**[How do you determine how strong your suspension needs to be?](https://www.reddit.com/r/robotics/comments/1tjuy6o/how_do_you_determine_how_strong_your_suspension/)**

Hello, I'm working on several different ground robot designs, and I've sort of gotten stuck on the issue of suspension. Specifically, how does one determine how strong a suspension system needs to be for a given application? How do you model the forces acting on the drivetrain that need to be counteracted by the suspension? I've researched many types of suspension systems for various types of drivetrains, but while they make sense conceptually, I'm still trying to figure out the numbers to use to reduce it to a standard solid mechanics problem. Thank you for your assistance and any resources.

16h ago

---

**[Lego quadruped strandbeest first steps🥹](https://www.reddit.com/r/robotics/comments/1tizmz3/lego_quadruped_strandbeest_first_steps/)**

1d ago

---

**[Mobile OpenArm!](https://www.reddit.com/r/robotics/comments/1tjbs3l/mobile_openarm/)**

Hey r/robotics, Like many in the open-source community, we’ve been frustrated by the massive hardware premiums required to get into embodied AI research. Industrial AMRs and collaborative setups easily cross the $50k mark. We wanted to change that, so we co-developed Mobile OpenArm X1 alongside OpenArm. It is a fully transparent, modular development platform engineered specifically for low-level control, simulation, and data collection. We managed to scale the hardware cost down significantly. For context, the base Education Edition features a LiDAR-guided autonomous mobile robot paired with a 16-DoF arm/gripper setup, hitting a hardware cost of $9,000. Core Specs & Tech Stack: Mobility & Kinematics: 4WD omnidirectional AMR base supporting 360° spatial turning and continuous 360° waist rotation. Sensing: Integrated LiDAR tracking and odometry for global localization, centimeter-level positioning, and dynamic obstacle avoidance. AI / Model Training: Native spatial-action data fusion (LiDAR point clouds + joint states) optimized for training Vision-Language-Action (VLA) models. Software Ecosystem: Out-of-the-box support for Hugging Face LeRobot, ACT, and Diffusion Policy, alongside simulation integration for Isaac Gym and MuJoCo. Transparency: Complete access to low-level driver source code and unified APIs. Our goal is to build an open foundation so developers can iterate faster without proprietary walls. The platform is currently up for pre-order, and the entire stack is decoupled and modular. We'd love to hear your thoughts on the hardware layout. Are there specific sensor payload configurations or simulation environments you’d like to see natively supported out of the box? Full disclosure: I am part of the core team building NVatom. Mobile OpenArm

1d ago

---

---

## Google News: "robotics"

**[China unveils first humanoid robot for household chores, ready as early as 2027](https://www.scmp.com/tech/article/3354371/commercial-humanoid-robots-china-may-soon-do-laundry-make-beds-care-elders)**

South China Morning Post • 1d ago

---

**[Humanoid’s New Deal: Bosch Will Build Its Robots With Schaeffler Parts](https://www.forbes.com/sites/johnkoetsier/2026/05/21/humanoids-new-deal-bosch-will-build-its-robots-with-schaeffler-parts/)**

Vertical integration or partnership: that is the question in humanoid robots. The UK's Humanoid has chosen ... and it just announced a big new partner.

Forbes • 1d ago

---

**[Hyundai Plans 25,000 ‘Atlas’ Humanoid Robots for Factories by 2028](https://www.eweek.com/news/hyundai-atlas-humanoid-robots-factories/)**

Hyundai plans to deploy 25,000 Atlas humanoid robots in its factories as Boston Dynamics scales production and robot training.

eWeek • 20h ago

---

**[Will Robotics Have a ChatGPT Moment?](https://spectrum.ieee.org/robotics-ai-breakthrough)**

A single breakthrough AI moment in robotics may not be the answer

IEEE Spectrum • 2d ago

---

**[AI robotic beehives installed in Florida community claim 70% reduction in colony collapse threatening crops](https://www.foxnews.com/science/ai-robotic-beehives-installed-florida-community-claim-70-reduction-colony-collapse-threatening-crops)**

A Florida community deploys AI-powered robotic beehives to protect declining bee populations that pollinate roughly 75% of the crops Americans eat.

Fox News • 11h ago

---

**[AI robotic beehives deployed in Pasco County farm community](https://www.fox13news.com/news/ai-robotic-beehives-deployed-pasco-county-farm-community)**

As the U.S. bee population declines, a farm community in Pasco County is using AI-powered technology to protect its bee colonies.

FOX 13 Tampa Bay • 1d ago

---

**[AI Robotic beehive system implemented in Pasco County](https://www.wfla.com/news/pasco-county/ai-robotic-beehive-system-implemented-in-pasco-county/)**

WFLA • 1d ago

---

**[Jeff Bezos describes his $38B startup Prometheus for the first time: 'Nothing to do with robotics'](https://www.geekwire.com/2026/jeff-bezos-describes-his-38b-startup-prometheus-for-the-first-time-nothing-to-do-with-robotics/)**

In a CNBC interview, Jeff Bezos offered the most detailed public description yet of Project Prometheus, calling the secretive startup an "artificial general engineer" building next-generation design tools for physical objects.

GeekWire • 1d ago

---

**[Kawasaki Heavy, Nvidia plan Silicon Valley robotics center, Nikkei reports](https://www.reuters.com/world/asia-pacific/kawasaki-heavy-nvidia-plan-silicon-valley-robotics-center-nikkei-reports-2026-05-21/)**

Reuters • 19h ago

---

**[Quantum Computing and Robotics Are Arriving Faster Than Most Investors Realize and After Years of Covering This Space These 3 ETFs Stand Out](https://finance.yahoo.com/news/quantum-computing-robotics-arriving-faster-171144893.html)**

Intuitive Surgical’s da Vinci 5 surgical platform, which began shipping in earnest on April 1, 2026, runs on 10,000 times the computing power of the da Vinci Xi and was co-engineered with NVIDIA’s Isaac platform. That is a working hospital robot, on the floor, today, that needed an AI compute stack nobody had five years ... Quantum Computing and Robotics Are Arriving Faster Than Most Investors Realize and After Years of Covering This Space These 3 ETFs Stand Out

Yahoo Finance • 18h ago

---

---

## YouTube Videos: "robotics"

**[Is There A Robot Revolution Happening? What’s Going On?](https://www.youtube.com/watch?v=w1VKIIxk0Vc)**

Robots are getting REALLY sophisticated…so why don't we all have our own personal robot assistant yet? Watch here to find out ...

📺 NBC News

👁️ 882 • 👍 18 • ⏱️ 2:37 • 15h ago

---

**[Man vs AI Robot: it’s officially over...](https://www.youtube.com/watch?v=j5MtBTPGJng)**

Man Vs Machine - we're entering the end times of AI deployment - do you want to live in a world of AI powered robots and LLM's ...

📺 Stylosa

👁️ 14K • 👍 369 • 💬 271 • ⏱️ 16:12 • 3d ago

---

**[Apple Just Started Selling $1,000 AI Home Robots in All Stores](https://www.youtube.com/watch?v=jDmOBHB-7Ik)**

Apple's new AI home robots are being described as a major step toward bringing advanced robotics into everyday households on ...

📺 Carros Show

👁️ 6K • 👍 231 • 💬 37 • ⏱️ 23:14 • 1d ago

---

**[Testing BotBrains limite, or lack thereof.  Four legs are over rated.  #robotics #ai #robot](https://www.youtube.com/watch?v=clPhKrgNCnc)**

📺 BotBot Robotics

👁️ 1K • 👍 12 • ⏱️ 0:23 • 17h ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 99K • 👍 3K • 💬 167 • ⏱️ 22:41 • 2d ago

---

**[Do humanoid robots pose national security risk?](https://www.youtube.com/watch?v=sNhskSj2mm0)**

ABC News investigates the rise of humanoid robots manufactured in China and why experts say they pose a risk to U.S. national ...

📺 Good Morning America

👁️ 1K • 👍 14 • 💬 1 • ⏱️ 3:22 • 21h ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 32 • 💬 5 • ⏱️ 0:07 • 1d ago

---

**[I SPENT EVERYTHING I had in War Robots…](https://www.youtube.com/watch?v=oz3FCRCYBkA)**

War Robots Gameplay: Spending ALL my SILVER for Ultimate Upgrades Here's my New Channel about Raid: ...

📺 Manni-Gaming

👁️ 16K • 👍 852 • 💬 120 • ⏱️ 13:23 • 1d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=0Mn9NtAX8JE)**

📺 Robot Julie 

👁️ 26K • 👍 110 • ⏱️ 0:24 • 2d ago

---

**[These New REALISTIC FEMALE ROBOTS Are Crossing the Line – Experts TERRIFIED](https://www.youtube.com/watch?v=OTEu_9KyfPE)**

The robots in this video look real. Move real. Talk real. And that's exactly what's making some of the world's top experts seriously ...

📺 AI Exposed

👁️ 143K • 👍 1K • 💬 76 • ⏱️ 12:25 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

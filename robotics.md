---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-23T12:10:05.518368+00:00'
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

**Last Updated:** July 23, 2026 at 12:10 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Built this 6DOF using aluminum angles and acrylic plates.](https://www.reddit.com/r/robotics/comments/1v45ity/built_this_6dof_using_aluminum_angles_and_acrylic/)**

Built this 6dof with parts bought from local hardware store. Lot of loose parts now, needs fine tune or redo. Plan is to create mobile arm. Waiting for wheels and step motor. Controlled by raspberry pi.

5h ago

---

**[What Finally Helped Me Understand Inverse Kinematics After Building a 6-Axis Robot Arm](https://www.reddit.com/r/robotics/comments/1v3907d/what_finally_helped_me_understand_inverse/)**

I spent the last year building a 6-axis desktop robot arm from scratch, and inverse kinematics was the hardest concept for me to internalize. Here’s what finally helped. Forward kinematics felt relatively straightforward. Given the joint angles, I could compute the end-effector pose by chaining homogeneous transformation matrices using a consistent frame convention. Denavit–Hartenberg parameters made the process systematic, and I had the basic idea working within a weekend. Inverse kinematics was much harder. Given a desired end-effector pose, which joint configurations reach it? There may be multiple solutions, or none at all. The elbow-up vs. elbow-down configurations alone took me days to understand and debug. Three things finally made it click: Build geometric intuition before deriving equations.​ I watched each joint move independently in a 3D simulator. In my arm, joint 1 mainly changes the base azimuth, while joints 2 and 3 determine the reach in a radial-height plane. Because the arm uses a conventional wrist structure, joints 4–6 mainly control orientation. Seeing the workspace gave the equations a physical meaning. Start with a 2-DOF planar arm.​ Forget the 6-axis arm for a week. A simple 2-link arm makes the cosine-law derivation and the elbow-up/elbow-down solutions easy to visualize. Then add a third link while explicitly accounting for end-effector orientation, and add more joints one at a time. Numerical methods aren’t cheating.​ I implemented a small Jacobian-based solver in Python. It worked surprisingly well, although it still depended on the initial guess and could struggle near singularities or unreachable targets. My biggest mistake was trying to derive closed-form IK equations before understanding the workspace geometry. If you can’t visualize where the arm can reach, the equations feel almost meaningless. What approach worked for you when learning IK? Did you start with analytical methods, numerical methods, or a combination of both?

1d ago

---

**[Built my first robot](https://www.reddit.com/r/robotics/comments/1v3kseq/built_my_first_robot/)**

Built my first robot still have a lot to learn. Open to any advice on how to improve look of wires. When I built this, I lost two of the baby screws for the knee of the robot so it topples over in the middle of its dance. But it was fun to build and I learned a lot. Also, open to any ideas on other kits or sites where I can create more stuff myself following tutorials and things like that

19h ago

---

**[I built a free interactive robotics learning platform with browser-based simulators. I'd love feedback from the robotics community.](https://www.reddit.com/r/robotics/comments/1v44ws7/i_built_a_free_interactive_robotics_learning/)**

6h ago

---

**[Humanoid robots are entering factories, but manufacturers still care more about reliability than form factor](https://www.reddit.com/r/robotics/comments/1v3ige8/humanoid_robots_are_entering_factories_but/)**

Most humanoid robots in factories are still being tested in pilot programs, and many are only reaching 20% to 50% effectiveness. A3 President Jeff Burnstein told Forbes that manufacturers are not focused on whether a robot looks human. They want systems that are reliable, affordable and safe. Safety remains a major barrier because there is no dedicated humanoid robot safety standard yet, and most systems currently operate behind fences or away from workers. Burnstein expects humanoids to find roles in factories, warehouses and logistics, but alongside traditional industrial robots, mobile robots and collaborative arms rather than replacing them. The article also covers labor shortages, manufacturing competitiveness and the growing robotics gap between the U.S. and China.

🔗 [Forbes](https://www.forbes.com/sites/johnkoetsier/2026/07/20/humanoid-robots-are-coming-to-factories-but-not-the-way-you-think/) • 21h ago

---

**[I turned a smartphone into a mobile robot. Here's my latest prototype.](https://www.reddit.com/r/robotics/comments/1v3i1t7/i_turned_a_smartphone_into_a_mobile_robot_heres/)**

Hi everyone! I've been building a small mobile robot that uses a smartphone as its onboard computer. The phone handles the camera, networking and user interface, while an Arduino controls the motors and peripherals. Current features: 📱 Smartphone onboard 🌐 Browser-based remote control 🎥 Live video 💡 LED lighting 🚨 Experimental security mode 🤖 BLE Follow Me (in progress) This video shows one of today's prototype tests. Some things worked, some didn't... and some moments were just funny. 😄 That's real robotics development. The next version will focus on: quieter drivetrain, better cable management, docking station, modular accessories. I'd really appreciate your feedback and ideas for V2. Two smartphones. One drives. One controls.

21h ago

---

**[3D DTOF LIDAR HM-LD1 for UAV Obstacle Avoidance](https://www.reddit.com/r/robotics/comments/1v3i7if/3d_dtof_lidar_hmld1_for_uav_obstacle_avoidance/)**

I got HM-LD1 working for obstacle avoidance. and l will open-source once code is ready.my drone drifts backward slightly after I release the sticks.Anyone else seen this?

21h ago

---

**[Why existing robotic hands could not be used for tactile sign language](https://www.reddit.com/r/robotics/comments/1v3ewzu/why_existing_robotic_hands_could_not_be_used_for/)**

Tatum Robotics originally expected to adapt an existing robotic hand for DeafBlind users. The problem was that American Sign Language requires precise finger positioning, while many standard robotic hands rely on rigid linkages that can create pinch points. That does not work when a person needs to hold the hand directly to receive tactile signing. The team instead developed a compliant, tendon-driven hand with additional degrees of freedom. DeafBlind users can place their hand on the robot and receive letters through movements designed to closely match a human hand.

23h ago

---

**[I got an old Puma 500. Any advice for building your own DC motor servo drives?](https://www.reddit.com/r/robotics/comments/1v3z1c2/i_got_an_old_puma_500_any_advice_for_building/)**

A while back I bought an old Unimate Puma 500 arm. It had no controller. I've since cleaned it, regreased it, serviced the motors, replaced the brake pads, machined repair parts, adjusted the bearings, and replaced the wiring loom & hoses. It's now mechanically as complete as I can get it. The Puma 500 uses six 24v brushed DC motors, which I *think* are 40 and 150w, but there's no datasheets on these old custom made motors. Each motor has a 24v magnetic brake with cork brake pads. And on the back of that there's the motor sensor, which is a 500ppr rotary optical encoder (with index) and an absolute laser-trimmed potentionmeter on a delicate reduction gearbox. Each sensor seems to be functioning fine, but testing them with an Arduino Every using hardware interupts, there is some jitter(?) on the optical encoder meaning the output per revolution varies up and down by a couple of points. The only electronics inside the optical encoder is a quad-comparator and some trimpots. They all seem quite clean. I know the Puma used an analogue servo amplifier system, but there's no circuit diagrams for them that I can find anyway. So making a bespoke digital system is what I expect. Does anyone have any advice for reducing the jitter, or otherwise connecting them to modern PID/motion-control systems/designs? Whether that's aditional filtering electronics, software compenation, comparison with the absolute encoder, or something I haven't considered. I had intended to run them into a pair of Arduino Everys in groups of three plus a 14-bit ADC for the pots then feed them out by RS-485. But the jitter, and the number of inputs (and the potentially high number of interupts per second) meaning high odds of misreads from overlapping interupts means I want to scrap this plan unless I want to run it a single axis at a time.

11h ago

---

**[Do you have a robot? (eu)](https://www.reddit.com/r/robotics/comments/1v3lk4n/do_you_have_a_robot_eu/)**

Hey guys. I am building a platform where you can have virtual rooms and I am currently looking for people who have skills in robotics. Virtual room allows connections to remote real world devices. I need to find a person who can build or rent me a robot in EU (I am from Finland) or has a robot SaaS and needs to scale operations beyond 10+ robots. Pilot Specs: - Can drive 5-30km on one charge and can carry around a 1-4 kg payload. - or/ a boat robot with a bit similar specs. - can be drone too. I have this idea where you could overlook and control 100+ robots from a single virtual room. So, if there are like-minded people or this resonates then let me know.

19h ago

---

---

## Google News: "robotics"

**[Tesla's push into AI and robotics is proving costly](https://www.axios.com/2026/07/22/tesla-earnings-ai-robotics-spending)**

Axios • 12h ago

---

**[Samsung Electronics creates robotics division; ex-Hyundai executive to head strategy](https://www.reuters.com/world/asia-pacific/samsung-electronics-creates-robotics-division-key-part-growth-strategy-2026-07-21/)**

Reuters • 2d ago

---

**[Samsung Electronics shares rise as robotics move highlights push into physical AI](https://www.cnbc.com/2026/07/21/samsung-electronics-sets-up-robotics-unit-amid-push-into-physical-ai-.html)**

Samsung Electronics shares rose as the company set up a robotics division in a push into physical AI.

CNBC • 2d ago

---

**[Samsung creates robotics-dedicated unit under CEO](https://www.koreajoongangdaily.com/business/samsung-creates-roboticsdedicated-unit-under-ceo/12784702)**

The tech giant is consolidating talent, research and production planning to accelerate the commercialization of humanoid robots.

Korea JoongAng Daily • 2d ago

---

**[China’s Unitree Robotics Is Leading the Humanoid Revolution](https://time.com/article/2026/07/23/unitree-china-human-robotics/)**

The humanoid revolution is coming—and the Chinese firm Unitree is leading the charge.

Time Magazine • 10m ago

---

**[Robotic Servicing Mission Launches with NASA Support](https://www.nasa.gov/technology/robotic-servicing-mission-launches-with-nasa-support/)**

Following its liftoff from Cape Canaveral on July 21 aboard a SpaceX Falcon 9 rocket, the Mission Robotic Vehicle (MRV) hosting the NASA-supported Robotic

NASA (.gov) • 18h ago

---

**[Travis Kalanick’s robotics company raises $1.7B, led by a16z](https://techcrunch.com/2026/07/22/travis-kalanicks-robotics-company-raises-1-7b-led-by-a16z/)**

Uber is also investing in Travis Kalanick's company Atoms, which has made gauzy claims about using industrial AI to modernize the world.

TechCrunch • 17h ago

---

**[Tesla’s profits slide despite growing revenue as it pivots to robotics and AI](https://www.theguardian.com/technology/2026/jul/22/tesla-profits-earnings)**

Shares in Elon Musk company fall more 3% in after-hours trading, as earnings per share miss Wall Street expectations

The Guardian • 15h ago

---

**[Volkswagen Strengthens Horizon Robotics Tie-Up to Advance Self-Driving Technology in China](https://www.wsj.com/business/autos/volkswagen-strengthens-horizon-robotics-tie-up-to-advance-self-driving-technology-in-china-9b4e72bd)**

WSJ • 1d ago

---

**[Ukrainian drones deliver robots directly into battle by sea and air](https://arstechnica.com/gadgets/2026/07/ukrainian-drones-deliver-robots-directly-into-battle-by-sea-and-air/)**

Ukraine's battlefield surge of robots now features airdrops and beach assaults.

Ars Technica • 1d ago

---

---

## YouTube Videos: "robotics"

**[America Doesn&#39;t Know What&#39;s Coming...China&#39;s Robot Factories](https://www.youtube.com/watch?v=3UEfc0XqJJ0)**

America Doesn't Know What's Coming | China's Robot Factories Chengdu is usually known for pandas, hotpot, teahouses, old ...

📺 Living in China

👁️ 28K • 👍 2K • 💬 108 • ⏱️ 12:28 • 1d ago

---

**[Robots Fight for $1M Prize in China&#39;s First Human Size Robot MMA League](https://www.youtube.com/watch?v=5IMU5or-VFo)**

The future of combat sports has arrived! Witness the high-stakes action as the Robot MMA Fight League officially kicks off in China ...

📺 Chris Wabs

👁️ 308K • 👍 7K • 💬 3K • ⏱️ 11:15 • 6d ago

---

**[America Is Now Building Humanoid AI Robot Soldiers for War](https://www.youtube.com/watch?v=Qm64Vm-lf80)**

An American robotics startup is preparing humanoid AI robots for war. Its Phantom machines have already been tested in Ukraine, ...

📺 AI Revolution

👁️ 25K • 👍 725 • 💬 105 • ⏱️ 13:15 • 4d ago

---

**[Real-Time Omni-Modal Interaction Driven Whole-Body Mobile Manipulation](https://www.youtube.com/watch?v=IiNbFPOUrz8)**

Unitree UnifoLM-OminiA-0.3 — a single model handling diverse home-care and wellness tasks, with omni-modal interactive ...

📺 Unitree Robotics

👁️ 1.9M • 👍 2K • 💬 376 • ⏱️ 2:15 • 3d ago

---

**[World&#39;s First Robot Fighting Tournament Is Insane](https://www.youtube.com/watch?v=aZ6o3SrzCWo)**

Humanoid robots have officially stepped into the ring. Watch the world's first robot fighting tournament and see how artificial ...

📺 DPCcars

👁️ 43K • 👍 478 • 💬 178 • ⏱️ 4:18 • 4d ago

---

**[China&#39;s New Robotic Bricklayer Built a Wall 6x Faster Than Humans—Construction Unions are Stunned](https://www.youtube.com/watch?v=phHhqt2df6I)**

China's latest robotic bricklayer is transforming the future of construction by building walls up to **6x faster than traditional human ...

📺 RedTech Insights

👁️ 20K • 👍 400 • 💬 33 • ⏱️ 19:31 • 2d ago

---

**[New Side Hustle: Training Robots (Is it Worth It?)](https://www.youtube.com/watch?v=yfZhpEupz5M)**

Humanoid robots have a big data problem. One solution? Pay humans to train them. I spent three weeks testing MicroAGI's Shift ...

📺 Joanna Stern

👁️ 87K • 👍 3K • 💬 269 • ⏱️ 12:02 • 6d ago

---

**[The UFC for Robots: China&#39;s Insane New Humanoid Fighting League](https://www.youtube.com/watch?v=0IqoJ-XxDtA)**

The UFC for Robots: China's Insane New Humanoid Fighting League The future of combat sports has officially arrived.

📺 Job Othoniel

👁️ 22K • 👍 144 • 💬 51 • ⏱️ 0:27 • 6d ago

---

**[Beni All-Terrain Following Camera Robot](https://www.youtube.com/watch?v=OdIy-kxjyuk)**

This is Beni and he is an all-terrain camera robot that can lock on to you and follow you while filming in 4K. Beni is more than just ...

📺 Air Photography

👁️ 83K • 👍 2K • 💬 217 • ⏱️ 7:15 • 6d ago

---

**[The Brothers Betting Their Robots Can Solve America&#39;s Welding Crisis | Path Robotics](https://www.youtube.com/watch?v=cI1XawnfEJE)**

America is running out of welders. By 2035, we'll lose 43% of America's welding workforce. @path_robotics is building robots to ...

📺 S3 | Science, Startups, & Stories

👁️ 35K • 👍 1K • 💬 93 • ⏱️ 14:37 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

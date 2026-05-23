---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-23T07:15:51.210644+00:00'
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

**Last Updated:** May 23, 2026 at 07:15 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Hypnotic Multi-Axis Robotics by KUKA](https://www.reddit.com/r/robotics/comments/1tkouh9/hypnotic_multiaxis_robotics_by_kuka/)**

14h ago

---

**[Hand taxonomy tests with my robotic hand & wrist](https://www.reddit.com/r/robotics/comments/1tkgco6/hand_taxonomy_tests_with_my_robotic_hand_wrist/)**

Evaluating some hand grip patterns following the https://www.eng.yale.edu/grablab/pubs/Feix_THMS2016.pdf paper. I didn't do all of them because I'm lazy and some of them are pretty similar. But I'm confident my hand can achieve all of them EXCEPT the disks grips and the inferior pinch since I lack independent intermediate phalanx actuation. I chose some random objects I could find lying around that fit each grip type to see how well the hand could actually hold real household items. Overall, I think it was quite successful, what do you think?

19h ago

---

**[Custom protocol, sub-40-ms Latency Teleoperation software](https://www.reddit.com/r/robotics/comments/1tkjuag/custom_protocol_sub40ms_latency_teleoperation/)**

Just came across this video of our low latency teleop software (Adamo in case anyone is interested) being used to teleoperate a robot from San Francisco to London. We built it using a custom protocol rather than webrtc so that it is a lot smoother, with less buffer than standard teleop software solutions. Please don't bash me for posting teleop content, I know some of you hate it haha, but it will get us to full autonomy dw!

17h ago

---

**[ROS News for the Week of May 18th, 2026](https://www.reddit.com/r/robotics/comments/1tkor8t/ros_news_for_the_week_of_may_18th_2026/)**

ROS News for the Week of May 18th, 2026    🎉 ROS 2 Lyrical Luth is here! Read the full release notes here, and snag your swag here!  You can read our full release announcement here.  Big thanks to all of our contributors, maintainers, testers, build farmers, OSRA members, and especially our ROS Boss @sloretz, and our infra lead @cottsay.  We’re going to take a long weekend break and get right back to it working on ROS 2 Makoa Mata-Mata! 🏄‍♀️             The ROS events calendar is...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-may-18th-2026/55022) • 14h ago

---

**[How to wake up this battery](https://www.reddit.com/r/robotics/comments/1tkvj9a/how_to_wake_up_this_battery/)**

10h ago

---

**[We made airsoft tank robots for our online video game](https://www.reddit.com/r/robotics/comments/1tk7tib/we_made_airsoft_tank_robots_for_our_online_video/)**

The real robot airsoft battles will be integrated with virtual battles seamlessly within the same matchmaking queue. We're using digital FPV equipment for the video link to a receiver pc, and then we send that to players over the internet via a custom UDP streaming protocol that also handles our normal game data. Virtual battles are standard video game servers. If you want to help with testing, we're looking for some people.

🔗 [youtube.com](https://www.youtube.com/watch?v=Nj5QkNiJvaU) • 1d ago

---

**[Building a runtime audit layer for mobile robots as EU AI Act logging / human oversight requirements approach](https://www.reddit.com/r/robotics/comments/1tkniag/building_a_runtime_audit_layer_for_mobile_robots/)**

Hey r/robotics, I’ve been working on an open-source middleware layer called runtime_integrity(formerly ros2_kinematic_guard). The problem I’m focusing on is runtime accountability for mobile robots. A robot can still be receiving valid commands while its physical execution has already diverged. Examples: wheel slip on wet or oily floors localization jumps stale or bursty velocity commands odometry mismatch command stream and physical motion going out of sync runtime_integrity sits between the autonomy stack and the base driver: /cmd_vel ↓ runtime_integrity ↓ /safe_cmd_vel It also watches odometry and emits structured runtime evidence when command and physical execution diverge. Example event: { "status": "RESYNCING", "dominantCause": "WHEEL_SLIP", "residual": 5.39, "guardAction": "BRAKE_AND_RESYNC", "interventionRequired": true, "complianceTags": ["human_oversight", "execution_integrity_audit"] } Why I think this matters now: As EU AI Act logging and human-oversight requirements approach for high-risk AI systems, robot vendors and integrators will need better runtime evidence than “something happened in a rosbag”. This package does not claim to make a robot compliant, and it does not replace safety PLCs, safety scanners, or hardware E-stops. The goal is narrower: planner commanded X robot physically behaved like Y runtime_integrity detected the mismatch a structured event explains why The repo includes a 5-minute ROS 2 demo using a lightweight mock AMR/AGV. No Gazebo, Isaac Sim, or real robot required. GitHub: https://github.com/ZC502/runtime_integrity.git I’d be interested in feedback from anyone working on AMRs/AGVs, safety logging, FMS/HMI systems, or post-incident debugging.

15h ago

---

**[Meet Xhand a dexterous hand for real world task](https://www.reddit.com/r/robotics/comments/1tjuztp/meet_xhand_a_dexterous_hand_for_real_world_task/)**

Meet XHand ✋ — precision, dexterity, and adaptability for real-world tasks. For building embodied AI solutions that bridge perception and action. XHand is just the beginning. #PhysicalAI #EmbodiedAI #Robotics #XHand #PNProbotics

1d ago

---

**[My color classification robot arm (repurpose tofu frying robot)](https://www.reddit.com/r/robotics/comments/1tjt0e0/my_color_classification_robot_arm_repurpose_tofu/)**

1d ago

---

**[Battling severe voltage sag on a 48V AMR under peak torque. How do you stop your servo drives from throttling?](https://www.reddit.com/r/robotics/comments/1tjw9hg/battling_severe_voltage_sag_on_a_48v_amr_under/)**

Hey everyone, looking for a sanity check on a heavy-payload AMR project (~700kg payload) running on a 48V LiFePO4 pack. Whenever the robot hits rough terrain or accelerates suddenly, the transient current draw causes our battery bus to sag hard, dipping down to 35V-36V for a few hundred milliseconds. Our current "industrial-grade" servo drives are losing their minds under this sag. We are hitting under-voltage faults that trigger random emergency stops, massive thermal spikes inside our sealed IP65 wheel hubs as the drives draw more current to compensate, and mushy velocity control right when we need tight torque response. We’ve debated adding a bulky buck-boost regulator just to keep the drive logic stable, but it kills our payload-to-weight ratio. For those building battery-powered platforms that survive high-torque transients, are you over-specifying the battery pack to stop the sag, or switching to drives with ultra-wide input voltage ranges? Also, how do you handle the thermal overhead in a sealed housing? Do GaN-based or ultra-high-efficiency drives actually solve the heat issue at the source? Trying to avoid a massive chassis redesign just to fit a bulkier cooling system. Any advice?

1d ago

---

---

## Google News: "robotics"

**[August Robotics lands $30M to automate precision construction with robots](https://siliconangle.com/2026/05/21/august-robotics-lands-30m-automate-precision-construction-robots/)**

August Robotics lands $30M to automate precision construction with robots - SiliconANGLE

SiliconANGLE • 1d ago

---

**[Will Robotics Have a ChatGPT Moment?](https://spectrum.ieee.org/robotics-ai-breakthrough)**

A single breakthrough AI moment in robotics may not be the answer

IEEE Spectrum • 2d ago

---

**[Are Humanoid Robots the End of Human Work?](https://nautil.us/are-humanoid-robots-the-end-of-human-work-1281110)**

Are Humanoid Robots the End of Human Work?: Here’s what the people making the robots think

Nautilus | Science • 1d ago

---

**[Watch Atlas Lift and Spin Like a Pro in This Week's Video Friday](https://spectrum.ieee.org/video-friday-humanoid-robot-learning)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 14h ago

---

**[China unveils first humanoid robot for household chores, ready as early as 2027](https://www.scmp.com/tech/article/3354371/commercial-humanoid-robots-china-may-soon-do-laundry-make-beds-care-elders)**

South China Morning Post • 1d ago

---

**[Jeff Bezos describes his $38B startup Prometheus for the first time: 'Nothing to do with robotics'](https://www.geekwire.com/2026/jeff-bezos-describes-his-38b-startup-prometheus-for-the-first-time-nothing-to-do-with-robotics/)**

In a CNBC interview, Jeff Bezos offered the most detailed public description yet of Project Prometheus, calling the secretive startup an "artificial general engineer" building next-generation design tools for physical objects.

GeekWire • 2d ago

---

**[Moto Pizza CEO launches robotics venture to bring automation in-house](https://www.bizjournals.com/seattle/news/2026/05/21/moto-pizza-ceo-lee-kindell-robotics-stadium-launch.html)**

The Business Journals • 1d ago

---

**[AI robotic beehives installed in Florida community claim 70% reduction in colony collapse threatening crops](https://www.foxnews.com/science/ai-robotic-beehives-installed-florida-community-claim-70-reduction-colony-collapse-threatening-crops)**

A Florida community deploys AI-powered robotic beehives to protect declining bee populations that pollinate roughly 75% of the crops Americans eat.

Fox News • 1d ago

---

**[Kawasaki Heavy, Nvidia plan Silicon Valley robotics center, Nikkei reports](https://finance.yahoo.com/sectors/technology/articles/kawasaki-heavy-nvidia-plan-silicon-160730316.html)**

May 21 () - Japan's Kawasaki Heavy Industries will partner with ‌Nvidia to develop solutions integrating ‌robotics with physical artificial intelligence, and will ​set up a joint development center in Silicon Valley, the Nikkei newspaper reported on Thursday. The collaboration will ‌initially focus ⁠on medical and mobility fields, with Nvidia's simulation technology ⁠to be applied to Kawasaki Heavy Industries' Corleo, a four-legged personal ​mobility robot ​under development, ​Nikkei added.

Yahoo Finance • 1d ago

---

**[Unlocking soft robotics control with AI's cousin: Reservoir computing](https://techxplore.com/news/2026-05-soft-robotics-ai-cousin-reservoir.html)**

Tech Xplore • 16h ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 10K • 👍 164 • 💬 77 • ⏱️ 5:15 • 12h ago

---

**[Is There A Robot Revolution Happening? What’s Going On?](https://www.youtube.com/watch?v=w1VKIIxk0Vc)**

Robots are getting REALLY sophisticated…so why don't we all have our own personal robot assistant yet? Watch here to find out ...

📺 NBC News

👁️ 1K • 👍 22 • ⏱️ 2:37 • 1d ago

---

**[Introducing Tektite Motor Snap! #ftc #robotics](https://www.youtube.com/watch?v=goUyWkmqYC4)**

📺 Tektite

👁️ 906 • 👍 14 • ⏱️ 0:30 • 2h ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 119K • 👍 3K • 💬 95 • ⏱️ 22:41 • 3d ago

---

**[How Nature Solved Robotics](https://www.youtube.com/watch?v=S67z2aekBrI)**

This video is both a story of my adventure with AI robotics and the fascinating lessons I learned along the way. Try Mammouth AI ...

📺 Art of the Problem

👁️ 17K • 👍 2K • 💬 128 • ⏱️ 27:25 • 16h ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 32 • 💬 5 • ⏱️ 0:07 • 1d ago

---

**[These New REALISTIC FEMALE ROBOTS Are Crossing the Line – Experts TERRIFIED](https://www.youtube.com/watch?v=OTEu_9KyfPE)**

The robots in this video look real. Move real. Talk real. And that's exactly what's making some of the world's top experts seriously ...

📺 AI Exposed

👁️ 145K • 👍 1K • 💬 76 • ⏱️ 12:25 • 6d ago

---

**[Do humanoid robots pose national security risk?](https://www.youtube.com/watch?v=sNhskSj2mm0)**

ABC News investigates the rise of humanoid robots manufactured in China and why experts say they pose a risk to U.S. national ...

📺 Good Morning America

👁️ 1K • 👍 14 • 💬 1 • ⏱️ 3:22 • 1d ago

---

**[Apple Just Started Selling $1,000 AI Home Robots in All Stores](https://www.youtube.com/watch?v=jDmOBHB-7Ik)**

Apple's new AI home robots are being described as a major step toward bringing advanced robotics into everyday households on ...

📺 Carros Show

👁️ 7K • 👍 260 • 💬 40 • ⏱️ 23:14 • 2d ago

---

**[Elon Musk On The Next Five Years Of AI And Robots](https://www.youtube.com/watch?v=3PTCFgmUVaE)**

From the Forbes Innovator 250 Celebration at Hotel Nia—Silicon Valley, Elon Musk shares why expects a billion humanoid robots ...

📺 Forbes

👁️ 21K • 👍 323 • 💬 51 • ⏱️ 0:53 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

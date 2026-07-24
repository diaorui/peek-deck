---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-24T17:05:06.517747+00:00'
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

**Last Updated:** July 24, 2026 at 17:05 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Unitree “Super Athlete" AS2-W (wheeled-leg variant of the AS2)](https://www.reddit.com/r/robotics/comments/1v582o5/unitree_super_athlete_as2w_wheeledleg_variant_of/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2080549171661295907 - Weight: ~25 kg with battery. - Speed: Over 6 m/s (higher than the pure-legged As2). - Payload: Continuous ~16 kg; higher static capacity. - Endurance: Unloaded >3 hours / 30+ km; loaded (>16 kg) >2 hours / >16 km. Same 648 Wh (15,000 mAh) battery class as the As2. - Mobility: Up to ~80 cm obstacles, 45° slopes, 30 cm stairs; strong on gravel, rocky, and uneven outdoor terrain. https://www.unitree.com/As2-W

6h ago

---

**[Embodied AI is getting scary cheap. We just got our sub-$1,000 open-source robot (AlohaMini2) to do autonomous mobile manipulation trained on a consumer 8GB GPU.](https://www.reddit.com/r/robotics/comments/1v535b3/embodied_ai_is_getting_scary_cheap_we_just_got/)**

Hey everyone, A while back, I posted here asking for advice on my $149 metal cycloidal actuator project. A lot of folks asked me why I was so obsessed with pushing the hardware BOM cost down so aggressively. Well, this video is exactly why. My co-founder Yiteng and I just released AlohaMini2. To our knowledge, it's the first sub-$1,000 self-build BOM robot capable of end-to-end, long-horizon autonomous tasks (like this grocery manipulation). Here is the technical takeaway that I think will interest this community: The Compute Barrier is Gone: This wasn't trained on a server farm. The AM-ACT policy was trained and deployed entirely on a standard 8GB consumer GPU. Data Efficiency: It only took 50 human demonstration episodes to reach a 50% end-to-end success rate on this specific long-horizon task. We are open-sourcing the entire repo (hardware files & codebase) because we want to prove that you don't need a multi-million-dollar lab to play with cutting-edge Embodied AI anymore. The Real Bottleneck Now? Hardware Reliability. While the software/policy side is moving at lightspeed, keeping a $1,000 robot mechanically alive during 24/7 RL training is a nightmare. 3D printed gears strip, cheap servos overheat. That’s exactly what drove me to start designing metal actuators in the first place. Repo link for anyone who wants to build one or dive into the code:https://github.com/liyiteng/AlohaMini I’m curious—if the software barrier is this low now, what tasks would you guys train a cheap $1k robot to do at home?

10h ago

---

**[New AMD Robotics SoC: X100 - 128GB Unified Memory](https://www.reddit.com/r/robotics/comments/1v57zsa/new_amd_robotics_soc_x100_128gb_unified_memory/)**

Saw on blog by Steve Macenski: https://opennav.org/news/opennav-robotics-workload-benchmark/ running extended ROS 2 workloads. Pretty cool HW-wise, especially with recent Jetson 50-100% price increase. Hopefully AMD won't price it same as new Thor price 👀 Also vote if you can what HW you use to run ROS (if you use ROS)

🔗 [AMD](https://www.amd.com/en/products/system-on-modules/kria/ai.html) • 6h ago

---

**[Autonomous RC car loses gps connection when starts the route.](https://www.reddit.com/r/robotics/comments/1v55vrx/autonomous_rc_car_loses_gps_connection_when/)**

Hi everyone I need your help! I don't know if this is the right place for this post, but I'll give it a shot. My thesis is to write a manual for this particular rover and also make a "test drive" with it. I drew the plan in mission planner, changed the necessary parameters and det the rc to auto. Every time it starts with here 3 being solid green and then stops and the colours are flashing yellow and red which I think it means that it lost connection. Then it gets solid green again but i have to switch it back to manual and then auto in order to start again to move and then suddenly stop. I want to clarify that it doesn't stop each tme after a specific amount of time, but it's random. I tried one suggestion which was to raise the here 3 up to 15cm (in the photo is 14.5cm) but once again it didn't work. I should note that lidar should have worked also (by work i mean it should have meade the rc to avoid obstacles) but it doesn't and i'm curious if this is causing the problem. Anyway don't hesitate to ask every detail you want in the comments, I will appreciate all the help you can give me!

8h ago

---

**[I built a laser-cut rack & pinion for a NEMA 17 stepper](https://www.reddit.com/r/robotics/comments/1v4l6c3/i_built_a_lasercut_rack_pinion_for_a_nema_17/)**

Design files (DXF) and Arduino code: https://drive.google.com/drive/folders/13WhHXtmIfWlrlRav29l_HFwwOCRubMLY?usp=sharing

23h ago

---

**[The second attempt tells more than the success clip](https://www.reddit.com/r/robotics/comments/1v58r1r/the_second_attempt_tells_more_than_the_success/)**

In a robot demo, I usually watch what happens right after the first miss. Does the robot look again and change its approach, repeat the same motion, or wait for someone off camera to reset the object? For a LingBot-VLA 2.0 evaluation, keep the camera running through the failed grasp and the retry. The useful details are the object's new pose, whether the policy receives a fresh observation, how the next approach point changes, and when a human takes over. A short uncut sequence would answer more than several successful clips. I am less sure how controlled the failure should be. A fixed perturbation makes comparisons easier, but it can also turn the demo into a lab exercise that misses messy real failures. How do people here test recovery and still keep the setup repeatable?

5h ago

---

**[Playto Labs is a scam](https://www.reddit.com/r/robotics/comments/1v4errx/playto_labs_is_a_scam/)**

Do not sign up with this company unless you want to be scammed. I signed up for their most expensive program, but was not satisfied and requested a refund. It was much less than I thought, but it still wasn't a small amount (a little under $1000). The teachers were nice, but my son was not learning much in terms of robotics. That's when things went south. After being promised my refund, they refused to actually refund me my money, and then ghosted me. This after I spent an additional $100 to ship the robotics kit back to them in India. I tracked it all the way there, just to see it refused by sender. This is what they do. I tried to dispute this with my credit card, but I just found out it was denied because Playto charges through a third party name (Raz*Skyfi Education). They know this, and use it as a loophole to not refund you your credit. Please stay away.

1d ago

---

**[The 20-second demo that broke my teammate (and what it taught me about debugging)](https://www.reddit.com/r/robotics/comments/1v54wj8/the_20second_demo_that_broke_my_teammate_and_what/)**

Last week, our marketing team asked me to help shoot a 20-second demo video. Just have our 6-axis arm (Alicia-M) pick up a wooden block, drop it into a small bin, then grab the bin and tip the block out. Twenty seconds. Simple. It was not simple. Here's what I learned watching a non-engineer try to teach this arm the sequence. The first step — pick up the block and drop it in the bin — was almost easy. The second step — grab the bin and tip the block out — broke her brain for two days. Two failure modes I watched her hit, over and over: I can't find the right angle to tip it out." She'd pick up the bin, then spend ten minutes trying different left/right tilts. Nothing worked. The block would either stay stuck in the bin or fly off in a random direction. The cause wasn't the angle she was choosing — it was that she was trying to fix the bin's orientation when the real problem was the block's exit path. The block leaves the bin at an angle that's the sum of the bin's tilt, the bin's rotation around vertical, and gravity. She was tuning one variable; the block was moving in three. The arm missed completely." She'd press go, the gripper would close on empty air, and she'd say "the arm missed it." But the arm didn't miss. The end effector was exactly where the program told it to be. She was watching the block from a camera angle that offset her mental "where" by 2-3 cm. The fix wasn't the arm. The fix was moving the camera to a top-down view, so her mental model matched the arm's coordinate frame. The lesson I didn't expect: I thought I was going to teach her. I came out learning to debug faster. Engineers debug with hypotheses: "the angle is off, let me check the code." Non-engineers debug with action: "let me try the other side, let me close harder." Her action-first approach was noisier — five parameter changes in the time it takes me to formulate one hypothesis — but after I asked her to ask "what did I just see?" before "what should I change?", the pattern emerged. By attempt 20, she could predict the failure before it happened. The third time the bin tilted the wrong way, she said "wait — I'm not picking the angle, I'm picking the trajectory the block will follow." And then she solved it in two tries. The rule I'm keeping: after every failure, describe what you saw. Then diagnose. For those who've taught a non-engineer to use a robot arm: what was the moment your student had the "I can read the failure now" breakthrough? Was it a "the angle is wrong" moment, or a "I'm chasing the wrong variable" moment?

9h ago

---

**[Caught these two little robots putting on a dance performance](https://www.reddit.com/r/robotics/comments/1v49m9t/caught_these_two_little_robots_putting_on_a_dance/)**

Two cute little robots dancing to the music and enjoying their moment in the spotlight. Their synchronized movements, tiny gestures, and playful rhythm were surprisingly delightful to watch. I came across this little performance during my day and couldn’t resist recording it.

1d ago

---

**[Built this 6DOF using aluminum angles and acrylic plates.](https://www.reddit.com/r/robotics/comments/1v45ity/built_this_6dof_using_aluminum_angles_and_acrylic/)**

Built this 6dof with parts bought from local hardware store. Lot of loose parts now, needs fine tune or redo. Plan is to create mobile arm. Waiting for wheels and step motor. Controlled by raspberry pi.

1d ago

---

---

## Google News: "robotics"

**[The Robots Cometh](https://time.com/article/2026/07/23/unitree-china-human-robotics/)**

The humanoid revolution is coming—and the Chinese firm Unitree is leading the charge.

Time Magazine • 1d ago

---

**[This Silicon Valley city is quietly becoming Robot Row. Here's who's clanking around.](https://www.businessinsider.com/robot-row-humanoid-hub-location-fremont-silicon-valley-agility-tesla-2026-7)**

A growing number of robotics companies now have a footprint in Fremont, which sits at the intersection of Silicon Valley talent and manufacturing.

Business Insider • 8h ago

---

**[Eric Trump-backed Foundation partners with AMD to develop humanoid robots](https://www.reuters.com/business/eric-trump-backed-foundation-partners-with-amd-develop-humanoid-robots-2026-07-23/)**

Reuters • 22h ago

---

**[US eyes ban on Chinese humanoid robots as US-China tech rivalry intensifies](https://www.scmp.com/tech/policy/article/3361622/us-eyes-ban-chinese-humanoid-robots-us-china-tech-rivalry-intensifies)**

South China Morning Post • 1d ago

---

**[Tesla's push into AI and robotics is proving costly](https://www.axios.com/2026/07/22/tesla-earnings-ai-robotics-spending)**

Axios • 1d ago

---

**[For The First Time Ever, Humanoid Robots Perform Surgery on Live Animals](https://www.sciencealert.com/world-first-humanoid-robots-perform-surgery-on-live-animals-this-could-prove-useful-in-space)**

For the first time ever, humanoid robots operated by surgeons have successfully performed laparoscopic gallbladder removal in pigs.

ScienceAlert • 2d ago

---

**[U.S. Robotics Leadership Is Not Guaranteed](https://www.piratewires.com/p/us-robotics-leadership-is-not-guaranteed)**

Pirate Wires • 23h ago

---

**[China's Unitree says 'GPT moment' for robots remains years away](https://asia.nikkei.com/spotlight/nikkei-forum/global-digital-summit/global-digital-summit-2026/china-s-unitree-says-gpt-moment-for-robots-remains-years-away)**

Humanoid leader to put almost half of IPO proceeds into embodied AI research

Nikkei Asia • 2d ago

---

**[Robots can now learn high-dexterity factory tasks from video with minimal training](https://interestingengineering.com/ai-robotics/robots-can-now-learn-high-dexterity-factory-tasks-from-video-with-minimal-training)**

Mimic Robotics unveils FLUX-mimic, enabling industrial robots to learn complex tasks from video with far less training data.

Interesting Engineering • 1h ago

---

**[Robotics Startup Genesis in Talks to Raise at $3 Billion Valuation](https://www.bloomberg.com/news/articles/2026-07-23/robotics-startup-genesis-in-talks-to-raise-about-500-million)**

Bloomberg.com • 9h ago

---

---

## YouTube Videos: "robotics"

**[Real-Time Omni-Modal Interaction Driven Whole-Body Mobile Manipulation](https://www.youtube.com/watch?v=IiNbFPOUrz8)**

Unitree UnifoLM-OminiA-0.3 — a single model handling diverse home-care and wellness tasks, with omni-modal interactive ...

📺 Unitree Robotics

👁️ 2.5M • 👍 2K • 💬 406 • ⏱️ 2:15 • 4d ago

---

**[World&#39;s First Robot Fighting Tournament Is Insane](https://www.youtube.com/watch?v=aZ6o3SrzCWo)**

Humanoid robots have officially stepped into the ring. Watch the world's first robot fighting tournament and see how artificial ...

📺 DPCcars

👁️ 47K • 👍 500 • 💬 188 • ⏱️ 4:18 • 6d ago

---

**[America Is Now Building Humanoid AI Robot Soldiers for War](https://www.youtube.com/watch?v=Qm64Vm-lf80)**

An American robotics startup is preparing humanoid AI robots for war. Its Phantom machines have already been tested in Ukraine, ...

📺 AI Revolution

👁️ 27K • 👍 748 • 💬 105 • ⏱️ 13:15 • 5d ago

---

**[America Doesn&#39;t Know What&#39;s Coming...China&#39;s Robot Factories](https://www.youtube.com/watch?v=3UEfc0XqJJ0)**

America Doesn't Know What's Coming | China's Robot Factories Chengdu is usually known for pandas, hotpot, teahouses, old ...

📺 Living in China

👁️ 49K • 👍 2K • 💬 155 • ⏱️ 12:28 • 3d ago

---

**[China&#39;s New Robotic Bricklayer Built a Wall 6x Faster Than Humans—Construction Unions are Stunned](https://www.youtube.com/watch?v=phHhqt2df6I)**

China's latest robotic bricklayer is transforming the future of construction by building walls up to **6x faster than traditional human ...

📺 RedTech Insights

👁️ 22K • 👍 432 • 💬 35 • ⏱️ 19:31 • 3d ago

---

**[The Brothers Betting Their Robots Can Solve America&#39;s Welding Crisis | Path Robotics](https://www.youtube.com/watch?v=cI1XawnfEJE)**

America is running out of welders. By 2035, we'll lose 43% of America's welding workforce. @path_robotics is building robots to ...

📺 S3 | Science, Startups, & Stories

👁️ 37K • 👍 1K • 💬 96 • ⏱️ 14:37 • 6d ago

---

**[A Chinese Robot Just Decapitated Another Robot In Public. Nobody Asked What Comes Next](https://www.youtube.com/watch?v=rUjlFRok3qk)**

Everyone is asking if killer robots are coming. Wrong question. One already knocked another robot's head clean off, on camera ...

📺 Ambrose In China

👁️ 568K • 👍 20K • 💬 4K • ⏱️ 2:25 • 4d ago

---

**[Losing a Head Doesn&#39;t Stop This Robot From Battling Another in the Ring](https://www.youtube.com/watch?v=FEcPelBd9t0)**

Humanoid robots fought inside a cage at a tournament in China. The two exchange a fury of blows before the black robot loses it's ...

📺 New York Post

👁️ 35K • 👍 759 • 💬 342 • ⏱️ 2:02 • 2d ago

---

**[NERF THIS IMMEDIATELY! War Robots Most Broken NONSENSE Ever!](https://www.youtube.com/watch?v=edTHUrJHedA)**

War Robots Gameplay: VULCAN with Urhag Sniper weapons NERF!!! My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 13K • 👍 535 • 💬 185 • ⏱️ 14:51 • 1d ago

---

**[What’s Wrong with Japanese Robotics and AI?](https://www.youtube.com/watch?v=gkzxgJH2Wzc)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: https://www.instagram.com/pro_robots Did Japan Lose the ...

📺 PRO ROBOTS

👁️ 10K • 👍 314 • 💬 36 • ⏱️ 15:59 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

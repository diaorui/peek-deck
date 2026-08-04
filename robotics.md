---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-04T10:10:18.752033+00:00'
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

**Last Updated:** August 04, 2026 at 10:10 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Using ai model vs explicit programming](https://www.reddit.com/r/robotics/comments/1ve6l20/using_ai_model_vs_explicit_programming/)**

On the previous video, people commented that the objects are placed on jigs in known positions, which implies that the movements could be programmed. This is fair, although the object can still bounce away randomly when it falls. So I tested different cases here. A benefit of using an advanced model is that it can handle small variations that can happen in real life as a free bonus, just by recognizing patterns within small amount of examples.

1d ago

---

**[A closer look at the animation editor for my 5-DOF robotic lamp](https://www.reddit.com/r/robotics/comments/1vdn1xm/a_closer_look_at_the_animation_editor_for_my_5dof/)**

I’ve briefly shown earlier versions of the editor in my previous posts, but this video gives a closer look at the complete workflow. This is Watti, my five-axis robotic lamp, and Watti Studio, the browser-based editor I built for creating its movements and lighting scenes. I’ve also refined the enclosure since my previous posts. It now looks cleaner and is much closer to what I imagine as the final design. In the video, I create a scene on the timeline, preview it on the virtual robot, and then run the same scene on the physical Watti. During playback, the real robot appears below the simulation so their movements can be compared directly. Motion and lighting share the same 25 Hz timeline. The complete scene is uploaded to a Raspberry Pi 5 and played locally through ROS 2, so the browser doesn’t need to remain connected during playback. I’ve also made the project repository public: https://github.com/Nikolay-Tyulkin/Watti There’s no source code yet, so it’s currently a public project preview rather than an open-source release. The repository already contains more extensive information about the architecture, hardware, current capabilities, and roadmap. I’ll also use it as a public development tracker, so anyone interested can follow the project’s progress. I’d be interested to hear what you think about the workflow and what features you would find useful in an editor like this.

1d ago

---

**[Built a $23 leader arm for teleoperation](https://www.reddit.com/r/robotics/comments/1vedrhr/built_a_23_leader_arm_for_teleoperation/)**

Please don't mind the cables and the messy table. I am new to the VLA and robot arm side of robotics and was primarily working on the legged locomotion. I thought of building the lerobot kit to work on vla. I felt the price was a bit steep for me so decided to build my own leader arm with encoders instead of motors. Parts and price list : 6 x AS5600 encoder - 186rs x 6 = 1,116rs (~11.7 usd) 6 x 608 bearing - 30rs x 6 = 180rs (~1.9 usd) 1 x CJMCU TCA9548A I2C 8 Channel- 59rs (~0.6 usd) 1 x esp32 - 550rs (~5.8 usd) wires - 200rs (~2.1 usd) M3x10mm screws (40pcs) - 128rs (~1.3 usd) Total cost - 2,233 rs. (~ 23.5 usd) (excluding 3d printed parts cost) for context, price of one ST3215 (used in the lerobot kit) in india is around 2,200rs (~23 USD) Haven't put it on github yet but will do it in a few days after some improvements and cleanups, and edit this post with the link.

20h ago

---

**[Why are there holes in cycloidal disk?](https://www.reddit.com/r/robotics/comments/1vdyw8y/why_are_there_holes_in_cycloidal_disk/)**

https://preview.redd.it/a6uwux1o52hh1.png?width=1324&format=png&auto=webp&s=662bcc147f409a1f919860d34370c79e470ecc3b I don't understand why there are holes in cycloidal driver and it's connected to "output flange"? I don't understand how the transmission is carried out to whatever you want it to move. Also, one more thing why is the drive shaft eccentrically placed and why is there a bearing around the driveshaft. This bearing im referring to, what does that do?

1d ago

---

**[Full run and a segment of a task. 100% from 16 examples.](https://www.reddit.com/r/robotics/comments/1vcyslb/full_run_and_a_segment_of_a_task_100_from_16/)**

To play with continuous learning, your base model needs to be data-efficient and stable, which we tested here. Because all irrelevant fluctuations can compound over time.

2d ago

---

**[Project PAL](https://www.reddit.com/r/robotics/comments/1vdpe4u/project_pal/)**

this is my second version of this companion i call PAL. his face is using a I2C oled display, the servos are generic SG90's he comunicates via BLE with the phone. the app was created with MIT app inventor. what are your thoughts on this project. im working on the jitteriness, the bottom servo is curently to weak so i'm adding asupport on the other side. the repo is on github (repo name : PAL-cube)

1d ago

---

**[How do you check when a joint hits the ground?](https://www.reddit.com/r/robotics/comments/1vdpq1x/how_do_you_check_when_a_joint_hits_the_ground/)**

1d ago

---

**[Structuring a Nav2 social-navigation stack for Unitree G1 — same code for sim and hardware?](https://www.reddit.com/r/robotics/comments/1vdali3/structuring_a_nav2_socialnavigation_stack_for/)**

Hi all, I'm a PhD student working on socially-aware navigation. I've built a custom Nav2 costmap layer that inflates cost around pedestrians (proxemic zones) so the planner routes around people. It works well on a TurtleBot3 in Gazebo. My target platform is the Unitree G1 humanoid, and I have hardware access confirmed, but I also need a standalone simulation demo (in case hardware time slips) — ideally with the same navigation code running in both. **My understanding of the architecture**: Everything above /cmd\_vel (Nav2 + my social layer) should be identical for sim and hardware. It consumes /scan, /odom, /tf and outputs /cmd\_vel. On the real G1, the built-in locomotion controller turns velocity commands into walking, and the onboard Livox Mid-360 provides the scan — so the "adapter" below /cmd\_vel is mostly provided by Unitree. In simulation, I have to substitute both: something to make the G1 walk from /cmd\_vel, and a simulated lidar/odom/TF for Nav2. **My questions:** For the sim side, what's the recommended setup for a G1 that (a) walks/moves from /cmd\_vel and (b) publishes a lidar scan + odom + TF that Nav2 can use? Is Gazebo (with a G1 model + simulated Livox) the right choice for a navigation demo, or are people using MuJoCo / Isaac for this? I've gotten an RL locomotion policy walking in unitree\_mujoco, but MuJoCo seems weak on the Nav2/sensor side. On hardware, is the high-level locomotion (velocity) API the right interface for Nav2 to drive, and does it cleanly accept a continuous /cmd\_vel stream from the controller server? Has anyone run Nav2 on a G1 (sim or real) and can share how they structured the sensor + locomotion interface so the navigation stack stays platform-agnostic? Any pointers, example repos, or "here's what I'd do differently" advice much appreciated. Happy to share my social costmap layer back once it's cleaned up. Thanks!

2d ago

---

**[What do u use for visual context?](https://www.reddit.com/r/robotics/comments/1vdd5bl/what_do_u_use_for_visual_context/)**

Hi alll, i was wondering what people use for visual context for ur robot, i have a project for visual context but for security cameras, and i thought maybe it could fit into robotics

2d ago

---

**[How will ROBOTICS change every day life for a human and society within the next 10 years?](https://www.reddit.com/r/robotics/comments/1vcy3ki/how_will_robotics_change_every_day_life_for_a/)**

With various companies developing humanoid robots and advancements in robots in general, will there be some huge change in society the same way the internet boom changed humans?

2d ago

---

---

## Google News: "robotics"

**[German Robotics Startup Agile Robots Set to Double Revenue This Year](https://www.wsj.com/tech/ai/german-robotics-startup-agile-robots-set-to-double-revenue-this-year-6d0a27dc)**

WSJ • 1d ago

---

**[Walden’s Wheeled Humanoids Aim to Redefine Factory Floor Work](https://spectrum.ieee.org/humanoid-robots-walden-robotics-toyota)**

The company aims to create physical AI tools for human workers

IEEE Spectrum • 2d ago

---

**[Trump’s AI protectionism has come for robotics](https://www.technologyreview.com/2026/08/03/1141056/trumps-ai-protectionism-has-come-for-robotics/)**

The FTC has banned foreign-made humanoids, making a fragile, nascent sector  part of America’s AI industrial policy.

technologyreview.com • 15h ago

---

**[U.S. Bans Imports Of AI Humanoid Robots To Protect Americans From A Massive Trojan Horse Invasion](https://www.forbes.com/sites/lanceeliot/2026/08/04/us-bans-imports-of-ai-humanoid-robots-to-protect-americans-from-a-massive-trojan-horse-invasion/)**

FCC has banned foreign-produced AI humanoid robots from being imported to the U.S. for various vital reasons. Here's the backstory. An AI Insider analysis and scoop.

Forbes • 2h ago

---

**[Family Offices Sidestep AI Fears in Deal Spree for Robotics Bets](https://www.bloomberg.com/news/articles/2026-08-04/family-offices-sidestep-ai-fears-in-deal-spree-for-robotics-bets)**

bloomberg.com • 27m ago

---

**[Americans in their 70s and 80s are among the first to bring AI robots into their homes](https://fortune.com/2026/08/03/gen-z-elliq-intuition-robotics-ai-companion-robot-older-adults/)**

ElliQ’s device has been commercially available since 2022.

Fortune • 19h ago

---

**[Neither human nor robot dog: meet the machine set to police our streets](https://www.futura-sciences.com/en/neither-human-nor-robot-dog-meet-the-machine-set-to-police-our-streets_36761/)**

Founded in Tallinn in 2025 by Sander Sebastian Agur and Arno Kütt, formerly of parcel delivery robotics company Cleveron, Rollo Robotics developed the platform, named 1ROLLO. Specifically, the team set out to address the long-standing engineering challenge of maintaining single-wheel stability during movement, turning, and stopping. Gyroscopic stabilization and technical...

Futura, le média qui explore le monde • 16h ago

---

**[New, free robotics program starting at Fauntleroy YMCA](https://westseattleblog.com/2026/08/new-free-robotics-program-starting-at-fauntleroy-ymca/)**

Registration is open for a new free robotics program for 9- to 15-year-olds, offered by the West Seattle YMCA and NUCOR (both WSB sponsors) - free, with limited space. Here's the announcement sent to us to share with you:
The West Seattle YMCA and NUCOR are excited to partner and provide a STEM Robotics Program for youth in our community. Using ...

West Seattle Blog... • 18h ago

---

**[Serve Robotics to Report Q2 Earnings: What to Expect From the Stock?](https://www.zacks.com/stock/news/2966675/serve-robotics-to-report-q2-earnings-what-to-expect-from-the-stock)**

Zacks Investment Research • 20h ago

---

**[US bans foreign-made robots, China threatens to retaliate](https://www.morningbrew.com/stories/us-bans-foreign-made-robots-china-retaliate)**

They won't come after the Roomba you already own, but it might make it harder to get a new one.

Morning Brew • 3d ago

---

---

## YouTube Videos: "robotics"

**[Gemini Robotics 2 brings whole body intelligence to robots](https://www.youtube.com/watch?v=4lSQnrMC6nY)**

For decades, we've dreamed of robots that can seamlessly step into our world and lend a hand. Now, that vision takes a ...

📺 Google DeepMind

👁️ 229K • 👍 6K • 💬 521 • ⏱️ 3:00 • 4d ago

---

**[FCC chair Carr defends new ban on foreign-made humanoid robots](https://www.youtube.com/watch?v=kTeCO57t9cs)**

The Trump administration will ban foreign-made humanoid robots in the U.S. as China seeks to dominate the emerging high-tech ...

📺 NBC News

👁️ 73K • 👍 390 • 💬 534 • ⏱️ 6:04 • 5d ago

---

**[J&amp;J’s Billion-Dollar Robot Bet](https://www.youtube.com/watch?v=rx0FFvpF8pI)**

After spending years and hundreds of millions of dollars, Johnson and Johnson has won FDA approval for its new surgical robot ...

📺 Bloomberg Television

👁️ 42K • 👍 720 • 💬 73 • ⏱️ 11:26 • 1d ago

---

**[The U.S. Just Banned Chinese Humanoid Robots… I Own Two](https://www.youtube.com/watch?v=wNaohV4eY0A)**

The U.S. just banned Chinese humanoid robots… or did it? I own the Unitree G1 and Agibot X2, so here's what the new U.S. ...

📺 KhanFlicks

👁️ 2K • 💬 33 • ⏱️ 3:45 • 5d ago

---

**[Robot version of Michael Jackson #robot #robotics #humanoid](https://www.youtube.com/watch?v=BEV65B5-l_o)**

📺 Vy Chuong - robot 

👁️ 1K • 👍 13 • ⏱️ 0:48 • 6h ago

---

**[The Chinese robot army transforming the UK&#39;s retail industry | BBC News](https://www.youtube.com/watch?v=H7IqXkQUqxk)**

Every time you click "buy" on an online order, the chances are that your purchase starts getting processed within minutes.

📺 BBC News

👁️ 170K • 👍 1K • 💬 602 • ⏱️ 3:14 • 1d ago

---

**[The $1/Hour Robot Is Coming: Four Industry Leaders Explain What’s Next](https://www.youtube.com/watch?v=TqNiSTeNtb0)**

(0:00) Intro: Humanoids, Robots, & AI+ (0:57) ANYbotics' Dr. Péter Fankhauser: Why ANYbotics Bet the Company on Four-Legged ...

📺 All-In Podcast

👁️ 113K • 👍 2K • 💬 301 • ⏱️ 1:08:35 • 5d ago

---

**[AGIBOT A3 Revealed Future Humanoid Robot Technology Unboxing](https://www.youtube.com/watch?v=mv4eXwJ05So)**

The new AGIBOT A3 humanoid robot has officially been revealed, showcasing advanced artificial intelligence, impressive mobility ...

📺 DPCcars

👁️ 5K • 👍 39 • 💬 11 • ⏱️ 2:46 • 6d ago

---

**[Fei-Fei Li is Solving the Hardest Problem in Robotics | World Labs with a16z](https://www.youtube.com/watch?v=-tabaM5l3s0)**

Last week, World Labs announced its acquisition of SceniX, bringing together two teams working on one of AI's biggest unsolved ...

📺 a16z

👁️ 28K • 💬 40 • ⏱️ 42:21 • 6d ago

---

**[Testing Our New Robotic Hand](https://www.youtube.com/watch?v=Nhr7ZnFZYkA)**

Special thanks to Andrea, Jason, and the whole engineering team that made this video possible. Want to join an awesome team ...

📺 Foundation Robotics

👁️ 18K • 👍 545 • 💬 29 • ⏱️ 5:33 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

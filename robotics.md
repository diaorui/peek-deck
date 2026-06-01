---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-01T05:25:32.854603+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** June 01, 2026 at 05:25 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Connected a Reachy Mini to GPT Realtime 2](https://www.reddit.com/r/robotics/comments/1tsz5vl/connected_a_reachy_mini_to_gpt_realtime_2/)**

Found a Reachy Mini lying around the office and spent an hour giving it a real-time voice brain via GPT Realtime 2. The model basically becomes Reachy. It hears through its mic, sees through its camera, talks through its speaker, and calls motion tools to physically react while it talks. For anyone who wants to do this, here's the repo: https://github.com/opper-ai/reachy-voice-realtime Note: most of the delay is just our turn-detection silence window (set long because we were in a noisy room), which is tunable in the repo, the model itself is built for low-latency speech-to-speech. Key things: Web UI to watch the camera feed, transcript, and tool calls live. 19 motion and perception tools the model calls mid-conversation (emotes, head/antenna/body movement, camera, sound direction). Mimics you, wave and it waves back, nod and it nods, tilt your head and it tilts. Runs on GPT Realtime 2, routed through Opper. Setup's in the README (Python 3.12+), MIT licensed.

13h ago

---

**[6 servos of 12 working](https://www.reddit.com/r/robotics/comments/1tthtf5/6_servos_of_12_working/)**

38m ago

---

**[How often do your designs fail ?](https://www.reddit.com/r/robotics/comments/1tszjfm/how_often_do_your_designs_fail/)**

Hi everyone, I recently had a comment said to me in which someone asked “do you even know if your robots will work?” And I said “yes” to which they scoffed. For context - I’ve been working with cable driven robots (continuum) which is very difficult in comparison to rigid serial link systems from my experience, and it’s taking a lot of trial and error on each design. I’ll have a really good outcome from one robot (shorter in length, good shaping) , and then go to design the next one to be a bit longer and have a completely different outcome (robot has self weight issues, buckling, etc) I’m primarily self taught with these systems and it’s quite a niche field in robotics - yet I’m just curious as to what everyone else’s experience is when designing and building real things that move. I may be taking this comment to heart but it’s really stuck with me in a negative way. I’d love to hear anyone else’s experiences and what they do to keep going.

13h ago

---

**[Fully 3D Printed WALL-E with Functional Tracks](https://www.reddit.com/r/robotics/comments/1ts3y40/fully_3d_printed_walle_with_functional_tracks/)**

I designed and 3D printed this fully articulated WALL-E in Autodesk Fusion. It features functional rolling tracks, a fully poseable body, an opening storage compartment, and several print-in-place components. The project involved multiple design iterations to optimize the track mechanism, joint tolerances, and printability for consumer FDM printers. The 3D printing files are available for free on my MakerWorld profile: https://makerworld.com/models/2865166?appSharePlatform=copy This is also the starting point for my next robotics project, where I plan to integrate DC motors, electronics, and a control system to create a fully mobile robotic platform.

1d ago

---

**[Get hands dirty on VLA+Immitation + RL](https://www.reddit.com/r/robotics/comments/1tt40u6/get_hands_dirty_on_vlaimmitation_rl/)**

10h ago

---

**[RA B601-DM ROS2 Monitoring Overlay - Open Source](https://www.reddit.com/r/robotics/comments/1tswgd6/ra_b601dm_ros2_monitoring_overlay_open_source/)**

https://preview.redd.it/fe1av44jdh4h1.png?width=673&format=png&auto=webp&s=8edda1ca704cadc43c8713b1f998096483772a77 The reBot Arm B601-DM has been open-sourced recently and their ROS2 driver is solid! But what I missed during my first sessions was a quick way to see if the hardware was actually healthy, so I built rebotarm_monitor: a small ROS 2 overlay for passive hardware monitoring & future observability planned. It watches the boring (but useful stuff); stale topics, value jumps, weird torques, unexpected status flags, and surfaces it as a standard diagnostic tree you can open in rqt_robot_monitor. Every threshold is a standard ROS2 parameter, so you can tune rates, jumps, velocity, torque or idle behaviour from YAML or launch args without touching code. Give me a star if you found it usefull x) https://github.com/danieldoradotalaveron-rb/rebotarm_monitor_ros2

15h ago

---

**[Anyone have experience with an Agibot G1? Looking for ROS2 advice.](https://www.reddit.com/r/robotics/comments/1tspp8r/anyone_have_experience_with_an_agibot_g1_looking/)**

Hi all, I have an Agibot G1 here. Wondering if anyone is working with this platform and can provide some advice on getting it operational in a ROS2 environment. The manual lists a ton of ROS2 topics that can be used to control various aspects of the robot, arm/head/torso motion, navigation, mapping etc. The latter (SLAM) being my first interest. However logging into the robot, no ROS2 topics are immediately visible. Starting the ROS daemon with ROS_LOCALHOST_ONLY (which is no good long-term, but I guess will do for now) shows a couple of topics but they seem to be subscribers, there's no data on any of them. Grateful for any advice.

20h ago

---

**[[ Removed by Reddit ]](https://www.reddit.com/r/robotics/comments/1tswc72/removed_by_reddit/)**

[ Removed by Reddit on account of violating the content policy. ]

15h ago

---

**[Lingxi X2 dodges thrown balls and goes up and down stairs (AGIBOT’s newly launched AGILE perception-motion foundation model)](https://www.reddit.com/r/robotics/comments/1trw4am/lingxi_x2_dodges_thrown_balls_and_goes_up_and/)**

From AGIBOT on 𝕏 (longer video): https://x.com/AGIBOTofficial/status/2059892813505142786

1d ago

---

**[Does there any Alternative for pancake brushless motor for robotics](https://www.reddit.com/r/robotics/comments/1tsucwl/does_there_any_alternative_for_pancake_brushless/)**

Hi. I saw a lot of people on YouTube use pancake brushless motor for their robotics, such as robot dog But the problem is it is very very expensive https://preview.redd.it/47qndg3pxg4h1.png?width=1566&format=png&auto=webp&s=9bdd07815b19eebfde8719c3dc2aa806187c44e1 So does there any perfect alternative for it I know about servo motor, but the motion space and speed is not the best

16h ago

---

---

## Google News: "robotics"

**[This Trump-linked startup plans to put humanoid robots in the military](https://www.cnbc.com/2026/05/30/humanoid-robots-ukraine-war-foundation-military-ai.html)**

With ties to the Trump family,  Foundation Robotics Labs is aiming to deploy humanoid robots in the military in the next 12 to 18 months.

CNBC • 1d ago

---

**[Nvidia picks Unitree for humanoid robot platform as Chinese startup eyes IPO](https://www.cnbc.com/2026/06/01/nvidia-unitree-humanoid-robotics-system-researchers.html)**

The U.S. chipmaker's first publicly available humanoid robotics system will use humanoids from Chinese startup Unitree.

CNBC • 24m ago

---

**[Robotics: Humanoid Hands Are Physical AI’s Anti-Hype Test](https://www.bloomberg.com/opinion/articles/2026-05-31/robotics-humanoid-hands-are-physical-ai-s-anti-hype-test)**

Bloomberg.com • 11h ago

---

**[Inside China's push for global dominance: Evs, robotics, AI, pandas](https://www.nbcnews.com/nightly-news/video/inside-china-s-push-for-global-dominance-evs-robotics-ai-pandas-264238661587)**

An inside look at China's push for global economic dominance with AI, humanoid robots, electric vehicles and the export of pandas. Plus, "NBC Nightly News" anchor Tom Llamas gets rare access to the restoration project underway at the Great Wall.

NBC News • 17h ago

---

**[Humanoids dance and thread needles as Japanese robotics developers look to outdo Chinese](https://www.ksl.com/article/51503542/humanoids-dance-and-thread-needles-as-japanese-robotics-developers-look-to-outdo-chinese)**

Mechanical hands dexterous enough to thread a needle, childlike dancing robots and adult-sized ones to help with deliveries were on display Thursday as the Humanoids Summit Tokyo opened.

KSL News • 2d ago

---

**[Children Read Intent in Human Eyes but Not in Robots](https://neurosciencenews.com/humanoid-robot-gaze-child-30790/)**

A new study reveals that 3-year-olds read intention in human eyes but fail to recognize nonverbal preferences in a robot's gaze.

Neuroscience News • 12h ago

---

**[Interested in Humanoid Robot Stocks? You Might Consider Buying This Humanoid Robotics ETF](https://www.fool.com/investing/2026/05/31/humanoid-robots-etf-stocks-best-to-buy/)**

This humanoid robotics ETF (KOID) has been performing wonderfully, though it's only been in existence for about a year.

The Motley Fool • 13h ago

---

**[China deploys humanoid robots to sort 1,200 parcels per hour in massive postal hub](https://interestingengineering.com/ai-robotics/china-deploys-humanoid-robots-in-postal-hub)**

Humanoid robots are now helping process millions of daily parcels inside China’s automated postal centers.

Interesting Engineering • 1d ago

---

**[‘Arms race’: why investors can’t let go of robotic hand developers in China](https://www.scmp.com/tech/article/3355365/unicorn-born-record-time-amid-arms-race-among-chinas-robotic-hand-developers)**

South China Morning Post • 1d ago

---

**[Why Richtech Robotics’ (RR) Latest Collaboration Could Change The Conversation](https://finance.yahoo.com/markets/stocks/articles/why-richtech-robotics-rr-latest-143820462.html)**

With a stock price of $3.02, Richtech Robotics Inc. (NASDAQ:RR) is among the 8 Best Up and Coming Penny Stocks to Buy Now. On May 7, Richtech Robotics Inc. (NASDAQ:RR) announced a prospective partnership with SoundHound AI (SOUN), entering into a non-binding letter of intent regarding a strategic collaboration. The proposed partnership would integrate SoundHound’s advanced agentic […]

Yahoo Finance • 14h ago

---

---

## YouTube Videos: "robotics"

**[The Future of Humanoid Robotics | Jonathan Hurst | TEDxPortland](https://www.youtube.com/watch?v=21BzAy5YEuE)**

NOTE FROM TED: TEDx events are independently organized by volunteers. The guidelines we give TEDx organizers are ...

📺 TEDx Talks

👁️ 36K • 👍 881 • 💬 126 • ⏱️ 19:39 • 2d ago

---

**[Tesla&#39;s $25,000 Robot Is Replacing Workers | Optimus Is Here](https://www.youtube.com/watch?v=5p5_dj0Hb-k)**

The full story of Tesla Optimus. Tesla's most ambitious bet ever, the chip behind it all, and the surprising state of the humanoid ...

📺 Ryan Shaw

👁️ 76K • 👍 3K • 💬 407 • ⏱️ 29:20 • 1d ago

---

**[Are consumers ready for humanoid robots?](https://www.youtube.com/watch?v=8nwBjW9Ja9Q)**

Humanoid robots are more impressive than ever before. Not long ago they would barely manage a few steps on stage before ...

📺 Financial Times

👁️ 21K • 👍 417 • 💬 75 • ⏱️ 5:11 • 3d ago

---

**[This $440 Million Startup Is Solving Robotics’ Biggest Problem](https://www.youtube.com/watch?v=PyGkn9DYm9s)**

Meet Generalist, the startup that says the next big leap in robotics won't come from fancier humanoid hardware. It will come from ...

📺 Forbes

👁️ 56K • 👍 1K • 💬 48 • ⏱️ 10:21 • 4d ago

---

**[Shoggoth 👾 Robot Spotlight — War Robots](https://www.youtube.com/watch?v=Csn_o89Y3Fg)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 153K • 👍 4K • 💬 279 • ⏱️ 1:55 • 5d ago

---

**[Shaq surprises Kenny and Chuck with ROBOTS 🤖😂 | Inside the NBA](https://www.youtube.com/watch?v=nIPenYETLtI)**

On Inside the NBA, Shaquille O'Neal surprises Kenny "The Jet" Smith and Charles Barkley with his robots. ✔️ Subscribe to ...

📺 ESPN

👁️ 312K • 👍 6K • 💬 577 • ⏱️ 4:57 • 6d ago

---

**[EVERYONE wants to play THIS HAWK Now! War Robots](https://www.youtube.com/watch?v=_1cp6FzL3Uw)**

War Robots Gameplay: Ultimate Hawk, that makes everyone happy! My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 12K • 👍 522 • 💬 90 • ⏱️ 19:00 • 1d ago

---

**[Arpo the Robot | Nannybot Vs Arpo - Battle of the Bots! | Funny Cartoons for Kids | Arpo and Daniel](https://www.youtube.com/watch?v=KXYp_1XlWr4)**

Join ARPO the Robot for an exciting livestream filled with fun, surprises, and laugh-out-loud moments! Whether he's on a ...

📺 ARPO: The Robot

👁️ 6K • 👍 20 • ⏱️ 1:02:02 • 5h ago

---

**[Meet LimX Luna—Our Next-Gen Full-Size Interactive Humanoid Robot.](https://www.youtube.com/watch?v=-lgo5xqgVko)**

From its elegant design to the advanced technology powering every step, Luna is more than a machine—it's a leap into the future.

📺 LimX Dynamics

👁️ 2.0M • 👍 11K • 💬 1K • ⏱️ 2:32 • 6d ago

---

**[Sword Is The #1 F2p Bot In War Robots Right Now... Meta Slayer](https://www.youtube.com/watch?v=JvlrRsCEWqs)**

The sword bot is everywhere. In the skies and on the ground. I think its the #1 f2p bot in the game right now. The absorber ability is ...

📺 PREDATOR WR

👁️ 11K • 👍 404 • 💬 95 • ⏱️ 13:36 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

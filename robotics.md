---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-31T21:31:59.979036+00:00'
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

**Last Updated:** May 31, 2026 at 21:31 UTC  
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

5h ago

---

**[How often do your designs fail ?](https://www.reddit.com/r/robotics/comments/1tszjfm/how_often_do_your_designs_fail/)**

Hi everyone, I recently had a comment said to me in which someone asked “do you even know if your robots will work?” And I said “yes” to which they scoffed. For context - I’ve been working with cable driven robots (continuum) which is very difficult in comparison to rigid serial link systems from my experience, and it’s taking a lot of trial and error on each design. I’ll have a really good outcome from one robot (shorter in length, good shaping) , and then go to design the next one to be a bit longer and have a completely different outcome (robot has self weight issues, buckling, etc) I’m primarily self taught with these systems and it’s quite a niche field in robotics - yet I’m just curious as to what everyone else’s experience is when designing and building real things that move. I may be taking this comment to heart but it’s really stuck with me in a negative way. I’d love to hear anyone else’s experiences and what they do to keep going.

5h ago

---

**[Fully 3D Printed WALL-E with Functional Tracks](https://www.reddit.com/r/robotics/comments/1ts3y40/fully_3d_printed_walle_with_functional_tracks/)**

I designed and 3D printed this fully articulated WALL-E in Autodesk Fusion. It features functional rolling tracks, a fully poseable body, an opening storage compartment, and several print-in-place components. The project involved multiple design iterations to optimize the track mechanism, joint tolerances, and printability for consumer FDM printers. The 3D printing files are available for free on my MakerWorld profile: https://makerworld.com/models/2865166?appSharePlatform=copy This is also the starting point for my next robotics project, where I plan to integrate DC motors, electronics, and a control system to create a fully mobile robotic platform.

1d ago

---

**[Get hands dirty on VLA+Immitation + RL](https://www.reddit.com/r/robotics/comments/1tt40u6/get_hands_dirty_on_vlaimmitation_rl/)**

2h ago

---

**[RA B601-DM ROS2 Monitoring Overlay - Open Source](https://www.reddit.com/r/robotics/comments/1tswgd6/ra_b601dm_ros2_monitoring_overlay_open_source/)**

https://preview.redd.it/fe1av44jdh4h1.png?width=673&format=png&auto=webp&s=8edda1ca704cadc43c8713b1f998096483772a77 The reBot Arm B601-DM has been open-sourced recently and their ROS2 driver is solid! But what I missed during my first sessions was a quick way to see if the hardware was actually healthy, so I built rebotarm_monitor: a small ROS 2 overlay for passive hardware monitoring & future observability planned. It watches the boring (but useful stuff); stale topics, value jumps, weird torques, unexpected status flags, and surfaces it as a standard diagnostic tree you can open in rqt_robot_monitor. Every threshold is a standard ROS2 parameter, so you can tune rates, jumps, velocity, torque or idle behaviour from YAML or launch args without touching code. Give me a star if you found it usefull x) https://github.com/danieldoradotalaveron-rb/rebotarm_monitor_ros2

7h ago

---

**[Does there any Alternative for pancake brushless motor for robotics](https://www.reddit.com/r/robotics/comments/1tsucwl/does_there_any_alternative_for_pancake_brushless/)**

Hi. I saw a lot of people on YouTube use pancake brushless motor for their robotics, such as robot dog But the problem is it is very very expensive https://preview.redd.it/47qndg3pxg4h1.png?width=1566&format=png&auto=webp&s=9bdd07815b19eebfde8719c3dc2aa806187c44e1 So does there any perfect alternative for it I know about servo motor, but the motion space and speed is not the best

8h ago

---

**[Anyone have experience with an Agibot G1? Looking for ROS2 advice.](https://www.reddit.com/r/robotics/comments/1tspp8r/anyone_have_experience_with_an_agibot_g1_looking/)**

Hi all, I have an Agibot G1 here. Wondering if anyone is working with this platform and can provide some advice on getting it operational in a ROS2 environment. The manual lists a ton of ROS2 topics that can be used to control various aspects of the robot, arm/head/torso motion, navigation, mapping etc. The latter (SLAM) being my first interest. However logging into the robot, no ROS2 topics are immediately visible. Starting the ROS daemon with ROS_LOCALHOST_ONLY (which is no good long-term, but I guess will do for now) shows a couple of topics but they seem to be subscribers, there's no data on any of them. Grateful for any advice.

12h ago

---

**[[ Removed by Reddit ]](https://www.reddit.com/r/robotics/comments/1tswc72/removed_by_reddit/)**

[ Removed by Reddit on account of violating the content policy. ]

7h ago

---

**[Lingxi X2 dodges thrown balls and goes up and down stairs (AGIBOT’s newly launched AGILE perception-motion foundation model)](https://www.reddit.com/r/robotics/comments/1trw4am/lingxi_x2_dodges_thrown_balls_and_goes_up_and/)**

From AGIBOT on 𝕏 (longer video): https://x.com/AGIBOTofficial/status/2059892813505142786

1d ago

---

**[What’s your biggest pain point when debugging RL policies right now?](https://www.reddit.com/r/robotics/comments/1tsuak8/whats_your_biggest_pain_point_when_debugging_rl/)**

For people training RL agents: What part of debugging takes the most time for you? Examples: - figuring out why policy suddenly collapsed - replaying bad episodes - comparing runs - reward debugging - environment bugs - logging / tracking experiments - visualizing failure cases What do you currently do for it? Scripts? WandB? Manual inspection?

8h ago

---

---

## Google News: "robotics"

**[This Trump-linked startup plans to put humanoid robots in the military](https://www.cnbc.com/2026/05/30/humanoid-robots-ukraine-war-foundation-military-ai.html)**

With ties to the Trump family,  Foundation Robotics Labs is aiming to deploy humanoid robots in the military in the next 12 to 18 months.

CNBC • 1d ago

---

**[Humanoid robots 'the future' of car making, says BMW](https://www.bbc.com/news/articles/cgmpwzzvxr2o)**

BMW is introducing humanoid robots to a car plant in Europe, building on similar projects in the US.

BBC • 2d ago

---

**[Inside China's push for global dominance: Evs, robotics, AI, pandas](https://www.nbcnews.com/nightly-news/video/inside-china-s-push-for-global-dominance-evs-robotics-ai-pandas-264238661587)**

An inside look at China's push for global economic dominance with AI, humanoid robots, electric vehicles and the export of pandas. Plus, "NBC Nightly News" anchor Tom Llamas gets rare access to the restoration project underway at the Great Wall.

NBC News • 9h ago

---

**[NVIDIA Research Advances Robotics From Simulation to the Real World](https://blogs.nvidia.com/blog/icra-research-robotics-simulation-to-real-world/)**

Featured at the International Conference on Robotics and Automation, eight new NVIDIA Research papers show how robots trained in simulation are moving into the real world.

NVIDIA Blog • 3d ago

---

**[Why Richtech Robotics’ (RR) Latest Collaboration Could Change The Conversation](https://finance.yahoo.com/markets/stocks/articles/why-richtech-robotics-rr-latest-143820462.html)**

With a stock price of $3.02, Richtech Robotics Inc. (NASDAQ:RR) is among the 8 Best Up and Coming Penny Stocks to Buy Now. On May 7, Richtech Robotics Inc. (NASDAQ:RR) announced a prospective partnership with SoundHound AI (SOUN), entering into a non-binding letter of intent regarding a strategic collaboration. The proposed partnership would integrate SoundHound’s advanced agentic […]

Yahoo Finance • 6h ago

---

**[Why robotic arms are now being integrated with CNC machines](https://www.therobotreport.com/why-robotic-arms-are-now-being-integrated-cnc-machines/)**

Robotic CNC machine tending is becoming more flexible as leading suppliers bring new software and integration to industry.

The Robot Report • 8h ago

---

**[2 Tech ETFs for Nearly Every Corner of the Digital Economy: From Semiconductors to Robotics](https://www.fool.com/investing/2026/05/29/2-tech-etfs-for-nearly-every-corner-of-the-digital/)**

Unless humanity enters another Stone Age, technology will continue to advance. Here's how you can profit from that knowledge.

The Motley Fool • 1d ago

---

**[Three Frederick County Robotics teams reflect on championship event experience](https://www.fredericknewspost.com/news/education/schools/public_k-12/high_school/three-frederick-county-robotics-teams-reflect-on-championship-event-experience/article_e9e02e62-ff4d-5dff-baca-989dc5162a5e.html)**

Three Frederick County Robotics teams have returned from the World Championship with memories, excitement for next season and tools for their future.

The Frederick News-Post • 2d ago

---

**[Elbit subsidiary FUSE acquires AI robotics firm Bluewhite](https://www.jpost.com/defense-and-tech/article-897651)**

'Autonomy and robotics are reshaping how defense forces operate today' - Eyal Dahan, CEO of FUSE, an Elbit Systems subsidiary.

The Jerusalem Post • 3d ago

---

**[The Robotics Stock Nobody’s Talking About Already Has a $23 Billion Backlog](https://investorplace.com/smartmoney/2026/05/robotics-stock-23-billion-backlog/)**

Even as Tesla breaks ground on a dedicated Optimus factory, I see a compelling alternative. It’s a company that directly competes with Optimus… but unlike Tesla, it’s already an established robotics player with a clear first-mover advantage.

InvestorPlace • 3d ago

---

---

## YouTube Videos: "robotics"

**[Stop Wasting Money On Expensive Robot Vacuums 2026](https://www.youtube.com/watch?v=HOMYo539G7g)**

In this video we look at robots in different price categories and provide more affordable picks. Higher End Alternatives ...

📺 Vacuum Nerds

👁️ 2K • 👍 58 • 💬 16 • ⏱️ 9:24 • 10h ago

---

**[The Future of Humanoid Robotics | Jonathan Hurst | TEDxPortland](https://www.youtube.com/watch?v=21BzAy5YEuE)**

NOTE FROM TED: TEDx events are independently organized by volunteers. The guidelines we give TEDx organizers are ...

📺 TEDx Talks

👁️ 26K • 👍 674 • 💬 106 • ⏱️ 19:39 • 2d ago

---

**[Tesla&#39;s $25,000 Robot Is Replacing Workers | Optimus Is Here](https://www.youtube.com/watch?v=5p5_dj0Hb-k)**

The full story of Tesla Optimus. Tesla's most ambitious bet ever, the chip behind it all, and the surprising state of the humanoid ...

📺 Ryan Shaw

👁️ 68K • 👍 2K • 💬 391 • ⏱️ 29:20 • 1d ago

---

**[Are consumers ready for humanoid robots?](https://www.youtube.com/watch?v=8nwBjW9Ja9Q)**

Humanoid robots are more impressive than ever before. Not long ago they would barely manage a few steps on stage before ...

📺 Financial Times

👁️ 19K • 👍 391 • 💬 73 • ⏱️ 5:11 • 2d ago

---

**[EVERYONE wants to play THIS HAWK Now! War Robots](https://www.youtube.com/watch?v=_1cp6FzL3Uw)**

War Robots Gameplay: Ultimate Hawk, that makes everyone happy! My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 11K • 👍 499 • 💬 88 • ⏱️ 19:00 • 1d ago

---

**[This $440 Million Startup Is Solving Robotics’ Biggest Problem](https://www.youtube.com/watch?v=PyGkn9DYm9s)**

Meet Generalist, the startup that says the next big leap in robotics won't come from fancier humanoid hardware. It will come from ...

📺 Forbes

👁️ 54K • 👍 1K • 💬 48 • ⏱️ 10:21 • 4d ago

---

**[NEW Vulcan Robot Is Here - Behemoth Jr With 3 Stage Energy Cannon | War Robots](https://www.youtube.com/watch?v=B_p2JLVIXQo)**

New Vulcan Robot has arrived. I had a feeling we were getting a new robot in this week's test server and we got it. This thing is ...

📺 PREDATOR WR

👁️ 13K • 👍 542 • 💬 98 • ⏱️ 13:43 • 1d ago

---

**[Sword Is The #1 F2p Bot In War Robots Right Now... Meta Slayer](https://www.youtube.com/watch?v=JvlrRsCEWqs)**

The sword bot is everywhere. In the skies and on the ground. I think its the #1 f2p bot in the game right now. The absorber ability is ...

📺 PREDATOR WR

👁️ 11K • 👍 402 • 💬 95 • ⏱️ 13:36 • 2d ago

---

**[Shaq surprises Kenny and Chuck with ROBOTS 🤖😂 | Inside the NBA](https://www.youtube.com/watch?v=nIPenYETLtI)**

On Inside the NBA, Shaquille O'Neal surprises Kenny "The Jet" Smith and Charles Barkley with his robots. ✔️ Subscribe to ...

📺 ESPN

👁️ 307K • 👍 6K • 💬 571 • ⏱️ 4:57 • 5d ago

---

**[NEW AI Robots Are Becoming TOO Human to Ignore... This Changes Everything](https://www.youtube.com/watch?v=uHfzK3wmZQM)**

The humanoid robot revolution just hit a level NOBODY saw coming — and 2026 might be the year everything changes!

📺 The AI Nexus

👁️ 7K • 👍 155 • 💬 21 • ⏱️ 18:41 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

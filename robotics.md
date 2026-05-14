---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-14T20:14:03.609312+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 14, 2026 at 20:14 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Johnny 5 Lego MOC: J5Moc](https://www.reddit.com/r/robotics/comments/1tcpaw1/johnny_5_lego_moc_j5moc/)**

Best Robot of the 80s! I designed this model based on the NOVA S.A.I.N.T-Robot from the movie Short Circuit. "Ey, laser lips! Your mama was a snowblower!"

14h ago

---

**[So many interesting guys to feature… but I don't have enough time to shoot and edit videos](https://www.reddit.com/r/robotics/comments/1td30zx/so_many_interesting_guys_to_feature_but_i_dont/)**

3h ago

---

**[Vision Tracker?](https://www.reddit.com/r/robotics/comments/1tclegi/vision_tracker/)**

CIWS-inspired computer vision tracking system using a Raspberry Pi 5 and ESP32. A Raspberry Pi handles OpenCV CSRT object tracking while the ESP32 controls pan/tilt motor movement realtime. It has a manual and auto mode shown in the video. Manual is controlled with an xbox controller via USB or bluetooth. No one close to me will think it’s cool so i figure reddit will.

17h ago

---

**[LD Robot D500 Watermark on my rover](https://www.reddit.com/r/robotics/comments/1td0x4r/ld_robot_d500_watermark_on_my_rover/)**

Finally added a small distance watermark overlay to my LD Robot D500 setup, so the measured range is always in front of my eyes while testing. Tiny improvement, but it actually makes debugging and live checks way more comfortable & safer

5h ago

---

**[This is where inspection robotics actually becomes useful](https://www.reddit.com/r/robotics/comments/1tc5nas/this_is_where_inspection_robotics_actually/)**

1d ago

---

**[Humanoid Robot like Unitree G1](https://www.reddit.com/r/robotics/comments/1td2a2n/humanoid_robot_like_unitree_g1/)**

How hard is it to create your own humanoid from scratch at home? A humanoid that is capable of walking and standing stable. How much would it cost at least? I know people are building quadruped robots at home under $10k but what about an humanoid? Is it even feasible?

4h ago

---

**[Robot Orders Hold Steady in Q1 2026 as Demand Broadens Across Non-Automotive Industries](https://www.reddit.com/r/robotics/comments/1tczjwf/robot_orders_hold_steady_in_q1_2026_as_demand/)**

A3’s Q1 2026 robot order data shows North American companies ordered 9,055 robots valued at $543 million. Overall units were nearly flat year over year, but the mix of demand shifted in a notable way. Automotive OEM orders were down sharply, with units falling 35.1% and revenue falling 48.2% compared to Q1 2025. That pulled down the total market because automotive programs tend to be large and cyclical. Outside of Automotive OEMs, several sectors posted strong unit growth. Life sciences/pharma/biomed was up 54.1%, semi/electronics/photonics was up 31.7%, plastics and rubber was up 25.2%, food and consumer goods was up 16%, and automotive component suppliers were up 28.1%. Cobots were one of the biggest parts of the report. Companies ordered 1,637 collaborative robots in Q1, up 55.6% in units and 78.2% in revenue year over year. Cobots accounted for 18.1% of all robot units ordered during the quarter.

🔗 [Automate](https://www.automate.org/robotics/news/robot-orders-hold-steady-in-q1-2026-as-demand-broadens-across-non-automotive-industries) • 5h ago

---

**[Wuji tech teases its newest, most advanced humanoid hand](https://www.reddit.com/r/robotics/comments/1tc541q/wuji_tech_teases_its_newest_most_advanced/)**

1d ago

---

**[Locomotion and Self-reconfiguration Autonomy for Spherical Freeform Modular Robots](https://www.reddit.com/r/robotics/comments/1tcrs2e/locomotion_and_selfreconfiguration_autonomy_for/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=GgozSTWPMjg) • 11h ago

---

**[My experience using Claude Code for robotics from the advice of r/robotics](https://www.reddit.com/r/robotics/comments/1tc4r9n/my_experience_using_claude_code_for_robotics_from/)**

Hey r/robotics community, A couple weeks back, I asked about how you all were managing AI development in robotics and I got a bunch of great responses. To summarize: My problems ROS 1 and ROS 2 commands/syntax, Gazebo versions, are consistently confused by Claude Code Claude doesn't really understand the asynchronous messaging structure or any runtime-specific errors/bugs I may run into due to its code The changes Claude Code makes during my development often lead my code in the wrong direction, making debugging take even longer Your solutions Many of you mentioned building custom tooling and skills really helps Claude orient itself Supplying your own context and description of the repository and standardizing it across claude sessions using an `ARCHITECTURE.md` / `CLAUDE.md` also really helps Minimal working examples are also very helpful. Having somewhere Claude can turn to and say, "this is a simple example of how things are supposed to work" helps the agent orient itself I implemented four changes into my setup: Custom MCP tools and skills Supplying context from my own repository Supplying minimal working examples I made myself and found off the internet Supplying documentation relevant to my software stack. For me, that was ROS 2 Jazzy, Gazebo Harmonic, PX4, and Nav2 After making these changes, I've seen a pretty sizeable increase in my development speed using AI in robotics. Previously, I was trying to fill my context window with the code I've already written, but that seemed to not be enough context for Claude to actually understand the software architecture or data pipeline in my codebase. With the changes I've mentioned above, I actually noticed that I can let Claude develop new nodes and software. There's significantly less problems when integrating Claude's code and existing code from what I've seen so far. One thing that was always an annoyance for me was Claude's lack of understanding of what was ROS 1 and what was ROS 2. I ended up creating a RAG database that can input relevant documentation for whatever Claude was working on and that's worked incredibly well. With this in pairing with some custom tool calls I've made, my setup no longer has any confusion on what's ROS 2 and what commands I have access to running ROS 2 Jazzy and Gazebo Harmonic in particular. Thanks for all of your help! I thought I'd leave this post here for those who may also run into something similar trying to use Claude Code for robotics. I'm considering even doing some custom evals for this setup on robotics-specific coding problems because of how much more consistent this setup seems to be. If anyone's already done something similar to this, would love to hear about it in the comments. Cheers!

1d ago

---

---

## Google News: "robotics"

**[Rivian CEO’s robotics startup tops $1 billion in funding: report](https://www.chicagobusiness.com/manufacturing-logistics/ccb-rivian-scaringe-robotics-mind-raises-funding-20260513/)**

A robotics startup founded by Rivian CEO RJ Scaringe has raised another $400 million and plans to deploy AI-powered robots at Rivian’s Normal factory.

Crain's Chicago Business • 1d ago

---

**[Rivian shares jump as AI robotics spinout Mind Robotics closes $400M round](https://finance.yahoo.com/news/rivian-shares-jump-ai-robotics-165500756.html)**

Rivian Automotive Inc (NASDAQ:RIVN) shares rose 4.2% on Wednesday after its spinout Mind Robotics, an artificial intelligence-driven industrial robotics company, closed a $400 million funding round that valued the startup at $3.4 billion. The May 2026 round was led by Kleiner Perkins and also...

Yahoo Finance • 1d ago

---

**[Rivian spinoff Mind Robotics raises another $400M](https://techcrunch.com/2026/05/13/rivian-spinoff-mind-robotics-raises-another-400m/)**

Mind Robotics, which was first revealed in late 2025, has now raised more than $1 billion to date.

TechCrunch • 1d ago

---

**[Science fiction becomes reality: Unitree Robotics unveils world’s first production-ready manned mecha](https://www.globaltimes.cn/page/202605/1360822.shtml)**

Unitree Robotics unveiled the GD01 on Tuesday, a manned transformable mecha priced from 3.9 million yuan ($650,000), quickly sparking heated discussion on Chinese social media, with many netizens describing it as highly futuristic and saying it felt like “science fiction becoming reality.”

Global Times • 2d ago

---

**[Figure AI’s Robots Work 17-Hour Shift, Sort 22,000 Packages](https://www.eweek.com/news/figure-helix-robots-22000-packages/)**

eWeek • 3h ago

---

**[Video David Muir reports on technological advances of China's humanoid robots - ABC News](https://abcnews.com/video/132938245/)**

With the global race for artificial intelligence and robotics technology in full swing, David Muir takes a closer look at the humanoid robots being built in China.

ABC News - Breaking News, Latest News and Videos • 20h ago

---

**[Fanuc Shares Surge After Partnership With Google on Physical AI](https://www.bloomberg.com/news/articles/2026-05-14/fanuc-shares-surge-after-partnership-with-google-on-physical-ai)**

Bloomberg.com • 14h ago

---

**[China wants more robots but not fewer workers](https://www.economist.com/finance-and-economics/2026/05/11/china-wants-more-robots-but-not-fewer-workers)**

The Economist • 3d ago

---

**[Humanoid Robotics In 2026: The Race From Pilot To Platform](https://kraneshares.com/humanoid-robotics-in-2026-the-race-from-pilot-to-platform/)**

The Robots Have Clocked In When Japan Airlines (JAL) deployed humanoid robots at Tokyo’s Haneda Airport in May 2026, the industry’s message was hard to miss. This was not a press conference stunt but a three-year operational commitment from a legacy aviation carrier in one of the world’s most safety-conscious regulatory environments, tasked with solving […]

KraneShares • 2d ago

---

**[NASA Invites Media to Annual Lunabotics Robotics Competition](https://www.nasa.gov/news-release/nasa-invites-media-to-annual-lunabotics-robotics-competition/)**

NASA will hold its 2026 Lunabotics Challenge Tuesday, May 19, to Thursday, May 21, at the Astronauts Memorial

NASA (.gov) • 22h ago

---

---

## YouTube Videos: "robotics"

**[AI Robots Just Unlocked Human-Level Skills… This Changes EVERYTHING](https://www.youtube.com/watch?v=xHxLB28wFxY)**

You're NOT ready for what just dropped in the world of robotics this week... Boston Dynamics Atlas pulled off a flawless handstand ...

📺 The AI Nexus

👁️ 6K • 👍 158 • 💬 18 • ⏱️ 55:02 • 1d ago

---

**[Robot Dogs Are A Security Nightmare](https://www.youtube.com/watch?v=lA8WuXDXfcI)**

Go to https://ground.news/benn for a better way to stay informed. Subscribe for 40% off unlimited access to world-wide coverage ...

📺 Benn Jordan

👁️ 724K • 👍 59K • 💬 5K • ⏱️ 23:53 • 4d ago

---

**[Top 8 NEW Most Realistic AI Robots of 2026 (Updated)](https://www.youtube.com/watch?v=QlBrPz4NcZM)**

Top 8 NEW Most Realistic AI Robots of 2026 (Updated) I know you're tired of those “REALISTIC AI ROBOT” videos where the ...

📺 Technology with Tyler

👁️ 4K • 👍 83 • 💬 17 • ⏱️ 21:16 • 1d ago

---

**[Unitree Unveils: GD01, A Manned Transformable Mecha, from $650,000](https://www.youtube.com/watch?v=oWOyUMJWptc)**

The world's first production-ready manned mecha. It can transform. It's a civilian vehicle. It weighs ~500kg with you inside. Please ...

📺 Unitree Robotics

👁️ 5.2M • 👍 11K • 💬 3K • ⏱️ 1:15 • 2d ago

---

**[Meet Amazon&#39;s $50,000 Robot - Inside Big Tech&#39;s Humanoid Takeover](https://www.youtube.com/watch?v=5d7lkdfe7fI)**

What if your next roommate wasn't human? On this episode of NYC Innovates, we meet Sprout, a 3.5ft robot that dances, does ...

📺 Cheddar

👁️ 473 • 👍 21 • 💬 4 • ⏱️ 10:22 • 6h ago

---

**[Humanoid robot’s Southwest flight sparks instant airline policy change](https://www.youtube.com/watch?v=pnw913voYHA)**

A Dallas business owner attempted something he believes had never been done: flying commercially with his 3.5‑foot humanoid ...

📺 CBS TEXAS

👁️ 97K • 👍 2K • 💬 894 • ⏱️ 3:03 • 21h ago

---

**[Unitree unveils world&#39;s first manned transformable robotic vehicle](https://www.youtube.com/watch?v=LpMElD7-RmM)**

Unitree Robotics has unveiled the GD01 — the world's first mass-produced rideable transforming mecha, with a starting price of ...

📺 CGTN Europe

👁️ 34K • 👍 314 • 💬 39 • ⏱️ 0:33 • 1d ago

---

**[Apple’s New $5,000 Home Robot iSiri Will Make You Forget About Cleaning Forever](https://www.youtube.com/watch?v=cg83PmGY09w)**

Apple's new home robot iSiri is being described as a major step toward fully automated smart living, combining advanced AI with ...

📺 Carros Show

👁️ 19K • 👍 268 • 💬 29 • ⏱️ 23:07 • 2d ago

---

**[The Most Insane Robot I&#39;ve Ever Seen](https://www.youtube.com/watch?v=m2KEIiB1WHE)**

New shorts each and every day. Hit subscribe if you enjoy our content!

📺 VEXR

👁️ 32K • 👍 1K • 💬 51 • ⏱️ 0:29 • 5h ago

---

**[The mecha robot that&#39;s actually production-ready #unitree #engineering #robotics](https://www.youtube.com/watch?v=vEMHIgqI-NU)**

Unitree Robotics just introduced what it calls the world's first production-ready manned transformable mecha. The Chinese ...

📺 Kalil 4.0

👁️ 12K • 👍 258 • 💬 15 • ⏱️ 0:41 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

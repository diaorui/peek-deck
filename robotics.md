---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-01T09:33:05.463649+00:00'
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

**Last Updated:** February 01, 2026 at 09:33 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[[XPENG IRON update] In the end, it didn't turn out well.](https://www.reddit.com/r/robotics/comments/1qso9oq/xpeng_iron_update_in_the_end_it_didnt_turn_out/)**

I hadn't seen the whole video yesterday when I posted it. From The Humanoid Hub on 𝕏: https://x.com/TheHumanoidHub/status/2017646098136141858

5h ago

---

**[Portable offline llm robot I made last night. This is obviously her naked prototype body so be nice to her](https://www.reddit.com/r/robotics/comments/1qsexfy/portable_offline_llm_robot_i_made_last_night_this/)**

The real meat and potatoes: I made this as a modular brain for my other robots I built recently. Right now I’m building her a tiny combat robot body so I can’t wait to program her fight moves. Already slightly tested it but just to get her to stand in a T pose then relax all motors after 5 seconds to get an idea of how to map her body. That was when I used a pi zero tho so more work is definitely needed. After that I need to completely redesign her casing. It’s literally made from an outer frame I printed in a rush and a piece of plastic that held her oled screen in the packaging.

12h ago

---

**[Building a cute little AI Robot with memory -Kuchi 😁](https://www.reddit.com/r/robotics/comments/1qsb4kp/building_a_cute_little_ai_robot_with_memory_kuchi/)**

Day:30 1- Base body and MCU from Sunfounder 2-Built over raspberry pi5 and powered by OpenAI 3- Connected to N8N for tooling like web search., scraping etc Let me know your thoughts 😊

14h ago

---

**[Making a heavy DC motor platform safe: contactors, E-stop, and runaway prevention](https://www.reddit.com/r/robotics/comments/1qs7huf/making_a_heavy_dc_motor_platform_safe_contactors/)**

Hi, I’m working on a repurposed electric wheelchair chassis (>100 kg, high-torque DC motors). Current test setup (yes, I know it’s not safe): • 2 DC motors • Sabertooth 2x32 • 24 V battery pack (2×12 V AGM) • Batteries connected directly to the Sabertooth • Motors connected directly to the Sabertooth • Control is classic RC (throttle + steering) • Motors have normally-closed electromagnetic brakes, but they are not wired yet (mechanically released) Right now: • As soon as I connect the batteries, the controller is powered • There is no real kill switch • The only way to stop everything is unplugging battery connectors • If something goes wrong, the platform could move uncontrollably I’m fully aware this is not acceptable, which is why I’m posting. My goal is to make this safe in as many realistic failure scenarios as possible: • If the main battery disconnects on a slope, the system should default to a safe state (this is where normally-closed electromagnetic brakes make sense). • If RC glitches, is lost, or a microcontroller crashes, the platform must not run away. • Whatever fails (RC, MCU, software, power), there should always be a solid hardware-level barrier preventing uncontrolled motion. I’m planning a hardware upgrade soon: • proper E-STOP / kill switch • DC contactors • wiring the electromagnetic brakes • and adding some kind of MCU in the control chain (ESP32 is the obvious option for me, but Raspberry Pi / onboard computer is also possible) The Sabertooth will remain only the motor power controller. The open question for me is the architecture: whether it’s better to keep “safety/control” and “robotics/autonomy” separated (for example one small MCU for safety + another board for higher-level stuff), or if people commonly keep everything on one controller. What I’m looking for is very practical advice: • How to design a solid anti-runaway architecture for this kind of platform • Where to physically cut power to make the system safe (battery side vs motor lines) • What type of DC contactors is typically used for high-torque DC motors (ratings, poles, inductive loads) • How normally-closed electromagnetic brakes are usually wired in a fail-safe way • How people typically split responsibilities between hardware safety, motor controller config, and a microcontroller (one vs two controllers, etc.) I’m not chasing theory or certifications. I want proven, practical solutions that people actually use to make platforms like this safe to power on. Thanks.

16h ago

---

**[XPENG IRON first public appearance since its release last November](https://www.reddit.com/r/robotics/comments/1qryyxx/xpeng_iron_first_public_appearance_since_its/)**

From: CyberRobo on 𝕏: https://x.com/CyberRobooo/status/2017544750694551618 RoboHub🤖 on 𝕏 (images): https://x.com/XRoboHub/status/2017541654173851909

23h ago

---

**[Why is it secretly flipping me off?](https://www.reddit.com/r/robotics/comments/1qslo30/why_is_it_secretly_flipping_me_off/)**

Saw this one at Wuhu train station in China. Answers questions at a desk. It looks like it has a lot of ability but it otherwise doesn't move at all. Even when you ask it to wave it says "sure, here's a friendly wave" but doesn't move an inch.

7h ago

---

**[Anyone here self-learning robotics (no degree)? Looking to learn together](https://www.reddit.com/r/robotics/comments/1qsojms/anyone_here_selflearning_robotics_no_degree/)**

hey! I’m just starting out in robotics and I’m learning on my own, not through a university or formal degree. I’m super curious about robotics, embedded systems, hardware + software but honestly it can feel pretty overwhelming figuring out where to start and what to focus on I was wondering if anyone else here is in a similar space: - Self-learning robotics - No robotics/engineering degree - Following online courses, yourube, books, projects, arduino/raspberry pi etc - getting stuck a lot but still want to keep going If so, would love to learn together…share resources, small projects, progress updates, failures etc. Maybe a small discord group orsomething if enough people are interested. Skill level doesn’t matter at all. Absolute beginners welcome. The goal is consistency and help eachother learn together If this sounds interesting, please leave a comment about: - What you’re currently learning - What you want to build someday - or just say i want to join thanks 🦾 Edit: I made a small beginner-friendly Discord for learning robotics together. Please join if you are interested. https://discord.gg/qP9pNK2SB

5h ago

---

**[The future of remote workers?](https://www.reddit.com/r/robotics/comments/1qsmoj2/the_future_of_remote_workers/)**

6h ago

---

**[First rover build! Resurrected my dad's 5yr old kits and scraps to make this little guy](https://www.reddit.com/r/robotics/comments/1qsjqlz/first_rover_build_resurrected_my_dads_5yr_old/)**

First time posting here! Ive been messing around with my dad’s scraps for a while, but finally found a rover kit! I built this chassis using a mix of 5-year-old kits and random scraps I had lying around. It was a late night, but getting an actual chassis/frame plus the wiring to work felt amazing. Really really simple build, put it together via an old ESP 32, ( after many cable, Bluetooth pairing, and firmware hassles ) archaic L298N motor driver, and for battery a basic series circuit to up the voltage ( don’t even have batteries sitting haha) I’ve been learning a ton from Practical Electronics for Inventors and The Art of Electronics, but I'm looking for what to tackle next. I’d love to hear your suggestions for: Books that bridge mechanical engineering and embedded systems. Courses on more advanced control (maybe leading into ROS 2?). I’ve played around built software applications with agentic workflows and played around w yolov8 as well. But definitely need more resources on robotics + AI. Let me know if you guys have any tips!!

8h ago

---

**[Parkour in the Wild -- ANYmal robot at ETH](https://www.reddit.com/r/robotics/comments/1qstmf6/parkour_in_the_wild_anymal_robot_at_eth/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=QDU_FicBPDo) • 25m ago

---

---

## Google News: "robotics"

**[Serve Robotics vs. Teradyne: Which Robotics Stock Is the Better Buy?](https://www.zacks.com/stock/news/2825962/serve-robotics-vs-teradyne-which-robotics-stock-is-the-better-buy)**

Zacks Investment Research • 1d ago

---

**[Lake Stevens robotics team receives world recognition](https://www.heraldnet.com/news/lake-stevens-robotics-team-receives-world-recognition/)**

Team Arsenic took second place at the recent ROBO-BASH in Bellingham, earning fifth place in the world.

Everett Herald • 2d ago

---

**[Lightspeed Backs Robotics Startup in $100 Million Round](https://www.bloomberg.com/news/articles/2026-01-29/fiat-toyota-tycoons-back-startup-robco-in-100-million-round)**

Bloomberg.com • 2d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.nbcnews.com/video/china-rolls-out-robot-cops-in-cities-to-push-humanoid-robots-in-daily-life-256872517804)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News’ Janis Mackey Frayer explains how China continues to advance robot technology and is pushing to integrate humanoid robots into daily life.

NBC News • 2d ago

---

**[Tesla to build 1 million Optimus robots per year at Fremont factory, Musk says](https://www.kron4.com/news/technology-ai/tesla-to-build-1-million-optimus-robots-per-year-at-fremont-factory-musk-says/)**

KRON4 • 2d ago

---

**[Into the Omniverse: Physical AI Open Models and Frameworks Advance Robots and Autonomous Systems](https://blogs.nvidia.com/blog/physical-ai-open-models-robot-autonomous-systems-omniverse/)**

By providing access to critical infrastructure — from simulation frameworks to AI models — NVIDIA is enabling collaborative development that accelerates the path to safer, more capable autonomous systems.

NVIDIA Blog • 2d ago

---

**[New York Robotics launches with 160 startups in its ecosystem](https://www.therobotreport.com/new-york-robotics-launches-160-startups-ecosystem/)**

New York Robotics is launching with over 80 industry partners, 20 academic partners, 40 robotics labs, and over 300 venture capital partners.

The Robot Report • 1d ago

---

**[Using electronics to build biohybrid robots with physical intelligence](https://www.nature.com/articles/s41928-025-01552-6)**

Biohybrid robots, which rely on living muscles to drive force generation, could be of use in applications ranging from microsurgery to unmanned exploration. But the development of untethered and autonomous machines will require the integration of onboard electronics for sensing, control and power.

Nature • 1d ago

---

**[AI Robotics Investment Opportunities Extend Beyond Big Tech](https://www.etftrends.com/disruptive-technology-content-hub/ai-robotics-investment-opportunities-extend-beyond-big-tech/)**

ETF Trends • 1d ago

---

**[Guest article: What CES really told us about robotics in the produce sector](https://agfundernews.com/guest-article-what-ces-really-told-us-about-robotics-in-the-produce-sector)**

The best robots in agriculture are the ones growers stop talking about because they just work, said panelists at CES 2026.

AgFunderNews • 1d ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 3K • 👍 55 • 💬 17 • ⏱️ 1:21 • 13h ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 80K • 👍 993 • 💬 207 • ⏱️ 14:25 • 1d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 621K • 👍 5K • 💬 2K • ⏱️ 3:13 • 2d ago

---

**[SaaS is over… Why you should build a robotics company in 2026](https://www.youtube.com/watch?v=FqfTQFuSalY)**

2026 will be the year of robotics. We're in an Will Smith spaghetti moment. Remember how AI-generated video looked horrific two ...

📺 Andreas Klinger ⅹ Europe's Most Ambitious Startups

👁️ 27K • 👍 2K • 💬 206 • ⏱️ 16:46 • 5d ago

---

**[Tesla Fremont factory ending Model S/X manufacturing to begin Optimus robot production](https://www.youtube.com/watch?v=liF86L_EvKQ)**

Andrea Nakano reports on the Tesla Fremont factory ending Model S/X production and using that part of the factory for mass ...

📺 KPIX | CBS NEWS BAY AREA

👁️ 67K • 👍 565 • 💬 333 • ⏱️ 4:36 • 3d ago

---

**[Figure upgrades its humanoid robot with new finger sensors. Real dexterity is coming. #AI #technews](https://www.youtube.com/watch?v=GS1zde45f7I)**

📺 Ryan Shaw

👁️ 2K • 👍 38 • 💬 2 • ⏱️ 1:03 • 6h ago

---

**[Robot That Grows Through Rubble To Find Survivors 🤖 #rescue #robotics #shorts](https://www.youtube.com/watch?v=haGH86W_f5A)**

The Growing Robot That Enters Collapsed Buildings Before Humans Do When disaster strikes and buildings collapse, reaching ...

📺 EcoZora

👁️ 366K • 👍 2K • 💬 152 • ⏱️ 0:07 • 6d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=b8vufpXa21Q)**

📺 Borunte Robot Lin 

👁️ 20K • 👍 81 • ⏱️ 0:22 • 1d ago

---

**[Humanoid Robots Are Coming. They Could Wipe Out This Entire Town](https://www.youtube.com/watch?v=6BJ0XbXOJcs)**

Hyundai is planning to place 30000 humanoid robots in its factories. We talked to an anonymous Hyundai worker who says his ...

📺 More Perfect Union

👁️ 190K • 👍 16K • 💬 2K • ⏱️ 2:59 • 4d ago

---

**[Robot that thinks 😳🤖Detects obstacles &amp; changes path automatically #roboarmy #arduinoprojects](https://www.youtube.com/watch?v=d_sDSfkI8ug)**

ObstacleAvoidance #ArduinoRobot #Robotics #TechReels #DIYProjects.

📺 Roboarmy

👁️ 14K • 👍 221 • 💬 2 • ⏱️ 0:20 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

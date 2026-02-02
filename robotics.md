---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-02T02:23:07.712680+00:00'
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

**Last Updated:** February 02, 2026 at 02:23 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[DEEP Robotics Lynx M20 in high-altitude snowfield logistics operations. Autonomous following, 45° slope climbing, and reliable payload transport in winter conditions.](https://www.reddit.com/r/robotics/comments/1qsvlt3/deep_robotics_lynx_m20_in_highaltitude_snowfield/)**

From DEEP Robotics on 𝕏: https://x.com/DeepRobotics_CN/status/2017114429360656740

15h ago

---

**[[XPENG IRON update] In the end, it didn't turn out well.](https://www.reddit.com/r/robotics/comments/1qso9oq/xpeng_iron_update_in_the_end_it_didnt_turn_out/)**

I hadn't seen the whole video yesterday when I posted it. From The Humanoid Hub on 𝕏: https://x.com/TheHumanoidHub/status/2017646098136141858

22h ago

---

**[We’re open-sourcing our SO101 Parallel Jaw Gripper. It requires zero extra hardware and became a game-changer for our experiments.](https://www.reddit.com/r/robotics/comments/1qtb7n1/were_opensourcing_our_so101_parallel_jaw_gripper/)**

Hi everyone, We are the team behind NormaCore, a unified toolkit designed to fix the fragmented workflow of building physical systems. While our goal is a complete ecosystem (unified API, visual tooling, and high-performance data pipelines), we believe in releasing early and often. Developer experience is at the core of our design philosophy. We got tired of hacking together disjointed tools, so we’re building a foundation that handles everything from complex robotics to distributed sensor networks. To kick off our open-source release cycle, we’re sharing the Parallel Jaw Gripper. It’s a part of a larger 7+1 DoF arm we are refining to bring high-end research robotics to makers and hobby projects. Fully 3D printed and SO101 compatible, the gripper features modular camera mounts and requires zero extra hardware assembly relies entirely on standard motor kit parts. We’d love your feedback on the design and the tooling behind it

🔗 [GitHub](https://github.com/norma-core/norma-core/blob/main/hardware/pgripper/README.md) • 5h ago

---

**[The future of remote workers?](https://www.reddit.com/r/robotics/comments/1qsmoj2/the_future_of_remote_workers/)**

23h ago

---

**[ICRA-IROS Transfer](https://www.reddit.com/r/robotics/comments/1qt2hih/icrairos_transfer/)**

Hello fellow roboticists, I have had a paper rejected from ICRA, and i'm planning to submit it to IROS. I have a question about the ICRA/IROS transfer process. This year they introduced a mechanism to transfer rejected papers along with the authors responses to reviewers to IROS. How does it work, and for those who experienced this during IROS2025, what has your overall experience been with it?

10h ago

---

**[Portable offline llm robot I made last night. This is obviously her naked prototype body so be nice to her](https://www.reddit.com/r/robotics/comments/1qsexfy/portable_offline_llm_robot_i_made_last_night_this/)**

The real meat and potatoes: I made this as a modular brain for my other robots I built recently. Right now I’m building her a tiny combat robot body so I can’t wait to program her fight moves. Already slightly tested it but just to get her to stand in a T pose then relax all motors after 5 seconds to get an idea of how to map her body. That was when I used a pi zero tho so more work is definitely needed. After that I need to completely redesign her casing. It’s literally made from an outer frame I printed in a rush and a piece of plastic that held her oled screen in the packaging.

1d ago

---

**[How to develop your research intuition ?](https://www.reddit.com/r/robotics/comments/1qsy3qk/how_to_develop_your_research_intuition/)**

Young PhD in Computer vision / Robotics here. I have recently read a post of Marie-Anne Lachaux, founding engineer of Llama and Mistral AI, talking about keys of success in research. One of them was « Have good intuition » to reduce the world of possibilities and dig into the right direction. How do you develop this intuition in research, especially in AI and Robotics?

13h ago

---

**[Building a cute little AI Robot with memory -Kuchi 😁](https://www.reddit.com/r/robotics/comments/1qsb4kp/building_a_cute_little_ai_robot_with_memory_kuchi/)**

Day:30 1- Base body and MCU from Sunfounder 2-Built over raspberry pi5 and powered by OpenAI 3- Connected to N8N for tooling like web search., scraping etc Let me know your thoughts 😊

1d ago

---

**[Why is it secretly flipping me off?](https://www.reddit.com/r/robotics/comments/1qslo30/why_is_it_secretly_flipping_me_off/)**

Saw this one at Wuhu train station in China. Answers questions at a desk. It looks like it has a lot of ability but it otherwise doesn't move at all. Even when you ask it to wave it says "sure, here's a friendly wave" but doesn't move an inch.

1d ago

---

**[Making a heavy DC motor platform safe: contactors, E-stop, and runaway prevention](https://www.reddit.com/r/robotics/comments/1qs7huf/making_a_heavy_dc_motor_platform_safe_contactors/)**

Hi, I’m working on a repurposed electric wheelchair chassis (>100 kg, high-torque DC motors). Current test setup (yes, I know it’s not safe): • 2 DC motors • Sabertooth 2x32 • 24 V battery pack (2×12 V AGM) • Batteries connected directly to the Sabertooth • Motors connected directly to the Sabertooth • Control is classic RC (throttle + steering) • Motors have normally-closed electromagnetic brakes, but they are not wired yet (mechanically released) Right now: • As soon as I connect the batteries, the controller is powered • There is no real kill switch • The only way to stop everything is unplugging battery connectors • If something goes wrong, the platform could move uncontrollably I’m fully aware this is not acceptable, which is why I’m posting. My goal is to make this safe in as many realistic failure scenarios as possible: • If the main battery disconnects on a slope, the system should default to a safe state (this is where normally-closed electromagnetic brakes make sense). • If RC glitches, is lost, or a microcontroller crashes, the platform must not run away. • Whatever fails (RC, MCU, software, power), there should always be a solid hardware-level barrier preventing uncontrolled motion. I’m planning a hardware upgrade soon: • proper E-STOP / kill switch • DC contactors • wiring the electromagnetic brakes • and adding some kind of MCU in the control chain (ESP32 is the obvious option for me, but Raspberry Pi / onboard computer is also possible) The Sabertooth will remain only the motor power controller. The open question for me is the architecture: whether it’s better to keep “safety/control” and “robotics/autonomy” separated (for example one small MCU for safety + another board for higher-level stuff), or if people commonly keep everything on one controller. What I’m looking for is very practical advice: • How to design a solid anti-runaway architecture for this kind of platform • Where to physically cut power to make the system safe (battery side vs motor lines) • What type of DC contactors is typically used for high-torque DC motors (ratings, poles, inductive loads) • How normally-closed electromagnetic brakes are usually wired in a fail-safe way • How people typically split responsibilities between hardware safety, motor controller config, and a microcontroller (one vs two controllers, etc.) I’m not chasing theory or certifications. I want proven, practical solutions that people actually use to make platforms like this safe to power on. Thanks.

1d ago

---

---

## Google News: "robotics"

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 7h ago

---

**[Serve Robotics vs. Teradyne: Which Robotics Stock Is the Better Buy?](https://www.zacks.com/stock/news/2825962/serve-robotics-vs-teradyne-which-robotics-stock-is-the-better-buy)**

Zacks Investment Research • 2d ago

---

**[Robotics, for better or for worse](https://opinion.inquirer.net/189405/robotics-for-better-or-for-worse)**

United States President Donald Trump recently signed an executive order assuring the global dominance of the US in artificial intelligence through deregulation and the preemption of state AI laws.

Inquirer.net • 4h ago

---

**[Lake Stevens robotics team receives world recognition](https://www.heraldnet.com/news/lake-stevens-robotics-team-receives-world-recognition/)**

Team Arsenic took second place at the recent ROBO-BASH in Bellingham, earning fifth place in the world.

Everett Herald • 2d ago

---

**[‘Optimus chain’: Chinese suppliers form backbone of Tesla’s humanoid robot plans](https://www.scmp.com/tech/tech-trends/article/3341953/optimus-chain-chinese-suppliers-form-backbone-teslas-humanoid-robot-initiative)**

Tesla’s pivot to producing humanoid robots is expected to engage a network of key Chinese component makers.

South China Morning Post • 20h ago

---

**[New York Robotics launches with 160 startups in its ecosystem](https://www.therobotreport.com/new-york-robotics-launches-160-startups-ecosystem/)**

New York Robotics is launching with over 80 industry partners, 20 academic partners, 40 robotics labs, and over 300 venture capital partners.

The Robot Report • 2d ago

---

**[AI Robotics Investment Opportunities Extend Beyond Big Tech](https://www.etftrends.com/disruptive-technology-content-hub/ai-robotics-investment-opportunities-extend-beyond-big-tech/)**

ETF Trends • 2d ago

---

**[Using electronics to build biohybrid robots with physical intelligence](https://www.nature.com/articles/s41928-025-01552-6)**

Biohybrid robots, which rely on living muscles to drive force generation, could be of use in applications ranging from microsurgery to unmanned exploration. But the development of untethered and autonomous machines will require the integration of onboard electronics for sensing, control and power.

Nature • 2d ago

---

**[Oceaneering International’s Subsea Robotics Shift Reshapes Energy And Defense Mix](https://finance.yahoo.com/news/oceaneering-international-subsea-robotics-shift-220614962.html)**

Oceaneering International (NYSE:OII) is seeing rising interest in its subsea robotics capabilities as it expands into defense and non energy markets. The company is building on its established offshore expertise to pursue contracts and partnerships beyond traditional oil and gas activity. This shift reflects a broader push to diversify its revenue sources into areas that are less tied to energy price cycles. For investors watching NYSE:OII, the focus is increasingly on how the robotics and...

Yahoo Finance • 4h ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.nbcnews.com/video/china-rolls-out-robot-cops-in-cities-to-push-humanoid-robots-in-daily-life-256872517804)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News’ Janis Mackey Frayer explains how China continues to advance robot technology and is pushing to integrate humanoid robots into daily life.

NBC News • 2d ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 8K • 👍 91 • 💬 24 • ⏱️ 1:21 • 1d ago

---

**[Most HUMANLIKE Robot Yet? XPENG Iron STUNS and STUMBLES as DroidUp Brings Most Fully Bionic Android](https://www.youtube.com/watch?v=rYqkI8gFvRc)**

The fast-rising Chinese EV maker XPENG's next-generation Iron humanoid robot is going viral. In footage making the rounds on ...

📺 Kalil 4.0

👁️ 2K • 👍 88 • 💬 21 • ⏱️ 7:44 • 18h ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 118K • 👍 1K • 💬 288 • ⏱️ 14:25 • 2d ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 3K • 👍 48 • 💬 11 • ⏱️ 2:06 • 10h ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 736K • 👍 6K • 💬 2K • ⏱️ 3:13 • 2d ago

---

**[Tesla Fremont factory ending Model S/X manufacturing to begin Optimus robot production](https://www.youtube.com/watch?v=liF86L_EvKQ)**

Andrea Nakano reports on the Tesla Fremont factory ending Model S/X production and using that part of the factory for mass ...

📺 KPIX | CBS NEWS BAY AREA

👁️ 69K • 👍 577 • 💬 337 • ⏱️ 4:36 • 3d ago

---

**[🔬 Sony’s Microsurgery Robot Prototype: Scaled Hand Control, Auto Tool Swaps, and 4K Precision](https://www.youtube.com/watch?v=OsEDfzhhAiA)**

This is Sony's prototype microsurgery assistance robot, designed for operations where human hands reach their physical limits.

📺 Fact

👁️ 13K • 👍 127 • 💬 4 • ⏱️ 0:06 • 10h ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=b8vufpXa21Q)**

📺 Borunte Robot Lin 

👁️ 32K • 👍 86 • ⏱️ 0:22 • 2d ago

---

**[Make Your Own Cute Dasai Mochi Robot🤖 | #ashwinprojects #AltiumStudentLab](https://www.youtube.com/watch?v=KsDxCDsoWMk)**

Make Your Own Cute Dasai Mochi Robot   | #ashwinprojects #AltiumStudentLab Accelerate Your Career in Electronics Design ...

📺 Ashwin Projects

👁️ 454K • 👍 15K • 💬 86 • ⏱️ 1:49 • 4d ago

---

**[World’s First Intelligent Grain Leveling Robot | AI‑Powered Unmanned Grain Storage Revolution #robot](https://www.youtube.com/watch?v=u2GVlWZG078)**

World's First Intelligent Grain Leveling Robot is Here And It's Changing The Future Of Grain Storage Forever. For the first time in ...

📺 Future Lens Pi

👁️ 33K • 💬 14 • ⏱️ 0:08 • 17h ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-01T14:53:43.258068+00:00'
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

**Last Updated:** February 01, 2026 at 14:53 UTC  
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

10h ago

---

**[DEEP Robotics Lynx M20 in high-altitude snowfield logistics operations. Autonomous following, 45° slope climbing, and reliable payload transport in winter conditions.](https://www.reddit.com/r/robotics/comments/1qsvlt3/deep_robotics_lynx_m20_in_highaltitude_snowfield/)**

From DEEP Robotics on 𝕏: https://x.com/DeepRobotics_CN/status/2017114429360656740

3h ago

---

**[Portable offline llm robot I made last night. This is obviously her naked prototype body so be nice to her](https://www.reddit.com/r/robotics/comments/1qsexfy/portable_offline_llm_robot_i_made_last_night_this/)**

The real meat and potatoes: I made this as a modular brain for my other robots I built recently. Right now I’m building her a tiny combat robot body so I can’t wait to program her fight moves. Already slightly tested it but just to get her to stand in a T pose then relax all motors after 5 seconds to get an idea of how to map her body. That was when I used a pi zero tho so more work is definitely needed. After that I need to completely redesign her casing. It’s literally made from an outer frame I printed in a rush and a piece of plastic that held her oled screen in the packaging.

17h ago

---

**[Building a cute little AI Robot with memory -Kuchi 😁](https://www.reddit.com/r/robotics/comments/1qsb4kp/building_a_cute_little_ai_robot_with_memory_kuchi/)**

Day:30 1- Base body and MCU from Sunfounder 2-Built over raspberry pi5 and powered by OpenAI 3- Connected to N8N for tooling like web search., scraping etc Let me know your thoughts 😊

19h ago

---

**[Why is it secretly flipping me off?](https://www.reddit.com/r/robotics/comments/1qslo30/why_is_it_secretly_flipping_me_off/)**

Saw this one at Wuhu train station in China. Answers questions at a desk. It looks like it has a lot of ability but it otherwise doesn't move at all. Even when you ask it to wave it says "sure, here's a friendly wave" but doesn't move an inch.

12h ago

---

**[Making a heavy DC motor platform safe: contactors, E-stop, and runaway prevention](https://www.reddit.com/r/robotics/comments/1qs7huf/making_a_heavy_dc_motor_platform_safe_contactors/)**

Hi, I’m working on a repurposed electric wheelchair chassis (>100 kg, high-torque DC motors). Current test setup (yes, I know it’s not safe): • 2 DC motors • Sabertooth 2x32 • 24 V battery pack (2×12 V AGM) • Batteries connected directly to the Sabertooth • Motors connected directly to the Sabertooth • Control is classic RC (throttle + steering) • Motors have normally-closed electromagnetic brakes, but they are not wired yet (mechanically released) Right now: • As soon as I connect the batteries, the controller is powered • There is no real kill switch • The only way to stop everything is unplugging battery connectors • If something goes wrong, the platform could move uncontrollably I’m fully aware this is not acceptable, which is why I’m posting. My goal is to make this safe in as many realistic failure scenarios as possible: • If the main battery disconnects on a slope, the system should default to a safe state (this is where normally-closed electromagnetic brakes make sense). • If RC glitches, is lost, or a microcontroller crashes, the platform must not run away. • Whatever fails (RC, MCU, software, power), there should always be a solid hardware-level barrier preventing uncontrolled motion. I’m planning a hardware upgrade soon: • proper E-STOP / kill switch • DC contactors • wiring the electromagnetic brakes • and adding some kind of MCU in the control chain (ESP32 is the obvious option for me, but Raspberry Pi / onboard computer is also possible) The Sabertooth will remain only the motor power controller. The open question for me is the architecture: whether it’s better to keep “safety/control” and “robotics/autonomy” separated (for example one small MCU for safety + another board for higher-level stuff), or if people commonly keep everything on one controller. What I’m looking for is very practical advice: • How to design a solid anti-runaway architecture for this kind of platform • Where to physically cut power to make the system safe (battery side vs motor lines) • What type of DC contactors is typically used for high-torque DC motors (ratings, poles, inductive loads) • How normally-closed electromagnetic brakes are usually wired in a fail-safe way • How people typically split responsibilities between hardware safety, motor controller config, and a microcontroller (one vs two controllers, etc.) I’m not chasing theory or certifications. I want proven, practical solutions that people actually use to make platforms like this safe to power on. Thanks.

22h ago

---

**[How to develop your research intuition ?](https://www.reddit.com/r/robotics/comments/1qsy3qk/how_to_develop_your_research_intuition/)**

Young PhD in Computer vision / Robotics here. I have recently read a post of Marie-Anne Lachaux, founding engineer of Llama and Mistral AI, talking about keys of success in research. One of them was « Have good intuition » to reduce the world of possibilities and dig into the right direction. How do you develop this intuition in research, especially in AI and Robotics?

1h ago

---

**[XPENG IRON first public appearance since its release last November](https://www.reddit.com/r/robotics/comments/1qryyxx/xpeng_iron_first_public_appearance_since_its/)**

From: CyberRobo on 𝕏: https://x.com/CyberRobooo/status/2017544750694551618 RoboHub🤖 on 𝕏 (images): https://x.com/XRoboHub/status/2017541654173851909

1d ago

---

**[The future of remote workers?](https://www.reddit.com/r/robotics/comments/1qsmoj2/the_future_of_remote_workers/)**

11h ago

---

**[First rover build! Resurrected my dad's 5yr old kits and scraps to make this little guy](https://www.reddit.com/r/robotics/comments/1qsjqlz/first_rover_build_resurrected_my_dads_5yr_old/)**

First time posting here! Ive been messing around with my dad’s scraps for a while, but finally found a rover kit! I built this chassis using a mix of 5-year-old kits and random scraps I had lying around. It was a late night, but getting an actual chassis/frame plus the wiring to work felt amazing. Really really simple build, put it together via an old ESP 32, ( after many cable, Bluetooth pairing, and firmware hassles ) archaic L298N motor driver, and for battery a basic series circuit to up the voltage ( don’t even have batteries sitting haha) I’ve been learning a ton from Practical Electronics for Inventors and The Art of Electronics, but I'm looking for what to tackle next. I’d love to hear your suggestions for: Books that bridge mechanical engineering and embedded systems. Courses on more advanced control (maybe leading into ROS 2?). I’ve played around built software applications with agentic workflows and played around w yolov8 as well. But definitely need more resources on robotics + AI. Let me know if you guys have any tips!!

14h ago

---

---

## Google News: "robotics"

**[Elon Musk is stressing robots over cars. Here are three humanoid parts suppliers that Morgan Stanley recommends](https://www.cnbc.com/2026/02/01/musk-is-stressing-robots-over-cars-these-suppliers-make-humanoid-parts.html)**

Morgan Stanley analysts highlight stocks of companies that sell specialized robotics parts.

CNBC • 1h ago

---

**[‘Optimus chain’: Chinese suppliers form backbone of Tesla’s humanoid robot plans](https://www.scmp.com/tech/tech-trends/article/3341953/optimus-chain-chinese-suppliers-form-backbone-teslas-humanoid-robot-initiative)**

Tesla’s pivot to producing humanoid robots is expected to engage a network of key Chinese component makers.

South China Morning Post • 8h ago

---

**[Report: humanoid robots set to drive demand for solid-state batteries](https://electrek.co/2026/01/30/report-humanoid-robots-set-to-drive-demand-for-solid-state-batteries/)**

Humanoid robots are set to soak up a whopping 75 GWh of solid-state battery capacity between now and 2035 – nearly 1500x growth!

Electrek • 1d ago

---

**[Tesla kills Models S and X to build humanoid robots instead](https://arstechnica.com/cars/2026/01/tesla-kills-models-s-and-x-to-build-humanoid-robots-instead/)**

EVs that were once industry-leading have long since been left behind.

Ars Technica • 3d ago

---

**[Elon Musk's plan to redesign the world's factories... and perhaps the planet too: humanoid robots that work 12 hours a day, never rest, and use artificial intelligence](https://www.ecoticias.com/en/elon-musks-plan-to-redesign-the-worlds-factories-and-perhaps-the-planet-too-humanoid-robots-that-work-12-hours-a-day-never-rest-and-use-artificial-intelligence/26445/)**

Tesla has quietly crossed a line that could reshape factory work worldwide. On January 21, 2026 the company began mass production of its Optimus Gen 3

ECOticias.com • 3h ago

---

**[What evolving robot standards mean for implementations of cobots](https://www.therobotreport.com/evolving-robot-standards-mean-cobots-implementations/)**

Changing robot standards provide an opportunity for designers of cobots to deliver improved safety and greater functionality, says IDEC.

The Robot Report • 1h ago

---

**[Bills would protect reefs, bar military live-fire training, expand robotics](https://www.staradvertiser.com/2026/02/01/hawaii-news/bills-would-protect-reefs-bar-military-live-fire-training-expand-robotics/)**

Hawaii’s watersheds and coral reefs would be recognized as “legal persons” with legal rights; high school robotics could become an interscholastic sport; military live-fire training would be banned on state land; and a new fee would be charged on any “sugar-sweetened” beverages under new House and Senate bills to be considered during the legislative session that’s scheduled to adjourn May 8.

Honolulu Star-Advertiser • 4h ago

---

**[Lake Stevens robotics team receives world recognition](https://www.heraldnet.com/news/lake-stevens-robotics-team-receives-world-recognition/)**

Team Arsenic took second place at the recent ROBO-BASH in Bellingham, earning fifth place in the world.

Everett Herald • 2d ago

---

**[Lightspeed Backs Robotics Startup in $100 Million Round](https://www.bloomberg.com/news/articles/2026-01-29/fiat-toyota-tycoons-back-startup-robco-in-100-million-round)**

Bloomberg.com • 2d ago

---

**[Tesla axes EV models in drive for robotics revenue](https://news.sky.com/story/tesla-axes-ev-models-in-drive-for-robotics-revenue-13500444)**

Investors liked what they heard about the future following the company's latest results, but Elon Musk is under huge pressure to deliver on his vision as a series of targets have been missed.

Sky News • 3d ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 4K • 👍 69 • 💬 20 • ⏱️ 1:21 • 18h ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 92K • 👍 1K • 💬 234 • ⏱️ 14:25 • 1d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 655K • 👍 6K • 💬 2K • ⏱️ 3:13 • 2d ago

---

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 289K • 💬 153 • ⏱️ 0:18 • 6d ago

---

**[SaaS is over… Why you should build a robotics company in 2026](https://www.youtube.com/watch?v=FqfTQFuSalY)**

2026 will be the year of robotics. We're in an Will Smith spaghetti moment. Remember how AI-generated video looked horrific two ...

📺 Andreas Klinger ⅹ Europe's Most Ambitious Startups

👁️ 28K • 👍 2K • 💬 207 • ⏱️ 16:46 • 6d ago

---

**[A Robot Woke Up and Asked WHERE HIS SKIN WAS…](https://www.youtube.com/watch?v=I9SnoYoCfnE)**

Wait, there was a robot who woke up and started asking for skin?! Sounds like a Life of Luxury video to me but somehow it's not…

📺 LaurenZside

👁️ 216K • 👍 14K • 💬 2K • ⏱️ 19:59 • 23h ago

---

**[Make Your Own Cute Dasai Mochi Robot🤖 | #ashwinprojects #AltiumStudentLab](https://www.youtube.com/watch?v=KsDxCDsoWMk)**

Make Your Own Cute Dasai Mochi Robot   | #ashwinprojects #AltiumStudentLab Accelerate Your Career in Electronics Design ...

📺 Ashwin Projects

👁️ 445K • 👍 15K • 💬 86 • ⏱️ 1:49 • 4d ago

---

**[Figure upgrades its humanoid robot with new finger sensors. Real dexterity is coming. #AI #technews](https://www.youtube.com/watch?v=GS1zde45f7I)**

📺 Ryan Shaw

👁️ 3K • 👍 47 • 💬 3 • ⏱️ 1:03 • 11h ago

---

**[Tesla Fremont factory ending Model S/X manufacturing to begin Optimus robot production](https://www.youtube.com/watch?v=liF86L_EvKQ)**

Andrea Nakano reports on the Tesla Fremont factory ending Model S/X production and using that part of the factory for mass ...

📺 KPIX | CBS NEWS BAY AREA

👁️ 67K • 👍 567 • 💬 333 • ⏱️ 4:36 • 3d ago

---

**[Robot That Grows Through Rubble To Find Survivors 🤖 #rescue #robotics #shorts](https://www.youtube.com/watch?v=haGH86W_f5A)**

The Growing Robot That Enters Collapsed Buildings Before Humans Do When disaster strikes and buildings collapse, reaching ...

📺 EcoZora

👁️ 366K • 👍 2K • 💬 152 • ⏱️ 0:07 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

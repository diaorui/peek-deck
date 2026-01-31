---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-31T22:49:31.132535+00:00'
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

**Last Updated:** January 31, 2026 at 22:49 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[XPENG IRON first public appearance since its release last November](https://www.reddit.com/r/robotics/comments/1qryyxx/xpeng_iron_first_public_appearance_since_its/)**

From: CyberRobo on 𝕏: https://x.com/CyberRobooo/status/2017544750694551618 RoboHub🤖 on 𝕏 (images): https://x.com/XRoboHub/status/2017541654173851909

12h ago

---

**[Making a heavy DC motor platform safe: contactors, E-stop, and runaway prevention](https://www.reddit.com/r/robotics/comments/1qs7huf/making_a_heavy_dc_motor_platform_safe_contactors/)**

Hi, I’m working on a repurposed electric wheelchair chassis (>100 kg, high-torque DC motors). Current test setup (yes, I know it’s not safe): • 2 DC motors • Sabertooth 2x32 • 24 V battery pack (2×12 V AGM) • Batteries connected directly to the Sabertooth • Motors connected directly to the Sabertooth • Control is classic RC (throttle + steering) • Motors have normally-closed electromagnetic brakes, but they are not wired yet (mechanically released) Right now: • As soon as I connect the batteries, the controller is powered • There is no real kill switch • The only way to stop everything is unplugging battery connectors • If something goes wrong, the platform could move uncontrollably I’m fully aware this is not acceptable, which is why I’m posting. My goal is to make this safe in as many realistic failure scenarios as possible: • If the main battery disconnects on a slope, the system should default to a safe state (this is where normally-closed electromagnetic brakes make sense). • If RC glitches, is lost, or a microcontroller crashes, the platform must not run away. • Whatever fails (RC, MCU, software, power), there should always be a solid hardware-level barrier preventing uncontrolled motion. I’m planning a hardware upgrade soon: • proper E-STOP / kill switch • DC contactors • wiring the electromagnetic brakes • and adding some kind of MCU in the control chain (ESP32 is the obvious option for me, but Raspberry Pi / onboard computer is also possible) The Sabertooth will remain only the motor power controller. The open question for me is the architecture: whether it’s better to keep “safety/control” and “robotics/autonomy” separated (for example one small MCU for safety + another board for higher-level stuff), or if people commonly keep everything on one controller. What I’m looking for is very practical advice: • How to design a solid anti-runaway architecture for this kind of platform • Where to physically cut power to make the system safe (battery side vs motor lines) • What type of DC contactors is typically used for high-torque DC motors (ratings, poles, inductive loads) • How normally-closed electromagnetic brakes are usually wired in a fail-safe way • How people typically split responsibilities between hardware safety, motor controller config, and a microcontroller (one vs two controllers, etc.) I’m not chasing theory or certifications. I want proven, practical solutions that people actually use to make platforms like this safe to power on. Thanks.

5h ago

---

**[Portable offline llm robot I made last night. This is obviously her naked prototype body so be nice to her](https://www.reddit.com/r/robotics/comments/1qsexfy/portable_offline_llm_robot_i_made_last_night_this/)**

The real meat and potatoes: I made this as a modular brain for my other robots I built recently. Right now I’m building her a tiny combat robot body so I can’t wait to program her fight moves. Already slightly tested it but just to get her to stand in a T pose then relax all motors after 5 seconds to get an idea of how to map her body. That was when I used a pi zero tho so more work is definitely needed. After that I need to completely redesign her casing. It’s literally made from an outer frame I printed in a rush and a piece of plastic that held her oled screen in the packaging.

1h ago

---

**[Building a cute little AI Robot with memory -Kuchi 😁](https://www.reddit.com/r/robotics/comments/1qsb4kp/building_a_cute_little_ai_robot_with_memory_kuchi/)**

Day:30 1- Base body and MCU from Sunfounder 2-Built over raspberry pi5 and powered by OpenAI 3- Connected to N8N for tooling like web search., scraping etc Let me know your thoughts 😊

3h ago

---

**[ICRA 2026 Acceptance Notification](https://www.reddit.com/r/robotics/comments/1qs19lr/icra_2026_acceptance_notification/)**

Has anyone already received a notification for their ICRA 2026 submission? As of January 31, 4 AM PST, my paper status is still “Decision Pending” rather than “Undisclosed.” Is this normal, or should it have updated by now?

10h ago

---

**[ICRA - ChatGPT Generated Rreviews?](https://www.reddit.com/r/robotics/comments/1qs7830/icra_chatgpt_generated_rreviews/)**

I just received the news that my ICRA submission was rejected. Which is fine. I never submitted with the expectation that it would get accepted but hoping that I would get some valuable feedback in the case of a rejection. Unfortunately this was not the case. The decision was made based on just two reviews. One of which was relatively neutral but seemingly written by someone who was not deeply familiar with the subject. Not a problem in itself but not a good basis for a decision in the case of only two reviews. The one that worries me more is the second review which in my opinion is likely written by ChatGPT or a similar LLM. I base this opinion on the way it is written going into unnecessary detail but also on the fact that most criticisms are just incorrect. Showing very limited understanding of the subject both in theoretical as well as in practical aspects as well as a lack of basic logic. This was my first time submitting to ICRA and if this is the kind of review quality to expect from a "top" conference it will also be the last time. It does not seem like a good conference unless you are doing mainstream research. I will include the review in question and invite anybody to read the preprint of my paper to form your own opinion. The preprint is identical to the version I submitted anonymization fron the double blind review. Modeling of UAV Tether Aerodynamics for Real-Time Simulation I would be happy about any feedback about my paper or your own experiences with ICRA and other "top" conferences. Following is the review. (Note when they talk about missing reference [?] this is due to the anonymization. I removed the citation when citing my own previous work) This paper addresses the important problem of modeling the tension forces and geometric shape of a tethered cable subjected to drag and wind forces, specifically within the context of drone tethering applications. The authors present a dual-solution approach: an analytical model based on the catenary equations, and a numerical solution derived using the IPOPT optimization solver within the CasADi framework. Despite the interesting and relevant application, the paper suffers from several major concerns that must be comprehensively addressed before publication. Major Comments: - Lack of Clarity and Novelty in Introduction The Introduction fails to clearly articulate the problem's relevance for tethered drone systems (e.g., increased energy consumption, system instability, or control degradation due to cable dynamics). This critical context is left for the reader to infer. More importantly, the authors do not explicitly define the novelty or scientific contribution of the proposed dual-solution approach over the existing state of the art. The introduction must clearly establish how this work advances previous research. - The State-of-the-Art section describes previous works but struggles to differentiate the current contribution. Solutions presented in references, such as [5] and [6], appear to address similar or potentially more complete aspects of the problem. The authors must rigorously specify what makes their approach unique and scientifically significant compared to these prior methods. Without this clarity, the paper's contribution remains ambiguous to the reader. - The Analytical Approach section, while well-explained, relies heavily on existing theory. However, the subsequent Numerical Solution section lacks sufficient justification for its necessity. Observing Figure 4, the analytical and numerical solutions for the cable shape are notably similar. Crucially, the paper does not provide a true ground truth or a comparative analysis (e.g., computational cost, convergence rate, robustness to highly non-ideal conditions) to argue for the superiority or necessity of the numerical optimization solver. The authors must explain the specific scenarios where the numerical approach offers a non-trivial advantage. - The real-world experiment, which aims to validate the proposed online estimation of cable shape and tension, highlights several critical issues: Redundancy: The numerical and analytical cable shape estimations appear to be almost overlapping, reinforcing the question regarding the necessity of the computationally intensive numerical approach. Inconsistency with Measurement: The force cell measurements diverge significantly from the results predicted by both the analytical and numerical models, suggesting a fundamental modeling or implementation flaw that must be investigated and corrected. Contradictory Assumption: The experimental section assumes zero wind, a highly restrictive and unrealistic simplification that directly contradicts the paper's central motivation presented in the Introduction ("...optimize the design, modeling, and control of drones tethered to a moving ground vehicle in real-world conditions like strong wind."). This assumption undermines the stated purpose and the validity of the drag modeling. Kinematic Error: The assumption that ground speed is equal to airspeed is fundamentally incorrect in real-world scenarios, where wind (a stated variable in the paper's premise) is a major differentiating factor. Minor Notes - Missing Reference: The phrase "In [?], we have looked at optimization of the tether parameters..." contains a placeholder. This reference should be corrected to: "In [Number], the authors..." to maintain academic style and anonymity during review. - Inappropriate Language: The sentence, "Besides the necessary interface changes, two new lines of code were added and two lines were adjusted, showing the flexibility of the approach," is more suitable for a technical report or implementation note. In a formal conference paper, this assertion should be replaced with a more rigorous, quantitative statement about the modularity and computational efficiency of the implementation. The core concept of modeling tether dynamics is valuable, but the current manuscript is incomplete and requires significant revision. The major issues stem from unvalidated model results, unjustified complexity of the numerical solution, and experimental assumptions that directly contradict the paper's stated goals regarding wind effects. The authors must provide stronger evidence of the scientific contribution and rigorously validate the models under the realistic conditions outlined in the introduction.

6h ago

---

**[Pib-Roboter im Selbstbau.](https://www.reddit.com/r/robotics/comments/1qs0vjp/pibroboter_im_selbstbau/)**

Fast fertiggestellt. Nur noch die Servo Bricks mit Strom versorgen. Dann kann der erste Test starten. #insento Pib.rocks Einige hundert Stunden hat der 3D-Drucker gedruckt. Etwa 150 Teile. Dazu hunderte Schrauben und Muttern, Kugellager. MEhr als 20 Servomotoren, Raspi, Monitor, 360 Grad Mikroarray, Kamera mit Objekterkennung. Und viele Arbeitsstunden - ich bin mal gespannt, ob dann alles funktioniert.

10h ago

---

**[Probably the world's best beer delivery robot :-)](https://www.reddit.com/r/robotics/comments/1qryd3l/probably_the_worlds_best_beer_delivery_robot/)**

It was good, old Boxie 1. Now, there is Boxie 2: stronger, better, more capable ... but it is shy to deliver the beer :-)

12h ago

---

**[Using low-cost Android smartphones as embedded telematics gateways on forklifts – sane or bad idea?](https://www.reddit.com/r/robotics/comments/1qs047w/using_lowcost_android_smartphones_as_embedded/)**

I’m working on an industrial telematics system for a client who operates a fleet of electric forklifts . The proposed architecture is to mount a low-cost Android smartphone permanently on each forklift . Role of the Android phone: - Acts as the edge gateway - 4G connectivity to cloud - GPS positioning and speed estimation - Shock detection using accelerometer - Inclination (pitch/roll) using sensors - Driver identification using front camera (event-based face recognition) - Bluetooth (BLE) communication with an ESP32 that handles CAN bus + battery/current sensors Hardware constraints: - Low-end Android phones (≈3–4 GB RAM, quad-core CPU) - Continuous charging from forklift 24V - Industrial vibration environment - Android 11–14 range This is for a real client, not a hobby project. My questions to engineers who’ve done industrial / Android-at-the-edge systems: Is this architecture considered reasonable in production, or a maintenance nightmare long-term? What are the biggest failure modes you’ve seen when using Android phones as embedded gateways? Would you strongly recommend replacing the phone with a dedicated telematics box instead? Any hard lessons around Android background limits, BLE reliability, or sensor accuracy in vehicles? If you’ve shipped something similar, what would you do differently today? I’m intentionally not relying on OEM forklift firmware to keep the system brand-agnostic. Looking for honest, experience-based feedback positive or negative.

11h ago

---

**[ICRA 2026 review discussion](https://www.reddit.com/r/robotics/comments/1qs2thb/icra_2026_review_discussion/)**

I guess it’s time for a new thread to discuss ICRA 2026 review results. This is my first first author submission and really looking forward to it 🙏

9h ago

---

---

## Google News: "robotics"

**[Tesla lurches into the Musk robotics era](https://www.ft.com/content/6a6cfa00-6f51-4abc-bd68-1738580bd2c5)**

Future of the company lies in equipping and running a global fleet of driverless taxis and in selling humanoid robots

Financial Times • 2d ago

---

**[Tesla to build 1 million Optimus robots per year at Fremont factory, Musk says](https://www.kron4.com/news/technology-ai/tesla-to-build-1-million-optimus-robots-per-year-at-fremont-factory-musk-says/)**

KRON4 • 2d ago

---

**[Tesla discontinues Model X and S vehicles as Elon Musk pivots to robotics](https://www.theguardian.com/technology/2026/jan/28/tesla-q4-earnings-estimates-elon-musk)**

Musk’s optimism for Optimus robot demand help EV maker beat quarterly expectations despite first-ever yearly revenue decline

The Guardian • 3d ago

---

**[Lake Stevens robotics team receives world recognition](https://www.heraldnet.com/news/lake-stevens-robotics-team-receives-world-recognition/)**

Team Arsenic took second place at the recent ROBO-BASH in Bellingham, earning fifth place in the world.

Everett Herald • 1d ago

---

**[Lightspeed Backs Robotics Startup in $100 Million Round](https://www.bloomberg.com/news/articles/2026-01-29/fiat-toyota-tycoons-back-startup-robco-in-100-million-round)**

Bloomberg.com • 2d ago

---

**[Into the Omniverse: Physical AI Open Models and Frameworks Advance Robots and Autonomous Systems](https://blogs.nvidia.com/blog/physical-ai-open-models-robot-autonomous-systems-omniverse/)**

By providing access to critical infrastructure — from simulation frameworks to AI models — NVIDIA is enabling collaborative development that accelerates the path to safer, more capable autonomous systems.

NVIDIA Blog • 2d ago

---

**[Ondas' American Robotics Optimus Drone Approved for Rapid Federal Procurement via DCMA Blue UAS Cleared List](https://ir.ondas.com/press-releases/detail/275/ondas-american-robotics-optimus-drone-approved-for-rapid)**

Ondas Holdings • 3d ago

---

**[Tesla axes EV models in drive for robotics revenue](https://news.sky.com/story/tesla-axes-ev-models-in-drive-for-robotics-revenue-13500444)**

Investors liked what they heard about the future following the company's latest results, but Elon Musk is under huge pressure to deliver on his vision as a series of targets have been missed.

Sky News • 2d ago

---

**[New York Robotics launches with 160 startups in its ecosystem](https://www.therobotreport.com/new-york-robotics-launches-160-startups-ecosystem/)**

New York Robotics is launching with over 80 industry partners, 20 academic partners, 40 robotics labs, and over 300 venture capital partners.

The Robot Report • 1d ago

---

**[Guest article: What CES really told us about robotics in the produce sector](https://agfundernews.com/guest-article-what-ces-really-told-us-about-robotics-in-the-produce-sector)**

The best robots in agriculture are the ones growers stop talking about because they just work, said panelists at CES 2026.

AgFunderNews • 1d ago

---

---

## YouTube Videos: "robotics"

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 46K • 👍 768 • 💬 126 • ⏱️ 14:25 • 23h ago

---

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 74 • 👍 7 • 💬 1 • ⏱️ 1:21 • 2h ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 419K • 👍 4K • 💬 2K • ⏱️ 3:13 • 1d ago

---

**[Introducing Helix 02](https://www.youtube.com/watch?v=lQsvTrRTBRs)**

Last year, Helix showed that a single neural network could control a humanoid's upper body from pixels. Today, Helix 02 extends ...

📺 Figure

👁️ 207K • 👍 12K • 💬 2K • ⏱️ 3:37 • 4d ago

---

**[No, Elon, we DON&#39;T need HUMANOID robots | MGUY Australia](https://www.youtube.com/watch?v=GOjQYeF0OTI)**

The Cybertruck, autonomous driving and now the mad Optimus humanoid robot - three of Elon's mad inventions that the world ...

📺 MGUY Australia

👁️ 17K • 👍 2K • 💬 855 • ⏱️ 8:11 • 1d ago

---

**[Humanoid Robots Lumi and Luna A5 at 1000 Subscriber Celebration | Future Robot Lab](https://www.youtube.com/watch?v=FaL-UbIZFmM)**

We are honored to celebrate an important milestone at Future Robot Lab. This video captures the special moment when ...

📺 Future Robot Lab

👁️ 21K • 👍 256 • 💬 41 • ⏱️ 9:38 • 5d ago

---

**[Tesla Fremont factory ending Model S/X manufacturing to begin Optimus robot production](https://www.youtube.com/watch?v=liF86L_EvKQ)**

Andrea Nakano reports on the Tesla Fremont factory ending Model S/X production and using that part of the factory for mass ...

📺 KPIX | CBS NEWS BAY AREA

👁️ 62K • 👍 540 • 💬 324 • ⏱️ 4:36 • 2d ago

---

**[Robot That Grows Through Rubble To Find Survivors 🤖 #rescue #robotics #shorts](https://www.youtube.com/watch?v=haGH86W_f5A)**

The Growing Robot That Enters Collapsed Buildings Before Humans Do When disaster strikes and buildings collapse, reaching ...

📺 EcoZora

👁️ 366K • 👍 2K • 💬 152 • ⏱️ 0:07 • 5d ago

---

**[Tesla CEO Elon Musk doubles down on robots](https://www.youtube.com/watch?v=B78RNAlYXLA)**

Tesla's fourth quarter earnings topped analyst estimates. CEO Elon Musk is betting big on robotics and AI with plans to spend $20 ...

📺 Yahoo Finance

👁️ 13K • 👍 174 • 💬 47 • ⏱️ 12:20 • 1d ago

---

**[Humanoid Robots Are Coming. They Could Wipe Out This Entire Town](https://www.youtube.com/watch?v=6BJ0XbXOJcs)**

Hyundai is planning to place 30000 humanoid robots in its factories. We talked to an anonymous Hyundai worker who says his ...

📺 More Perfect Union

👁️ 190K • 👍 16K • 💬 2K • ⏱️ 2:59 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

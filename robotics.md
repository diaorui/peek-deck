---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-31T17:51:03.817266+00:00'
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

**Last Updated:** January 31, 2026 at 17:51 UTC  
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

7h ago

---

**[ICRA 2026 Acceptance Notification](https://www.reddit.com/r/robotics/comments/1qs19lr/icra_2026_acceptance_notification/)**

Has anyone already received a notification for their ICRA 2026 submission? As of January 31, 4 AM PST, my paper status is still “Decision Pending” rather than “Undisclosed.” Is this normal, or should it have updated by now?

5h ago

---

**[Probably the world's best beer delivery robot :-)](https://www.reddit.com/r/robotics/comments/1qryd3l/probably_the_worlds_best_beer_delivery_robot/)**

It was good, old Boxie 1. Now, there is Boxie 2: stronger, better, more capable ... but it is shy to deliver the beer :-)

7h ago

---

**[Pib-Roboter im Selbstbau.](https://www.reddit.com/r/robotics/comments/1qs0vjp/pibroboter_im_selbstbau/)**

Fast fertiggestellt. Nur noch die Servo Bricks mit Strom versorgen. Dann kann der erste Test starten. #insento Pib.rocks Einige hundert Stunden hat der 3D-Drucker gedruckt. Etwa 150 Teile. Dazu hunderte Schrauben und Muttern, Kugellager. MEhr als 20 Servomotoren, Raspi, Monitor, 360 Grad Mikroarray, Kamera mit Objekterkennung. Und viele Arbeitsstunden - ich bin mal gespannt, ob dann alles funktioniert.

5h ago

---

**[BUILDING DRONE WITH STM32F103C8T6](https://www.reddit.com/r/robotics/comments/1qs5gao/building_drone_with_stm32f103c8t6/)**

2h ago

---

**[ICRA 2026 review discussion](https://www.reddit.com/r/robotics/comments/1qs2thb/icra_2026_review_discussion/)**

I guess it’s time for a new thread to discuss ICRA 2026 review results. This is my first first author submission and really looking forward to it 🙏

4h ago

---

**[Using low-cost Android smartphones as embedded telematics gateways on forklifts – sane or bad idea?](https://www.reddit.com/r/robotics/comments/1qs047w/using_lowcost_android_smartphones_as_embedded/)**

I’m working on an industrial telematics system for a client who operates a fleet of electric forklifts . The proposed architecture is to mount a low-cost Android smartphone permanently on each forklift . Role of the Android phone: - Acts as the edge gateway - 4G connectivity to cloud - GPS positioning and speed estimation - Shock detection using accelerometer - Inclination (pitch/roll) using sensors - Driver identification using front camera (event-based face recognition) - Bluetooth (BLE) communication with an ESP32 that handles CAN bus + battery/current sensors Hardware constraints: - Low-end Android phones (≈3–4 GB RAM, quad-core CPU) - Continuous charging from forklift 24V - Industrial vibration environment - Android 11–14 range This is for a real client, not a hobby project. My questions to engineers who’ve done industrial / Android-at-the-edge systems: Is this architecture considered reasonable in production, or a maintenance nightmare long-term? What are the biggest failure modes you’ve seen when using Android phones as embedded gateways? Would you strongly recommend replacing the phone with a dedicated telematics box instead? Any hard lessons around Android background limits, BLE reliability, or sensor accuracy in vehicles? If you’ve shipped something similar, what would you do differently today? I’m intentionally not relying on OEM forklift firmware to keep the system brand-agnostic. Looking for honest, experience-based feedback positive or negative.

6h ago

---

**[Making a heavy DC motor platform safe: contactors, E-stop, and runaway prevention](https://www.reddit.com/r/robotics/comments/1qs7huf/making_a_heavy_dc_motor_platform_safe_contactors/)**

Hi, I’m working on a repurposed electric wheelchair chassis (>100 kg, high-torque DC motors). Current test setup (yes, I know it’s not safe): • 2 DC motors • Sabertooth 2x32 • 24 V battery pack (2×12 V AGM) • Batteries connected directly to the Sabertooth • Motors connected directly to the Sabertooth • Control is classic RC (throttle + steering) • Motors have normally-closed electromagnetic brakes, but they are not wired yet (mechanically released) Right now: • As soon as I connect the batteries, the controller is powered • There is no real kill switch • The only way to stop everything is unplugging battery connectors • If something goes wrong, the platform could move uncontrollably I’m fully aware this is not acceptable, which is why I’m posting. My goal is to make this safe in as many realistic failure scenarios as possible: • If the main battery disconnects on a slope, the system should default to a safe state (this is where normally-closed electromagnetic brakes make sense). • If RC glitches, is lost, or a microcontroller crashes, the platform must not run away. • Whatever fails (RC, MCU, software, power), there should always be a solid hardware-level barrier preventing uncontrolled motion. I’m planning a hardware upgrade soon: • proper E-STOP / kill switch • DC contactors • wiring the electromagnetic brakes • and adding some kind of MCU in the control chain (ESP32 is the obvious option for me, but Raspberry Pi / onboard computer is also possible) The Sabertooth will remain only the motor power controller. The open question for me is the architecture: whether it’s better to keep “safety/control” and “robotics/autonomy” separated (for example one small MCU for safety + another board for higher-level stuff), or if people commonly keep everything on one controller. What I’m looking for is very practical advice: • How to design a solid anti-runaway architecture for this kind of platform • Where to physically cut power to make the system safe (battery side vs motor lines) • What type of DC contactors is typically used for high-torque DC motors (ratings, poles, inductive loads) • How normally-closed electromagnetic brakes are usually wired in a fail-safe way • How people typically split responsibilities between hardware safety, motor controller config, and a microcontroller (one vs two controllers, etc.) I’m not chasing theory or certifications. I want proven, practical solutions that people actually use to make platforms like this safe to power on. Thanks.

57m ago

---

**[ICRA - ChatGPT Generated Rreviews?](https://www.reddit.com/r/robotics/comments/1qs7830/icra_chatgpt_generated_rreviews/)**

I just received the news that my ICRA submission was rejected. Which is fine. I never submitted with the expectation that it would get accepted but hoping that I would get some valuable feedback in the case of a rejection. Unfortunately this was not the case. The decision was made based on just two reviews. One of which was relatively neutral but seemingly written by someone who was not deeply familiar with the subject. Not a problem in itself but not a good basis for a decision in the case of only two reviews. The one that worries me more is the second review which in my opinion is likely written by ChatGPT or a similar LLM. I base this opinion on the way it is written going into unnecessary detail but also on the fact that most criticisms are just incorrect. Showing very limited understanding of the subject both in theoretical as well as in practical aspects as well as a lack of basic logic. This was my first time submitting to ICRA and if this is the kind of review quality to expect from a "top" conference it will also be the last time. It does not seem like a good conference unless you are doing mainstream research. I will include the review in question and invite anybody to read the preprint of my paper to form your own opinion. The preprint is identical to the version I submitted anonymization fron the double blind review. Modeling of UAV Tether Aerodynamics for Real-Time Simulation I would be happy about any feedback about my paper or your own experiences with ICRA and other "top" conferences. Following is the review. (Note when they talk about missing reference [?] this is due to the anonymization. I removed the citation when citing my own previous work) This paper addresses the important problem of modeling the tension forces and geometric shape of a tethered cable subjected to drag and wind forces, specifically within the context of drone tethering applications. The authors present a dual-solution approach: an analytical model based on the catenary equations, and a numerical solution derived using the IPOPT optimization solver within the CasADi framework. Despite the interesting and relevant application, the paper suffers from several major concerns that must be comprehensively addressed before publication. Major Comments: - Lack of Clarity and Novelty in Introduction The Introduction fails to clearly articulate the problem's relevance for tethered drone systems (e.g., increased energy consumption, system instability, or control degradation due to cable dynamics). This critical context is left for the reader to infer. More importantly, the authors do not explicitly define the novelty or scientific contribution of the proposed dual-solution approach over the existing state of the art. The introduction must clearly establish how this work advances previous research. - The State-of-the-Art section describes previous works but struggles to differentiate the current contribution. Solutions presented in references, such as [5] and [6], appear to address similar or potentially more complete aspects of the problem. The authors must rigorously specify what makes their approach unique and scientifically significant compared to these prior methods. Without this clarity, the paper's contribution remains ambiguous to the reader. - The Analytical Approach section, while well-explained, relies heavily on existing theory. However, the subsequent Numerical Solution section lacks sufficient justification for its necessity. Observing Figure 4, the analytical and numerical solutions for the cable shape are notably similar. Crucially, the paper does not provide a true ground truth or a comparative analysis (e.g., computational cost, convergence rate, robustness to highly non-ideal conditions) to argue for the superiority or necessity of the numerical optimization solver. The authors must explain the specific scenarios where the numerical approach offers a non-trivial advantage. - The real-world experiment, which aims to validate the proposed online estimation of cable shape and tension, highlights several critical issues: Redundancy: The numerical and analytical cable shape estimations appear to be almost overlapping, reinforcing the question regarding the necessity of the computationally intensive numerical approach. Inconsistency with Measurement: The force cell measurements diverge significantly from the results predicted by both the analytical and numerical models, suggesting a fundamental modeling or implementation flaw that must be investigated and corrected. Contradictory Assumption: The experimental section assumes zero wind, a highly restrictive and unrealistic simplification that directly contradicts the paper's central motivation presented in the Introduction ("...optimize the design, modeling, and control of drones tethered to a moving ground vehicle in real-world conditions like strong wind."). This assumption undermines the stated purpose and the validity of the drag modeling. Kinematic Error: The assumption that ground speed is equal to airspeed is fundamentally incorrect in real-world scenarios, where wind (a stated variable in the paper's premise) is a major differentiating factor. Minor Notes - Missing Reference: The phrase "In [?], we have looked at optimization of the tether parameters..." contains a placeholder. This reference should be corrected to: "In [Number], the authors..." to maintain academic style and anonymity during review. - Inappropriate Language: The sentence, "Besides the necessary interface changes, two new lines of code were added and two lines were adjusted, showing the flexibility of the approach," is more suitable for a technical report or implementation note. In a formal conference paper, this assertion should be replaced with a more rigorous, quantitative statement about the modularity and computational efficiency of the implementation. The core concept of modeling tether dynamics is valuable, but the current manuscript is incomplete and requires significant revision. The major issues stem from unvalidated model results, unjustified complexity of the numerical solution, and experimental assumptions that directly contradict the paper's stated goals regarding wind effects. The authors must provide stronger evidence of the scientific contribution and rigorously validate the models under the realistic conditions outlined in the introduction.

1h ago

---

**[How China’s Military Robots Learn From Animals](https://www.reddit.com/r/robotics/comments/1qs6qv7/how_chinas_military_robots_learn_from_animals/)**

https://www.wsj.com/tech/ai/how-chinas-military-robots-learn-from-animals-4fc0394b "After observing how hawks target their prey, engineers at one of China’s top military-linked universities trained defensive drones to single out and destroy vulnerable enemy aircraft. On the opposite side, these scientists used the flight behavior of doves to train the attacking drones how to dodge their hawk-trained adversaries... ...As drones have become cheaper and more capable, sci-fi visions of AI-powered robot armies clashing on the battlefield have inched closer to reality... ...Recent research into drone intelligence is yielding new algorithms modeled on the behavior of several animal groups—including ants, sheep, coyotes and whales—that could theoretically give drones rules for how to coordinate with one another. Few of these new algorithms have been tested in realistic battlefield scenarios."

1h ago

---

---

## Google News: "robotics"

**[Tesla lurches into the Musk robotics era](https://www.ft.com/content/6a6cfa00-6f51-4abc-bd68-1738580bd2c5)**

Future of the company lies in equipping and running a global fleet of driverless taxis and in selling humanoid robots

Financial Times • 2d ago

---

**[Tesla discontinues Model X and S vehicles as Elon Musk pivots to robotics](https://www.theguardian.com/technology/2026/jan/28/tesla-q4-earnings-estimates-elon-musk)**

Musk’s optimism for Optimus robot demand help EV maker beat quarterly expectations despite first-ever yearly revenue decline

The Guardian • 2d ago

---

**[Tesla doubles spending with $20B AI and robotics push](https://finance.yahoo.com/news/tesla-doubles-spending-20b-ai-161254007.html)**

Record investment marks a shift away from traditional EVs toward automation.

Yahoo Finance • 2d ago

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

**[Lake Stevens robotics team receives world recognition](https://www.heraldnet.com/news/lake-stevens-robotics-team-receives-world-recognition/)**

Team Arsenic took second place at the recent ROBO-BASH in Bellingham, earning fifth place in the world.

Everett Herald • 1d ago

---

**[Tesla axes EV models in drive for robotics revenue](https://news.sky.com/story/tesla-axes-ev-models-in-drive-for-robotics-revenue-13500444)**

Investors liked what they heard about the future following the company's latest results, but Elon Musk is under huge pressure to deliver on his vision as a series of targets have been missed.

Sky News • 2d ago

---

**[New York Robotics launches with 160 startups in its ecosystem](https://www.therobotreport.com/new-york-robotics-launches-160-startups-ecosystem/)**

New York Robotics is launching with over 80 industry partners, 20 academic partners, 40 robotics labs, and over 300 venture capital partners.

The Robot Report • 1d ago

---

**[The lonely promise of cute robots](https://www.theverge.com/column/870438/optimizer-mirumi-loneliness-social-companion-robots)**

Mirumi is adorably boring, unless you’re my cat.

The Verge • 1d ago

---

---

## YouTube Videos: "robotics"

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 32K • 👍 643 • 💬 88 • ⏱️ 14:25 • 18h ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 327K • 👍 4K • 💬 1K • ⏱️ 3:13 • 1d ago

---

**[The Next Robotics Boom Is Healthcare (3 Stocks to Watch)](https://www.youtube.com/watch?v=iMGDPSqvjiY)**

Robotics stocks are gaining attention as healthcare technology continues to evolve, and stock market investors are paying ...

📺 MarketBeat

👁️ 13K • 👍 562 • 💬 23 • ⏱️ 16:59 • 17h ago

---

**[No, Elon, we DON&#39;T need HUMANOID robots | MGUY Australia](https://www.youtube.com/watch?v=GOjQYeF0OTI)**

The Cybertruck, autonomous driving and now the mad Optimus humanoid robot - three of Elon's mad inventions that the world ...

📺 MGUY Australia

👁️ 16K • 👍 2K • 💬 840 • ⏱️ 8:11 • 1d ago

---

**[Robot that thinks 😳🤖Detects obstacles &amp; changes path automatically #roboarmy #arduinoprojects](https://www.youtube.com/watch?v=d_sDSfkI8ug)**

ObstacleAvoidance #ArduinoRobot #Robotics #TechReels #DIYProjects.

📺 Roboarmy

👁️ 9K • 👍 161 • 💬 1 • ⏱️ 0:20 • 1d ago

---

**[Humanoid Robots Are Coming. They Could Wipe Out This Entire Town](https://www.youtube.com/watch?v=6BJ0XbXOJcs)**

Hyundai is planning to place 30000 humanoid robots in its factories. We talked to an anonymous Hyundai worker who says his ...

📺 More Perfect Union

👁️ 190K • 👍 16K • 💬 2K • ⏱️ 2:59 • 4d ago

---

**[Pacman Universe – Advanced Robotic Character Animation | StrEat](https://www.youtube.com/watch?v=dm57WnYor00)**

Pacman Universe – Advanced Robotic Character Animation | StrEat Pacman Universe presents a new futuristic 3D animation.

📺 StrEat

👁️ 275K • 👍 553 • 4d ago

---

**[Why AI Pizza Machines Are Actually Worrying Workers 🍕](https://www.youtube.com/watch?v=U7tlOl7s3ns)**

Some people are getting concerned because automatic AI pizza-making machines are slowly appearing on streets worldwide.

📺 Taylor Jollie

👁️ 21K • 👍 115 • 💬 12 • ⏱️ 0:19 • 2d ago

---

**[Keep watching the robots](https://www.youtube.com/watch?v=bAYIW1aQ_c8)**

Keep watching the robots—because every day brings breakthrough moments that redefine what machines can do and what our ...

📺 Dark Waters

👁️ 249K • 👍 5K • 💬 572 • ⏱️ 0:23 • 1d ago

---

**[This robot hand is better than a human one](https://www.youtube.com/watch?v=4mNYTnM826k)**

📺 QCT

👁️ 9K • 👍 96 • 💬 9 • ⏱️ 0:22 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

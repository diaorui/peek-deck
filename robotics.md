---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-01T02:31:37.551918+00:00'
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

**Last Updated:** February 01, 2026 at 02:31 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Portable offline llm robot I made last night. This is obviously her naked prototype body so be nice to her](https://www.reddit.com/r/robotics/comments/1qsexfy/portable_offline_llm_robot_i_made_last_night_this/)**

The real meat and potatoes: I made this as a modular brain for my other robots I built recently. Right now I’m building her a tiny combat robot body so I can’t wait to program her fight moves. Already slightly tested it but just to get her to stand in a T pose then relax all motors after 5 seconds to get an idea of how to map her body. That was when I used a pi zero tho so more work is definitely needed. After that I need to completely redesign her casing. It’s literally made from an outer frame I printed in a rush and a piece of plastic that held her oled screen in the packaging.

4h ago

---

**[Making a heavy DC motor platform safe: contactors, E-stop, and runaway prevention](https://www.reddit.com/r/robotics/comments/1qs7huf/making_a_heavy_dc_motor_platform_safe_contactors/)**

Hi, I’m working on a repurposed electric wheelchair chassis (>100 kg, high-torque DC motors). Current test setup (yes, I know it’s not safe): • 2 DC motors • Sabertooth 2x32 • 24 V battery pack (2×12 V AGM) • Batteries connected directly to the Sabertooth • Motors connected directly to the Sabertooth • Control is classic RC (throttle + steering) • Motors have normally-closed electromagnetic brakes, but they are not wired yet (mechanically released) Right now: • As soon as I connect the batteries, the controller is powered • There is no real kill switch • The only way to stop everything is unplugging battery connectors • If something goes wrong, the platform could move uncontrollably I’m fully aware this is not acceptable, which is why I’m posting. My goal is to make this safe in as many realistic failure scenarios as possible: • If the main battery disconnects on a slope, the system should default to a safe state (this is where normally-closed electromagnetic brakes make sense). • If RC glitches, is lost, or a microcontroller crashes, the platform must not run away. • Whatever fails (RC, MCU, software, power), there should always be a solid hardware-level barrier preventing uncontrolled motion. I’m planning a hardware upgrade soon: • proper E-STOP / kill switch • DC contactors • wiring the electromagnetic brakes • and adding some kind of MCU in the control chain (ESP32 is the obvious option for me, but Raspberry Pi / onboard computer is also possible) The Sabertooth will remain only the motor power controller. The open question for me is the architecture: whether it’s better to keep “safety/control” and “robotics/autonomy” separated (for example one small MCU for safety + another board for higher-level stuff), or if people commonly keep everything on one controller. What I’m looking for is very practical advice: • How to design a solid anti-runaway architecture for this kind of platform • Where to physically cut power to make the system safe (battery side vs motor lines) • What type of DC contactors is typically used for high-torque DC motors (ratings, poles, inductive loads) • How normally-closed electromagnetic brakes are usually wired in a fail-safe way • How people typically split responsibilities between hardware safety, motor controller config, and a microcontroller (one vs two controllers, etc.) I’m not chasing theory or certifications. I want proven, practical solutions that people actually use to make platforms like this safe to power on. Thanks.

9h ago

---

**[XPENG IRON first public appearance since its release last November](https://www.reddit.com/r/robotics/comments/1qryyxx/xpeng_iron_first_public_appearance_since_its/)**

From: CyberRobo on 𝕏: https://x.com/CyberRobooo/status/2017544750694551618 RoboHub🤖 on 𝕏 (images): https://x.com/XRoboHub/status/2017541654173851909

16h ago

---

**[Building a cute little AI Robot with memory -Kuchi 😁](https://www.reddit.com/r/robotics/comments/1qsb4kp/building_a_cute_little_ai_robot_with_memory_kuchi/)**

Day:30 1- Base body and MCU from Sunfounder 2-Built over raspberry pi5 and powered by OpenAI 3- Connected to N8N for tooling like web search., scraping etc Let me know your thoughts 😊

7h ago

---

**[Why is it secretly flipping me off?](https://www.reddit.com/r/robotics/comments/1qslo30/why_is_it_secretly_flipping_me_off/)**

Saw this one at Wuhu train station in China. Answers questions at a desk. It looks like it has a lot of ability but it otherwise doesn't move at all. Even when you ask it to wave it says "sure, here's a friendly wave" but doesn't move an inch.

17m ago

---

**[Pib-Roboter im Selbstbau.](https://www.reddit.com/r/robotics/comments/1qs0vjp/pibroboter_im_selbstbau/)**

Fast fertiggestellt. Nur noch die Servo Bricks mit Strom versorgen. Dann kann der erste Test starten. #insento Pib.rocks Einige hundert Stunden hat der 3D-Drucker gedruckt. Etwa 150 Teile. Dazu hunderte Schrauben und Muttern, Kugellager. MEhr als 20 Servomotoren, Raspi, Monitor, 360 Grad Mikroarray, Kamera mit Objekterkennung. Und viele Arbeitsstunden - ich bin mal gespannt, ob dann alles funktioniert.

14h ago

---

**[ICRA 2026 Acceptance Notification](https://www.reddit.com/r/robotics/comments/1qs19lr/icra_2026_acceptance_notification/)**

Has anyone already received a notification for their ICRA 2026 submission? As of January 31, 4 AM PST, my paper status is still “Decision Pending” rather than “Undisclosed.” Is this normal, or should it have updated by now?

13h ago

---

**[ICRA - ChatGPT Generated Rreviews?](https://www.reddit.com/r/robotics/comments/1qs7830/icra_chatgpt_generated_rreviews/)**

I just received the news that my ICRA submission was rejected. Which is fine. I never submitted with the expectation that it would get accepted but hoping that I would get some valuable feedback in the case of a rejection. Unfortunately this was not the case. The decision was made based on just two reviews. One of which was relatively neutral but seemingly written by someone who was not deeply familiar with the subject. Not a problem in itself but not a good basis for a decision in the case of only two reviews. The one that worries me more is the second review which in my opinion is likely written by ChatGPT or a similar LLM. I base this opinion on the way it is written going into unnecessary detail but also on the fact that most criticisms are just incorrect. Showing very limited understanding of the subject both in theoretical as well as in practical aspects as well as a lack of basic logic. This was my first time submitting to ICRA and if this is the kind of review quality to expect from a "top" conference it will also be the last time. It does not seem like a good conference unless you are doing mainstream research. I will include the review in question and invite anybody to read the preprint of my paper to form your own opinion. The preprint is identical to the version I submitted anonymization fron the double blind review. Modeling of UAV Tether Aerodynamics for Real-Time Simulation I would be happy about any feedback about my paper or your own experiences with ICRA and other "top" conferences. Following is the review. (Note when they talk about missing reference [?] this is due to the anonymization. I removed the citation when citing my own previous work) This paper addresses the important problem of modeling the tension forces and geometric shape of a tethered cable subjected to drag and wind forces, specifically within the context of drone tethering applications. The authors present a dual-solution approach: an analytical model based on the catenary equations, and a numerical solution derived using the IPOPT optimization solver within the CasADi framework. Despite the interesting and relevant application, the paper suffers from several major concerns that must be comprehensively addressed before publication. Major Comments: - Lack of Clarity and Novelty in Introduction The Introduction fails to clearly articulate the problem's relevance for tethered drone systems (e.g., increased energy consumption, system instability, or control degradation due to cable dynamics). This critical context is left for the reader to infer. More importantly, the authors do not explicitly define the novelty or scientific contribution of the proposed dual-solution approach over the existing state of the art. The introduction must clearly establish how this work advances previous research. - The State-of-the-Art section describes previous works but struggles to differentiate the current contribution. Solutions presented in references, such as [5] and [6], appear to address similar or potentially more complete aspects of the problem. The authors must rigorously specify what makes their approach unique and scientifically significant compared to these prior methods. Without this clarity, the paper's contribution remains ambiguous to the reader. - The Analytical Approach section, while well-explained, relies heavily on existing theory. However, the subsequent Numerical Solution section lacks sufficient justification for its necessity. Observing Figure 4, the analytical and numerical solutions for the cable shape are notably similar. Crucially, the paper does not provide a true ground truth or a comparative analysis (e.g., computational cost, convergence rate, robustness to highly non-ideal conditions) to argue for the superiority or necessity of the numerical optimization solver. The authors must explain the specific scenarios where the numerical approach offers a non-trivial advantage. - The real-world experiment, which aims to validate the proposed online estimation of cable shape and tension, highlights several critical issues: Redundancy: The numerical and analytical cable shape estimations appear to be almost overlapping, reinforcing the question regarding the necessity of the computationally intensive numerical approach. Inconsistency with Measurement: The force cell measurements diverge significantly from the results predicted by both the analytical and numerical models, suggesting a fundamental modeling or implementation flaw that must be investigated and corrected. Contradictory Assumption: The experimental section assumes zero wind, a highly restrictive and unrealistic simplification that directly contradicts the paper's central motivation presented in the Introduction ("...optimize the design, modeling, and control of drones tethered to a moving ground vehicle in real-world conditions like strong wind."). This assumption undermines the stated purpose and the validity of the drag modeling. Kinematic Error: The assumption that ground speed is equal to airspeed is fundamentally incorrect in real-world scenarios, where wind (a stated variable in the paper's premise) is a major differentiating factor. Minor Notes - Missing Reference: The phrase "In [?], we have looked at optimization of the tether parameters..." contains a placeholder. This reference should be corrected to: "In [Number], the authors..." to maintain academic style and anonymity during review. - Inappropriate Language: The sentence, "Besides the necessary interface changes, two new lines of code were added and two lines were adjusted, showing the flexibility of the approach," is more suitable for a technical report or implementation note. In a formal conference paper, this assertion should be replaced with a more rigorous, quantitative statement about the modularity and computational efficiency of the implementation. The core concept of modeling tether dynamics is valuable, but the current manuscript is incomplete and requires significant revision. The major issues stem from unvalidated model results, unjustified complexity of the numerical solution, and experimental assumptions that directly contradict the paper's stated goals regarding wind effects. The authors must provide stronger evidence of the scientific contribution and rigorously validate the models under the realistic conditions outlined in the introduction.

9h ago

---

**[First rover build! Resurrected my dad's 5yr old kits and scraps to make this little guy](https://www.reddit.com/r/robotics/comments/1qsjqlz/first_rover_build_resurrected_my_dads_5yr_old/)**

First time posting here! Ive been messing around with my dad’s scraps for a while, but finally found a rover kit! I built this chassis using a mix of 5-year-old kits and random scraps I had lying around. It was a late night, but getting an actual chassis/frame plus the wiring to work felt amazing. Really really simple build, put it together via an old ESP 32, ( after many cable, Bluetooth pairing, and firmware hassles ) archaic L298N motor driver, and for battery a basic series circuit to up the voltage ( don’t even have batteries sitting haha) I’ve been learning a ton from Practical Electronics for Inventors and The Art of Electronics, but I'm looking for what to tackle next. I’d love to hear your suggestions for: Books that bridge mechanical engineering and embedded systems. Courses on more advanced control (maybe leading into ROS 2?). I’ve played around built software applications with agentic workflows and played around w yolov8 as well. But definitely need more resources on robotics + AI. Let me know if you guys have any tips!!

1h ago

---

**[Probably the world's best beer delivery robot :-)](https://www.reddit.com/r/robotics/comments/1qryd3l/probably_the_worlds_best_beer_delivery_robot/)**

It was good, old Boxie 1. Now, there is Boxie 2: stronger, better, more capable ... but it is shy to deliver the beer :-)

16h ago

---

---

## Google News: "robotics"

**[Lightspeed Backs Robotics Startup in $100 Million Round](https://www.bloomberg.com/news/articles/2026-01-29/fiat-toyota-tycoons-back-startup-robco-in-100-million-round)**

Bloomberg.com • 2d ago

---

**[Lake Stevens robotics team receives world recognition](https://www.heraldnet.com/news/lake-stevens-robotics-team-receives-world-recognition/)**

Team Arsenic took second place at the recent ROBO-BASH in Bellingham, earning fifth place in the world.

Everett Herald • 1d ago

---

**[Into the Omniverse: Physical AI Open Models and Frameworks Advance Robots and Autonomous Systems](https://blogs.nvidia.com/blog/physical-ai-open-models-robot-autonomous-systems-omniverse/)**

By providing access to critical infrastructure — from simulation frameworks to AI models — NVIDIA is enabling collaborative development that accelerates the path to safer, more capable autonomous systems.

NVIDIA Blog • 2d ago

---

**[Tesla lurches into the Musk robotics era](https://www.ft.com/content/6a6cfa00-6f51-4abc-bd68-1738580bd2c5)**

Future of the company lies in equipping and running a global fleet of driverless taxis and in selling humanoid robots

Financial Times • 2d ago

---

**[Tesla cuts car models in shift to robots and AI](https://www.bbc.com/news/articles/c620177qdg5o)**

Multi-billionaire Elon Musk also announced plans to end production of its Model S and Model X vehicles.

BBC • 2d ago

---

**[Tesla kills Models S and X to build humanoid robots instead](https://arstechnica.com/cars/2026/01/tesla-kills-models-s-and-x-to-build-humanoid-robots-instead/)**

EVs that were once industry-leading have long since been left behind.

Ars Technica • 2d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.nbcnews.com/video/china-rolls-out-robot-cops-in-cities-to-push-humanoid-robots-in-daily-life-256872517804)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News’ Janis Mackey Frayer explains how China continues to advance robot technology and is pushing to integrate humanoid robots into daily life.

NBC News • 1d ago

---

**[New York Robotics launches with 160 startups in its ecosystem](https://www.therobotreport.com/new-york-robotics-launches-160-startups-ecosystem/)**

New York Robotics is launching with over 80 industry partners, 20 academic partners, 40 robotics labs, and over 300 venture capital partners.

The Robot Report • 1d ago

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

👁️ 1K • 👍 31 • 💬 7 • ⏱️ 1:21 • 6h ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 61K • 👍 885 • 💬 192 • ⏱️ 14:25 • 1d ago

---

**[Most Lifelike Robot Yet? #robots #robotics #humanoidrobot #airobot #technology](https://www.youtube.com/watch?v=A22D5SBL8ig)**

Did China just develop the world's most realistic android yet? The Shanghai-based startup DroidUp just introduced its first ...

📺 Kalil 4.0

👁️ 3K • 👍 99 • 💬 14 • ⏱️ 0:48 • 7h ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 528K • 👍 5K • 💬 2K • ⏱️ 3:13 • 1d ago

---

**[SaaS is over… Why you should build a robotics company in 2026](https://www.youtube.com/watch?v=FqfTQFuSalY)**

2026 will be the year of robotics. We're in an Will Smith spaghetti moment. Remember how AI-generated video looked horrific two ...

📺 Andreas Klinger ⅹ Europe's Most Ambitious Startups

👁️ 27K • 👍 2K • 💬 205 • ⏱️ 16:46 • 5d ago

---

**[Elon Musk: Why AI and Robotics are the End of Money](https://www.youtube.com/watch?v=YOyXh6b3D9c)**

Is money a permanent fixture of humanity, or just a temporary tool for labor allocation? Elon Musk explains why the rise of AI and ...

📺 SpaceTakers

👁️ 15K • 👍 574 • 💬 25 • ⏱️ 0:59 • 3d ago

---

**[Introducing Helix 02](https://www.youtube.com/watch?v=lQsvTrRTBRs)**

Last year, Helix showed that a single neural network could control a humanoid's upper body from pixels. Today, Helix 02 extends ...

📺 Figure

👁️ 206K • 👍 12K • 💬 2K • ⏱️ 3:37 • 4d ago

---

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 289K • 💬 153 • ⏱️ 0:18 • 6d ago

---

**[Tesla bets big on robotics](https://www.youtube.com/watch?v=yEAf1Mw0qYk)**

Steve Westly, former Tesla board member and founder of the Westly Group, joins 'Squawk on the Street' to discuss Tesla's latest ...

📺 CNBC Television

👁️ 11K • 👍 82 • 💬 79 • ⏱️ 3:43 • 2d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=b8vufpXa21Q)**

📺 Borunte Robot Lin 

👁️ 5K • 👍 27 • ⏱️ 0:22 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

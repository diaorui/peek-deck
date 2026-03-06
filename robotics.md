---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-06T16:42:56.126337+00:00'
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

**Last Updated:** March 06, 2026 at 16:42 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[My robotics arm object grasping project !](https://www.reddit.com/r/robotics/comments/1rmh1vw/my_robotics_arm_object_grasping_project/)**

I have finished my robotics arm object grasping project ! Initially , I want to make a depth camera by myself for loss cost , but it ' s too difficult for me . I have tested several camera , I finded P008G is great for it ' s highly accurate depth data . I did a great job !

1h ago

---

**[HexGrip V1.0: Designing a 3-DOF Omni-Wrist. From "Block of Plastic" to "Fluid Motion"](https://www.reddit.com/r/robotics/comments/1rm93wd/hexgrip_v10_designing_a_3dof_omniwrist_from_block/)**

Update on my 6-DOF desktop arm project: I’ve officially moved into the mechanical prototyping phase, starting with the most complex hurdle—the Wrist. The goal was to pack 3 degrees of freedom into a compact volume while keeping everything 3D printable. I modeled an Omni-Wrist mechanism in OnShape with “perfect” dimensions, using a series of butt-hinge linkages with 3D-printed pins. On-screen, the digital assembly worked flawlessly, but reality hit hard. The Fail: My first print had zero play. While "zero-clearance" sounds great in CAD, filament expansion turned the whole assembly into a static paperweight. The tolerances were too tight, the hinges seized, and the pins were impossible to seat without snapping the linkages. The Pivot: I went back to the "Model-Print-Iterate" cycle. I increased the clearances to 0.2mm and redesigned the pivot points as snap-fit pins. This allows the linkages to stay secure under pressure while maintaining enough "fluidity" for manual movement. The Query: For those who build small-scale linkages: Pin Durability: Do 3D-printed pins actually hold up under the repetitive stress of a 6-DOF arm, or is it a fool's errand? Should I move to metal dowel pins now before I build the rest of the arm? Hinge Alternatives: Given the friction issues with 3D-printed butt hinges, is there a more efficient hinge style or linkage structure you'd recommend for a 3-DOF wrist that is easier to assemble and maintain?

7h ago

---

**[I’ve open-sourced my robots!](https://www.reddit.com/r/robotics/comments/1rll5z2/ive_opensourced_my_robots/)**

1d ago

---

**[What’s the point of making robots human-shaped?](https://www.reddit.com/r/robotics/comments/1rma1gq/whats_the_point_of_making_robots_humanshaped/)**

From an engineering perspective, wouldn’t other designs—like cantilever-type or hemispherical robots—be more practical and efficient for most real-world applications? Human-shaped robots seem mechanically complex, expensive, and often less stable compared to simpler structures. So is the humanoid form mainly for environments designed for humans, or is it more about research, marketing, and public perception?

6h ago

---

**[I got frustrated missing robotics deployments and layoffs, so I wrote a flightradar24-style autonomous NLP scraper to track the industry globally](https://www.reddit.com/r/robotics/comments/1rmdrlj/i_got_frustrated_missing_robotics_deployments_and/)**

As someone who follows the robotics industry closely, tracking company-level signals manually was impossible. I started building this as a personal tool and eventually put it online. How the engine works: A Python scraper hits multiple major robotics/AV newswires every 30 minutes via a systemd timer. Each headline is deduplicated and run through an NLP classification layer that categorises signals into four types: Deployments, Financials, Layoffs, and Leadership changes. roboradar24

3h ago

---

**[Bimo can walk on a carpet now!](https://www.reddit.com/r/robotics/comments/1rlkvpj/bimo_can_walk_on_a_carpet_now/)**

For those following the project, this is Bimo walking on a regular carpet, something that used to be very unreliable without hand-tuning the environment or the RL model. Over the last months I’ve retrained and tweaked the walking model so it’s much more robust: it now keeps a stable heading instead of drifting or turning, and it tolerates uneven contact and small disturbances much better than before. Next on the roadmap are behaviors such as: turning gaits, better recovery under sustained pushes, and more pre-programmed motions to make Bimo a practical research and tinkering platform rather than just a locomotion demo. As these stabilize, I’ll be adding them to the open-source GitHub repo and documenting them in the Discord so others can build on top of this. If you want to see the full kit and platform details, there’s also a page on the Mekion site with specs and pre-order info.

1d ago

---

**[Crossroads In Robotics Career](https://www.reddit.com/r/robotics/comments/1rlw8ja/crossroads_in_robotics_career/)**

I have been a robotics engineer all my life, worked 3 years full-time and am about to graduate from Carnegie Mellon with a masters degree in Robotics in May. I've been offered a position at Apple (camera modules) to help build smart front cameras. But, it doesn't involve robotics hardware - think of it as ML-based CV on edge at scale. Over my masters degree, I've built a keen interest in RL and autonomy in robotics; I am afraid I will lose touch and fall behind this domain that's poised to explode. On the flip side, there's the uncertainty in the job market for engineers at my level and all the pros that come with working at Apple. If you were in my shoes, how would you navigate this situation? Happy to provide any clarifications needed.

18h ago

---

**[Xiaomi Shows Humanoid Robots Working Autonomously on Production Lines with 90.2% Success Rate](https://www.reddit.com/r/robotics/comments/1rmixa6/xiaomi_shows_humanoid_robots_working_autonomously/)**

3m ago

---

**[DIY BLDC motor problem](https://www.reddit.com/r/robotics/comments/1rlwwnm/diy_bldc_motor_problem/)**

Hey guys, so I'm trying to make a custom bldc motor for a future quadroped robot project. My design has 18 coils and 20 magnets in the stator and the rotor. I used 0.5mm copper wire for the coils and 10x5x2mm magnets for the rotor. For the ESC I'm using the 40A brushless motor esc with a 3S lipo battery. The stator's inner diameter is roughly 80 mm and outer diameter is around 100mm. However after assembling the motor and plugging it into the ESC the coils had extremely low pull force (it can barely move a single magnet) . What could be the issue here? I've tried rewiring the coils but it didn't change anything. All of the coils are wired clockwise with the ends of each phase soldered together. Also do you have any tips on how to make a motor that has more torque? What I'm aiming for is 12 Nm

17h ago

---

**[Hyundai Mobis In-Wheel Motor System used in an Unmanned Firefighting Robot](https://www.reddit.com/r/robotics/comments/1rlmwhj/hyundai_mobis_inwheel_motor_system_used_in_an/)**

At the core of the Unmanned Firefighting Robot is a compact 6×6 in-wheel motor system that integrates drive, braking, and steering within each wheel unit.

23h ago

---

---

## Google News: "robotics"

**[Amazon cuts jobs in robotics unit as layoffs continue: report](https://www.foxbusiness.com/technology/amazon-cuts-jobs-robotics-unit-layoffs-continue)**

Amazon cut at least 100 positions in its robotics unit, continuing a sweeping corporate downsizing tied to artificial intelligence efficiencies and cost controls.

Fox Business • 22h ago

---

**[Amazon cuts more jobs; this time in robotics unit](https://www.reuters.com/business/world-at-work/amazon-cuts-more-jobs-this-time-robotics-unit-2026-03-04/)**

Reuters • 1d ago

---

**[Amazon Quietly Abandoned Its Robot Innovation](https://www.bgr.com/2112422/amazon-abandons-warehouse-robot-blue-jay/)**

Amazon recently abandoned an innovative robotic line that it had deployed last year in an effort to streamline some of its warehouse operations.

bgr.com • 18h ago

---

**[Neura Robotics Raising €1 Billion in Round Backed by Tether](https://www.bloomberg.com/news/articles/2026-03-04/neura-robotics-raising-1-billion-in-round-backed-by-tether)**

Bloomberg.com • 2d ago

---

**[E-bike starts fire at Yale University's robotics lab on Hillhouse Avenue, New Haven official says](https://www.nhregister.com/news/article/new-haven-hillhouse-ave-yale-lab-e-bike-fire-21957068.php)**

New Haven Register • 1d ago

---

**[Prediction: AI Robotics Will Be a $375 Billion Industry. This Stock Is Positioned to Win in 2026.](https://www.fool.com/investing/2026/03/05/prediction-ai-robotics-will-be-a-375-billion-indus/)**

When all is said and done, practicality trumps technological "wow!"

The Motley Fool • 13h ago

---

**[Graphene-based 'artificial skin' brings human-like touch closer to robots](https://techxplore.com/news/2026-03-graphene-based-artificial-skin-human.html)**

Tech Xplore • 23h ago

---

**[Compostable soft robots for plant monitoring](https://www.nature.com/articles/s41893-025-01757-9)**

Soft robots inspired by living organisms hold the promise of gentle, adaptable interactions with the natural world, but leave behind persistent waste. Now scientists show a fully compostable robotic system that addresses this limitation by offering durable performance and decomposing safely into the soil at the end of its life.

Nature • 1d ago

---

**[Xiaomi trials humanoid robots in its EV factory — says they're like 'interns'](https://www.cnbc.com/2026/03/04/xiaomi-humanoid-robots-ev-factory-.html)**

Two humanoid robots can complete 90% of the work in three hours, Xiaomi President Lu Weibing told CNBC.

CNBC • 2d ago

---

**[Bellefontaine Robotics teams pass with flying colors at championship](https://www.peakofohio.com/local-news/bellefontaine-robotics-teams-pass-with-flying-colors-at-championship/)**

Two robotics teams from Bellefontaine Middle School delivered strong performances at the Ohio State VEX Championship, with one team securing a coveted spot at the […]

Peak of Ohio • 7h ago

---

---

## YouTube Videos: "robotics"

**[Unrestricted AI in a robot does exactly what experts warned](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

AI robot. ChatGPT in Robot. Could AI become dangerous? Can we trust AI? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 343K • 👍 24K • 💬 3K • ⏱️ 16:54 • 2d ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=7I-KWkV0JUM)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN

👁️ 13K • 👍 311 • 💬 27 • ⏱️ 29:41 • 16h ago

---

**[Shocking Light-Powered Robot Runs Without Batteries &amp; Cyborg Cockroach](https://www.youtube.com/watch?v=2_igeW1d8RA)**

Robotics just entered a very strange new phase. Scientists built a tiny robot that runs purely on light with no batteries, processors, ...

📺 AI Revolution

👁️ 17K • 👍 686 • 💬 49 • ⏱️ 14:35 • 1d ago

---

**[This Robot &amp; Elon Musk Dance Broke the Internet 🕺🔥#ElonMusk #Tesla #Optimus #TeslaBot #Robotics](https://www.youtube.com/watch?v=EnduYx4nguI)**

A moment like this perfectly captures how technology can be both revolutionary and entertaining at the same time. Watching Elon ...

📺 Billionaire Shots

👁️ 34K • 👍 2K • 💬 242 • ⏱️ 0:13 • 2d ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=sFFMMg2XWyQ)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN Europe

👁️ 249K • 👍 421 • 💬 7 • ⏱️ 29:40 • 2d ago

---

**[Motor Gearbox on a Servo | 26949 Royal Society of Robotics | FTC Snapshot](https://www.youtube.com/watch?v=G0jAlOgIxMA)**

26949 Royal Society of Robotics | FTC Snapshot Oklahoma's 26949 Royal Society of Robotics, a Worlds bound team, showcases ...

📺 FUN Robotics Network

👁️ 5K • 👍 132 • ⏱️ 1:06 • 1d ago

---

**[Joe Rogan Is Worried About Robot Eyes](https://www.youtube.com/watch?v=Sqv1fuF9r0w)**

📺 DATARK

👁️ 30K • 👍 413 • 💬 4 • ⏱️ 0:25 • 1d ago

---

**[Japan&#39;s Most Famous Android Builder Finds His Robot Legs in China #humanoidrobots #robotics #robots](https://www.youtube.com/watch?v=xqMWtcsLyYc)**

Japan's Most Famous Android Builder Just Found His Robot Legs in China The Japanese robotics legend Hiroshi Ishiguro is ...

📺 Kalil 4.0

👁️ 828 • 👍 22 • 💬 1 • ⏱️ 1:08 • 20h ago

---

**[Quickest Intake in DECODE? | 3565 Ghost Robotics | FTC Snapshot](https://www.youtube.com/watch?v=ex9anz-_BCs)**

Currently ranked 10th in the world, 3565 Ghost Robotics showcases one of the fastest compliant intakes in FTC DECODE.

📺 FUN Robotics Network

👁️ 5K • 👍 91 • 💬 1 • ⏱️ 1:11 • 2d ago

---

**[China&#39;s Xiaomi Just DESTROYED Apple and Tesla in the Humanoid Robot Race](https://www.youtube.com/watch?v=Iw1JMO4mqZg)**

China's biggest consumer tech companies are entering the humanoid robot race. Companies like Xiaomi and Honor Device Co., ...

📺 Kalil 4.0

👁️ 609 • 👍 19 • 💬 3 • ⏱️ 7:17 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

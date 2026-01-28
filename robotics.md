---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-28T23:29:42.833743+00:00'
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

**Last Updated:** January 28, 2026 at 23:29 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Dexterous robotic hands: 2009 - 2014 - 2025](https://www.reddit.com/r/robotics/comments/1qp7z15/dexterous_robotic_hands_2009_2014_2025/)**

12h ago

---

**[Figure 03 handling glassware, fully autonomous](https://www.reddit.com/r/robotics/comments/1qpn1dq/figure_03_handling_glassware_fully_autonomous/)**

2h ago

---

**[Feedback on Our Open-Source Animatronics DIY Set!](https://www.reddit.com/r/robotics/comments/1qpalpq/feedback_on_our_opensource_animatronics_diy_set/)**

We are building a 3d-printable animatronics robots, Mostly the same 3d printed parts lets you assemble different animal robots, and we are trying to make it on the cheapest way possible (less than $50 is the target). Current list: Robotic dog Spider Robotic arm So far 300 people downloaded it from GrabCAD and Instructables, Got some positive feedbacks. And feedbacks to making the walking more smoother(Planning to add spring and weights) and assembly a bit easier(Planning for a snap fit). Why this post? We are currently working on the V2 of it, We are trying to put the design Infront of as many peoples and get their thoughts, ideas for new animals, making existing much better. Will appreciate any inputs. Link for files : https://grabcad.com/library/diy-robotic-dog-1 Assembly : https://www.instructables.com/Trix/ Reposting it here, Haven't got any replies last time 💀

10h ago

---

**[Who needs a lab? 17yo coding an autonomous interceptor drone system using ROS and OpenCV in his bedroom.](https://www.reddit.com/r/robotics/comments/1qppmc7/who_needs_a_lab_17yo_coding_an_autonomous/)**

I recently came across the work of a 17-year-old developer named Alperen, who is building something truly remarkable in his bedroom. Due to privacy concerns and the sensitive nature of the tech, he prefers to keep his face hidden, but his work speaks for itself. While most people are familiar with basic 2D object tracking seen in simple MP4 video tutorials, Alperen has taken it to a professional defense-grade level. Using ROS (Robot Operating System) and OpenCV within the Gazebo simulation environment, he has developed a system that calculates real-time 3D depth and spatial coordinates. This isn't just following pixels; it’s an active interceptor logic where the drone dynamically adjusts its velocity, altitude, and trajectory to maintain a precise lock on its target. It is fascinating to see such high-level autonomous flight control and computer vision being pioneered on a home PC by someone so young. This project demonstrates how the gap between hobbyist coding and sophisticated defense technology is rapidly closing through open-source tools and pure talent.

1h ago

---

**[Centimeter-Accurate Indoor Tracking for Swarming Drones Using Ultrasound ToF](https://www.reddit.com/r/robotics/comments/1qp5kc4/centimeteraccurate_indoor_tracking_for_swarming/)**

3 x Super-Beacons as stationary beacons for precise 3D indoor positioning 1 x (Mini-RX + External Microphone + Deflector) as a mobile beacon for the drone 1 x Modem v5.1 as a central controller This is not an autonomous flight - the drone was remotely controlled. But it shows precise indoor 3D tracking capabilities for swarming drones.

15h ago

---

**[iRobot cofounder on robotics as a toolkit, not a single destination](https://www.reddit.com/r/robotics/comments/1qpg3sr/irobot_cofounder_on_robotics_as_a_toolkit_not_a/)**

Former iRobot CEO Colin Angle talks about how robotics isn’t really a single “thing,” and that defaulting to humanoids as the mental model ends up flattening what’s actually going on in the field. He ties it back to his time at iRobot and how a lot of success or failure came down to very specific questions about value and trust, not form factor. Amazon attempted to acquire the declining company from bankruptcy but after an 18-month process the deal fell through. Angle is now with another company.

7h ago

---

**[We built humanoid legs from scratch in 100 days](https://www.reddit.com/r/robotics/comments/1qp85l2/we_built_humanoid_legs_from_scratch_in_100_days/)**

Hi, it's Emre from the Asimov team. I've been sharing our daily humanoid progress here, and thanks for your support along the way! We've open-sourced the leg design with CAD files, actuator list, and XML files for simulation. Now we're sharing a writeup on how we built it. Quick intro: Asimov is an open-source humanoid robot. We only have legs right now and are planning to finalize the full body by March 2026. It's going to be modular, so you can build the parts you need. Selling the robot isn't our priority right now. https://preview.redd.it/ljxqu6pdk2gg1.png?width=2000&format=png&auto=webp&s=71c244fb3cfc31cd5a768b7b1488babd8e04dcc0 Each leg has 6 DOF. The complete legs subsystem costs just over $10k, roughly $8.5k for actuators and joint parts, the rest for batteries and control modules. We designed for modularity and low-volume manufacturing. Most structural parts are compatible with MJF 3D printing. The only CNC requirement is the knee plate, which we simplified from a two-part assembly to a single plate. Actuators & Motors list and design files: https://github.com/asimovinc/asimov-v0 https://preview.redd.it/zalsj3eik2gg1.png?width=1200&format=png&auto=webp&s=734adca3a9d1c928acbf75cd95e44c3d4640ed93 We chose a parallel RSU ankle rather than a simple serial ankle. RSU gives us two-DOF ankles with both roll and pitch. Torque sharing between two motors means we can place heavy components closer to the hip, which improves rigidity and backdrivability. Linear actuators would have been another option, higher strength, more tendon-like look, but slower and more expensive. We added a toe joint that's articulated but not actuated. During push-off, the toe rocker helps the foot roll instead of pivoting on a rigid edge. Better traction, better forward propulsion, without adding another powered joint. https://preview.redd.it/skiqez2gk2gg1.png?width=1200&format=png&auto=webp&s=59d8951c9d20d2a10f547879a346c65e5b2e0bcf Our initial hip-pitch actuator was mounted at 45 degrees. This limited hip flexion and made sitting impossible. We're moving to a horizontal mount to recover range of motion. We're also upgrading ankle pivot components from aluminum to steel, and tightening manufacturing tolerances after missing some holes in early builds. https://preview.redd.it/o5wrtthkk2gg1.png?width=1200&format=png&auto=webp&s=5bebbe9c662e8e0a15ac6ea6b788530d0d1d66fd Next up is the upper body. We're working on arms and torso in parallel, targeting full-body integration by March. The complete robot will have 26 DOF and come in under 40kg. Sneak industrial design render of complete Asimov humanoid. Full writeup with diagrams and specs here: https://news.asimov.inc/p/how-we-built-humanoid-legs-from-the

12h ago

---

**[Sprout robot from Fauna Robotics](https://www.reddit.com/r/robotics/comments/1qoio9e/sprout_robot_from_fauna_robotics/)**

Hey all, a quick showcase of the Sprout robot from Fauna Robotics. I’m a postdoc in Talmo Pereira’s lab at the Salk Institute working on computational models for motor control. In my experience, robots usually take weeks or months of network, hardware, and software debugging before you can even start experiments. This was the opposite. We turned it on and were up and running immediately, which made me appreciate how much legwork must’ve gone into making the setup so smooth. So far we’ve: - Got Sprout walking, crouching, crawling, dancing and even jumping. - The robot was able to correct for perturbations and imbalances showing robust control policies. - Done full-body VR teleop with a Meta Quest (Fauna’s app worked great) Big win is that it actually was able to successfully deploy robust control policies out of the box. Setup was straightforward, and it feels physically safe. I held the safety harness like an overbearing parent, but the robot didn’t need me. It was gentle, regained balance, and stopped on its own. No affiliation with Fauna Robotics, just sharing an academic lab evaluation of a commercially available research platform. Impressive performance so far and excited to start training policies for more complex tasks. What new tasks should we train Sprout to perform?

1d ago

---

**[Autonomous tractor from Netherlands! A fully autonomous tractor from Dutch company AgXeed, designed to work on fields without any human supervision.](https://www.reddit.com/r/robotics/comments/1qobnmo/autonomous_tractor_from_netherlands_a_fully/)**

From Lukas Ziegler on 𝕏: https://x.com/lukas_m_ziegler/status/2016112237019042259 AgXeed website: https://www.agxeed.com/

1d ago

---

**[Meet Sprout](https://www.reddit.com/r/robotics/comments/1qok4u0/meet_sprout/)**

Meet Sprout. Fauna Robotics are releasing a new kind of robotics platform. One designed to move out of the lab and into the real world, closer to the people who will shape what robots become next. @faunarobotics

1d ago

---

---

## Google News: "robotics"

**[Crew Studies Robotics and Virtual Reality Advancing Space Tech](https://www.nasa.gov/blogs/spacestation/2026/01/27/crew-studies-robotics-and-virtual-reality-advancing-space-tech/)**

Robotics and virtual reality filled the science schedule aboard the International Space Station on Tuesday as the Expedition 74 crew promoted education and explored human research. The orbital trio also inspected safety equipment, worked on cargo swaps, and conducted Earth observations.

NASA (.gov) • 1d ago

---

**[Forget Tesla: This EV Stock Is Beating It in Robotics and It's Dirt Cheap.](https://www.fool.com/investing/2026/01/27/forget-tesla-this-ev-stock-is-beating-tesla-in-rob/)**

Boston Dynamics' Atlas appears to have an edge over Tesla's Optimus.

The Motley Fool • 18h ago

---

**[Synthetic 'muscle' with microfluidic blood vessels shows promise for soft robotics](https://techxplore.com/news/2026-01-synthetic-muscle-microfluidic-blood-vessels.html)**

Tech Xplore • 1d ago

---

**[Richtech Robotics soars after announcing partnership with Microsoft to use AI to improve its robots](https://sherwood.news/markets/richtech-robotics-soars-after-announcing-partnership-with-microsoft-to-use/)**

The most momentous day for ADAM since serving Jensen Huang a margarita....

Sherwood News • 1d ago

---

**[Microsoft and Richtech give retail and service robots an AI boost](https://www.stocktitan.net/news/RR/richtech-robotics-collaborates-with-microsoft-to-advance-agentic-ai-2ptsobdmvovn.html)**

ADAM, Richtech's Azure-powered robot, now uses vision, voice and contextual data to improve retail workflows and customer interactions.

Stock Titan • 1d ago

---

**[Richtech Robotics Collaborates with Microsoft to Advance Agentic AI in Real-World Robotics Applications](https://www.globenewswire.com/news-release/2026/01/27/3226450/0/en/richtech-robotics-collaborates-with-microsoft-to-advance-agentic-ai-in-real-world-robotics-applications.html)**

Joint engineering effort with Microsoft AI Co-Innovation Labs enhances Richtech’s ADAM robot and extends intelligent automation across physical...

GlobeNewswire • 1d ago

---

**[Washington Brings Its Silicon Valley-Building Playbook to Robotics](https://www.tradingview.com/news/investorplace:61fd29dc3094b:0-washington-brings-its-silicon-valley-building-playbook-to-robotics/)**

Most people think Silicon Valley was built by entrepreneurs.Garage tinkerers. Venture capitalists. Risk-taking founders chasing consumer demand.It’s a comforting story … because it makes America’s greatest tech boom feel accidental… almost inevitable.But the truth is more useful for investors: Sili…

TradingView • 10h ago

---

**[State of robotics industry report 2026](https://www.therobotreport.com/state-of-robotics-industry-report-2026/)**

State of Robotics Industry Report 2026 offers a clear-eyed assessment of where the market stands today and where it’s headed.

The Robot Report • 2d ago

---

**[Not ready for robots in homes? The maker of a friendly new humanoid thinks it might change your mind](https://apnews.com/article/friendly-home-robot-fauna-robotics-sprout-57b396cd6f4b98ef83913a5efa9e0db2)**

A new humanoid robot named Sprout, developed by Fauna Robotics, is making its debut. Unlike sleek and powerful-looking machines from companies like Tesla, Sprout is designed to be approachable and friendly.

AP News • 1d ago

---

**[Ondas' American Robotics Optimus Drone Approved for Rapid Federal Procurement via DCMA Blue UAS Cleared List](https://finance.yahoo.com/news/ondas-american-robotics-optimus-drone-133000330.html)**

Approval confirms compliance with Department of War cybersecurity, supply-chain, and operational standards, further positioning Ondas' dual-use autonomous platform for expanded deployment across defense and critical infrastructure applications Milestone ...

Yahoo Finance • 9h ago

---

---

## YouTube Videos: "robotics"

**[Helix 02 by Figure Proves Humanoid Robots Can Finally Feel](https://www.youtube.com/watch?v=tz-t1EQ44n0)**

Helix 02 from Figure is changing what humanoid robots are capable of by adding something vision alone could never solve: touch ...

📺 DPCcars

👁️ 5K • 👍 165 • 💬 20 • ⏱️ 1:18 • 22h ago

---

**[The Most Complex Task a Humanoid Robot Has Ever Done? #Robot #AI #Tech](https://www.youtube.com/watch?v=3aAnqRLqqos)**

Figure AI says its flagship humanoid is more autonomous than ever thanks to its newly upgraded robot brain. The Silicon Valley ...

📺 Kalil 4.0

👁️ 991 • 👍 51 • 💬 1 • ⏱️ 0:39 • 6h ago

---

**[The German Robots Are Replacing Forklifts Inside Factories](https://www.youtube.com/watch?v=tCis6jGzxnk)**

Day 172 of watching tech evolve. German startup Filics has built autonomous warehouse robots that move in any direction, work ...

📺 Deepen

👁️ 19K • 👍 399 • 💬 10 • ⏱️ 0:29 • 4d ago

---

**[Drag-on welding robot.#industrial #welding #robot #spraying #stamping #machine](https://www.youtube.com/watch?v=i8vRsqt5ORw)**

📺 Borunte robot-Lin 

👁️ 32K • 👍 115 • 💬 2 • ⏱️ 0:21 • 4d ago

---

**[This Girl Discovered a Lost Robot in the Mountain](https://www.youtube.com/watch?v=v6GRptrADk4)**

In the depths of a mysterious mountain forest, a young girl named Jessica stumbles upon a lost, abandoned Aegis Suit robot ...

📺 Technology Next World

👁️ 49K • 👍 430 • 💬 17 • ⏱️ 3:53 • 4d ago

---

**[Elon Musk Repairs High-Tech Robotic 🕵️ Wings on Female 💲Android in Futuristic 🧪 Ai-concept.](https://www.youtube.com/watch?v=qBIpFr_d3Vg)**

RoboticWings #FuturisticLab #Android #SciFi #Robotics #AIArt #Cyberpunk #HighTech #ArtificialIntelligence #TeslaBot ...

📺 AITECHGADGETS

👁️ 242K • 💬 138 • ⏱️ 0:18 • 2d ago

---

**[Design Analysis on Sprout Robot from Fauna Robotics](https://www.youtube.com/watch?v=4aaRN2SQrAY)**

Get FREE Robotics & AI Resources (Guide, Textbooks, Courses, Resume Template, Code & Discounts) – Sign up via the pop-up ...

📺 Kevin Wood | Robotics & AI

👁️ 896 • 👍 26 • 💬 2 • ⏱️ 3:51 • 17h ago

---

**[SaaS is over… Why you should build a robotics company in 2026](https://www.youtube.com/watch?v=FqfTQFuSalY)**

2026 will be the year of robotics. We're in an Will Smith spaghetti moment. Remember how AI-generated video looked horrific two ...

📺 Andreas Klinger ⅹ Europe's Most Ambitious Startups

👁️ 14K • 👍 934 • 💬 146 • ⏱️ 16:46 • 2d ago

---

**[Viral video shows autonomous snow blower at work in New Jersey](https://www.youtube.com/watch?v=c7vetvwsn-Q)**

Sandra Bookman has more on the viral video and the man behind the handy invention.

📺 Eyewitness News ABC7NY

👁️ 525K • 👍 4K • 💬 799 • ⏱️ 2:01 • 2d ago

---

**[Fauna Robotics unveils friendly humanoid robot Sprout](https://www.youtube.com/watch?v=V2uf8k1pGyY)**

Sprout, a 3 1/2-foot-tall humanoid from Fauna Robotics, debuts with a soft foam body, expressive moves and a friendly vibe.

📺 Associated Press

👁️ 15K • 👍 122 • 💬 12 • ⏱️ 0:55 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

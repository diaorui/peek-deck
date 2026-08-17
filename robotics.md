---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-17T18:43:36.867919+00:00'
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

**Last Updated:** August 17, 2026 at 18:43 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[LoRa / Sub-GHz Antenna Optimization: From Ceramic to FPC](https://www.reddit.com/r/robotics/comments/1vqm6wp/lora_subghz_antenna_optimization_from_ceramic_to/)**

We recently worked on the RF design of a compact LoRa/GNSS Nomad Terminal handheld device, which is based on LoRa, designed to communicate/ navigate, and deploy anywhere. The antenna turned out to be one of the more challenging parts. For a small handheld, antenna performance is affected by much more than the antenna itself. The PCB, ground plane, battery, display, enclosure, and even the way the device is held can all influence the final RF performance. During the project, we evaluated several antenna configurations: Ceramic Antenna → FPC Antenna + Coaxial Cable → FPC Antenna + Pogo Pin The final FPC antenna configuration was validated with both RF measurements and outdoor testing, achieving S11 of -11.13 dB @ 868 MHz, -12.82 dB @ 915 MHz, and a 3 km LoRa link in our field test. 1. Ceramic Antenna The initial design used a ceramic antenna for its compact size and simple integration. However, its placement was relatively constrained, limiting our ability to optimize the surrounding RF environment. 2. FPC + Coaxial Cable We then tested an FPC antenna with a coaxial connection. This gave us more freedom to position the antenna away from the PCB, battery, and display, but introduced additional cabling and mechanical complexity. 3. FPC + Pogo Pin The final approach uses an FPC antenna connected through pogo pins. It provides flexible antenna placement while keeping the RF connection and mechanical structure compact. The main takeaway from the project was that antenna performance in a compact LoRa device is a system-level problem. Antenna selection, placement, PCB layout, and mechanical design all need to be considered together. The main takeaway from the project was that antenna performance in a compact LoRa device is a system-level problem. Antenna selection, placement, PCB layout, and mechanical design all need to be considered together. The complete What’s the biggest antenna design challenge you’ve encountered when working with compact LoRa or Sub-GHz devices? Share your experience togehther！

10h ago

---

**[Building my first humanoid robot from scratch — the head now has local voice + vision](https://www.reddit.com/r/robotics/comments/1vqt31b/building_my_first_humanoid_robot_from_scratch_the/)**

I’ve been building a humanoid robotics project called Evopien, mostly as a solo engineering project, and I’ve reached the point where the first head prototype can actually interact in a reasonably coherent way. I decided not to start with arms or locomotion. My first milestone was to get the basic sensory/conversational system working properly: camera → visual input microphone array → speech local ASR → transcription local LLM → reasoning/conversation local TTS → speech output The whole thing currently runs on an NVIDIA Jetson Orin Nano Super 8GB. The head can now: listen and speak locally continue listening while it is speaking be interrupted naturally switch between English and Spanish use the camera when asked visual questions answer based on a current camera frame The current hardware is intentionally pretty ugly. C920, ReSpeaker, external speakers, Jetson and cables. I’m trying to prove the architecture before spending time designing the physical head. The next major step is moving from a stationary conversational head toward proper perception/attention and eventually head movement, followed later by arms and hands. Here is the current demo if anyone wants to see it working: https://www.youtube.com/watch?v=iAxzePzF4cM I’d especially appreciate criticism from people who have gone from a perception prototype into actual physical robotics. What would you make the next milestone before starting the mechanical head?

4h ago

---

**[Looking for help for a 3d printed part](https://www.reddit.com/r/robotics/comments/1vqc4l7/looking_for_help_for_a_3d_printed_part/)**

I’m currently building a 3d printer scara arm and I’m trying to incorporate a tool changer into it. I would switch between a sharpie and a pneumatic gripper. I can’t really find a good model online and I definitely don’t have the skills to develop that by myself. Does anybody know of a good model that ”locks” it to the robot body so no magnets.

19h ago

---

**[Cubic Doggo found a nice spot on the ramp 🐾 (Sim-vs-Real)](https://www.reddit.com/r/robotics/comments/1vpu2sd/cubic_doggo_found_a_nice_spot_on_the_ramp/)**

Doggo is chill and calm in the simulation, but in real life, he's having uncontrollable happy wiggles trying to balance himself while finding the right spot on the ramp. Repo: 06Z Neucommu Audio Credit: Soul_Serenity_Sounds from Pixabay

1d ago

---

**[Built a small autonomous household robot that can complete tasks end to end](https://www.reddit.com/r/robotics/comments/1vp27ra/built_a_small_autonomous_household_robot_that_can/)**

I’ve been working on this robot project for a while and finally got it to the point where it can complete a full task autonomously. It explores and navigates the room, localize objects, approach them and manipulate them with the arm. I built the XLeRobot myself, printing the parts, getting cheap servos, wiring it together. It uses Orbbec Gemini 2 camera for RGBD and wheel odometry to move around the space. I fine tuned SmolVLA on my local GPU (Rtx 4060 ti 16GB) with a dataset I gathered using Quest 3s. The project is open source, I’ll try to post the links below.

2d ago

---

**[Bonsai just hit a 100,000 downloads on crates.io! 🎉](https://www.reddit.com/r/robotics/comments/1vp0pml/bonsai_just_hit_a_100000_downloads_on_cratesio/)**

A little over 4 years ago I started Bonsai as a side project: a Rust library for building complex, deterministic AI behavior with behavior trees. It has since found its way into a wide range of applications. The video shows two of them: on the left, a Titanfall 2 gameplay where all the players except the first person view is a NPC (bot) driven by Bonsai behavior trees. On the right, a robot from NASA lunabotics 2026 autonomously digging and dumping regolith in a simulated lunar environment – also powered by Bonsai. A lot of the library's usefulness today comes from the community. Thanks to everyone who has contributed PRs, filed issues, and pushed it further than I would have on my own. Github repo link in the comments!

2d ago

---

**[Planned upgrades: * Raspberry Pi 5 — 16 GB RAM as the main controller * 🖥️ Add an onboard display/screen * 🗣️ Add an AI speaking and voice-interaction system * 🚶 Develop a walking system * 🛞 Add stronger wheels for improved movement and stability * ⚙️ Upgrade the mechanical system](https://www.reddit.com/r/robotics/comments/1vqd45l/planned_upgrades_raspberry_pi_5_16_gb_ram_as_the/)**

18h ago

---

**[Probando 12 válvulas pepepako antiguas empaquetadas con un controlador microbit desde mi celular.](https://www.reddit.com/r/robotics/comments/1vpq5ib/probando_12_válvulas_pepepako_antiguas/)**

Mostrando como funcionaban 12 válvulas antigua versión empaquetadas en línea dirigidas por un controlador microbit desde mi celular para ver como funcionaban de 1 en 1,en grupos y variando lapresion de cada una para comprobar proporcionalidad.

🔗 [youtu.be](https://youtu.be/nIWjN0zeS64?is=gZYktrEd0qfCfEwv) • 1d ago

---

**[Day 2 of building an Iron Man helmet from scratch](https://www.reddit.com/r/robotics/comments/1vpdxq5/day_2_of_building_an_iron_man_helmet_from_scratch/)**

Day 2 of the CAD build. Started refining the rough shape from Day 1 and working on the different sections of the helmet. Still a long way from the finished model, but it's starting to look like an actual Iron Man helmet now 😂 The plan is still: CAD → 3D print → servos → moving helmet Recording the progress every day, so we'll see where this ends up.

1d ago

---

**[Jennifer Marie Godden](https://www.reddit.com/r/robotics/comments/1vpr4iu/jennifer_marie_godden/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [YouTube](https://youtube.com/shorts/RvWqiSV1TVg?is=ERP_qHlE9F2xIM2i) • 1d ago

---

---

## Google News: "robotics"

**[The 25 most promising robotics startups in 2026, according to investors](https://www.businessinsider.com/robotics-tech-ai-startups-investors-funding-2026-8)**

We asked investors from Sequoia, Felicis, Bessemer, and more to highlight promising robotics startups, as the sector sees an investment boom in 2026.

Business Insider • 8h ago

---

**[Exclusive: SoftBank Is Investing $200 Million in Autonomous Construction Startup Gravis Robotics](https://www.inc.com/georgia-fearn/exclusive-softbank-is-investing-200-million-in-autonomous-construction-startup-gravis-robotics/91390995)**

'You press play, the machine will drive itself to the start and essentially do that entire job without intervention,' the Gravis CEO says.

inc.com • 6h ago

---

**[How to Make a Robot Better at Its Job? Give It Eyes.](https://www.nytimes.com/2026/08/17/business/robots-stellantis-inbolt.html)**

The New York Times • 9h ago

---

**[Serve Robotics plots new strategy after breakup with Uber Eats](https://www.axios.com/2026/08/17/serve-robotics-uber-grubhub-doordash-washington)**

axios.com • 6h ago

---

**[Watch How Delivery Robots Can Transform the Last Mile](https://www.bloomberg.com/news/videos/2026-08-17/how-delivery-robots-can-transform-the-last-mile-video)**

Bloomberg.com • 18h ago

---

**[Uber Sells Serve Robotics Stake, Catches Company Off Guard: ‘Differing Views’ Sour Partnership](https://finance.yahoo.com/technology/ai/articles/uber-sells-serve-robotics-stake-013116691.html)**

Serve Robotics investors were already nursing loss after disappointing quarterly financial results. Another blow came days later when long0time Uber Technologies dumped its entire stake in the autonomous delivery robot company. According to a regulatory filing on Friday, Uber disclosed...

Yahoo Finance • 17h ago

---

**[Humanoid robots could patrol southern border, CEO pitches, as futuristic technology moves closer to reality](https://www.foxnews.com/politics/humanoid-robots-patrol-southern-border-ceo-pitches-futuristic-technology-moves-closer-reality)**

Foundation CEO Sankaet Pathak said humanoid robots could conduct autonomous surveillance and reconnaissance along the southern border's rugged terrain.

Fox News • 1d ago

---

**[Humanoids move beyond dancing in real-world firefighting challenge](https://interestingengineering.com/ai-robotics/whrg-humanoid-robot-firefighting-beijing)**

Twenty-three humanoid robots faced a simulated firefighting mission in Beijing, testing their skills in realistic emergency conditions.

Interesting Engineering • 9h ago

---

**[China shock looms for robotics as physical AI race heats up: think tank](https://asia.nikkei.com/business/china-tech/china-shock-looms-for-robotics-as-physical-ai-race-heats-up-think-tank)**

Taiwan's DSET says Beijing making 'whole of nation' push similar to EV, drone strategy

Nikkei Asia • 17h ago

---

**[Week Ends Aboard Station With Robotics, Spacewalk Reviews, and Science](https://www.nasa.gov/blogs/spacestation/2026/08/14/week-ends-aboard-station-with-robotics-spacewalk-reviews-and-science/)**

Expedition 75 ended the week studying Canadarm2 robotic arm maneuvers and reviewing procedures for a spacewalk to support the removal and replacement of a space-to-ground antenna on Tuesday, Aug. 18. Science remained on Friday’s schedule as the International Space Station residents studied space exercise techniques, explored aerodynamic drag forces, and more.

NASA (.gov) • 3d ago

---

---

## YouTube Videos: "robotics"

**[I spent 3 days at MIT... the robot hype is worse than you think](https://www.youtube.com/watch?v=aB5LGrHISqY)**

Omnigent is an open source meta-harness to run all your AI agents in one place. Try it free - https://bit.ly/4fXzeo8 I spent last week ...

📺 Fireship

👁️ 988K • 👍 23K • 💬 2K • ⏱️ 7:02 • 6d ago

---

**[DR02 Humanoid Robot |  Steady Steps, Steady Progress](https://www.youtube.com/watch?v=5gd2b0cmfyU)**

Our DR02 humanoid robot takes on the stairs with stable, controlled movement—steady steps, steady progress.

📺 DEEP Robotics

👁️ 32K • 👍 116 • 💬 14 • ⏱️ 0:18 • 5d ago

---

**[The Many Problems With Home Robotics](https://www.youtube.com/watch?v=EMj1fl17Tv8)**

Home robots have long been the stuff of sci-fi dreams (and nightmares), but they lag behind AI chatbots, AI agents, and even their ...

📺 CNET

👁️ 8K • 👍 287 • 💬 45 • ⏱️ 5:16 • 1d ago

---

**[Why the US government is trying to ban this Chinese dancing robot | Explainer](https://www.youtube.com/watch?v=RzqtTunpXlE)**

The Federal Communications Commission on 28 July announced a ban on humanoid robots from China including the popular ...

📺 Guardian News

👁️ 40K • 👍 482 • 💬 133 • ⏱️ 3:48 • 6d ago

---

**[MASSIVE robotics deal pushes physical AI into US shipbuilding](https://www.youtube.com/watch?v=fhzTrAfskQk)**

GrayMatter Robotics CEO Ariyan Kabir explains how AI-powered robots could supercharge U.S. shipbuilding, boost American ...

📺 Fox Business Clips

👁️ 40K • 👍 557 • 💬 108 • ⏱️ 7:05 • 6d ago

---

**[How Many Robots Will You Own? | Conversations in Action](https://www.youtube.com/watch?v=bMuKKamrDh4)**

What happens when robots move beyond intelligence and begin learning from experience? In Conversations in Action Ep. 1, ...

📺 Imagination in Action

👁️ 10K • 👍 334 • 💬 46 • ⏱️ 1:12:16 • 6d ago

---

**[Chinese robot maker Unitree set to become China&#39;s first humanoid robot stock | DW News](https://www.youtube.com/watch?v=P3W6dKx7u1Y)**

Chinese robot maker Unitree has opened subscriptions for its Shanghai IPO, as it seeks to raise around 900 million dollars for ...

📺 DW News

👁️ 19K • 👍 242 • 💬 166 • ⏱️ 13:41 • 6d ago

---

**[China&#39;s Banned T800 Humanoid Robots Fight on US Soil #robotics #robot #robotfight](https://www.youtube.com/watch?v=5370gd35zhI)**

China's T800 robots just had their first fight on US soil. The San Francisco startup REK (Robot Entertainment Kombat) hosted a ...

📺 Kalil 4.0

👁️ 6K • 👍 172 • 💬 27 • ⏱️ 0:56 • 16h ago

---

**[Chinese company unveils robot that jumps 2 meters](https://www.youtube.com/watch?v=Bd5x9HF3-44)**

Can robots outrun and outjump humans? Well, this one can… Chinese robotics company Unitree has unveiled its new ...

📺 CGTN Europe

👁️ 856 • 👍 36 • 💬 2 • ⏱️ 0:23 • 2h ago

---

**[The 9-Foot-Tall AI Humanoid Robot at the Center of China’s Robotics Revolution](https://www.youtube.com/watch?v=j3wi7ILmSWA)**

Read More: https://time.com/article/2026/07/23/unitree-china-human-robotics/ Inside China's humanoid robot revolution, Unitree ...

📺 TIME

👁️ 232K • 👍 3K • 💬 610 • ⏱️ 10:16 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

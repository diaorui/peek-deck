---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-17T20:55:08.980909+00:00'
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

**Last Updated:** August 17, 2026 at 20:55 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Hexapod walking and leveling at the same time!](https://www.reddit.com/r/robotics/comments/1vqxvcx/hexapod_walking_and_leveling_at_the_same_time/)**

This is my custom robotics project I have been working on for the past year. I'll be posting more on my X account RhettBrewer. I will also be posting other projects and future ones there too!

3h ago

---

**[The robot is only the tip of the iceberg](https://www.reddit.com/r/robotics/comments/1vqyb9x/the_robot_is_only_the_tip_of_the_iceberg/)**

The physical design is finally locked down, and the digital model now mirrors the optimized physical robot. What you see here has taken a lot of work, but surprisingly, most of the development over the last two years has been on the part you can't see: the software. I have been developing Robert's operating system alongside the mechanics - coordinating 30 servos, synchronized movements, speech, vision, sensors, driving and AI interaction so that they can all work together. The ultimate goal is to give AI a physical embodiment through which it can see, speak, move and interact with the world. The mechanical design has gone through the same process of continuous refinement. It is now divided into self-contained modules that make Robert much easier to build, maintain and repair.

3h ago

---

**[Voice and gestures are becoming part of the interface for home robots](https://www.reddit.com/r/robotics/comments/1vqwy7f/voice_and_gestures_are_becoming_part_of_the/)**

Matic’s latest update lets its robot vacuum respond to spoken commands and gestures rather than relying only on an app. The system is still working within a defined set of actions, but the broader robotics question is more interesting: how much of human-robot interaction should depend on people learning an interface, versus robots learning to interpret the ways people already communicate? As robots move into homes and other less structured environments, voice, pointing, movement and context may become increasingly important parts of the control layer.

4h ago

---

**[4-servo quadruped robot walks upside down on a magnetic ceiling — passive magnets, no adhesion tech (open-source platform)](https://www.reddit.com/r/robotics/comments/1vqyty5/4servo_quadruped_robot_walks_upside_down_on_a/)**

Turns out you don't need active adhesion (vacuum, electromagnets) for ceiling locomotion — passive permanent magnets in Quaddle open source robot's foot tips are enough, as long as the gait is designed for holding contact upside down instead of just an inverted version of the ground-walking gait. The interesting part wasn't the magnets, it was the gait — same open source robotics platform OpenCat, same 4 servos, just a different motion profile. Planning to open source this gait's code before it ships too, so anyone curious can adapt it, not just read about it. Anyone else working on non-standard locomotion modes (climbing, inverted, whatever) — what ended up being the hardest part for you?

🔗 [youtube.com](https://www.youtube.com/watch?v=XRWFeB5-ZbM) • 3h ago

---

**[LoRa / Sub-GHz Antenna Optimization: From Ceramic to FPC](https://www.reddit.com/r/robotics/comments/1vqm6wp/lora_subghz_antenna_optimization_from_ceramic_to/)**

We recently worked on the RF design of a compact LoRa/GNSS Nomad Terminal handheld device, which is based on LoRa, designed to communicate/ navigate, and deploy anywhere. The antenna turned out to be one of the more challenging parts. For a small handheld, antenna performance is affected by much more than the antenna itself. The PCB, ground plane, battery, display, enclosure, and even the way the device is held can all influence the final RF performance. During the project, we evaluated several antenna configurations: Ceramic Antenna → FPC Antenna + Coaxial Cable → FPC Antenna + Pogo Pin The final FPC antenna configuration was validated with both RF measurements and outdoor testing, achieving S11 of -11.13 dB @ 868 MHz, -12.82 dB @ 915 MHz, and a 3 km LoRa link in our field test. 1. Ceramic Antenna The initial design used a ceramic antenna for its compact size and simple integration. However, its placement was relatively constrained, limiting our ability to optimize the surrounding RF environment. 2. FPC + Coaxial Cable We then tested an FPC antenna with a coaxial connection. This gave us more freedom to position the antenna away from the PCB, battery, and display, but introduced additional cabling and mechanical complexity. 3. FPC + Pogo Pin The final approach uses an FPC antenna connected through pogo pins. It provides flexible antenna placement while keeping the RF connection and mechanical structure compact. The main takeaway from the project was that antenna performance in a compact LoRa device is a system-level problem. Antenna selection, placement, PCB layout, and mechanical design all need to be considered together. The main takeaway from the project was that antenna performance in a compact LoRa device is a system-level problem. Antenna selection, placement, PCB layout, and mechanical design all need to be considered together. The complete What’s the biggest antenna design challenge you’ve encountered when working with compact LoRa or Sub-GHz devices? Share your experience togehther！

12h ago

---

**[Modeling an Omni-directional Robot in Simscape](https://www.reddit.com/r/robotics/comments/1vr2cdo/modeling_an_omnidirectional_robot_in_simscape/)**

If you are interested in learning how to model any robot in Simscape, I am working on a blog series that tries to go through the whole process. It is still work in progress but has most of the modeling process already covered. Take a look, feel free to leave feedback or reach out to me with questions if you have any.

🔗 [siddharthv.com](https://siddharthv.com/robotics/) • 1h ago

---

**[Building my first humanoid robot from scratch — the head now has local voice + vision](https://www.reddit.com/r/robotics/comments/1vqt31b/building_my_first_humanoid_robot_from_scratch_the/)**

I’ve been building a humanoid robotics project called Evopien, mostly as a solo engineering project, and I’ve reached the point where the first head prototype can actually interact in a reasonably coherent way. I decided not to start with arms or locomotion. My first milestone was to get the basic sensory/conversational system working properly: camera → visual input microphone array → speech local ASR → transcription local LLM → reasoning/conversation local TTS → speech output The whole thing currently runs on an NVIDIA Jetson Orin Nano Super 8GB. The head can now: listen and speak locally continue listening while it is speaking be interrupted naturally switch between English and Spanish use the camera when asked visual questions answer based on a current camera frame The current hardware is intentionally pretty ugly. C920, ReSpeaker, external speakers, Jetson and cables. I’m trying to prove the architecture before spending time designing the physical head. The next major step is moving from a stationary conversational head toward proper perception/attention and eventually head movement, followed later by arms and hands. Here is the current demo if anyone wants to see it working: https://www.youtube.com/watch?v=iAxzePzF4cM I’d especially appreciate criticism from people who have gone from a perception prototype into actual physical robotics. What would you make the next milestone before starting the mechanical head?

6h ago

---

**[Looking for help for a 3d printed part](https://www.reddit.com/r/robotics/comments/1vqc4l7/looking_for_help_for_a_3d_printed_part/)**

I’m currently building a 3d printer scara arm and I’m trying to incorporate a tool changer into it. I would switch between a sharpie and a pneumatic gripper. I can’t really find a good model online and I definitely don’t have the skills to develop that by myself. Does anybody know of a good model that ”locks” it to the robot body so no magnets.

21h ago

---

**[Cubic Doggo found a nice spot on the ramp 🐾 (Sim-vs-Real)](https://www.reddit.com/r/robotics/comments/1vpu2sd/cubic_doggo_found_a_nice_spot_on_the_ramp/)**

Doggo is chill and calm in the simulation, but in real life, he's having uncontrollable happy wiggles trying to balance himself while finding the right spot on the ramp. Repo: 06Z Neucommu Audio Credit: Soul_Serenity_Sounds from Pixabay

1d ago

---

**[Built a small autonomous household robot that can complete tasks end to end](https://www.reddit.com/r/robotics/comments/1vp27ra/built_a_small_autonomous_household_robot_that_can/)**

I’ve been working on this robot project for a while and finally got it to the point where it can complete a full task autonomously. It explores and navigates the room, localize objects, approach them and manipulate them with the arm. I built the XLeRobot myself, printing the parts, getting cheap servos, wiring it together. It uses Orbbec Gemini 2 camera for RGBD and wheel odometry to move around the space. I fine tuned SmolVLA on my local GPU (Rtx 4060 ti 16GB) with a dataset I gathered using Quest 3s. The project is open source, I’ll try to post the links below.

2d ago

---

---

## Google News: "robotics"

**[The 25 most promising robotics startups in 2026, according to investors](https://www.businessinsider.com/robotics-tech-ai-startups-investors-funding-2026-8)**

We asked investors from Sequoia, Felicis, Bessemer, and more to highlight promising robotics startups, as the sector sees an investment boom in 2026.

Business Insider • 10h ago

---

**[Exclusive: SoftBank Is Investing $200 Million in Autonomous Construction Startup Gravis Robotics](https://www.inc.com/georgia-fearn/exclusive-softbank-is-investing-200-million-in-autonomous-construction-startup-gravis-robotics/91390995)**

'You press play, the machine will drive itself to the start and essentially do that entire job without intervention,' the Gravis CEO says.

inc.com • 5h ago

---

**[How to Make a Robot Better at Its Job? Give It Eyes.](https://www.nytimes.com/2026/08/17/business/robots-stellantis-inbolt.html)**

The New York Times • 11h ago

---

**[Watch How Delivery Robots Can Transform the Last Mile](https://www.bloomberg.com/news/videos/2026-08-17/how-delivery-robots-can-transform-the-last-mile-video)**

Bloomberg.com • 20h ago

---

**[Serve Robotics plots new strategy after breakup with Uber Eats](https://www.axios.com/2026/08/17/serve-robotics-uber-grubhub-doordash-washington)**

Axios • 8h ago

---

**[Humanoid robots could patrol southern border, CEO pitches, as futuristic technology moves closer to reality](https://www.foxnews.com/politics/humanoid-robots-patrol-southern-border-ceo-pitches-futuristic-technology-moves-closer-reality)**

Foundation CEO Sankaet Pathak said humanoid robots could conduct autonomous surveillance and reconnaissance along the southern border's rugged terrain.

Fox News • 1d ago

---

**[Humanoids move beyond dancing in real-world firefighting challenge](https://interestingengineering.com/ai-robotics/whrg-humanoid-robot-firefighting-beijing)**

Twenty-three humanoid robots faced a simulated firefighting mission in Beijing, testing their skills in realistic emergency conditions.

Interesting Engineering • 11h ago

---

**[Inside Persona’s Bold Bet On Humanoid Welders In Shipyards](https://spectrum.ieee.org/persona-ai-humanoid-robot-welding)**

Persona AI sees near-term economic viability in heavy industrial humanoids

IEEE Spectrum • 1d ago

---

**[Uber Sells Serve Robotics Stake, Catches Company Off Guard: ‘Differing Views’ Sour Partnership](https://finance.yahoo.com/technology/ai/articles/uber-sells-serve-robotics-stake-013116691.html)**

Serve Robotics investors were already nursing loss after disappointing quarterly financial results. Another blow came days later when long0time Uber Technologies dumped its entire stake in the autonomous delivery robot company. According to a regulatory filing on Friday, Uber disclosed...

Yahoo Finance • 19h ago

---

**[Gravis Robotics gets $200M from SoftBank to retrofit excavators with self-driving AI systems](https://siliconangle.com/2026/08/17/gravis-robotics-gets-200m-funding-softbank-retrofit-excavators-self-driving-ai-systems/)**

Gravis Robotics gets $200M from SoftBank to retrofit excavators with self-driving AI systems - SiliconANGLE

SiliconANGLE • 7h ago

---

---

## YouTube Videos: "robotics"

**[DR02 Humanoid Robot |  Steady Steps, Steady Progress](https://www.youtube.com/watch?v=5gd2b0cmfyU)**

Our DR02 humanoid robot takes on the stairs with stable, controlled movement—steady steps, steady progress.

📺 DEEP Robotics

👁️ 32K • 👍 116 • 💬 14 • ⏱️ 0:18 • 5d ago

---

**[I spent 3 days at MIT... the robot hype is worse than you think](https://www.youtube.com/watch?v=aB5LGrHISqY)**

Omnigent is an open source meta-harness to run all your AI agents in one place. Try it free - https://bit.ly/4fXzeo8 I spent last week ...

📺 Fireship

👁️ 990K • 👍 23K • 💬 2K • ⏱️ 7:02 • 6d ago

---

**[Why the US government is trying to ban this Chinese dancing robot | Explainer](https://www.youtube.com/watch?v=RzqtTunpXlE)**

The Federal Communications Commission on 28 July announced a ban on humanoid robots from China including the popular ...

📺 Guardian News

👁️ 40K • 👍 482 • 💬 133 • ⏱️ 3:48 • 6d ago

---

**[The Many Problems With Home Robotics](https://www.youtube.com/watch?v=EMj1fl17Tv8)**

Home robots have long been the stuff of sci-fi dreams (and nightmares), but they lag behind AI chatbots, AI agents, and even their ...

📺 CNET

👁️ 8K • 👍 292 • 💬 45 • ⏱️ 5:16 • 1d ago

---

**[MASSIVE robotics deal pushes physical AI into US shipbuilding](https://www.youtube.com/watch?v=fhzTrAfskQk)**

GrayMatter Robotics CEO Ariyan Kabir explains how AI-powered robots could supercharge U.S. shipbuilding, boost American ...

📺 Fox Business Clips

👁️ 40K • 👍 557 • 💬 108 • ⏱️ 7:05 • 6d ago

---

**[How Many Robots Will You Own? | Conversations in Action](https://www.youtube.com/watch?v=bMuKKamrDh4)**

What happens when robots move beyond intelligence and begin learning from experience? In Conversations in Action Ep. 1, ...

📺 Imagination in Action

👁️ 10K • 👍 343 • 💬 46 • ⏱️ 1:12:16 • 6d ago

---

**[Chinese robot maker Unitree set to become China&#39;s first humanoid robot stock | DW News](https://www.youtube.com/watch?v=P3W6dKx7u1Y)**

Chinese robot maker Unitree has opened subscriptions for its Shanghai IPO, as it seeks to raise around 900 million dollars for ...

📺 DW News

👁️ 19K • 👍 242 • 💬 166 • ⏱️ 13:41 • 6d ago

---

**[Chinese company unveils robot that jumps 2 meters](https://www.youtube.com/watch?v=Bd5x9HF3-44)**

Can robots outrun and outjump humans? Well, this one can… Chinese robotics company Unitree has unveiled its new ...

📺 CGTN Europe

👁️ 4K • 👍 188 • 💬 16 • ⏱️ 0:23 • 4h ago

---

**[China&#39;s Banned T800 Humanoid Robots Fight on US Soil #robotics #robot #robotfight](https://www.youtube.com/watch?v=5370gd35zhI)**

China's T800 robots just had their first fight on US soil. The San Francisco startup REK (Robot Entertainment Kombat) hosted a ...

📺 Kalil 4.0

👁️ 7K • 👍 195 • 💬 30 • ⏱️ 0:56 • 18h ago

---

**[Beni Camera Robot: It Replaced My $5,000 Camera Rig 🤯](https://www.youtube.com/watch?v=ufoDSiEjRHU)**

Beni is an all-terrain Camera Robot designed to follow you and capture smooth, hands-free footage. In this video, I take Beni ...

📺 KhanFlicks

👁️ 57K • 💬 60 • ⏱️ 8:34 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

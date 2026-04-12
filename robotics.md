---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-12T23:36:17.303013+00:00'
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

**Last Updated:** April 12, 2026 at 23:36 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Somewhere in Poland](https://www.reddit.com/r/robotics/comments/1sjhnd1/somewhere_in_poland/)**

8h ago

---

**[massive robotic hand that produce up to11000 pound force.](https://www.reddit.com/r/robotics/comments/1sjmxyz/massive_robotic_hand_that_produce_up_to11000/)**

4h ago

---

**[LS3 Boston Dynamics Mini Resin Printing](https://www.reddit.com/r/robotics/comments/1sj8q52/ls3_boston_dynamics_mini_resin_printing/)**

Hi everyone! I've been developing the LS3 BostonDynamics Mini quadruped for a while now. The goal was to create a modular, 3D-printable frame that can carry a Raspberry Pi. It’s still a work in progress, but the mechanical assembly is finally done! I'm happy to discuss the kinematics or electronics if anyone is interested!

15h ago

---

**[I've finally built the Bimo Robotics Kit v1.0, an open-source bipedal robotics platform.](https://www.reddit.com/r/robotics/comments/1sjhufo/ive_finally_built_the_bimo_robotics_kit_v10_an/)**

After more than two years of solo development, I'm releasing v1.0 of the Bimo Robotics Kit. Bimo is an open-source bipedal robotics platform designed as a complete research and education kit. The core value is the full sim-to-real pipeline: you train RL locomotion models in Isaac Lab and deploy directly on the physical hardware. The v1.0 release includes: - Startup guide (zero to walking in one session) - Full MCU code for the onboard microcontroller. - Main controller board overview and pinout. - Updated Bimo API for hardware control. - Improved Isaac Lab task code for more stable sim-to-real transfer. - Pre-trained stable walking model. Turning and push recovery models are next on the Isaac Lab environment roadmap. The platform ships with a walking model as a baseline you can extend, which is kind of the point for a research kit. Check out all the details here: - Github: https://github.com/mekion/the-bimo-project - Discord: https://discord.gg/9uXsArwXHG - Mekion: https://www.mekion.com/product/ Happy to answer questions about the Isaac Lab integration, the hardware design decisions, or what it's like building this as a solo founder. Let me know what you think about the project.

7h ago

---

**[In early April, Generalist AI unveiled GEN-1, a general-purpose AI model for mastery of simple physical tasks](https://www.reddit.com/r/robotics/comments/1sjan8z/in_early_april_generalist_ai_unveiled_gen1_a/)**

Technical blog post with multiple videos: https://generalistai.com/blog/apr-02-2026-GEN-1

13h ago

---

**[Found this open-source 'Pixar lamp' while procrastinating today. the engineering under the hood is actually insane for a weekend build](https://www.reddit.com/r/robotics/comments/1sj9u8y/found_this_opensource_pixar_lamp_while/)**

I know we usually only post our own projects here, but i was procrastinating on my own codebase today and went down a rabbit hole looking at github repos from some 48h REDHackathon happening in shanghai right now (hosted by rednote I think? today is their demo day). tbh i mostly expected to see a bunch of hastily duct-taped openai wrappers and weekend spaghetti code. clicked on one of the hardware submissions called Mira. at first glance the picture just looks like a cute 3d-printed pixar lamp. I figured it was just a physical shell with a basic python script piping some face tracking coordinates directly to a couple servos. but looking at the actual code... the system architecture is surprisingly hardcore. They didnt just hardcode reactions. they built a full embodied interaction system. the pipeline goes from single camera input -> vision event extraction -> scene selection -> local bridge / safety layer -> ESP32 firmware. Instead of raw tracking they built a scene-based motion choreography abstraction. it interprets visual data into states like 'curious_observe', 'cute_probe', and 'standup_reminder'. The esp32 firmware isnt a toy either... it has a custom binary serial protocol, touch thresholds, and ack/err handling. they even built offline rehearsal scripts, fault injection, and a web director console so they could test the logic without the physical hardware glitching out on stage. Most ai right now just sits in a chat window waiting for a prompt. this thing is trying to actually notice your presence in a physical space and respond with body language and light rhythms before you even say a word. idk, seeing hardware prototypes with this level of release-oriented engineering come out of a 48h builder camp makes me feel pretty lazy today lol. its just a stark reminder that the next phase of ai probably isnt going to be on a screen, but actually sitting on our desks observing us. anyway just thought id share something cool that isnt another b2b saas wrapper. repo if anyone wants to look at the c++ / esp32 logic (not mine obviously): github.com/JunkaiWang-TheoPhy/Mira-Light-AI-That-Sees-You

14h ago

---

**[Kame Robotics unveils a compact open-source quadruped for desk-top robotics experiments](https://www.reddit.com/r/robotics/comments/1siofos/kame_robotics_unveils_a_compact_opensource/)**

1d ago

---

**[PNP Robotics: Haptic Teleoperation for data collection.](https://www.reddit.com/r/robotics/comments/1sj5dfk/pnp_robotics_haptic_teleoperation_for_data/)**

PNP Robotics: Haptic Teleoperation for data collection. At the Embodied AI Conference, we’re excited to showcase our integration of the Haply Inverse3 haptic joystick with Franka robots, enabling real-time pose control and immersive haptic feedback for intuitive teleoperation. EmbodiedAI #HapticTeleoperation #Franka #Haply #Robotics #Teleoperation

18h ago

---

**[GIL (General Intelligence Layer)](https://www.reddit.com/r/robotics/comments/1sjnx41/gil_general_intelligence_layer/)**

Hello everyone, a few months ago i had this idea of a layer that helps Robis unterstand the world. with the Help of a few tools that are generalized an AI Agent can steer any Robot and the engineers only need to change the control layer. I open sourced the whole thing and sat together with universities in switzerland as well as robotic companies in europe. All of them are very interested to make this happen and i will continue to sit together with them to make this project happen. If you are interested as well feel free to clone it and try it out 😇 I have opened the Github Repo to the Public for research use. If you have Questions feel free to ask, i will post more infos in the Comments.

🔗 [GitHub](https://github.com/beyondExp/GIL) • 4h ago

---

**[Unitree H1 at 10 m/s (Leg length: 0.4+0.4=0.8m, body weight: approx. 62kg)](https://www.reddit.com/r/robotics/comments/1sigfd3/unitree_h1_at_10_ms_leg_length_040408m_body/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2042912788717408509

1d ago

---

---

## Google News: "robotics"

**[Building the Future of Texas Robotics](https://news.utexas.edu/2026/04/09/building-the-future-of-texas-robotics/)**

Deepu Talla helps bring the future of robotics closer to reality through the Nvidia-Talla Endowment for Texas Robotics.

The University of Texas at Austin • 3d ago

---

**[Unitree’s H1 robot hits 10 m/s sprint speed, getting close to Usain Bolt’s 100m world record](https://www.globaltimes.cn/page/202604/1358712.shtml)**

Chinese robotics startup Unitree Robotics released a video on Saturday showing its H1 robot reached a sprint speed of up to 10 meters per second, noting that the humanoid robot broke the world record again.

Global Times • 13h ago

---

**[UP robotics teams compete for Michigan FIRST Robotics state finals](https://www.uppermichiganssource.com/2026/04/11/up-robotics-teams-compete-michigan-first-robotics-state-finals/)**

40 teams battled during the two-day district qualifiers at Escanaba High School.

Upper Michigan's Source • 1d ago

---

**[CEO Andy Jassy shares 3 ways Amazon is innovating to make customers’ lives easier and better](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ceo-andy-jassy-robotics-rural-delivery-broadband)**

In his annual letter to shareholders, Jassy shares how robotics, faster rural delivery, and broadband connectivity for underserved customers and geographies will help improve the customer experience.

About Amazon • 2d ago

---

**[New humanoid robots replacing workers in factories](https://www.nbcnews.com/video/shorts/new-humanoid-robots-replacing-workers-in-factories-261041221991)**

Meet 'Digit', a humanoid robotic worker made by Agility Robotics, now part of a new wave of robots replacing workers at companies like Schaeffler, Toyota, and GXO. NBC News' Brian Cheung takes a look.

NBC News • 3d ago

---

**[Opinion | Meet Abi, the AI-powered robot companion for senior care](https://www.washingtonpost.com/opinions/2026/04/09/ai-robot-senior-care-abi/)**

This new tech from Australia is coming to America’s senior care facilities.

The Washington Post • 2d ago

---

**[Hidden in plain sight: Robots reveal ‘shipwreck city’ below the surface of a Washington lake](https://www.10tv.com/article/news/nation-world/robotics-underwater-detection-shipwrecks-sonar-survey-remote-operated-vehicle-washington-lake-union/507-d5e09930-31c1-491f-8c8b-01f9fcbba5b8)**

'Shipwreck city': A high-tech survey has found dozens of possible wrecks in Washington state, with robotics capturing images in areas too dangerous for divers.

10TV • 5h ago

---

**[Students shine at Wolfpack Robotics’ Robo Rally](https://www.timesleader.com/news/1738534/students-shine-at-wolfpack-robotics-robo-rally)**

<p>PLAINS TWP. — It was a celebration of robotics on Saturday as regional schools gathered at Wilkes-Barre Area High School for Wolfpack Robotics’ second Robo Rally.</p>

Times Leader • 23h ago

---

**[Electrofluidic fiber muscles could enable silent robotic systems](https://techxplore.com/news/2026-04-electrofluidic-fiber-muscles-enable-silent.html)**

Tech Xplore • 3d ago

---

**[Resolved: Laundry folding is the future of home robotics](https://www.pcworld.com/article/3110605/resolved-laundry-folding-is-the-future-of-home-robotics.html)**

Hot on the heels of LG's laundry-folding robot showcased at CES, Syncere has released a much more elegant home robot that marries a floor lamp to laundry-folding functions.

PCWorld • 3d ago

---

---

## YouTube Videos: "robotics"

**[Ukraine’s New Combat Robots are Absolutely Shredding Russia Right Now](https://www.youtube.com/watch?v=RvDmz7cBAcE)**

Go to https://www.artwine.com to get your limited bottle of Ukrainian sparkling wine, rescued from the cellars of Bakhmut. Must be ...

📺 Paul Warburg

👁️ 167K • 👍 16K • 💬 1K • ⏱️ 31:17 • 19h ago

---

**[New AI Robot Is Starting to Feel Human (Artificial Humans Are Here)](https://www.youtube.com/watch?v=HOgCL8lKuDc)**

Try Seedance 2.0 with Claude on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-LDckkB Realbotix just launched ...

📺 AI Revolution

👁️ 54K • 👍 1K • 💬 136 • ⏱️ 14:57 • 1d ago

---

**[Why Every Tech Expert is Now Watching This New AI Robot](https://www.youtube.com/watch?v=bwBYN9hun84)**

Imagine a task so delicate it's been the "holy grail" of engineering for three decades. We're talking about handling things that fold, ...

📺 PRO ROBOTS

👁️ 20K • 👍 619 • 💬 42 • ⏱️ 6:30 • 4d ago

---

**[Unitree H1 AI Robot SHOCKS the World AGAIN… Breaks Speed Record!](https://www.youtube.com/watch?v=5vrTfZNOu-o)**

This humanoid robot just hit 10 meters per second — matching the speed of elite human sprinters. Unitree's H1 AI robot isn't ...

📺 The AI Nexus

👁️ 5K • 👍 184 • 💬 18 • ⏱️ 25:42 • 20h ago

---

**[AI agent in a robot does exactly what experts warned](https://www.youtube.com/watch?v=woTy4dTiT20)**

Could AI become dangerous? Can we trust AI Agents? AGI. Use code insideai at https://incogni.com/insideai to get an exclusive ...

📺 InsideAI

👁️ 510K • 👍 20K • 💬 2K • ⏱️ 16:24 • 3d ago

---

**[This Is Ridiculously Bad... Acid Anguisher Are Terrible Now | War Robots](https://www.youtube.com/watch?v=RAVXK_8ThLA)**

Acid Titan shotguns have fallen into the ground. I havent been seeing them around as much recently. But this is insane, I did not ...

📺 PREDATOR WR

👁️ 7K • 👍 346 • 💬 56 • ⏱️ 14:11 • 11h ago

---

**[Humanoid robots take over manual job at auto parts plant](https://www.youtube.com/watch?v=JMxKpo_Llt8)**

Humanoid robots are being used for some manual tasks at the Schaeffler auto parts plant in Cheraw, S.C. Proponents argue that ...

📺 NBC News

👁️ 104K • 👍 1K • 💬 737 • ⏱️ 4:56 • 2d ago

---

**[These NEW Human-Like AI Robots of 2026 Just SHOCKED the World!](https://www.youtube.com/watch?v=FOfieag6fi4)**

The world wasn't ready for what 2026 had in store — a wave of humanoid robots so advanced, so eerily lifelike, that the line ...

📺 The AI Nexus

👁️ 9K • 👍 276 • 💬 19 • ⏱️ 16:42 • 6d ago

---

**[Why the Lymow One Plus is the Best Robot Mower Not Sponsored](https://www.youtube.com/watch?v=TCBaaSISul8)**

Lymow → https://lymowtradecolimited.pxf.io/OYr2VG The Lymow One Plus isn't your average robot mower. Instead of those tiny, ...

📺 How To with Doc

👁️ 16K • 👍 936 • 💬 167 • ⏱️ 21:24 • 3d ago

---

**[CURIE IS ACTUALLY OVERPOWERED WITH BASILEUS! SECRET STRONG ROBOT? (War Robots)](https://www.youtube.com/watch?v=lNqyCD5fuxs)**

In this video I tested out the Curie with Basileus. https://wr.my.games/Wolfblood7.

📺 Wolfblood7

👁️ 2K • 👍 127 • 💬 27 • ⏱️ 13:17 • 15h ago

---

---

*Generated by PeekDeck - A glance is all you need*

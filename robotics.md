---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-13T13:28:44.186633+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** April 13, 2026 at 13:28 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Beijing’s Humanoid Robot Half Marathon, Night Run Test - Around 40% of teams are running fully autonomous, remote-controlled runs get a 1.2× penalty (Beijing's E-Town Half Marathon on April 19 with 100+ teams, 300+ humanoids competing)](https://www.reddit.com/r/robotics/comments/1sk6p2y/beijings_humanoid_robot_half_marathon_night_run/)**

3h ago

---

**[massive robotic hand that produce up to11000 pound force.](https://www.reddit.com/r/robotics/comments/1sjmxyz/massive_robotic_hand_that_produce_up_to11000/)**

18h ago

---

**[Somewhere in Poland](https://www.reddit.com/r/robotics/comments/1sjhnd1/somewhere_in_poland/)**

21h ago

---

**[Custom World Creation in Gazebo Ignition (gz-sim) — What's Your Workflow in 2026?](https://www.reddit.com/r/robotics/comments/1sk6ew1/custom_world_creation_in_gazebo_ignition_gzsim/)**

The Building Editor is gone in Gazebo Ignition, so what's the best way to create custom worlds now without hand-coding raw SDF? I'm using ROS2 + Gazebo Harmonic and want to build environments like roads, terrain, and indoor spaces. I've looked at Blender → DAE → SDF, Fuel models, and heightmaps but not sure what people actually use in practice. Like building the custom 3d model and export it to sdf something kind of. Any tools, tutorials, or repos you'd recommend?

3h ago

---

**[I've finally built the Bimo Robotics Kit v1.0, an open-source bipedal robotics platform.](https://www.reddit.com/r/robotics/comments/1sjhufo/ive_finally_built_the_bimo_robotics_kit_v10_an/)**

After more than two years of solo development, I'm releasing v1.0 of the Bimo Robotics Kit. Bimo is an open-source bipedal robotics platform designed as a complete research and education kit. The core value is the full sim-to-real pipeline: you train RL locomotion models in Isaac Lab and deploy directly on the physical hardware. The v1.0 release includes: - Startup guide (zero to walking in one session) - Full MCU code for the onboard microcontroller. - Main controller board overview and pinout. - Updated Bimo API for hardware control. - Improved Isaac Lab task code for more stable sim-to-real transfer. - Pre-trained stable walking model. Turning and push recovery models are next on the Isaac Lab environment roadmap. The platform ships with a walking model as a baseline you can extend, which is kind of the point for a research kit. Check out all the details here: - Github: https://github.com/mekion/the-bimo-project - Discord: https://discord.gg/9uXsArwXHG - Mekion: https://www.mekion.com/product/ Happy to answer questions about the Isaac Lab integration, the hardware design decisions, or what it's like building this as a solo founder. Let me know what you think about the project.

21h ago

---

**[LS3 Boston Dynamics Mini Resin Printing](https://www.reddit.com/r/robotics/comments/1sj8q52/ls3_boston_dynamics_mini_resin_printing/)**

Hi everyone! I've been developing the LS3 BostonDynamics Mini quadruped for a while now. The goal was to create a modular, 3D-printable frame that can carry a Raspberry Pi. It’s still a work in progress, but the mechanical assembly is finally done! I'm happy to discuss the kinematics or electronics if anyone is interested!

1d ago

---

**[In early April, Generalist AI unveiled GEN-1, a general-purpose AI model for mastery of simple physical tasks](https://www.reddit.com/r/robotics/comments/1sjan8z/in_early_april_generalist_ai_unveiled_gen1_a/)**

Technical blog post with multiple videos: https://generalistai.com/blog/apr-02-2026-GEN-1

1d ago

---

**[Found this open-source 'Pixar lamp' while procrastinating today. the engineering under the hood is actually insane for a weekend build](https://www.reddit.com/r/robotics/comments/1sj9u8y/found_this_opensource_pixar_lamp_while/)**

I know we usually only post our own projects here, but i was procrastinating on my own codebase today and went down a rabbit hole looking at github repos from some 48h REDHackathon happening in shanghai right now (hosted by rednote I think? today is their demo day). tbh i mostly expected to see a bunch of hastily duct-taped openai wrappers and weekend spaghetti code. clicked on one of the hardware submissions called Mira. at first glance the picture just looks like a cute 3d-printed pixar lamp. I figured it was just a physical shell with a basic python script piping some face tracking coordinates directly to a couple servos. but looking at the actual code... the system architecture is surprisingly hardcore. They didnt just hardcode reactions. they built a full embodied interaction system. the pipeline goes from single camera input -> vision event extraction -> scene selection -> local bridge / safety layer -> ESP32 firmware. Instead of raw tracking they built a scene-based motion choreography abstraction. it interprets visual data into states like 'curious_observe', 'cute_probe', and 'standup_reminder'. The esp32 firmware isnt a toy either... it has a custom binary serial protocol, touch thresholds, and ack/err handling. they even built offline rehearsal scripts, fault injection, and a web director console so they could test the logic without the physical hardware glitching out on stage. Most ai right now just sits in a chat window waiting for a prompt. this thing is trying to actually notice your presence in a physical space and respond with body language and light rhythms before you even say a word. idk, seeing hardware prototypes with this level of release-oriented engineering come out of a 48h builder camp makes me feel pretty lazy today lol. its just a stark reminder that the next phase of ai probably isnt going to be on a screen, but actually sitting on our desks observing us. anyway just thought id share something cool that isnt another b2b saas wrapper. repo if anyone wants to look at the c++ / esp32 logic (not mine obviously): github.com/JunkaiWang-TheoPhy/Mira-Light-AI-That-Sees-You

1d ago

---

**[Kame Robotics unveils a compact open-source quadruped for desk-top robotics experiments](https://www.reddit.com/r/robotics/comments/1siofos/kame_robotics_unveils_a_compact_opensource/)**

1d ago

---

**[PNP Robotics: Haptic Teleoperation for data collection.](https://www.reddit.com/r/robotics/comments/1sj5dfk/pnp_robotics_haptic_teleoperation_for_data/)**

PNP Robotics: Haptic Teleoperation for data collection. At the Embodied AI Conference, we’re excited to showcase our integration of the Haply Inverse3 haptic joystick with Franka robots, enabling real-time pose control and immersive haptic feedback for intuitive teleoperation. EmbodiedAI #HapticTeleoperation #Franka #Haply #Robotics #Teleoperation

1d ago

---

---

## Google News: "robotics"

**[Robotic birds mimic mating to help bring back vanishing grouse](https://interestingengineering.com/ai-robotics/robotic-sage-grouse-conservation)**

Robotic bird decoys mimic mating rituals to help restore declining sage grouse populations in US national parks.

Interesting Engineering • 2d ago

---

**[Hidden in plain sight: Robots reveal ‘shipwreck city’ below the surface of a Washington lake](https://www.9news.com/article/news/nation-world/robotics-underwater-detection-shipwrecks-sonar-survey-remote-operated-vehicle-washington-lake-union/507-d5e09930-31c1-491f-8c8b-01f9fcbba5b8)**

'Shipwreck city': A high-tech survey has found dozens of possible wrecks in Washington state, with robotics capturing images in areas too dangerous for divers.

KUSA.com • 19h ago

---

**[Humanoid robots show off their language and boxing skills in Hong Kong](https://www.newsday.com/business/robots-humanoid-hong-kong-china-e55104)**

A humanoid robot called X2 Ultra from China's leading humanoid robot manufacturer AGIBOT has been impressing visitors in Hong Kong.

Newsday • 48m ago

---

**[UP robotics teams compete for Michigan FIRST Robotics state finals](https://www.uppermichiganssource.com/2026/04/11/up-robotics-teams-compete-michigan-first-robotics-state-finals/)**

40 teams battled during the two-day district qualifiers at Escanaba High School.

Upper Michigan's Source • 1d ago

---

**[This robot sees danger, decides its route and powers over obstacles while carrying loads](https://techxplore.com/news/2026-04-robot-danger-route-powers-obstacles.html)**

Tech Xplore • 23h ago

---

**[Humanoid robots to compete in Beijing half-marathon](https://www.scmp.com/video/sport/3349927/chinese-teams-fine-tune-robots-beijing-humanoid-half-marathon)**

Read more on the story: https://sc.mp/4obcc
  Sections of Beijing were closed off for a test run ahead of the second humanoid robot half-marathon to be held in the world. The race is scheduled to be…

South China Morning Post • 2h ago

---

**[CEO Andy Jassy shares 3 ways Amazon is innovating to make customers’ lives easier and better](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ceo-andy-jassy-robotics-rural-delivery-broadband)**

In his annual letter to shareholders, Jassy shares how robotics, faster rural delivery, and broadband connectivity for underserved customers and geographies will help improve the customer experience.

About Amazon • 2d ago

---

**[High School Robotics Teams Shine At The Granite City Regional In St. Cloud](https://wjon.com/granite-city-robotics-tournament/)**

Hundreds of high school students gathered in St. Cloud for an intense FIRST Robotics tournament, showcasing skills and collaboration in a unique three-versus-three format at River's Edge Convention Center.

WJON • 23h ago

---

**[Minth: A Small Cap Quietly Pivoting To AI And Robots (OTCMKTS:MNTHF)](https://seekingalpha.com/article/4890175-minth-a-small-cap-quietly-pivoting-to-ai-and-robots)**

Minth Group is a profitable dividend auto supplier pivoting to EV battery housings, AI data center cooling, & robotics. Learn more about MNTHF stock here.

Seeking Alpha • 1h ago

---

**[Corvus Robotics Launches Corvus Trident, an AI Powered Device That Tracks Every Pallet from Dock Door to Departure](https://markets.businessinsider.com/news/stocks/corvus-robotics-launches-corvus-trident-an-ai-powered-device-that-tracks-every-pallet-from-dock-door-to-departure-1036015241)**

ATLANTA, April  13, 2026  (GLOBE NEWSWIRE) -- (MODEX 2026, Booth  A3818 )  — Corvus Robotics  today announced Corvus Trident, a new AI powered dev...

markets.businessinsider.com • 1h ago

---

---

## YouTube Videos: "robotics"

**[New AI Robot Is Starting to Feel Human (Artificial Humans Are Here)](https://www.youtube.com/watch?v=HOgCL8lKuDc)**

Try Seedance 2.0 with Claude on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-LDckkB Realbotix just launched ...

📺 AI Revolution

👁️ 72K • 👍 1K • 💬 151 • ⏱️ 14:57 • 1d ago

---

**[Ukraine’s New Combat Robots are Absolutely Shredding Russia Right Now](https://www.youtube.com/watch?v=RvDmz7cBAcE)**

Go to https://www.artwine.com to get your limited bottle of Ukrainian sparkling wine, rescued from the cellars of Bakhmut. Must be ...

📺 Paul Warburg

👁️ 207K • 👍 18K • 💬 1K • ⏱️ 31:17 • 1d ago

---

**[Mind-Blowing Robots You Must See! Robots Just Blew Our Minds 🤖✨#singapore #ai #robotics](https://www.youtube.com/watch?v=iZBYkpuOdkk)**

📺 SS tiny labs

👁️ 1K • 👍 13 • ⏱️ 0:55 • 11h ago

---

**[Spraying robot #robot #machine #industrialrobots #automation #spray](https://www.youtube.com/watch?v=W6I2539CBP8)**

📺 zhulongfeng 6

👁️ 3K • 👍 15 • ⏱️ 0:12 • 11h ago

---

**[This Is Ridiculously Bad... Acid Anguisher Are Terrible Now | War Robots](https://www.youtube.com/watch?v=RAVXK_8ThLA)**

Acid Titan shotguns have fallen into the ground. I havent been seeing them around as much recently. But this is insane, I did not ...

📺 PREDATOR WR

👁️ 12K • 👍 469 • 💬 64 • ⏱️ 14:11 • 1d ago

---

**[Better than Lebron? Check out AI powered robot](https://www.youtube.com/watch?v=rOLlqmKskp0)**

Toyota Motor Corp. unveiled its latest AI-powered basketball robot, CUE7, on Sunday, giving the media a preview during a ...

📺 WeShow Sports

👁️ 5K • 👍 91 • 💬 16 • ⏱️ 3:02 • 1d ago

---

**[I SAW MY FiRST delivery robot #minivacay #robot #justthebells10](https://www.youtube.com/watch?v=yGJyWvJ9uS4)**

📺 Just the Bells 10

👁️ 30K • 👍 1K • 💬 67 • ⏱️ 0:33 • 2d ago

---

**[Disney&#39;s New Olaf Robot Isn&#39;t What You Think](https://www.youtube.com/watch?v=VvXhpnvjVGE)**

Everyone is getting 7 things wrong about Disney's new Olaf animatronic. I asked Imagineering how the free roaming Olaf works, ...

📺 Guide2WDW

👁️ 38K • 👍 975 • 💬 97 • ⏱️ 19:30 • 3d ago

---

**[Why the Lymow One Plus is the Best Robot Mower Not Sponsored](https://www.youtube.com/watch?v=TCBaaSISul8)**

Lymow → https://lymowtradecolimited.pxf.io/OYr2VG The Lymow One Plus isn't your average robot mower. Instead of those tiny, ...

📺 How To with Doc

👁️ 18K • 👍 987 • 💬 184 • ⏱️ 21:24 • 3d ago

---

**[AMMIT cannot even die right… War Robots](https://www.youtube.com/watch?v=Mz7zB43oDos)**

War Robots Gameplay: AMMIT with VELOS weapons is nuts! My War Robots Creator Link: https://wr.my.games/manni - Code: ...

📺 Manni-Gaming

👁️ 12K • 👍 561 • 💬 126 • ⏱️ 14:46 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

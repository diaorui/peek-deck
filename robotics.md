---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-13T10:14:17.549363+00:00'
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

**Last Updated:** April 13, 2026 at 10:14 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[massive robotic hand that produce up to11000 pound force.](https://www.reddit.com/r/robotics/comments/1sjmxyz/massive_robotic_hand_that_produce_up_to11000/)**

15h ago

---

**[Somewhere in Poland](https://www.reddit.com/r/robotics/comments/1sjhnd1/somewhere_in_poland/)**

18h ago

---

**[I've finally built the Bimo Robotics Kit v1.0, an open-source bipedal robotics platform.](https://www.reddit.com/r/robotics/comments/1sjhufo/ive_finally_built_the_bimo_robotics_kit_v10_an/)**

After more than two years of solo development, I'm releasing v1.0 of the Bimo Robotics Kit. Bimo is an open-source bipedal robotics platform designed as a complete research and education kit. The core value is the full sim-to-real pipeline: you train RL locomotion models in Isaac Lab and deploy directly on the physical hardware. The v1.0 release includes: - Startup guide (zero to walking in one session) - Full MCU code for the onboard microcontroller. - Main controller board overview and pinout. - Updated Bimo API for hardware control. - Improved Isaac Lab task code for more stable sim-to-real transfer. - Pre-trained stable walking model. Turning and push recovery models are next on the Isaac Lab environment roadmap. The platform ships with a walking model as a baseline you can extend, which is kind of the point for a research kit. Check out all the details here: - Github: https://github.com/mekion/the-bimo-project - Discord: https://discord.gg/9uXsArwXHG - Mekion: https://www.mekion.com/product/ Happy to answer questions about the Isaac Lab integration, the hardware design decisions, or what it's like building this as a solo founder. Let me know what you think about the project.

18h ago

---

**[LS3 Boston Dynamics Mini Resin Printing](https://www.reddit.com/r/robotics/comments/1sj8q52/ls3_boston_dynamics_mini_resin_printing/)**

Hi everyone! I've been developing the LS3 BostonDynamics Mini quadruped for a while now. The goal was to create a modular, 3D-printable frame that can carry a Raspberry Pi. It’s still a work in progress, but the mechanical assembly is finally done! I'm happy to discuss the kinematics or electronics if anyone is interested!

1d ago

---

**[In early April, Generalist AI unveiled GEN-1, a general-purpose AI model for mastery of simple physical tasks](https://www.reddit.com/r/robotics/comments/1sjan8z/in_early_april_generalist_ai_unveiled_gen1_a/)**

Technical blog post with multiple videos: https://generalistai.com/blog/apr-02-2026-GEN-1

1d ago

---

**[Custom World Creation in Gazebo Ignition (gz-sim) — What's Your Workflow in 2026?](https://www.reddit.com/r/robotics/comments/1sk6ew1/custom_world_creation_in_gazebo_ignition_gzsim/)**

The Building Editor is gone in Gazebo Ignition, so what's the best way to create custom worlds now without hand-coding raw SDF? I'm using ROS2 + Gazebo Harmonic and want to build environments like roads, terrain, and indoor spaces. I've looked at Blender → DAE → SDF, Fuel models, and heightmaps but not sure what people actually use in practice. Like building the custom 3d model and export it to sdf something kind of. Any tools, tutorials, or repos you'd recommend?

8m ago

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

**[ROS 2 Pan Tilt Camera](https://www.reddit.com/r/robotics/comments/1sjgxh4/ros_2_pan_tilt_camera/)**

Recently I was spending time building my ROS 2 robots and one functionality I always wanted was Pan Tilt camera, so I built it 🚀 I designed motor housing with CAD, and used micro-ros to control MCU. Lastly I made simple PID object follower using high speed, low latency Isaac ROS object detection running on Robot’s Jetson.

🔗 [youtu.be](https://youtu.be/CmBWlHjohjg) • 19h ago

---

---

## Google News: "robotics"

**[Robotic birds mimic mating to help bring back vanishing grouse](https://interestingengineering.com/ai-robotics/robotic-sage-grouse-conservation)**

Robotic bird decoys mimic mating rituals to help restore declining sage grouse populations in US national parks.

Interesting Engineering • 2d ago

---

**[Hidden in plain sight: Robots reveal ‘shipwreck city’ below the surface of a Washington lake](https://www.9news.com/article/news/nation-world/robotics-underwater-detection-shipwrecks-sonar-survey-remote-operated-vehicle-washington-lake-union/507-d5e09930-31c1-491f-8c8b-01f9fcbba5b8)**

'Shipwreck city': A high-tech survey has found dozens of possible wrecks in Washington state, with robotics capturing images in areas too dangerous for divers.

KUSA.com • 15h ago

---

**[Unitree’s H1 robot hits 10 m/s sprint speed, getting close to Usain Bolt’s 100m world record](https://www.globaltimes.cn/page/202604/1358712.shtml)**

Chinese robotics startup Unitree Robotics released a video on Saturday showing its H1 robot reached a sprint speed of up to 10 meters per second, noting that the humanoid robot broke the world record again.

Global Times • 23h ago

---

**[UP robotics teams compete for Michigan FIRST Robotics state finals](https://www.uppermichiganssource.com/2026/04/11/up-robotics-teams-compete-michigan-first-robotics-state-finals/)**

40 teams battled during the two-day district qualifiers at Escanaba High School.

Upper Michigan's Source • 1d ago

---

**[CEO Andy Jassy shares 3 ways Amazon is innovating to make customers’ lives easier and better](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ceo-andy-jassy-robotics-rural-delivery-broadband)**

In his annual letter to shareholders, Jassy shares how robotics, faster rural delivery, and broadband connectivity for underserved customers and geographies will help improve the customer experience.

About Amazon • 2d ago

---

**[Students shine at Wolfpack Robotics’ Robo Rally](https://www.timesleader.com/news/1738534/students-shine-at-wolfpack-robotics-robo-rally)**

<p>PLAINS TWP. — It was a celebration of robotics on Saturday as regional schools gathered at Wilkes-Barre Area High School for Wolfpack Robotics’ second Robo Rally.</p>

Times Leader • 1d ago

---

**[Israel's 10D bets on physical AI and deep tech as its next frontier](https://www.ynetnews.com/business/article/hjodjvfnbe)**

The early-stage fund, which backed Mentee Robotics from its Series A, is doubling down on hardware-meets-AI companies — a space many still shy away from

ynetnews • 15h ago

---

**[Harding FIRST robotics team going to nationals](https://www.tribtoday.com/news/local-news/2026/04/harding-first-robotics-team-going-to-nationals/)**

WARREN — The Warren G. Harding High School FIRST Robotics Team E.L.I.T.E (Encouraging Learning in Technology and Engineering)  48, ...

tribtoday.com • 6h ago

---

**[High School Robotics Teams Shine At The Granite City Regional In St. Cloud](https://wjon.com/granite-city-robotics-tournament/)**

Hundreds of high school students gathered in St. Cloud for an intense FIRST Robotics tournament, showcasing skills and collaboration in a unique three-versus-three format at River's Edge Convention Center.

WJON • 19h ago

---

**[Humanoid robots take over manual job at auto parts plant](https://www.nbcnews.com/video/humanoid-robots-take-over-manual-job-at-auto-parts-plant-261061189841)**

Humanoid robots are being used for some manual tasks at the Schaeffler auto parts plant in Cheraw, S.C. Proponents argue that the robots will not replace humans but rather displace them to different roles in the company. NBC News’ Brian Cheung gets a firsthand look at how the robots work and how they’re impacting the workforce.

NBC News • 3d ago

---

---

## YouTube Videos: "robotics"

**[New AI Robot Is Starting to Feel Human (Artificial Humans Are Here)](https://www.youtube.com/watch?v=HOgCL8lKuDc)**

Try Seedance 2.0 with Claude on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-LDckkB Realbotix just launched ...

📺 AI Revolution

👁️ 70K • 👍 1K • 💬 150 • ⏱️ 14:57 • 1d ago

---

**[Ukraine’s New Combat Robots are Absolutely Shredding Russia Right Now](https://www.youtube.com/watch?v=RvDmz7cBAcE)**

Go to https://www.artwine.com to get your limited bottle of Ukrainian sparkling wine, rescued from the cellars of Bakhmut. Must be ...

📺 Paul Warburg

👁️ 202K • 👍 18K • 💬 1K • ⏱️ 31:17 • 1d ago

---

**[Mind-Blowing Robots You Must See! Robots Just Blew Our Minds 🤖✨#singapore #ai #robotics](https://www.youtube.com/watch?v=iZBYkpuOdkk)**

📺 SS tiny labs

👁️ 1K • 👍 13 • ⏱️ 0:55 • 8h ago

---

**[This Is Ridiculously Bad... Acid Anguisher Are Terrible Now | War Robots](https://www.youtube.com/watch?v=RAVXK_8ThLA)**

Acid Titan shotguns have fallen into the ground. I havent been seeing them around as much recently. But this is insane, I did not ...

📺 PREDATOR WR

👁️ 11K • 👍 463 • 💬 63 • ⏱️ 14:11 • 22h ago

---

**[Better than Lebron? Check out AI powered robot](https://www.youtube.com/watch?v=rOLlqmKskp0)**

Toyota Motor Corp. unveiled its latest AI-powered basketball robot, CUE7, on Sunday, giving the media a preview during a ...

📺 WeShow Sports

👁️ 4K • 👍 70 • 💬 11 • ⏱️ 3:02 • 23h ago

---

**[Spraying robot #robot #machine #industrialrobots #automation #spray](https://www.youtube.com/watch?v=W6I2539CBP8)**

📺 zhulongfeng 6

👁️ 2K • 👍 9 • ⏱️ 0:12 • 8h ago

---

**[Disney&#39;s New Olaf Robot Isn&#39;t What You Think](https://www.youtube.com/watch?v=VvXhpnvjVGE)**

Everyone is getting 7 things wrong about Disney's new Olaf animatronic. I asked Imagineering how the free roaming Olaf works, ...

📺 Guide2WDW

👁️ 38K • 👍 959 • 💬 96 • ⏱️ 19:30 • 3d ago

---

**[I SAW MY FiRST delivery robot #minivacay #robot #justthebells10](https://www.youtube.com/watch?v=yGJyWvJ9uS4)**

📺 Just the Bells 10

👁️ 30K • 👍 1K • 💬 67 • ⏱️ 0:33 • 2d ago

---

**[South Korea Is Building Robots the World Didn’t See Coming!](https://www.youtube.com/watch?v=H09m8a3oL_4)**

South Korea is building robots you've only seen in movies, from giant walking machines to exoskeletons that give people back ...

📺 DeCode

👁️ 57K • 👍 1K • 💬 94 • ⏱️ 14:45 • 3d ago

---

**[CURIE IS ACTUALLY OVERPOWERED WITH BASILEUS! SECRET STRONG ROBOT? (War Robots)](https://www.youtube.com/watch?v=lNqyCD5fuxs)**

In this video I tested out the Curie with Basileus. https://wr.my.games/Wolfblood7.

📺 Wolfblood7

👁️ 3K • 👍 147 • 💬 34 • ⏱️ 13:17 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

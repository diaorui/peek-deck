---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-13T02:47:01.476774+00:00'
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

**Last Updated:** April 13, 2026 at 02:47 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Somewhere in Poland](https://www.reddit.com/r/robotics/comments/1sjhnd1/somewhere_in_poland/)**

11h ago

---

**[massive robotic hand that produce up to11000 pound force.](https://www.reddit.com/r/robotics/comments/1sjmxyz/massive_robotic_hand_that_produce_up_to11000/)**

7h ago

---

**[LS3 Boston Dynamics Mini Resin Printing](https://www.reddit.com/r/robotics/comments/1sj8q52/ls3_boston_dynamics_mini_resin_printing/)**

Hi everyone! I've been developing the LS3 BostonDynamics Mini quadruped for a while now. The goal was to create a modular, 3D-printable frame that can carry a Raspberry Pi. It’s still a work in progress, but the mechanical assembly is finally done! I'm happy to discuss the kinematics or electronics if anyone is interested!

18h ago

---

**[I've finally built the Bimo Robotics Kit v1.0, an open-source bipedal robotics platform.](https://www.reddit.com/r/robotics/comments/1sjhufo/ive_finally_built_the_bimo_robotics_kit_v10_an/)**

After more than two years of solo development, I'm releasing v1.0 of the Bimo Robotics Kit. Bimo is an open-source bipedal robotics platform designed as a complete research and education kit. The core value is the full sim-to-real pipeline: you train RL locomotion models in Isaac Lab and deploy directly on the physical hardware. The v1.0 release includes: - Startup guide (zero to walking in one session) - Full MCU code for the onboard microcontroller. - Main controller board overview and pinout. - Updated Bimo API for hardware control. - Improved Isaac Lab task code for more stable sim-to-real transfer. - Pre-trained stable walking model. Turning and push recovery models are next on the Isaac Lab environment roadmap. The platform ships with a walking model as a baseline you can extend, which is kind of the point for a research kit. Check out all the details here: - Github: https://github.com/mekion/the-bimo-project - Discord: https://discord.gg/9uXsArwXHG - Mekion: https://www.mekion.com/product/ Happy to answer questions about the Isaac Lab integration, the hardware design decisions, or what it's like building this as a solo founder. Let me know what you think about the project.

11h ago

---

**[In early April, Generalist AI unveiled GEN-1, a general-purpose AI model for mastery of simple physical tasks](https://www.reddit.com/r/robotics/comments/1sjan8z/in_early_april_generalist_ai_unveiled_gen1_a/)**

Technical blog post with multiple videos: https://generalistai.com/blog/apr-02-2026-GEN-1

16h ago

---

**[Found this open-source 'Pixar lamp' while procrastinating today. the engineering under the hood is actually insane for a weekend build](https://www.reddit.com/r/robotics/comments/1sj9u8y/found_this_opensource_pixar_lamp_while/)**

I know we usually only post our own projects here, but i was procrastinating on my own codebase today and went down a rabbit hole looking at github repos from some 48h REDHackathon happening in shanghai right now (hosted by rednote I think? today is their demo day). tbh i mostly expected to see a bunch of hastily duct-taped openai wrappers and weekend spaghetti code. clicked on one of the hardware submissions called Mira. at first glance the picture just looks like a cute 3d-printed pixar lamp. I figured it was just a physical shell with a basic python script piping some face tracking coordinates directly to a couple servos. but looking at the actual code... the system architecture is surprisingly hardcore. They didnt just hardcode reactions. they built a full embodied interaction system. the pipeline goes from single camera input -> vision event extraction -> scene selection -> local bridge / safety layer -> ESP32 firmware. Instead of raw tracking they built a scene-based motion choreography abstraction. it interprets visual data into states like 'curious_observe', 'cute_probe', and 'standup_reminder'. The esp32 firmware isnt a toy either... it has a custom binary serial protocol, touch thresholds, and ack/err handling. they even built offline rehearsal scripts, fault injection, and a web director console so they could test the logic without the physical hardware glitching out on stage. Most ai right now just sits in a chat window waiting for a prompt. this thing is trying to actually notice your presence in a physical space and respond with body language and light rhythms before you even say a word. idk, seeing hardware prototypes with this level of release-oriented engineering come out of a 48h builder camp makes me feel pretty lazy today lol. its just a stark reminder that the next phase of ai probably isnt going to be on a screen, but actually sitting on our desks observing us. anyway just thought id share something cool that isnt another b2b saas wrapper. repo if anyone wants to look at the c++ / esp32 logic (not mine obviously): github.com/JunkaiWang-TheoPhy/Mira-Light-AI-That-Sees-You

17h ago

---

**[Kame Robotics unveils a compact open-source quadruped for desk-top robotics experiments](https://www.reddit.com/r/robotics/comments/1siofos/kame_robotics_unveils_a_compact_opensource/)**

1d ago

---

**[Issues with axis 0 in odive 3.6 clones](https://www.reddit.com/r/robotics/comments/1sjw683/issues_with_axis_0_in_odive_36_clones/)**

I bought a Chinese clone ODrive 3.6 (56V) from Banggood to run two hoverboard motors, but I’m having a weird issue where Axis 0 won’t work properly while Axis 1 works fine. Axis 0 sometimes makes it through the motor calibration phase, but then fails during the encoder polarity step. Other times it just constantly throws a DRV_FAULT, but last_drv_fault stays at 0, which is confusing. At first I assumed the board was faulty, so I ordered two more similar boards from AliExpress but both of them have the exact same issue: Axis 0 doesn’t work at all, Axis 1 is fine. I’ve tried: lowering calibration current original firmware firmware versions 0.5.4 and 0.5.6 pretty much every other troubleshooting step I could think of Still no luck. Has anyone run into this issue with these clone ODrive boards and managed to fix it? #odrive #odesc #Hoverboard #FOC #motor

1h ago

---

**[PNP Robotics: Haptic Teleoperation for data collection.](https://www.reddit.com/r/robotics/comments/1sj5dfk/pnp_robotics_haptic_teleoperation_for_data/)**

PNP Robotics: Haptic Teleoperation for data collection. At the Embodied AI Conference, we’re excited to showcase our integration of the Haply Inverse3 haptic joystick with Franka robots, enabling real-time pose control and immersive haptic feedback for intuitive teleoperation. EmbodiedAI #HapticTeleoperation #Franka #Haply #Robotics #Teleoperation

21h ago

---

**[GIL (General Intelligence Layer)](https://www.reddit.com/r/robotics/comments/1sjnx41/gil_general_intelligence_layer/)**

Hello everyone, a few months ago i had this idea of a layer that helps Robis unterstand the world. with the Help of a few tools that are generalized an AI Agent can steer any Robot and the engineers only need to change the control layer. I open sourced the whole thing and sat together with universities in switzerland as well as robotic companies in europe. All of them are very interested to make this happen and i will continue to sit together with them to make this project happen. If you are interested as well feel free to clone it and try it out 😇 I have opened the Github Repo to the Public for research use. If you have Questions feel free to ask, i will post more infos in the Comments.

🔗 [GitHub](https://github.com/beyondExp/GIL) • 7h ago

---

---

## Google News: "robotics"

**[Hidden in plain sight: Robots reveal ‘shipwreck city’ below the surface of a Washington lake](https://www.kare11.com/article/news/nation-world/robotics-underwater-detection-shipwrecks-sonar-survey-remote-operated-vehicle-washington-lake-union/507-d5e09930-31c1-491f-8c8b-01f9fcbba5b8)**

'Shipwreck city': A high-tech survey has found dozens of possible wrecks in Washington state, with robotics capturing images in areas too dangerous for divers.

kare11.com • 8h ago

---

**[UP robotics teams compete for Michigan FIRST Robotics state finals](https://www.uppermichiganssource.com/2026/04/11/up-robotics-teams-compete-michigan-first-robotics-state-finals/)**

40 teams battled during the two-day district qualifiers at Escanaba High School.

Upper Michigan's Source • 1d ago

---

**[Unitree’s H1 robot hits 10 m/s sprint speed, getting close to Usain Bolt’s 100m world record](https://www.globaltimes.cn/page/202604/1358712.shtml)**

Chinese robotics startup Unitree Robotics released a video on Saturday showing its H1 robot reached a sprint speed of up to 10 meters per second, noting that the humanoid robot broke the world record again.

Global Times • 16h ago

---

**[New humanoid robots replacing workers in factories](https://www.nbcnews.com/video/shorts/new-humanoid-robots-replacing-workers-in-factories-261041221991)**

Meet 'Digit', a humanoid robotic worker made by Agility Robotics, now part of a new wave of robots replacing workers at companies like Schaeffler, Toyota, and GXO. NBC News' Brian Cheung takes a look.

NBC News • 3d ago

---

**[CEO Andy Jassy shares 3 ways Amazon is innovating to make customers’ lives easier and better](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ceo-andy-jassy-robotics-rural-delivery-broadband)**

In his annual letter to shareholders, Jassy shares how robotics, faster rural delivery, and broadband connectivity for underserved customers and geographies will help improve the customer experience.

About Amazon • 2d ago

---

**[High School Robotics Teams Shine At The Granite City Regional In St. Cloud](https://wjon.com/granite-city-robotics-tournament/)**

Hundreds of high school students gathered in St. Cloud for an intense FIRST Robotics tournament, showcasing skills and collaboration in a unique three-versus-three format at River's Edge Convention Center.

WJON • 12h ago

---

**[Israel's 10D bets on physical AI and deep tech as its next frontier](https://www.ynetnews.com/business/article/hjodjvfnbe)**

The early-stage fund, which backed Mentee Robotics from its Series A, is doubling down on hardware-meets-AI companies — a space many still shy away from

ynetnews • 7h ago

---

**[Opinion | Meet Abi, the AI-powered robot companion for senior care](https://www.washingtonpost.com/opinions/2026/04/09/ai-robot-senior-care-abi/)**

This new tech from Australia is coming to America’s senior care facilities.

The Washington Post • 2d ago

---

**[Students shine at Wolfpack Robotics’ Robo Rally](https://www.timesleader.com/news/1738534/students-shine-at-wolfpack-robotics-robo-rally)**

<p>PLAINS TWP. — It was a celebration of robotics on Saturday as regional schools gathered at Wilkes-Barre Area High School for Wolfpack Robotics’ second Robo Rally.</p>

Times Leader • 1d ago

---

**[China’s Robotics Champion Is Going Public. Its PLA Ties and Western Dependence Aren’t.](https://www.kharon.com/brief/unitree-robotics-ipo-china-pla-robot-wolf)**

The Shanghai IPO of Unitree Robotics is “part of China’s broader positioning in the global race for physical AI,” Sunny Cheung of the Jamestown Foundation said. But its filings tell only part of the story.

Kharon • 3d ago

---

---

## YouTube Videos: "robotics"

**[New AI Robot Is Starting to Feel Human (Artificial Humans Are Here)](https://www.youtube.com/watch?v=HOgCL8lKuDc)**

Try Seedance 2.0 with Claude on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-LDckkB Realbotix just launched ...

📺 AI Revolution

👁️ 62K • 👍 1K • 💬 139 • ⏱️ 14:57 • 1d ago

---

**[This Is Ridiculously Bad... Acid Anguisher Are Terrible Now | War Robots](https://www.youtube.com/watch?v=RAVXK_8ThLA)**

Acid Titan shotguns have fallen into the ground. I havent been seeing them around as much recently. But this is insane, I did not ...

📺 PREDATOR WR

👁️ 8K • 👍 413 • 💬 61 • ⏱️ 14:11 • 14h ago

---

**[Disney&#39;s New Olaf Robot Isn&#39;t What You Think](https://www.youtube.com/watch?v=VvXhpnvjVGE)**

Everyone is getting 7 things wrong about Disney's new Olaf animatronic. I asked Imagineering how the free roaming Olaf works, ...

📺 Guide2WDW

👁️ 36K • 👍 926 • 💬 96 • ⏱️ 19:30 • 3d ago

---

**[CURIE IS ACTUALLY OVERPOWERED WITH BASILEUS! SECRET STRONG ROBOT? (War Robots)](https://www.youtube.com/watch?v=lNqyCD5fuxs)**

In this video I tested out the Curie with Basileus. https://wr.my.games/Wolfblood7.

📺 Wolfblood7

👁️ 3K • 👍 138 • 💬 33 • ⏱️ 13:17 • 18h ago

---

**[Better than Lebron? Check out AI powered robot](https://www.youtube.com/watch?v=rOLlqmKskp0)**

Toyota Motor Corp. unveiled its latest AI-powered basketball robot, CUE7, on Sunday, giving the media a preview during a ...

📺 WeShow Sports

👁️ 1K • 👍 28 • 💬 8 • ⏱️ 3:02 • 15h ago

---

**[The Fastest Robots I&#39;ve Seen in Person](https://www.youtube.com/watch?v=TEWUaD9BmNE)**

I've been to CES (Las Vegas, Nevada), World Robot Conference (Beijing, China), and IREX (Tokyo, Japan). These are the fastest ...

📺 Automatic Addison

👁️ 1K • 👍 47 • 💬 8 • ⏱️ 1:38 • 14h ago

---

**[VEX Robotics | 2026-2027 Game Name Reveal](https://www.youtube.com/watch?v=J6xuR3l0blM)**

SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Start the clock! VEX Worlds ...

📺 VEX Robotics

👁️ 115K • 👍 1K • 💬 181 • ⏱️ 1:30 • 2d ago

---

**[I SAW MY FiRST delivery robot #minivacay #robot #justthebells10](https://www.youtube.com/watch?v=yGJyWvJ9uS4)**

📺 Just the Bells 10

👁️ 29K • 👍 1K • 💬 66 • ⏱️ 0:33 • 2d ago

---

**[Unitree H1 Humanoid Robot Breaks Limits at 22.4 MPH](https://www.youtube.com/watch?v=sfcqAZcWoMo)**

The Unitree H1 humanoid robot just reached an incredible 10 meters per second, which is about 22.4 miles per hour, putting it ...

📺 DPCcars

👁️ 62K • 👍 257 • 💬 117 • ⏱️ 1:24 • 1d ago

---

**[Dual Shooter To Turret Transition | 9233 Luminous Robotics Team | REBUILT Pit Stop](https://www.youtube.com/watch?v=lIDSk8s68Qc)**

Dual Shooter To Turret Transition | 9233 Luminous Robotics Team | REBUILT Pit Stop This video is supported by Kettering ...

📺 FUN Robotics Network

👁️ 995 • 👍 24 • ⏱️ 0:51 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*

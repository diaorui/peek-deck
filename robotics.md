---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-12T14:08:40.469289+00:00'
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

**Last Updated:** April 12, 2026 at 14:08 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[LS3 Boston Dynamics Mini Resin Printing](https://www.reddit.com/r/robotics/comments/1sj8q52/ls3_boston_dynamics_mini_resin_printing/)**

Hi everyone! I've been developing the LS3 BostonDynamics Mini quadruped for a while now. The goal was to create a modular, 3D-printable frame that can carry a Raspberry Pi. It’s still a work in progress, but the mechanical assembly is finally done! I'm happy to discuss the kinematics or electronics if anyone is interested!

5h ago

---

**[In early April, Generalist AI unveiled GEN-1, a general-purpose AI model for mastery of simple physical tasks](https://www.reddit.com/r/robotics/comments/1sjan8z/in_early_april_generalist_ai_unveiled_gen1_a/)**

Technical blog post with multiple videos: https://generalistai.com/blog/apr-02-2026-GEN-1

3h ago

---

**[Kame Robotics unveils a compact open-source quadruped for desk-top robotics experiments](https://www.reddit.com/r/robotics/comments/1siofos/kame_robotics_unveils_a_compact_opensource/)**

21h ago

---

**[Found this open-source 'Pixar lamp' while procrastinating today. the engineering under the hood is actually insane for a weekend build](https://www.reddit.com/r/robotics/comments/1sj9u8y/found_this_opensource_pixar_lamp_while/)**

I know we usually only post our own projects here, but i was procrastinating on my own codebase today and went down a rabbit hole looking at github repos from some 48h REDHackathon happening in shanghai right now (hosted by rednote I think? today is their demo day). tbh i mostly expected to see a bunch of hastily duct-taped openai wrappers and weekend spaghetti code. clicked on one of the hardware submissions called Mira. at first glance the picture just looks like a cute 3d-printed pixar lamp. I figured it was just a physical shell with a basic python script piping some face tracking coordinates directly to a couple servos. but looking at the actual code... the system architecture is surprisingly hardcore. They didnt just hardcode reactions. they built a full embodied interaction system. the pipeline goes from single camera input -> vision event extraction -> scene selection -> local bridge / safety layer -> ESP32 firmware. Instead of raw tracking they built a scene-based motion choreography abstraction. it interprets visual data into states like 'curious_observe', 'cute_probe', and 'standup_reminder'. The esp32 firmware isnt a toy either... it has a custom binary serial protocol, touch thresholds, and ack/err handling. they even built offline rehearsal scripts, fault injection, and a web director console so they could test the logic without the physical hardware glitching out on stage. Most ai right now just sits in a chat window waiting for a prompt. this thing is trying to actually notice your presence in a physical space and respond with body language and light rhythms before you even say a word. idk, seeing hardware prototypes with this level of release-oriented engineering come out of a 48h builder camp makes me feel pretty lazy today lol. its just a stark reminder that the next phase of ai probably isnt going to be on a screen, but actually sitting on our desks observing us. anyway just thought id share something cool that isnt another b2b saas wrapper. repo if anyone wants to look at the c++ / esp32 logic (not mine obviously): github.com/JunkaiWang-TheoPhy/Mira-Light-AI-That-Sees-You

4h ago

---

**[PNP Robotics: Haptic Teleoperation for data collection.](https://www.reddit.com/r/robotics/comments/1sj5dfk/pnp_robotics_haptic_teleoperation_for_data/)**

PNP Robotics: Haptic Teleoperation for data collection. At the Embodied AI Conference, we’re excited to showcase our integration of the Haply Inverse3 haptic joystick with Franka robots, enabling real-time pose control and immersive haptic feedback for intuitive teleoperation. EmbodiedAI #HapticTeleoperation #Franka #Haply #Robotics #Teleoperation

8h ago

---

**[Unitree H1 at 10 m/s (Leg length: 0.4+0.4=0.8m, body weight: approx. 62kg)](https://www.reddit.com/r/robotics/comments/1sigfd3/unitree_h1_at_10_ms_leg_length_040408m_body/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2042912788717408509

1d ago

---

**[MIT CSAIL Director Daniela Rus on the Future of Robotics](https://www.reddit.com/r/robotics/comments/1sjcj62/mit_csail_director_daniela_rus_on_the_future_of/)**

MIT’s Daniela Rus talks about how robotics is starting to overlap more with biology and AI. One project uses machine learning to analyze sperm whale sounds, finding repeatable patterns and even predicting what comes next. There’s also work inspired by animals like octopuses, looking at more flexible, distributed control systems instead of rigid robot designs.

🔗 [Automate](http://automate.org/robotics/industry-insights/mit-csail-director-daniela-rus-on-the-future-of-robotics) • 2h ago

---

**[People with 10+ years in industrial automation - is the robotics hype matching reality on the floor?](https://www.reddit.com/r/robotics/comments/1siej3f/people_with_10_years_in_industrial_automation_is/)**

I've been seeing a lot of noise from the tech world about robotics being the next big wave. Curious what people actually deploying and maintaining these systems think. What's working, what's vaporware, and what does the gap between a demo and a real production deployment actually look like?

1d ago

---

**[cambotv1 update 12-04-2026 #automobile #robotics #cad #raspberrypi #rob...](https://www.reddit.com/r/robotics/comments/1sj9b4i/cambotv1_update_12042026_automobile_robotics_cad/)**

I got finnaly my orp-cambotv1 working. It was a struggle i had to change my motor holders and print a new 12v motor holder(still possible work in progress) but i did it. i only need to to make the code more readable and documentible

🔗 [youtube.com](https://youtube.com/shorts/lO5StFCWxCo?si=HMFmLq7GH5zTx3M_) • 5h ago

---

**[Found this open-source 'Pixar lamp' while procrastinating today. the engineering under the hood is actually insane for a weekend build](https://www.reddit.com/r/robotics/comments/1sin63l/found_this_opensource_pixar_lamp_while/)**

I know we usually only post our own projects here, but i was procrastinating on my own codebase today and went down a rabbit hole looking at github repos from some 48h REDHackathon happening in shanghai right now (hosted by rednote I think? today is their demo day). tbh i mostly expected to see a bunch of hastily duct-taped openai wrappers and weekend spaghetti code. clicked on one of the hardware submissions called Mira. at first glance the picture just looks like a cute 3d-printed pixar lamp. I figured it was just a physical shell with a basic python script piping some face tracking coordinates directly to a couple servos. but looking at the actual code... the system architecture is surprisingly hardcore. They didnt just hardcode reactions. they built a full embodied interaction system. the pipeline goes from single camera input -> vision event extraction -> scene selection -> local bridge / safety layer -> ESP32 firmware. Instead of raw tracking they built a scene-based motion choreography abstraction. it interprets visual data into states like 'curious_observe', 'cute_probe', and 'standup_reminder'. The esp32 firmware isnt a toy either... it has a custom binary serial protocol, touch thresholds, and ack/err handling. they even built offline rehearsal scripts, fault injection, and a web director console so they could test the logic without the physical hardware glitching out on stage. Most ai right now just sits in a chat window waiting for a prompt. this thing is trying to actually notice your presence in a physical space and respond with body language and light rhythms before you even say a word. idk, seeing hardware prototypes with this level of release-oriented engineering come out of a 48h builder camp makes me feel pretty lazy today lol. its just a stark reminder that the next phase of ai probably isnt going to be on a screen, but actually sitting on our desks observing us. anyway just thought id share something cool that isnt another b2b saas wrapper. repo if anyone wants to look at the c++ / esp32 logic (not mine obviously): github.com/JunkaiWang-TheoPhy/Mira-Light-AI-That-Sees-You

21h ago

---

---

## Google News: "robotics"

**[Building the Future of Texas Robotics](https://news.utexas.edu/2026/04/09/building-the-future-of-texas-robotics/)**

Deepu Talla helps bring the future of robotics closer to reality through the Nvidia-Talla Endowment for Texas Robotics.

The University of Texas at Austin • 2d ago

---

**[CEO Andy Jassy shares 3 ways Amazon is innovating to make customers’ lives easier and better](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ceo-andy-jassy-robotics-rural-delivery-broadband)**

In his annual letter to shareholders, Jassy shares how robotics, faster rural delivery, and broadband connectivity for underserved customers and geographies will help improve the customer experience.

About Amazon • 1d ago

---

**[Opinion | Meet Abi, the AI-powered robot companion for senior care](https://www.washingtonpost.com/opinions/2026/04/09/ai-robot-senior-care-abi/)**

This new tech from Australia is coming to America’s senior care facilities.

The Washington Post • 2d ago

---

**[Humanoid robots hit mass production in China](https://www.foxnews.com/tech/humanoid-robots-hit-mass-production-china)**

A Chinese factory is producing humanoid robots every 30 minutes, marking a shift toward large-scale manufacturing and broader adoption.

Fox News • 2d ago

---

**[Electrofluidic fiber muscles could enable silent robotic systems](https://techxplore.com/news/2026-04-electrofluidic-fiber-muscles-enable-silent.html)**

Tech Xplore • 2d ago

---

**[New humanoid robots replacing workers in factories](https://www.nbcnews.com/video/shorts/new-humanoid-robots-replacing-workers-in-factories-261041221991)**

Meet 'Digit', a humanoid robotic worker made by Agility Robotics, now part of a new wave of robots replacing workers at companies like Schaeffler, Toyota, and GXO. NBC News' Brian Cheung takes a look.

NBC News • 2d ago

---

**[Robotic birds mimic mating to help bring back vanishing grouse](https://interestingengineering.com/ai-robotics/robotic-sage-grouse-conservation)**

Robotic bird decoys mimic mating rituals to help restore declining sage grouse populations in US national parks.

Interesting Engineering • 1d ago

---

**[National robotics push caught in delayed Trump-Xi meeting](https://www.politico.com/news/2026/04/09/national-robotics-trump-xi-china-00861918)**

Politico • 3d ago

---

**[China’s Robotics Champion Is Going Public. Its PLA Ties and Western Dependence Aren’t.](https://www.kharon.com/brief/unitree-robotics-ipo-china-pla-robot-wolf)**

The Shanghai IPO of Unitree Robotics is “part of China’s broader positioning in the global race for physical AI,” Sunny Cheung of the Jamestown Foundation said. But its filings tell only part of the story.

Kharon • 2d ago

---

**[Resolved: Laundry folding is the future of home robotics](https://www.pcworld.com/article/3110605/resolved-laundry-folding-is-the-future-of-home-robotics.html)**

Hot on the heels of LG's laundry-folding robot showcased at CES, Syncere has released a much more elegant home robot that marries a floor lamp to laundry-folding functions.

PCWorld • 2d ago

---

---

## YouTube Videos: "robotics"

**[New AI Robot Is Starting to Feel Human (Artificial Humans Are Here)](https://www.youtube.com/watch?v=HOgCL8lKuDc)**

Try Seedance 2.0 with Claude on Higgsfield: https://higgsfield.ai/s/seedance-2-0-airevolutionx-LDckkB Realbotix just launched ...

📺 AI Revolution

👁️ 43K • 👍 860 • 💬 116 • ⏱️ 14:57 • 14h ago

---

**[Ukraine’s New Combat Robots are Absolutely Shredding Russia Right Now](https://www.youtube.com/watch?v=RvDmz7cBAcE)**

Go to https://www.artwine.com to get your limited bottle of Ukrainian sparkling wine, rescued from the cellars of Bakhmut. Must be ...

📺 Paul Warburg

👁️ 108K • 👍 12K • 💬 827 • ⏱️ 31:17 • 10h ago

---

**[AI agent in a robot does exactly what experts warned](https://www.youtube.com/watch?v=woTy4dTiT20)**

Could AI become dangerous? Can we trust AI Agents? AGI. Use code insideai at https://incogni.com/insideai to get an exclusive ...

📺 InsideAI

👁️ 473K • 👍 19K • 💬 2K • ⏱️ 16:24 • 2d ago

---

**[Humanoid robots take over manual job at auto parts plant](https://www.youtube.com/watch?v=JMxKpo_Llt8)**

Humanoid robots are being used for some manual tasks at the Schaeffler auto parts plant in Cheraw, S.C. Proponents argue that ...

📺 NBC News

👁️ 90K • 👍 1K • 💬 634 • ⏱️ 4:56 • 2d ago

---

**[Toyota unveils AI basketball robot CUE7](https://www.youtube.com/watch?v=Nm3fEub7U4w)**

Toyota Motor Corp. showcased its latest AI-powered basketball robot, CUE7, showcasing advances in AI robotics. The robot will ...

📺 Al Jazeera English

👁️ 2K • 👍 67 • 💬 3 • ⏱️ 0:42 • 1h ago

---

**[Disney&#39;s New Olaf Robot Isn&#39;t What You Think](https://www.youtube.com/watch?v=VvXhpnvjVGE)**

Everyone is getting 7 things wrong about Disney's new Olaf animatronic. I asked Imagineering how the free roaming Olaf works, ...

📺 Guide2WDW

👁️ 30K • 👍 807 • 💬 91 • ⏱️ 19:30 • 2d ago

---

**[Unitree H1 Humanoid Robot Breaks Limits at 22.4 MPH](https://www.youtube.com/watch?v=sfcqAZcWoMo)**

The Unitree H1 humanoid robot just reached an incredible 10 meters per second, which is about 22.4 miles per hour, putting it ...

📺 DPCcars

👁️ 33K • 👍 209 • 💬 71 • ⏱️ 1:24 • 1d ago

---

**[I SAW MY FiRST delivery robot #minivacay #robot #justthebells10](https://www.youtube.com/watch?v=yGJyWvJ9uS4)**

📺 Just the Bells 10

👁️ 28K • 👍 1K • 💬 60 • ⏱️ 0:33 • 1d ago

---

**[10m/s!! Unitree Breaks the World Record Again😊](https://www.youtube.com/watch?v=zoMDadPQLKA)**

With the physique of an ordinary person, running at a world champion's speed! Leg length: 0.4+0.4=0.8m, body weight: approx.

📺 Unitree Robotics

👁️ 1.8M • 👍 1K • 💬 200 • ⏱️ 0:31 • 1d ago

---

**[Why the Lymow One Plus is the Best Robot Mower Not Sponsored](https://www.youtube.com/watch?v=TCBaaSISul8)**

Lymow → https://lymowtradecolimited.pxf.io/OYr2VG The Lymow One Plus isn't your average robot mower. Instead of those tiny, ...

📺 How To with Doc

👁️ 15K • 👍 873 • 💬 162 • ⏱️ 21:24 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

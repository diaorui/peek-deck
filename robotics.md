---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-11T22:34:02.257179+00:00'
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

**Last Updated:** April 11, 2026 at 22:34 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Kame Robotics unveils a compact open-source quadruped for desk-top robotics experiments](https://www.reddit.com/r/robotics/comments/1siofos/kame_robotics_unveils_a_compact_opensource/)**

5h ago

---

**[Unitree H1 at 10 m/s (Leg length: 0.4+0.4=0.8m, body weight: approx. 62kg)](https://www.reddit.com/r/robotics/comments/1sigfd3/unitree_h1_at_10_ms_leg_length_040408m_body/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2042912788717408509

11h ago

---

**[People with 10+ years in industrial automation - is the robotics hype matching reality on the floor?](https://www.reddit.com/r/robotics/comments/1siej3f/people_with_10_years_in_industrial_automation_is/)**

I've been seeing a lot of noise from the tech world about robotics being the next big wave. Curious what people actually deploying and maintaining these systems think. What's working, what's vaporware, and what does the gap between a demo and a real production deployment actually look like?

12h ago

---

**[Found this open-source 'Pixar lamp' while procrastinating today. the engineering under the hood is actually insane for a weekend build](https://www.reddit.com/r/robotics/comments/1sin63l/found_this_opensource_pixar_lamp_while/)**

I know we usually only post our own projects here, but i was procrastinating on my own codebase today and went down a rabbit hole looking at github repos from some 48h REDHackathon happening in shanghai right now (hosted by rednote I think? today is their demo day). tbh i mostly expected to see a bunch of hastily duct-taped openai wrappers and weekend spaghetti code. clicked on one of the hardware submissions called Mira. at first glance the picture just looks like a cute 3d-printed pixar lamp. I figured it was just a physical shell with a basic python script piping some face tracking coordinates directly to a couple servos. but looking at the actual code... the system architecture is surprisingly hardcore. They didnt just hardcode reactions. they built a full embodied interaction system. the pipeline goes from single camera input -> vision event extraction -> scene selection -> local bridge / safety layer -> ESP32 firmware. Instead of raw tracking they built a scene-based motion choreography abstraction. it interprets visual data into states like 'curious_observe', 'cute_probe', and 'standup_reminder'. The esp32 firmware isnt a toy either... it has a custom binary serial protocol, touch thresholds, and ack/err handling. they even built offline rehearsal scripts, fault injection, and a web director console so they could test the logic without the physical hardware glitching out on stage. Most ai right now just sits in a chat window waiting for a prompt. this thing is trying to actually notice your presence in a physical space and respond with body language and light rhythms before you even say a word. idk, seeing hardware prototypes with this level of release-oriented engineering come out of a 48h builder camp makes me feel pretty lazy today lol. its just a stark reminder that the next phase of ai probably isnt going to be on a screen, but actually sitting on our desks observing us. anyway just thought id share something cool that isnt another b2b saas wrapper. repo if anyone wants to look at the c++ / esp32 logic (not mine obviously): github.com/JunkaiWang-TheoPhy/Mira-Light-AI-That-Sees-You

6h ago

---

**[XSTO introduces a hybrid biped robot that rolls on wheels and jumps over obstacles](https://www.reddit.com/r/robotics/comments/1shskju/xsto_introduces_a_hybrid_biped_robot_that_rolls/)**

1d ago

---

**[What actuator is this? CS2 recoil shoulder device](https://www.reddit.com/r/robotics/comments/1siva97/what_actuator_is_this_cs2_recoil_shoulder_device/)**

Hey, I came across this YouTube short of a CS2 player using a device that physically “kicks” his shoulder to simulate recoil, and I’m trying to figure out exactly what kind of actuator this is. Here’s the video: https://www.youtube.com/shorts/B08AjXtAGAg Thanks!

1h ago

---

**[Help! Isaac sim 4.5.0 on GCP T4: vulkan reports wrong version (535.32) despite 535.288 installed.](https://www.reddit.com/r/robotics/comments/1siuypj/help_isaac_sim_450_on_gcp_t4_vulkan_reports_wrong/)**

1h ago

---

**[Sumobot inquiry](https://www.reddit.com/r/robotics/comments/1sinbhd/sumobot_inquiry/)**

So there is this competition that we will be joining next month to qualify for nationals. I have seen many builds that include a so-called "pull up switch", for 2 months I had been trying to find out how to create one of those, since there are no existing tutorials online. I reckon it is a micro switch connected to the driver but still confused. Does anyone have an idea on how pull up switches are made, or done? We are using one of those cytron URC10 R1.1 SumoBot Controller.

6h ago

---

**[This robot is deployed in real homes in Shenzhen as part of a cleaning service. Not a lab demo, actual apartments with pets, kids' toys, and clutter](https://www.reddit.com/r/robotics/comments/1shnzv2/this_robot_is_deployed_in_real_homes_in_shenzhen/)**

58 Home partnered with X Square Robot to launch a cleaning service in Shenzhen where a human cleaner shows up with a robot partner. The robot handles structured tasks like wiping surfaces, picking up debris, and tidying, while the human handles everything that requires judgment. What makes this interesting from a technical standpoint: the robot runs on an end-to-end VLA (Vision-Language-Action) model called WALL-A that takes video and language input and outputs motor commands directly with no intermediate planning layer. But the real story isn't the model architecture, it's the deployment strategy. The company frames this as "grass-fed vs grain-fed" training data. Models trained on clean lab data perform well in controlled environments but fall apart in real homes where every apartment has a different layout, random clutter on the floor, pets walking through the workspace, kids' toys in unpredictable places. You can see in this video exactly why that matters: the robot is navigating around a Corgi, working in a room absolutely covered in children's toys, and dealing with narrow doorways in a real Chinese apartment. None of this is a problem you'd encounter in a lab. A few years ago this kind of footage would have been a staged demo. The fact that it's a paying service operating in real apartments suggests robots in everyday homes are closer than most people think.

1d ago

---

**[Yaskawa details](https://www.reddit.com/r/robotics/comments/1sidxld/yaskawa_details/)**

I'm currently working on a Yaskawa Ms-100 with Dx100, changing a wrist unit. The manual we have is for a MS-100II with DX200. This manual says the wrist uses flange sealant. We removed the wrist and found that there is an O-ring. The manual does not show this O-ring on the parts list or diagram. I cannot find a MS100 specific manual on Yaskawa's site, only the MS100II. Is anyone familiar with these that could offer some advice?

13h ago

---

---

## Google News: "robotics"

**[CEO Andy Jassy shares 3 ways Amazon is innovating to make customers’ lives easier and better](https://www.aboutamazon.com/news/innovation-at-amazon/amazon-ceo-andy-jassy-robotics-rural-delivery-broadband)**

In his annual letter to shareholders, Jassy shares how robotics, faster rural delivery, and broadband connectivity for underserved customers and geographies will help improve the customer experience.

About Amazon • 1d ago

---

**[Building the Future of Texas Robotics](https://news.utexas.edu/2026/04/09/building-the-future-of-texas-robotics/)**

Deepu Talla helps bring the future of robotics closer to reality through the Nvidia-Talla Endowment for Texas Robotics.

The University of Texas at Austin • 2d ago

---

**[Opinion | Meet Abi, the AI-powered robot companion for senior care](https://www.washingtonpost.com/opinions/2026/04/09/ai-robot-senior-care-abi/)**

This new tech from Australia is coming to America’s senior care facilities.

The Washington Post • 1d ago

---

**[Local robotics team could make it to world championships, here’s how to help](https://www.news9.com/oklahoma-city-news/okc-robotics-team-world-championship-fundraiser)**

A local team could take Oklahoma to the global stage through robotics.

News 9 • 1d ago

---

**[Robotic birds mimic mating to help bring back vanishing grouse](https://interestingengineering.com/ai-robotics/robotic-sage-grouse-conservation)**

Robotic bird decoys mimic mating rituals to help restore declining sage grouse populations in US national parks.

Interesting Engineering • 1d ago

---

**[New humanoid robots replacing workers in factories](https://www.nbcnews.com/video/shorts/new-humanoid-robots-replacing-workers-in-factories-261041221991)**

Meet 'Digit', a humanoid robotic worker made by Agility Robotics, now part of a new wave of robots replacing workers at companies like Schaeffler, Toyota, and GXO. NBC News' Brian Cheung takes a look.

NBC News • 4h ago

---

**[Humanoid robots hit mass production in China](https://www.foxnews.com/tech/humanoid-robots-hit-mass-production-china)**

A Chinese factory is producing humanoid robots every 30 minutes, marking a shift toward large-scale manufacturing and broader adoption.

Fox News • 2d ago

---

**[Unitree to debut cheapest humanoid robot globally via Alibaba: sources](https://www.scmp.com/tech/article/3349489/chinas-unitree-debut-cheapest-humanoid-robot-globally-alibaba-site-sources)**

South China Morning Post • 2d ago

---

**[Minnesota college student mentors Japanese robotics team she founded](https://www.cbsnews.com/minnesota/video/minnesota-college-student-mentors-japanese-robotics-team-she-founded/)**

Robots are undoubtedly a big part of the future. In this edition of Home Team, Mike Max introduces Kanon Nakajima, a local robot buff in Minnesota whose story started in Japan.

CBS News • 5h ago

---

**[National robotics push caught in delayed Trump-Xi meeting](https://www.politico.com/news/2026/04/09/national-robotics-trump-xi-china-00861918)**

Politico • 2d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid robots take over manual job at auto parts plant](https://www.youtube.com/watch?v=JMxKpo_Llt8)**

Humanoid robots are being used for some manual tasks at the Schaeffler auto parts plant in Cheraw, S.C. Proponents argue that ...

📺 NBC News

👁️ 69K • 👍 950 • 💬 521 • ⏱️ 4:56 • 1d ago

---

**[AI agent in a robot does exactly what experts warned](https://www.youtube.com/watch?v=woTy4dTiT20)**

Could AI become dangerous? Can we trust AI Agents? AGI. Use code insideai at https://incogni.com/insideai to get an exclusive ...

📺 InsideAI

👁️ 373K • 👍 16K • 💬 1K • ⏱️ 16:24 • 2d ago

---

**[Unitree H1 Humanoid Robot Breaks Limits at 22.4 MPH](https://www.youtube.com/watch?v=sfcqAZcWoMo)**

The Unitree H1 humanoid robot just reached an incredible 10 meters per second, which is about 22.4 miles per hour, putting it ...

📺 DPCcars

👁️ 2K • 👍 68 • 💬 15 • ⏱️ 1:24 • 8h ago

---

**[Disney&#39;s New Olaf Robot Isn&#39;t What You Think](https://www.youtube.com/watch?v=VvXhpnvjVGE)**

Everyone is getting 7 things wrong about Disney's new Olaf animatronic. I asked Imagineering how the free roaming Olaf works, ...

📺 Guide2WDW

👁️ 24K • 👍 682 • 💬 87 • ⏱️ 19:30 • 2d ago

---

**[Unitree H1 Humanoid Robot Reclaims Record for Fastest Robot? #robotics #robot #unitreerobotics](https://www.youtube.com/watch?v=rSgpueUzl6g)**

Unitree's H1 humanoid robot is back on top. Or is it? The Chinese robotics leader just shared footage of its full-sized humanoid to ...

📺 Kalil 4.0

👁️ 737 • 👍 41 • 💬 4 • ⏱️ 1:02 • 2h ago

---

**[Why the Lymow One Plus is the Best Robot Mower Not Sponsored](https://www.youtube.com/watch?v=TCBaaSISul8)**

Lymow → https://lymowtradecolimited.pxf.io/OYr2VG The Lymow One Plus isn't your average robot mower. Instead of those tiny, ...

📺 How To with Doc

👁️ 13K • 👍 817 • 💬 156 • ⏱️ 21:24 • 2d ago

---

**[I SAW MY FiRST delivery robot #minivacay #robot #justthebells10](https://www.youtube.com/watch?v=yGJyWvJ9uS4)**

📺 Just the Bells 10

👁️ 21K • 👍 1K • 💬 50 • ⏱️ 0:33 • 21h ago

---

**[South Korea Is Building Robots the World Didn’t See Coming!](https://www.youtube.com/watch?v=H09m8a3oL_4)**

South Korea is building robots you've only seen in movies, from giant walking machines to exoskeletons that give people back ...

📺 DeCode

👁️ 49K • 👍 926 • 💬 87 • ⏱️ 14:45 • 2d ago

---

**[I TESTED THE HOVER IN CHAMPION LEAGUE! FINALLY USING THIS ROBOT! (War Robots)](https://www.youtube.com/watch?v=KShsWuXuvXY)**

In this video I tested out the Hover in Champion league. https://wr.my.games/Wolfblood7.

📺 Wolfblood7

👁️ 3K • 👍 163 • 💬 43 • ⏱️ 13:54 • 15h ago

---

**[Are AI soldiers about to take over the battlefield? | DW News](https://www.youtube.com/watch?v=q83LtZza5eA)**

US startup Foundation is developing humanoid robots for military use. The goal is for its Phantom model to identify targets and ...

📺 DW News

👁️ 72K • 👍 550 • 💬 101 • ⏱️ 1:22 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

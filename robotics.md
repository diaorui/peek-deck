---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-02T16:01:43.783255+00:00'
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

**Last Updated:** April 02, 2026 at 16:01 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[building a desktop robot. turns out response timing and lip sync matter way more than the LLM itself for HRI.](https://www.reddit.com/r/robotics/comments/1sajyvt/building_a_desktop_robot_turns_out_response/)**

been working on this little desktop robot prototype called Kitto for a while now. honestly most of the hype right now is just cramming the biggest model possible into a plastic shell. but testing the interaction on this thing... if the timing is off it just feels like a glorified smart speaker. to make it actually feel 'alive' on a desk, the idle animations and the instant switch to a listening state carry like 90% of the weight. tbh we ended up spending way more time tuning the audio-to-viseme mapping for the face than we did tweaking the actual API prompts. current stack is just an esp32s3+esp32p4 (planning to migrate to a linux board soon so we can handle local processing and maybe hook into openclaw). the screen isnt playing pre-rendered video files btw. the mouth movements are code-driven in real-time by analyzing the audio stream. latency is still my biggest headache though. pinging the api, getting the TTS audio back, and triggering the animation states fast enough to not break the illusion is tough on this hardware. its getting there but still a lot of code to fix. definately not pitching this as finished hardware yet, mostly just looking for honest feedback on the HRI approach. curious how you guys are handling TTS latency in your own conversational builds right now?

54m ago

---

**["Follow Me" Mode: Real-time human tracking with YOLOv8](https://www.reddit.com/r/robotics/comments/1sac61n/follow_me_mode_realtime_human_tracking_with_yolov8/)**

6h ago

---

**[China announces its first automated manufacturing line capable of producing 10K humanoid robots per year - 1 robot every 30 minutes](https://www.reddit.com/r/robotics/comments/1s9qso0/china_announces_its_first_automated_manufacturing/)**

22h ago

---

**[Olaf couldn't handle too many human questions, suddenly crashed, collapsed, and its carrot nose fell off](https://www.reddit.com/r/robotics/comments/1s9g61s/olaf_couldnt_handle_too_many_human_questions/)**

1d ago

---

**[IROS 2026 number of submitted papers](https://www.reddit.com/r/robotics/comments/1safe8v/iros_2026_number_of_submitted_papers/)**

Has anyone seen an estimate for the number of submissions this year? I could not find an official announcement. Maybe the submission IDs could give a rough idea.

4h ago

---

**[I made my robot wal JUST LIKE BAYMAX](https://www.reddit.com/r/robotics/comments/1sabqhy/i_made_my_robot_wal_just_like_baymax/)**

it uses only two motors to walk unlike most other bipedal robots. What do you guys think? Also I just made the base and hand for now ! https://www.youtube.com/watch?v=InKbSM_C5Xc

7h ago

---

**[LLMs in industrial robotics workflows](https://www.reddit.com/r/robotics/comments/1sag8h6/llms_in_industrial_robotics_workflows/)**

LLMs are being used in industrial robotics to generate robot motion code, PLC logic, and supporting automation scripts from natural language inputs. The primary application is in repetitive tasks such as sequencing, template generation, and initial system configuration. Outputs are reviewed, tested, and refined by engineers before deployment. When combined with simulation, this allows portions of robotic systems to be developed and tested prior to full hardware availability, reducing reliance on sequential commissioning.

🔗 [Automate](https://www.automate.org/ai/industry-insights/accelerating-industrial-automation-with-llms) • 3h ago

---

**[Common Motors across Cobots, Humanoids, Robot Dogs](https://www.reddit.com/r/robotics/comments/1sal8nj/common_motors_across_cobots_humanoids_robot_dogs/)**

Hello Everyone, I am trying to understand any commanization of motors & actuator specs in robotics (Humanoids, cobots, robot dogs) landscape. There has been quite significant progress in the last couple of years. I now see that companies like Unitree, Tesla already scaling up their robots. I understand that the motors and actuators they are using has been specifically made for their own applications but I was wondering if there is one single common motor and actuator that is common across these applications. Here is what I found out: PMSM + QDD for Robot dogs BLDC + Harmonics - Industrial precision Is there any specific range/specs across the motors and actuators that can be made like an off the shelf component? Any leads would be helpful.

8m ago

---

**[Working on an ego/exo dataset](https://www.reddit.com/r/robotics/comments/1sa17xd/working_on_an_egoexo_dataset/)**

I’m in a unique position as a small business owner and I’m looking for advice. I’ve been a long time follower of r/datahoarder and I think my friends over here in r/robotics might find what I have useful. I’ve been hanging on to about 12tb of MP4 footage that I captured at my business hoping I would find a use for it one day. Now it seems like every other day I read another article about the data scarcity in robotics training and the sim to real gap. So I’m wondering if I might be able to connect some pieces and license this video as a dataset. I did some research and found that a first person view seems to be the most valuable for embodied AI training so I recently I added GoPros on my customers to capture that as well. I think what I have may be useful for some training cases. It is a lot of video of human object interaction and high force material interactions and real world unscripted human dynamics. Theres a ton of edge case stuff where things don’t go exactly like it was planned because of the chaotic atmosphere. I have a few hundred hours of the GoPro footage and about 6500 hours of the cctv footage. Currently adding a few hundred hours per month of video with pretty open customizability. I’ve been tinkering with Yolo and SAM2 models as well. All the personal identifiable information has been cleared and all customers are aware of the use of this video for AI training purposes. Would this be useful for some of you and if so, what would be the best way to package it for you? I appreciate your time!

16h ago

---

**[Text. Wave. Move. — Openclaw Controls Our Robot](https://www.reddit.com/r/robotics/comments/1sa8hos/text_wave_move_openclaw_controls_our_robot/)**

10h ago

---

---

## Google News: "robotics"

**[Sea Stars Can Lose an Arm and Soldier On. What If Robots Could Do the Same?](https://www.smithsonianmag.com/innovation/sea-stars-can-lose-an-arm-and-soldier-on-what-if-robots-could-do-the-same-180988453/)**

Bioinspiration looks to nature for clues on how to build more efficient, resilient robots

Smithsonian Magazine • 14m ago

---

**[Station Crew Works Robotics, Research as Artemis II Launch Preps Continue](https://www.nasa.gov/blogs/general-blog/2026/04/01/station-crew-works-robotics-research-as-artemis-ii-launch-preps-continue/)**

Robotics training and human research were the primary duties for the Expedition 74 crew aboard the International Space Station on Wednesday. The orbital residents rounded out their shift with spacesuit work, cargo operations, and Earth observations.

NASA (.gov) • 20h ago

---

**[FedEx’s next AI leap to feature RFID, robotics](https://www.supplychaindive.com/news/fedex-ai-usage-rfid-robotics-network-2/816220/)**

The carrier is scaling its use of physical assets powered by AI to strengthen network reliability and improve connectivity with shippers, a FedEx executive said.

Supply Chain Dive • 1d ago

---

**[The world’s largest humanoid robot maker is going public](https://restofworld.org/2026/unitree-china-humanoid-robot-shanghai-ipo/)**

Rest of World • 2d ago

---

**[The gig workers who are training humanoid robots at home](https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/)**

People in Nigeria and India are strapping iPhones onto their heads and recording themselves doing chores.

MIT Technology Review • 1d ago

---

**[Gill Pratt Says Humanoid Robots’ Moment Is Finally Here](https://spectrum.ieee.org/humanoid-robots-gill-pratt-darpa)**

The architect of the DARPA Robotics Challenge explains how their brains have caught up

spectrum.ieee.org • 1d ago

---

**[Researchers build a robotic swarm with no electronics, no batteries and no brains](https://techxplore.com/news/2026-04-robotic-swarm-electronics-batteries-brains.html)**

Tech Xplore • 1d ago

---

**[Robots learn to ask humans for help](https://www.axios.com/2026/04/01/robots-delivery-serve-tmobile)**

Axios • 7h ago

---

**[Ambarella Sees Growth In Industrial Robotics (NASDAQ:AMBA)](https://seekingalpha.com/article/4888105-ambarella-sees-growth-in-industrial-robotics)**

Ambarella, Inc. Buy thesis: edge AI growth via CV7 chip & Cooper platform in robotics/auto, with $84.28 PT. Click for more on AMBA stock prospects.

Seeking Alpha • 10m ago

---

**[How Disney Imagineers are using AI and robotics to reshape the company’s theme parks](https://www.fastcompany.com/91519970/disney-imagineers-ai-and-robotics-paris-park)**

From robotic Olaf to reinforcement learning, the company is rethinking how its attractions come to life.

Fast Company • 5h ago

---

---

## YouTube Videos: "robotics"

**[Brett Adcock - Shawn Ryan’s First Interview with a Robot | SRS #292](https://www.youtube.com/watch?v=99pOdGEGu6s)**

Brett Adcock is a technology entrepreneur focused on building companies in robotics, artificial intelligence, and aerospace.

📺 Shawn Ryan Show

👁️ 457K • 👍 9K • 💬 3K • ⏱️ 2:57:09 • 2d ago

---

**[Xiaomi’s New AI Robot Hand Works Like a REAL Human… This Is INSANE](https://www.youtube.com/watch?v=Ubpk3tOl9gw)**

Xiaomi just dropped a robotic hand so realistic, it might fool you into thinking it's human — and that's just the START of what's ...

📺 The AI Nexus

👁️ 3K • 👍 153 • 💬 12 • ⏱️ 20:43 • 1d ago

---

**[Shawn Ryan Tests a Real Humanoid Robot](https://www.youtube.com/watch?v=HWq9cFhTvvQ)**

Shawn Ryan gets hands-on with a real humanoid robot powered entirely by AI. In this clip, we break down how this robot sees, ...

📺 Shawn Ryan Show

👁️ 293K • 👍 16K • 💬 3K • ⏱️ 8:48 • 19h ago

---

**[Every Home Will Have a Humanoid Robot in 10 Years](https://www.youtube.com/watch?v=u4NLSzMP8z0)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCkoujZQZatbqy4KGcgjpVxQ/join Support the Shawn ...

📺 Shawn Ryan Clips

👁️ 9K • 👍 324 • 💬 133 • ⏱️ 15:18 • 2d ago

---

**[The Real-Life Future of Humanoid Robots](https://www.youtube.com/watch?v=ktwtZNKDV0E)**

Brett Adcock shares his vision for the future of humanoid robots, why he believes synthetic humans will become one of the most ...

📺 Shawn Ryan Show

👁️ 71K • 👍 2K • 💬 681 • ⏱️ 14:05 • 5d ago

---

**[Nvidia Shocked Everyone by Announcing the Smartest AI Robot That Can Do Anything](https://www.youtube.com/watch?v=fW_vymTb2ZM)**

A new wave of attention is building around Nvidia as the company pushes further into advanced robotics with a concept focused ...

📺 Carros Show

👁️ 4K • 👍 62 • 💬 4 • ⏱️ 8:42 • 5d ago

---

**[Shawn Ryan Gets a Real-Life Robot 😳](https://www.youtube.com/watch?v=fQdJb7YzDRc)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCkoujZQZatbqy4KGcgjpVxQ/join Support the Shawn ...

📺 Shawn Ryan Show

👁️ 1.0M • 👍 17K • 💬 1K • ⏱️ 0:28 • 2d ago

---

**[The Six-Servo Robot Dog - it&#39;s open source!](https://www.youtube.com/watch?v=2eKb_2N0SBI)**

Ad: Check out PCBWay for all your project needs! Get $10 off orders over $30 with code: PCBWay-JamesBruton-10 ...

📺 James Bruton

👁️ 49K • 👍 3K • 💬 180 • ⏱️ 16:17 • 2d ago

---

**[Unitree Open‑Source: High‑Quality Real‑Robot Dataset for Humanoid Robots](https://www.youtube.com/watch?v=pN_bj5-QyW8)**

Unitree open-sources UnifoLM-WBT-Dataset — a high-quality real-world humanoid robot whole-body teleoperation (WBT) ...

📺 Unitree Robotics

👁️ 9.0M • 👍 589 • 💬 98 • ⏱️ 1:28 • 6d ago

---

**[He almost violated the first law of robotics #youtubeshorts #funny #robot #funnyshorts #laugh](https://www.youtube.com/watch?v=ascGyPgPd34)**

📺 Warm tide

👁️ 985K • 👍 8K • 💬 60 • ⏱️ 0:53 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-03T15:09:16.194569+00:00'
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

**Last Updated:** April 03, 2026 at 15:09 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Simulation is a beautiful pain in RL](https://www.reddit.com/r/robotics/comments/1sbbj7n/simulation_is_a_beautiful_pain_in_rl/)**

Appreciate all the feedback and love on the recent videos, here's another clip of the dev process worth sharing. This one starts with an ugly moment, the right leg clips the edge and stumbles on a stair jump. Took a few days to track down the real issue. Turned out to be a mechanical transmission resistance in the hip joint, not a bug in the code. After the fix, clean landing. We're at around stable 30cm (~12")now. Sim does 40 or even higher, but 30 clears real stairs and that's what matters. (Getting to 30 in real life was harder than it sounds) Basic locomotion is getting solid, so next step: giving this little guy some eyes and ears, maybe. Legs first, then brains. sim2real is always humbling!

3h ago

---

**[Autonomous valet robot demonstrating precise self-parking in a real-world setting](https://www.reddit.com/r/robotics/comments/1san0l2/autonomous_valet_robot_demonstrating_precise/)**

22h ago

---

**[Generalist | Introducing GEN-1](https://www.reddit.com/r/robotics/comments/1saoiaj/generalist_introducing_gen1/)**

21h ago

---

**[RoboBaton mini and Raspberry Pi](https://www.reddit.com/r/robotics/comments/1sbdusb/robobaton_mini_and_raspberry_pi/)**

l find that RoboBaton mini is good to use. I was originally planning to use Intel's T265, but discovered it had been discontinued. I found RoboBaton Mini on myrobotproject's website. I successfully got it working with my Raspberry Pi. I will open-source the code on GitHub later. I hope everyone can connect with me to discuss and explore other use cases for the Mini.

1h ago

---

**[building a desktop robot. turns out response timing and lip sync matter way more than the LLM itself for HRI.](https://www.reddit.com/r/robotics/comments/1sajyvt/building_a_desktop_robot_turns_out_response/)**

been working on this little desktop robot prototype called Kitto for a while now. honestly most of the hype right now is just cramming the biggest model possible into a plastic shell. but testing the interaction on this thing... if the timing is off it just feels like a glorified smart speaker. to make it actually feel 'alive' on a desk, the idle animations and the instant switch to a listening state carry like 90% of the weight. tbh we ended up spending way more time tuning the audio-to-viseme mapping for the face than we did tweaking the actual API prompts. current stack is just an esp32s3+esp32p4 (planning to migrate to a linux board soon so we can handle local processing and maybe hook into openclaw). the screen isnt playing pre-rendered video files btw. the mouth movements are code-driven in real-time by analyzing the audio stream. latency is still my biggest headache though. pinging the api, getting the TTS audio back, and triggering the animation states fast enough to not break the illusion is tough on this hardware. its getting there but still a lot of code to fix. definately not pitching this as finished hardware yet, mostly just looking for honest feedback on the HRI approach. curious how you guys are handling TTS latency in your own conversational builds right now?

1d ago

---

**[My Pi 3b+ Self Roving Robot](https://www.reddit.com/r/robotics/comments/1saw4e3/my_pi_3b_self_roving_robot/)**

Running 3 HC-SR04’s doing object detection and avoidance. Just getting my encoders working. Hoping to be mapping soon. Definitely a fun project.

16h ago

---

**[4DOF Controller for an Automated Projector Project](https://www.reddit.com/r/robotics/comments/1sb00oz/4dof_controller_for_an_automated_projector_project/)**

https://www.youtube.com/@ALMA.GeoffreyAment Chapter 2, a home theatre, 3D printed parts, motorized projector, home decoration, and DIY electronics -- if you know of anyone else that might be interested in this stuff, sharing to others would really help me out! Hope to see you around here or YouTube :)

13h ago

---

**[Robotics Studio](https://www.reddit.com/r/robotics/comments/1sapdsp/robotics_studio/)**

20h ago

---

**[simple tool share: stepper coil identification helper](https://www.reddit.com/r/robotics/comments/1sb4n6g/simple_tool_share_stepper_coil_identification/)**

https://xuanbuilds.github.io/stepper-coil-identification-helper/ I understand 99% of you on the sub don't need this, but here is the context: As a beginner, I struggled to connect stepper motors to drivers. The wiring order varies between motors, and the wire colors don’t indicate how they are grouped. Once I understood that a 2-phase bipolar stepper simply consists of two wire pairs forming two coils, the problem became trivial: identify one pair, and the other is immediately known. At that point, you can already connect the motor to a driver such as a DRV8825 and get it running. I built this simple tool to internalize that concept—and to help other beginners get tinkering quickly without needing to read about steppers first. After doing this a few times, it becomes obvious how simple coil identification is, and the helper becomes unnecessary. You’ll need a multimeter with continuity tester.

9h ago

---

**["Follow Me" Mode: Real-time human tracking with YOLOv8](https://www.reddit.com/r/robotics/comments/1sac61n/follow_me_mode_realtime_human_tracking_with_yolov8/)**

1d ago

---

---

## Google News: "robotics"

**[Exclusive: Anvil Robotics Raises $5.5M to Build ‘Legos for Robots’ Platform For Physical AI Teams](https://news.crunchbase.com/robotics/physical-ai-custom-robot-builder-seed-funding-anvil/)**

Anvil Robotics, an eight-month-old startup that aims to be the “Legos for robots,” has raised $5.5 million in a seed funding round, it tells Crunchbase News exclusively.

news.crunchbase.com • 1d ago

---

**[Under the Skin of America’s Humanoid Robots: Chinese Technology](https://www.wsj.com/tech/under-the-skin-of-americas-humanoid-robots-chinese-technology-27dd4fdf?gaa_at=eafs&gaa_n=AWEtsqdLyWl4kGL8BRLJCr9FVBdJgk21prXOhFutw13VZCu5alkdxN4rcqD8&gaa_ts=69cfce23&gaa_sig=8REyC7R09B85m-LxxSQaNVOG_p3pyyV-Y5RyIB6KRQKaR4mU8h1M_3ro3gXOM4kht2xI9tgM2klwfCLaF9qhDg%3D%3D)**

WSJ • 12h ago

---

**[The gig workers who are training humanoid robots at home](https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/)**

People in Nigeria and India are strapping iPhones onto their heads and recording themselves doing chores.

MIT Technology Review • 2d ago

---

**[Generalist Is Betting Its Robot-Training Gloves Will Usher In Robotics’ ChatGPT Moment](https://www.forbes.com/sites/annatong/2026/04/02/generalist-is-betting-its-robot-training-gloves-will-usher-in-robotics-chatgpt-moment/)**

Forbes • 1d ago

---

**[Air-powered artificial muscles could help robots lift 100 times their weight](https://techxplore.com/news/2026-04-air-powered-artificial-muscles-robots.html)**

Tech Xplore • 23h ago

---

**[Station Crew Works Robotics, Research as Artemis II Launch Preps Continue](https://www.nasa.gov/blogs/general-blog/2026/04/01/station-crew-works-robotics-research-as-artemis-ii-launch-preps-continue/)**

Robotics training and human research were the primary duties for the Expedition 74 crew aboard the International Space Station on Wednesday. The orbital residents rounded out their shift with spacesuit work, cargo operations, and Earth observations.

NASA (.gov) • 1d ago

---

**[Hyundai Motor Unveils "Next Starts Now" Campaign, Set to Showcase Robotics at FIFA World Cup 2026™](https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-unveils-next-starts-now-campaign%252C-set-to-showcase-robotics-at-fifa-world-cup-2026%25E2%2584%25A2-0000001147)**

Hyundai Motor Unveils "Next Starts Now" Campaign, Set to Showcase Robotics at FIFA World Cup 2026™

Hyundai • 2d ago

---

**[FedEx’s next AI leap to feature RFID, robotics](https://www.supplychaindive.com/news/fedex-ai-usage-rfid-robotics-network-2/816220/)**

The carrier is scaling its use of physical assets powered by AI to strengthen network reliability and improve connectivity with shippers, a FedEx executive said.

Supply Chain Dive • 2d ago

---

**[Local Robotics Teams Raising Funds to Attend World Competition](https://www.newsdakota.com/2026/04/02/local-robotics-teams-raising-funds-to-attend-world-competition/)**

VALLEY CITY, N.D. (NewsDakota.com) – Two local school districts are sending their robotics teams to the world competition. Valley City Jr/Sr High Coach- Joelle Manlove said Three Geniuses and the New Guy have been invited to compete

News Dakota • 18h ago

---

**[Robots learn to ask humans for help](https://www.axios.com/2026/04/01/robots-delivery-serve-tmobile)**

Axios • 1d ago

---

---

## YouTube Videos: "robotics"

**[Every Home Will Have a Humanoid Robot in 10 Years](https://www.youtube.com/watch?v=u4NLSzMP8z0)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCkoujZQZatbqy4KGcgjpVxQ/join Support the Shawn ...

📺 Shawn Ryan Clips

👁️ 10K • 👍 334 • 💬 135 • ⏱️ 15:18 • 3d ago

---

**[Robotic Frog VS Frog](https://www.youtube.com/watch?v=kwzDGQAzyuw)**

I put REAL animals up against their robotic versions in a series of intense head-to-head challenges: From speed and agility to ...

📺 Alex Turk

👁️ 231K • 👍 2K • 💬 77 • ⏱️ 9:36 • 6d ago

---

**[The Real-Life Future of Humanoid Robots](https://www.youtube.com/watch?v=ktwtZNKDV0E)**

Brett Adcock shares his vision for the future of humanoid robots, why he believes synthetic humans will become one of the most ...

📺 Shawn Ryan Show

👁️ 73K • 👍 2K • 💬 685 • ⏱️ 14:05 • 6d ago

---

**[Melania Trump Promotes Humanoid Robots as Potential Educators | The View](https://www.youtube.com/watch?v=q6fcoXkiVnQ)**

'The View' co-hosts and Abby Huntsman react to the first lady's sneak peek at the classroom of the future. Subscribe to our ...

📺 The View

👁️ 78K • 👍 1K • 💬 446 • ⏱️ 6:42 • 6d ago

---

**[Xiaomi’s New AI Robot Hand Works Like a REAL Human… This Is INSANE](https://www.youtube.com/watch?v=Ubpk3tOl9gw)**

Xiaomi just dropped a robotic hand so realistic, it might fool you into thinking it's human — and that's just the START of what's ...

📺 The AI Nexus

👁️ 4K • 👍 173 • 💬 13 • ⏱️ 20:43 • 2d ago

---

**[I broke a robot in China](https://www.youtube.com/watch?v=7U3vjVfwChc)**

China is leading the world in humanoid robot shipments. Powered by artificial intelligence, these machines are setting new ...

📺 CGTN

👁️ 26K • 👍 245 • 💬 37 • ⏱️ 1:54 • 1d ago

---

**[Shawn Ryan Tests a Real Humanoid Robot](https://www.youtube.com/watch?v=HWq9cFhTvvQ)**

Shawn Ryan gets hands-on with a real humanoid robot powered entirely by AI. In this clip, we break down how this robot sees, ...

📺 Shawn Ryan Show

👁️ 673K • 👍 28K • 💬 5K • ⏱️ 8:48 • 1d ago

---

**[Nvidia Shocked Everyone by Announcing the Smartest AI Robot That Can Do Anything](https://www.youtube.com/watch?v=fW_vymTb2ZM)**

A new wave of attention is building around Nvidia as the company pushes further into advanced robotics with a concept focused ...

📺 Carros Show

👁️ 4K • 👍 62 • 💬 4 • ⏱️ 8:42 • 6d ago

---

**[Jen picks humanoid over Melania](https://www.youtube.com/watch?v=TKnzU1XhcNU)**

Robot vs. Melania? After Melania Trump brings an AI-powered humanoid to the White House, Jen makes her pick.

📺 MS NOW

👁️ 53K • 👍 2K • 💬 296 • ⏱️ 2:01 • 6d ago

---

**[China&#39;s Robots Learned Kung Fu. Now They&#39;re Terrifying](https://www.youtube.com/watch?v=UKLvMLtNXpE)**

679 million people watched China's robots perform fully autonomous kung fu at the 2026 Spring Festival Gala. Backflips.

📺 TechFrontierNow

👁️ 25K • 👍 635 • 💬 83 • ⏱️ 9:00 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

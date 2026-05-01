---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-01T06:27:35.997264+00:00'
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

**Last Updated:** May 01, 2026 at 06:27 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Extendible robotic arm](https://www.reddit.com/r/robotics/comments/1t0ijod/extendible_robotic_arm/)**

Here is an extendable robotic arm I developed based on the NASA's Rollable Slit-Tube Boom (STEM) concept. It can extend up to 5 ft. It was redesigned to be easier and more affordable to manufacture, with all parts 3D printed. The current use case is sanding large epoxy tables or plates or decks. I ran out of resources before building a more advanced version. Curious to hear what other use cases people see for something like this.

2h ago

---

**[Japan Airlines is officially deploying humanoid robots for ground operations at Haneda Airport starting next month](https://www.reddit.com/r/robotics/comments/1t021sl/japan_airlines_is_officially_deploying_humanoid/)**

Japan Airlines is set to begin trialing humanoid robots for ground operations at Tokyo’s Haneda Airport starting in May 2026, as part of efforts to tackle a growing labor shortage. The robots, developed in partnership with robotics firms, will assist with physically demanding tasks such as moving baggage and cargo on the tarmac. The initiative comes amid rising tourism and an aging population, which have increased pressure on airport staff. While the robots can handle repetitive manual work, key responsibilities like safety oversight will remain with human workers. The multi-year trial aims to evaluate whether humanoid machines can improve efficiency and reduce workload without requiring major infrastructure change. Source

13h ago

---

**[sim: perfect backflip. real: perfect faceplant](https://www.reddit.com/r/robotics/comments/1szufp9/sim_perfect_backflip_real_perfect_faceplant/)**

the flip itself actually goes through, full rotation. but the landing... face meets floor every time lol dug into it for a while. found that the damping in our sim was too high, so the joints in simulation were way smoother than the real ones. the policy just never had to deal with that kind of impact force on landing. working on dialing it down to match actual hardware now also been getting a ton of questions lately about how we do RL training, sim2real workflow, domain randomization, all that. finally put together a longer writeup covering what we've tried and where we messed up. posted it on r/MondoRobotics if anyone wants to check it out: https://www.reddit.com/r/MondoRobotics/comments/1szuepv/our_rl_journey_so_far_what_we_learned_what_broke/ happy to answer stuff here too

18h ago

---

**[Watched a robot grill on May Day and I can't stop thinking about the Haymarket affair](https://www.reddit.com/r/robotics/comments/1t0aqrm/watched_a_robot_grill_on_may_day_and_i_cant_stop/)**

Today is May Day. International Workers' Day. The holiday exists because in 1886, workers in Chicago went on strike demanding one thing: stop making people work 80 hours a week. Things got violent. People died. Eventually, decades later, the 8-hour workday became law. 140 years later I'm watching a robot handle a grill on that same day. The machine doesn't observe the holiday. Doesn't observe any day. It just runs. The thing those workers were actually asking for was less human suffering at machines. That kind of happened. Just not through shorter shifts. Through the machine taking the job entirely. Good outcome? Weird outcome? Genuinely no idea. Anyway, happy May Day. The robots have it covered.

8h ago

---

**[Open sourced a multi-sensor fusion perception system inspired by Lattice OS architecture. Runs on Jetson Orin Nano.](https://www.reddit.com/r/robotics/comments/1t0k5ii/open_sourced_a_multisensor_fusion_perception/)**

Been working on a community reference implementation of the connected-sensor situational awareness concept that systems like Anduril's Lattice popularized. The idea: multiple low-cost sensors fused at the edge into a single coherent world model. What actually runs: YOLOv8n via TensorRT FP16, adaptive 6-state Kalman filter [x, y, z, vx, vy, vz] per world object, Hungarian tracking with appearance re-ID, and self-calibrating ground-plane homography between cameras. The architecture decision I think is most relevant for robotics: singleton perception pipeline. One detect-track-fuse loop runs per tick regardless of how many downstream consumers exist. State broadcasts as pre-serialized msgpack binary snapshots. This pattern maps well to robot middleware (ROS2 pub/sub) and means the edge compute budget scales with sensor count, not consumer count. Not military grade, not affiliated with Anduril. Pure research and learning project. Posting because the multi-sensor fusion patterns here (sensor trust scoring, adaptive Kalman noise, cross-camera re-ID) seem directly applicable to robotics work. Repo: github.com/mandarwagh9/overwatch. MIT license. Anyone working on similar multi-sensor fusion at the edge? Curious how people handle clock drift between sensors in practice.

1h ago

---

**[Hello! Need some help with simulations](https://www.reddit.com/r/robotics/comments/1t07o79/hello_need_some_help_with_simulations/)**

Hello, I am new to robotics and simulation stuff. I was working on my PyBullet simulation of my robot, but the joints do not seem to be connected at all. I have tried everything from reassembling the CAD to checking if the origins are correct and even remaking some of the links, but I cannot figure it out at all any tips?

10h ago

---

**[Geyser Interlock Schematic to prevent dry heating in Proteus](https://www.reddit.com/r/robotics/comments/1t0klqu/geyser_interlock_schematic_to_prevent_dry_heating/)**

38m ago

---

**[Unitree G1 performing tricks with a new policy OmniXtreme](https://www.reddit.com/r/robotics/comments/1szk5va/unitree_g1_performing_tricks_with_a_new_policy/)**

1d ago

---

**[Robot Camera Arm on Rails Filming a Running Scene](https://www.reddit.com/r/robotics/comments/1sz54y6/robot_camera_arm_on_rails_filming_a_running_scene/)**

1d ago

---

**[This Toyota Walk me robotic chair looks slightly creepy](https://www.reddit.com/r/robotics/comments/1sznrkw/this_toyota_walk_me_robotic_chair_looks_slightly/)**

[ Removed by Reddit in response to a copyright notice. ]

1d ago

---

---

## Google News: "robotics"

**[SoftBank plans to list new AI and robotics company in the US](https://www.ft.com/content/55c7d99c-7e68-453c-b784-33d6b9838e16?syn-25a6b1a6=1)**

Masayoshi Son plots IPO for business named Roze as soon as this year

Financial Times • 1d ago

---

**[SoftBank reportedly weighs $100 billion valuation for new AI and robotics spinout in potential U.S. IPO](https://www.cnbc.com/2026/04/30/softbank-roze-ai-robotics-ipo-100-billion-ft-report.html)**

SoftBank Group is planning to create and list a standalone artificial intelligence and robotics company, coined "Roze" in the U.S.

CNBC • 1d ago

---

**[SoftBank Plots IPO for New Robotics Venture](https://www.wsj.com/tech/ai/softbank-plots-ipo-for-new-robotics-venture-c52c2297)**

WSJ • 1d ago

---

**[I've Covered Robots for Years. This One Is Different](https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/)**

From sorting chicken nuggets to screwing in light bulbs, Eka’s robots are eerily lifelike. But do they have real physical smarts?

WIRED • 1d ago

---

**[The robots are leaving the lab: the megatrend of automation](https://www.theguardian.com/global-x-invest-in-innovation/2026/may/01/the-robots-are-leaving-the-lab-the-megatrend-of-automation)**

Until recently, humanoid robots seemed like a distant sci-fi dream. Now, they’re on the brink of driving economic transformation.

The Guardian • 2h ago

---

**[Japan Airlines trials humanoid robots as ground handlers](https://www.bbc.com/news/articles/cpwp87j1llvo)**

These robots may in future help clean cabins and operate ground support equipment.

BBC • 2d ago

---

**[The Top 10 Humanoid Robots, Ranked: Tesla, Unitree, and More](https://www.eweek.com/news/humanoid-robot-power-rankings-list/)**

Explore the top humanoid robots from Tesla, Unitree, Agility Robotics, UBTech, and more, ranked by momentum, real-world use, and commercial potential.

eWeek • 1d ago

---

**[Humanoid Maker 1X Opens New US Factory, Plans to Build 10,000 Home Robots in First Year](https://www.bloomberg.com/news/articles/2026-04-30/humanoid-maker-1x-opens-us-factory-plans-to-make-10-000-home-robots-this-year)**

Bloomberg.com • 16h ago

---

**[Rethinking robotics with physical intelligence](https://www.darpa.mil/news/2026/rethinking-robotics)**

DARPA is looking to tackle these challenges by embedding intelligence directly into the physical materials of robotic systems.

darpa.mil • 1d ago

---

**[DAIMON Robotics Wants to Give Robot Hands a Sense of Touch](https://spectrum.ieee.org/daimon-robotics-physical-ai)**

A powerful embodied AI dataset will enable robots to perform dexterous manipulation

IEEE Spectrum • 16h ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robots and the Gap Between Hype and Reality | Bloomberg Primer](https://www.youtube.com/watch?v=UQZooauU-FQ)**

Humanoid robots that use AI are moving from viral videos to real-world work. From artificial intelligence training and data gaps to ...

📺 Bloomberg Originals

👁️ 161K • 👍 3K • 💬 207 • ⏱️ 24:02 • 1d ago

---

**[Elon Musk&#39;s Smartest AI Robot Humiliates US Politicians With Its Intelligence](https://www.youtube.com/watch?v=BlOMUT2rcY0)**

Elon Musk presents a new AI-powered robot concept focused on pushing the limits of machine intelligence and real-time ...

📺 Carros Show

👁️ 21K • 👍 596 • 💬 53 • ⏱️ 8:27 • 3d ago

---

**[Japan Airlines to replace workers with humanoid robots](https://www.youtube.com/watch?v=_Lgughpiamw)**

Japan Airlines is trialling humanoid robots for luggage handling due to rising visitor numbers and a drop in the number of people ...

📺 Sky News Australia

👁️ 7K • 👍 116 • 💬 120 • ⏱️ 2:15 • 8h ago

---

**[China Just Built An AI Robot Army](https://www.youtube.com/watch?v=omtM-tl1Sj8)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: / pro_robots China is no longer just building robots for factories ...

📺 PRO ROBOTS

👁️ 13K • 👍 364 • 💬 48 • ⏱️ 18:35 • 4d ago

---

**[VEX IQ Robotics Competition : Level Up | 2026-2027 Game](https://www.youtube.com/watch?v=KP0FYPW604E)**

ORDER HERE: SUBSCRIBE: https://www.vex.com/YouTube ----------------------------------------------------------------------- Official Game ...

📺 VEX Robotics

👁️ 21K • 👍 618 • 💬 223 • ⏱️ 3:51 • 8h ago

---

**[The Pivot to Robots Has Already Begun | What The Future](https://www.youtube.com/watch?v=zw9LAjm9pso)**

Flash, a humanoid robot made by Chinese smartphone company Honor, just smashed the human world record for the ...

📺 CNET

👁️ 14K • 👍 288 • 💬 36 • ⏱️ 4:53 • 4d ago

---

**[Chinese Robots Are Flooding America. I Brought One Home.](https://www.youtube.com/watch?v=ucy9VTLDwPU)**

The Chinese-made Unitree G1 humanoid robots are making their way into the U.S. And they aren't just in viral videos but in major ...

📺 Joanna Stern

👁️ 124K • 👍 5K • 💬 635 • ⏱️ 11:11 • 1d ago

---

**[1X&#39;s New Humanoid Robot Factory to Build 10,000 NEOs #robot #robotics #humanoidrobots](https://www.youtube.com/watch?v=wIfGi3u-yl0)**

1X Technologies says it built its new robot factory in just a few months to fulfill more than 10000 preorders for its NEO humanoid ...

📺 Kalil 4.0

👁️ 1K • 👍 26 • ⏱️ 0:44 • 9h ago

---

**[Amazon&#39;s GEN 3.5 AI Robot Launch (AI NEWS)](https://www.youtube.com/watch?v=dhUXlqBttw0)**

NEURA Robotics has established a strategic partnership with Amazon to deploy the 4NE1 humanoid robot into logistics ...

📺 AI News

👁️ 5K • 👍 136 • 💬 15 • ⏱️ 8:19 • 6d ago

---

**[1 Robot Every Hour Figure AI Is Scaling Faster Than Expected](https://www.youtube.com/watch?v=rroW6afxLgo)**

Figure AI just revealed a massive production breakthrough, scaling humanoid robot output 24 times in just 120 days.

📺 DPCcars

👁️ 3K • 👍 71 • 💬 17 • ⏱️ 3:25 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

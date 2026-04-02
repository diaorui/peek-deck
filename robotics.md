---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-02T09:34:54.413289+00:00'
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

**Last Updated:** April 02, 2026 at 09:34 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[China announces its first automated manufacturing line capable of producing 10K humanoid robots per year - 1 robot every 30 minutes](https://www.reddit.com/r/robotics/comments/1s9qso0/china_announces_its_first_automated_manufacturing/)**

16h ago

---

**[Olaf couldn't handle too many human questions, suddenly crashed, collapsed, and its carrot nose fell off](https://www.reddit.com/r/robotics/comments/1s9g61s/olaf_couldnt_handle_too_many_human_questions/)**

23h ago

---

**["Follow Me" Mode: Real-time human tracking with YOLOv8](https://www.reddit.com/r/robotics/comments/1sac61n/follow_me_mode_realtime_human_tracking_with_yolov8/)**

33m ago

---

**[Working on an ego/exo dataset](https://www.reddit.com/r/robotics/comments/1sa17xd/working_on_an_egoexo_dataset/)**

I’m in a unique position as a small business owner and I’m looking for advice. I’ve been a long time follower of r/datahoarder and I think my friends over here in r/robotics might find what I have useful. I’ve been hanging on to about 12tb of MP4 footage that I captured at my business hoping I would find a use for it one day. Now it seems like every other day I read another article about the data scarcity in robotics training and the sim to real gap. So I’m wondering if I might be able to connect some pieces and license this video as a dataset. I did some research and found that a first person view seems to be the most valuable for embodied AI training so I recently I added GoPros on my customers to capture that as well. I think what I have may be useful for some training cases. It is a lot of video of human object interaction and high force material interactions and real world unscripted human dynamics. Theres a ton of edge case stuff where things don’t go exactly like it was planned because of the chaotic atmosphere. I have a few hundred hours of the GoPro footage and about 6500 hours of the cctv footage. Currently adding a few hundred hours per month of video with pretty open customizability. I’ve been tinkering with Yolo and SAM2 models as well. All the personal identifiable information has been cleared and all customers are aware of the use of this video for AI training purposes. Would this be useful for some of you and if so, what would be the best way to package it for you? I appreciate your time!

9h ago

---

**[Our personal AI robotic arm is on the way!](https://www.reddit.com/r/robotics/comments/1sab8gj/our_personal_ai_robotic_arm_is_on_the_way/)**

1h ago

---

**[meche.ai- Hardware engineering tools!](https://www.reddit.com/r/robotics/comments/1sa9nhr/mecheai_hardware_engineering_tools/)**

Hi! I’m working on bunch of tools for product design engineers and going to add them under [https://meche.ai\](https://meche.ai) Currently I have: [https://printadvisor.ai\](https://printadvisor.ai) (material selection, print settings feedback) [https://tolanalysis.com\](https://tolanalysis.com) (tolerance stack up, Monte Carlo sim, Cpk analysis) [https://dfmanalysis.com/\](https://dfmanalysis.com/) (DFM for CNC, sheet metal) [https://pd.meche.ai\](https://pd.meche.ai) (PD interview prep tool) [https://cad.meche.ai\](https://cad.meche.ai) (CAD viewer which is beautiful) Please check them and let me know if you have any thoughts/feedback 🙏 I’m planning to build more tools that I can put into use myself and for the community! So far I love building with Claude and Cursor. Feels like a new power got unlocked! 🔓

3h ago

---

**[Assembly of parts](https://www.reddit.com/r/robotics/comments/1sack2t/assembly_of_parts/)**

8m ago

---

**[Text. Wave. Move. — Openclaw Controls Our Robot](https://www.reddit.com/r/robotics/comments/1sa8hos/text_wave_move_openclaw_controls_our_robot/)**

4h ago

---

**[I made my robot wal JUST LIKE BAYMAX](https://www.reddit.com/r/robotics/comments/1sabqhy/i_made_my_robot_wal_just_like_baymax/)**

it uses only two motors to walk unlike most other bipedal robots. What do you guys think? Also I just made the base and hand for now ! https://www.youtube.com/watch?v=InKbSM_C5Xc

59m ago

---

**[Analytically-seeded 3D bounded-curvature path solver (robust + batched) — would an API be useful?](https://www.reddit.com/r/robotics/comments/1saajey/analyticallyseeded_3d_boundedcurvature_path/)**

I’ve been working on a different approach to the 3D bounded-curvature path planning problem (Dubins-type), and I’m trying to gauge whether something like this is useful in robotics workflows. Most implementations I’ve used rely on either: iterative solvers (shooting / optimisation), or sampling-based planners (RRT*, etc.) These work, but can be sensitive to initialisation and may struggle with convergence in certain geometries — especially when evaluating many candidate trajectories. What this approach does Solves the 3D curve–line–curve problem for full pose constraints (position + direction) Uses analytical construction to initialise the solution, followed by a fast solve Supports variable curvature (radius) rather than fixed-radius Dubins Returns multiple valid solution branches, ranked by total path length Includes parameters to sweep ranges of curvature (radius) and evaluate resulting solutions Computational behaviour Because the initialisation is analytical: avoids fragile starting guesses significantly improves convergence reliability keeps runtime predictable The formulation is also fully vectorisable. In a GPU implementation, when evaluated in large batches (O(10³–10⁴)): <0.1 ms per query (amortised) For smaller batches / single queries, CPU execution is typically: ~10–20 ms per solve (Currently running on a Ryzen 5950X + RTX 3080 Ti server — API overhead on top of this. Not optimised for single-shot latency; the benefit comes from batching.) Why this seems useful The main advantage isn’t just speed — it’s that it becomes practical to: evaluate large numbers of candidate trajectories sweep curvature ranges and optimise trajectory selection select from multiple valid solutions ranked by path length avoid solver failure modes caused by poor initialisation Question I currently have this running behind an API and am considering exposing it more broadly. Would something like this be useful in your workflow? In particular: Do you need to evaluate many candidate trajectories quickly, or mostly solve single paths? Are convergence / initialisation issues a bottleneck in practice? Would you use an API for this, or prefer a local library? Would the ability to sweep curvature parameters and optimise solutions be valuable? Happy to share more detail or provide access if there’s interest.

2h ago

---

---

## Google News: "robotics"

**[Station Crew Works Robotics, Research as Artemis II Launch Preps Continue](https://www.nasa.gov/blogs/general-blog/2026/04/01/station-crew-works-robotics-research-as-artemis-ii-launch-preps-continue/)**

Robotics training and human research were the primary duties for the Expedition 74 crew aboard the International Space Station on Wednesday. The orbital residents rounded out their shift with spacesuit work, cargo operations, and Earth observations.

nasa.gov • 13h ago

---

**[The gig workers who are training humanoid robots at home](https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/)**

People in Nigeria and India are strapping iPhones onto their heads and recording themselves doing chores.

technologyreview.com • 22h ago

---

**[The world’s largest humanoid robot maker is going public](https://restofworld.org/2026/unitree-china-humanoid-robot-shanghai-ipo/)**

Rest of World • 1d ago

---

**[Europe Vies to Be Humanoid Robot Leader in Global Tech Race](https://www.bloomberg.com/news/articles/2026-04-01/europe-vies-to-be-humanoid-robot-leader-in-global-tech-race)**

Bloomberg.com • 19h ago

---

**[Robots learn to ask humans for help](https://www.axios.com/2026/04/01/robots-delivery-serve-tmobile)**

axios.com • 13h ago

---

**[Researchers build a robotic swarm with no electronics, no batteries and no brains](https://techxplore.com/news/2026-04-robotic-swarm-electronics-batteries-brains.html)**

Tech Xplore • 19h ago

---

**[OpenAI to Expand to East Bay With Plans For Huge New Robotics Facility](https://sfist.com/2026/03/31/openai-to-expand-to-east-bay-with-plans-for-new-200-000-square-foot-robotics-facility/)**

OpenAI signed a new lease on a 202,000-square-foot waterfront site near the Richmond ferry terminal in its first East Bay expansion, and it’s believed the company will be opening a robotics facility there.

SFist • 1d ago

---

**[DNA robots could deliver drugs and hunt viruses inside your body](https://www.sciencedaily.com/releases/2026/03/260331001104.htm)**

DNA robots are emerging as tiny programmable machines that could one day deliver drugs, hunt viruses, and build molecular-scale devices. By borrowing ideas from traditional robotics and combining them with DNA folding techniques, scientists are creating structures that can move and act with precision. These robots can be guided using chemical reactions or external signals like light and magnetic fields.

ScienceDaily • 1d ago

---

**[FF Announces Fourth Quarter and Full Year 2025 Financial Results: Stockholders’ Equity Turns Positive; First Month of EAI Robotics Delivery Beats Target with Positive Product Gross Margin](https://www.businesswire.com/news/home/20260331069322/en/FF-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results-Stockholders-Equity-Turns-Positive-First-Month-of-EAI-Robotics-Delivery-Beats-Target-with-Positive-Product-Gross-Margin)**

Faraday Future Intelligent Electric Inc. (Nasdaq: FFAI) ("FF", "Faraday Future", or the "Company"), a California-based global Embodied AI (EAI) ecosystem com...

Business Wire • 1d ago

---

**[Voyager, Icarus Robotics to test free-flying robot on space station](https://www.reuters.com/science/voyager-icarus-robotics-test-free-flying-robot-space-station-2026-03-30/)**

Reuters • 2d ago

---

---

## YouTube Videos: "robotics"

**[Brett Adcock - Shawn Ryan’s First Interview with a Robot | SRS #292](https://www.youtube.com/watch?v=99pOdGEGu6s)**

Brett Adcock is a technology entrepreneur focused on building companies in robotics, artificial intelligence, and aerospace.

📺 Shawn Ryan Show

👁️ 444K • 👍 9K • 💬 3K • ⏱️ 2:57:09 • 2d ago

---

**[Xiaomi’s New AI Robot Hand Works Like a REAL Human… This Is INSANE](https://www.youtube.com/watch?v=Ubpk3tOl9gw)**

Xiaomi just dropped a robotic hand so realistic, it might fool you into thinking it's human — and that's just the START of what's ...

📺 The AI Nexus

👁️ 3K • 👍 143 • 💬 11 • ⏱️ 20:43 • 1d ago

---

**[Every Home Will Have a Humanoid Robot in 10 Years](https://www.youtube.com/watch?v=u4NLSzMP8z0)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCkoujZQZatbqy4KGcgjpVxQ/join Support the Shawn ...

📺 Shawn Ryan Clips

👁️ 9K • 👍 314 • 💬 132 • ⏱️ 15:18 • 2d ago

---

**[Robotic Frog VS Frog](https://www.youtube.com/watch?v=kwzDGQAzyuw)**

I put REAL animals up against their robotic versions in a series of intense head-to-head challenges: From speed and agility to ...

📺 Alex Turk

👁️ 199K • 👍 2K • 💬 73 • ⏱️ 9:36 • 5d ago

---

**[Melania Trump Goes OFF THE RAILS With Alarming Robot Teacher Announcement](https://www.youtube.com/watch?v=JsTKgM8fYUk)**

Melania Trump sparks alarm over a White House event where she walked in with a robot and made an announcement about ...

📺 The Damage Report

👁️ 19K • 👍 907 • 💬 441 • ⏱️ 8:42 • 6d ago

---

**[Humanoid robot ‘Figure 3’ appears alongside Melania Trump](https://www.youtube.com/watch?v=GVFi0eUMhoM)**

A humanoid robot named "Figure 3" walked alongside Melania Trump as she opened a global summit in Washington, drawing ...

📺 Global News

👁️ 29K • 👍 198 • 💬 77 • ⏱️ 0:47 • 6d ago

---

**[The Real-Life Future of Humanoid Robots](https://www.youtube.com/watch?v=ktwtZNKDV0E)**

Brett Adcock shares his vision for the future of humanoid robots, why he believes synthetic humans will become one of the most ...

📺 Shawn Ryan Show

👁️ 71K • 👍 2K • 💬 676 • ⏱️ 14:05 • 5d ago

---

**[“Three People CAN’T Stop It” - Robot Malfunction Sends Restaurant Into Chaos](https://www.youtube.com/watch?v=l0F6IEluvRo)**

Patrick Bet-David reacts to a viral moment where a restaurant robot malfunctions and starts acting unpredictably, raising serious ...

📺 Valuetainment

👁️ 123K • 👍 3K • 💬 348 • ⏱️ 11:21 • 6d ago

---

**[Unitree Open‑Source: High‑Quality Real‑Robot Dataset for Humanoid Robots](https://www.youtube.com/watch?v=pN_bj5-QyW8)**

Unitree open-sources UnifoLM-WBT-Dataset — a high-quality real-world humanoid robot whole-body teleoperation (WBT) ...

📺 Unitree Robotics

👁️ 8.4M • 👍 568 • 💬 96 • ⏱️ 1:28 • 6d ago

---

**[Roborock Saros 20 – Best Robot Vacuum of 2026 – So Far](https://www.youtube.com/watch?v=knsnUmWDVNY)**

We put the Roborock Saros 20 through our standard battery of tests! ✔️ Get the Saros 20 on Amazon https://geni.us/ChLf9 Top ...

📺 Vacuum Nerds

👁️ 16K • 👍 249 • 💬 71 • ⏱️ 14:43 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

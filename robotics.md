---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-24T17:30:02.851504+00:00'
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

**Last Updated:** April 24, 2026 at 17:30 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[SO-101's for it's ACT together](https://www.reddit.com/r/robotics/comments/1sudm58/so101s_for_its_act_together/)**

First rollout of a simple ACT model and the right looks like it got its ACT together The movement could be smoother I think. The robot still has to learn how to handle weird orientation of the cube. Wrote about it here https://x.com/pbshgthm/status/2047640796699267497

5h ago

---

**[Spin-tracking robot takes on elite table-tennis players - SonyAI](https://www.reddit.com/r/robotics/comments/1stuamz/spintracking_robot_takes_on_elite_tabletennis/)**

21h ago

---

**[Ahead form robotics new Origin F1 face](https://www.reddit.com/r/robotics/comments/1stz82p/ahead_form_robotics_new_origin_f1_face/)**

17h ago

---

**[We put an acoustic camera on a robot dog for gas leak detection – what else should we do with it?](https://www.reddit.com/r/robotics/comments/1sug0vn/we_put_an_acoustic_camera_on_a_robot_dog_for_gas/)**

Hi r/robotics, We’re the team from Hertzinno, and we develop industrial acoustic cameras (real-time sound visualization). Recently we’ve been integrating our acoustic camera with quadruped robots for autonomous inspection tasks. The obvious use cases so far: · Compressed air & gas leak detection (finding invisible leaks with sound) · Mechanical fault localization (bearing wear, abnormal noises in motors/gearboxes) But we bet this community has way more creative ideas than we can come up with in our engineering bubble. So we’d love to ask: What surprising or non-obvious applications do you see for a mobile acoustic camera robot?

3h ago

---

**[Why the VLA architecture hits a ceiling in real homes, and what a unified multimodal approach looks like in practice](https://www.reddit.com/r/robotics/comments/1suel0v/why_the_vla_architecture_hits_a_ceiling_in_real/)**

I've been thinking a lot about why current embodied AI models struggle so hard to cross the gap from lab demos to actual unstructured environments, and I think the root cause is architectural. Most of the field has converged on VLA (Vision-Language-Action) as the default paradigm for robot foundation models. It works well enough in controlled settings, but after reading about recent real-home deployment attempts and digging into the technical critiques, I'm increasingly convinced VLA has a structural ceiling that no amount of scaling will fix. The core issue is that VLA is three separate modules stitched together in sequence. Vision recognizes objects, language parses the instruction, action generates a trajectory. Data passes across module boundaries at each step, and each handoff loses information and adds latency. By the time rich visual context reaches the action head, it has been compressed into what amounts to a blurry summary. Think of it like a game of telephone: the vision module "sees" that a plate is hanging halfway off the table edge, but by the time that spatial detail reaches the action planner through the language bottleneck, the geometric nuance that would let the robot nudge it back is gone. The second problem is deeper. VLA models fundamentally learn to imitate trajectories they've seen during training. They don't build an internal model of physics. The robot doesn't understand why a cup falls when pushed off a surface. It doesn't reason about gravity, inertia, or friction. It just replays the closest matching trajectory from its training distribution. This means every novel situation (and homes are basically infinite novel situations) requires either a training example that's close enough or the robot fails. A cat jumping on a table, a sock in an unexpected spot, a different carpet friction than the lab floor: each of these can break the pipeline. Third, error recovery is essentially nonexistent. When a VLA model fails mid-task, it typically halts and returns an error. It cannot learn from that failure in situ. The failure data has to be collected, shipped back to a training pipeline, incorporated into a new training run, and redeployed. This makes the gap between lab performance and real world performance almost impossible to close at scale. The best analogy I've seen for an alternative approach comes from Apple Silicon's unified memory architecture. Pre-M1 Macs had CPU, GPU, and memory as separate components shuttling data between them, with all the bandwidth and latency penalties that implies. Unified memory put everything in one shared pool, and the performance jump was massive. The same logic applies to embodied AI: instead of three separate modules passing data sequentially, what if vision, language, action, and physics prediction were all trained jointly inside a single network from the start? This is essentially what a World Unified Model (WUM) architecture attempts. X Square Robot recently announced WALL-B, which they describe as a natively multimodal foundation model where all modalities (vision, audio, language, touch, action) are synchronously labeled and jointly trained from day one. No inter-module boundaries, no sequential data transfer. The robot sees a cup and begins preparing the reach simultaneously; it feels the weight and adjusts force in the same forward pass rather than waiting for a separate module to process the feedback. What makes this interesting technically is three specific capabilities they claim emerge from this architecture. First, native proprioception: the model internally senses its own spatial dimensions (arm reach, body width) and can judge whether it fits through a gap or can reach an object without relying on external sensors or constantly observing its own body. Second, physics grounding: the model predicts gravity, inertia, and friction, enabling zero-shot generalization because physics is consistent across environments. A plate half off a table edge gets pushed back not because the robot saw that specific scenario in training, but because it predicts the plate will fall. Third, in-the-wild self-evolution: on failure, the model adjusts strategy and retries, and if the retry succeeds, the result updates the model parameters directly. No engineer retraining, no trip back to the lab. I want to be clear about limitations here. Their own CEO described the current model as being at an "intern" stage. The robots will make mistakes, sometimes stop mid-task to "think," and still need remote assistance. They've committed to deploying WALL-B-powered robots into volunteer households starting May 26, which is a bold timeline. Whether the architecture delivers on these claims in messy real environments is very much an open question. The data strategy is also worth noting. They've been collecting what they call "milk data" from hundreds of volunteer households (as opposed to clean lab data, which they call "sugar water"). The argument is that messy, variable, unpredictable real-home data is what actually drives generalization, and that a data flywheel from real deployments is the actual moat. Curious what people here think about the VLA ceiling argument. Is the sequential module architecture fundamentally limiting, or is it just a scaling problem? And does training all modalities jointly from scratch actually produce emergent physics understanding, or is that a stretch?

4h ago

---

**[US Air Force tests Anduril semiautonomous combat jet drone without direct pilot control](https://www.reddit.com/r/robotics/comments/1subhoa/us_air_force_tests_anduril_semiautonomous_combat/)**

The U.S. Air Force tested a jet-powered YFQ-44A drone that can fly missions on its own, without a pilot controlling it in real time.

🔗 [Interesting Engineering](https://interestingengineering.com/military/usaf-jet-drone-semiautonomous-flight-test) • 7h ago

---

**[Unitree has added wheels, roller skates, and ice skates to their G1](https://www.reddit.com/r/robotics/comments/1stewlj/unitree_has_added_wheels_roller_skates_and_ice/)**

From Unitree on 𝕏: https://x.com/UnitreeRobotics/status/2047257759473946705

1d ago

---

**[How useful has Claude Code been for you?](https://www.reddit.com/r/robotics/comments/1suelxj/how_useful_has_claude_code_been_for_you/)**

Hey everyone, I've been building autonomous drones with a monocular camera and have been trying to make good use out of Claude Code for my software development. I noticed that while it's great at writing the boilerplate of my ROS2 nodes, the second I get into runtime messaging, Claude has no idea when one message will publish compared to another. Similarly, when I'm doing any work regarding transforms, Claude seems to have no idea about the robots actual position in a world, and it ends up simply guessing what the right transform is. I get a little frustrated by it because I look at web development and see how much Claude has increased the speed of development there. Some of the super AI-first people are letting their agents run overnight. I feel like if I tried that right now, it would just destroy my repository, since I have to hold Claude's hand at every stage. I'm using ROS2 Jazzy and PX4. Anyone else seeing similar problems? If so, how are you currently getting around it?

4h ago

---

**[Robots learning complex tasks by observing humans how self aware are they really.](https://www.reddit.com/r/robotics/comments/1suj5kl/robots_learning_complex_tasks_by_observing_humans/)**

Robots are now able to learn complex tasks by observing humans. This marks a shift toward more flexible and adaptive systems, while also sparking debate around how real the concept of “self-awareness” actually is.

🔗 [NPR](https://www.npr.org/2026/04/24/nx-s1-5797863/self-aware-robots-future-laundry-work-home) • 1h ago

---

**[I feel like we’re mixing up “clean” and “sanitized” way too casually](https://www.reddit.com/r/robotics/comments/1suc8r1/i_feel_like_were_mixing_up_clean_and_sanitized/)**

Since my baby started crawling, I’ve been wondering about the difference between “cleaning” and “sanitizing” and whether my robot vacuum actually provides one over the other. The more I read, the more I realize that the two terms get mixed up in conversations, but when it comes to my baby, I want to be sure the floor is sanitized, not just clean. Roller brushes seem to agitate the floor, lifting up debris, but I’ve started to wonder if they’re just redistributing fine particles instead of really removing them. Flat pads, on the other hand, seem to cover more area but don’t agitate the floor as much, meaning they don’t have the same power to lift debris. So the question is: can either of these methods actually sanitize the floor? Or are we just focusing on making the floor look clean? I’m curious if anyone has looked into this from a sanitation standpoint. I want to ensure my baby’s floor is not only free of visible dirt but also of any harmful germs or particles. Has anyone experimented with comparing these methods or found a better alternative for sanitizing, especially for babies?

6h ago

---

---

## Google News: "robotics"

**[Pudu Robotics raises nearly $150M as it targets industrial applications](https://www.therobotreport.com/pudu-robotics-raises-nearly-150m-targets-industrial-applications/)**

Pudu plans to use the funding to develop its embodied AI, grow its product portfolio, and expand in global markets beyond service robots.

The Robot Report • 22h ago

---

**[Accenture, Vodafone Procure & Connect and SAP Pilot Humanoid Robotics in Warehouse Operations](https://newsroom.accenture.com/news/2026/accenture-vodafone-procure-connect-and-sap-pilot-humanoid-robotics-in-warehouse-operations)**

Accenture (NYSE: ACN), together with Vodafone Procure & Connect and SAP, is piloting the use of humanoid robotics in warehouse environments, demonstrating how physical AI can enhance operational efficiency, improve safety, and enable new approaches to workforce and business model design.

Accenture • 2d ago

---

**['Self-aware' robots can learn complex tasks by watching humans. Is that a good thing?](https://www.npr.org/2026/04/24/nx-s1-5797863/self-aware-robots-future-laundry-work-home)**

Scientists say they've made a key breakthrough that would allow robots to figure out complex tasks on their own — but experts say it raises questions about how much risk comes with letting robots be in charge of their own learning.

NPR • 7h ago

---

**[Physical AI: Where Artificial Intelligence Rubber Meets The Road](https://www.investors.com/news/physical-ai-jensen-huang-nvidia-artificial-intelligence-robotics/)**

Investor's Business Daily • 21h ago

---

**[German robotics, automation company picks Greenville for headquarters](https://www.greenvilleonline.com/story/money/business/2026/04/23/idealworks-chooses-greenville-for-u-s-headquarters-heres-why/89737706007/)**

Idealworks spun out of BMW Group in Munich, and the Greenville location puts it in the middle of some of the most advanced manufacturing in the U.S.

Greenville Online • 1d ago

---

**[IDF escalates use of robots in Lebanon to target Hezbollah infrastructure](https://www.jpost.com/defense-and-tech/article-893843)**

The IDF has ramped up its use of robots in warfare against Hezbollah in Bint Jbail, accelerating the destruction of weapons infrastructure as military operations intensify.

The Jerusalem Post • 2d ago

---

**[Tesla investors really need to see progress on Robotaxi, robotics](https://finance.yahoo.com/video/tesla-investors-really-need-to-see-progress-on-robotaxi-robotics-214456931.html)**

Tesla (TSLA) reported first quarter results on Wednesday after the closing bell. Adjusted earnings per share (EPS) came in at $0.41 (compared to analyst estimates of $0.34), and revenue came in at $22.39 billion (compared to analyst estimates of $22.19 billion). Yahoo Finance Senior Autos Reporter Pras Subramanian and Barron's associate editor Al Root discuss what investors need from Tesla on robotaxi and robots.

Yahoo Finance • 1d ago

---

**[Tesla: The Street Wrongly Hates The Capex Plan, AI & Robotics On Track (NASDAQ:TSLA)](https://seekingalpha.com/article/4894026-tesla-the-street-wrongly-hates-the-capex-plan-ai-and-robotics-on-track)**

Tesla delivered a Q1 double-beat, but shares fell as high capex spending and cautious AI scaling tempered optimism. Read more on TSLA stock here.

Seeking Alpha • 1h ago

---

**[Tesla Beats First-Quarter Expectations Amid Pivot To Robotics, AI](https://www.forbes.com/sites/aliciapark/2026/04/22/tesla-beats-first-quarter-expectations-amid-business-pivot-to-robotics-ai/)**

The automaker said demand for its vehicles has rebounded from recent declines .

Forbes • 1d ago

---

**[US ramps up humanoid robotics as China threat grows in AI race](https://www.foxbusiness.com/video/6393711598112)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump discuss battlefield robotics, national security risks, and China competition on ‘Mornings with Maria.

Fox Business • 1d ago

---

---

## YouTube Videos: "robotics"

**[Unitree Robot With Wheels Moves In Ways You Did Not Expect](https://www.youtube.com/watch?v=H-X7v7Y4oPc)**

Unitree just revealed a humanoid robot using wheels, skates, and even ice blades, and it completely changes how we think about ...

📺 DPCcars

👁️ 3K • 👍 39 • 💬 28 • ⏱️ 4:20 • 1d ago

---

**[This robot can beat you at table tennis](https://www.youtube.com/watch?v=EH8kZDc7OLk)**

For the first time, an AI-powered machine has bested elite-level athletes at a physical sport. 'Ace' is a table tennis-playing robot.

📺 nature video

👁️ 81K • 👍 1K • 💬 170 • ⏱️ 13:38 • 2d ago

---

**[China&#39;s Robotics Innovation Is Moving Faster Than Anyone Realizes](https://www.youtube.com/watch?v=qB0SsWTEBlU)**

I thought this would be just another robot demo... I was wrong.At this launch event, X Square Robot introduced a new kind of home ...

📺 Barrett

👁️ 6K • 👍 209 • 💬 14 • ⏱️ 5:43 • 1d ago

---

**[Chinese humanoid robots outrun humans in half-marathon, setting records](https://www.youtube.com/watch?v=k5_Tlgvt-c8)**

Over a hundred Chinese-made humanoid robots participated in a half-marathon race in Beijing on Sunday. The second inaugural ...

📺 Global News

👁️ 207K • 👍 2K • 💬 138 • ⏱️ 0:46 • 4d ago

---

**[New AI Robot From China Breaks Human Limits](https://www.youtube.com/watch?v=EJbJMg2RNgw)**

AGIBOT just rolled out a full new wave of humanoid robots and AI models built for real deployment, while researchers in South ...

📺 AI Revolution

👁️ 34K • 👍 819 • 💬 54 • ⏱️ 16:29 • 3d ago

---

**[Real dogs meet Elon Musk robot dog](https://www.youtube.com/watch?v=oNhJwi4b99Q)**

An Elon Musk robotic dog was seen wandering around San Francisco, bumping into some furry friends. It's all to promote a new ...

📺 CNN

👁️ 160K • 👍 2K • 💬 396 • ⏱️ 0:42 • 5d ago

---

**[50 Minutes: How China&#39;s Robot Destroyed the Half Marathon Record](https://www.youtube.com/watch?v=pH8tVBqCRLY)**

In Beijing, a humanoid robot just completed a 21-kilometer half-marathon in an astonishing 50 minutes and 26 seconds, marking ...

📺 Capital Markets AI

👁️ 34K • 👍 648 • 💬 150 • ⏱️ 8:58 • 5d ago

---

**[UNEXPECTED LINK: Trump family TIED to humanoid robot CLASH with China](https://www.youtube.com/watch?v=SWoVms-enPU)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump ...

📺 Fox Business

👁️ 50K • 👍 1K • 💬 362 • ⏱️ 10:17 • 1d ago

---

**[AI Robots Are Glitching BAD… We Might Have A Problem! (2026)](https://www.youtube.com/watch?v=6p1Me03BPhM)**

AI robots failing and glitching 2026 is becoming impossible to ignore. From humanoid robots malfunctioning to AI systems ...

📺 MindSeeded

👁️ 306K • 👍 17K • 💬 3K • ⏱️ 14:10 • 6d ago

---

**[Chinese humanoid robot beats world record for fastest human half-marathon | ABC NEWS](https://www.youtube.com/watch?v=tcfAm3hNQbk)**

A humanoid robot has beaten the human record for the world's fastest half-marathon by finishing in just over 50 minutes. Dozens ...

📺 ABC News (Australia)

👁️ 100K • 👍 645 • ⏱️ 6:44 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

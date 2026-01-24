---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-24T07:41:00.614071+00:00'
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

**Last Updated:** January 24, 2026 at 07:41 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[First field test of 'Papaya Pathfinder', my 3D-printed Rocker-Bogie rover. Checking suspension geometry and motor torque on uneven terrain.](https://www.reddit.com/r/robotics/comments/1ql44r0/first_field_test_of_papaya_pathfinder_my/)**

9h ago

---

**[RIVR robot vs human; Just Eat takeway delivery](https://www.reddit.com/r/robotics/comments/1qkquft/rivr_robot_vs_human_just_eat_takeway_delivery/)**

18h ago

---

**[Walking robot](https://www.reddit.com/r/robotics/comments/1qlg5di/walking_robot/)**

40m ago

---

**[We thought the design was locked. Then early testers asked for "Eyes". Now we are conflicted.](https://www.reddit.com/r/robotics/comments/1qkz4i6/we_thought_the_design_was_locked_then_early/)**

Quick update post-CES. We thought we had the hardware definition 99% done, but the feedback from our first batch of hands-on users is making us second-guess two major decisions. Need a sanity check from you guys before we commit to the final molds/firmware. **Dilemma 1: Vex (The Pet Bot) - Does it need "Eyes"?** Right now, Vex is a sleek, minimalist sphere. It looks like a piece of high-end audio gear or a giant moving camera lens. But the feedback we keep getting from pet owners is: _"It feels too much like a surveillance tool. Give it eyes so it feels like a companion."_ We are torn. * **Option A (Current):** Keep it clean. It's a robot, not a cartoon character. * **Option B (Change):** Add digital eye expressions (using the existing LED matrix or screen). My worry: Does adding fake digital eyes make it look "friendly", or does it just make it look like a cheap toy? Where is the line? **Dilemma 2: Aura (The AI) - Jarvis vs. Her** We originally tuned Aura's voice to sound crisp, futuristic, and efficient. Think TARS from Interstellar or Jarvis. We wanted it to feel "Smart". But users are telling us it feels cold. They are asking for more "human" imperfections—pauses, mood swings, maybe even sounding tired in the evening. We can re-train the TTS (Text-to-Speech) model, but I'm worried about the "Uncanny Valley". **Do you actually want your desktop robot to sound emotional, or do you just want it to give you the weather report quickly?** If you have a strong opinion on either, let me know. We are literally testing the "Emotional Voice" update in our internal build right now. _(As always, looking for more people to roast these decisions in our discord beta group. Let me know if you want an invite.)_

12h ago

---

**[My new Quadruped project](https://www.reddit.com/r/robotics/comments/1qkj4u8/my_new_quadruped_project/)**

This is my new project 'DEFY'. I plan to make it into a 3D printer and I plan to use SLM metal printing and carbon fiber parts appropriately. (I'm a 19-year-old dropout and my dream is to work for a company even if it's an internship!) 😼👍

1d ago

---

**[Google Gemini Is Taking Control of Humanoid Robots on Auto Factory Floors](https://www.reddit.com/r/robotics/comments/1qkk6gv/google_gemini_is_taking_control_of_humanoid/)**

The ultimate crossover: Boston Dynamics' electric Atlas robot now has a Google Gemini brain. A new report details how DeepMind is integrating its multimodal AI into the robot, allowing Atlas to understand natural language commands (like 'Find the breaker box'), reason about its environment, and plan complex tasks autonomously. The partnership aims to deploy these 'physically intelligent' humanoids into Hyundai factories by 2026.

🔗 [WIRED](https://www.wired.com/story/google-boston-dynamics-gemini-powered-robot-atlas/) • 1d ago

---

**[I know the theory but i don't know how to build a robot](https://www.reddit.com/r/robotics/comments/1ql5xzt/i_know_the_theory_but_i_dont_know_how_to_build_a/)**

I have a fairly solid understanding of the theory behind robotics, both in terms of kinematics/dynamics and sensors/actuators. During my CS master’s degree I took a robotics course, where I worked extensively with ROS2 and other tools like RViz. However, on the practical side I’ve never really built anything with my hands. Right now I have a Raspberry Pi and access to a 3D printer, and since taking that robotics course a few months ago I’ve become really passionate about the topic and would like to start working on some projects. Given that I already have a strong theoretical background and coding experience, but little hands-on experience with actually assembling a robot, where would you recommend starting?

8h ago

---

**[My 3D printed robot lifts 2kg](https://www.reddit.com/r/robotics/comments/1qkdka0/my_3d_printed_robot_lifts_2kg/)**

1d ago

---

**[ROS News for the Week of January 19th, 2026](https://www.reddit.com/r/robotics/comments/1ql1plp/ros_news_for_the_week_of_january_19th_2026/)**

ROS News for the Week of January 19th, 2026      🦾 🇰🇷 This week marked our first ever regional ROSCon in South Korea!                Our ROS social calendar has filled back up again. There is a Gazebo Community Meeting on Forest3D next Wednesday and ROS By-The-Bay with Main Street Autonomy and @skye.galaxy next Thursday. The following week there is a robotics Dev room at FOSDEM and a Dronecode Meetup in Leuven, Belgium. This week we also announced a ROS Singapore Meetup...

🔗 [Open Robotics Discourse](https://discourse.openrobotics.org/t/ros-news-for-the-week-of-january-19th-2026/52057) • 11h ago

---

**[Robotics -> biomechanics polytopes](https://www.reddit.com/r/robotics/comments/1qkwg4q/robotics_biomechanics_polytopes/)**

LTDR; this is a geometric kernel for measuring constraint-induced force distribution collapse in redundant systems. This is not novel in robotics, but I would like some feedback. It is usable, it uses the stock walking gait model in OpenSim so the lowerbody is muscle actuated and the upper body and torso are coordinate / torque actuated. Each frame will read out feasible or infeasible(the configuration/pose). If infeasible you can diagnose the infeasibility (gravity scaling/DoF masking/joint specific actuation, constraint switches) If feasible, then you get the effective dimensions of the polytope(so far I’ve seen up to 70% reduction of the dimensions). This creates a near unique equilibrium solution as a consequence of “optionality”(or lack of). Btw this is quasi static analysis. #Readme# Force Pathway Measurement Theory (FPMT) applies feasible wrench polytope methods from robotics to quantify constraint-induced force distribution collapse in redundant musculoskeletal systems. Rather than selecting a single solution via optimization, FPMT computes the entire admissible set of internal forces satisfying equilibrium and geometric constraints. This allows for measuring "optionality" (the feasible set size) and determining when force distributions become deterministic due to constraints. FPMT computes the full admissible set of internal forces and reports optionality metrics (Chebyshev clearance, CCI, effective dimension) instead of selecting a single solution via optimization. —— I’ve had engineers try to poke holes already, the big ask really is the math. Here is the GitHub for my project: https://github.com/mechanist01/FPMT Here’s the paper that inspired it: https://arxiv.org/pdf/2110.06790

14h ago

---

---

## Google News: "robotics"

**[Introducing Rho-alpha, the new robotics model from Microsoft](https://www.microsoft.com/en-us/research/story/advancing-ai-for-the-physical-world/)**

Rho-alpha, which translates natural language commands into control signals for robotic systems doing bimanual manipulation tasks, aims to make physical systems more adaptable by using physical sensing modalities like touch and continuous learning from human feedback.

Microsoft • 3h ago

---

**[Inside the OpenAI lab where workers train robotic arms to fold laundry and toast bread](https://www.businessinsider.com/open-ai-robotics-lab-humanoid-robots-2026-1)**

OpenAI has rapidly scaled its robotics lab over the past year and plans to open up a second lab, insiders say.

Business Insider • 1d ago

---

**[Saga Robotics bets big on US vineyards with new GM, fresh capital](https://agfundernews.com/saga-robotics-bets-big-on-us-vineyards-with-new-gm-fresh-capital-for-uv-c-bots-chemical-free-winegrowing-is-the-holy-grail)**

During the 2025 California wine grape season, Saga Robotics increased treated acreage tenfold and expects to nearly triple it again in 2026.

AgFunderNews • 1d ago

---

**[Nvidia's Jensen Huang says AI robotics is a 'once-in-a-generation' opportunity for Europe](https://www.cnbc.com/2026/01/21/nvidia-jensen-huang-robotics-opportunity-europe-.html)**

Europe's industrial base sets it up well to lead in the physical AI space, Huang told WEF

CNBC • 2d ago

---

**[Microsoft Research reveals Rho-alpha vision-language-action model for robots](https://www.therobotreport.com/microsoft-research-reveals-rho-alpha-vision-language-action-model-for-robots/)**

The Rho-alpha model incorporates sensor modalities such as tactile feedback and is trained with human guidance, says Microsoft.

The Robot Report • 2d ago

---

**[Serve Enters Healthcare With Diligent Robotics Acquisition](https://finance.yahoo.com/news/serve-enters-healthcare-diligent-robotics-161400132.html)**

SERV enters healthcare with a $29M stock deal for Diligent Robotics, adding Moxi hospital robots and expanding its platform into indoor environments.

Yahoo Finance • 2d ago

---

**[Elon Musk says Tesla will likely sell humanoid robots by end of next year](https://www.foxbusiness.com/economy/elon-musk-says-tesla-likely-sell-humanoid-robots-end-next-year)**

Elon Musk said Tesla's Optimus humanoid robots could be available for public purchase by the end of 2027, saying the robots should be reliable, safe and capable of a range of functions.

Fox Business • 1d ago

---

**[Elon Musk, a fierce Davos critic, tells World Economic Forum that robots will outnumber humans](https://www.cbsnews.com/news/elon-musk-davos-world-economic-forum/)**

The billionaire CEO of Tesla and SpaceX, in his first appearance at Davos, said Tesla could start selling its Optimus robots next year.

CBS News • 1d ago

---

**[Elon Musk: Humanoid robots will be sold by 'end of next year'](https://finance.yahoo.com/video/elon-musk-humanoid-robots-sold-190041670.html)**

Tesla (TSLA) CEO and SpaceX (SPAX.PVT) founder Elon Musk sat down for an interview at the 2026 World Economic Forum (WEF) in Davos, Switzerland, on Thursday. Watch the video above to hear Musk's updates on humanoid robots. Watch Musk's full World Economic Forum address. More from Davos: Watch President Trump's full World Economic Forum address. Watch Nvidia CEO Jensen Huang's conversation with BlackRock CEO Larry Fink. For more expert insight and the latest market action, click&nbsp;here.

Yahoo Finance • 1d ago

---

**[Dr. Oz: AI and robots can already provide medical care](https://www.axios.com/2026/01/22/dr-oz-davos-ai-medical-health)**

Axios • 1d ago

---

---

## YouTube Videos: "robotics"

**[Xpeng’s New ET1 AI Robot Just Broke the AI  Humanoid Limit — Optimus Killer Enters Mass Production](https://www.youtube.com/watch?v=T8IYzqINZJY)**

XPENG Robotics just changed the game — their new ET1 AI humanoid robot has officially entered mass production, and it's ...

📺 The AI Nexus

👁️ 1K • 👍 78 • 💬 10 • ⏱️ 18:41 • 8h ago

---

**[Figure&#39;s New AI Robot Runs Like a Real Human... Figure 03’s secret “Fitness Program”](https://www.youtube.com/watch?v=G0xbD8Dwka0)**

Figure AI just broke the internet — their new Figure 03 humanoid robot is running like a real human, and the footage looks unreal.

📺 The AI Nexus

👁️ 8K • 👍 236 • 💬 21 • ⏱️ 19:35 • 5d ago

---

**[Elon Musk: My prediction is that there will be more robots than people](https://www.youtube.com/watch?v=fqIfoLrOSbA)**

Elon Musk, CEO of Tesla, sits down with Larry Fink, chair and CEO at BlackRock, to discuss the future of robotics, the impact of ...

📺 CNBC Television

👁️ 7K • 👍 70 • 💬 52 • ⏱️ 2:47 • 1d ago

---

**[Most Humanlike AI Robot at CES 2026 Will Make You UNCOMFORTABLE](https://www.youtube.com/watch?v=nGJ6u_5RkOw)**

CES 2026 just unveiled the most humanlike AI robot ever created — and it's making everyone deeply uncomfortable. Standing ...

📺 The AI Nexus

👁️ 3K • 👍 95 • 💬 19 • ⏱️ 26:30 • 4d ago

---

**[This is the &#39;problem&#39; with robotics for the last seven decades: Skild AI CEO](https://www.youtube.com/watch?v=8em2F0kqO90)**

Skild AI co-founder and CEO Deepak Pathak explains how robots are trained by watching humans perform tasks and more on ...

📺 Fox Business

👁️ 14K • 👍 231 • 💬 47 • ⏱️ 5:12 • 5d ago

---

**[Tesla is betting on robots &amp; robotaxis, but former bull Ross Gerber is skeptical](https://www.youtube.com/watch?v=fzuqnIGorNA)**

Gerber Kawasaki Wealth and Investment Management CEO, Ross Gerber, joins Market Domination host Josh Lipton to discuss ...

📺 Yahoo Finance

👁️ 471 • 👍 24 • 💬 6 • ⏱️ 6:39 • 2h ago

---

**[This Humanoid Robot Just Gave Me a Massage… | CES 2026 | ROBOTERA L7](https://www.youtube.com/watch?v=6NXerYBsLzQ)**

At CES 2026, I didn't expect a humanoid robot to do this… This RobotEra robot can safely interact with humans in ways that feel ...

📺 KhanFlicks

👁️ 79K • 💬 36 • ⏱️ 12:09 • 6d ago

---

**[Which Robot has the Best Fall Recovery? China Robot Vs USA Robot #robot #robotics](https://www.youtube.com/watch?v=KkMdPRka1qE)**

📺 Chris Wabs

👁️ 16K • 👍 114 • 💬 29 • ⏱️ 0:17 • 4d ago

---

**[Build The Deadliest Robot, Win $1,000!](https://www.youtube.com/watch?v=82QfRP6PSko)**

We built extreme robots and fought them in an actual arena! The deadliest robot wins $1000! BUY THE MERCH!

📺 Stay Wild

👁️ 3.9M • 👍 39K • 💬 2K • ⏱️ 33:05 • 5d ago

---

**[NEW Robot AMMIT takes over War Robots now! (FULL REVIEW)](https://www.youtube.com/watch?v=D9OQisokKgU)**

War Robots Gameplay: NEW Robot AMMIT Mk3 - completely taking over! #warrobots #warrobotsgameplay #wr My Best-Of-War ...

📺 Manni-Gaming

👁️ 11K • 👍 718 • 💬 161 • ⏱️ 28:24 • 18h ago

---

---

*Generated by PeekDeck - A glance is all you need*

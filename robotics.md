---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-01-24T12:43:01.696750+00:00'
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

**Last Updated:** January 24, 2026 at 12:43 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Walking robot](https://www.reddit.com/r/robotics/comments/1qlg5di/walking_robot/)**

5h ago

---

**[Instructions for my cycloidal drive are now available](https://www.reddit.com/r/robotics/comments/1qlhx97/instructions_for_my_cycloidal_drive_are_now/)**

A while a go I uploaded a post about my diy cycloidal drive I built with the help of JLCCNC. Some of you asked for building instructions. The full building instructions with the bill of materials is now online on Instructables: https://www.instructables.com/Building-a-Custom-Cycloidal-Drive-for-Robotic-Arm/ The gearbox has very little to no backlash and can tolerate very high bearing loads, while beeing realatively inexpensive to build.

3h ago

---

**[First field test of 'Papaya Pathfinder', my 3D-printed Rocker-Bogie rover. Checking suspension geometry and motor torque on uneven terrain.](https://www.reddit.com/r/robotics/comments/1ql44r0/first_field_test_of_papaya_pathfinder_my/)**

14h ago

---

**[Autonomous Drone Landing Pad](https://www.reddit.com/r/robotics/comments/1qlho6t/autonomous_drone_landing_pad/)**

https://marvelmind.com/3d_vertical_map/

4h ago

---

**[Precise Positioning For Autonomous Boats Without GPS](https://www.reddit.com/r/robotics/comments/1qllqpd/precise_positioning_for_autonomous_boats_without/)**

Typical cases: - Docking of smaller unmanned boats to larger ships - rescue operations, etc. - Boats indoors - universities, research - Boats with underwater sonars for the floor imaging - GNSSs are intentionally jammed - https://marvelmind.com/solution/boats/

14m ago

---

**[RIVR robot vs human; Just Eat takeway delivery](https://www.reddit.com/r/robotics/comments/1qkquft/rivr_robot_vs_human_just_eat_takeway_delivery/)**

23h ago

---

**[Experience with running VLA models (Pi0.5, SmolVLA) on SO-101 arms. Main takeaway: these require really beefy GPUs even for inference. Observations and questions.](https://www.reddit.com/r/robotics/comments/1qljzmh/experience_with_running_vla_models_pi05_smolvla/)**

I’m exploring VLA models, training my LeRobot SO-101 arms to do some simple, fun tasks. My first task to start with: "pickup the green cube and drop it in the bowl". It's been surprisingly challenging, and led me to a few observations and questions. Pi0.5 Pi0.5 is described as a general VLA, that can generalise to messy environments, I figured that I should be able to run my task on the arms, and see how it performs before doing any finetuning. This is a simple task, and a general adaptable model, so perhaps it'd be able to perform it straight away. Running it on my M1 Pro MBP with 16GB of RAM, it took about 10 minutes to get started, then maxed out my computer memory and ultimately forced it to restart before any inference could happen. I reduced the camera output to a low enough frame size and fps down to 15 to help the performance, but even so, I had the same result. So this is my first learning -- these models require very high-spec hardware. M1 Pro MBP of course isn't the latest, and I'm happy to upgrade, but it surprised me that this was far beyond it's capabilities. SmolVLA So then I tried with SmolVLA base. This did run! Without any pre-training, the arms essentially go rigid, and then refuse to move from that position. So this will require a lot of fine-tuning to work. But it's not clear to me if this is because: it doesn't understand the setup of the arms, possibly positions and relationships between motors etc. it hasn't seen my home and table environment and problem before Or both of those things. If I was able to get Pi0.5 working, should my expectation be the same? That it would simply run, but fail to respond. Or perhaps I'm doing something wrong, maybe there's a setup step I missed? Broader observations I was aware that of course that transformer models take a lot of processing power, but the impression I had from the various demos (tshirt folding, coffee making etc.) is that these robot arms were running autonomously, perhaps on their own hardware, or perhaps hooked up to a supporting machine. But my impression here is that they'd actually need to be hooked up to a REALLY BEEFY maxed out machine, in order to work. Another option I considered is running this on a remote machine, with a service like runpod. My instinct is this would introduce too much latency. I'm wondering how others are handling these issues, and what people would recommend? This then leads to bigger questions I'm more curious about: how humanoids like 1X and Optimus would be expected to work. With beefy GPUs and compute onboard, or perhaps operating from a local base station? Running inference remotely would surely have too much latency.

1h ago

---

**[We thought the design was locked. Then early testers asked for "Eyes". Now we are conflicted.](https://www.reddit.com/r/robotics/comments/1qkz4i6/we_thought_the_design_was_locked_then_early/)**

Quick update post-CES. We thought we had the hardware definition 99% done, but the feedback from our first batch of hands-on users is making us second-guess two major decisions. Need a sanity check from you guys before we commit to the final molds/firmware. **Dilemma 1: Vex (The Pet Bot) - Does it need "Eyes"?** Right now, Vex is a sleek, minimalist sphere. It looks like a piece of high-end audio gear or a giant moving camera lens. But the feedback we keep getting from pet owners is: _"It feels too much like a surveillance tool. Give it eyes so it feels like a companion."_ We are torn. * **Option A (Current):** Keep it clean. It's a robot, not a cartoon character. * **Option B (Change):** Add digital eye expressions (using the existing LED matrix or screen). My worry: Does adding fake digital eyes make it look "friendly", or does it just make it look like a cheap toy? Where is the line? **Dilemma 2: Aura (The AI) - Jarvis vs. Her** We originally tuned Aura's voice to sound crisp, futuristic, and efficient. Think TARS from Interstellar or Jarvis. We wanted it to feel "Smart". But users are telling us it feels cold. They are asking for more "human" imperfections—pauses, mood swings, maybe even sounding tired in the evening. We can re-train the TTS (Text-to-Speech) model, but I'm worried about the "Uncanny Valley". **Do you actually want your desktop robot to sound emotional, or do you just want it to give you the weather report quickly?** If you have a strong opinion on either, let me know. We are literally testing the "Emotional Voice" update in our internal build right now. _(As always, looking for more people to roast these decisions in our discord beta group. Let me know if you want an invite.)_

18h ago

---

**[The open-source Stack-chan project is getting an official hardware kit: What are your thoughts on (co-creative) desktop robotics?](https://www.reddit.com/r/robotics/comments/1qlkyof/the_opensource_stackchan_project_is_getting_an/)**

I've been following the Stack-chan project for a while: it's an open-source AI desktop robot originally developed by Shinya Ishikawa that runs on the M5Stack ecosystem. M5Stack just launched an official Kickstarter to make the hardware more accessible, and I'm curious to get this sub's take on the platform. Do you think open-source modular platforms like this are the future for hobbyist robotics, or is the (co-creation) model too fragmented for serious development?

57m ago

---

**[My new Quadruped project](https://www.reddit.com/r/robotics/comments/1qkj4u8/my_new_quadruped_project/)**

This is my new project 'DEFY'. I plan to make it into a 3D printer and I plan to use SLM metal printing and carbon fiber parts appropriately. (I'm a 19-year-old dropout and my dream is to work for a company even if it's an internship!) 😼👍

1d ago

---

---

## Google News: "robotics"

**[Introducing Rho-alpha, the new robotics model from Microsoft](https://www.microsoft.com/en-us/research/story/advancing-ai-for-the-physical-world/)**

Rho-alpha, which translates natural language commands into control signals for robotic systems doing bimanual manipulation tasks, aims to make physical systems more adaptable by using physical sensing modalities like touch and continuous learning from human feedback.

Microsoft • 2h ago

---

**[Inside the OpenAI lab where workers train robotic arms to fold laundry and toast bread](https://www.businessinsider.com/open-ai-robotics-lab-humanoid-robots-2026-1)**

OpenAI has rapidly scaled its robotics lab over the past year and plans to open up a second lab, insiders say.

Business Insider • 2d ago

---

**[Saga Robotics bets big on US vineyards with new GM, fresh capital](https://agfundernews.com/saga-robotics-bets-big-on-us-vineyards-with-new-gm-fresh-capital-for-uv-c-bots-chemical-free-winegrowing-is-the-holy-grail)**

During the 2025 California wine grape season, Saga Robotics increased treated acreage tenfold and expects to nearly triple it again in 2026.

AgFunderNews • 1d ago

---

**[Microsoft Research reveals Rho-alpha vision-language-action model for robots](https://www.therobotreport.com/microsoft-research-reveals-rho-alpha-vision-language-action-model-for-robots/)**

The Rho-alpha model incorporates sensor modalities such as tactile feedback and is trained with human guidance, says Microsoft.

The Robot Report • 2d ago

---

**[Nvidia's Jensen Huang says AI robotics is a 'once-in-a-generation' opportunity for Europe](https://www.cnbc.com/2026/01/21/nvidia-jensen-huang-robotics-opportunity-europe-.html)**

Europe's industrial base sets it up well to lead in the physical AI space, Huang told WEF

CNBC • 2d ago

---

**[Jim Cramer on Serve Robotics: “We’re Not Going to Go Into Robotics Other Than to Say That We Want Tesla”](https://finance.yahoo.com/news/jim-cramer-serve-robotics-not-145951419.html)**

Serve Robotics Inc. (NASDAQ:SERV) is one of the stocks on Jim Cramer’s radar. During the lightning round, a caller sought Cramer’s opinion of the company, and he replied: Okay, we’re not going to go into robotics other than to say that we want Tesla. I know Tesla’s done nothing. I heard that a hundred thousand […]

Yahoo Finance • 1d ago

---

**[Elon Musk, a fierce Davos critic, tells World Economic Forum that robots will outnumber humans](https://www.cbsnews.com/news/elon-musk-davos-world-economic-forum/)**

The billionaire CEO of Tesla and SpaceX, in his first appearance at Davos, said Tesla could start selling its Optimus robots next year.

CBS News • 1d ago

---

**[Elon Musk says Tesla will likely sell humanoid robots by end of next year](https://www.foxbusiness.com/economy/elon-musk-says-tesla-likely-sell-humanoid-robots-end-next-year)**

Elon Musk said Tesla's Optimus humanoid robots could be available for public purchase by the end of 2027, saying the robots should be reliable, safe and capable of a range of functions.

Fox Business • 1d ago

---

**[Elon Musk says humanoid robots will outnumber humans](https://finance.yahoo.com/video/elon-musk-says-humanoid-robots-173000912.html)**

Tesla (TSLA) CEO and SpaceX (SPAX.PVT) founder Elon Musk said at this year's World Economic Form (WEF) that humanoid robots will eventually outnumber humans. Robinhood chief investment officer Stephanie Guild, Yahoo Finance Senior Reporter Ines Ferré, and Yahoo Finance Senior Reporter Brooke DiPalma joins Opening Bid host Brian Sozzi to discuss Musk's bullish claims on robotics. Check out Musk's comments on humanoid robots and Tesla's robotaxi, and watch his full WEF interview. To watch more expert insights and analysis on the latest market action, check out more&nbsp;Opening Bid.

Yahoo Finance • 19h ago

---

**[Dr. Oz: AI and robots can already provide medical care](https://www.axios.com/2026/01/22/dr-oz-davos-ai-medical-health)**

Axios • 1d ago

---

---

## YouTube Videos: "robotics"

**[Xpeng’s New ET1 AI Robot Just Broke the AI  Humanoid Limit — Optimus Killer Enters Mass Production](https://www.youtube.com/watch?v=T8IYzqINZJY)**

XPENG Robotics just changed the game — their new ET1 AI humanoid robot has officially entered mass production, and it's ...

📺 The AI Nexus

👁️ 3K • 👍 101 • 💬 16 • ⏱️ 18:41 • 13h ago

---

**[Elon Musk: My prediction is that there will be more robots than people](https://www.youtube.com/watch?v=fqIfoLrOSbA)**

Elon Musk, CEO of Tesla, sits down with Larry Fink, chair and CEO at BlackRock, to discuss the future of robotics, the impact of ...

📺 CNBC Television

👁️ 8K • 👍 74 • 💬 53 • ⏱️ 2:47 • 1d ago

---

**[Tesla is ‘definitely in line’ for $500 stock price amid robot rise: R &#39;Ray&#39; Wang](https://www.youtube.com/watch?v=n7DFi-qXikk)**

Constellation Research founder R 'Ray' Wang joins 'Varney & Co.' to discuss the new U.S.-controlled TikTok entity and why he ...

📺 Fox Business Clips

👁️ 14K • 👍 219 • 💬 82 • ⏱️ 3:39 • 18h ago

---

**[Tesla is betting on robots &amp; robotaxis, but former bull Ross Gerber is skeptical](https://www.youtube.com/watch?v=fzuqnIGorNA)**

Gerber Kawasaki Wealth and Investment Management CEO, Ross Gerber, joins Market Domination host Josh Lipton to discuss ...

📺 Yahoo Finance

👁️ 2K • 👍 48 • 💬 12 • ⏱️ 6:39 • 7h ago

---

**[0% survival: Russian soldiers vs Ukrainian robots](https://www.youtube.com/watch?v=_BQ1xQ-o__M)**

Our interactive news map: https://www.rfunews.com/map Subscribe to unlock full access to the map + exclusive strategic ...

📺 RFU News — Strategic Geopolitics

👁️ 131K • 👍 14K • 💬 498 • ⏱️ 5:29 • 1d ago

---

**[Figure&#39;s New AI Robot Runs Like a Real Human... Figure 03’s secret “Fitness Program”](https://www.youtube.com/watch?v=G0xbD8Dwka0)**

Figure AI just broke the internet — their new Figure 03 humanoid robot is running like a real human, and the footage looks unreal.

📺 The AI Nexus

👁️ 8K • 👍 237 • 💬 21 • ⏱️ 19:35 • 5d ago

---

**[Robots Are Addicted to Getting Hit By Trains](https://www.youtube.com/watch?v=IHRo8i-qaeU)**

Starforge PC https://starforgepc.com/moist-yt Get Goof Juice and use code MOIST https://gamersupps.gg/moist Our soap ...

📺 penguinz0

👁️ 1.1M • 👍 48K • 💬 4K • ⏱️ 9:14 • 3d ago

---

**[&#39;ABUNDANCE FOR ALL&#39;: Musk says AI and robotics could play a key part around the world](https://www.youtube.com/watch?v=vBtKyfvR41E)**

Elon Musk says AI and robotics could play a key part in giving everyone around the world 'a very high standard of living,' but the ...

📺 Fox News

👁️ 45K • 👍 1K • 💬 230 • ⏱️ 0:49 • 1d ago

---

**[The question with AI and robotics is very simple](https://www.youtube.com/watch?v=Va_IEFdZCjo)**

📺 Bernie Sanders

👁️ 23K • 👍 2K • 💬 106 • ⏱️ 1:13 • 1d ago

---

**[Is this the “picks and shovels” for the robotics industry? #trendingshorts #ai #robotics #tech](https://www.youtube.com/watch?v=J-0cXdGwJ6w)**

Will this company be the “picks and shovels” of the robotics industry? Skild AI, a Pittsburgh-based startup founded in 2023 by ...

📺 Rowan Cheung

👁️ 5K • 👍 328 • 💬 2 • ⏱️ 1:13 • 16h ago

---

---

*Generated by PeekDeck - A glance is all you need*

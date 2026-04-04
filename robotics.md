---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-04T02:13:35.345994+00:00'
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

**Last Updated:** April 04, 2026 at 02:13 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Humanoid robots undergoing training](https://www.reddit.com/r/robotics/comments/1sbj504/humanoid_robots_undergoing_training/)**

9h ago

---

**[Simulation is a beautiful pain in RL](https://www.reddit.com/r/robotics/comments/1sbbj7n/simulation_is_a_beautiful_pain_in_rl/)**

Appreciate all the feedback and love on the recent videos, here's another clip of the dev process worth sharing. This one starts with an ugly moment, the right leg clips the edge and stumbles on a stair jump. Took a few days to track down the real issue. Turned out to be a mechanical transmission resistance in the hip joint, not a bug in the code. After the fix, clean landing. We're at around stable 30cm (~12")now. Sim does 40 or even higher, but 30 clears real stairs and that's what matters. (Getting to 30 in real life was harder than it sounds) Basic locomotion is getting solid, so next step: giving this little guy some eyes and ears, maybe. Legs first, then brains. sim2real is always humbling!

14h ago

---

**[Infrastructure for training general-purpose robot policies](https://www.reddit.com/r/robotics/comments/1sbi10l/infrastructure_for_training_generalpurpose_robot/)**

If human demonstration data proves to be the underlying factor that determines scaling laws in general-purpose robotics, the infrastructure that captures that data will determine how fast we get there. Despite all the research novelty in ChatGPT, its success at its core can be attributed to one foundational fact - the scaling law of transformers. Have transformers made their way into robotics and are we seeing similar scaling laws? The answer is yes. Recent studies showed task completion rates jumping from 30% to 70% when human demonstration data scaled from 1,000 to 20,000 hours — a log-linear trend that mirrors exactly what we saw in language and vision. Labs are racing to train generalist policies - a robot brain that can solve any task under any embodiment. But the library of physical interactions required to train these policies doesn’t exist yet. Solving this data bottleneck is one of the most important problems for the next few years. We’ve seen dozens of companies emerge in this space and noticed the same pattern repeat: every egocentric data company makes tradeoffs between quality, scale, and diversity. I have been working at FPV Labs on the principle that high-quality data is orders of magnitude more valuable than sheer volume. Self-driving cars collect thousands of hours per day, but only a small fraction is useful for training. Studies like RT-2 showed that as little as 1% of data improves task success by 25%. There’s clearly a power law in the downstream impact of data. We spent months obsessing over data quality - building our stack, discarding it, rebuilding it, and iterating until we found a formula that doesn’t compromise quality at scale and laying the infrastructure rails as we embark into this future. We are excited to be building what we think of is the infra layer for the internet archive of data for our robotic companions of the future. Happy to answer questions about our hardware, data methodology, or what we’ve learned so far. fpvlabs.ai

9h ago

---

**[RoboBaton mini and Raspberry Pi](https://www.reddit.com/r/robotics/comments/1sbdusb/robobaton_mini_and_raspberry_pi/)**

l find that RoboBaton mini is good to use. I was originally planning to use Intel's T265, but discovered it had been discontinued. I found RoboBaton Mini on myrobotproject's website. I successfully got it working with my Raspberry Pi. I will open-source the code on GitHub later. I hope everyone can connect with me to discuss and explore other use cases for the Mini.

12h ago

---

**[ROS News for the Week of March 31st, 2026](https://www.reddit.com/r/robotics/comments/1sbnizu/ros_news_for_the_week_of_march_31st_2026/)**

Read all of the ROS news on Open Robotics Discourse. Picture is the Innate.bot MARS robot. They're running a hackathon at YCombinator next Saturday.

6h ago

---

**[Suggestions for battery](https://www.reddit.com/r/robotics/comments/1sbh2tx/suggestions_for_battery/)**

i need y'all to give me suggestions for the battery part im having two 6v n20 600rpm motors and also the battery is connected to the buck which powers the esp32 the sensors are powered from the esp32 3.3v all the things are working perfectly just the prblm im facing is o hVe 7.4v lipo battery but its too big and bulky for this size and makes it heavier too so can you suggest some batteries (rechargeable) 7.4v thats smaller and compact in size to fit on the upper part (where my thumb is placed)

10h ago

---

**[Autonomous valet robot demonstrating precise self-parking in a real-world setting](https://www.reddit.com/r/robotics/comments/1san0l2/autonomous_valet_robot_demonstrating_precise/)**

1d ago

---

**[From Idea to Robot Brain - ML/NN Solutions That Work : prageeth_ma](https://www.reddit.com/r/robotics/comments/1sbprgy/from_idea_to_robot_brain_mlnn_solutions_that_work/)**

Most people think building a robot is about hardware. It’s not. The real problem is the brain. I’ve been spending time working on neural networks for robotics things like vision, movement control, and terrain understanding. Trying to make them actually usable in real systems, not just something that works in theory. Recently I put together a Fiverr gig around this. mainly to start getting real projects and push myself further. If you’re curious how I approach it, you can check it out here Fiverr username: prageeth_ma I’m still growing this, so even just clicking the link helps more than you think. If you're building something or even thinking about it, I’d honestly like to hear about it. #robotics #machinelearning #artificialintelligence #engineering #fiverr

5h ago

---

**[Generalist | Introducing GEN-1](https://www.reddit.com/r/robotics/comments/1saoiaj/generalist_introducing_gen1/)**

1d ago

---

**[building a desktop robot. turns out response timing and lip sync matter way more than the LLM itself for HRI.](https://www.reddit.com/r/robotics/comments/1sajyvt/building_a_desktop_robot_turns_out_response/)**

been working on this little desktop robot prototype called Kitto for a while now. honestly most of the hype right now is just cramming the biggest model possible into a plastic shell. but testing the interaction on this thing... if the timing is off it just feels like a glorified smart speaker. to make it actually feel 'alive' on a desk, the idle animations and the instant switch to a listening state carry like 90% of the weight. tbh we ended up spending way more time tuning the audio-to-viseme mapping for the face than we did tweaking the actual API prompts. current stack is just an esp32s3+esp32p4 (planning to migrate to a linux board soon so we can handle local processing and maybe hook into openclaw). the screen isnt playing pre-rendered video files btw. the mouth movements are code-driven in real-time by analyzing the audio stream. latency is still my biggest headache though. pinging the api, getting the TTS audio back, and triggering the animation states fast enough to not break the illusion is tough on this hardware. its getting there but still a lot of code to fix. definately not pitching this as finished hardware yet, mostly just looking for honest feedback on the HRI approach. curious how you guys are handling TTS latency in your own conversational builds right now?

1d ago

---

---

## Google News: "robotics"

**[Exclusive: Anvil Robotics Raises $5.5M to Build ‘Legos for Robots’ Platform For Physical AI Teams](https://news.crunchbase.com/robotics/physical-ai-custom-robot-builder-seed-funding-anvil/)**

Anvil Robotics, an eight-month-old startup that aims to be the “Legos for robots,” has raised $5.5 million in a seed funding round, it tells Crunchbase News exclusively.

Crunchbase News • 1d ago

---

**[The gig workers who are training humanoid robots at home](https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/)**

People in Nigeria and India are strapping iPhones onto their heads and recording themselves doing chores.

MIT Technology Review • 2d ago

---

**[Video Friday: Digit Learns to Dance—Virtually Overnight](https://spectrum.ieee.org/video-humanoid-dancing)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[Under the Skin of America’s Humanoid Robots: Chinese Technology](https://www.wsj.com/tech/under-the-skin-of-americas-humanoid-robots-chinese-technology-27dd4fdf?gaa_at=eafs&gaa_n=AWEtsqcFNRUZMsjKxcrhFDckX67ja1cR8tKNjE9nc-CTtHPcwdPx09I7ajYI&gaa_ts=69d0773c&gaa_sig=RTYjMkqm9ALlyHJ2NxKmwcosCNHT1eKNigyUs_37pIGR3QE3_cAcpq43LYoOlLZzFwzpx4kIAk_OU4iyWv5Vfg%3D%3D)**

WSJ • 23h ago

---

**[Chinese Robot Pioneer UBTech Offers $18 Million for AI Scientist](https://www.bloomberg.com/news/articles/2026-04-03/chinese-robot-pioneer-ubtech-offers-18-million-for-ai-scientist)**

Bloomberg.com • 21h ago

---

**[Think Robots Are Impressive Now? Just Wait Until They Have 6G](https://www.cnet.com/tech/computing/think-robots-are-impressive-now-just-wait-until-they-have-6g/)**

This next-generation network technology won't just make our phones faster; it'll unlock new capabilities in robots, turning them into all-sensing, always-learning fleets.

CNET • 16h ago

---

**[China’s smart factory employs over 100 humanoid robots as interns in automation push](https://interestingengineering.com/ai-robotics/china-ai-humanoid-robots-factory-internships)**

Humanoid robots begin factory training in China, learning real tasks and signaling a shift toward AI-driven industrial automation.

Interesting Engineering • 14h ago

---

**[AI startup trains Chinese humanoid robots in Japanese hospitality](https://asia.nikkei.com/business/technology/artificial-intelligence/ai-startup-trains-chinese-humanoid-robots-in-japanese-hospitality)**

Japan companies eye tech from China despite security risks due to lack of options

Nikkei Asia • 1d ago

---

**[Sanctuary AI’s robotic hand demonstrates zero-shot in-hand manipulation](https://www.therobotreport.com/sanctuary-ais-robotic-hand-demonstrates-zero-shot-in-hand-manipulation/)**

Sanctuary AI said the robotic hand and AI system achieves the target orientation 10 times in a row without dropping the cube.

The Robot Report • 1d ago

---

**[How Disney Imagineers are using AI and robotics to reshape the company’s theme parks](https://www.fastcompany.com/91519970/disney-imagineers-ai-and-robotics-paris-park)**

From robotic Olaf to reinforcement learning, the company is rethinking how its attractions come to life.

Fast Company • 16h ago

---

---

## YouTube Videos: "robotics"

**[Shawn Ryan Tests a Real Humanoid Robot](https://www.youtube.com/watch?v=HWq9cFhTvvQ)**

Shawn Ryan gets hands-on with a real humanoid robot powered entirely by AI. In this clip, we break down how this robot sees, ...

📺 Shawn Ryan Show

👁️ 814K • 👍 32K • 💬 5K • ⏱️ 8:48 • 2d ago

---

**[Xiaomi’s New AI Robot Hand Works Like a REAL Human… This Is INSANE](https://www.youtube.com/watch?v=Ubpk3tOl9gw)**

Xiaomi just dropped a robotic hand so realistic, it might fool you into thinking it's human — and that's just the START of what's ...

📺 The AI Nexus

👁️ 4K • 👍 179 • 💬 13 • ⏱️ 20:43 • 3d ago

---

**[Skyfood, the Robot as a Service 🤖#robotics #robot #furry #startup #engineering](https://www.youtube.com/watch?v=x14HZyTQ1z4)**

📺 Confusion & Mekhy

👁️ 743 • 👍 34 • 💬 19 • ⏱️ 2:03 • 4h ago

---

**[Samsung Introduces &quot;Galaxy BOT&quot; — A Humanoid Robot That Can Do Anything](https://www.youtube.com/watch?v=N3eRvZP6oVU)**

Samsung is drawing significant attention with its new concept known as “Galaxy BOT,” a humanoid robot designed to perform a ...

📺 Carros Show

👁️ 5K • 👍 146 • 💬 8 • ⏱️ 8:25 • 5d ago

---

**[I broke a robot in China](https://www.youtube.com/watch?v=7U3vjVfwChc)**

China is leading the world in humanoid robot shipments. Powered by artificial intelligence, these machines are setting new ...

📺 CGTN

👁️ 30K • 👍 265 • 💬 41 • ⏱️ 1:54 • 1d ago

---

**[Shawn Ryan SHOCKED—They’re Mass-Producing Human Robots… Like iPhones](https://www.youtube.com/watch?v=-mkpQrPb8d0)**

Shawn Ryan comes into direct contact with a humanoid robot and the CEO who wants to have every family own one.

📺 Aaron Page 

👁️ 40K • 👍 1K • 💬 394 • ⏱️ 13:41 • 1d ago

---

**[Fat Jinu Does the Robot Trend 🤯](https://www.youtube.com/watch?v=aXaOgdF9C7U)**

rumi #huntrix #kpop #kpopdemonhunters #shorts #celebrity #trend #makeup #mira #zoey #jinu Production Disclosure (Channel: ...

📺 Faces of Culture

👁️ 3.6M • 👍 9K • 💬 7 • ⏱️ 0:04 • 1d ago

---

**[Engineering the Experience – How Do Robots Work on a Cruise Ship?](https://www.youtube.com/watch?v=AezeHLJedYc)**

How do robots work on a cruise ship? In this episode of Engineering the Experience, Royal Caribbean explores the robotics and ...

📺 Royal Caribbean

👁️ 6K • 👍 175 • 💬 15 • ⏱️ 4:51 • 1d ago

---

**[Olaf Robot Freezes up at Disneyland Paris and Falls Over](https://www.youtube.com/watch?v=QjgAZcS2wFI)**

During a recent fan meet-and-greet at Disneyland Paris, Olaf the snowman froze up and took a tumble in front of shocked fans.

📺 TODAY

👁️ 10K • 👍 156 • 💬 24 • ⏱️ 1:20 • 1d ago

---

**[Joe Rogan Watches Soldier Test INSANE Robotic Legs 🤖🦿💥 #Shorts](https://www.youtube.com/watch?v=zbopLtVrukQ)**

Joe Rogan Watches Soldier Test INSANE Robotic Legs #Shorts This is the future of the battlefield. A soldier straps on ...

📺 Silent Sentry

👁️ 83K • 👍 1K • 💬 32 • ⏱️ 0:17 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*

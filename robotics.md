---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-04T11:37:23.505014+00:00'
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

**Last Updated:** April 04, 2026 at 11:37 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Humanoid robots undergoing training](https://www.reddit.com/r/robotics/comments/1sbj504/humanoid_robots_undergoing_training/)**

18h ago

---

**[I analyzed every public LeRobot dataset on HuggingFace. Almost half would fail training.](https://www.reddit.com/r/robotics/comments/1sc5a3g/i_analyzed_every_public_lerobot_dataset_on/)**

I analyzed every public LeRobot dataset on HuggingFace. Almost half would fail training. Got tired of burning GPU hours on data that looked fine but trained terribly. So I wrote something to check datasets before training — grades A through F based on dead joints, action divergence, episode consistency, etc. Ran it across 45+ public datasets. Some findings: 42% actually ready to train 35% have critical issues (dead servos, contradictory demos) Action divergence is the single biggest predictor of training failure Several high-download datasets have problems nobody's flagged 50 consistent demos reliably beats 200 sloppy ones The thing that surprised me most: datasets with high action divergence (demonstrator doing different things in the same state) fail even with Diffusion Policy. You basically need to filter to one strategy or the policy just averages them into mush. Anyone else checking their data quality before training, or just yolo-ing it?

1h ago

---

**[Simulation is a beautiful pain in RL](https://www.reddit.com/r/robotics/comments/1sbbj7n/simulation_is_a_beautiful_pain_in_rl/)**

Appreciate all the feedback and love on the recent videos, here's another clip of the dev process worth sharing. This one starts with an ugly moment, the right leg clips the edge and stumbles on a stair jump. Took a few days to track down the real issue. Turned out to be a mechanical transmission resistance in the hip joint, not a bug in the code. After the fix, clean landing. We're at around stable 30cm (~12")now. Sim does 40 or even higher, but 30 clears real stairs and that's what matters. (Getting to 30 in real life was harder than it sounds) Basic locomotion is getting solid, so next step: giving this little guy some eyes and ears, maybe. Legs first, then brains. sim2real is always humbling!

23h ago

---

**[Infrastructure for training general-purpose robot policies](https://www.reddit.com/r/robotics/comments/1sbi10l/infrastructure_for_training_generalpurpose_robot/)**

If human demonstration data proves to be the underlying factor that determines scaling laws in general-purpose robotics, the infrastructure that captures that data will determine how fast we get there. Despite all the research novelty in ChatGPT, its success at its core can be attributed to one foundational fact - the scaling law of transformers. Have transformers made their way into robotics and are we seeing similar scaling laws? The answer is yes. Recent studies showed task completion rates jumping from 30% to 70% when human demonstration data scaled from 1,000 to 20,000 hours — a log-linear trend that mirrors exactly what we saw in language and vision. Labs are racing to train generalist policies - a robot brain that can solve any task under any embodiment. But the library of physical interactions required to train these policies doesn’t exist yet. Solving this data bottleneck is one of the most important problems for the next few years. We’ve seen dozens of companies emerge in this space and noticed the same pattern repeat: every egocentric data company makes tradeoffs between quality, scale, and diversity. I have been working at FPV Labs on the principle that high-quality data is orders of magnitude more valuable than sheer volume. Self-driving cars collect thousands of hours per day, but only a small fraction is useful for training. Studies like RT-2 showed that as little as 1% of data improves task success by 25%. There’s clearly a power law in the downstream impact of data. We spent months obsessing over data quality - building our stack, discarding it, rebuilding it, and iterating until we found a formula that doesn’t compromise quality at scale and laying the infrastructure rails as we embark into this future. We are excited to be building what we think of is the infra layer for the internet archive of data for our robotic companions of the future. Happy to answer questions about our hardware, data methodology, or what we’ve learned so far. fpvlabs.ai

19h ago

---

**[RoboBaton mini and Raspberry Pi](https://www.reddit.com/r/robotics/comments/1sbdusb/robobaton_mini_and_raspberry_pi/)**

l find that RoboBaton mini is good to use. I was originally planning to use Intel's T265, but discovered it had been discontinued. I found RoboBaton Mini on myrobotproject's website. I successfully got it working with my Raspberry Pi. I will open-source the code on GitHub later. I hope everyone can connect with me to discuss and explore other use cases for the Mini.

21h ago

---

**[PeppyOS v0.6.0: Now with variants and flavors](https://www.reddit.com/r/robotics/comments/1sc0or9/peppyos_v060_now_with_variants_and_flavors/)**

Hey everyone, A few weeks ago I shared PeppyOS, a simpler alternative to ROS 2 that I've been building. The feedback was really helpful, and I've been heads-down since then working on one of the biggest feature of the framework: Variants and flavors (the ability to define a single communication interface for different pieces of code). The goal hasn't changed: someone new should be able to pick this up and have nodes communicating in about half an hour. I'd love to hear what you think, especially from people who tried it last time.

6h ago

---

**[ROS News for the Week of March 31st, 2026](https://www.reddit.com/r/robotics/comments/1sbnizu/ros_news_for_the_week_of_march_31st_2026/)**

Read all of the ROS news on Open Robotics Discourse. Picture is the Innate.bot MARS robot. They're running a hackathon at YCombinator next Saturday.

15h ago

---

**[Autonomous valet robot demonstrating precise self-parking in a real-world setting](https://www.reddit.com/r/robotics/comments/1san0l2/autonomous_valet_robot_demonstrating_precise/)**

1d ago

---

**[Suggestions for battery](https://www.reddit.com/r/robotics/comments/1sbh2tx/suggestions_for_battery/)**

i need y'all to give me suggestions for the battery part im having two 6v n20 600rpm motors and also the battery is connected to the buck which powers the esp32 the sensors are powered from the esp32 3.3v all the things are working perfectly just the prblm im facing is o hVe 7.4v lipo battery but its too big and bulky for this size and makes it heavier too so can you suggest some batteries (rechargeable) 7.4v thats smaller and compact in size to fit on the upper part (where my thumb is placed)

19h ago

---

**[Generalist | Introducing GEN-1](https://www.reddit.com/r/robotics/comments/1saoiaj/generalist_introducing_gen1/)**

1d ago

---

---

## Google News: "robotics"

**[Exclusive: Anvil Robotics Raises $5.5M to Build ‘Legos for Robots’ Platform For Physical AI Teams](https://news.crunchbase.com/robotics/physical-ai-custom-robot-builder-seed-funding-anvil/)**

Anvil Robotics, an eight-month-old startup that aims to be the “Legos for robots,” has raised $5.5 million in a seed funding round, it tells Crunchbase News exclusively.

news.crunchbase.com • 1d ago

---

**[Under the Skin of America’s Humanoid Robots: Chinese Technology](https://www.wsj.com/tech/under-the-skin-of-americas-humanoid-robots-chinese-technology-27dd4fdf?gaa_at=eafs&gaa_n=AWEtsqfrq7SPUzcoCMJgCkYyy8DgWPf6I5yz9xzrfM7MdemyFiorRU84AaKI&gaa_ts=69d0f279&gaa_sig=T7EpEDxOupP8rmUf8mqH79t47nDiZIhhO6IFCFnPgvuCu-3wIDZ9XfRMcDr9rpghVcV1_TPmujTcoAVVJx4aDw%3D%3D)**

WSJ • 1d ago

---

**[China’s smart factory employs over 100 humanoid robots as interns in automation push](https://interestingengineering.com/ai-robotics/china-ai-humanoid-robots-factory-internships)**

Humanoid robots begin factory training in China, learning real tasks and signaling a shift toward AI-driven industrial automation.

Interesting Engineering • 23h ago

---

**[Video Friday: Digit Learns to Dance—Virtually Overnight](https://spectrum.ieee.org/video-humanoid-dancing)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 2d ago

---

**[Week Wraps Aboard Station with Spacesuits, Eye Checks, Robotics, and More](https://www.nasa.gov/blogs/spacestation/2026/04/03/week-wraps-aboard-station-with-spacesuits-eye-checks-robotics-and-more/)**

Spacesuit work and eye checks wrapped up the week for the Expedition 74 crew aboard the International Space Station. The orbital residents also focused on robotics, cargo transfers, and science hardware maintenance at the end of the week.

NASA (.gov) • 14h ago

---

**[How Disney Imagineers are using AI and robotics to reshape the company’s theme parks](https://www.fastcompany.com/91519970/disney-imagineers-ai-and-robotics-paris-park)**

From robotic Olaf to reinforcement learning, the company is rethinking how its attractions come to life.

Fast Company • 1d ago

---

**[US scientists make air-powered muscles that help robots lift 100x their weight](https://interestingengineering.com/ai-robotics/artificial-muscles-robot-lift-more-weight)**

US researchers have built air-powered muscles that help robots lift 100 times their weight while staying lightweight and untethered.

Interesting Engineering • 15h ago

---

**[North Fork robotics team heads to world championship](https://suffolktimes.timesreview.com/2026/04/north-fork-robotics-team-heads-to-world-championship/)**

Team R.I.C.E. 870 will go back to the FIRST world championship for the seventh time after a victory at the L.I. regional competition in March.

The Suffolk Times • 1d ago

---

**[City of Fountains Regional Robotics Competition underway at Park Hill South](https://www.yahoo.com/news/articles/city-fountains-regional-robotics-competition-232256046.html)**

The City of Fountains Regional Robotics Competition kicked off Friday morning at Park Hill South High School.

Yahoo • 12h ago

---

**[Robots learn to ask humans for help](https://www.axios.com/2026/04/01/robots-delivery-serve-tmobile)**

Axios • 2d ago

---

---

## YouTube Videos: "robotics"

**[Xiaomi’s New AI Robot Hand Works Like a REAL Human… This Is INSANE](https://www.youtube.com/watch?v=Ubpk3tOl9gw)**

Xiaomi just dropped a robotic hand so realistic, it might fool you into thinking it's human — and that's just the START of what's ...

📺 The AI Nexus

👁️ 4K • 👍 177 • 💬 13 • ⏱️ 20:43 • 3d ago

---

**[I broke a robot in China](https://www.youtube.com/watch?v=7U3vjVfwChc)**

China is leading the world in humanoid robot shipments. Powered by artificial intelligence, these machines are setting new ...

📺 CGTN

👁️ 31K • 👍 272 • 💬 57 • ⏱️ 1:54 • 2d ago

---

**[Xiaomi Unveils &quot;Mi Bot&quot; - Robot Assistant That Can Sell Phones](https://www.youtube.com/watch?v=WgxEbw1i_PM)**

Xiaomi is attracting attention with a new concept known as “Mi Bot,” a robotic assistant designed to operate in retail environments ...

📺 Carros Show

👁️ 5K • 👍 98 • 💬 3 • ⏱️ 8:55 • 5d ago

---

**[Female Robots 🤖 Serving food now 😂](https://www.youtube.com/watch?v=AqxWV9ij4BY)**

📺 Mike Mizzle

👁️ 119K • 👍 4K • 💬 260 • ⏱️ 0:44 • 1d ago

---

**[Fat Jinu Does the Robot Trend 🤯](https://www.youtube.com/watch?v=aXaOgdF9C7U)**

rumi #huntrix #kpop #kpopdemonhunters #shorts #celebrity #trend #makeup #mira #zoey #jinu Production Disclosure (Channel: ...

📺 Faces of Culture

👁️ 4.2M • 👍 10K • 💬 8 • ⏱️ 0:04 • 2d ago

---

**[Shawn Ryan Tests a Real Humanoid Robot](https://www.youtube.com/watch?v=HWq9cFhTvvQ)**

Shawn Ryan gets hands-on with a real humanoid robot powered entirely by AI. In this clip, we break down how this robot sees, ...

📺 Shawn Ryan Show

👁️ 873K • 👍 33K • 💬 5K • ⏱️ 8:48 • 2d ago

---

**[Olaf Robot Freezes up at Disneyland Paris and Falls Over](https://www.youtube.com/watch?v=QjgAZcS2wFI)**

During a recent fan meet-and-greet at Disneyland Paris, Olaf the snowman froze up and took a tumble in front of shocked fans.

📺 TODAY

👁️ 12K • 👍 180 • 💬 28 • ⏱️ 1:20 • 1d ago

---

**[Shawn Ryan SHOCKED—They’re Mass-Producing Human Robots… Like iPhones](https://www.youtube.com/watch?v=-mkpQrPb8d0)**

Shawn Ryan comes into direct contact with a humanoid robot and the CEO who wants to have every family own one.

📺 Aaron Page 

👁️ 47K • 👍 2K • 💬 430 • ⏱️ 13:41 • 1d ago

---

**[War Robots Most Broken RAVANA Ever!](https://www.youtube.com/watch?v=t67ObSD1yp8)**

War Robots Gameplay: Ravana with Kroko - absolutely OP! My War Robots Creator Link: https://wr.my.games/manni - Code: ...

📺 Manni-Gaming

👁️ 12K • 👍 514 • 💬 78 • ⏱️ 22:06 • 1d ago

---

**[The Coolest Robot on the Planet 🤯](https://www.youtube.com/watch?v=t37TaaFsHDM)**

Join this channel to get access to perks: https://www.youtube.com/channel/UCkoujZQZatbqy4KGcgjpVxQ/join Support the Shawn ...

📺 Shawn Ryan Show

👁️ 942K • 👍 21K • 💬 2K • ⏱️ 0:44 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

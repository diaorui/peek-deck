---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-04T04:29:34.883845+00:00'
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

**Last Updated:** April 04, 2026 at 04:29 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Humanoid robots undergoing training](https://www.reddit.com/r/robotics/comments/1sbj504/humanoid_robots_undergoing_training/)**

11h ago

---

**[Simulation is a beautiful pain in RL](https://www.reddit.com/r/robotics/comments/1sbbj7n/simulation_is_a_beautiful_pain_in_rl/)**

Appreciate all the feedback and love on the recent videos, here's another clip of the dev process worth sharing. This one starts with an ugly moment, the right leg clips the edge and stumbles on a stair jump. Took a few days to track down the real issue. Turned out to be a mechanical transmission resistance in the hip joint, not a bug in the code. After the fix, clean landing. We're at around stable 30cm (~12")now. Sim does 40 or even higher, but 30 clears real stairs and that's what matters. (Getting to 30 in real life was harder than it sounds) Basic locomotion is getting solid, so next step: giving this little guy some eyes and ears, maybe. Legs first, then brains. sim2real is always humbling!

16h ago

---

**[Infrastructure for training general-purpose robot policies](https://www.reddit.com/r/robotics/comments/1sbi10l/infrastructure_for_training_generalpurpose_robot/)**

If human demonstration data proves to be the underlying factor that determines scaling laws in general-purpose robotics, the infrastructure that captures that data will determine how fast we get there. Despite all the research novelty in ChatGPT, its success at its core can be attributed to one foundational fact - the scaling law of transformers. Have transformers made their way into robotics and are we seeing similar scaling laws? The answer is yes. Recent studies showed task completion rates jumping from 30% to 70% when human demonstration data scaled from 1,000 to 20,000 hours — a log-linear trend that mirrors exactly what we saw in language and vision. Labs are racing to train generalist policies - a robot brain that can solve any task under any embodiment. But the library of physical interactions required to train these policies doesn’t exist yet. Solving this data bottleneck is one of the most important problems for the next few years. We’ve seen dozens of companies emerge in this space and noticed the same pattern repeat: every egocentric data company makes tradeoffs between quality, scale, and diversity. I have been working at FPV Labs on the principle that high-quality data is orders of magnitude more valuable than sheer volume. Self-driving cars collect thousands of hours per day, but only a small fraction is useful for training. Studies like RT-2 showed that as little as 1% of data improves task success by 25%. There’s clearly a power law in the downstream impact of data. We spent months obsessing over data quality - building our stack, discarding it, rebuilding it, and iterating until we found a formula that doesn’t compromise quality at scale and laying the infrastructure rails as we embark into this future. We are excited to be building what we think of is the infra layer for the internet archive of data for our robotic companions of the future. Happy to answer questions about our hardware, data methodology, or what we’ve learned so far. fpvlabs.ai

12h ago

---

**[RoboBaton mini and Raspberry Pi](https://www.reddit.com/r/robotics/comments/1sbdusb/robobaton_mini_and_raspberry_pi/)**

l find that RoboBaton mini is good to use. I was originally planning to use Intel's T265, but discovered it had been discontinued. I found RoboBaton Mini on myrobotproject's website. I successfully got it working with my Raspberry Pi. I will open-source the code on GitHub later. I hope everyone can connect with me to discuss and explore other use cases for the Mini.

14h ago

---

**[ROS News for the Week of March 31st, 2026](https://www.reddit.com/r/robotics/comments/1sbnizu/ros_news_for_the_week_of_march_31st_2026/)**

Read all of the ROS news on Open Robotics Discourse. Picture is the Innate.bot MARS robot. They're running a hackathon at YCombinator next Saturday.

8h ago

---

**[Suggestions for battery](https://www.reddit.com/r/robotics/comments/1sbh2tx/suggestions_for_battery/)**

i need y'all to give me suggestions for the battery part im having two 6v n20 600rpm motors and also the battery is connected to the buck which powers the esp32 the sensors are powered from the esp32 3.3v all the things are working perfectly just the prblm im facing is o hVe 7.4v lipo battery but its too big and bulky for this size and makes it heavier too so can you suggest some batteries (rechargeable) 7.4v thats smaller and compact in size to fit on the upper part (where my thumb is placed)

12h ago

---

**[Autonomous valet robot demonstrating precise self-parking in a real-world setting](https://www.reddit.com/r/robotics/comments/1san0l2/autonomous_valet_robot_demonstrating_precise/)**

1d ago

---

**[From Idea to Robot Brain - ML/NN Solutions That Work : prageeth_ma](https://www.reddit.com/r/robotics/comments/1sbprgy/from_idea_to_robot_brain_mlnn_solutions_that_work/)**

Most people think building a robot is about hardware. It’s not. The real problem is the brain. I’ve been spending time working on neural networks for robotics things like vision, movement control, and terrain understanding. Trying to make them actually usable in real systems, not just something that works in theory. Recently I put together a Fiverr gig around this. mainly to start getting real projects and push myself further. If you’re curious how I approach it, you can check it out here Fiverr username: prageeth_ma I’m still growing this, so even just clicking the link helps more than you think. If you're building something or even thinking about it, I’d honestly like to hear about it. #robotics #machinelearning #artificialintelligence #engineering #fiverr

7h ago

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

**[How Disney Imagineers are using AI and robotics to reshape the company’s theme parks](https://www.fastcompany.com/91519970/disney-imagineers-ai-and-robotics-paris-park)**

From robotic Olaf to reinforcement learning, the company is rethinking how its attractions come to life.

Fast Company • 18h ago

---

**[The gig workers who are training humanoid robots at home](https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/)**

People in Nigeria and India are strapping iPhones onto their heads and recording themselves doing chores.

MIT Technology Review • 2d ago

---

**[Under the Skin of America’s Humanoid Robots: Chinese Technology](https://www.wsj.com/tech/under-the-skin-of-americas-humanoid-robots-chinese-technology-27dd4fdf?gaa_at=eafs&gaa_n=AWEtsqdmkhiY7eQsY82B3o3Tj2SdssYFolMRq4ZGleLkNM6fwRenoGMnZzup&gaa_ts=69d0971b&gaa_sig=nF3jYlHFDlcAwVzC76XGqKbxCCrg5yERSsqHQowN3EVzD0aBZG0-Ssp-WK5VidpWJQS-I-r0uuhjtjTEHTV4rA%3D%3D)**

WSJ • 1d ago

---

**[Video Friday: Digit Learns to Dance—Virtually Overnight](https://spectrum.ieee.org/video-humanoid-dancing)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[Week Wraps Aboard Station with Spacesuits, Eye Checks, Robotics, and More](https://www.nasa.gov/blogs/spacestation/2026/04/03/week-wraps-aboard-station-with-spacesuits-eye-checks-robotics-and-more/)**

Spacesuit work and eye checks wrapped up the week for the Expedition 74 crew aboard the International Space Station. The orbital residents also focused on robotics, cargo transfers, and science hardware maintenance at the end of the week.

NASA (.gov) • 7h ago

---

**[NASA given demonstration of robotic space rock lab in Leicester](https://www.bbc.com/news/articles/c98mj46m2qvo)**

A laboratory has been developed which can safely store and analyse samples from space.

BBC • 22h ago

---

**[Air-powered artificial muscles could help robots lift 100 times their weight](https://techxplore.com/news/2026-04-air-powered-artificial-muscles-robots.html)**

Tech Xplore • 1d ago

---

**[North Fork robotics team heads to world championship](https://suffolktimes.timesreview.com/2026/04/north-fork-robotics-team-heads-to-world-championship/)**

Team R.I.C.E. 870 will go back to the FIRST world championship for the seventh time after a victory at the L.I. regional competition in March.

The Suffolk Times • 18h ago

---

**[City of Fountains Regional Robotics Competition underway at Park Hill South](https://www.yahoo.com/news/articles/city-fountains-regional-robotics-competition-232256046.html)**

The City of Fountains Regional Robotics Competition kicked off Friday morning at Park Hill South High School.

Yahoo • 5h ago

---

---

## YouTube Videos: "robotics"

**[Xiaomi’s New AI Robot Hand Works Like a REAL Human… This Is INSANE](https://www.youtube.com/watch?v=Ubpk3tOl9gw)**

Xiaomi just dropped a robotic hand so realistic, it might fool you into thinking it's human — and that's just the START of what's ...

📺 The AI Nexus

👁️ 4K • 👍 179 • 💬 13 • ⏱️ 20:43 • 3d ago

---

**[Shawn Ryan Tests a Real Humanoid Robot](https://www.youtube.com/watch?v=HWq9cFhTvvQ)**

Shawn Ryan gets hands-on with a real humanoid robot powered entirely by AI. In this clip, we break down how this robot sees, ...

📺 Shawn Ryan Show

👁️ 838K • 👍 32K • 💬 5K • ⏱️ 8:48 • 2d ago

---

**[I Tested a Robot Wheelchair… It Passed](https://www.youtube.com/watch?v=UU4L3c6ijdc)**

Saw an autonomous wheelchair at Mayo Clinic… so I stepped in front of it. It stopped instantly. Honestly… better reaction time ...

📺 Todd Swank

👁️ 839 • 👍 5 • ⏱️ 0:21 • 2h ago

---

**[Shawn Ryan SHOCKED—They’re Mass-Producing Human Robots… Like iPhones](https://www.youtube.com/watch?v=-mkpQrPb8d0)**

Shawn Ryan comes into direct contact with a humanoid robot and the CEO who wants to have every family own one.

📺 Aaron Page 

👁️ 42K • 👍 2K • 💬 410 • ⏱️ 13:41 • 1d ago

---

**[Skyfood, the Robot as a Service 🤖#robotics #robot #furry #startup #engineering](https://www.youtube.com/watch?v=x14HZyTQ1z4)**

📺 Confusion & Mekhy

👁️ 751 • 👍 35 • 💬 20 • ⏱️ 2:03 • 7h ago

---

**[Fat Jinu Does the Robot Trend 🤯](https://www.youtube.com/watch?v=aXaOgdF9C7U)**

rumi #huntrix #kpop #kpopdemonhunters #shorts #celebrity #trend #makeup #mira #zoey #jinu Production Disclosure (Channel: ...

📺 Faces of Culture

👁️ 3.7M • 👍 9K • 💬 7 • ⏱️ 0:04 • 2d ago

---

**[Olaf Robot Freezes up at Disneyland Paris and Falls Over](https://www.youtube.com/watch?v=QjgAZcS2wFI)**

During a recent fan meet-and-greet at Disneyland Paris, Olaf the snowman froze up and took a tumble in front of shocked fans.

📺 TODAY

👁️ 11K • 👍 160 • 💬 24 • ⏱️ 1:20 • 1d ago

---

**[welding robot#robot #industrial #welding #machines #automation](https://www.youtube.com/watch?v=2hTTd9-A5Jw)**

📺 zhulongfeng 6

👁️ 30K • 👍 133 • 💬 2 • ⏱️ 0:22 • 2d ago

---

**[Robotics in the MCU!](https://www.youtube.com/watch?v=F6ILTk4HsHc)**

All titles are now streaming on @disneyplus ▻ SUBSCRIBE to the channel to get notified when new Marvel videos are posted: ...

📺 Marvel Entertainment

👁️ 44K • 👍 3K • 💬 79 • ⏱️ 2:28 • 4d ago

---

**[Brett Adcock - Shawn Ryan’s First Interview with a Robot | SRS #292](https://www.youtube.com/watch?v=99pOdGEGu6s)**

Brett Adcock is a technology entrepreneur focused on building companies in robotics, artificial intelligence, and aerospace.

📺 Shawn Ryan Show

👁️ 499K • 👍 10K • 💬 3K • ⏱️ 2:57:09 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

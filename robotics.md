---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-03T17:04:16.115406+00:00'
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

**Last Updated:** April 03, 2026 at 17:04 UTC  
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

5h ago

---

**[RoboBaton mini and Raspberry Pi](https://www.reddit.com/r/robotics/comments/1sbdusb/robobaton_mini_and_raspberry_pi/)**

l find that RoboBaton mini is good to use. I was originally planning to use Intel's T265, but discovered it had been discontinued. I found RoboBaton Mini on myrobotproject's website. I successfully got it working with my Raspberry Pi. I will open-source the code on GitHub later. I hope everyone can connect with me to discuss and explore other use cases for the Mini.

3h ago

---

**[Infrastructure for training general-purpose robot policies](https://www.reddit.com/r/robotics/comments/1sbi10l/infrastructure_for_training_generalpurpose_robot/)**

If human demonstration data proves to be the underlying factor that determines scaling laws in general-purpose robotics, the infrastructure that captures that data will determine how fast we get there. Despite all the research novelty in ChatGPT, its success at its core can be attributed to one foundational fact - the scaling law of transformers. Have transformers made their way into robotics and are we seeing similar scaling laws? The answer is yes. Recent studies showed task completion rates jumping from 30% to 70% when human demonstration data scaled from 1,000 to 20,000 hours — a log-linear trend that mirrors exactly what we saw in language and vision. Labs are racing to train generalist policies - a robot brain that can solve any task under any embodiment. But the library of physical interactions required to train these policies doesn’t exist yet. Solving this data bottleneck is one of the most important problems for the next few years. We’ve seen dozens of companies emerge in this space and noticed the same pattern repeat: every egocentric data company makes tradeoffs between quality, scale, and diversity. I have been working at FPV Labs on the principle that high-quality data is orders of magnitude more valuable than sheer volume. Self-driving cars collect thousands of hours per day, but only a small fraction is useful for training. Studies like RT-2 showed that as little as 1% of data improves task success by 25%. There’s clearly a power law in the downstream impact of data. We spent months obsessing over data quality - building our stack, discarding it, rebuilding it, and iterating until we found a formula that doesn’t compromise quality at scale and laying the infrastructure rails as we embark into this future. We are excited to be building what we think of is the infra layer for the internet archive of data for our robotic companions of the future. Happy to answer questions about our hardware, data methodology, or what we’ve learned so far. fpvlabs.ai

47m ago

---

**[Autonomous valet robot demonstrating precise self-parking in a real-world setting](https://www.reddit.com/r/robotics/comments/1san0l2/autonomous_valet_robot_demonstrating_precise/)**

1d ago

---

**[Generalist | Introducing GEN-1](https://www.reddit.com/r/robotics/comments/1saoiaj/generalist_introducing_gen1/)**

23h ago

---

**[Suggestions for battery](https://www.reddit.com/r/robotics/comments/1sbh2tx/suggestions_for_battery/)**

i need y'all to give me suggestions for the battery part im having two 6v n20 600rpm motors and also the battery is connected to the buck which powers the esp32 the sensors are powered from the esp32 3.3v all the things are working perfectly just the prblm im facing is o hVe 7.4v lipo battery but its too big and bulky for this size and makes it heavier too so can you suggest some batteries (rechargeable) 7.4v thats smaller and compact in size to fit on the upper part (where my thumb is placed)

1h ago

---

**[Humanoid robots undergoing training](https://www.reddit.com/r/robotics/comments/1sbj504/humanoid_robots_undergoing_training/)**

6m ago

---

**[building a desktop robot. turns out response timing and lip sync matter way more than the LLM itself for HRI.](https://www.reddit.com/r/robotics/comments/1sajyvt/building_a_desktop_robot_turns_out_response/)**

been working on this little desktop robot prototype called Kitto for a while now. honestly most of the hype right now is just cramming the biggest model possible into a plastic shell. but testing the interaction on this thing... if the timing is off it just feels like a glorified smart speaker. to make it actually feel 'alive' on a desk, the idle animations and the instant switch to a listening state carry like 90% of the weight. tbh we ended up spending way more time tuning the audio-to-viseme mapping for the face than we did tweaking the actual API prompts. current stack is just an esp32s3+esp32p4 (planning to migrate to a linux board soon so we can handle local processing and maybe hook into openclaw). the screen isnt playing pre-rendered video files btw. the mouth movements are code-driven in real-time by analyzing the audio stream. latency is still my biggest headache though. pinging the api, getting the TTS audio back, and triggering the animation states fast enough to not break the illusion is tough on this hardware. its getting there but still a lot of code to fix. definately not pitching this as finished hardware yet, mostly just looking for honest feedback on the HRI approach. curious how you guys are handling TTS latency in your own conversational builds right now?

1d ago

---

**[Robotic welding recommendation](https://www.reddit.com/r/robotics/comments/1sbhlve/robotic_welding_recommendation/)**

It will be very helpful for me if you did the survey as this is my graduation project i need to know what does the market need to start the project and i only have 2 months left so please help with your recommendations

🔗 [Google Docs](https://forms.gle/4FJuhLhkqY8YZ8SKA) • 1h ago

---

**[Robotics short paper](https://www.reddit.com/r/robotics/comments/1sbh6ge/robotics_short_paper/)**

Hi everyone, I'm an undergraduate who conducted an independent robotics project, and I am planning on submitting a 4-page write-up of my work to a workshop or small conference. Upon looking online, I am not sure where to find conferences to submit to; is there any venue that has options to submit short papers, and would a workshop (such as at IROS) be an applicable place for something like this? Thanks

1h ago

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

**[Under the Skin of America’s Humanoid Robots: Chinese Technology](https://www.wsj.com/tech/under-the-skin-of-americas-humanoid-robots-chinese-technology-27dd4fdf?gaa_at=eafs&gaa_n=AWEtsqdNz08usScyqUXAI1MM9uo7IVnrX8N6BctLaFvqif9Wi3I4hpJzWthF&gaa_ts=69cff67b&gaa_sig=crjIgGqNLZu05zCoXhqz9V_Uytof4FwJSrl6vY-VJfgRu38LS9Jfg7wQvm_DJmOS9m2KC3AER54hfM-vGFDocA%3D%3D)**

WSJ • 14h ago

---

**[How Disney Imagineers are using AI and robotics to reshape the company’s theme parks](https://www.fastcompany.com/91519970/disney-imagineers-ai-and-robotics-paris-park)**

From robotic Olaf to reinforcement learning, the company is rethinking how its attractions come to life.

Fast Company • 1d ago

---

**[Station Crew Works Robotics, Research as Artemis II Launch Preps Continue](https://www.nasa.gov/blogs/general-blog/2026/04/01/station-crew-works-robotics-research-as-artemis-ii-launch-preps-continue/)**

Robotics training and human research were the primary duties for the Expedition 74 crew aboard the International Space Station on Wednesday. The orbital residents rounded out their shift with spacesuit work, cargo operations, and Earth observations.

NASA (.gov) • 1d ago

---

**[Wi-Fi That Can Withstand a Nuclear Reactor](https://spectrum.ieee.org/robotics-in-nuclear-industry)**

Six months in a nuclear reactor? This receiver chip can take it

IEEE Spectrum • 1d ago

---

**[Air-powered artificial muscles could help robots lift 100 times their weight](https://techxplore.com/news/2026-04-air-powered-artificial-muscles-robots.html)**

Tech Xplore • 1d ago

---

**[South Burlington robotics team gearing up to compete in high-level regional competition](https://www.mynbc5.com/article/south-burlington-robotics-high-level-competition/70927937)**

"It's just a nice opportunity to really connect with people who aren't in your state," said team co-captain Levi Duteau.

WPTZ • 55m ago

---

**[FedEx’s next AI leap to feature RFID, robotics](https://www.supplychaindive.com/news/fedex-ai-usage-rfid-robotics-network-2/816220/)**

The carrier is scaling its use of physical assets powered by AI to strengthen network reliability and improve connectivity with shippers, a FedEx executive said.

Supply Chain Dive • 2d ago

---

**[Hyundai Motor Unveils "Next Starts Now" Campaign, Set to Showcase Robotics at FIFA World Cup 2026™](https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-unveils-next-starts-now-campaign%252C-set-to-showcase-robotics-at-fifa-world-cup-2026%25E2%2584%25A2-0000001147)**

Hyundai Motor Unveils "Next Starts Now" Campaign, Set to Showcase Robotics at FIFA World Cup 2026™

Hyundai • 2d ago

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

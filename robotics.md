---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-24T20:06:15.249470+00:00'
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

**Last Updated:** May 24, 2026 at 20:06 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Update on my vibro-quad (vibration-based quadrupedal robot)](https://www.reddit.com/r/robotics/comments/1tmcj2h/update_on_my_vibroquad_vibrationbased_quadrupedal/)**

I've finally submitted my PhD thesis and have some time to work on my favourite robot build so far. I managed to implement omnidirectional motion and field-centric drive. It's not perfect yet (I switched from a 9-axis IMU to a 6-axis, and now drift is a real issue), but I definitely think this is a good proof of concept. Has anyone seen this approach before? Most vibration robots I've found are either single-direction bristlebots or differential swarm bots like Kilobots. I haven't found much on holonomic vibration drive. Curious if I'm reinventing the wheel.

6h ago

---

**[The "evil when it wakes up" robot got a voice and emotions. (video)](https://www.reddit.com/r/robotics/comments/1tmb7og/the_evil_when_it_wakes_up_robot_got_a_voice_and/)**

A few weeks ago I posted OLAF here — the open-source embodied AI agent that looked a bit evil when it woke up. (That was the upside of 4 months of melted components and 50+ PCBs I now use as coasters.) I said voice and the AI brain layer were next. That's what this is. OLAF talks now, and it expresses. And since "it looks evil" was basically the headline last time — I tried to make it cute this round. You can tell me if it worked. Quick reminder of what OLAF is: not a robot built to do tasks. An AI agent with a physical presence — something that thinks, responds and reacts in the real world. This update is about giving it presence you can actually feel. What's new (v1 expression system): 15 expressions, 3 intensity levels each Vocalizations — laughs, sighs, thinking sounds, so there's no dead silence while it processes Emotion is driven by tags the LLM emits, which the body renders on the face + movement How it's wired: Pi 5 + AI kit orchestrates everything (the brain from the last post) Voice loop: wake word → VAD → speech-to-text → LLM → text-to-speech, half-duplex, with an activity state machine (sleeping / waking / listening / thinking / speaking) Heavy AI in the cloud: GPT-OSS 120B on Groq, Cartesia for the voice The pipeline publishes typed expression events over DDS to the body, so brain and body stay decoupled Still raw (honest as always): The "hmm" filler lands a beat too late Head movements aren't synced to speech yet — next big one It still can't do tasks… but it's genuinely fun to talk to Still no case. Wires everywhere. Same as last time — Claude as a coding partner made the iteration speed stupid. Weeks into hours. Last post (the evil wake-up / coaster saga): https://www.reddit.com/r/robotics/comments/1rwvo2s/my_robot_looks_evil_when_it_wakes_up_4_months_of/ Brain + hardware: https://github.com/kamalkantsingh10/OLAF Voice agent: https://github.com/kamalkantsingh10/olaf_companion Full demo on YouTube (sound on): https://youtube.com/shorts/PHwZBDvPOgQ Repo's open — feedback or a star both welcome. Happy to answer anything — the build, the Pi setup, the voice pipeline, the brain/body DDS contract, latency, whatever. And be honest: cute now, or still a little evil?

7h ago

---

**[Cracked open an AMR on my day off.](https://www.reddit.com/r/robotics/comments/1tmkz8f/cracked_open_an_amr_on_my_day_off/)**

So this is how I spend my Sundays now. Picked up a fleet of AMRs and decided to reverse engineer it from the chassis up. Top’s off, I’m on the laptop sniffing what I can, and I’ve hit the point where the community brain trust would save me a few weekends. A few of these will end up on eBay in the coming weeks!

1h ago

---

**[Robot Dog Feet](https://www.reddit.com/r/robotics/comments/1tmj3rj/robot_dog_feet/)**

Hello, im currently building q robot dog similar to the MIT Mini Cheetah. However i cannot for the life of me find what kind of feet they used. Currently im using tpu spheres i 3d printed but getting a lot of slippage. Any reccomendations on the feet or what the actual Mini Cheetah used?

2h ago

---

**[Depth tracking on a ~25$ rover](https://www.reddit.com/r/robotics/comments/1tlnos3/depth_tracking_on_a_25_rover/)**

Hey everybody! My current research project is to build a swarm of affordable, 3d printed rovers that can navigate through a room and play a cooperative game. I have already looked at ArUco trackers for navigation but am now exploring Depth Anything V2. Basically I want to get the most out of the ~15$ ESP32 S3 Sense and just use the computer (with a decent graphics card) to handle the navigation part of things. The plan is now: ArUco markers around the room - global position and Orientation via solvePnP Depth View - for obstacle avoidance, maybe other rovers or people Rovers handle their own temperature and battery auto shut down Camera feeds streamed to PC via Wifi - all navigation logic runs there Some people on here recommend ROS2, and as I looked into it, it was quite overwhelming. Right now I am using a Python based Web Interface that I built. As a beginner I was curious to hear your thoughts, if this path forward could work or if I am moving towards a dead end :-X

1d ago

---

**[You helped me name my last robot, Arctos, and you didn't disappoint! Now I need your help naming this new AGV. I will use the comment with the most upvotes.](https://www.reddit.com/r/robotics/comments/1tlbohc/you_helped_me_name_my_last_robot_arctos_and_you/)**

Hey r/robotics, A while back, this community helped me choose the name "Arctos" for my 6-DOF robotic arm project, and it has been an incredible journey since then. Now, I’m back with a new build: a mobile manipulator base designed to carry the arm, and it needs an official name. As promised, I’ll name it after whichever community suggestion gets the most upvotes! The Specs: - Drivetrain: 4x NEMA 23 stepper motors with TMC2209 drivers - Chassis: 3D-printed modular structure reinforced with M8 threaded rods - Brain & Control: ESP32 handling low-level tasks, paired with a custom Android app - Software Ecosystem: Fully integrated into Arctos Studio. ( Will do ROS/Isaac sim integration) - Sensors: 4x ultrasonic sensors, LiDAR, and a depth camera - Scavenged Tech: Powered by reused cordless drill batteries, using an old smartphone for its IMU and RGB camera - The Goal: An ultra-accessible, heavy-duty AGV with a target build cost of ~$250 USD, capable of carrying a 25kg payload. What's Next: The physical chassis is assembled and moving. Next up is implementing full SLAM navigation, VLM (Vision-Language Model) task grounding for autonomous manipulation, and mounting the arm on top. Drop your best name ideas below! Let's see what you guys come up with this time.

1d ago

---

**[Thinking about building a planar maglev positioning stage as a project — what would you do with it?](https://www.reddit.com/r/robotics/comments/1tlzm4n/thinking_about_building_a_planar_maglev/)**

I'm planning to take on a build project: a planar magnetic levitation platform. Small scale to start — roughly 300mm stator tile, a floating puck with 6-DOF (XY translation, Z, rotation, tilt), aiming for ~10μm precision and 1m/s or so. Multiple pucks on the same surface eventually. A few things I know it can do: - Contactless positioning (no mechanical wear, no backlash) - Spin/tilt/vibrate the puck while it's hovering - Pass power and signals through the puck But before I go deep on the design, I'd love to hear what the robotics community thinks: - If this existed as a buildable/open platform, what would you use it for? - What capability would make it a "must try" vs just a cool demo? - What pitfalls should I be watching out for? I've got a demo video of a similar industrial system. (Not a company, not selling anything. Just a builder looking for input from people who think about motion control.) https://reddit.com/link/1tlzm4n/video/wl52d9tnzz2h1/player

17h ago

---

**[Robot arm](https://www.reddit.com/r/robotics/comments/1tlad5y/robot_arm/)**

1d ago

---

**[Building (mostly) 3d-printed robot arm](https://www.reddit.com/r/robotics/comments/1tlbljh/building_mostly_3dprinted_robot_arm/)**

1d ago

---

**[What is the biggest communication bottleneck between robot operators, system architects, and task‑level decision layers](https://www.reddit.com/r/robotics/comments/1tme5gj/what_is_the_biggest_communication_bottleneck/)**

I’m trying to understand where real‑world robotics teams lose the most clarity when a task moves from: > – the operator, > – to the system architect, > – to the robot’s perception/decision layer. > > In your experience, which communication layer breaks most often? > – task specification, > – environment representation, > – feedback loops, > – or translating “what the robot sees” into “what the robot should do”. > > If you could magically fix one bottleneck in your workflow, which one would it be — and why.

5h ago

---

---

## Google News: "robotics"

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 1d ago

---

**[Humanoid robots work nonstop in package test](https://www.foxnews.com/tech/humanoid-robots-work-nonstop-package-test)**

Figure AI claims its three humanoid robots completed over 24 hours of continuous autonomous package sorting without any human control in a warehouse test.

Fox News • 3h ago

---

**[China is deploying the first home cleaning humanoid robot butlers](https://www.fastcompany.com/91546673/china-is-deploying-the-first-home-cleaning-humanoid-robot-butlers)**

The SeeLight S1 may be the first commercial humanoid robot that will be deployed at homes to do all chores in the household.

Fast Company • 9h ago

---

**[China's Walker humanoid robot amazes with precise ballet performance](https://interestingengineering.com/ai-robotics/chinese-humanoid-robot-stuns-with-ballet)**

UBTECH demonstates its new Walker C1 robot performing Swan Lake ballet with humans, showing advanced humanoid control.

Interesting Engineering • 9h ago

---

**[Job training for robots: How China is getting machines ready to join the workforce](https://www.cnbc.com/2026/05/21/china-robots-humanoid-job-training.html)**

Tesla CEO Elon Musk said on the company's fourth-quarter earnings call that China is the biggest competition for humanoid robots.

CNBC • 2d ago

---

**[Southwest Bans Humanoid Robots After Viral Passenger Flights](https://www.techrepublic.com/article/news-southwest-bans-humanoid-robots-flights/)**

Southwest banned human-like and animal-like robots from cabins and checked baggage after viral flights raised concerns about lithium-ion battery safety.

TechRepublic • 2d ago

---

**[China puts humanoid robots through tea harvesting field trials](https://interestingengineering.com/ai-robotics/china-tests-humanoid-robots-in-tea-farms-before-the-2026-world-robot-games)**

China is testing humanoid robots in tea production as part of preparations for the 2026 World Humanoid Robot Games.

Interesting Engineering • 2d ago

---

**[Google, Japanese firm ship 1,000 robots in automation push](https://interestingengineering.com/ai-robotics/google-fanuc-physical-ai-industrial-robots)**

Google and FANUC partner to advance autonomous industrial robots for smarter factory automation systems.

Interesting Engineering • 1d ago

---

**[UK’s Humanoid partners with Bosch to mass-produce HMND robots for industries](https://interestingengineering.com/ai-robotics/uk-humanoid-bosch-industrial-robot)**

Humanoid partners Bosch to scale HMND humanoid robot production after successful 2026 proof of concept trials.

Interesting Engineering • 2d ago

---

**[China unveils first humanoid robot for household chores, ready as early as 2027](https://www.scmp.com/tech/article/3354371/commercial-humanoid-robots-china-may-soon-do-laundry-make-beds-care-elders)**

South China Morning Post • 3d ago

---

---

## YouTube Videos: "robotics"

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 6K • 👍 153 • 💬 28 • ⏱️ 18:21 • 18h ago

---

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 35K • 👍 450 • 💬 169 • ⏱️ 5:15 • 2d ago

---

**[T800 Terminator? Humanoid Robot GAME CHANGERS In 2026 ($40,000 AI ROBOT)](https://www.youtube.com/watch?v=3E3KyJsC8uE)**

The mass production era is officially here. As a brand new 10000-unit factory line fires up, we look at the biggest humanoid robot ...

📺 AI News

👁️ 7K • 👍 153 • 💬 34 • ⏱️ 8:02 • 1d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 143K • 👍 3K • 💬 112 • ⏱️ 22:41 • 4d ago

---

**[My Neighbor HATES my New Robot Lawn Mower 😅](https://www.youtube.com/watch?v=6cNXy5ckcV0)**

STOP paying hundreds of dollars a month for lawn mower services and SWITCH to the Sunseeker Elite X7 Gen2 robotic lawn ...

📺 Max Tech

👁️ 5K • 👍 106 • 💬 10 • ⏱️ 10:08 • 2d ago

---

**[MOVA LiDax Ultra 3000 - Is This the Best Robot Lawn Mower?](https://www.youtube.com/watch?v=JlCdMKebkeY)**

Testing the MOVA LiDax Ultra 3000 AWD over the past few weeks has been seriously impressive. The AWD system handled ...

📺 Steve DOES

👁️ 32K • 👍 327 • 💬 2 • ⏱️ 16:22 • 2d ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 33 • 💬 5 • ⏱️ 0:07 • 3d ago

---

**[Ranking The Wildest Country Robots #robots #viral #shorts](https://www.youtube.com/watch?v=cfdL_mK0qUg)**

In this video, we rank different robots inspired by countries like China, Australia, Russia, the USA, and the United Kingdom.

📺 The area

👁️ 106K • 👍 3K • 💬 155 • ⏱️ 0:50 • 5d ago

---

**[Would you let this humanoid robot into your home? 👀 #trendingshorts #tech #ai #robot](https://www.youtube.com/watch?v=iiUR4k6M0KM)**

1X Technologies, an OpenAI-backed startup founded in Norway and now based in Palo Alto, has opened a 58000 square foot ...

📺 Rowan Cheung

👁️ 479K • 👍 13K • 💬 798 • ⏱️ 1:34 • 6d ago

---

**[Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!](https://www.youtube.com/watch?v=faBkVCEEEHQ)**

Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry! Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!

📺 TESLA CAR WORLD

👁️ 28K • 👍 499 • 💬 54 • ⏱️ 15:32 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

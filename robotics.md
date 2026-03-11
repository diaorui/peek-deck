---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-11T13:03:17.017608+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** March 11, 2026 at 13:03 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[BDX Droids at Disneyland during the Season of the Force event](https://www.reddit.com/r/robotics/comments/1rq212v/bdx_droids_at_disneyland_during_the_season_of_the/)**

BDX Droids are small autonomous bipedic droids created by Walt Disney Imagineering for Disneyland theme parks. Inspiration for walking movements was taken from the waddle of a duck, creating a stable walk while still keeping the appearance fun, as with Star Wars droids.

20h ago

---

**[Building a navigation software that will only require a camera, a raspberry pi and a WiFi connection (DAY 1)](https://www.reddit.com/r/robotics/comments/1rqpnrb/building_a_navigation_software_that_will_only/)**

Hi guys, so I've been building robots for a while, some of you might have seen my other posts. And as I builder I realize building the hardware, and getting it to move, is usually just half the battle, making it autonomous and capable of reasoning where to go and how to navigate is a whole other ordeal. So I thought: Wouldn't it be cool if all you needed to give a robot (or drone) intelligent navigation was: a camera, a raspberry pi & WiFi. No expensive LiDAR, no expensive Jetson, no complicated setup. So I'm starting to build this crazy idea in public. For now I have achieved: > Simple navigation ability by combining a monocular depth estimation model with a VLM > Is controlling a unreal engine simulation to navigate. > Simulation running locally talking to AI models on the cloud via a simple API > Up next: reducing on the latency and improving navigation path estimation Just wanted to share this out there in case there's more people who would also like to see the robots they build be able to be autonomous in a more easy manner.

2h ago

---

**[Share a fantastic job](https://www.reddit.com/r/robotics/comments/1rq1e5q/share_a_fantastic_job/)**

Look at this interesting robotic grasping project, accomplished with the assistance of a 3D depth camera P050. It outputs highly accurate RGBD data.

20h ago

---

**[My Magnetic Guided AGV Demonstrator](https://www.reddit.com/r/robotics/comments/1rpydju/my_magnetic_guided_agv_demonstrator/)**

This video shows the AGV in action that follows a magnetic line, with markers along the track telling the robot which branch to take at forks, where to slow down and where to stop for charging. I realise that line following feels old-school in this age of laser guidance and humanoid robots. But, hey, it costs less, and is super accurate. On the right side are the ceiling view of the track, and of the supervisory PC screen. Every 200 ms the robot publishes battery voltage, operating state, and distance traveled. The robot position is reconstructed from encoder odometry and displayed by a small Python program (which still needs some optimization to make the motion smoother on screen). The robot controller communicates with the magnetic sensor and motor controller over CAN bus, while WiFi/MQTT is used for supervision and command. The navigation control loop runs every 10 ms locally. MQTT overhead has no impact on real-time execution. MQTT topics are custom for now, but I may migrate to VDA5050 in a future version. I also wrote a short architecture note describing the system and software structure. I'll be happy to share, if anyone is interested. Curious to hear any thoughts or suggestions.

22h ago

---

**[Lipo S3 charging + load for a project](https://www.reddit.com/r/robotics/comments/1rqmkpa/lipo_s3_charging_load_for_a_project/)**

Hi all, I am getting into the hobby and I build this cute robot which I currently running from usb-c cable going directly to the ESP32. I want to add batteries for it but I am looking for the best (and safe way) to go. Few things I want: Chargeable via USB-C Chargeable while powered on (I believe this may be a bit sketchy)\ I use lipo 3s (because I already have it and I may want more Vs in the future projects) I hope this drawing makes sense to you, but I want to clarify if it is a good plan? (Just to clarify 4 thinner wires are for balancing and thicker ones for the main load. I would use lipo 3s with XT30 connection). Thanks https://preview.redd.it/0no1gx2a5dog1.png?width=1504&format=png&auto=webp&s=a096d1ae4ace9ad7303706de897e116cf9b7b1de

6h ago

---

**[Watch humanoids play soccer. Upcoming Livestream for the RoboCup German Open 2026](https://www.reddit.com/r/robotics/comments/1rql7ph/watch_humanoids_play_soccer_upcoming_livestream/)**

Erlebt live spannende Wettbewerbe, innovative Robotik, packende Matches und faszinierende Technologien aus der Welt des RoboCup. Heute starten die Teams in d...

🔗 [YouTube](https://www.youtube.com/live/pQkf3MvBr2s?is=ABwodU_7hzekDwtO) • 7h ago

---

**[Figure's Helix 2 - Full Body Autonomy Video](https://www.reddit.com/r/robotics/comments/1rq45b6/figures_helix_2_full_body_autonomy_video/)**

19h ago

---

**[Reflex Robotics releases first episode of "At Your Service"](https://www.reddit.com/r/robotics/comments/1rpc547/reflex_robotics_releases_first_episode_of_at_your/)**

1d ago

---

**[Beware of DFR robot & US warehouse scam](https://www.reddit.com/r/robotics/comments/1rprmo5/beware_of_dfr_robot_us_warehouse_scam/)**

I recently bought a a lattepanda sigma 32gb almost $700 product from dfr robot. After it arrived dead on arrival I contacted them within 1 hour of delivery & they forwarded me to latte panda support team. They were able to verify the board is not functioning & requested dfr to issue a replacement. Here’s the kicker they want me to ship it back to china from the us on my own dime and only willing to cover $30 shipping fee. Keep in mind this would at the very least cost $70-100 to ship internationally to china as well as the time it would take for the process. I asked DFR robot why it couldn’t be shipped to their California location as I bought it from the US website & it was shipped within the US as well & costs. They stopped answering completely. Now I will have to contact my bank in the AM to help with the issue even though they initially blocked the transaction from happening( now I see why) to see what can be done. In the meantime I’m out of almost $700 for a useless piece of hardware. I’m just glad I didn’t go ahead and place the order for the rest of what I would’ve needed which would’ve been 30 boards total then I would definitely been fkd. posting this so anybody in the future thinking about buying from them & you happened to get a bad product. Don’t expect for them to honor their warranty nor return policy it’s a scam. So save your money. All this because I needed a 32GB device for a warehouse project smh

1d ago

---

**[Finally a robot that does more than a backflip. What are your thoughts?](https://www.reddit.com/r/robotics/comments/1rp7usf/finally_a_robot_that_does_more_than_a_backflip/)**

1d ago

---

---

## Google News: "robotics"

**[Nosh Robotics’ $1,500 robot chef doesn’t need any help with dinner](https://www.theverge.com/tech/892655/nosh-robotics-nosh-one-launch)**

This robo-chef can take over your meal prep.

The Verge • 15h ago

---

**[AI Robotics Startup Rhoda Valued at $1.7 Billion in New Funding](https://www.bloomberg.com/news/articles/2026-03-10/ai-robotics-startup-rhoda-valued-at-1-7-billion-in-new-funding)**

Bloomberg • 23h ago

---

**[Rhoda AI Exits Stealth with $450 Million Series A to Bring Robots Out of the Lab and Into the Real World](https://www.businesswire.com/news/home/20260310715139/en/Rhoda-AI-Exits-Stealth-with-%24450-Million-Series-A-to-Bring-Robots-Out-of-the-Lab-and-Into-the-Real-World)**

Rhoda AI today announced its public launch after 18 months in stealth, unveiling FutureVision, a new approach to robotic intelligence based on video-predicti...

Business Wire • 22h ago

---

**[Former Google AI Researcher Sets Up AI Robotics Startup in Tokyo](https://finance.yahoo.com/news/former-google-ai-researcher-sets-041500137.html)**

Integral AI Inc., a five-year-old company founded by former Google researchers Jad Tarifi and Nima Asgharbeygi, develops AI models geared for automated systems such as robots and self-driving cars.  The company has worked with auto parts maker Denso Corp. since 2021 to help teach industrial robots new skills by observing demonstrations.  The 15-person startup is holding initial discussions with Toyota Motor Corp., Sony Group Corp., Honda Motor Co., Nissan Motor Co. and Mitsui Chemicals Inc. to pitch them on how artificial intelligence can advance manufacturing processes.

Yahoo Finance • 2d ago

---

**[How Pokémon Go is giving delivery robots an inch-perfect view of the world](https://www.technologyreview.com/2026/03/10/1134099/how-pokemon-go-is-helping-robots-deliver-pizza-on-time/)**

Niantic's AI spinout is training a new world model using 30 billion images of urban landmarks crowdsourced from players.

MIT Technology Review • 23h ago

---

**[Humanoid Robots Exit Labs: Mapping the Technical Path to Embodied AI at AW 2026](https://www.eetimes.com/humanoid-robots-exit-labs-mapping-the-technical-path-to-embodied-ai-at-aw-2026/)**

The AW 2026 expo in Seoul highlights a pivotal shift as humanoid robots move from research labs to industrial applications.

EE Times • 12h ago

---

**[World's largest humanoid robot training center to launch in Germany](https://interestingengineering.com/ai-robotics/worlds-largest-humanoid-robot-training-center)**

Germany will unveil a huge robot gym where humanoids train with humans to learn everyday tasks and generate valuable AI training data.

Interesting Engineering • 17h ago

---

**[Qualcomm’s partnership with Neura Robotics is just the beginning](https://techcrunch.com/2026/03/09/qualcomms-partnership-with-neura-robotics-is-just-the-beginning/)**

Neura Robotics is going to build new robots on top of Qualcomm's new IQ10 processors that were released at CES.

TechCrunch • 1d ago

---

**[Factorial Drives Solid-State Battery Expansion to Drones and Robotics with IQT and Strategic Partners](https://www.businesswire.com/news/home/20260310039385/en/Factorial-Drives-Solid-State-Battery-Expansion-to-Drones-and-Robotics-with-IQT-and-Strategic-Partners)**

Factorial Energy secures strategic investment to accelerate expansion into high-growth markets, including drones and mobile robotics.

Business Wire • 1d ago

---

**[Nvidia and ABB launch partnership for AI-enabled autonomous robots](https://www.ft.com/content/c77d99a4-8d75-4f34-8a71-6b1361ebb9b9)**

Industrial robots that can be trained in virtual conditions are being trialled by Foxconn

Financial Times • 1d ago

---

---

## YouTube Videos: "robotics"

**[Shocking Light-Powered Robot Runs Without Batteries &amp; Cyborg Cockroach](https://www.youtube.com/watch?v=2_igeW1d8RA)**

Robotics just entered a very strange new phase. Scientists built a tiny robot that runs purely on light with no batteries, processors, ...

📺 AI Revolution

👁️ 26K • 👍 851 • 💬 62 • ⏱️ 14:35 • 6d ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=7I-KWkV0JUM)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN

👁️ 261K • 👍 3K • 💬 406 • ⏱️ 29:41 • 5d ago

---

**[China&#39;s Most Agile Robots in 2026 – They&#39;re Doing Things That Shouldn&#39;t Be Possible](https://www.youtube.com/watch?v=_z5NxUToeZU)**

China's humanoid robots just performed the world's first continuous parkour flips, 3-meter aerial flips, and a 7.5-rotation Airflare ...

📺 TechFrontierNow

👁️ 62K • 👍 400 • 💬 91 • ⏱️ 9:26 • 6d ago

---

**[New OpenClaw Robot Feels Shockingly Aware (Detonated Skynet)](https://www.youtube.com/watch?v=LBYiSAj10aA)**

OpenClaw just demonstrated a system that lets robots build a persistent memory of the real world. Instead of only navigating a ...

📺 AI Revolution

👁️ 63K • 👍 2K • 💬 97 • ⏱️ 14:51 • 2d ago

---

**[Buying AI Robots from TEMU... what could go wrong?](https://www.youtube.com/watch?v=6MEmlewaLPQ)**

Go check out these robots if you're interested, temu actually has a ton of them https://temu.to/k/py4i66elux1 Buy used tech from ...

📺 Smokin' Silicon

👁️ 40K • 👍 1K • 💬 108 • ⏱️ 10:52 • 3d ago

---

**[Non-Stop INSANE Robot Fighting Action: Round 2 of NHRL&#39;s 2026 Pro World Championship KO Show (March)](https://www.youtube.com/watch?v=7tQ5Gyr3SYE)**

Round 2 of the 2026 NHRL Pro World Championship kicks off NOW! PRIME TIME is here: https://youtube.com/live/-x5Fzq4Hig0 ...

📺 NHRL

👁️ 361K • 👍 503 • 💬 21 • ⏱️ 3:35:12 • 3d ago

---

**[This Humanoid Robot Can Clean Your Living Room by Itself | Helix 02 Demo](https://www.youtube.com/watch?v=W2kSX0jflvg)**

A powerful new humanoid robot system called Helix 02 is showing how artificial intelligence could soon transform everyday life.

📺 DPCcars

👁️ 10K • 👍 80 • 💬 22 • ⏱️ 3:48 • 1d ago

---

**[Inside the World’s Largest AI-Driven Brahman Bull Leather Factory | Robotic Jacket Production](https://www.youtube.com/watch?v=okP5YczyK7M)**

Discover the full high-tech transformation of Brahman bull leather into premium luxury jackets in this exclusive AI-driven factory ...

📺 NeoForge

👁️ 4K • 👍 8 • ⏱️ 11:42 • 20h ago

---

**[My Year Living with a Robot | Emily Kate Genatowski | TED](https://www.youtube.com/watch?v=rIg-Zt7bFHY)**

Imagine a robot moving into your home. How would it change your daily life? Historian Emily Kate Genatowski shares five ...

📺 TED

👁️ 23K • 👍 526 • 💬 53 • ⏱️ 13:51 • 4d ago

---

**[NEW Sniper Titan WAYMAKER Gameplay [War Robots]](https://www.youtube.com/watch?v=MzbhADGfBAI)**

War Robots Gameplay: NEW Sniper Titan WAYMAKER is coming to WR. Here's my new YouTube Channel @ManniRAID ...

📺 Manni-Gaming

👁️ 26K • 👍 1K • 💬 221 • ⏱️ 15:49 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

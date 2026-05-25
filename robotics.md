---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-25T12:36:03.385937+00:00'
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

**Last Updated:** May 25, 2026 at 12:36 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Stairs are hard — part 2](https://www.reddit.com/r/robotics/comments/1tmvczp/stairs_are_hard_part_2/)**

New hardware, outdoor steps this time. I push the stick forward, the robot detects the stairs and decides when to jump on its own. First part is daytime, clears all 3 steps, off the top, landed upright. Second part is at night: first attempt doesn't make it up, second one clears it. Added the night footage to show the controller input. Just push forward, everything else is the RL policy: stair detection, jump timing, balance, recovery. Big upgrade from last time where I was triggering every jump manually. Still working on making it more consistent.

10h ago

---

**[Need some help figuring out gait mechanics and servo torque](https://www.reddit.com/r/robotics/comments/1tmyamn/need_some_help_figuring_out_gait_mechanics_and/)**

As the title suggests, I'm struggling to figure out how to really program a proper gait for my quadrupedal robot; I've looked into tripod gaits and such, but does anyone have any advice for how to implement reinforcement learning or something similar? I'm considering attaching an IMU to the setup but I still don't know how to like get the legs to adapt and "figure it out themselves". I'm using an ESP32 as the main microcontroller with the arduino as just a sort of power source (will switch out in the future), and therefore I'm using the Arduino IDE for programming and haven't explored micropython My main problem is that I don't think my servos have enough torque to push the entire build off the ground, should I shorten the limbs or try other gaits first? Right now I'm hardcoding the servo positions and its been more like trial-and-error, if anyone has ANY advice or recommendations, I would really appreciate it. I'm aware that this post may be too vague, but pls feel free to dm me about the project.

8h ago

---

**[Update on my vibro-quad (vibration-based quadrupedal robot)](https://www.reddit.com/r/robotics/comments/1tmcj2h/update_on_my_vibroquad_vibrationbased_quadrupedal/)**

I've finally submitted my PhD thesis and have some time to work on my favourite robot build so far. I managed to implement omnidirectional motion and field-centric drive. It's not perfect yet (I switched from a 9-axis IMU to a 6-axis, and now drift is a real issue), but I definitely think this is a good proof of concept. Has anyone seen this approach before? Most vibration robots I've found are either single-direction bristlebots or differential swarm bots like Kilobots. I haven't found much on holonomic vibration drive. Curious if I'm reinventing the wheel.

22h ago

---

**[If you use NVIDIA Isaac Sim for reinforcement learning, do you use Isaac Lab with it? Just want to get a sense of what the status quo is.](https://www.reddit.com/r/robotics/comments/1tn1ged/if_you_use_nvidia_isaac_sim_for_reinforcement/)**

The reason for this query is that I am in the process of shifting to Isaac Sim / Isaac Lab since that is what seems to be in use nowadays. However, Isaac Lab is proving to be somewhat difficult to handle. While it handles the logging, and the creation of multi-actor systems for algorithms like PPO beautifully, its documentation leaves much to be desired. I am also concerned about the ease of setting up new robotic environments, actions, rewards, policies and possibly even custom algorithms. So, what is it that you do at your lab?

5h ago

---

**[new Nodding Mechanism is on robot now](https://www.reddit.com/r/robotics/comments/1tmxbff/new_nodding_mechanism_is_on_robot_now/)**

8h ago

---

**[People can no longer complain that unitree is not focusing on being useful ,they are starting to do figure things ofcourse still a little clumpsy Conference room mess cleanup test](https://www.reddit.com/r/robotics/comments/1tn1w3f/people_can_no_longer_complain_that_unitree_is_not/)**

So what do you make of this ,I read the title, it says "world model" and "VLA," so did they combine it ?It seems like a big deal. I feel like this is a big step. So what do you guys think ,I think I can finally say unitree has become a legitimate competitor to figure

🔗 [youtu.be](https://youtu.be/zqqIpVsMYkE?si=zFUFEpw4XYrZZKgo) • 5h ago

---

**[New RealSense SDK Beta Release!](https://www.reddit.com/r/robotics/comments/1tmp6ec/new_realsense_sdk_beta_release/)**

SDK Highlights - Partial-device-allowed is now the default — D400/D500 USB no longer silently drops degraded enumerations (configurable). - Jetson JP6 / 6.2.2 support added; fixes missing metadata over USB3 on JP6. - Bundled D400 firmware removed from the SDK package. - NEON acceleration: new BUILD_WITH_NEON flag; CUDA falls back to NEON; pointcloud correction. - MIPI driver version exposed via camera_info; new External Sync XU. Viewer - Non-blocking stop-stream, fixes for read-only options, Linux recording load, Win11 taskbar icon, MIPI FW update flow. DFU - Correct downgrade-counter opcode, flash-lock detection fix, skip reset on unsigned FW, d401_gmsl min FW → 5.17.2.2. Bug Fixes - Python deadlock, WMF reset crash, Ctrl+C re-entrancy, D435 initial enumeration, D555 DB3 playback, rs-dds-adapter Windows leak. --- MIPI Driver Highlights - JetPack 7 on NVIDIA Thor — new platform support (RSDSO-20559). - JetPack 5.1.6 and 6.2.2 added (RSDSO-21191, RSDSO-21146). - MAX96712 multi-camera: dual-camera per deserializer on JP6.x and quad-D457 via full-slave mode (RSDSO-20613). - External sync via TSC PWM (Thor-friendly), restored MAX9296 + consolidated MAX9295 GPIO tunneling (RSDSO-21407). - New carrier boards: Advantech (Orin, JP6/JP7) and AVerMedia (JP6.x). - Link tuning: MAX96712 lanes raised to 2500 Mbps; MFP6 added for links B–D. Stability - DS5 reset/detection rework, MAX9296 power_off underflow fix (spurious XCLR), JP6.x DTB deploy fix. --- D555 New Features - On-camera Object Detection (DamoYolo) — real-time bounding boxes/class/confidence published alongside streams; toggle via Color.option.Object_Detection_Enable. - UFO (UDP Fragmentation Offload) — higher throughput at high-res/fps; auto-enabled for standard MTU, disabled for jumbo frames. SafeDDS - More concurrent viewers per camera, better discovery, high-load stability, reliable notification delivery, stream-open timeout fix. ROS2 - Topic rename _CompressedColor → _Color/compressed; depth-unit in metadata; reduced topic overhead; CompressedColor auto-sync with RGB; better ROS2cli reliability. DFU - Real-time progress to host, pre-update integrity check, improved transfer reliability. Bug Fixes - Stream open timeout (RSDEV-6686), message drops under load (RSDEV-6314), network stall (RSDEV-6955), camera_info resolution mismatch (RSDEV-6683), ROS2 param/node CLI issues, 4-stream stability (RSDEV-7109). More info: https://github.com/realsenseai/librealsense/releases/tag/v2.58.1

14h ago

---

**[Meet LimX Luna—Our Next-Gen Full-Size Interactive Humanoid Robot. Are they legitimate competitor?](https://www.reddit.com/r/robotics/comments/1tn3079/meet_limx_lunaour_nextgen_fullsize_interactive/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/-lgo5xqgVko?si=M1M-LnBZNLJIgs7R) • 4h ago

---

**[Cracked open an AMR on my day off.](https://www.reddit.com/r/robotics/comments/1tmkz8f/cracked_open_an_amr_on_my_day_off/)**

So this is how I spend my Sundays now. Picked up a fleet of AMRs and decided to reverse engineer it from the chassis up. Top’s off, I’m on the laptop sniffing what I can, and I’ve hit the point where the community brain trust would save me a few weekends. A few of these will end up on eBay in the coming weeks!

17h ago

---

**[Robot Dog Feet](https://www.reddit.com/r/robotics/comments/1tmj3rj/robot_dog_feet/)**

Hello, im currently building q robot dog similar to the MIT Mini Cheetah. However i cannot for the life of me find what kind of feet they used. Currently im using tpu spheres i 3d printed but getting a lot of slippage. Any reccomendations on the feet or what the actual Mini Cheetah used?

18h ago

---

---

## Google News: "robotics"

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 2d ago

---

**[Humanoid robots work nonstop in package test](https://www.foxnews.com/tech/humanoid-robots-work-nonstop-package-test)**

Figure AI claims its three humanoid robots completed over 24 hours of continuous autonomous package sorting without any human control in a warehouse test.

Fox News • 20h ago

---

**[China is deploying the first home cleaning humanoid robot butlers](https://www.fastcompany.com/91546673/china-is-deploying-the-first-home-cleaning-humanoid-robot-butlers)**

The SeeLight S1 may be the first commercial humanoid robot that will be deployed at homes to do all chores in the household.

Fast Company • 1d ago

---

**[Amazon celebrates opening of Virginia Beach robotics facility](https://www.pilotonline.com/2026/05/24/amazon-robotics-facility-virginia-beach/)**

It’s Amazon’s third robotics fulfillment center in Virginia.

The Virginian-Pilot • 22h ago

---

**[Tesla Model S Sparked Elon Musk's AI, Robotics And Space Revolution: 'Little Did We Know,' Says Cathie Wood](https://finance.yahoo.com/sectors/technology/articles/tesla-model-sparked-elon-musks-113132838.html)**

Investor Cathie Wood of ARK Invest has hailed the Tesla Inc. Model S following its sunset for kicking off a “revolution” led by Elon Musk in the artificial intelligence, outer space exploration and robotics sectors. Little Did We Know Wood,...

Yahoo Finance • 1d ago

---

**[Q&A: How video helps build robot brains for physical AI](https://www.computerworld.com/article/4175902/qa-how-video-helps-build-robot-brains-for-physical-ai.html)**

Though many companies use YouTube videos for training, Kate Shen, the co-founder of startup Anaxi Labs, is looking in a different direction.

Computerworld • 1h ago

---

**[Ukraine’s Ground Robots Are Becoming Battlefield Platforms—And Procurement Is About to Surge](https://united24media.com/world/ukraines-ground-robots-are-becoming-battlefield-platforms-and-procurement-is-about-to-surge-19106)**

Ukraine plans UGV procurement Ukraine 2026 to double in 2026, reaching nearly 25,000 units, adding EW, radar, missiles and mortars to combat roles.

UNITED24 Media • 1d ago

---

**[New framework helps robots turn complex language into precise 3D actions](https://techxplore.com/news/2026-05-framework-robots-complex-language-precise.html)**

Tech Xplore • 2d ago

---

**[Metro Detroit students gain access to new $5M AI, robotics learning hub](https://www.mlive.com/news/detroit/2026/05/metro-detroit-students-gain-access-to-new-5m-ai-robotics-learning-hub.html)**

MLive.com • 1d ago

---

**[The Next AI Revolution Isn’t Chatbots. It’s Robotics](https://www.inc.com/heather-wilde/the-next-ai-revolution-isnt-chatbots-its-robotics/91344941)**

AI world models are transforming robotics by enabling robots to learn, adapt, and interact with real-world environments more intelligently.

inc.com • 1d ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 56K • 👍 619 • 💬 251 • ⏱️ 5:15 • 2d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 154K • 👍 3K • 💬 122 • ⏱️ 22:41 • 5d ago

---

**[MOVA LiDax Ultra 3000 - Is This the Best Robot Lawn Mower?](https://www.youtube.com/watch?v=JlCdMKebkeY)**

Testing the MOVA LiDax Ultra 3000 AWD over the past few weeks has been seriously impressive. The AWD system handled ...

📺 Steve DOES

👁️ 48K • 👍 496 • 💬 4 • ⏱️ 16:22 • 2d ago

---

**[Robot Vacuum Running! iRobot Edition #3](https://www.youtube.com/watch?v=DqsxWPWhIrI)**

📺 Planet Roomba

👁️ 3K • ⏱️ 14:27 • 22h ago

---

**[NEW LUMIN Laser Guns Fire around the Corner [War Robots]](https://www.youtube.com/watch?v=Btn2F-Cl8vQ)**

War Robots Gameplay: NEW LUMIN Laser Guns fire around the corner - WR My War Robots Creator Link: ...

📺 Manni-Gaming

👁️ 10K • 👍 489 • 💬 141 • ⏱️ 16:48 • 1d ago

---

**[Atlas Robot Is Stronger Than People Expected](https://www.youtube.com/watch?v=tShZ4bBhMTo)**

Boston Dynamics just revealed one of the craziest Atlas robot demonstrations yet. The humanoid robot is now capable of lifting ...

📺 DPCcars

👁️ 31K • 👍 220 • 💬 62 • ⏱️ 3:26 • 6d ago

---

**[Ranking The Wildest Country Robots #robots #viral #shorts](https://www.youtube.com/watch?v=cfdL_mK0qUg)**

In this video, we rank different robots inspired by countries like China, Australia, Russia, the USA, and the United Kingdom.

📺 The area

👁️ 122K • 👍 4K • 💬 169 • ⏱️ 0:50 • 5d ago

---

**[Would you let this humanoid robot into your home? 👀 #trendingshorts #tech #ai #robot](https://www.youtube.com/watch?v=iiUR4k6M0KM)**

1X Technologies, an OpenAI-backed startup founded in Norway and now based in Palo Alto, has opened a 58000 square foot ...

📺 Rowan Cheung

👁️ 511K • 👍 14K • 💬 866 • ⏱️ 1:34 • 6d ago

---

**[Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!](https://www.youtube.com/watch?v=faBkVCEEEHQ)**

Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry! Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!

📺 TESLA CAR WORLD

👁️ 29K • 👍 511 • 💬 55 • ⏱️ 15:32 • 5d ago

---

**[FINALLY BETTER MATCHMAKING? NEW TORTUGA&#39;S STANDOFF GAMEMODE? (War Robots)](https://www.youtube.com/watch?v=4GdaSGRiHQ4)**

In this video I tested out the newest gamemode. https://wr.my.games/Wolfblood7.

📺 Wolfblood7

👁️ 3K • 👍 139 • 💬 28 • ⏱️ 14:02 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

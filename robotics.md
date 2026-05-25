---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-25T00:00:13.739460+00:00'
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

**Last Updated:** May 25, 2026 at 00:00 UTC  
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

10h ago

---

**[New RealSense SDK Beta Release!](https://www.reddit.com/r/robotics/comments/1tmp6ec/new_realsense_sdk_beta_release/)**

SDK Highlights - Partial-device-allowed is now the default — D400/D500 USB no longer silently drops degraded enumerations (configurable). - Jetson JP6 / 6.2.2 support added; fixes missing metadata over USB3 on JP6. - Bundled D400 firmware removed from the SDK package. - NEON acceleration: new BUILD_WITH_NEON flag; CUDA falls back to NEON; pointcloud correction. - MIPI driver version exposed via camera_info; new External Sync XU. Viewer - Non-blocking stop-stream, fixes for read-only options, Linux recording load, Win11 taskbar icon, MIPI FW update flow. DFU - Correct downgrade-counter opcode, flash-lock detection fix, skip reset on unsigned FW, d401_gmsl min FW → 5.17.2.2. Bug Fixes - Python deadlock, WMF reset crash, Ctrl+C re-entrancy, D435 initial enumeration, D555 DB3 playback, rs-dds-adapter Windows leak. --- MIPI Driver Highlights - JetPack 7 on NVIDIA Thor — new platform support (RSDSO-20559). - JetPack 5.1.6 and 6.2.2 added (RSDSO-21191, RSDSO-21146). - MAX96712 multi-camera: dual-camera per deserializer on JP6.x and quad-D457 via full-slave mode (RSDSO-20613). - External sync via TSC PWM (Thor-friendly), restored MAX9296 + consolidated MAX9295 GPIO tunneling (RSDSO-21407). - New carrier boards: Advantech (Orin, JP6/JP7) and AVerMedia (JP6.x). - Link tuning: MAX96712 lanes raised to 2500 Mbps; MFP6 added for links B–D. Stability - DS5 reset/detection rework, MAX9296 power_off underflow fix (spurious XCLR), JP6.x DTB deploy fix. --- D555 New Features - On-camera Object Detection (DamoYolo) — real-time bounding boxes/class/confidence published alongside streams; toggle via Color.option.Object_Detection_Enable. - UFO (UDP Fragmentation Offload) — higher throughput at high-res/fps; auto-enabled for standard MTU, disabled for jumbo frames. SafeDDS - More concurrent viewers per camera, better discovery, high-load stability, reliable notification delivery, stream-open timeout fix. ROS2 - Topic rename _CompressedColor → _Color/compressed; depth-unit in metadata; reduced topic overhead; CompressedColor auto-sync with RGB; better ROS2cli reliability. DFU - Real-time progress to host, pre-update integrity check, improved transfer reliability. Bug Fixes - Stream open timeout (RSDEV-6686), message drops under load (RSDEV-6314), network stall (RSDEV-6955), camera_info resolution mismatch (RSDEV-6683), ROS2 param/node CLI issues, 4-stream stability (RSDEV-7109). More info: https://github.com/realsenseai/librealsense/releases/tag/v2.58.1

2h ago

---

**[Robot Dog Feet](https://www.reddit.com/r/robotics/comments/1tmj3rj/robot_dog_feet/)**

Hello, im currently building q robot dog similar to the MIT Mini Cheetah. However i cannot for the life of me find what kind of feet they used. Currently im using tpu spheres i 3d printed but getting a lot of slippage. Any reccomendations on the feet or what the actual Mini Cheetah used?

6h ago

---

**[Cracked open an AMR on my day off.](https://www.reddit.com/r/robotics/comments/1tmkz8f/cracked_open_an_amr_on_my_day_off/)**

So this is how I spend my Sundays now. Picked up a fleet of AMRs and decided to reverse engineer it from the chassis up. Top’s off, I’m on the laptop sniffing what I can, and I’ve hit the point where the community brain trust would save me a few weekends. A few of these will end up on eBay in the coming weeks!

5h ago

---

**[Depth tracking on a ~25$ rover](https://www.reddit.com/r/robotics/comments/1tlnos3/depth_tracking_on_a_25_rover/)**

Hey everybody! My current research project is to build a swarm of affordable, 3d printed rovers that can navigate through a room and play a cooperative game. I have already looked at ArUco trackers for navigation but am now exploring Depth Anything V2. Basically I want to get the most out of the ~15$ ESP32 S3 Sense and just use the computer (with a decent graphics card) to handle the navigation part of things. The plan is now: ArUco markers around the room - global position and Orientation via solvePnP Depth View - for obstacle avoidance, maybe other rovers or people Rovers handle their own temperature and battery auto shut down Camera feeds streamed to PC via Wifi - all navigation logic runs there Some people on here recommend ROS2, and as I looked into it, it was quite overwhelming. Right now I am using a Python based Web Interface that I built. As a beginner I was curious to hear your thoughts, if this path forward could work or if I am moving towards a dead end :-X

1d ago

---

**[You helped me name my last robot, Arctos, and you didn't disappoint! Now I need your help naming this new AGV. I will use the comment with the most upvotes.](https://www.reddit.com/r/robotics/comments/1tlbohc/you_helped_me_name_my_last_robot_arctos_and_you/)**

Hey r/robotics, A while back, this community helped me choose the name "Arctos" for my 6-DOF robotic arm project, and it has been an incredible journey since then. Now, I’m back with a new build: a mobile manipulator base designed to carry the arm, and it needs an official name. As promised, I’ll name it after whichever community suggestion gets the most upvotes! The Specs: - Drivetrain: 4x NEMA 23 stepper motors with TMC2209 drivers - Chassis: 3D-printed modular structure reinforced with M8 threaded rods - Brain & Control: ESP32 handling low-level tasks, paired with a custom Android app - Software Ecosystem: Fully integrated into Arctos Studio. ( Will do ROS/Isaac sim integration) - Sensors: 4x ultrasonic sensors, LiDAR, and a depth camera - Scavenged Tech: Powered by reused cordless drill batteries, using an old smartphone for its IMU and RGB camera - The Goal: An ultra-accessible, heavy-duty AGV with a target build cost of ~$250 USD, capable of carrying a 25kg payload. What's Next: The physical chassis is assembled and moving. Next up is implementing full SLAM navigation, VLM (Vision-Language Model) task grounding for autonomous manipulation, and mounting the arm on top. Drop your best name ideas below! Let's see what you guys come up with this time.

1d ago

---

**[Robot arm](https://www.reddit.com/r/robotics/comments/1tlad5y/robot_arm/)**

1d ago

---

**[Thinking about building a planar maglev positioning stage as a project — what would you do with it?](https://www.reddit.com/r/robotics/comments/1tlzm4n/thinking_about_building_a_planar_maglev/)**

I'm planning to take on a build project: a planar magnetic levitation platform. Small scale to start — roughly 300mm stator tile, a floating puck with 6-DOF (XY translation, Z, rotation, tilt), aiming for ~10μm precision and 1m/s or so. Multiple pucks on the same surface eventually. A few things I know it can do: - Contactless positioning (no mechanical wear, no backlash) - Spin/tilt/vibrate the puck while it's hovering - Pass power and signals through the puck But before I go deep on the design, I'd love to hear what the robotics community thinks: - If this existed as a buildable/open platform, what would you use it for? - What capability would make it a "must try" vs just a cool demo? - What pitfalls should I be watching out for? I've got a demo video of a similar industrial system. (Not a company, not selling anything. Just a builder looking for input from people who think about motion control.) https://reddit.com/link/1tlzm4n/video/wl52d9tnzz2h1/player

21h ago

---

**[Building (mostly) 3d-printed robot arm](https://www.reddit.com/r/robotics/comments/1tlbljh/building_mostly_3dprinted_robot_arm/)**

1d ago

---

**[What is the biggest communication bottleneck between robot operators, system architects, and task‑level decision layers](https://www.reddit.com/r/robotics/comments/1tme5gj/what_is_the_biggest_communication_bottleneck/)**

I’m trying to understand where real‑world robotics teams lose the most clarity when a task moves from: > – the operator, > – to the system architect, > – to the robot’s perception/decision layer. > > In your experience, which communication layer breaks most often? > – task specification, > – environment representation, > – feedback loops, > – or translating “what the robot sees” into “what the robot should do”. > > If you could magically fix one bottleneck in your workflow, which one would it be — and why.

9h ago

---

---

## Google News: "robotics"

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 1d ago

---

**[Humanoid robots work nonstop in package test](https://www.foxnews.com/tech/humanoid-robots-work-nonstop-package-test)**

Figure AI claims its three humanoid robots completed over 24 hours of continuous autonomous package sorting without any human control in a warehouse test.

Fox News • 7h ago

---

**[China is deploying the first home cleaning humanoid robot butlers](https://www.fastcompany.com/91546673/china-is-deploying-the-first-home-cleaning-humanoid-robot-butlers)**

The SeeLight S1 may be the first commercial humanoid robot that will be deployed at homes to do all chores in the household.

Fast Company • 13h ago

---

**[China's Walker humanoid robot amazes with precise ballet performance](https://interestingengineering.com/ai-robotics/chinese-humanoid-robot-stuns-with-ballet)**

UBTECH demonstates its new Walker C1 robot performing Swan Lake ballet with humans, showing advanced humanoid control.

Interesting Engineering • 12h ago

---

**[Robots Expand Presence in Daily Life and Industry](https://www.chosun.com/english/video-en/2026/05/25/AKNATIPOH5AM7PPDXPAMJAIYI4/)**

Robots Expand Presence in Daily Life and Industry The Picture From festival processions to factory floors, robots demonstrate growing versatility and market potential

조선일보 • 1h ago

---

**[Southwest Bans Humanoid Robots After Viral Passenger Flights](https://www.techrepublic.com/article/news-southwest-bans-humanoid-robots-flights/)**

Southwest banned human-like and animal-like robots from cabins and checked baggage after viral flights raised concerns about lithium-ion battery safety.

TechRepublic • 2d ago

---

**[China puts humanoid robots through tea harvesting field trials](https://interestingengineering.com/ai-robotics/china-tests-humanoid-robots-in-tea-farms-before-the-2026-world-robot-games)**

China is testing humanoid robots in tea production as part of preparations for the 2026 World Humanoid Robot Games.

Interesting Engineering • 2d ago

---

**[UK’s Humanoid partners with Bosch to mass-produce HMND robots for industries](https://interestingengineering.com/ai-robotics/uk-humanoid-bosch-industrial-robot)**

Humanoid partners Bosch to scale HMND humanoid robot production after successful 2026 proof of concept trials.

Interesting Engineering • 2d ago

---

**[Amazon celebrates opening of Virginia Beach robotics facility](https://www.pilotonline.com/2026/05/24/amazon-robotics-facility-virginia-beach/)**

It’s Amazon’s third robotics fulfillment center in Virginia.

The Virginian-Pilot • 9h ago

---

**[Robotics as a Service: Unlocking a Massive New Market](https://etfdb.com/artificial-intelligence-content-hub/unlocking-a-massive-new-market-robotics-as-a-service/)**

ETF Database • 3d ago

---

---

## YouTube Videos: "robotics"

**[Figure 03 AI Robot Reveals Its UNFAIR Advantage… Humans Can’t Match It](https://www.youtube.com/watch?v=NPOqqDASRCA)**

A 22-year-old intern just beat a humanoid robot… but this might be the LAST time a human wins like this. In Figure AI's wild Man ...

📺 The AI Nexus

👁️ 7K • 👍 166 • 💬 38 • ⏱️ 18:21 • 22h ago

---

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 42K • 👍 502 • 💬 201 • ⏱️ 5:15 • 2d ago

---

**[China&#39;s New Huawei-Backed Humanoid Robot Maid #robot #robotics #humanoidrobot](https://www.youtube.com/watch?v=8x1QbYZLswM)**

The Huawei-backed startup GigaAI just launched its AI-powered robot maid. The wheeled humanoid, named the SeeLight S1, ...

📺 Kalil 4.0

👁️ 719 • 👍 27 • ⏱️ 0:41 • 4h ago

---

**[T800 Terminator? Humanoid Robot GAME CHANGERS In 2026 ($40,000 AI ROBOT)](https://www.youtube.com/watch?v=3E3KyJsC8uE)**

The mass production era is officially here. As a brand new 10000-unit factory line fires up, we look at the biggest humanoid robot ...

📺 AI News

👁️ 8K • 👍 171 • 💬 37 • ⏱️ 8:02 • 1d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 148K • 👍 3K • 💬 119 • ⏱️ 22:41 • 5d ago

---

**[MOVA LiDax Ultra 3000 - Is This the Best Robot Lawn Mower?](https://www.youtube.com/watch?v=JlCdMKebkeY)**

Testing the MOVA LiDax Ultra 3000 AWD over the past few weeks has been seriously impressive. The AWD system handled ...

📺 Steve DOES

👁️ 37K • 👍 425 • 💬 2 • ⏱️ 16:22 • 2d ago

---

**[Ranking The Wildest Country Robots #robots #viral #shorts](https://www.youtube.com/watch?v=cfdL_mK0qUg)**

In this video, we rank different robots inspired by countries like China, Australia, Russia, the USA, and the United Kingdom.

📺 The area

👁️ 113K • 👍 4K • 💬 162 • ⏱️ 0:50 • 5d ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 19K • 👍 33 • 💬 5 • ⏱️ 0:07 • 3d ago

---

**[Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!](https://www.youtube.com/watch?v=faBkVCEEEHQ)**

Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry! Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!

📺 TESLA CAR WORLD

👁️ 29K • 👍 502 • 💬 54 • ⏱️ 15:32 • 4d ago

---

**[Man vs AI Robot: it’s officially over...](https://www.youtube.com/watch?v=j5MtBTPGJng)**

Man Vs Machine - we're entering the end times of AI deployment - do you want to live in a world of AI powered robots and LLM's ...

📺 Stylosa

👁️ 16K • 👍 421 • 💬 296 • ⏱️ 16:12 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

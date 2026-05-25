---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-25T08:57:17.557903+00:00'
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

**Last Updated:** May 25, 2026 at 08:57 UTC  
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

6h ago

---

**[Update on my vibro-quad (vibration-based quadrupedal robot)](https://www.reddit.com/r/robotics/comments/1tmcj2h/update_on_my_vibroquad_vibrationbased_quadrupedal/)**

I've finally submitted my PhD thesis and have some time to work on my favourite robot build so far. I managed to implement omnidirectional motion and field-centric drive. It's not perfect yet (I switched from a 9-axis IMU to a 6-axis, and now drift is a real issue), but I definitely think this is a good proof of concept. Has anyone seen this approach before? Most vibration robots I've found are either single-direction bristlebots or differential swarm bots like Kilobots. I haven't found much on holonomic vibration drive. Curious if I'm reinventing the wheel.

19h ago

---

**[People can no longer complain that unitree is not focusing on being useful ,they are starting to do figure things ofcourse still a little clumpsy Conference room mess cleanup test](https://www.reddit.com/r/robotics/comments/1tn1w3f/people_can_no_longer_complain_that_unitree_is_not/)**

So what do you make of this ,I read the title, it says "world model" and "VLA," so did they combine it ?It seems like a big deal. I feel like this is a big step. So what do you guys think ,I think I can finally say unitree has become a legitimate competitor to figure

🔗 [youtu.be](https://youtu.be/zqqIpVsMYkE?si=zFUFEpw4XYrZZKgo) • 1h ago

---

**[If you use NVIDIA Isaac Sim for reinforcement learning, do you use Isaac Lab with it? Just want to get a sense of what the status quo is.](https://www.reddit.com/r/robotics/comments/1tn1ged/if_you_use_nvidia_isaac_sim_for_reinforcement/)**

The reason for this query is that I am in the process of shifting to Isaac Sim / Isaac Lab since that is what seems to be in use nowadays. However, Isaac Lab is proving to be somewhat difficult to handle. While it handles the logging, and the creation of multi-actor systems for algorithms like PPO beautifully, its documentation leaves much to be desired. I am also concerned about the ease of setting up new robotic environments, actions, rewards, policies and possibly even custom algorithms. So, what is it that you do at your lab?

1h ago

---

**[Need some help figuring out gait mechanics and servo torque](https://www.reddit.com/r/robotics/comments/1tmyamn/need_some_help_figuring_out_gait_mechanics_and/)**

As the title suggests, I'm struggling to figure out how to really program a proper gait for my quadrupedal robot; I've looked into tripod gaits and such, but does anyone have any advice for how to implement reinforcement learning or something similar? I'm considering attaching an IMU to the setup but I still don't know how to like get the legs to adapt and "figure it out themselves". I'm using an ESP32 as the main microcontroller with the arduino as just a sort of power source (will switch out in the future), and therefore I'm using the Arduino IDE for programming and haven't explored micropython My main problem is that I don't think my servos have enough torque to push the entire build off the ground, should I shorten the limbs or try other gaits first? Right now I'm hardcoding the servo positions and its been more like trial-and-error, if anyone has ANY advice or recommendations, I would really appreciate it. I'm aware that this post may be too vague, but pls feel free to dm me about the project.

4h ago

---

**[new Nodding Mechanism is on robot now](https://www.reddit.com/r/robotics/comments/1tmxbff/new_nodding_mechanism_is_on_robot_now/)**

5h ago

---

**[Meet LimX Luna—Our Next-Gen Full-Size Interactive Humanoid Robot. Are they legitimate competitor?](https://www.reddit.com/r/robotics/comments/1tn3079/meet_limx_lunaour_nextgen_fullsize_interactive/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/-lgo5xqgVko?si=M1M-LnBZNLJIgs7R) • 23m ago

---

**[New RealSense SDK Beta Release!](https://www.reddit.com/r/robotics/comments/1tmp6ec/new_realsense_sdk_beta_release/)**

SDK Highlights - Partial-device-allowed is now the default — D400/D500 USB no longer silently drops degraded enumerations (configurable). - Jetson JP6 / 6.2.2 support added; fixes missing metadata over USB3 on JP6. - Bundled D400 firmware removed from the SDK package. - NEON acceleration: new BUILD_WITH_NEON flag; CUDA falls back to NEON; pointcloud correction. - MIPI driver version exposed via camera_info; new External Sync XU. Viewer - Non-blocking stop-stream, fixes for read-only options, Linux recording load, Win11 taskbar icon, MIPI FW update flow. DFU - Correct downgrade-counter opcode, flash-lock detection fix, skip reset on unsigned FW, d401_gmsl min FW → 5.17.2.2. Bug Fixes - Python deadlock, WMF reset crash, Ctrl+C re-entrancy, D435 initial enumeration, D555 DB3 playback, rs-dds-adapter Windows leak. --- MIPI Driver Highlights - JetPack 7 on NVIDIA Thor — new platform support (RSDSO-20559). - JetPack 5.1.6 and 6.2.2 added (RSDSO-21191, RSDSO-21146). - MAX96712 multi-camera: dual-camera per deserializer on JP6.x and quad-D457 via full-slave mode (RSDSO-20613). - External sync via TSC PWM (Thor-friendly), restored MAX9296 + consolidated MAX9295 GPIO tunneling (RSDSO-21407). - New carrier boards: Advantech (Orin, JP6/JP7) and AVerMedia (JP6.x). - Link tuning: MAX96712 lanes raised to 2500 Mbps; MFP6 added for links B–D. Stability - DS5 reset/detection rework, MAX9296 power_off underflow fix (spurious XCLR), JP6.x DTB deploy fix. --- D555 New Features - On-camera Object Detection (DamoYolo) — real-time bounding boxes/class/confidence published alongside streams; toggle via Color.option.Object_Detection_Enable. - UFO (UDP Fragmentation Offload) — higher throughput at high-res/fps; auto-enabled for standard MTU, disabled for jumbo frames. SafeDDS - More concurrent viewers per camera, better discovery, high-load stability, reliable notification delivery, stream-open timeout fix. ROS2 - Topic rename _CompressedColor → _Color/compressed; depth-unit in metadata; reduced topic overhead; CompressedColor auto-sync with RGB; better ROS2cli reliability. DFU - Real-time progress to host, pre-update integrity check, improved transfer reliability. Bug Fixes - Stream open timeout (RSDEV-6686), message drops under load (RSDEV-6314), network stall (RSDEV-6955), camera_info resolution mismatch (RSDEV-6683), ROS2 param/node CLI issues, 4-stream stability (RSDEV-7109). More info: https://github.com/realsenseai/librealsense/releases/tag/v2.58.1

11h ago

---

**[Cracked open an AMR on my day off.](https://www.reddit.com/r/robotics/comments/1tmkz8f/cracked_open_an_amr_on_my_day_off/)**

So this is how I spend my Sundays now. Picked up a fleet of AMRs and decided to reverse engineer it from the chassis up. Top’s off, I’m on the laptop sniffing what I can, and I’ve hit the point where the community brain trust would save me a few weekends. A few of these will end up on eBay in the coming weeks!

13h ago

---

**[Robot Dog Feet](https://www.reddit.com/r/robotics/comments/1tmj3rj/robot_dog_feet/)**

Hello, im currently building q robot dog similar to the MIT Mini Cheetah. However i cannot for the life of me find what kind of feet they used. Currently im using tpu spheres i 3d printed but getting a lot of slippage. Any reccomendations on the feet or what the actual Mini Cheetah used?

15h ago

---

---

## Google News: "robotics"

**[Humanoid robots work nonstop in package test](https://www.foxnews.com/tech/humanoid-robots-work-nonstop-package-test)**

Figure AI claims its three humanoid robots completed over 24 hours of continuous autonomous package sorting without any human control in a warehouse test.

Fox News • 16h ago

---

**[China's Walker humanoid robot amazes with precise ballet performance](https://interestingengineering.com/ai-robotics/chinese-humanoid-robot-stuns-with-ballet)**

UBTECH demonstates its new Walker C1 robot performing Swan Lake ballet with humans, showing advanced humanoid control.

Interesting Engineering • 21h ago

---

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 1d ago

---

**[China is deploying the first home cleaning humanoid robot butlers](https://www.fastcompany.com/91546673/china-is-deploying-the-first-home-cleaning-humanoid-robot-butlers)**

The SeeLight S1 may be the first commercial humanoid robot that will be deployed at homes to do all chores in the household.

Fast Company • 22h ago

---

**[Every humanoid robot in China set to receive personal identification number](https://www.scmp.com/tech/policy/article/3354747/china-give-every-humanoid-robot-digital-id-push-boost-industry-standards)**

South China Morning Post • 25m ago

---

**[Southwest Bans Humanoid Robots After Viral Passenger Flights](https://www.techrepublic.com/article/news-southwest-bans-humanoid-robots-flights/)**

Southwest banned human-like and animal-like robots from cabins and checked baggage after viral flights raised concerns about lithium-ion battery safety.

TechRepublic • 2d ago

---

**[Google, Japanese firm ship 1,000 robots in automation push](https://interestingengineering.com/ai-robotics/google-fanuc-physical-ai-industrial-robots)**

Google and FANUC partner to advance autonomous industrial robots for smarter factory automation systems.

Interesting Engineering • 2d ago

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

The Virginian-Pilot • 18h ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 53K • 👍 602 • 💬 238 • ⏱️ 5:15 • 2d ago

---

**[T800 Terminator? Humanoid Robot GAME CHANGERS In 2026 ($40,000 AI ROBOT)](https://www.youtube.com/watch?v=3E3KyJsC8uE)**

The mass production era is officially here. As a brand new 10000-unit factory line fires up, we look at the biggest humanoid robot ...

📺 AI News

👁️ 9K • 👍 182 • 💬 37 • ⏱️ 8:02 • 1d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 153K • 👍 3K • 💬 122 • ⏱️ 22:41 • 5d ago

---

**[China&#39;s New Huawei-Backed Humanoid Robot Maid #robot #robotics #humanoidrobot](https://www.youtube.com/watch?v=8x1QbYZLswM)**

The Huawei-backed startup GigaAI just launched its AI-powered robot maid. The wheeled humanoid, named the SeeLight S1, ...

📺 Kalil 4.0

👁️ 1K • 👍 42 • 💬 1 • ⏱️ 0:41 • 13h ago

---

**[MOVA LiDax Ultra 3000 - Is This the Best Robot Lawn Mower?](https://www.youtube.com/watch?v=JlCdMKebkeY)**

Testing the MOVA LiDax Ultra 3000 AWD over the past few weeks has been seriously impressive. The AWD system handled ...

📺 Steve DOES

👁️ 45K • 👍 497 • 💬 2 • ⏱️ 16:22 • 2d ago

---

**[NEW LUMIN Laser Guns Fire around the Corner [War Robots]](https://www.youtube.com/watch?v=Btn2F-Cl8vQ)**

War Robots Gameplay: NEW LUMIN Laser Guns fire around the corner - WR My War Robots Creator Link: ...

📺 Manni-Gaming

👁️ 10K • 👍 478 • 💬 138 • ⏱️ 16:48 • 21h ago

---

**[Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!](https://www.youtube.com/watch?v=faBkVCEEEHQ)**

Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry! Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!

📺 TESLA CAR WORLD

👁️ 29K • 👍 505 • 💬 54 • ⏱️ 15:32 • 4d ago

---

**[Atlas Robot Is Stronger Than People Expected](https://www.youtube.com/watch?v=tShZ4bBhMTo)**

Boston Dynamics just revealed one of the craziest Atlas robot demonstrations yet. The humanoid robot is now capable of lifting ...

📺 DPCcars

👁️ 31K • 👍 220 • 💬 62 • ⏱️ 3:26 • 6d ago

---

**[Ranking The Wildest Country Robots #robots #viral #shorts](https://www.youtube.com/watch?v=cfdL_mK0qUg)**

In this video, we rank different robots inspired by countries like China, Australia, Russia, the USA, and the United Kingdom.

📺 The area

👁️ 118K • 👍 4K • 💬 167 • ⏱️ 0:50 • 5d ago

---

**[Robot Vacuum Running! iRobot Edition #3](https://www.youtube.com/watch?v=DqsxWPWhIrI)**

📺 Planet Roomba

👁️ 2K • ⏱️ 14:27 • 18h ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-26T00:06:12.470991+00:00'
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

**Last Updated:** May 26, 2026 at 00:06 UTC  
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

21h ago

---

**[Robotica arm, 3 axis](https://www.reddit.com/r/robotics/comments/1tncu8d/robotica_arm_3_axis/)**

8h ago

---

**[Need some help figuring out gait mechanics and servo torque](https://www.reddit.com/r/robotics/comments/1tmyamn/need_some_help_figuring_out_gait_mechanics_and/)**

As the title suggests, I'm struggling to figure out how to really program a proper gait for my quadrupedal robot; I've looked into tripod gaits and such, but does anyone have any advice for how to implement reinforcement learning or something similar? I'm considering attaching an IMU to the setup but I still don't know how to like get the legs to adapt and "figure it out themselves". I'm using an ESP32 as the main microcontroller with the arduino as just a sort of power source (will switch out in the future), and therefore I'm using the Arduino IDE for programming and haven't explored micropython My main problem is that I don't think my servos have enough torque to push the entire build off the ground, should I shorten the limbs or try other gaits first? Right now I'm hardcoding the servo positions and its been more like trial-and-error, if anyone has ANY advice or recommendations, I would really appreciate it. I'm aware that this post may be too vague, but pls feel free to dm me about the project.

19h ago

---

**[Peg-in-hole Insertion using Sensor Fusion & RL](https://www.reddit.com/r/robotics/comments/1tno63j/peginhole_insertion_using_sensor_fusion_rl/)**

I am working on a peg-in-hole robotic assembly thesis with a Doosan M1013, ROS2 & an eye-in-hand RGB-D camera. The upstream perception system gives a coarse hole/block pose from stationary RGB-D cameras. Based on prior measurements/error propagation, the pre-insertion uncertainty may be around 3–5 mm average and up to 7–11 mm worst case, with about 1–2° angular error. I want to train a contact-rich insertion policy using vision + force/torque + proprioception, starting from a pre-insert pose about 5–20 mm above the hole. The task should eventually generalize across several cross-section geometries. For people who have worked on force-guided or vision-force peg-in-hole insertion: is this initial error range realistic for an RL/contact policy to handle directly, or would you recommend adding a TCP-camera visual refinement step before starting the RL policy? I am especially interested in practical experience with: ±5 mm vs ±10 mm initial xy error 1–2° orientation error force/torque-based local search after first contact sim-to-real transfer difficulty whether eye-in-hand visual refinement is worth the extra time I am new to this field. Kindly help me out.

1h ago

---

**[I got tired of exporting massive CSV files to debug signal noise with remote teammates, so I built an open-source browser viewer (Feedback wanted)](https://www.reddit.com/r/robotics/comments/1tnfmrg/i_got_tired_of_exporting_massive_csv_files_to/)**

Hey everyone, I’m a robotics engineer working across both the programming and electronics, debugging remotely with a teammate or getting code guys to understand a physical hardware glitch is a massive bottleneck. Usually, my choices are taking a blurry phone picture of my oscilloscope screen to send over Slack, or exporting a massive, CSV file that crashes basic spreadsheet apps and completely kills any signal interactivity. Software engineers have GitHub, Figma, and Linear for instant cloud collaboration. Hardware engineers get USB flash drives and proprietary enterprise desktop software. To bridge this gap, I built a completely free, browser-based, hostless platform designed to act like an opensource viewer for hardware signal data.

🔗 [wavebench.vercel.app](https://wavebench.vercel.app/) • 6h ago

---

**[Ajuda com baterias](https://www.reddit.com/r/robotics/comments/1tnlobv/ajuda_com_baterias/)**

3h ago

---

**[If you use NVIDIA Isaac Sim for reinforcement learning, do you use Isaac Lab with it? Just want to get a sense of what the status quo is.](https://www.reddit.com/r/robotics/comments/1tn1ged/if_you_use_nvidia_isaac_sim_for_reinforcement/)**

The reason for this query is that I am in the process of shifting to Isaac Sim / Isaac Lab since that is what seems to be in use nowadays. However, Isaac Lab is proving to be somewhat difficult to handle. While it handles the logging, and the creation of multi-actor systems for algorithms like PPO beautifully, its documentation leaves much to be desired. I am also concerned about the ease of setting up new robotic environments, actions, rewards, policies and possibly even custom algorithms. So, what is it that you do at your lab?

16h ago

---

**[Update on my vibro-quad (vibration-based quadrupedal robot)](https://www.reddit.com/r/robotics/comments/1tmcj2h/update_on_my_vibroquad_vibrationbased_quadrupedal/)**

I've finally submitted my PhD thesis and have some time to work on my favourite robot build so far. I managed to implement omnidirectional motion and field-centric drive. It's not perfect yet (I switched from a 9-axis IMU to a 6-axis, and now drift is a real issue), but I definitely think this is a good proof of concept. Has anyone seen this approach before? Most vibration robots I've found are either single-direction bristlebots or differential swarm bots like Kilobots. I haven't found much on holonomic vibration drive. Curious if I'm reinventing the wheel.

1d ago

---

**[Meet LimX Luna—Our Next-Gen Full-Size Interactive Humanoid Robot. Are they legitimate competitor?](https://www.reddit.com/r/robotics/comments/1tn3079/meet_limx_lunaour_nextgen_fullsize_interactive/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtu.be](https://youtu.be/-lgo5xqgVko?si=M1M-LnBZNLJIgs7R) • 15h ago

---

**[new Nodding Mechanism is on robot now](https://www.reddit.com/r/robotics/comments/1tmxbff/new_nodding_mechanism_is_on_robot_now/)**

20h ago

---

---

## Google News: "robotics"

**[Delivery robots are spreading across LA. Residents ‘both pity and hate them’](https://www.theguardian.com/us-news/2026/may/25/los-angeles-delivery-robots)**

A region known for its lack of walkability now has more obstacles for pedestrians to contend with

The Guardian • 10h ago

---

**[Former NASA Robotics Chief: America is building the wrong kind of robots — and China knows it](https://fortune.com/2026/05/23/humanoid-robots-america-china-adaptability-deployment-ambrose-nasa/)**

The U.S. is optimizing humanoid robots for factory demos and backflips. A former NASA robotics division chief explains why adaptability — not performance — is the metric that will determine who leads global manufacturing.

Fortune • 2d ago

---

**[Humanoid Turns to Bosch to Bring Its Warehouse Robots Into Mass Production](https://www.eweek.com/news/humanoid-bosch-warehouse-robots-production/)**

Humanoid’s Bosch deal moves HMND 01 warehouse robots toward mass production after a German logistics pilot tested box-handling workflows in March.

eWeek • 11h ago

---

**[Every humanoid robot in China set to receive personal identification number](https://www.scmp.com/tech/policy/article/3354747/china-give-every-humanoid-robot-digital-id-push-boost-industry-standards)**

South China Morning Post • 15h ago

---

**[Amazon celebrates opening of Virginia Beach robotics facility](https://www.pilotonline.com/2026/05/24/amazon-robotics-facility-virginia-beach/)**

It’s Amazon’s third robotics fulfillment center in Virginia.

The Virginian-Pilot • 1d ago

---

**[Los Gatos High robotics team takes top honors in international competition](https://www.mercurynews.com/2026/05/24/los-gatos-high-robotics-team-takes-top-honors-in-international-competition/)**

Iron Claw hooks a spot in world championship finals.

The Mercury News • 1d ago

---

**[Popular robotics company shuts down and liquidates all assets](https://www.thestreet.com/technology/popular-robotics-company-shuts-down-and-liquidates-all-assets)**

thestreet.com • 9h ago

---

**[Tesla Model S Sparked Elon Musk's AI, Robotics And Space Revolution: 'Little Did We Know,' Says Cathie Wood](https://finance.yahoo.com/sectors/technology/articles/tesla-model-sparked-elon-musks-113132838.html)**

Investor Cathie Wood of ARK Invest has hailed the Tesla Inc. Model S following its sunset for kicking off a “revolution” led by Elon Musk in the artificial intelligence, outer space exploration and robotics sectors. Little Did We Know Wood,...

Yahoo Finance • 1d ago

---

**[Faraday Future Founder and Global CEO YT Jia Shares Weekly Investor Update: FF’s Largest-Ever 23-Unit Robot Order Marks Another Step Toward Becoming a Pathbreaker and Driving Force in the Global B2C Robotics Market](https://www.morningstar.com/news/business-wire/20260525830679/faraday-future-founder-and-global-ceo-yt-jia-shares-weekly-investor-update-ffs-largest-ever-23-unit-robot-order-marks-another-step-toward-becoming-a-pathbreaker-and-driving-force-in-the-global-b2c-robotics-market)**

Morningstar • 36m ago

---

**[Ukraine’s Ground Robots Are Becoming Battlefield Platforms—And Procurement Is About to Surge](https://united24media.com/world/ukraines-ground-robots-are-becoming-battlefield-platforms-and-procurement-is-about-to-surge-19106)**

Ukraine plans UGV procurement Ukraine 2026 to double in 2026, reaching nearly 25,000 units, adding EW, radar, missiles and mortars to combat roles.

UNITED24 Media • 2d ago

---

---

## YouTube Videos: "robotics"

**[Potential dangers of humanoid robots](https://www.youtube.com/watch?v=01ZSOp4yYAE)**

Humanoid robots are devices that could be used to improve our daily lives. But could they also be used for surveillance?

📺 ABC News

👁️ 65K • 👍 753 • 💬 292 • ⏱️ 5:15 • 3d ago

---

**[STILL EARLY! Top 4 Robotics Stocks that are Better Than Nvidia](https://www.youtube.com/watch?v=JJPsh0CIIfA)**

Here are 4 robotics stocks to outperform Nvidia going forward. Join SeekingAlpha Premium for $30 off an annual plan: ...

📺 Fin Tek

👁️ 160K • 👍 3K • 💬 123 • ⏱️ 22:41 • 6d ago

---

**[Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!](https://www.youtube.com/watch?v=faBkVCEEEHQ)**

Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry! Tesla Bot Gen 3 AI5 Upgrade Finally Destroy Robot Industry!

📺 TESLA CAR WORLD

👁️ 30K • 👍 519 • 💬 55 • ⏱️ 15:32 • 5d ago

---

**[Ranking The Wildest Country Robots #robots #viral #shorts](https://www.youtube.com/watch?v=cfdL_mK0qUg)**

In this video, we rank different robots inspired by countries like China, Australia, Russia, the USA, and the United Kingdom.

📺 The area

👁️ 132K • 👍 4K • 💬 178 • ⏱️ 0:50 • 6d ago

---

**[AI Robots Just SHOCKED The World… This Is Getting Too Real](https://www.youtube.com/watch?v=ohySlGQMDkE)**

What's happening in robotics right now is straight-up unbelievable — and you NEED to see this before anyone else does.

📺 The AI Nexus

👁️ 5K • 👍 100 • 💬 8 • ⏱️ 20:16 • 6d ago

---

**[Robots Now Communicate Like Ant Colonies 🐜🤖 #robotics #ai #shorts](https://www.youtube.com/watch?v=GXQ07hkfAmY)**

Ant-Inspired Robots Just Learned A New Language What if robots could communicate exactly like ants? Researchers at the ...

📺 EcoZora

👁️ 17K • 👍 33 • 💬 5 • ⏱️ 0:07 • 4d ago

---

**[Robot falls during Michael Jackson performance, gets dragged off stage](https://www.youtube.com/watch?v=9TIk9n_ka_I)**

Hee, hee: Billie Jean may not have been its lover — but the floor definitely was. A humanoid robot went viral after tripping and ...

📺 CNA

👁️ 342K • 👍 3K • 💬 475 • ⏱️ 0:44 • 4d ago

---

**[PEEKING ABOVE BUILDINGS — War Robots 12.1 Overview](https://www.youtube.com/watch?v=s4FtwjBDasI)**

Get the update on your app store: https://wr.my.games/play ➡️ Get the update through the official APK: ...

📺 War Robots [WR]

👁️ 60K • 👍 2K • 💬 345 • ⏱️ 3:14 • 5d ago

---

**[Dancing Robot Fail | Bill Burr](https://www.youtube.com/watch?v=Oe-lr0hRI10)**

From @BillBurrOfficial - Thursday Afternoon Monday Morning Podcast 5-21-26 Watch the Full Episode Here: ...

📺 Bill Burr

👁️ 15K • 👍 469 • 💬 43 • ⏱️ 0:51 • 3d ago

---

**[Southwest Airlines adds robot ban after viral Love Field flight](https://www.youtube.com/watch?v=5qIcnLTqeJY)**

After a human-like robot took a flight from Dallas Love Field to Las Vegas, Southwest Airlines changed their baggage policy to ban ...

📺 FOX 4 Dallas-Fort Worth

👁️ 65K • 👍 183 • 💬 158 • ⏱️ 2:49 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

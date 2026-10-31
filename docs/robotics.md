---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-31T08:41:29.055510+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- news
- social
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** October 31, 2026 at 08:41 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Reachy Mini "Level UP" update](https://www.reddit.com/r/robotics/comments/1xikqpw/reachy_mini_level_up_update/)**

Hello, Today we're doing a big release for Reachy Mini. It mainly contains three things: A hoverboard, to give Reachy Mini some much-needed mobility. I'm a big inverted pendulum fan and I absolutely love this one, sometimes I just do sit → stand up → sit → stand up on repeat because it's so smooth (in the demo above it isn't smooth as it hits the ground, but that was my fault, I messed up the IMU setup) A smartphone app, available on iOS and Android: no computer needed to interact with the robot anymore NFC tags, allowing for new angles of creative personalization (e.g. one hat = one personality) We hope you'll build great things with these new tools, learn stuff and have fun!

1d ago

---

**[Reachy Mini can finally move. Hugging Face are launching Reachy Mini "Level Up", a set of new accessories for Reachy Mini: wheels, phone apps, and hats that change its personality](https://www.reddit.com/r/robotics/comments/1xihfah/reachy_mini_can_finally_move_hugging_face_are/)**

https://pollen-robotics.com/reachy-mini/#level-up From Thomas Wolf on 𝕏: https://x.com/Thom_Wolf/status/2115764335498965468

1d ago

---

**[Getting a π0.5 policy trained on one YAM rig to work on another: fine-tuning ablations, a latency bug, and fitting it in 16 GB](https://www.reddit.com/r/robotics/comments/1xip9dr/getting_a_π05_policy_trained_on_one_yam_rig_to/)**

A few weeks ago we ran a live π0.5 demo at IROS, and getting there turned into a good lesson in how many things can go wrong between "the policy works on the data rig" and "the policy works somewhere else." Our cofounder Bayley wrote it up in three parts, and I figured people here would find the details useful. The setup: we had a clean pick-and-place dataset from one YAM rig and wanted a checkpoint trained on it to run on a different YAM setup, in a convention hall none of us had seen. That's a common spot for smaller labs too, working with the rig they already have instead of rebuilding the one the data came from. Part 1: fine-tuning Most of the ablations ran in a path-traced MuJoCo sim he built, so we could do thousands of rollouts a day without resetting anything. The biggest takeaway was to train the VLM and not just the action expert. Expert-only got 51% pickups and 12% dropoffs. The full fine-tune got 89% and 53%, and an r=128 LoRA got 84% and 59% while fitting in 32 GB. Lighting was the surprise. Hard light from 10 cm disks (basically bare bulbs) roughly halved the expert-only checkpoint and didn't hurt the full fine-tune at all. Cameras turned out to matter more. Nudging the overhead camera barely changed whether the arm lifted the target, but it broke placing, and shifting the wrist camera 1 cm sideways made 11 of 30 paired rollouts worse. The same scene rendered under four lighting setups in our sim, from large soft panels down to 10 cm disks (roughly bare bulbs). The hard-light setup roughly halved the expert-only checkpoint and didn't affect the full fine-tune. Part 2: latency On the real rig, performance was worse than it should have been, and we were close to doing an RL pass to fix it. Then someone actually watched the video feed in the inference dashboard and saw it lagging by several hundred milliseconds. The culprit was Python's buffered pipe holding camera frames until 64 KB built up. Our sim had said up to 280 ms of latency didn't matter. The robot disagreed, probably because near misses knock things around in ways a simple physics model smooths over. After that he went after inference itself. The stock LeRobot code ran at over 230 ms per step, and he got it to 87 ms on an RTX 5090 Mobile by casting weights to bf16 once instead of on every call, capturing a CUDA graph for the action expert, removing an autograd graph nobody was using, exporting SigLIP to ONNX, and switching Gemma to fp16 (GeForce cards run bf16 at half speed). Once it was fast enough, the policy started doing what our operators do: a quick approach, a pause, a small correction, then the grab. Mean inference latency per step on an RTX 5090 Mobile, from over 230 ms with the stock LeRobot code down to 87 ms. Each bar is one change. Part 3: memory 24 GB laptop GPUs keep getting harder to find, so the last piece was getting the stack under 16 GB. Two fixes took peak VRAM from about 22 GB to 11.2 GB: not building a throwaway fp32 backbone at load, and not keeping PyTorch copies around next to the TensorRT engines. It now runs on cards like the RTX 5080 and 5070 Ti. Peak VRAM for the rollout stack, before and after the two fixes, against 16 GB (RTX 5080 / 5070 Ti) and 24 GB (RTX 5090 Mobile) cards. One caveat: the Part 1 numbers are from sim, which scores a little higher than our real rig, but the trends held up. Full write-ups are on our blog (I work at PrismaX, where Bayley is cofounder), and both repos are open source: Part 1, fine-tuning: https://blog.prismax.ai/article.html?slug=openpi-pi05-fine-tuning Part 2, latency: https://blog.prismax.ai/article.html?slug=latency-vs-pi05-rollout-performance Part 3, memory: https://blog.prismax.ai/article.html?slug=pi05-inference-in-16gb Simulator: https://github.com/PrismaXAI/yamulator Rollout stack: https://github.com/PrismaXAI/prism-pi Happy to answer questions or pass them along to Bayley.

1d ago

---

**[Heyy Guys See my Latest Project](https://www.reddit.com/r/robotics/comments/1xitn4j/heyy_guys_see_my_latest_project/)**

So I saw this cute little robot somewhere( 3d design credit to the original creator don't know his reference ) and thought, why not build it myself. I got the body 3D printed and started playing around with the open-source code, but honestly, it was pretty basic compared to what I had in mind for this little dude. So I ended up spending almost the next month building my own ecosystem around it. Now Yeti has 100+ emotions and behaviours, along with a gyro, microphone, LDR and touch sensors. I also added different functionalities so it can work as both a little robot and a clock, with sounds, reactions and different behaviours depending on how you interact with it. The feature I'm probably most excited about is that you can flash new firmware to Yeti directly from your phone over Bluetooth. No Arduino IDE, laptop or cable needed. I also built a companion app that lets your phone connect to Yeti automatically when you're nearby. And then I went a bit overboard. I made it possible for different Yetis to communicate with each other through their phones over the internet. So two Yetis paired with different phones can exchange messages, little scribbles, sounds and other stuff. You can even send things like a cute Happy Birthday message/sound to another Yeti. This is honestly the first time I've built something like this, so I'd really love to hear what you guys think. I'm still figuring out what Yeti should become and what else I can add to it. Would love feedback from people into robotics, ESP32, or just building random little things like this

1d ago

---

**[We built a robot policy competition that ranks in two sims, then runs the top 10 on a real Franka](https://www.reddit.com/r/robotics/comments/1xirva5/we_built_a_robot_policy_competition_that_ranks_in/)**

Hey - in March I posted PhAIL here. We ran robot AI models on a real robot doing bin picking, and the best one did 64 picks/hour, against 1,300 for a human. The top comment was about how brutal the gap between sim and real is. Everyone trains and tests in sim, and nobody really knows how much a sim score tells you about a real robot. We don't know either. Since then we added a DROID benchmark to PhAIL, and together with Nebius we started a competition to get an answer. If some of you come and take part, we'll be really happy, that's partly why I'm posting. But mostly we want to have fun with the community and see how big the gap actually is. The story is simple. You train a policy, pack it into Docker, submit and we score it in two sims: MolmoSpaces now, RoboLab starting from 16 Nov. In December the top 10 will run the same image on our real Franka, on tasks like the DROID benchmark, but on a different set. So being great in one sim is not enough. You need to do well in both, and then the real robot decides. Which makes me wonder: what would a robot have to do in the finale for you to believe the result? I think the winner will be whoever balances the two sims and the real robot best, and I'm curious how people will approach it. We also added a couple of constraints on purpose. The policy has to fit in 24 GB, which is what a 4090 has, so a lot of people can test at home. That's also less than current top models need (FLUX 3 Action takes about 35 GB), so you can't just take the biggest model and fine-tune it. And thinking isn't free: the sim clock keeps running while your model computes, the same way a real robot keeps moving. RTC support is coming soon, so potentially you can think for more time, and still finish on time. We don't want everyone to wait until December to see real-robot results, so every week we'll run a few of the submitted policies on the real Franka and share the results with participants. What made this possible is our framework, positronic. A policy Docker image serves one API, and we built it so that a new sim plugs in almost for free. That's how one submission runs in two sims and on the real robot. We also made the whole entry (sign-up, submission, results) work through your coding agent, because that's how most of us work now. There are example images for π0.5, GR00T N1.7 and MolmoAct2 to start from. Whatever we learn about sim vs real, we'll publish it. Prizes are $23.5k in Nebius GPU and eval credits, and $1k of that goes to the best open-source write-up. Everything is at competition.phail.ai And if you're curious about the infra we built to run the competition, let me know in the comments, happy to tell more about it.

1d ago

---

**[Redesigning my DIY USV after its first field test — moving toward a modular robotics platform](https://www.reddit.com/r/robotics/comments/1xilg4g/redesigning_my_diy_usv_after_its_first_field_test/)**

https://preview.redd.it/v0jg3tlh0fyh1.png?width=1672&format=png&auto=webp&s=d3413892cbe266c89f69d47960024d001e68f01a https://preview.redd.it/71xajvod1fyh1.png?width=1295&format=png&auto=webp&s=df05c6a061996500d77af66f921e3ff97a30b890 Hi everyone! A while ago, I shared the first version of my DIY unmanned surface vehicle, BN-USV. Since then, I've been working on a second version, and I wanted to share some of the design changes and the reasoning behind them. Here's the earlier V1 post for context: https://www.reddit.com/r/raspberry_pi/s/n3gdRr99w9 The first prototype taught me that getting a robot to work reliably on the water is quite different from testing individual components indoors. While the basic RC operation worked, the field test highlighted several areas that needed improvement, including heading estimation, control response, weight distribution, and access to the onboard electronics. For V2, I'm focusing on three major changes: 1. A modular hull design Instead of treating the hull as one integrated structure, I'm dividing it into replaceable sections. The goal is to make it easier to modify individual parts, experiment with different configurations, and repair damaged components without rebuilding the entire boat. https://preview.redd.it/ubz33w0s0fyh1.png?width=1920&format=png&auto=webp&s=4008bfe00ce855ac7d53927158995f7e42310c84 2. A distributed control architecture I'm redesigning the electronics around a main module and two propulsion modules connected through CAN communication. The Raspberry Pi 5 will handle higher-level processing, while ESP32-based controllers will manage lower-level control and safety functions. One important goal is for each propulsion module to respond safely to communication failures without depending entirely on the main computer. https://preview.redd.it/1ugqmvcu0fyh1.png?width=1920&format=png&auto=webp&s=e520f66d7c4bb1aa9a8541934f4c1980b69ed36d https://preview.redd.it/3xsxtvcu0fyh1.png?width=1920&format=png&auto=webp&s=13dfae9f0ded6d3736b04afb7cf4aefa8d62f843 3. Prioritizing reliability before autonomy Initially, I wanted to move quickly toward waypoint-based autonomous navigation. However, the first field test made it clear that reliable manual control, predictable steering behavior, and robust communication should come first. I'm now focusing on those fundamentals before moving further into autonomous navigation. V2 is still under development, so these are design goals rather than fully validated improvements. I'll continue sharing the development process, including the things that don't work as expected. The long-term goal is to make BN-USV a modular platform for marine robotics experiments, education, research, and custom applications. I'm developing BN-USV as part of BrillNova, with the aim of eventually making the hardware platform commercially available. I'm also sharing the software and development process publicly. I'd love to hear your thoughts: For those building outdoor robots, has modularity made maintenance and experimentation easier, or has it introduced more complexity than expected? Project links GitHub: https://github.com/Brillnova YouTube (development videos): https://www.youtube.com/@Brillnova Thanks for reading!

1d ago

---

**[Mino's first autonomous stroll outside](https://www.reddit.com/r/robotics/comments/1xit2za/minos_first_autonomous_stroll_outside/)**

Mino's software stack is based on ROS 2. We both went to the ROS conference (ROSCon) this week to meet some of the folks that make our favorite middleware possible. I wanted Mino to come with me and interact with people at the conference, so I coded a special companion app for the event on the robot's Jetson Orin Nano. What you see in the video is the first outdoors test of the app before going to the train station on Monday. With Mino's open-source software building blocks and some help from a coding agent (Mino's code base is agent-friendly), this app was ready in a weekend. Depth estimation, person detection and tracking, pose feedback, odometry and motion control come out-of-the-box. The agent just had to glue Mino's capabilities together with the behavior logic I specified. Want to program your own apps on Mino? Subscribe on Kickstarter or to our waitlist to get notified when the Kickstarter campaign launches and catch the early-bird discounts. If the campaign succeeds, the source code of this app will ship with the robot! This is what the app does. It has three states: finding person, following person and hanging out with person. In the "finding person" state, the robot stays in place, looking around with base and head rotation until a person is detected. When that happens, the state changes to "following person", which tries to approach the person while keeping them at the center of the field of view and ignoring other people around. When close enough to the person, the state changes to "hanging out", which stays in place and keeps eye contact with the person. If they move away beyond a threshold, the state goes back to "following person" or, if the person is no longer found, to "finding person". The robot perceives each person's position and speed in 3D. A tuned YOLO-World detects people fully or partially inside the field of view of the cameras (the eyes). People detected with enough confidence get their 3D bounding boxes estimated by back-projecting their 2D counterparts to 3D space with the depth image from the stereo pair. They are then tracked across frames based on bounding box overlap and appearance similarity. Appearance is modeled with the embeddings from a classifier on each person's crop, and tracks are smoothed with a Kalman filter. Once the robot sees its buddy, it keeps re-calculating trajectories to steer its base and head to the target pose. The trajectories are followed by periodically sending head pose and base velocity commands to our custom hardware at the base. That hardware estimates the full-body pose and runs several control loops to achieve what's commanded from the Jetson. All that at high frequency and bounded latency. What would you create with Mino? Let me know in the comments 🙏

1d ago

---

**[Building a robot Lamp: Busiest month since day 1](https://www.reddit.com/r/robotics/comments/1xhkat2/building_a_robot_lamp_busiest_month_since_day_1/)**

Lamp's first commit was on 24 March. October has been the busiest month since: 4,092 commits on the main development branch so far, more than double April, the previous high at 1,615. The two busiest weeks ever were the last two. In the last post I said the hardware stays as it is while we focus on production. That hasn't changed. Everything below is software, plus the work needed to build many lamps instead of one. 1. A way to program it Someone asked in the last thread whether you can buy the lamp and change it with Claude Code. There's now a documented path for that. docs/develop.md takes about 10 minutes: a fake lamp that runs on your laptop, so you don't need the hardware, Python and JavaScript SDKs, pairing, and lamp-mcp. Skills moved to format 2. You check a skill, push it, sign it with your own key, and share it. Lamp refuses a package that is unsigned, changed, or renamed. 2. Knowing who said what Lamp now ties each line to the face and voice that said it and keeps each person's memory separate. If you talk to it before it recognizes you, those lines are attached to you once it does. It only keeps what you said about yourself. Not its own words, not your questions. "Forget everything" now asks once and runs only on the same person's yes. Forgetting one specific thing went from 9 s to under 400 ms on a 10 MB memory store. How we trained our Lamp in the office 3. Camera permissions per skill A skill gets the camera image only after the owner allows that specific skill. Checking whether someone is in the room is a separate, smaller permission that doesn't include the image. Installing a skill by hand in place of a Store skill removes the permission. Onboarding also asks once whether Lamp may notice facial expressions, and stores only a yes. 4. Giving way to a hand Last time someone asked whether the STS3215s give real position feedback. They do, and Lamp now uses it to tell a push from a fault. If a joint is carried away from its goal, Lamp treats it as a hand, stops what it was doing, and doesn't look around again for 30 s unless asked. Onboarding has a step for this: hold the base, tilt the head, let go when told. If an arm strains three times, Lamp sits down, rests for 30 minutes, then gets back up. EDIT: I tested a demo build, this feature is still on local branches, not fully public on the repo yet 5. Skills don't touch hardware · New lamps calibrate their servos at the factory before the first run · A new Orange Pi image boots straight into setup · lampOS 0.0.4 and 0.0.5 shipped on 22 Oct, including a fix for a button that could get stuck in a held state · The Fusion 360 file for the current body is in the repo. 5. Smaller changes · Speech starts streaming within 400 ms of the first part of an answer · The evening glow stays at least one level below your own light · "Tap to talk" is now "Press to talk". Not Done Yet Naming two people in the same room, add-ons, and ignoring lines meant for someone else in a busy room are built but off by default until they pass on real lamps. Mood reading is at 39% on our internal tracker, and we don't count it as done. a fleet of Lamps

2d ago

---

**[Using the OpenMV AE3 for IMU/image-synchronized visual-inertial odometry](https://www.reddit.com/r/robotics/comments/1xidr38/using_the_openmv_ae3_for_imuimagesynchronized/)**

https://preview.redd.it/6luau7aazcyh1.jpeg?width=600&format=pjpg&auto=webp&s=3582a461288ba2fa664509463ce37253f4275527 The OpenMV AE3 is a small camera that integrates both a global shutter sensor and an IMU. It can be programmed using Python scripts. I created a small script and modified firmware that sync the camera’s exposure with a specific IMU measurement, enabling better visual-inertial odometry as described in Nikolic et al., “A Synchronized Visual-Inertial Sensor System with FPGA Pre-Processing for Accurate Real-Time SLAM,” ICRA 2014. The firmware change adds a shared clock between the two CPU cores. The IMU runs at 208 Hz, and I trigger a camera exposure at every 10th IMU measurement, which gives about 20 FPS. Code: https://github.com/chobitsfan/openmv_img_imu Test flights with Kimera-VIO: Outdoor flight at 3 m/s: https://youtu.be/SfjxIDYtIhU Indoor flight: https://youtu.be/Cprryyq9pao

2d ago

---

**[I made a caniuse-style table of which robot learning policies run on which robots. Tell me where it's wrong](https://www.reddit.com/r/robotics/comments/1xilksa/i_made_a_caniusestyle_table_of_which_robot/)**

I kept seeing the same questions in LeRobot threads: does SmolVLA run on a Koch arm, will π0.5 fit on a Jetson Orin Nano, has anyone trained GR00T N1.7 on an SO-101. The answers were scattered across docs, papers, Hub model cards and GitHub issues, so I put them in one table. https://caniembody.pages.dev It covers 24 robots and 21 policies (ACT, Diffusion Policy, SmolVLA, π0/π0.5, GR00T N1.7, X-VLA, OpenVLA-OFT and others). Every filled cell links to its source, with the date it was checked and the versions it applies to. 193 of the 504 robot-policy pairs have evidence so far. The rest are marked as having none, and I'm not guessing. A few things it does differently: - Each cell says what kind of evidence backs it: official docs, a public checkpoint, an issue thread, a paper. - "Partial" usually means someone trained it on that robot's data, but nobody has published a real-robot run. - Inference speeds always come with runtime, precision and camera count. SmolVLA on the same 8 GB Orin Nano measures under 1 Hz in PyTorch fp32 and over 5 Hz as split ONNX fp16. - The data is open (CC BY 4.0) with a JSON API, so you can use it in your own tools. I'd like to know which cells are wrong. If you've run one of these policies on one of these robots, especially if it failed, a link to a checkpoint, video or log is enough. Every cell has a "Dispute this cell" button that opens a pre-filled GitHub issue.

1d ago

---

---

## Google News: "robotics"

**[​Factory robot maker opens Madison Heights HQ to get closer to Detroit automakers​](https://www.crainsdetroit.com/manufacturing-logistics/cdb-ati-robotics-opens-madison-heights-20261029/)**

Ati Robotics is betting that proximity to Detroit’s automakers and suppliers will position it as a frontrunner in the future of factory innovation.

Crain's Detroit • 22h ago

---

**[Let's Have Some Fun: Spot Plays With a Tire, Reachy Mini Races Microduck](https://spectrum.ieee.org/video-friday-whole-body-manipulation)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 16h ago

---

**[Agility Robotics and Churchill Capital Corp XI Announce Expected Gross Capital Raise of Approximately $465 Million and Anticipated Closing of Business Combination](https://finance.yahoo.com/technology/ai/articles/agility-robotics-churchill-capital-corp-110000046.html)**

Business combination expected to close on November 4, 2026, subject to Churchill XI shareholder approval; the combined company expected to begin trading on Nasdaq under ticker symbol “AGLT” on November 5, 2026. Agility is expected to be the only U.S. publicly listed pure-play humanoid robotics company with proven, active commercial deployments. SALEM, Ore. and NEW YORK, Oct. 30, 2026 (GLOBE NEWSWIRE) -- Agility Robotics, a leading humanoid robotics and physical AI company, and Churchill Capital

Yahoo Finance • 21h ago

---

**['It’s pretty awesome': Korah robotics team is number one in the world](https://www.sootoday.com/inspire/its-pretty-awesome-korah-robotics-team-is-number-one-in-the-world-12957271)**

Another Korah team currently sits at second in Canada and 14th in the world

SooToday.com • 21h ago

---

**[The Humanoid Robot Market Could Be Worth More Than $7 Trillion. Here Are 3 Stocks to Own.](https://www.fool.com/investing/2026/10/29/the-humanoid-robot-market-could-be-worth-more-than/)**

The industry is still in its infancy, but it's becoming clear which names are best positioned to lead it to full viability.

The Motley Fool • 1d ago

---

**[The Rare Earths Powering the Next Wave of Robotics](https://www.barchart.com/story/news/8513371/the-rare-earths-powering-the-next-wave-of-robotics)**

Barchart.com • 2d ago

---

**[Krafton-backed Ludo Robotics releases robot intelligence model designed around human intent](https://siliconangle.com/2026/10/30/krafton-backed-ludo-robotics-releases-robot-intelligence-model-designed-around-human-intent/)**

Krafton-backed Ludo Robotics releases robot intelligence model designed around human intent - SiliconANGLE

SiliconANGLE • 14h ago

---

**[Opentrons Raises $40M in Series E to Expand Its Robotics, Software, Data Infrastructure](https://www.genengnews.com/topics/artificial-intelligence/opentrons-raises-40m-in-series-e-to-expand-its-robotics-software-data-infrastructure/)**

Plans include investing in AI-driven experimental execution, extending its automation capabilities, and expanding into new markets.

Genetic Engineering and Biotechnology News • 13h ago

---

**[Nucor invests in youth robotics to inspire future STEM leaders](https://norfolkdailynews.com/news/nucor-invests-in-youth-robotics-to-inspire-future-stem-leaders/article_a0aff69f-3331-486a-98c9-c0fdb0be230b.html)**

Nucor is strengthening its commitment to youth robotics and STEM education through its support of the Northeast iHub and local robotics programs, helping students develop skills that can lead to

The Norfolk Daily News • 18h ago

---

**[STEM, robotics open house Nov. 17](https://www.winonapost.com/community/stem-robotics-open-house-nov-17/article_d5bf1d4a-920c-4fce-bb53-e75badbf10fa.html)**

Local business leaders, community partners, and residents are invited to explore the connection between STEM education and Winona’s future workforce at Building the Future: STEM and Workforce Development Business and

Winona Post • 11h ago

---

---

## YouTube Videos: "robotics"

**[This Cute Robot Stole the Show at NVIDIA 🤖🥹#jensenhuang #nvidia #shorts](https://www.youtube.com/watch?v=DBOKSJYANgk)**

Meet Grek, the adorable robot that stole the show on stage with NVIDIA's CEO! From learning to walk in a virtual world to ...

📺 VisionX Lab

👁️ 950K • 👍 28K • 💬 961 • ⏱️ 0:59 • 5d ago

---

**[AI agent builds itself a robot body, does exactly what experts warned](https://www.youtube.com/watch?v=QRVz697rEx0)**

AI Robot. Is AI dangerous? Can we trust AI? AI Agents and AGI. Use code insideai at https://incogni.com/insideai to get an ...

📺 InsideAI

👁️ 2.5M • 👍 44K • 💬 4K • ⏱️ 15:05 • 5d ago

---

**[Robots roaming grocery stores could put millions of retail jobs at risk](https://www.youtube.com/watch?v=OzrF9T08D98)**

NewsNation's Nancy Loo reports on the growing number of robots used at grocery stores to check inventory and restock items, ...

📺 NewsNation

👁️ 47K • 👍 400 • 💬 117 • ⏱️ 5:15 • 2d ago

---

**[This Cute Robot Has TWO NVIDIA Computers Inside 🤯#nvidia #robot](https://www.youtube.com/watch?v=EaWBrZ4qL2M)**

Meet Blue — this little robot is showing off some seriously impressive technology! NVIDIA's CEO demonstrates real-time ...

📺 VisionX Lab

👁️ 168K • 👍 5K • 💬 232 • ⏱️ 0:58 • 2d ago

---

**[Elon Musk&#39;s Humanoid Robot Bodyguard 👀 #elonmusk #shorts](https://www.youtube.com/watch?v=svFO2f6mXc4)**

Subscribe to VisionX Lab for more fascinating moments from Elon Musk, cutting-edge technology, AI, and the future. Disclaimer: ...

📺 VisionX Lab

👁️ 315K • 👍 4K • 💬 384 • ⏱️ 0:11 • 5d ago

---

**[Tesla Leaked Optimus 3 At Earnings Call | It&#39;s As Good As They Say](https://www.youtube.com/watch?v=gS1iOU_JnkA)**

Tesla has started production of Optimus on a line in Fremont, and on their third quarter earnings call Elon Musk said "there is no ...

📺 Ryan Shaw

👁️ 131K • 👍 2K • 💬 184 • ⏱️ 37:43 • 6d ago

---

**[These Transformers Turn Into Robots By Themselves 🤯](https://www.youtube.com/watch?v=Bf1OO5a9MjE)**

Original video credit: IG/@zeroframe_studio. This collection of interactive Robosen Transformers robots can transform completely ...

📺 History Seeker

👁️ 35K • 👍 836 • 💬 21 • ⏱️ 0:09 • 8h ago

---

**[OpenAI&#39;s First AI Robot Is Finally Happening (ChatGPT Gets a Body)](https://www.youtube.com/watch?v=BhdPuzza7i0)**

OpenAI is officially building its first humanoid robot, and Sam Altman has confirmed a major demonstration planned for 2027.

📺 MACHINEKIND

👁️ 43K • 👍 591 • 💬 46 • ⏱️ 13:33 • 3d ago

---

**[FIRST LOOK! New ULTIMATE Fafnir &amp; ASTRA Robot &amp; OPHAN Titan | WR - War Robots](https://www.youtube.com/watch?v=WGETP_IJpAw)**

Buying D-Gems? Use code *BeefyWR* on WR Webshop — it helps support the channel:) https://wr.my.games/Beefster War ...

📺 Beefy

👁️ 17K • 👍 359 • 💬 192 • ⏱️ 6:34 • 18h ago

---

**[Truck mode to Robot mode！MM02 Magnificent Mecha Optimus Prime A/B version transformation.](https://www.youtube.com/watch?v=vtvu9TFfWMw)**

Truck mode to Robot mode！MM02 Magnificent Mecha Optimus Prime A/B version transformation.

📺 Maximals Heart

👁️ 80K • 👍 2K • 💬 190 • ⏱️ 20:03 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

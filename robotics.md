---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-07T11:45:48.610998+00:00'
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

**Last Updated:** February 07, 2026 at 11:45 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Atlas, from Boston Dynamics, does gymnastics, lands on its toes, then performs a backflip.](https://www.reddit.com/r/robotics/comments/1qxdo57/atlas_from_boston_dynamics_does_gymnastics_lands/)**

From CyberRobo on 𝕏: https://x.com/CyberRobooo/status/2019598569909743755

1d ago

---

**[Birthday gift ideas for boyfriend (CS senior + humanoid robotics, practical not flashy)](https://www.reddit.com/r/robotics/comments/1qy80pk/birthday_gift_ideas_for_boyfriend_cs_senior/)**

My boyfriend is a computer science major and is about to graduate. He’s really into robotics, especially humanoid robots, and he currently works in a research lab where they’re building a humanoid that can catch objects. Most of what I see him doing is simulation and coding work on his computer. Last year I got him an Arduino kit, and he already has a toolkit, but he doesn’t really use either one much on his own (as far as I see). He’s pretty thrifty and values practicality over “cool” gadgets. For context, he uses a Mac and has a portable monitor that fits in his backpack. He doesn’t currently use an external keyboard or mouse, but I don’t think he cares much about those. I want to get him something he’ll genuinely use in his future work. Since he mostly works in teams through his lab/club (not solo at-home build projects), I’m not looking for another kit. Any gift ideas from people in CS/robotics, or partners of people in this field, that are truly useful and not gimmicky? Thank you!!

3h ago

---

**[Controlling UR12E remotely](https://www.reddit.com/r/robotics/comments/1qy9iz9/controlling_ur12e_remotely/)**

I’m working with the UR12E and trying to send movement commands from a desktop. currently using ROS/moveit. I’m creating paths on RViz and they are valid. When pressing “execute” the arm doesn’t move. Sometimes there are errors regarding tolerances (which I’m looking into) and other times it doesn’t return an error, but tells me the movement is planned. previous culprits have been the ros joint controller / ros scaled joint controller (scaled is now being used). has anyone faced similar issues? Keen to be pointed to some places in docs to understand further.

2h ago

---

**[CasADi → native GPU kernels → Pytorch / Cupy / C++ [Batch 100K + evaluations in ms]](https://www.reddit.com/r/robotics/comments/1qxy5p7/casadi_native_gpu_kernels_pytorch_cupy_c_batch/)**

Just pushed an update to casadi-on-gpu that lets you generate CUDA kernels directly from CasADi and call them from C++, PyTorch, or CuPy. Useful for MPC, sampling, system ID, and robotics pipelines at scale.

11h ago

---

**[MKS ODrive Mini + AS5047P SPI Encoder: OVERSPEED error when using startup_closed_loop_control](https://www.reddit.com/r/robotics/comments/1qy6rmk/mks_odrive_mini_as5047p_spi_encoder_overspeed/)**

Hey everyone, I'm working with an MKS ODrive Mini (firmware v0.5.1, based on ODrive v3.6) with an onboard AS5047P absolute SPI encoder and an Eagle Power 90kV BLDC motor. I've successfully calibrated the motor and can reliably enter closed-loop control mode manually, but I'm running into issues when trying to make it enter closed-loop automatically on startup. What Works: Manual calibration completes successfully Manual closed-loop entry works perfectly every time: ​ odrv0.axis0.error = 0 odrv0.axis0.requested_state = 8 # CLOSED_LOOP_CONTROL # Motor enters closed-loop with no errors The Problem: When I enable startup_closed_loop_control = True, the ODrive immediately throws an OVERSPEED error on power-up and fails to enter closed-loop mode. Current Configuration: # Encoder (AS5047P on GPIO7) odrv0.axis0.encoder.config.mode = 257 # ABS_SPI odrv0.axis0.encoder.config.cpr = 16384 odrv0.axis0.encoder.config.abs_spi_cs_gpio_pin = 7 odrv0.axis0.encoder.config.pre_calibrated = True odrv0.axis0.encoder.config.bandwidth = 100 # Motor odrv0.axis0.motor.config.pre_calibrated = True # Controller odrv0.axis0.controller.config.control_mode = 3 # POSITION_CONTROL odrv0.axis0.controller.config.input_mode = 1 # PASSTHROUGH odrv0.axis0.controller.config.vel_limit = 100 odrv0.axis0.controller.config.circular_setpoints = True # Startup odrv0.axis0.config.startup_motor_calibration = False odrv0.axis0.config.startup_encoder_offset_calibration = False odrv0.axis0.config.startup_encoder_index_search = False odrv0.axis0.config.startup_closed_loop_control = True # This causes OVERSPEED Errors on Startup: AxisError.CONTROLLER_FAILED MotorError.CONTROL_DEADLINE_MISSED ControllerError.OVERSPEED What I've Tried: Increased vel_limit from 50 to 100 to 200 - still fails Reduced encoder bandwidth from 1000 to 100 to 50 - still fails Enabled circular_setpoints to avoid position tracking issues Verified encoder mode is set to ABS_SPI (257) Confirmed all calibrations are marked as pre_calibrated = True Suspected Issue: I believe there's a race condition where the controller tries to enter closed-loop mode before the AS5047P SPI encoder has fully initialized and is providing stable readings, causing a spurious high velocity reading that triggers the overspeed protection. Questions: Is there a way to add a startup delay before startup_closed_loop_control executes? Are there specific encoder settings for the AS5047P on the MKS ODrive Mini that I'm missing? Is this a known firmware limitation with SPI encoders on ODrive v3.6-based boards? Should I consider updating the firmware, or is there a configuration workaround? Workaround: I can use a Teensy 4.1 with CAN bus to send the closed-loop command after a 3-second delay, which works perfectly. But I'd prefer the ODrive to handle this autonomously if possible. Any help would be greatly appreciated! Has anyone successfully used startup_closed_loop_control with an AS5047P encoder? Hardware: MKS ODrive Mini V1.0 Firmware: 0.5.1 (based on ODrive v3.6-56V) Encoder: AS5047P (onboard, SPI) Motor: Eagle Power 90kV BLDC Voltage: 8V-56V (running 3S-13S safe) EDIT: For anyone finding this later - the Teensy/microcontroller solution with a startup delay works flawlessly. Yes i used claude to summarize this (im a backend dev dont have much experience with robotics just wanted tot try it out)

5h ago

---

**[Ball-and-Socket… But for Locomotion, Enchanted Tools](https://www.reddit.com/r/robotics/comments/1qx3nuo/ballandsocket_but_for_locomotion_enchanted_tools/)**

1d ago

---

**[Does anyone have experience with finetuning Huggingface's SmolVLA model on SO-101?](https://www.reddit.com/r/robotics/comments/1qxm907/does_anyone_have_experience_with_finetuning/)**

Hello everyone! Recently I tried to test the SmolVLA model from a paper that HuggingFace published, that uses relatively small VLA model for Imitation Learning on a SO-101 arm. They have a library called LeRobot that has a lot of stuff to handle robots. First I tried to run a pretrained model, which didn't work. Then I tried finetuning the model on a dataset that I collected. I gradually moved from 30 episodes to 120 with a simple task of picking up a cube and putting it in the designated place. The robot still can't solve the task at all and frankly does not improve with the increase in data amount. So my question is the following: have anybody experimented with LeRobot + smolvla + SO-101? What is your experience? Did you manage to run it? Basically, how much more time can I expect to sink into this or should I switch to another model, or from a robot to a simulator first, or something else?

19h ago

---

**[Robotics engineer meets UX problems](https://www.reddit.com/r/robotics/comments/1qwo57d/robotics_engineer_meets_ux_problems/)**

Felt so excited to see the robot I've been working on getting this much attention. Guess I need to step up my UX game though :/

1d ago

---

**[Cartwheel Robotics Shutdown- What Do You Think?](https://www.reddit.com/r/robotics/comments/1qxf32f/cartwheel_robotics_shutdown_what_do_you_think/)**

Cartwheel Robotics shutting down is a reminder of how misaligned capital can be. Great teams struggle for funding while massive checks keep flowing elsewhere. Scott’s advice hits home: “No money is better than the wrong money.” https://preview.redd.it/ov7omrf40vhg1.png?width=716&format=png&auto=webp&s=b0ce7c7ceaa4607cfdc5de89775cfcddf883c3fe

1d ago

---

**[Open-source CI gate + offline debug packets (seeking pilot teams or hobbyist creators)](https://www.reddit.com/r/robotics/comments/1qxt7da/opensource_ci_gate_offline_debug_packets_seeking/)**

Hey everyone — I’m a CS student working on an open-source tool called PF Gate that is supposed to be a supplement to the process of robotics debugging. If you run sims/log replays and deal with “it worked yesterday / what changed?” regressions, PF Gate sits in CI and turns a run into: deterministic PASS / WARN / FAIL / QUARANTINE (CI-friendly exit codes) JUnit output so results show up directly in CI UI an offline report.html “debug packet” auditable receipts explaining exactly why it flagged a run (plus policy + artifact hashes for provenance) diff-as-gate mode so CI failures include regression context vs a baseline It runs locally/in CI (no log upload). If you already have your own logs (rosbags/MCAP/custom), the idea is to adapt them into a canonical trace.jsonl (adapter guide included). This is just a fun project to me. I hope that this can be of help to anyone. Thank you in advance for checking it out, and if you have any questions feel free to DM me. If you do use it, I would love feedback on what worked and what didn’t. Thank y’all!

🔗 [GitHub](https://github.com/QPFAI/PF-Gate) • 15h ago

---

---

## Google News: "robotics"

**[China is running the EV playbook on humanoid robots — and it’s working](https://restofworld.org/2026/china-humanoid-robots-unitree-agibot-tesla-optimus/)**

Rest of World • 2d ago

---

**[China Is Going All-In to Beat the U.S. on Humanoid Robots](https://www.wsj.com/tech/china-is-going-all-in-to-beat-the-u-s-on-humanoid-robots-b9c434d2?gaa_at=eafs&gaa_n=AWEtsqfjrDI5T_QPlFVs_40tpRH4hd9YrlvINdwUq3J14sxc1mZdsoh_WSyb&gaa_ts=6987295c&gaa_sig=YZNBPf6nY_Ak2fe-2KY77VCE0PE31WGBi_8us3klg8c6KkJNu2Vc-mtWRu5dZvhjZxso8_vD4640ndcFBgGMTw%3D%3D)**

The Wall Street Journal • 1h ago

---

**[I'm a 25-year-old founder who loves robots but too many humanoids are militant and creepy-looking. Things need to change—just look at Elon Musk](https://fortune.com/2026/02/05/25-year-old-robotics-founder-says-too-many-creepy-militant-look-at-elon-musk/)**

Who’s raising our robots? Teaching social norms in the age of humanoid robots.

Fortune • 1d ago

---

**[Walmart to add automation, robotics to Louisiana distribution center](https://www.supplychaindive.com/news/walmart-automation-robotics-opelousas-louisiana-distribution-center/811025/)**

The retailer’s $330 million investment, slated to start this year, is part of a larger effort to upgrade all 42 of its regional distribution facilities.

Supply Chain Dive • 1d ago

---

**[Hail our new robot overlords! Amazon warehouse tour offers glimpse of future](https://www.theguardian.com/technology/2026/feb/06/amazon-georgia-warehouse-tour-robots)**

At its new Stone Mountain, Georgia, facility, Roomba-like robots shuffle between stacks, another adds shipping labels while another arranges packages in pallets

The Guardian • 23h ago

---

**[ETM brings its transverse flux motor technology to robotics](https://www.therobotreport.com/etm-brings-its-transverse-flux-motor-technology-to-robotics/)**

ETM said its TFM technology enables OEMs to simplify mechanical designs, reduce costs, and achieve performance benchmarks.

The Robot Report • 2d ago

---

**[Making robots useful and affordable will need better motors](https://www.bbc.com/news/articles/c5y46356zzyo)**

Firms are working to make the motors that drive robots more efficient and cheaper.

BBC • 1d ago

---

**["Robots Need Your Body": New Site Lets AI Rent Human Labour](https://www.ndtv.com/feature/robots-need-your-body-new-site-lets-ai-rent-human-labour-10960601)**

Rentahuman.ai is a new marketplace where AI software acts as the employer, hiring humans to perform physical "real-world" tasks, effectively turning people into an on-demand service layer for autonomous agents.

NDTV • 20h ago

---

**[Soft robots can now be 3D printed to move exactly as designed](https://interestingengineering.com/ai-robotics/harvard-3d-printing-soft-robots-shape-morphing)**

Harvard engineers 3D print soft robots with built-in air channels that bend and change shape predictably when inflated.

Interesting Engineering • 15h ago

---

**[Apple Teaching Swift and Robotics Across Its India Supply Chain](https://www.macrumors.com/2026/02/04/apple-teaching-swift-and-robotics-in-india/)**

Apple today announced a new Education Hub in Bengaluru as part of an expanded effort to provide technical training and skills development for employees across its supply chain in India. Apple said the new Apple Education Hub in Bengaluru will serve as a centralized training and coordination facility for supplier employees in India, marking the company's first education hub of its kind in the country.

MacRumors • 2d ago

---

---

## YouTube Videos: "robotics"

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 164K • 👍 4K • 💬 687 • ⏱️ 13:31 • 2d ago

---

**[Yann LeCun Just Called Out the Entire Robotics Industry](https://www.youtube.com/watch?v=ArG8GiIHmjE)**

Checkout Free Community: - https://www.skool.com/theaigridcommunity Follow Me on Twitter https://twitter.com/TheAiGrid ...

📺 TheAIGRID

👁️ 19K • 👍 597 • 💬 193 • ⏱️ 13:22 • 4d ago

---

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 23K • 👍 201 • 💬 41 • ⏱️ 1:21 • 6d ago

---

**[He Tried to Troll a Tesla Robot. The Robot Trolled Him Back 🤯🍿](https://www.youtube.com/watch?v=8sw7pOaOkik)**

Tesla's Optimus Gen 2 demonstrates its advanced low-latency tracking and tactile precision by playfully interacting with a person ...

📺 Batya Feuer

👁️ 9K • 👍 172 • 💬 13 • ⏱️ 0:25 • 2d ago

---

**[Capybara Rebuilds a Robot Lion After Sabotage vs Brianna! 🦁🤖 #capybara](https://www.youtube.com/watch?v=Pwu7G4jC3FA)**

Capybara's golden robot lion was sabotaged by Brianna before the big competition! But Cappy didn't give up — he rebuilt ...

📺 CapyEscapes

👁️ 842 • 👍 29 • 💬 5 • ⏱️ 0:59 • 15m ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=eDubNRxWb88)**

📺 Lin of Brant robot 

👁️ 23K • 👍 53 • 💬 1 • ⏱️ 0:19 • 4d ago

---

**[Bolt — world&#39;s fastest humanoid robot from Chinese firm MirrorMe](https://www.youtube.com/watch?v=iws-5C-qPno)**

MirrorMe launched the humanoid robot — Bolt — on Monday, achieving a peak running speed of 10 meters per second in ...

📺 CnEVPost

👁️ 32K • 👍 306 • 💬 79 • ⏱️ 1:09 • 4d ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 76K • 👍 506 • 💬 36 • ⏱️ 0:06 • 3d ago

---

**[ChatGPT in a kids robot does exactly what experts warned.](https://www.youtube.com/watch?v=LF4o4Z01Q0I)**

AI in a kids toy does what experts warned. Can we trust AI? Get Inside AI's exclusive Nord VPN deal here: ...

📺 InsideAI

👁️ 766K • 👍 32K • 💬 5K • ⏱️ 15:47 • 6d ago

---

**[IShowSpeed Started Beefing with an AI Robot on Stream 😂](https://www.youtube.com/watch?v=8ga7WPMN6GE)**

Credits: IShowSpeed Live ishowspeed started beefing with an ai robot on stream after the robot responded back with ...

📺 WClipMedia

👁️ 624K • 👍 4K • 💬 24 • ⏱️ 0:26 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

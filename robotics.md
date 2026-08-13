---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-13T18:27:10.695351+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- news
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** August 13, 2026 at 18:27 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A robot claw to spin a globe on my desk](https://www.reddit.com/r/robotics/comments/1vn4psz/a_robot_claw_to_spin_a_globe_on_my_desk/)**

I was obsessed when I first saw Mark Setrakian’s claw robot so I decided to make my own. Here it’s running in standalone mode using an Arduino, 12 Dynamixel XL430s and 4 potentiometers to control the globe’s speed/direction, height, width, and depth of each offset step. I’ve done more movements using a Python based GUI on my laptop but that requires a usb connection. Full video on my build with links to STLs, code and parts list here: https://youtu.be/pEU04FVNeZw Next project is a Leaper from Arc Raiders. Just need to figure out how to trigger a rocket to make a robot spider jump.

10h ago

---

**[Hexapod Spider Robot (Half-finished)](https://www.reddit.com/r/robotics/comments/1vn17c3/hexapod_spider_robot_halffinished/)**

(Note: Every component is made from scratch in Fusion). I originally planned to add a lightweight robot arm at the top center of the robot, after the calculations... (Inspiration comes from MakeYourPets)

13h ago

---

**[Building a 5-digit Recognition System on ESP32-S3](https://www.reddit.com/r/robotics/comments/1vn5cml/building_a_5digit_recognition_system_on_esp32s3/)**

I've been experimenting with running a complete digit recognition system directly on an ESP32-S3 using TensorFlow Lite Micro. The goal was to recognize 5-digit readings (such as meter displays) completely on-device without relying on a PC or cloud inference. The hardware I used was an ESP32-S3 development board with an onboard camera and AMOLED display (Makerfabs MaTouch ESP32-S3 AI Camera), but the workflow should apply to similar ESP32-S3 camera boards. How it works: Data Collection: Flashed a utility firmware to capture camera frames aligned via an on-screen yellow bounding box, outputting labeled image pairs and a label.csv. Model Training & INT8 Quantization: Trained a lightweight CNN model and quantized it to INT8 to run within the ESP32-S3's memory limits. On-Device Inference: Compiled the quantized model directly into the ESP-IDF binary and deployed it back to the board. The result is surprisingly reliable—it reads all 5 digits cleanly in real time. Hardware & Tech Stack: Board: Makerfabs MaTouch ESP32-S3 AMOLED AI Camera Framework: ESP-IDF + TensorFlow Lite Micro Tooling: Custom Python tools for capture & quantization I put together a detailed write-up covering the complete workflow on GitHub, in case anyone wants to reproduce or adapt it for a similar project. I'd also love to hear how others approach digit recognition with TensorFlow Lite Micro. Have you found any effective ways to improve accuracy or speed up the data collection process?

9h ago

---

**[Folding a towel: hands vs code, and the hands still win](https://www.reddit.com/r/robotics/comments/1vn4r8r/folding_a_towel_hands_vs_code_and_the_hands_still/)**

This week a student came by and tried our teaching arms, both hands on two of them, teleoperating our control arms. First try, the arms folded the towel. That's exactly why we still keep teleoperation around. You don't write a line of code. You just move. The teaching arms are linked to the control arms, so your motion gets copied onto them in real time. Which means someone with zero experience can do the kind of thing that would otherwise take ages to hand-program. Watching him work, two things hit me. One: this is still the fastest way we have to pull real manipulation data. Fabric is the hardest to deal with. No fixed grasp point, and it keeps sliding off to the side. A human hand just knows how to teach it the right move. Two: it's a straight check on whether the motion actually holds up. If a person can't move the arm cleanly themselves, all the algorithm and programming in the world probably won't fix it. That's why the towel became our test. Soft. Slippery. Never the same twice. And honestly, if you want a robot to fold a towel, the fastest way I know is still a human on the teaching arms. The models haven't beaten that trick yet.

10h ago

---

**[SLAM Camera Board + Obstacle Mapping](https://www.reddit.com/r/robotics/comments/1vmfavq/slam_camera_board_obstacle_mapping/)**

This is yet another update from my project. Mighty Camera runs VIO on-device realtime in a tiny package. This gives us accurate camera motion. Using that + the camera feed, the SDK estimates depth and builds a 3D map of obstacles around it. This means a robot or drone can use Mighty for things like: - Collision avoidance - Motion planning - Autonomous navigation No stereo camera or depth sensor needed. Just Mighty’s global shutter camera + IMU.

1d ago

---

**[Looking for study partners — robotics software engineering (ROS2, C++, SLAM)](https://www.reddit.com/r/robotics/comments/1vmd52w/looking_for_study_partners_robotics_software/)**

Recent CS/BCA grad here, actively job hunting for robotics SWE roles. Been building a TurtleBot + ROS2 Humble project (Docker, React dashboard, Nav2, Gazebo sim) and want to go deeper on C++, Linux, and SLAM with people who are serious about it. Thinking a small group (Discord/weekly calls) where we: Work through ROS2 concepts and share resources Review each other's projects/code Mock interview each other for robotics SWE roles Keep each other accountable If you're learning robotics software (student, self-taught, or between jobs), drop a comment or DM. Open to remote/India-based folks especially, but anyone's welcome.

1d ago

---

**[I built a local web app for curating SO-101 datasets across v2.1, v3.1, framerates, and camera setups](https://www.reddit.com/r/robotics/comments/1vn3y5a/i_built_a_local_web_app_for_curating_so101/)**

I've been training Lingbot-va and Dreamzero lately. For anyone who doesn't know, those need a lot of diverse data, both in terms of environment and play data. That pushed me toward the huge pool of SO-101 datasets that already exist for VLA and ACT training. The problem is those datasets are a mess to combine. Most of them are repetitive, and the task descriptions are generic. They sit on different versions, v2.1 or v3.1. Different framerates, different quality, different camera angles. And at the end you still have to balance the whole thing before it's usable. So I built Dataset Assembly Studio, a local web app that runs over a folder of LeRobot datasets and takes them to a verified v2.1 export. The flow is a set of tabs. Sources, output contract, camera mapping, joint mapping, episodes, tasks, balance, preflight, export. It validates every source before it can be used. Invalid parquet, missing metadata, single-camera recordings, and episodes under two seconds get rejected up front. Camera views can be previewed before mapping, one to wrist and one to a second canonical camera. The six SO-101 joints for both action and observation.state are mapped automatically, with manual correction when a source uses another order. Curation works one dataset at a time. You stage episodes with gallery checkboxes, load all camera views for a focused episode, edit final prompts, and save approved checkpoints. Source files are never modified, all state lives under .dataset_studio/. Global balance groups tasks by a local embedding and caps the episode count per task group. Then a blocking preflight checks camera, joint, schema, media, duration, prompt, destination, and checkpoint compatibility before export. The export runs in the background, rebuilds indices, and writes normalized v2.1 data with exactly two camera streams. A .tar.gz is only prepared if you ask for it. Everything runs locally, no auth, no cloud. A Groq API key is optional just for naming task groups, everything else works without it. Repo: github.com/mekala-2405/dataset-assembly-studio Static demo : https://projects.mharsh.me/data_assembly_studio check out my portfolio and other projects : mharsh.me Walkthrough : https://www.youtube.com/watch?v=bJFGVuzufwQ If you've been through the same dataset grind, I'd love to hear how you handle it and some feedback . The attached video might sound like AI-Slop please bear with it .

10h ago

---

**[Why Real-World Movement Is So Hard for Exoskeletons](https://www.reddit.com/r/robotics/comments/1vmhsz8/why_realworld_movement_is_so_hard_for_exoskeletons/)**

Exoskeletons can handle predictable movements pretty well. Everyday movement is a lot messier. Kathryn Zealand of Skip explains why something as simple as bending down can create a control problem, and how the company is using machine learning to better understand what a person is actually trying to do. Full ep: https://www.youtube.com/watch?v=jDR8xeU-GFQ

1d ago

---

**[Has anyone deployed VLA-based robots in production?](https://www.reddit.com/r/robotics/comments/1vmeaqq/has_anyone_deployed_vlabased_robots_in_production/)**

There's of course a lot of hype around the new robot foundation models, but seems that there are not many real deployments. Has anyone tried making this things work in production? Which tasks did you try? Did you have to end up collecting a lot of data to fine tune the model?

1d ago

---

**[I built a Raspberry Pi and ESP32-based USV — first system integration and field test](https://www.reddit.com/r/robotics/comments/1vmekgh/i_built_a_raspberry_pi_and_esp32based_usv_first/)**

Hi everyone, I’ve been developing a small unmanned surface vehicle called BN-USV, and I recently completed its first system integration and field test. The hull was designed in FreeCAD and 3D-printed in PETG. The onboard system uses a Raspberry Pi 5 for navigation, sensor processing, data logging, and mission-level control, while an ESP32-S3 handles real-time thruster control and safety-related functions. The vehicle uses two independently controlled thrusters and steers through differential thrust. It collects navigation data from GPS, IMU, and magnetometer sensors. Waypoint-based autonomous navigation is planned for the next stage of development. The main goals of this first field test were to evaluate: Hull buoyancy and stability Manual RC control and steering response Communication between the Raspberry Pi and ESP32 Navigation sensor data collection Power, vibration, and other system issues under real operating conditions This was not yet a polished autonomous-navigation demonstration. It was an early system integration test conducted before implementing and validating waypoint navigation. The vehicle also behaved quite differently on the water than I had expected from indoor testing. However, the test provided useful data and revealed several areas that need improvement, particularly sensor calibration, heading estimation, control response, and the onboard electronics. I put together a video showing both the development process and the vehicle’s first field test: https://youtu.be/Lz2eOEANyZo I’m now developing a more modular second version of the platform, together with improved navigation and waypoint control. The long-term goal is to develop BN-USV into a practical modular platform for marine research, education, environmental monitoring, and autonomous-navigation experiments. Full disclosure: I’m developing BN-USV as part of BrillNova, with the long-term goal of turning it into a commercial modular hardware platform. The software and development process will remain open and publicly documented. I’d be very interested to hear feedback, especially from anyone who has worked with small USVs, autonomous boats, marine robotics, sensor fusion, or differential-thrust control. Thanks!

1d ago

---

---

## Google News: "robotics"

**[Workers Are Teaching AI-Powered Robots to Take Over Their Jobs](https://www.bloomberg.com/news/features/2026-08-12/thousands-of-india-workers-are-helping-ai-firms-train-robots-to-replace-them)**

Robotics companies are competing to collect videos of humans stitching shoes and welding steel to give their machines new skills.

Bloomberg.com • 21h ago

---

**[Humanoid robots trained on 1M hours of human video achieve up to 90% task success](https://interestingengineering.com/ai-robotics/dyna-robotics-dyna-2-human-video-robot-training)**

Dyna Robotics trains its new robot model on one million hours of human video to improve physical task performance.

Interesting Engineering • 2d ago

---

**[America Wants to Make Its Own Humanoid Robots. That Won’t Be Easy.](https://www.nytimes.com/2026/08/13/business/humanoid-robot-us-china.html)**

The New York Times • 9h ago

---

**[Naval Academy Integrates Robotics, Autonomous Systems Into Summer Training](https://www.war.gov/News/News-Stories/Article/Article/4569991/naval-academy-integrates-robotics-autonomous-systems-into-summer-training/)**

The Department of War provides the military forces needed to deter war and ensure our nation's security.

U.S. Department of War (.gov) • 23h ago

---

**[Canadian-based robotics company opens 1st U.S. facility in Lexington, bringing 111 jobs](https://www.lex18.com/news/covering-kentucky/canadian-based-robotics-company-opens-1st-u-s-facility-in-lexington-bringing-111-jobs)**

A Canadian-based automation and robotics company has officially opened its first U.S. manufacturing operation in Lexington.

LEX 18 News • 1d ago

---

**[The Latest Robotics IPO is 8000X Oversubscribed. These ETFs Could Take Off if Humanoid Robotics Are The Next Big Thing.](https://finance.yahoo.com/markets/stocks/articles/latest-robotics-ipo-8000x-oversubscribed-225120337.html)**

A Chinese humanoid robotics IPO just shattered demand records, and the shockwave is already hitting a handful of niche ETFs built exactly for this moment. Whether that momentum holds depends on two wildcards most investors are not watching closely enough.

Yahoo Finance • 19h ago

---

**[Uber surprised robotics company Serve by selling its entire stake](https://techcrunch.com/2026/08/11/uber-surprised-robotics-company-serve-by-selling-its-entire-stake/)**

The divesture comes comes as the two once-tight companies have started to diverge on the business side.

TechCrunch • 1d ago

---

**[FCC robot ban: Can you still purchase new products?](https://mashable.com/tech/fcc-bans-robots-vacuums-what-to-know)**

Expect more banned products in the future, experts warn.

Mashable • 3h ago

---

**['A huge win': Utah State University, technical colleges partner to bolster robotics workforce](https://www.ksl.com/article/51608468/a-huge-win-utah-state-university-technical-colleges-partner-to-bolster-robotics-workforce)**

Utah State University is expanding access to robotics and automation education through a new degree program aimed at turning hands-on experience and training into college credits.

KSL.com • 1d ago

---

**[San Mateo County Could Be First to Regulate Humanoid Robots for Commercial Use](https://www.kqed.org/news/12094873/san-mateo-county-could-be-first-to-regulate-humanoid-robots-for-commercial-use)**

Researchers say that humanoid robots have a long way to go before they are officially ready for work.

KQED • 1d ago

---

---

## YouTube Videos: "robotics"

**[3 Robotics Stocks Under $10 With Massive Upside](https://www.youtube.com/watch?v=8a9dMO3glNE)**

Thanks to Monarch for partnering with me! Start your free trial and get 50% off your first year of total money clarity using my link ...

📺 MarketBeat

👁️ 31K • 👍 940 • 💬 42 • ⏱️ 25:41 • 19h ago

---

**[Something Is Seriously Wrong With This Rescue Robot...](https://www.youtube.com/watch?v=shGN84z4SpI)**

We know Spiritually, we are either influenced by God, or evil. Well this new robotic creation has many asking why the robot looks ...

📺 Aaron Page 

👁️ 11K • 👍 1K • 💬 202 • ⏱️ 13:50 • 2d ago

---

**[I spent 3 days at MIT... the robot hype is worse than you think](https://www.youtube.com/watch?v=aB5LGrHISqY)**

Omnigent is an open source meta-harness to run all your AI agents in one place. Try it free - https://bit.ly/4fXzeo8 I spent last week ...

📺 Fireship

👁️ 866K • 👍 21K • 💬 2K • ⏱️ 7:02 • 2d ago

---

**[Chelsea Finn: This is the State of the Art in Robotics](https://www.youtube.com/watch?v=cRZNwgvcWUg)**

Robots can already fold laundry, make espresso, clean kitchens, and assemble things. The harder problem is getting them to do ...

📺 Y Combinator

👁️ 16K • 👍 481 • 💬 15 • ⏱️ 58:18 • 1d ago

---

**[Why the US government is trying to ban this Chinese dancing robot | Explainer](https://www.youtube.com/watch?v=RzqtTunpXlE)**

The Federal Communications Commission on 28 July announced a ban on humanoid robots from China including the popular ...

📺 Guardian News

👁️ 35K • 👍 415 • 💬 107 • ⏱️ 3:48 • 2d ago

---

**[MASSIVE robotics deal pushes physical AI into US shipbuilding](https://www.youtube.com/watch?v=fhzTrAfskQk)**

GrayMatter Robotics CEO Ariyan Kabir explains how AI-powered robots could supercharge U.S. shipbuilding, boost American ...

📺 Fox Business Clips

👁️ 37K • 👍 531 • 💬 105 • ⏱️ 7:05 • 2d ago

---

**[Robot Teachers are Canceled.](https://www.youtube.com/watch?v=eTCfPsC1yN4)**

📺 Ben Esherick

👁️ 638K • 👍 30K • 💬 782 • ⏱️ 0:35 • 6d ago

---

**[$1.4 Billion Robot &quot;Died&quot; on Stage](https://www.youtube.com/watch?v=7KTiXWvw7mc)**

FREE GUIDE: The Content Creator's AI Blueprint – https://FirstMovers.ai/blueprint/ A robot just raised its fist at a Qualcomm ...

📺 Julia McCoy

👁️ 60K • 👍 2K • 💬 237 • ⏱️ 9:02 • 5d ago

---

**[Satyress Threehalves Is the Most Terrifying Robot Yet #Robotics #AI #Tech](https://www.youtube.com/watch?v=LLuFDQV7Js0)**

The Satyress Threehalves robot looks absolutely terrifying. This seven-foot-tall centaur robot has four legs, a humanoid body, and ...

📺 Custom Adventurist

👁️ 51K • 👍 3K • 💬 217 • ⏱️ 1:02 • 6d ago

---

**[This Transformer Robot Went To The Moon](https://www.youtube.com/watch?v=uargNhK22vs)**

This tiny transformer robot was built for the moon… It's about the size of a baseball, BUT INSIDE…are cameras, two wheels, and a ...

📺 Cleo Abram

👁️ 1.0M • 👍 54K • 💬 685 • ⏱️ 0:32 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

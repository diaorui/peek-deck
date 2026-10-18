---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-10-18T18:47:50.986914+00:00'
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

**Last Updated:** October 18, 2026 at 18:47 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I Built a Drone With Only One Motor – And a Poor Man's High Speed Camera](https://www.reddit.com/r/robotics/comments/1x8zyvp/i_built_a_drone_with_only_one_motor_and_a_poor/)**

I've been working on an under-actuated drone that can fly with only one motor for the last few months. The propeller hub is 3D printed out of PPA-CF and has a hinge, so when the motor accelerates the blades lag behind and one pitches up while the other pitches down. By pulsing the motor torque 300 times a second, timed to the rotor angle, the drone controls its pitch and roll with the same motor that produces its thrust. Along the way I also built a "poor man's high speed camera" - a camera flash synced to my camera and motor controller, so I could take images of the propeller at precise angles to analyze its behavior. The mechanical simplicity hides a lot of software. At almost 20,000 RPM, a 0.2 ms control loop is already 20 degrees of rotation late, so I wrote custom firmware for the motor controller to compute the torque pulses on board. The body also slowly spins, so the drone gets its heading from an infrared "lighthouse" beacon in the corner of the room that it sees once per revolution. The full video explaining how it all works is available on youtube: https://www.youtube.com/watch?v=Ndftcft6XhU The code and CAD are open source on github: https://github.com/jyjblrd/single-propeller-drone

8h ago

---

**[Development over 8 months yay](https://www.reddit.com/r/robotics/comments/1x90h84/development_over_8_months_yay/)**

I posted here 8 months ago and am only now posting again, haha. This is how I've improved over the past 8 months: MK5 V1: The appearance was impressive, but... Yes, I lacked torque. MK5 V2: Hmm... MK6 V1: it walks!! it walks!! it walks!! 🐕🐕 MK6 V2: Laser cut leg Hell yeah😎😎 Two-arm guy Two-leg guy : w.i.p DMs are welcome, and those who really want to see them can do so in Seoul😎 T h a n k y o u !

7h ago

---

**[Spot stepped on it.](https://www.reddit.com/r/robotics/comments/1x93wc2/spot_stepped_on_it/)**

MK6 got stepped on by Spot. It said it didn't hurt much lol. I think this was the evening of the day I developed the MK6 V2 and participated in the Maker Faire. 2026.09.19 😎👍

4h ago

---

**[Humanoid robot Digit 5 targets 20-hour workdays with 9-minute charging](https://www.reddit.com/r/robotics/comments/1x90sfg/humanoid_robot_digit_5_targets_20hour_workdays/)**

Agility Robotics says its upcoming Digit 5 humanoid will use Nyobolt batteries to deliver 90 minutes of operation after a nine-minute charge. The targeted 10:1 run-to-charge ratio could support more than 20 productive hours per day in warehouses and manufacturing facilities. Early-access deployment is planned for the first half of 2027, but the company has not yet disclosed the battery capacity, cycle-life rating, or independent real-world test results.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/humanoid-robot-digit-5-workdays) • 7h ago

---

**[3D Printed Rocker-Bogie Mars Rover | ESP32-CAM | 6-Wheel Robotic Platform](https://www.reddit.com/r/robotics/comments/1x9666z/3d_printed_rockerbogie_mars_rover_esp32cam_6wheel/)**

More info about cad and STL https://cults3d.com/en/3d-model/game/3d-printed-rocker-bogie-mars-rover-esp32-cam-6-wheel-robotic-platform

3h ago

---

**[DIY robot arm that plays Nine Men's Morris](https://www.reddit.com/r/robotics/comments/1x8lkji/diy_robot_arm_that_plays_nine_mens_morris/)**

This little robot arm was designed for educational purposes. The goal was to build a small, simple 3D-printed arm capable of precise, smooth movements. The first version has 4 DOF, with room for future expansion. The J1, J2 and J3 joints use factory-made POM gears from the main gear of a Tarot 450 model helicopter. These mesh with the factory-made metal gears on the round NEMA 14 stepper motors, which are designed for 3D printer extruders. Torque is transmitted to the J3 joint through a GT2 belt, allowing all the steppers to remain at the base of the arm. J4 is driven by an RC servo. It has some backlash, which could be eliminated with spring preload. The controller is an inexpensive 3D printer board, the BTT SKR Pico, equipped with quiet TMC2209 stepper drivers. These can detect motor stalls, allowing sensorless homing. The gripper is made of flexible TPU. The servo pulls a central filament, causing the fingers to bend inward. It's a very simple design that tolerates small positioning errors without putting much strain on the servo. To make the programming more interesting, we set ourselves the goal of building a robot that could play Nine Men's Morris by recognizing its opponent's moves using a camera. This video was recorded the first time the arm was able to play a game. Its movements will become smoother and much faster as development continues. We developed custom Arduino-based firmware for the Pico board. By feeding motion commands into a queue, it allows the arm to move continuously, with smoothly rounded transitions between movements. All higher-level tasks are handled by Python code running on a PC. When powered on, the arm first moves to its home position and then moves out of the camera's field of view. The software calibrates itself using the camera image and identifies the positions on the board. During the game, it watches the opponent's moves, calculates a response, and executes its own move.

21h ago

---

**[Massachusetts Robotics Map](https://www.reddit.com/r/robotics/comments/1x86iow/massachusetts_robotics_map/)**

They say robotics moved west, but Boston didn’t get the memo. 🦞 The Massachusetts ecosystem is one of the world's leading hubs for robotics, combining top research, companies, and deep-tech investment. At its core are Massachusetts Institute of Technology (MIT) and Harvard University which produce world-class researchers, engineers, and robotics startups. Many of today's leading robotics companies trace their roots back to these universities. The region is also home to companies like Boston Dynamics, whose work has inspired advances in humanoid and mobile robots. Around these companies, a dense network of suppliers, experienced engineers, entrepreneurs, and investors has developed, making it easier for new startups to build and scale. Massachusetts also has one of the strongest deep-tech funding ecosystems in the world, with venture capital firms that understand robotics, AI, and hardware. The Massachusetts robotics ecosystem is further strengthened by leading research organizations such as Toyota Research Institute and RAI Institute, which are advancing AI, dexterous manipulation, and next-generation robotics while attracting world-class researchers and engineers. Not to mention initiatives like MassRobotics which is home to so many great robotics companies. In simple terms: → You need world-class robotics talent → recruit from MIT and Harvard. → You want experienced robotics engineers → hire people who have built robots at top companies. → You need funding → access investors with decades of experience backing deep-tech startups.

1d ago

---

**[My robot dog kept finding new ways to move across gravel](https://www.reddit.com/r/robotics/comments/1x8h4ga/my_robot_dog_kept_finding_new_ways_to_move_across/)**

Quaddle rolling and surviving a patch of loose gravel. Whenever a move fails, it just flips itself back up instead of staying down — driven by Auto Mode on its built-in IMU (tilt, fall, lift/drop, and shock detection all handled the same way). What terrain would you want to test a small quadruped's movements against?

1d ago

---

**[Same payload, same reach, very different behavior in production — wrist geometry is why](https://www.reddit.com/r/robotics/comments/1x8w8h0/same_payload_same_reach_very_different_behavior/)**

I keep running into robot selection discussions where the word "configuration" gets used for two completely different things, and the mixup causes real problems downstream. Under ISO 9787, configuration technically means the set of joint values that determines the robot shape at any time. In selection discussions, engineers usually mean the mechanism architecture: inline wrist, offset wrist, or the cobot-style layout with parallel middle axes. Those are different questions, and a datasheet will not sort them out for you. How I break it down: The first three joints place the wrist center. The last three set tool attitude. If joints 4, 5, 6 intersect at one point, you have the classical inline wrist: partially decoupled position and orientation, analytic inverse kinematics, and decades of offline programming support. That is a big reason the PUMA-type architecture still dominates industrial robotics. Offset wrists give up that geometric convenience for clear process reasons: more orientation envelope and better obstacle avoidance for long tools such as spray guns, torches, and abrasive heads. The cost lands in IK complexity, singularity analysis, and trajectory continuity. Cobot layouts reorder the middle axes (2, 3, 4 parallel) around compact joint modules, not around the classical wrist-center geometry. Fine for light tending, screwdriving, and lab automation, but it should not be treated as identical to the traditional industrial arm. The layer most people skip: one TCP pose on a typical inline-wrist robot can correspond to up to eight IK solutions. Front/back, elbow-up/elbow-down, flip/no-flip. A lot of "programming problems" are wrong-branch problems for the path, not wrong-robot problems. And singularity behavior follows the geometry, not the catalog page. Shoulder, elbow, and wrist singularities all shift when the wrist geometry changes. Question for people who do this for a living: do you evaluate posture-branch availability during selection, or does it usually surface at commissioning? I wrote up the full breakdown with the geometric details here, if useful: https://zanerobotics.substack.com/p/3-serial-six-axis-robot-arm-configurations?r=6ysx3o

12h ago

---

**[PCB mount servo drives vs traditional panel mount for compact robotic joints](https://www.reddit.com/r/robotics/comments/1x8w5ms/pcb_mount_servo_drives_vs_traditional_panel_mount/)**

i Want to know how roboticists here handle the packaging headaches on tight builds.Panel mounted drives make servicing and thermal heatsinking easy, but routing high-current motor phases and encoder lines through 6 articulated joints is a nightmare. Lately we’ve looked at ditching the central cabinet and dropping miniature PCB mount drives (like Elmo and Synapticon) right onto custom joint carrier boards. Is the wiring reduction worth the inevitable thermal dissipation and serviceability trade-offs?

12h ago

---

---

## Google News: "robotics"

**[Amazon Has Now Deployed Over 1 Million Robots, Which Is Bad News for Its 1.5 Million Workers](https://futurism.com/future-society/amazon-robotics-automation-warehouse-labor-safety)**

Amazon's record-breaking robotics deployment is squeezing its human warehouse workers in more ways than one.

Futurism • 1d ago

---

**[Robotics Startup With Rivian Ties Gets Former Ford EV Chief, Tesla Exec](https://www.wsj.com/livecoverage/stock-market-today-bank-earnings-10-13-2026/card/rivian-s-robotics-spinoff-gets-former-ford-ev-chief-tesla-exec-NxULz4c3VCFHq5zFaOIy)**

WSJ • 4d ago

---

**[Robots could boost US manufacturing as America races to keep pace with China, expert says](https://www.foxbusiness.com/technology/robots-could-boost-us-manufacturing-america-races-keep-pace-china-expert-says)**

A Path Robotics executive told FOX Business that automation will be critical to expanding U.S. manufacturing as worker shortages persist and China moves faster to adopt robotics.

Fox Business • 2d ago

---

**[Fincantieri to invest $100 million in robotics, artificial intelligence at shipyards](https://www.masoncountypress.com/2026/10/17/fincantieri-to-invest-100-million-in-robotics-artificial-intelligence-at-shipyards/)**

MARINETTE, Wis. — Fincantieri, one of the world’s largest shipbuilders, announced plans to invest nearly $100 million in robotics, artificial intelligence and advanced automation at its shipyards around the world, including its three facilities in Wisconsin. The Italian-based company announced Oct. 15 that it was expanding its BOOST² — The Shipyard of the Future program, an initiative launched three years ago to develop and introduce new technologies into shipbuilding operations. The investment is part of the company’s 2026-2030 industrial plan. More than 450 employees at 13 shipyards worldwide have participated in the program, including employees at Fincantieri Marinette Marine and the company’s Wisconsin System of Shipyards. Fincantieri operates three Wisconsin facilities: Marinette Marine in Marinette, Bay Shipbuilding in Sturgeon Bay and ACE Marine in Green Bay. Marinette Marine specializes in military shipbuilding, including vessels for the U.S. Navy. Bay Shipbuilding constructs, repairs and converts commercial vessels, including Great Lakes freighters. ACE Marine specializes in aluminum vessels for military and commercial applications. The modernization program focuses on integrating artificial intelligence with robotics to improve production efficiency, workplace safety and construction quality. One of the technologies being developed is known as Physical AI, which allows intelligent robotic systems to interact with their […]

MasonCountyPress.com • 1d ago

---

**[Delivery Robots Accused Of Scanning Customers’ Faces, Sharing Biometric Data](https://blockclubchicago.org/2026/10/16/delivery-robots-accused-of-scanning-customers-faces-sharing-biometric-data/)**

Block Club Chicago • 1d ago

---

**[Chinese startup DexForce trains humanoid robots using virtual data to slash costs](https://www.reuters.com/technology/chinese-startup-dexforce-trains-humanoid-robots-using-virtual-data-slash-costs-2026-10-15/)**

Reuters • 3d ago

---

**[US humanoid robot Digit 5 targets 20-hour workdays with 9-minute charging](https://interestingengineering.com/ai-robotics/humanoid-robot-digit-5-workdays)**

Agility’s Digit 5 humanoid robot targets over 20 hours of daily work using a Nyobolt battery that delivers a 90-minute runtime.

Interesting Engineering • 22h ago

---

**[OpenAI Is Building A Humanoid Robot, But The Body Isn't The Real Challenge](https://www.engadget.com/2285040/openai-humanoid-robot-sam-altman-statement-real-challenge/)**

With Tesla and XPENG already working on humanoids, OpenAI CEO Sam Altman says creating the 'brain' is more difficult than building the robots themselves.

Engadget • 19h ago

---

**[Chinese robotics firms race to roll out components and data systems, helping robots perceive, understand, interact with real world](https://www.globaltimes.cn/page/202610/1372460.shtml)**

At the Humanoid Robot Data Training Center in Beijing's western Shijingshan District, dozens of robots stood in their workrooms, learning how to pick up an object steadily and quickly. This is not a simple task - the robot must

Global Times • 13h ago

---

**[Bioinspired robot airdrops into remote waters via morphing wing-sail](https://newatlas.com/robotics/albatross-robot-sail-seed-boat/)**

“Fall like a maple seed, sail like a boat” sounds like advice from legendary heavyweight boxer Muhammad Ali. In reality, it describes a new robotic platform scientists have created for fast, long-term deployment to monitor remote waters.

New Atlas • 23h ago

---

---

## YouTube Videos: "robotics"

**[Tesla Reveals Major New Optimus Robot Update](https://www.youtube.com/watch?v=oy8mzP_y2H4)**

Remove your personal information online with Delete Me using my link https://joindeleteme.com/TESLASPACE20 - And enter ...

📺 The Tesla Space

👁️ 88K • 👍 3K • 💬 154 • ⏱️ 13:59 • 3d ago

---

**[Robots That Predict the Future: Dyna-2 &amp; Physical AI — Jason Ma, Dyna Robotics](https://www.youtube.com/watch?v=BHiYomkfoGQ)**

From training a world-action model on over one million hours of human video to deploying robots that fold thousands of napkins ...

📺 Latent Space

👁️ 17K • 👍 87 • 💬 6 • ⏱️ 1:21:06 • 5d ago

---

**[Humanoid Robots in Action at World Summit AI](https://www.youtube.com/watch?v=h01WB8f6Xqg)**

What does the future of humanoid robotics actually look like? At World Summit AI, I had the opportunity to see some fascinating ...

📺 Bernard Marr

👁️ 82K • 👍 7K • 💬 17 • ⏱️ 1:30 • 5d ago

---

**[BYD Reveals Its Own Humanoid Robot and wants to Make Millions of Them...](https://www.youtube.com/watch?v=skUIW0cb9NM)**

BYD Reveals Its Own Humanoid Robot and wants to Make Millions of Them... Chinese auto giant BYD has officially unveiled the ...

📺 The Electric Viking

👁️ 39K • 👍 566 • 💬 90 • ⏱️ 5:29 • 5d ago

---

**[The hopes and risks of bringing humanoid robots into our homes](https://www.youtube.com/watch?v=-g5xHE-rxjE)**

Life-like, humanoid robots have captured our imagination for decades. Now, those robots work in factories and assembly lines all ...

📺 PBS NewsHour

👁️ 44K • 👍 661 • ⏱️ 26:47 • 1d ago

---

**[Faraday Future Unveils $2,490 Humanoid Robot! #Shorts](https://www.youtube.com/watch?v=PEFpaqRjylQ)**

Tesla expects Optimus to cost $20000, but Faraday Future just shocked the robotics world by unveiling the FF Nova: a full-sized ...

📺 LogicLayers

👁️ 1K • 👍 16 • ⏱️ 0:34 • 10h ago

---

**[China’s Humanoid Robots Now Carry Riot Shields! 🤖🛡️](https://www.youtube.com/watch?v=Z3LnwybwvAY)**

China's NORINCO has showcased its Fuxi humanoid robots performing coordinated drills with riot shields and batons. Weighing ...

📺 Nexio Core

👁️ 7K • 💬 2 • ⏱️ 0:05 • 15h ago

---

**[These AI Robots Are Getting OUT OF CONTROL… Here’s What’s Actually Real](https://www.youtube.com/watch?v=NjcCxL9zcQQ)**

AI robots are advancing faster than ever, but how much of what we see online is actually real? From humanoid robot fights to ...

📺 The AI Nexus

👁️ 11K • 👍 75 • 💬 17 • ⏱️ 1:21:36 • 6d ago

---

**[Robostrategy CEO Andrew Kang showcases &#39;Taku&#39; the robot and talks the physical AI race](https://www.youtube.com/watch?v=eRHDxFkQlYw)**

Andrew Kang, Robostrategy co-founder and CEO, joins 'Closing Bell Overtime' to talk teh increase in hysical AI and what that ...

📺 CNBC Television

👁️ 51K • 👍 177 • 💬 68 • ⏱️ 5:19 • 4d ago

---

**[robot gropes girl in germany: teens probed #shorts](https://www.youtube.com/watch?v=H4kKt1XlWxU)**

Two teenagers in Cologne, Germany are under police investigation after a remote-controlled robot allegedly groped a 16-year-old ...

📺 Indiatimes

👁️ 2K • 👍 25 • ⏱️ 0:29 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*

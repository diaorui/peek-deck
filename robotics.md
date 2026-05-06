---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-05-06T13:13:33.930273+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** May 06, 2026 at 13:13 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Homemade robotic hand & wrist doing actual stuff](https://www.reddit.com/r/robotics/comments/1t51e0f/homemade_robotic_hand_wrist_doing_actual_stuff/)**

Well, what good is designing a hand if it can't actually do anything, so here's a couple actions (all in real time) I was able to achieve with my hand & wrist combo! Surprising just how many more poses and gestures having a wrist allows for vs just a hand. Design wise, not much has changed since my last post, aside from a few tolerance and material improvements. Instead, I've been putting it through its paces, making sure it can work decently accurately, reliably, and safely. Maybe v21 a little bit later...

9h ago

---

**[Testing cingoli di Wall-E](https://www.reddit.com/r/robotics/comments/1t52tyl/testing_cingoli_di_walle/)**

8h ago

---

**[Boston Dynamics posted a video of the new production version electric Atlas spinning its body while balancing on its arms](https://www.reddit.com/r/robotics/comments/1t4h0sf/boston_dynamics_posted_a_video_of_the_new/)**

22h ago

---

**[Built an Autonomous Mobile Robot (AMR) for warehouse automation - from CAD to code.](https://www.reddit.com/r/robotics/comments/1t5a31j/built_an_autonomous_mobile_robot_amr_for/)**

Designed the chassis in Fusion 360, exported to URDF, and built the full stack using ROS 2. Stack: Nav2 for navigation & path planning ArUco-based visual docking for precise alignment Custom waypoint sequencing for multi-shelf tasks Gazebo + RViz for simulation & visualization Challenge: LiDAR point cloud rotated with the robot in RViz, breaking the mapping and navigation. Root cause: odom/TF mismatch during turns. Fix: Developed a GroundTruthOdom node using Gazebo pose data to publish stable /odom and consistent TF, including handling ROS-Gazebo timestamp issues. In the video: robot autonomously services requests for Shelf B and Shelf C and delivers them to the drop-off zone. Happy to discuss the system or challenges!

1h ago

---

**[Ai2 released MolmoAct 2: a fully open-source action reasoning model for real-world robotics (with MolmoAct 2-Bimanual YAM dataset)](https://www.reddit.com/r/robotics/comments/1t56zqa/ai2_released_molmoact_2_a_fully_opensource_action/)**

Blog: https://allenai.org/blog/molmoact2 Models: https://huggingface.co/collections/allenai/molmoact2-models Training dataset: https://huggingface.co/collections/allenai/molmoact2-datasets From Ai2 on 𝕏 (long thread): https://x.com/allen_ai/status/2051708880455868501

4h ago

---

**[Open Source Simple Software to Calibrate Fisheye Cameras](https://www.reddit.com/r/robotics/comments/1t57fd6/open_source_simple_software_to_calibrate_fisheye/)**

Hi, so I got stuck with a 160deg wide camera for my robot, which I wanted to use to do visual SLAM, but the raw video itself was too distorted for it to be good, so I vibecoded a toolkit to figure out the intrinsic parameters of my camera and be able to undistort the footage. It took me some time, at first the distortion was still there, so I went ahead and created a program that helped me sample ~60 frames with a mini guide on which positions I should record for best results, and yeah it worked, I was able to undistort my video from my 160deg camera, so I figured to share if anyone is also using wide cameras on their robots. I know this ain't nothing new or ground breaking, there are probably tools out there that already do this and I was just too lazy to look them up and set them up, but hey if this turns out helpful for someone besides just me, I'm happy with that. REPO LINK: https://github.com/L42ARO/Fisheye-Calibration

4h ago

---

**[I Built Rocky from project hail Mary as a walking talking robot](https://www.reddit.com/r/robotics/comments/1t5aqw6/i_built_rocky_from_project_hail_mary_as_a_walking/)**

Basically I had a raspberry pi 5, connected to 7 servos, the pi connected with gemeni who in addition to being able to respond to you like Rocky would, in Rockys voice, also used tool calling to control the body

🔗 [youtu.be](https://youtu.be/FG5cwNxvOp8) • 1h ago

---

**[Harvard engineers built ant-like robots that work together without central control](https://www.reddit.com/r/robotics/comments/1t4xl9d/harvard_engineers_built_antlike_robots_that_work/)**

Researchers from the Harvard John A. Paulson School of Engineering and Applied Sciences and the Faculty of Arts and Sciences developed small cooperative robots that can organize themselves to either build structures or dismantle them, using only simple rules and changes in their surroundings.

🔗 [The Brighter Side of News](http://thebrighterside.news/post/harvard-engineers-built-ant-like-robots-that-work-together-without-central-control) • 12h ago

---

**[Autonomous solar panel installation: Crawler base, robotic arm, suction system, AI vision, and 3D sensors — placing ~30 kg panels with ±1–2 mm precision. At about 1 panel every 30 seconds.](https://www.reddit.com/r/robotics/comments/1t4alwf/autonomous_solar_panel_installation_crawler_base/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2051330286190035151

1d ago

---

**[Presenting the XR-4 „Rehbar“ („Pioneer“ in Urdu 🇵🇰)](https://www.reddit.com/r/robotics/comments/1t4au4m/presenting_the_xr4_rehbar_pioneer_in_urdu/)**

XR-4 Rehbar I wanted to showcase a personal project that I had been working on for around a year. As a graduate student in EE and embedded engineer working in Industrial IoT, I have wanted to pivot to robotics and autonomous mobility for a long time. With simulation and virtual environments not being possible for technical reasons and on account of being a very hands-on kind of learner and with the goal of going through a process of building something from scratch, I decided to build a test platform in the form of a rover which I can modify, upgrade and build upon. I also researched similar open-source, hobbyist and professional projects to draw inspiration. Several projects on Instructables and Reddit helped me in refining my ideas and the LeoRover platform from FictionLab was something which made me go: „this is it, this is what my rover should be like“. I want this platform to be easily reconfigurable and upgradeable. It is definitely not meant to be a hobby project, it is intended to stand somewhere between a hobby/DIY project and a high end platform like the LeoRover which is not for the average engineer looking to upskill in his home lab or develop and test out some stuff on his own, only being affordable if you’re a university lab or a government funded research institution. With that, I present the XR-4 Rehbar (lit. „Pioneer“ in Urdu) GitHub: rover-xr4 The GitHub repo and documentation is not up to date at this point, I will be updating them and this post in the near future. Electronics and Software CTU - Control and Telemetry Unit: sends telecommands to the OBC i.e. steering commands, lights and peripherals and receives telemetry (voltage and current, GPS data, IMU data, temperature and statuses) over the ESP-NOW protocol. Tested outdoors LoS range was 100-120m OBC - Onboard Controller: motor and steering control, power monitoring, safety related functionality. Sends telemetry to CTU and receives telecommands from CTU over ESP-NOW. Lower level controller which can interface with a SBC based mission computer on the future for autonomous operations The software for both CTU and OBC is written using a mix of Arduino and ESPIDF toolkits in VSCode and is available in the GitHub repo linked above. Mechanical and Structures Modified 4-wheel rocker suspension with differential drive/skid steering. Each wheel is driven by an independent 12V 100RPM Brushed DC motor without encoders (motors with encoders were just too expensive, sadly). The structure is 3D printed in its entirety except the rocker arms which are extruded Aluminium profiles. I am currently cleaning up and standardizing the naming convention of my CAD so that I can open source it. It will be up soon. A note on future work: I am working on upgrading the platform with autonomous navigation and driving and currently looking at architectural options for that I.e. options for hardware and sensors, communication and control architectures. Cost is obviously a concern and I want to limit it by using as much of the hardware I already have since I am funding this project myself. Lastly, I will welcome any and all questions, comments, opinions, criticism and ideas about anything - the design, electronics and the future work options (guidance, inspiration and ideas are badly needed :)) Thank you :)

1d ago

---

---

## Google News: "robotics"

**[MolmoAct 2: An open foundation for robots that work in the real world](https://allenai.org/blog/molmoact2)**

MolmoAct 2 is a fully open robotics foundation model that brings faster, stronger 3D action reasoning to real-world robot tasks, alongside a major new bimanual manipulation dataset for researchers to study, reproduce, and build on.

Allen AI • 21h ago

---

**[Ahead of Race to IPO, OpenAI Discussed Spinning Out Robotics, Hardware Divisions](https://www.wsj.com/tech/ahead-of-race-to-ipo-openai-discussed-spinning-out-robotics-hardware-divisions-18c89706)**

WSJ • 1d ago

---

**[Delivery robots still learning from 'edge cases,' scientists say](https://chicago.suntimes.com/news/2026/05/06/delivery-robots-chicago-crashes-damage)**

Engineering experts who were part of a University of Pennsylvania study offer some solutions: Improve the robots' complex internal sensors and address the problem of clean glass being harder to see than a dirty surface.

Chicago Sun-Times • 2h ago

---

**[Underwater robotics expert reveals 'shipwreck city' hiding beneath major urban lake](https://www.foxnews.com/travel/underwater-robotics-expert-reveals-shipwreck-city-hiding-beneath-major-urban-lake)**

An underwater robotics expert is exploring nearly 100 targets in Seattle's Lake Union, calling the area a "shipwreck city" full of hidden maritime history.

Fox News • 1d ago

---

**[Robots move in as waste firms struggle to find staff](https://www.bbc.com/news/articles/cvg0w84q1wyo)**

Humanoid robots are being added to the automation of waste sorting.

BBC • 1d ago

---

**[Schaeffler sees humanoid robotics orders in three-digit million euros by 2030](https://finance.yahoo.com/sectors/technology/articles/schaeffler-sees-humanoid-robotics-orders-112441111.html)**

Schaeffler expects its humanoid robotics business to build an order book in the hundreds of millions of euros by 2030, ‌the chief executive of the German machine and car parts maker said ‌on Tuesday.  CEO Klaus Rosenfeld, talking to Reuters after the company's first-quarter results, did not give a more ​specific estimate for the potential order book.  "We have been investing significantly in the humanoid robotics area and at the moment we are collaborating with around 45 humanoid robotics players globally," Rosenfeld said.

Yahoo Finance • 1d ago

---

**[Auburn team wins largest student robotics competition in the world](https://wire.auburn.edu/content/ocm/2026/05/auburn-wins-vex-u-robotics-world-championships.php)**

Aubie2, a team representing the Auburn Robotics Club, recently won the 2026 VEX Robotics World Championships in St. Louis. Squaring off against top teams from around the world, the squad of freshmen and sophomores emerged on top of what Guinness World Records calls the largest robotics competition on the planet — and inspiring the next generation of robotics enthusiasts in the process.

Auburn University • 3d ago

---

**[SAIL tech lets robots perform human-scale tasks far more quickly](https://newatlas.com/robotics/sail-robots-human-scale-tasks/)**

Thanks to researchers at Georgia Tech, robots have taken several new steps towards replacing human labor – and not simply for dangerous tasks such as mining the depths of the Earth and exploring the Moon, or difficult tasks such as high-speed mass-assembly of thousands of cars.

New Atlas • 1d ago

---

**[C2 Robotics christens first US export Speartooth LUUV](https://www.navalnews.com/naval-news/2026/05/c2-robotics-christens-first-us-export-speartooth-luuv/)**

C2 Robotics has today marked a significant milestone with the commissioning and christening of its Speartooth Large Uncrewed Undersea Vehicle (LUUV), the first to be delivered to the United States.

navalnews.com • 5d ago

---

**[A Battle of the Robots](https://now.tufts.edu/2026/05/04/battle-robots)**

On a Monday afternoon in the Tsungming Tu Complex, a flurry of small robots battled each other. No, this wasn’t an invasion straight out of sci-fi—it was

Tufts Now • 2d ago

---

---

## YouTube Videos: "robotics"

**[Elon Musk&#39;s Cheapest $500 Optimus Robot Version Finally Hitting the Market](https://www.youtube.com/watch?v=4pq8KuycgDM)**

Elon Musk's more affordable version of the Optimus robot is being discussed as a step toward making humanoid robotics ...

📺 Carros Show

👁️ 1K • 👍 45 • 💬 15 • ⏱️ 8:07 • 19h ago

---

**[AI Robots Join Armed SWAT Police And Shock The Public Worldwide](https://www.youtube.com/watch?v=Rha0LytNWxk)**

AI robots are moving from labs into real streets. China has already shown humanoid robots walking with SWAT officers, guiding ...

📺 AI Revolution

👁️ 8K • 👍 327 • 💬 49 • ⏱️ 13:16 • 14h ago

---

**[Humanoid Robot Gets Pushed and Instantly Recovers Like a Human](https://www.youtube.com/watch?v=9XmCqkHRT0I)**

This humanoid robot just did something most machines cannot do. After being pushed, it instantly recovers and keeps moving like ...

📺 DPCcars

👁️ 12K • 👍 120 • 💬 55 • ⏱️ 3:09 • 1d ago

---

**[The Engineering Reason this Robot Feels Human | 1X Neo Factory](https://www.youtube.com/watch?v=Uh1bj4nZvXg)**

I walked into this factory expecting to be impressed by the robots. What I wasn't expecting was to find one quietly sorting parts in ...

📺 Tiff In Tech

👁️ 47K • 👍 1K • 💬 111 • ⏱️ 11:06 • 5d ago

---

**[This Southern California city has an issue with food delivery robots](https://www.youtube.com/watch?v=O7dLeFqZLic)**

You've probably seen them before: those little four-wheeled robots delivering food along sidewalks in communities across SoCal.

📺 KTLA 5

👁️ 14K • 👍 120 • 💬 58 • ⏱️ 2:14 • 17h ago

---

**[Japan Airlines to replace workers with humanoid robots](https://www.youtube.com/watch?v=_Lgughpiamw)**

Japan Airlines is trialling humanoid robots for luggage handling due to rising visitor numbers and a drop in the number of people ...

📺 Sky News Australia

👁️ 62K • 👍 794 • 💬 362 • ⏱️ 2:15 • 5d ago

---

**[CHEATER in War Robots - REALTALK](https://www.youtube.com/watch?v=KzpE5llTDVY)**

War Robots Gameplay about different cases of Cheating - WR My War Robots Creator Link: https://wr.my.games/manni - Code: ...

📺 Manni-Gaming

👁️ 16K • 👍 1K • 💬 370 • ⏱️ 19:36 • 23h ago

---

**[AI ROBOTS Ready to TAKE OVER — Figure 03 + 1X NEO Just Shocked the World](https://www.youtube.com/watch?v=FspQyTAvJTU)**

The humanoid robot revolution just kicked into HYPER-SPEED — and you're not ready for what's coming! Figure AI and 1X just ...

📺 The AI Nexus

👁️ 3K • 👍 114 • 💬 13 • ⏱️ 20:22 • 1d ago

---

**[I Built an Even Better Robot Dog](https://www.youtube.com/watch?v=GFLa1b1juUo)**

Let's make another Ropebot dog! Subscribe to my Patreon: https://www.patreon.com/aaedmusayt Buy the CARA 2.0 project files: ...

📺 Aaed Musa

👁️ 111K • 👍 11K • 💬 696 • ⏱️ 22:12 • 4d ago

---

**[Is my Gearbox Precise? #3dprinting #gearbox #testing #robotics](https://www.youtube.com/watch?v=8Bh0IXDBw20)**

I test to see if my 3D printed gearbox is precise. I made a pointer attachment for the gearbox to see if it returns to the same position ...

📺 Advanced Hobby Lab

👁️ 151K • 👍 2K • 💬 14 • ⏱️ 0:28 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

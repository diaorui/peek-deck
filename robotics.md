---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-04T19:22:47.414850+00:00'
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

**Last Updated:** February 04, 2026 at 19:22 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Mistral robotics team is hiring.](https://www.reddit.com/r/robotics/comments/1qvm6p4/mistral_robotics_team_is_hiring/)**

From Olivier Duchenne on 𝕏: https://x.com/inventorOli/status/2018719028462657922 And Guillaume Lample on 𝕏: "Mistral robotics team is hiring. Join us!": https://x.com/GuillaumeLample/status/2018719626578796665

7h ago

---

**[Day 135 of building Asimov, an open-source humanoid. Assembling the upper body now, speaker and other components going in](https://www.reddit.com/r/robotics/comments/1qvluxh/day_135_of_building_asimov_an_opensource_humanoid/)**

Asimov is an open-source humanoid robot. We open-sourced the leg design and XML files for simulation. It's built with off-the-shelf components and 3D-printable parts. All files and parts are here: https://github.com/asimovinc/asimov-v0

8h ago

---

**[My custom quadruped ecosystem: 2 years of work on mechanics, electronics, and ROS 2 software.](https://www.reddit.com/r/robotics/comments/1qvqbug/my_custom_quadruped_ecosystem_2_years_of_work_on/)**

Hi everyone! I’m excited to finally share a project I’ve been working on for the past 2 years. I developed the entire ecosystem from scratch: from the initial mechanical design and fabrication to the electronics and the full software architecture. My main goal was to build a robot that is as user-friendly as possible. Fabrication and hardware Design on Solidworks Maker 3D printed on an Ender 3 V2 and a Bambu Lab X1C 2 parts for the case are cut with a laser cutter (in a Fab-Lab) Materials : PLA, PETG, TPU, ABS, PC and plywood Electronics NVIDIA Jetson Orin Nano : handles the communication with the cameras and the controller 3 Arduino nano, one in each part of the robot (front, middle and back). They interface with the sensors and actuators. Teensy 4.1: Handles the IMU with SPI communication. Acts as a bridge between the Arduino and the Jetson : Communicates by I2C with Arduino Reads and publishes directly on topics with micro-ROS. Controller is a Legion GO. I used it to have physical joystick, touch sensitive screen, with easy to use driver (thanks to Windows 11). The physical Joy an button are detected like a real Xbox controller. Software ROS 2 Humble and Ubuntu 22 on the Jetson. Windows 11 on the Legion Go. Python for the Legion Go and Jetson. C++ (Arduino) for the Teensy and the Nanos. The user interface on the legion go is developed using Pygame. Sensors 2 MIPI CSI cameras (one has night vision). 1 BNO085 and 1 MPU 6050 for the IMU. 5 distance sensors (Time Of flight sensors) sensors for temperature, touch sensitivity, tension, current, etc. Actuators 12 Lynxmotion LSS V2 servos. Within the weight and dimensions of my robot, it's not the best solution (Slightly underpowered), but I made the choice to focus on user experience and a professional product appearance instead of mobility for this robot. 3 standart 90g servomoteurs for the moving parts in the Head 4 fans for cooling, LEDs, laser, Swappable Batteries and Alimentation Wired alimentation is possible with classic jack connector Swappable DIY batteries : 5S1P 21700 with Molicel P42A Custom 3D printed case If you want to see more of the robot in action, I have a longer video here: https://youtu.be/xeyl0i7DunE?si=ifOYklHHlQlqF0qz Feel free to ask me anything about the build, I’ll be happy to answer your questions!

4h ago

---

**[I built a drone with six radars that refuses to hit power lines](https://www.reddit.com/r/robotics/comments/1qvercu/i_built_a_drone_with_six_radars_that_refuses_to/)**

The drone has six mmWave radars to sense power lines from any direction, all connected to a Raspberry Pi. Based on these detections, the desired velocity (from a pilot or autonomous system) then gets modified to guide the drone around the power line. Everything runs in real time on the Pi with ROS2 middleware and PX4 flight stack. If you're interested, you can check out the paper: https://arxiv.org/abs/2602.03229, or the full video with voice-over: https://www.youtube.com/watch?v=rJW3eEC-5Ao

14h ago

---

**[HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (Paper and project page)](https://www.reddit.com/r/robotics/comments/1qvkoyn/humanx_toward_agile_and_generalizable_humanoid/)**

Paper: https://arxiv.org/abs/2602.02473 Project Page: https://wyhuai.github.io/human-x/ From Yinhuai on 𝕏: https://x.com/NliGjvJbycSeD6t/status/2018713031157465495 Previous post: An Unitree trained to play basketball and the first human block against a humanoid: https://www.reddit.com/r/robotics/comments/1p2w932/an_unitree_trained_to_play_basketball_and_the/

9h ago

---

**[Rodney Brooks on why humans still do the grasping](https://www.reddit.com/r/robotics/comments/1qvab5h/rodney_brooks_on_why_humans_still_do_the_grasping/)**

Brooks argues that the real bottleneck is still physical interaction with the world. Humans don’t just copy motions when they pick something up. They constantly sense force, adjust grip, and adapt in ways that are hard to formalize or capture in data. Many current systems learn from vision or teleoperation, but that misses what happens at the point of contact. His view isn’t that automation can’t help. It’s that value today comes from supporting humans around these tasks rather than replacing them. Reducing walking, lifting, and strain is achievable now, while true human-level grasping remains a long-term challenge.

18h ago

---

**[OpenClaw + RealSense + QWEN + ROS = Physical AI](https://www.reddit.com/r/robotics/comments/1qv7byt/openclaw_realsense_qwen_ros_physical_ai/)**

Mind Blown! Have you heard about ClawdBot now called OpenClaw? It’s an open source personal AI assistant with over 150k stars on GitHub. I connected a RealSense camera to it and my robot started following me!

20h ago

---

**[Slight robotics research rant](https://www.reddit.com/r/robotics/comments/1qvf946/slight_robotics_research_rant/)**

Not sure where else to rant and have people understand where I am coming from. But here it goes - I am a master's student in mechanical engineering, specializing in robotics. I entered with an existing research idea in mind, given that I have completed 2 years of undergraduate research in this lab. At first, I was able to work on my existing idea, especially since it was novel. But then came Trump's funding cuts, and my school/lab was essentially out of funds (and because my PI bought the Unitree G1 complete package lol). I lost my funding, and research now is pretty restricted. With that, I have been advised to start preliminary research in a completely different field. I did try to return to my prior research, but I received negative feedback. There was a strong sense coming from my PI that I should do research in human-robot interaction (HRI). I spoke to some peers in the lab, and from the sounds of it, I was pushed to do research in this area of robotics mainly so that I can work on a novel idea and get NSF funding (ideally) for the lab, depending on the proposal, since this area of robotics has been getting alot of traction lately due to safety concerns. Although I do have a pretty interesting/novel idea in this field (and I would be more than happy to chat with anyone about it), I sort of dread it. I've been delaying research on this topic because working on it isn't exciting, and the work itself steers me into an industrial field separate from my dreams. To top it off, I hate our weekly lab meetings (where we present our week's work and what we plan to do the following week). It's been about 4 months since I first explained my work (pertaining to Trust in HRI), and almost every meeting ends with my PI saying he doesn't understand the topic of trust. I figured I was the issue in explaining it, but all my peers understood it and found it extremely interesting. The first thing they asked, as well, was whether I transferred to a PhD program. Mainly due to the fact that master's research typically deals with the applications of PhD research, while PhDs focus on completely novel ideas. However, my work has involved complete reformulations / new formulations of statistical means that PhD students would focus on. I spent many sleepless nights reading many statistical textbooks and so on. I even spent nearly a month reading psychology papers to better understand human Trust on the human level (spoiler, psychologists appear to barely understand it as well). In the end, though, it does not matter how hard or how much I work on this topic because if my PI doesn't approve of it, then I cannot complete my thesis, which feels like a punch to the throat. Fortunately, I have a second-round interview with ASML and a backup secured internship with NASA, so that might help steer me back onto my ideal path or open new doors for research. But the next year of research sounds like it'll suck... Wishing I had a separate hot topic to research that the PI would at least somewhat understand and approve of. It's the least I can ask for after doing 6+ hours a day of unpaid research :') P.S. Sorry if this rant was scattered. Brain still in overdrive from school.

14h ago

---

**[Joints made with rolling contact surfaces](https://www.reddit.com/r/robotics/comments/1quvbyp/joints_made_with_rolling_contact_surfaces/)**

See this LINK. Cool article about a new design for robot joints that roll instead of pivoting like normal hinges. Seems like a very practical design that would be easy to make with 3D printing, and can be passive or motor-driven. The joints use specially shaped (non-circular) rolling surfaces that can be “programmed” to move in very specific ways. Compared to regular joints, these rolling joints can follow complex paths much more accurately The joints can also change how force is transmitted, giving more strength where it’s needed and more speed elsewhere. From this academic article:C.J. Decker, T.G. Chen, M.C. Yuen, & R.J. Wood, Noncircular rolling contact joints enable programmed behavior in robotic linkages, Proc. Natl. Acad. Sci. U.S.A. https://doi.org/10.1073/pnas.2521406123 (2026). The authors show that a joint designed this way can closely match the motion of a human knee, far better than standard hinges. They also build a robotic gripper that can lift over three times more weight than a similar gripper with ordinary joints.

1d ago

---

**[Final jet engine scale model design](https://www.reddit.com/r/robotics/comments/1qvfmy1/final_jet_engine_scale_model_design/)**

14h ago

---

---

## Google News: "robotics"

**[Bedrock, an A.I. Start-Up for Construction, Raises $270 Million](https://www.nytimes.com/2026/02/04/business/dealbook/bedrock-robotics-ai-fundraise.html)**

The New York Times • 6h ago

---

**[Robotics Will Break AI infrastructure: Here’s What Comes Next](https://www.nextplatform.com/2026/02/03/robotics-will-break-ai-infrastructure-heres-what-comes-next/)**

SPONSORED CONTENT  Physical AI and robotics are moving from the lab to the real world – and the cost of getting it wrong is no longer theoretical. With

The Next Platform • 1d ago

---

**[ETM brings its transverse flux motor technology to robotics](https://www.therobotreport.com/etm-brings-its-transverse-flux-motor-technology-to-robotics/)**

ETM said its TFM technology enables OEMs to simplify mechanical designs, reduce costs, and achieve performance benchmarks.

The Robot Report • 3h ago

---

**[World’s first ‘biomimetic AI robot’ debuts in Shanghai](https://www.scmp.com/video/china/3342129/worlds-first-fully-biomimetic-embodied-intelligent-robot-debuts-shanghai)**

The world&rsquo;s first &ldquo;fully biomimetic embodied intelligent robot&rdquo; debuted in Shanghai on January 30, 2026. The company behind the robot, DroidUp, claims the human-like…

South China Morning Post • 2d ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 2d ago

---

**[Humanoid Robotics Market in 2026 Transformative Trends and Technological Advancements](https://finance.yahoo.com/news/humanoid-robotics-market-2026-transformative-151500387.html)**

According to Precedence Research, humanoid robotics is advancing rapidly, with key companies leading the charge toward mass production and real-world deployments. Tesla, Boston Dynamics, and Figure AI are at the forefront of this transformation, focusing on building general-purpose humanoid robots, with significant funding and operational goals. These companies are not only innovating in design but are also gearing up for large-scale production, making humanoid robots a reality for various secto

Yahoo Finance • 4h ago

---

**[Apple Teaching Swift and Robotics Across Its India Supply Chain](https://www.macrumors.com/2026/02/04/apple-teaching-swift-and-robotics-in-india/)**

Apple today announced a new Education Hub in Bengaluru as part of an expanded effort to provide technical training and skills development for employees across its supply chain in India. Apple said the new Apple Education Hub in Bengaluru will serve as a centralized training and coordination facility for supplier employees in India, marking the company's first education hub of its kind in the country.

MacRumors • 7h ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 1d ago

---

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 3d ago

---

**[COMMENTARY: Teaching mathematics with coding and robotics can transform California math instruction](https://edsource.org/2026/california-math-framework-coding-robotics/750225)**

A hands-on, integrated approach has the potential to transform math from a gatekeeper into a gateway for STEM opportunities for all students.

EdSource • 2d ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 18K • 👍 161 • 💬 35 • ⏱️ 1:21 • 3d ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 26K • 👍 115 • 💬 44 • ⏱️ 2:06 • 3d ago

---

**[30 million won humanoid robot for sale at Seoul’s supermarket](https://www.youtube.com/watch?v=qHpFZ3f2a_E)**

You can watch this video at https://koreanow.com Copyright(C) Unauthorized use, distribution, and employment of AI-based tools ...

📺 KOREA NOW

👁️ 4K • 👍 91 • 💬 22 • ⏱️ 1:54 • 1d ago

---

**[SSLC IT Chapter 6: The World of Robots | LED, Buzzer | Practical | Xylem SSLC](https://www.youtube.com/watch?v=csQEZkNlb2Q)**

sslc #xylemsslc #sslcpublicexam #sslcit Xylem New Year Offer Live Now !! Join Asthra Batch, Use Coupon Code "NY15", ...

📺 Xylem SSLC

👁️ 245K • 👍 9K • 💬 676 • ⏱️ 23:34 • 4d ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 65K • 👍 431 • 💬 17 • ⏱️ 0:06 • 17h ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 788K • 👍 7K • 💬 3K • ⏱️ 3:13 • 5d ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 138K • 👍 1K • 💬 282 • ⏱️ 14:25 • 4d ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=yOXhsjonNHk)**

📺 Lin of Brant robot 

👁️ 25K • 👍 76 • ⏱️ 0:19 • 4d ago

---

**[Tesla Optimus robot will allow for amazing abundance. #fyp #viral #tesla #optimus #teslarobot](https://www.youtube.com/watch?v=CPDqiFW1AhI)**

📺 Tesla Owners Silicon Valley

👁️ 2.7M • 👍 76K • 💬 1K • ⏱️ 0:40 • 2d ago

---

**[No One Is Using This Right Now... Smuta Stryx Is INSANE Now - COOKS Kaji Campers | War Robots](https://www.youtube.com/watch?v=WrAHOQY-t8U)**

Smuta Stryx is terrifying. I havent used the Smuta in awhile. But the other day an enemy player cooked me with them. So now I feel ...

📺 PREDATOR WR

👁️ 3K • 👍 215 • 💬 35 • ⏱️ 13:56 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*

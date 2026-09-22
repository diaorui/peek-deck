---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-09-22T01:28:14.630088+00:00'
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

**Last Updated:** September 22, 2026 at 01:28 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Servo Motor finger mechanism](https://www.reddit.com/r/robotics/comments/1wlw0sr/servo_motor_finger_mechanism/)**

Link 🔗 https://cults3d.com/fr/mod%C3%A8le-3d/gadget/servo-motor-finger-mechanism Full hand kit soon inchaAllah Servo Motor finger mechanism

1d ago

---

**[[Showcase] The drone flies a 3D building complex with no map, no GNSS, no compass and no lidar: two cameras do both the seeing and the localizing (ROS 2, PX4, Gazebo, CUDA)](https://www.reddit.com/r/robotics/comments/1wlsrqn/showcase_the_drone_flies_a_3d_building_complex/)**

(GIF: an industrial room 58 m short of the goal. Left is Gazebo, the drone among pipes and beams; right is RViz, where pink is the obstacle memory, the cyan fan is the current stereo depth return, orange is the committed route and the magenta sphere is the goal. In these nine seconds the speed law does its whole job: the drone crawls at 0.2 m/s where the pair resolves little, runs up to 2.5 m/s where it resolves far enough, and is back at 0.1 m/s before the next corner.) Flight video: https://www.youtube.com/watch?v=OUuAj2WNKzs Two weeks ago I posted the same location flown with a 3D lidar. The lidar is gone now, and so is GNSS and the magnetometer. The airframe carries a forward stereo pair (1280 x 960, 120 degrees, 0.20 m baseline, 7.5 Hz) and two 8 x 8 time-of-flight sensors looking up and down. That pair does both jobs: stereo depth becomes the obstacle memory the planner searches, and a stereo MSCKF on the same images is the position and heading PX4 flies on, in place of satellites and compass. So: a start, a goal, a multi-storey building with shafts and openings at different altitudes, and nothing but two cameras and an IMU. The location is the DARPA Subterranean Challenge "Urban Circuit Practice 01" world published by Open Robotics on Gazebo Fuel (CC BY 4.0). Numbers from the release, five consecutive flights on one commit with nothing changed between them: 410 to 629 m of path, 1.48 to 1.79 m/s mean speed with every hold and replan counted, no collisions. Five more on the same commit with the lidar instead, for comparison: 2.42 to 2.67 m/s. Cameras are slower because confident stereo depth reaches 6.4 m against the lidar's 35, and the drone only flies as fast as it can stop inside the range the sensor is guaranteed to have resolved. The check I am most pleased with is a new one. The mission monitor decides the drone arrived by asking the drone where it thinks it is, and an odometry drifts by metres, so it can arrive perfectly in its own coordinates while standing somewhere else. Every flight now fails unless the true position from the simulator is inside the 2.0 m capture radius at the moment the goal is acknowledged. Over the five camera flights the truth stood 0.47 to 1.42 m from the goal. What cost me the most flights was not the filter but the things around it: the autopilot resetting its clock synchronisation whenever the simulation ran below real time (about a second without navigation each time), the autopilot's gate on external odometry being tighter than the estimator's own corrections, and telling the filter the gyroscope was eighteen times noisier than it is, which let the noise of every visual update walk the one direction no camera can observe. Limitations, honestly: the drift has no bound (0.1 to 0.4 percent of the path), so a mission three times longer would miss the 2.0 m radius; it is one location and one start-goal pair; it is simulation only and not validated for a real aircraft; and the multi-vehicle missions have not been flown on cameras yet. MIT licensed. On a Linux host with Docker and an NVIDIA GPU, one script prepares a fresh clone (dev image, PX4 build, workspace, environment assets) and starts the flight: git clone https://github.com/formiat/px4-ros2-drone-nav.git cd px4-ros2-drone-nav ./scripts/bootstrap.sh https://github.com/formiat/px4-ros2-drone-nav Happy to answer anything, and I would like to hear from people who have flown a single camera pair as both the perception and the localization sensor: what broke first?

1d ago

---

**[Watti update: the first follower-created animations running on the physical robot](https://www.reddit.com/r/robotics/comments/1wlsaih/watti_update_the_first_followercreated_animations/)**

Another small Watti update. I ran a very early closed test of Watti Studio. A few followers created animations directly from their phones and computers, and I manually transferred them to the physical robot. This was only the first validation of the idea. For the next closed test, I plan to connect Watti Studio directly to Watti and automate the entire pipeline - animation submission, queueing, playback, recording, and video delivery. Which animation is your favorite? Would you be interested in joining the next closed test? If you’d like to learn more about Watti’s architecture and the hardware I’m using, the pre-release repository is available here: https://github.com/Nikolay-Tyulkin/Watti

1d ago

---

**[Designing my own adaptive gripper for a robotic arm in Siemens NX, looking for advice and measurements](https://www.reddit.com/r/robotics/comments/1wmbbtn/designing_my_own_adaptive_gripper_for_a_robotic/)**

Hi everyone, I'm building a robotic arm and I'm currently working on the gripper. I want to use an adaptive gripper (one that conforms to the shape of the object), but most of the designs I've found online aren't great, so I've decided to design my own. I recently came across a design on Instagram that looks exactly like what I'm going for, but I can't find it anywhere to buy or download. I'm designing it in Siemens NX and I'll be using a Feetech STS3215 servo to drive it. Does anyone have tips, reference designs or measurements for this kind of gripper? Thanks in advance!

13h ago

---

**[My goalkeeper bot](https://www.reddit.com/r/robotics/comments/1wmbk4e/my_goalkeeper_bot/)**

Before and after training

12h ago

---

**[Helical gear question](https://www.reddit.com/r/robotics/comments/1wm8ri6/helical_gear_question/)**

How do I connect these Helical gears like this? It's being run by a RDS3115mg servo motor, and supposed to be a tilt up and down set up

15h ago

---

**[Help with regards to Installing ROS + MuJoCo on my Mac](https://www.reddit.com/r/robotics/comments/1wm3o51/help_with_regards_to_installing_ros_mujoco_on_my/)**

For some projects I need to work with ROS 2 and simulate through MuJoCo. MuJoCo runs natively on Mac with full graphics performance. The simulation quality was insane when I tried messing around with real world robots like Spot from Boston Dynamics. But for some projects I need ROS to work with and I tried with my Parallels VM and the performance in terms of graphics was not that great because it used the CPU for rendering. I tried using Robostack and the performance of basic ROS itself hit a lot of problems. Any workarounds or possible solutions? PS: I don’t want answers like get a PC or something because that ain’t really viable option for me

20h ago

---

**[Same moving carriage for both Stepper motors](https://www.reddit.com/r/robotics/comments/1wm63tm/same_moving_carriage_for_both_stepper_motors/)**

Rack-and-pinion for the Linear carriage. With another Stepper motor for Pan movement mounted on the same carriage. Let's test it.

17h ago

---

**[My first-ever Fusion 360 project is a pan-tilt camera](https://www.reddit.com/r/robotics/comments/1wlddf9/my_firstever_fusion_360_project_is_a_pantilt/)**

Hey everyone! ​I recently finished school for automation while working as a scaffolder, and I decided to dive headfirst into learning CAD. This auto-tracking pan-tilt camera assembly is my very first design in Fusion 360! ​It took 6 revisions to get here, but V1.6 printed out with an amazingly snug press-fit—everything fits together smoothly with zero mechanical slop. Current Hardware & Next Steps: Right now, it runs on an ESP32-S3 Sense board for initial testing, but the rear compartment is sized with extra volume so I can upgrade to a Raspberry Pi for real-time edge-AI / YOLO object tracking down the road. Would love to hear your thoughts, feedback, or suggestions for improving future revisions!

1d ago

---

**[Building an optical sorter for potato harvest](https://www.reddit.com/r/robotics/comments/1wlgx3p/building_an_optical_sorter_for_potato_harvest/)**

Hello all, I’m a farmer from the Netherlands and I am interested in robotics. I am starting to work on a project that I would like to get feedback on. During the potato harvest a lot of soil clods come in with the potatoes. At this moment, the only reliable way for me to remove them before the potatoes go into storage is with people standing alongside a conveyor belt picking them out. I would like to see if I can automate that process with a machine that I can build myself. Since tools like ChatGPT and Claude became available, I have developed a habit of thinking: “How hard can it be? I’ll just build it myself.”. This approach has the danger of discovering halfway through a project that there is an entire layer of complexity that I didn’t even know existed. So, before I start buying cameras, pneumatic components and machines, I would like a reality check from people who know more about robotics than I do. Current solutions There are commercial optical sorting machines that can already do what I need. For example: Flikweert Divider Select https://flikweertvision.com/nl/machines/divider-select/ Downs Cropvision https://www.downs-fr.com/produits/downs-cropvision/ For my operation these machines are currently too expensive to financially justify. And I also think I only need a fraction of what these machines can do. There is also a much simpler machine for separating clods from potatoes This type of machine uses a steel roller. Potatoes and clods rebound from the roller with different trajectories because of their different physical properties. An adjustable divider then separates the two streams. Traditional clod separator https://www.youtube.com/watch?v=d_j7X2TJx3M This sounds like the solution to my problem, but I want to remove the clods directly during harvest, before the potatoes go into storage. At that point our clay clods can still be wet and soft. They do not behave sufficiently differently from a potato when they hit the steel roller, so the mechanical separation becomes much less reliable. The project The practical target would be to process 20–30 tons/hour over a 1-meter-wide belt. Potatoes and clods are generally up to around 70 mm. The system does not need to be perfect. Missing some clods is acceptable, and occasionally rejecting a potato together with a clod is also acceptable. I have divided the project into 3 parts: Mechanical hardware, vision/ejector hardware and software. I’m most comfortable with the mechanical part of the project. The frame, conveyors, motors, mounting brackets, compressed air, etc., I can fabricate and modify this kind of equipment myself. Instead of building the whole mechanical machine from scratch, I’m considering buying one of those traditional clod separators and using it as the mechanical base (see picture 1 and 2). The machine that I would like to use as a basis has an input conveyor belt that is 1-meter-wide and already has the two discharge paths I need. https://preview.redd.it/arpbeh76doqh1.jpg?width=300&format=pjpg&auto=webp&s=ec5facf2e86f447b6d739ba14e991870e438fcda Picture 1: Traditional clod separator https://preview.redd.it/j8h5nj76doqh1.jpg?width=301&format=pjpg&auto=webp&s=cb1e522703c2308bb275ffd781d39036e62039be Picture 2: Traditional clod separator My idea would be to remove the steel roller and replace it with a row of individually controlled pneumatic ejector fingers (see picture 3). Above the 1-meter input conveyor would install a camera with controlled lighting (see picture 4). https://preview.redd.it/kcc84h76doqh1.jpg?width=410&format=pjpg&auto=webp&s=d35e1872bcdcaaff61362c6c979f3757d2607cbc Picture 3: Pneumatic fingers https://preview.redd.it/tesjzf76doqh1.png?width=372&format=png&auto=webp&s=70e37da4a2e0a2941fcd255a93713410d3fa70da Picture 4: Cameras and controlled lighting The vision system needs to distinguish between a potato and a clod, determine its position on the belt, and eventually trigger the correct pneumatic finger when the clod reaches the end of the conveyor. Picture 5 shows roughly the view a camera would have of the conveyor belt with potatoes and clods. https://preview.redd.it/ztlx5h76doqh1.png?width=605&format=png&auto=webp&s=f8bc97d1485c329b4df4bd5d029a1efe13d7caad Picture 5: Conveyor belt with potatoes and clods When it comes to vision and ejector hardware I am thinking of using 1 or 2 global-shutter cameras mounted on top of the 1-meter feed conveyor in an enclosed environment with LED lighting and 20 pneumatic ejector fingers across the width of the conveyor belt. My questions would be: Are 1 or 2 global-shutter cameras a realistic starting point for this kind of application? What kind of cameras would you suggest? Would you build this from standard pneumatic cylinders and valves, or are there existing modules/components that would make much more sense for my situation? When it comes to the software, I’m not a professional programmer so I would need to rely as much as possible on existing camera SDKs, vision frameworks and libraries rather than inventing everything from scratch. Conceptually I imagine the system as: Camera → detect potato/clod → determine position → track conveyor movement → select ejector finger(s) → fire at exactly the right moment. First a vision computer decides what needs to be rejected and where it is. Second, an encoder tracks how far the conveyor has moved. Lastly a PLC/Real-time controller handles the timing of the pneumatic valves. My questions would be: Is this realistically something I can build myself without professional programming experience, or am I underestimating how much expertise this requires? Does my concept make sense, or am I underestimating the integration and timing problem of the vision computer, encoder and PLC controller? How hard can this be? I understand very well that this is not a simple project and that is the reason why I’m posting here first. I would like to get your feedback and insights on my ideas and project. Thank you!

1d ago

---

---

## Google News: "robotics"

**[China slows humanoid robot IPO rush as hype outruns reality](https://www.reuters.com/business/finance/china-slows-humanoid-robot-ipo-rush-hype-outruns-reality-2026-09-21/)**

Reuters • 22h ago

---

**[Boston Dynamics Opens Robotics Metaplant Application Center to Train Humanoid Robots for Manufacturing Tasks](https://bostondynamics.com/news/boston-dynamics-opens-robotics-metaplant-application-center-to-train-humanoid-robots-for-manufacturing-tasks/)**

Boston Dynamics today announced the next chapter in its robotics and AI strategy with the launch of the Robotics Metaplant Application Center (RMAC)

Boston Dynamics • 10h ago

---

**[Humanoid robots fight in cage match in Shanghai](https://www.aljazeera.com/video/newsfeed/2026/9/20/humanoid-robots-fight-in-cage-match-in-shanghai)**

Humanoid robots fight in cage match in Shanghai

Al Jazeera • 1d ago

---

**[Behold: Video of "First-Ever" Human Versus Robot MMA Fight](https://futurism.com/robots-and-machines/first-ever-human-versus-robot-mma-fight)**

A new viral video making the rounds on social media shows a humanoid robot fighting a TikTok influencer in the ring.

Futurism • 7h ago

---

**[Boston Dynamics' humanoid robots start training at Hyundai plant](https://www.axios.com/local/boston/2026/09/21/boston-dynamics-humanoid-robots-hyundai-metaplant)**

Axios • 6h ago

---

**[Boston Dynamics opens Metaplant Application Center to train Atlas humanoids](https://www.therobotreport.com/boston-dynamics-opens-metaplant-application-center-train-atlas-humanoid-robots/)**

The new Robotics Metaplant Application Center is training humanoids as part of Hyundai's Metaplant America in Georgia.

The Robot Report • 12h ago

---

**[Dongfeng to trial-produce humanoid robots by year-end, targets human-level capability by end of 2027](https://cnevpost.com/2026/09/20/dongfeng-trial-produce-humanoid-robots-year-end/)**

Dongfeng's humanoid robot will enter factories in October to handle sorting and quality inspection, with small-batch trial production to begin at the end of the year.

CnEVPost • 1d ago

---

**[Humanoid robot sales tally hit 7,000 globally last year](https://www.reuters.com/technology/humanoid-robot-sales-tally-hit-7000-globally-last-year-2026-09-21/)**

Reuters • 2h ago

---

**[Scientists Create New Humanoid Robot That Flinches in Fear When You Come Close](https://futurism.com/robots-and-machines/new-humanoid-robot-flinches-human-close)**

Robotics company Agility Robotics' latest humanoid robot cowers in fear and drops to its knees when a human turns the corner.

Futurism • 1d ago

---

**[Folkestone school's robotics team aims to inspire next generation](https://www.bbc.com/news/articles/cmwyz83xgn9jo)**

The group from Folkestone is set to compete at the First Global Challenge in South Korea.

BBC • 20h ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s T800 Fights People Now #robot #ai #robotics](https://www.youtube.com/watch?v=KVxA_EHk88U)**

China's T800 is now fighting worldwide against both robots and humans. EngineAI is ramping up production of its ...

📺 Kalil 4.0

👁️ 2K • 👍 51 • 💬 9 • ⏱️ 1:16 • 5h ago

---

**[ITKAN x SWYFT BIOBUZZ Ri3D Intake Analysis #ftc #biobuzz #robotics #first #swyft #itkan #ri3d](https://www.youtube.com/watch?v=AOzftXADIVA)**

ITKAN x SWYFT BIOBUZZ Ri3D Intake Analysis #ftc #biobuzz #robotics #first #swyft #itkan #ri3d.

📺 SWYFT Robotics

👁️ 608 • 👍 3 • ⏱️ 0:20 • 1h ago

---

**[Nidal Wonder Challenges a Human Robot.. 😰](https://www.youtube.com/watch?v=VNnlaQEMg6E)**

shorts #robot #nalish #flipoff #flips #crazy #viral.

📺 Aycid

👁️ 4K • 👍 106 • 💬 2 • ⏱️ 0:38 • 1h ago

---

**[The SELF-AWARE ROBOT Has Taken Over The World | I Made A Self-Aware Robot](https://www.youtube.com/watch?v=GzlKjm-nl2M)**

LIGHTS ARE OFF Channel: @LIGHTSAREOFF My last video on The Self-Aware Robot: https://youtu.be/F_MES5VHue8 In todays ...

📺 EmortalMarcus

👁️ 308K • 👍 10K • 💬 857 • ⏱️ 55:24 • 2d ago

---

**[Chinese robots dance their way into America’s Got Talent finale](https://www.youtube.com/watch?v=_Xr9NxyG_GU)**

Subscribe to our YouTube channel for free here: https://sc.mp/subscribe-youtube Read more about this topic: https://sc.mp/8185aa ...

📺 South China Morning Post

👁️ 94K • 👍 934 • 💬 174 • ⏱️ 2:40 • 18h ago

---

**[World’s first human vs. robot fight](https://www.youtube.com/watch?v=CDsX4KP0HhA)**

The world's FIRST human vs. robot fight. Is the end near or do we still stand a chance? #robot.

📺 Frankie Lapenna

👁️ 3.3M • 👍 136K • 💬 11K • ⏱️ 0:45 • 1d ago

---

**[How To Destroy A Self-Aware Robot](https://www.youtube.com/watch?v=B0-v46oMCp4)**

I got a little bit bored so we saw How To Destroy A Self-Aware Robot SUBSCRIBE TO GOAT @LIGHTSAREOFF New Merch ...

📺 Socks Live 

👁️ 190K • 👍 5K • 💬 554 • ⏱️ 36:24 • 1d ago

---

**[AI Robots Are OUT OF CONTROL… It&#39;s Already Starting!](https://www.youtube.com/watch?v=V0wAGFaV_Ew)**

AI robots are getting OUT OF CONTROL. From humanoid robots chasing people with knives and handling guns to robot fights, ...

📺 MindSeeded

👁️ 884K • 👍 14K • 💬 2K • ⏱️ 16:24 • 4d ago

---

**[4K Djedi Robot Entered the Great Pyramid&#39;s Sealed Shaft - Revealing NEVER Before SEEN Footage](https://www.youtube.com/watch?v=pvANZ5xuBQU)**

The Djedi robot explored a sealed shaft inside the Great Pyramid, capturing the first images of a mysterious second barrier.

📺 IMPOSSIBLE ARCHIVES

👁️ 640K • 👍 4K • 💬 266 • ⏱️ 11:34 • 2d ago

---

**[I Cheated Mark Rober&#39;s Casino with a Robot](https://www.youtube.com/watch?v=hZgIaDdPkTQ)**

I Built a Robot Poker Chip to cheat at Roulette. PCBWay is the best place to order your PCBs, 3D Prints and CNC'd parts.

📺 Concept Bytes

👁️ 75K • 👍 1K • 💬 109 • ⏱️ 14:41 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

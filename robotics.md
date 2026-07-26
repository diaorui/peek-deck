---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-26T12:38:13.640670+00:00'
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

**Last Updated:** July 26, 2026 at 12:38 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I moved my 3D-printed robot lamp to a Raspberry Pi 5 and added controllable lighting](https://www.reddit.com/r/robotics/comments/1v6gd10/i_moved_my_3dprinted_robot_lamp_to_a_raspberry_pi/)**

A small update on my robotic desk lamp: the entire control system now runs on a Raspberry Pi 5. The lamp uses 24 V RobStride BLDC servo motors connected over CAN. The Raspberry Pi now handles motor control, lighting, and animation playback locally, so the lamp no longer needs to be continuously controlled by my main PC. I still use a separate animation editor that I built for creating movements. Each joint has its own timeline with position keyframes, velocity, torque limits, and controller parameters. Finished animations are sent to the lamp and played back locally. I’ve also installed an addressable LED ring with a 3D-printed diffuser inside the head. Brightness and transitions are now part of the same animation timeline, allowing the light to be synchronized with movement. This video is a quick test of the new setup. I’m currently tuning the motor parameters, brightness curves, and transition timings before using the light in more expressive animations.

17h ago

---

**[Probably on of the cutest humanoids, i wouldn’t mind this little dude doing my laundry](https://www.reddit.com/r/robotics/comments/1v6xull/probably_on_of_the_cutest_humanoids_i_wouldnt/)**

4h ago

---

**["Gave my DIY arm a new 'shoulder' and it feels brand new."](https://www.reddit.com/r/robotics/comments/1v6qvk3/gave_my_diy_arm_a_new_shoulder_and_it_feels_brand/)**

Just finished modifying the arm holder/mount for my DIY robot. The old PLA bracket was flexing too much under load, so I redesigned it to be sturdier. Watch the clip to see the improved range of motion. The difference is night and day. No more wobbly joints! Next step is to test the weight capacity.

10h ago

---

**[Analog integrating gyroscope](https://www.reddit.com/r/robotics/comments/1v6n6e3/analog_integrating_gyroscope/)**

Built from a 1980s RC helicopter mechanical rate gyro (futaba) and continuous rotation servo. The gyro normally has centering springs but they have been removed to increase sensitivity. The gyro has a hall effect sensor in it and an analog circuit which generates PWM pulses that the servo uses as a velocity control. A 3 axis version of this arrangement is what made the Apollo guidance computer so accurate at knowing its own pose over long distances and times. This single axis version could be a gyrocompass in a robot or aircraft, to maintain heading even if the magnetic compass quits working etc Now we have laser ring gyros and other extremely accurate solid state sensors and amazing computational power and algorithms to integrate the readings to probably surpass any internal flywheel arrangements accuracy.

13h ago

---

**[Pouring cup Robot](https://www.reddit.com/r/robotics/comments/1v61zoy/pouring_cup_robot/)**

1d ago

---

**[Cubic Doggo Upgrade: Walking with IMU!](https://www.reddit.com/r/robotics/comments/1v69uqf/cubic_doggo_upgrade_walking_with_imu/)**

Hello hello, development of the upgrade, CubicDoggo 06R (High Mobility, sort of), is now complete, and the full project is documented on GitHub: https://github.com/SphericalCowww/CubicDoggo_06R The previous post can be found here. But yeah, the performance is not as ideal. You can see it's still wobbling when just standing there, and the IMU is not even balanced to be parallel to the ground. The effect of the IMU during walking is also difficult to notice because of how wonky it walks to begin with and how bad I am at controlling it to walk in a straight line, lol. However, you can see the subtle sign right before it stops walking. Its front-right leg is fully extended. This is also why I hit the stop button, because the next step may make the joint flip backwards, causing it to fall. Happened a few times, actually. Without IMU, though, what happens is worse, in that it simply tumbles and rolls over. Also happened a few times, oh well. Next step will be 06Z Neucommu with simulation and RL, and 07B Wouf with stronger servos (a lot of mechanical reinforcement was actually planned for 07B). This is no Unitree superdog, but I am still excited about its progress and enjoy all the Reddit discussions :)

22h ago

---

**[Anybody with a pen plotter here?](https://www.reddit.com/r/robotics/comments/1v6ys9j/anybody_with_a_pen_plotter_here/)**

I am from India, and want someone here, with a pen plotter to make some work using it. I want paper sizes from a5 to A1 (chart paper).

3h ago

---

**[Polka v0.5 Released! All-in-one ROS2 Lidar node](https://www.reddit.com/r/robotics/comments/1v65bx1/polka_v05_released_allinone_ros2_lidar_node/)**

I’ve just released Polka v0.5.0! It’s an efficient 2D/3D Lidar processing node handling merging, filtering, and deskewing. This update brings 6.2x faster deskewing, live parameter tuning, smarter IMU handling, and a built-in diagnostics dashboard. If it saves your perception stack compute and brings a faster solution, please drop a star! https://github.com/Pana1v/polka It supports 5 distros.

1d ago

---

**[How an Event Camera Works: An Interactive Explanation](https://www.reddit.com/r/robotics/comments/1v6puyq/how_an_event_camera_works_an_interactive/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://youtube.com/watch?v=df-fBJkoO-E&si=swBepOPHO9tFu9xD) • 11h ago

---

**[AC/DC Control Interface](https://www.reddit.com/r/robotics/comments/1v6f016/acdc_control_interface/)**

https://www.youtube.com/@ALMA.Industries Built a control panel with on/off switches to control DC power supplies (48v, 12v, 24v). AC Outlets always give power regardless of switch states. Used hold home outlets and switches. Turns out to be something I use quite frequently. Full build is in the link above.

18h ago

---

---

## Google News: "robotics"

**[The Robots Cometh](https://time.com/article/2026/07/23/unitree-china-human-robotics/)**

The humanoid revolution is coming—and the Chinese firm Unitree is leading the charge.

Time Magazine • 3d ago

---

**[What's Next for Humanoids After This Week's Cage Match and Cowboying?](https://spectrum.ieee.org/video-friday-physical-ai-robotics)**

Your weekly selection of awesome robot videos

IEEE Spectrum • 1d ago

---

**[With Washington’s help, humanoid robots can transform US manufacturing](https://thehill.com/opinion/technology/5988461-ai-humanoid-robotics-policy/)**

The Hill • 1d ago

---

**[Robotics Startup Genesis in Talks to Raise at $3 Billion Valuation](https://www.bloomberg.com/news/articles/2026-07-23/robotics-startup-genesis-in-talks-to-raise-about-500-million)**

Bloomberg.com • 2d ago

---

**[Spider-inspired four-legged robot boat could track and retrieve people from water](https://interestingengineering.com/ai-robotics/four-legged-robotic-boat-water-rescues)**

A four-legged robotic boat inspired by fishing spiders could track and retrieve people from water during rescue missions.

Interesting Engineering • 1d ago

---

**[Hooper turned robotics engineer? Franck Kepnang walks through unique academic path](https://www.on3.com/teams/kentucky-wildcats/news/hooper-turned-robotics-engineer-franck-kepnang-walks-through-unique-academic-path/)**

Kentucky's 7-foot shot-blocker has a fascinating life outside of basketball.

On3 • 1d ago

---

**[Mobileye CEO Amnon Shashua to step aside as company pushes into robotaxis, robotics](https://techcrunch.com/2026/07/23/mobileye-ceo-amnon-shashua-to-step-aside-as-company-pushes-into-robotaxis-robotics/)**

Shashua has been invited to take the chairman of the board seat.

TechCrunch • 2d ago

---

**[Tech Moves: Agility Robotics gets CFO; Microsoft security departure; Zap's legal officer; new KEXP CPTO](https://www.geekwire.com/2026/tech-moves-agility-robotics-gets-cfo-microsoft-security-departure-zaps-legal-officer-new-kexp-cto/)**

Agility Robotics names a CFO ahead of its plans to go public, moving its current CFO/COO into an operations-focused role. Microsoft loses another security leader while Zap Energy gets a chief legal officer.

GeekWire • 2d ago

---

**[AMD Lays Out AI Vision Across Cloud, Client And Robotics (AMD)](https://seekingalpha.com/article/4925512-amd-lays-out-ai-vision-across-cloud-client-robotics)**

Seeking Alpha • 1d ago

---

**[Israeli researchers teach micro-robots to scale obstacles and carry living bacteria](https://www.ynetnews.com/health_science/article/r18zdgxrmg)**

Tel Aviv University researchers develop micro-robots that use magnetic and electric fields to cross obstacles, move between surfaces and transport delicate biological cargo

Ynetnews • 7h ago

---

---

## YouTube Videos: "robotics"

**[Real-Time Omni-Modal Interaction Driven Whole-Body Mobile Manipulation](https://www.youtube.com/watch?v=IiNbFPOUrz8)**

Unitree UnifoLM-OminiA-0.3 — a single model handling diverse home-care and wellness tasks, with omni-modal interactive ...

📺 Unitree Robotics

👁️ 3.3M • 👍 2K • 💬 438 • ⏱️ 2:15 • 6d ago

---

**[A Silicon Valley company with Eric Trump as an advisor is making robot soldiers](https://www.youtube.com/watch?v=9O2iIZt25p4)**

One Silicon Valley company thinks that robot soldiers are the future of warfare. Eric Trump is an advisor and they've already got a ...

📺 NBC News

👁️ 16K • 👍 165 • 💬 90 • ⏱️ 5:29 • 3d ago

---

**[They&#39;re Giving Robots &#39;Smart Skin&#39; Now (I Touched It)](https://www.youtube.com/watch?v=3vGWIPIDpB4)**

Gene.01 is the new humanoid robot from Generative Bionics, featuring "smart skin" embedded with touch sensors and proximity ...

📺 CNET

👁️ 488 • 👍 50 • 💬 4 • ⏱️ 4:23 • 38m ago

---

**[America Doesn&#39;t Know What&#39;s Coming...China&#39;s Robot Factories](https://www.youtube.com/watch?v=3UEfc0XqJJ0)**

America Doesn't Know What's Coming | China's Robot Factories Chengdu is usually known for pandas, hotpot, teahouses, old ...

📺 Living in China

👁️ 81K • 👍 2K • 💬 203 • ⏱️ 12:28 • 4d ago

---

**[Humanoid Robotics at the BMW Group Plant Spartanburg [4K]](https://www.youtube.com/watch?v=NFD0i63FDFk)**

BMW Group intensifies the use of digitalization and the use of artificial intelligence (AI) in production. With so-called Physical AI, ...

📺 The Wheel Network

👁️ 22K • 👍 462 • 💬 134 • ⏱️ 6:24 • 4d ago

---

**[What’s Wrong with Japanese Robotics and AI?](https://www.youtube.com/watch?v=gkzxgJH2Wzc)**

For business inquiries: info.prorobots@gmail.com ✓ Instagram: https://www.instagram.com/pro_robots Did Japan Lose the ...

📺 PRO ROBOTS

👁️ 11K • 👍 328 • 💬 39 • ⏱️ 15:59 • 6d ago

---

**[Unitree AS2 W Shows The Future Of Autonomous Robots](https://www.youtube.com/watch?v=OePErI3OoRI)**

The new Unitree AS2-W is changing what wheel-legged robots can do. Watch it climb steep rocks, cross streams, tackle rough ...

📺 DPCcars

👁️ 17K • 👍 146 • 💬 59 • ⏱️ 2:32 • 1d ago

---

**[Losing a Head Doesn&#39;t Stop This Robot From Battling Another in the Ring](https://www.youtube.com/watch?v=FEcPelBd9t0)**

Humanoid robots fought inside a cage at a tournament in China. The two exchange a fury of blows before the black robot loses it's ...

📺 New York Post

👁️ 48K • 👍 944 • 💬 409 • ⏱️ 2:02 • 3d ago

---

**[China’s T800 Robots Fight Just SHOCKED the World!](https://www.youtube.com/watch?v=QbnCPSLDkpw)**

A humanoid robot named Matador took a brutal high kick to the head, and its head rolled across the cage floor. Then Matador ...

📺 NextGen Humanoids

👁️ 21K • 👍 448 • 💬 84 • ⏱️ 8:56 • 6d ago

---

**[A Chinese Robot Just Decapitated Another Robot In Public. Nobody Asked What Comes Next](https://www.youtube.com/watch?v=rUjlFRok3qk)**

Everyone is asking if killer robots are coming. Wrong question. One already knocked another robot's head clean off, on camera ...

📺 Ambrose In China

👁️ 694K • 👍 24K • 💬 5K • ⏱️ 2:25 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

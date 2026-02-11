---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-11T22:40:55.598126+00:00'
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

**Last Updated:** February 11, 2026 at 22:40 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Boston Dynamics veteran and CEO, Robert Playter, steps down after more than 30 years with company](https://www.reddit.com/r/robotics/comments/1r23voi/boston_dynamics_veteran_and_ceo_robert_playter/)**

Boston Dynamics CEO Robert Playter told staff on Tuesday that he'll be stepping down from the company. He first joined Boston Dynamics in 1994.

🔗 [Business Insider](https://www.businessinsider.com/boston-dynamics-ceo-robert-playter-steps-down-memo-2026-2) • 5h ago

---

**[Advice on Designing This Type of Track System](https://www.reddit.com/r/robotics/comments/1r24nqf/advice_on_designing_this_type_of_track_system/)**

I’m interested in designing a robot with wheels and tracks similar to this style, but I don’t yet have much experience developing this type of system from scratch. I have some knowledge of AutoCAD and recently started using Fusion 360 with the goal of learning more about project development focused on robotics. I’m able to interpret technical drawings in multiple views and model them in 3D, as well as replicate existing models. However, my experience is limited to that. I have never designed a complete system entirely from scratch, especially something like an articulated track system that works together with drive wheels. I would appreciate guidance or advice on how to properly start and structure this kind of project.

4h ago

---

**[Wish I started Robotics Sooner, what should I do?](https://www.reddit.com/r/robotics/comments/1r1smj4/wish_i_started_robotics_sooner_what_should_i_do/)**

Hey. I'm a 2nd year college student who just recently switched into my school's Electrical Engineering program and even though I'm still young (20) I wish I started tinkering with robots/soldering sooner. Money is not an issue, so I'm wondering what you guys would recommend I do to push myself closer to working on robot design/doing things that scratch that itch.

13h ago

---

**[Beginner Robotics Club.](https://www.reddit.com/r/robotics/comments/1r1lequ/beginner_robotics_club/)**

Hey everyone! I'm going to be starting a robotics club at my community college and I was hoping I could get some help on some beginner friendly projects for the club and maybe how the club should be structured. I, and most of the people I know that are going to be a part of the club have basically no experience with robotics and we want to keep the club inclusive to everyone on campus. Any advice would help!

19h ago

---

**[Simulation / Digital Twin of a Robot Arm Ball Balancing Setup](https://www.reddit.com/r/robotics/comments/1r1sr70/simulation_digital_twin_of_a_robot_arm_ball/)**

Hi everyone, I currently have a real-world setup consisting of a UR3e with a flat square platform attached to the end effector. There’s a ball on top of the platform, and I use a camera detection pipeline to detect the ball position and balance it. The controller is currently a simple PID (though I’m working toward switching to MPC). Now I want to build a digital twin / simulation of this system. I’m considering MuJoCo, but I have zero experience with it. I’ve also heard about something like the ROS–Unity integration / ROS Unity Hub, and I’m not sure which direction makes more sense or where I should start. What I want to achieve in simulation: Import a URDF of the UR3e Attach a static square platform to the end effector (this part seems straightforward) Add a ball that rolls on top of the platform Have proper collision and physics behavior The platform has four sides (like a shallow box), so if the ball hits the edge, it should collide and stop rather than just fall off If the end effector tilts, the plate tilts The ball should realistically roll “downhill” due to gravity when the plate is tilted So my main physics questions: Is this realistically achievable in both MuJoCo and Unity? Can I define proper rolling friction and contact friction between the ball and the plate? Will the physics engine handle realistic rolling behavior when I tilt the TCP? Matching Simulation to Reality (Friction Identification) Another big question: how would you recommend estimating the friction coefficients from the real system so I can plug them into the simulation? I was thinking something along the lines of: Tilt the plate to a known angle Measure how long the ball takes to travel across a 40 cm plate Repeat multiple times Use that data to estimate an effective friction coefficient Is that a reasonable approach? Are there better system identification methods people typically use for this kind of setup? Real-Time Digital Twin Long-term, I would like: When the real robot is balancing the ball, the simulated version reflects the same joint motions and plate tilt. While working purely in simulation, I’d also like a simulated camera plugin that gives me the ball position, which feeds into my detection pipeline and controller (PID now, possibly MPC later). So effectively: Simulation → virtual camera → detection → controller → robot motion And eventually also: real robot → mirrored digital twin Main Questions Would you recommend MuJoCo or Unity (ROS integration) for this use case? Where would you start if you had zero experience with both? Is one significantly better for contact-rich rolling dynamics like this? Has anyone built something similar (ball balancing / contact dynamics on a robot arm)? I also found a Unity UR simulation project that I can link below if helpful. Any guidance on architecture, tools, or first steps would be greatly appreciated. Thanks! TL;DR: I have a UR3e ball-balancing setup and want to build a physics-accurate digital twin (with rolling friction, collisions, and camera simulation). Should I use MuJoCo or Unity/ROS, and how would I match real-world friction parameters to simulation? Links: - https://github.com/rparak/Unity3D_Robotics_UR

13h ago

---

**[La funny song](https://www.reddit.com/r/robotics/comments/1r1lrig/la_funny_song/)**

19h ago

---

**[I built URDFViewer.com, a robotic workcell analysis and visualization tool](https://www.reddit.com/r/robotics/comments/1r1f3dp/i_built_urdfviewercom_a_robotic_workcell_analysis/)**

While developing ROS2 applications for robotic arm projects, we found it was difficult to guarantee that a robot would execute a full sequence of motion without failure. In pick-and-place applications, the challenge was reaching a pose and approaching along a defined direction. In welding or surface finishing applications, the difficulty was selecting a suitable start pose without discovering failure midway through execution. Many early iterations involved trial and error to find a working set of joint configurations that could serve as good “seeds” for further IK and motion planning. Over time, we built internal offline utilities to nearly guarantee that our configurations and workspace designs would work. These relied heavily on open-source libraries like TRAC-IK, along with extracting meaningful metrics such as manipulability. Eventually, we decided to package the internal tool we were using and open it up to anyone working on robotic application setup or pre-deployment validation. What the platform offers: a. Select from a list of supported robots, or upload your own. Any serial chain in standard robot_description format should work. b. Move the robot using interactive markers, direct joint control, or by setting a target pose. If you only need FK/IK exploration, you can stop here. The tool continuously displays end-effector pose and joint states. c. Insert obstacles to resemble your working scene. d. Create regions of interest and add orientation constraints, such as holding a glass upright or maintaining a welding direction. e. Run analysis to determine: Whether a single IK branch can serve the entire region Whether all poses within the region are reachable Whether the region is reachable but discontinuous in joint space How we hope it helps users: a. Select a suitable robot for an application by comparing results across platforms. b. Help robotics professionals, including non-engineers, create and validate workcells early. c. Create, share, and collaborate on scenes with colleagues or clients. We’re planning to add much more to this tool, and we hope user feedback helps shape its future development. Give it a try.

🔗 [urdfviewer.com](https://urdfviewer.com) • 1d ago

---

**[K-bot](https://www.reddit.com/r/robotics/comments/1r18pvw/kbot/)**

Hello everyone, since K-Scale Labs (https://kscale.ai) shut down and they still kept everything open-source on their GitHub page, I was wondering if anyone has actually tried to build their humanoid robot on their own. Do you guys think it would be worth it or not and why?

1d ago

---

**[The world's first 'biomimetic AI robot' just strolled in from the uncanny valley - and yes, it's super-creepy](https://www.reddit.com/r/robotics/comments/1r0zrzk/the_worlds_first_biomimetic_ai_robot_just/)**

A Shanghai startup, DroidUp, has unveiled Moya, a biomimetic AI robot designed to cross the uncanny valley. Unlike plastic and metal droids, Moya features silicone skin that is heated to human body temperature and mimics subtle facial expressions like eyebrow raises. Standing 5'5" and weighing 70 lbs, Moya is built on a modular platform that allows for swapping between male and female presentations. With a price tag of ~$173k, DroidUp aims to deploy these warm companions in healthcare and business by late 2026.

🔗 [TechRadar](https://www.techradar.com/computing/the-worlds-first-biomimetic-ai-robot-just-strolled-in-from-the-uncanny-valley-and-yes-its-super-creepy) • 1d ago

---

**[Connections for ball balancing robot!](https://www.reddit.com/r/robotics/comments/1r1ovz3/connections_for_ball_balancing_robot/)**

So I am working on the project of ball balancing robot so the body after robots has been the three servo motor and connections I have no idea so the components for the connections are arduino, IMU sensor (MPU9250/6500)., ESR-32,PCA9685... So these are the components which I am having for ball balancing robot I kindly request you to suggest me how to made the connection of it it may be you guys can suggest me like any article for that or a YouTube video and if required for more components kindly let me know it will be grateful I just have one week for the project to be submitted....

17h ago

---

---

## Google News: "robotics"

**[Upside Robotics is reducing fertilizer use and waste in corn crops](https://techcrunch.com/2026/02/11/upside-robotics-is-reducing-fertilizer-use-and-waste-in-corn-crops/)**

Upside Robotics builds autonomous solar-powered robots that can help farmers reduce their fertilizer use by 70%.

TechCrunch • 6h ago

---

**[Haply Robotics raises $16 million to build the “steering wheels” for physical AI](https://betakit.com/haply-robotics-raises-16-million-to-build-the-steering-wheels-for-physical-ai/)**

How the Montréal startup plans to own the touch layer of robotics.

BetaKit • 2d ago

---

**[Symbotic acquires autonomous forklift maker Fox Robotics](https://www.therobotreport.com/symbotic-acquires-autonomous-forklift-maker-fox-robotics/)**

Symbotic has acquired autonomous forklift developer Fox Robotics in a move that broadens its logistics robotics offerings.

The Robot Report • 1d ago

---

**[China's Alibaba launches AI model to power robots as tech giants talk up 'physical AI'](https://www.cnbc.com/2026/02/10/alibaba-ai-model-robotics-rynnbrain-china.html)**

Nvidia and Google are among a handful of major tech giants developing models for robotics and so-called "phyiscal AI."

CNBC • 1d ago

---

**[AI In Robotics - New Position Paper](https://ifr.org/ifr-press-releases/news/ai-in-robotics-new-position-paper)**

A new generation of AI-powered robots moving from research labs into the real world is fueled by AI tech companies and analysts forecasting a multitrillion-dollar market. The vision is to give artificial intelligence its own robot body. What are the trends, challenges, and commercial applications?

IFR International Federation of Robotics • 1d ago

---

**[Construction Embraces AI Agents, Safety Systems and Robotics as Labor Pressures Mount](https://www.pymnts.com/artificial-intelligence-2/2026/construction-embraces-ai-agents-safety-systems-and-robotics-as-labor-pressures-mount/)**

Artificial intelligence is no longer confined to experimental pilots in the construction industry. It is moving into the operational core of how projects

PYMNTS.com • 19h ago

---

**[Robot dogs become first responders for police at 2026 World Cup](https://interestingengineering.com/ai-robotics/mexico-robot-dogs-world-cup-security)**

Mexico will deploy robot dogs during the 2026 World Cup to scout threats and protect police before officers intervene.

Interesting Engineering • 1d ago

---

**[Tesla stock gets latest synopsis from Jim Cramer: ‘It’s actually a robotics company’](https://www.teslarati.com/tesla-tsla-gets-latest-synopsis-jim-cramer-actually-obotics-company/)**

Tesla stock got its latest synopsis from Wall Street analyst Jim Cramer, who finally realized something that many fans of the company have known all along: it's not a car company. Instead, it's a robotics company.

Teslarati • 3h ago

---

**[AI, Robotaxis, and Robotics: Why Elon Musk and Tesla Are Set to Join "Magnificent Seven" Peers on a Massive Spending Spree](https://www.fool.com/investing/2026/02/09/ai-robotaxis-robotics-elon-musk-tesla-mag-7/)**

The once-thriving electric vehicle leader is investing in a new future.

The Motley Fool • 2d ago

---

**[Tesla's Robotics Revolution Won't Save It (NASDAQ:TSLA)](https://seekingalpha.com/article/4867567-teslas-robotics-revolution-would-not-save-it)**

Seeking Alpha • 2d ago

---

---

## YouTube Videos: "robotics"

**[Boston Dynamics New ATLAS Just Went Full Human Mode (Insane Upgrade)](https://www.youtube.com/watch?v=9aaE5BkD0Ls)**

A massive robotics shift is unfolding right in front of us. Boston Dynamics has revealed a major new Atlas update developed with ...

📺 AI Revolution

👁️ 40K • 👍 1K • 💬 99 • ⏱️ 11:59 • 23h ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 265K • 👍 5K • 💬 984 • ⏱️ 13:31 • 6d ago

---

**[Elon Musk on Why Everyone Will Want an Optimus Robot by 2027](https://www.youtube.com/watch?v=dWRqUdVBKjE)**

Will a robot soon be watching your children or caring for your parents? Elon Musk predicts a future where billions of humanoid ...

📺 SpaceTakers

👁️ 49K • 👍 928 • 💬 85 • ⏱️ 0:29 • 6d ago

---

**[China&#39;s Pink Hair Humanoid Robot Craze! #humanoidrobot #robotics #robot](https://www.youtube.com/watch?v=hZAnVumhgv4)**

Pink haired humanoid robots are trending in China. Xuan, the hyper-realistic robotic elf developed by AheadForm, sang a love ...

📺 Kalil 4.0

👁️ 2K • 👍 68 • 💬 2 • ⏱️ 0:57 • 18h ago

---

**[Chinese Robotic Hand With Human Level Dexterity](https://www.youtube.com/watch?v=ynodBTnsuis)**

Pan Motor's Wuji Hand packs twenty fully actuated joints into a sub six hundred gram robotic hand, delivering fine motor control, ...

📺 Deepen

👁️ 29K • 👍 480 • 💬 12 • ⏱️ 0:19 • 3d ago

---

**[Tesla Was Never a Car Company #teslaoptimus  #elonmusk  #teslarobot  #teslabotgen3 #humanoidrobots](https://www.youtube.com/watch?v=slqW7zBA6Oc)**

They laughed when Elon Musk brought a man in a spandex suit on stage. But in 2026, nobody is laughing. Tesla was never a car ...

📺 By 2050

👁️ 1.1M • 👍 18K • 💬 476 • ⏱️ 1:00 • 3d ago

---

**[SHOCKING: XPeng’s New IRON Robot COLLAPSES in Public...](https://www.youtube.com/watch?v=4MNfUBZNRFU)**

XPeng's brand-new IRON humanoid robot just collapsed in public, and the footage has taken the internet by storm. In this video ...

📺 The AI Nexus

👁️ 8K • 👍 142 • 💬 35 • ⏱️ 19:22 • 6d ago

---

**[The real test for humanoid robots isn’t performance.](https://www.youtube.com/watch?v=4iU9kfIZnhs)**

Humanoid robots don't fail at tasks. They fail at presence. The hardest part of building humanoid robots isn't hardware.

📺 Slidebean

👁️ 14K • 👍 503 • 💬 27 • ⏱️ 1:21 • 1d ago

---

**[Elon: This Robot Could Replace Surgeons👀 #elonmusk #ai #Robotics #Optimus #Innovation #surgeon](https://www.youtube.com/watch?v=BHKQFCh-7fg)**

A bold prediction like this instantly sparks curiosity and debate across the world. The idea that advanced robotics and artificial ...

📺 Billionaire Shots

👁️ 13K • 👍 812 • 💬 101 • ⏱️ 0:36 • 1d ago

---

**[Atlas Airborne | Boston Dynamics &amp; @rai-inst](https://www.youtube.com/watch?v=UNorxwlZlFk)**

Now that the Atlas enterprise platform is getting to work, the research version gets one last run in the sun. Our engineers made ...

📺 Boston Dynamics

👁️ 1.4M • 👍 41K • 💬 4K • ⏱️ 1:38 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

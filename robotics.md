---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-27T14:34:46.383961+00:00'
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

**Last Updated:** April 27, 2026 at 14:34 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[We're open-sourcing Asimov v1, a humanoid robot](https://www.reddit.com/r/robotics/comments/1swz3ob/were_opensourcing_asimov_v1_a_humanoid_robot/)**

We're open-sourcing Asimov v1, a humanoid robot. We're releasing the mechanical design files and simulation model for a full-size humanoid robot. So you can build it, customize it, and train on it. Asimov v1 is 1.2 m tall, 35 kg, with 25 actuated degrees of freedom. Structural parts machined in 7075 aluminium and 3D-printed in MJF PA12 nylon. Height: 1.2 m Weight: 35 kg Degrees of Freedom: 25 actuated + 2 passive Legs: 6 DOF x 2 + toe x 2 Arms: 5 DOF x 2 (shoulder pitch/roll/yaw, elbow, wrist yaw) Torso: 1 DOF waist yaw, 10 W 4 ohm speaker, 6 DOF IMU Head: 2 DOF neck (neck yaw, neck pitch), Quad microphone array, 2MP monocular camera CAN Bus: 5 @ 1Mbps + 1 @ 500kbps Onboard Compute: Raspberry Pi 5 (media + network) + Radxa CM5 (motion control) Structural Materials: 7075 aluminium, MJF PA12 nylon The simulation model runs on MuJoCo. 25 actuated joints, 28 link meshes, friction-tuned foot contacts. Ready for locomotion policy training out of the box. Links: GitHub: github.com/asimovinc/asimov-v1 User Manual: manual.asimov.inc Most humanoid robots are controlled by the companies that build them. Asimov v1 is built for the rest of us. Build it, test it, and share your feedback with the community.

4h ago

---

**[An Open-Source Exoskeleton Project - OpenEXO](https://www.reddit.com/r/robotics/comments/1swy8r0/an_opensource_exoskeleton_project_openexo/)**

Here is their website OpenEXO. Perhaps it can help you build your first exoskeleton. They are currently developing and updating a new generation of exoskeletons.

5h ago

---

**[I tried to build a 5 DOF robot arm](https://www.reddit.com/r/robotics/comments/1swqpml/i_tried_to_build_a_5_dof_robot_arm/)**

So this is a project I built a while ago and put on hold while I plan some upgrades. I just wanted to share it with the community and some things I've learned/experienced along the way. Build details are here: https://www.hackster.io/ian-hong/completely-custom-built-5-axis-robot-arm-515001 Kinematics The frame assignment of the D-H method is quite painful and every resource online has a slightly different (and sometimes ambiguous) explanation, but none was 100% correct. To solve the inverse kinematics analytically, you can decouple the first 3 joints (responsible for position) and the wrist joints (responsible for rotation). Pure position control is not sufficient for smooth motions because each joint moves a different amount. Hardware 3D printed parts are not as accurate as I would have liked. A snug fit in the bearings would sometimes cause the joints to lock up because they rotate slightly eccentrically. The backlash in the servo gears are not to be underestimated. Turning them by hand, they feel solid, but when you have a 100mm+ lever arm to it, you really notice the backlash and it compounds. Sometimes this backlash would cause the arm to oscillate because it can't reach the target position exactly without overcompensating in the opposite direction. Communication This is where I learned about binary protocols (you might remember my article from last week). Anyway, there are more fun features to be implemented (like an actual gripper) and improvements to be made. For all of you who built your own robot arm, what do you use it for and what challenges did you run into?

12h ago

---

**[Why robots can’t learn by watching you yet](https://www.reddit.com/r/robotics/comments/1sx2j8z/why_robots_cant_learn_by_watching_you_yet/)**

Professor Ranjay Krishna explains a gap between modern AI and robotics. Language models can take examples, adapt to new inputs, and improve output in real time. That behavior does not translate to physical systems. In robotics, if a task changes even slightly, the system often fails. A different object, a new position, or a small variation in the environment can break what it learned. The idea of showing a robot how to do something once and having it learn by watching is still out of reach. Research areas like imitation learning and continual learning have not solved this in real-world settings.

1h ago

---

**[Soft robotic fish powered by SMA springs](https://www.reddit.com/r/robotics/comments/1sx22lf/soft_robotic_fish_powered_by_sma_springs/)**

I’ve been experimenting with biomimetic propulsion using a soft robotic fish actuated by SMA springs. I built a MATLAB model to simulate the tail motion and developed a controller that computes how each SMA should heat/contract to follow a desired trajectory. The goal is to understand stability and motion before building the real prototype. The physical prototype is now assembled and ready for testing. Still a work in progress, but it’s been a fun mix of soft robotics, kinematics, and control ⚙️🐬.

2h ago

---

**[Ascento Guard: A Two-Wheeled Jumping Security Robot Developed at ETH Zurich](https://www.reddit.com/r/robotics/comments/1swcjc1/ascento_guard_a_twowheeled_jumping_security_robot/)**

21h ago

---

**[Spatial Topology as MCP server for your robot llm?](https://www.reddit.com/r/robotics/comments/1swxbsx/spatial_topology_as_mcp_server_for_your_robot_llm/)**

(I am not form robotics backgroudn but mainly on the computer vision side) Curious how people are representing indoor spaces in a way that’s usable for higher-level reasoning. Not talking about navigation, but a secondary system that IDs the same space corectly and maitnains any memories or just help robot with understanding spatial arangeemnt of floors (floorplans). answering questions like: what are the human-defined spaces here? (rooms, zones, etc.) what spaces are adjacent / connected? how do you tie llm memory or events to a location in a building? how do you encode things like access rules or preferred paths (e.g. time-based flows)? Why I am asking: I am building a MCP server over floorplan geoemtry + topology (can opensource it), and want to see how useful udnerstading a floorplan as defined by humans IS for robots

6h ago

---

**[Working at my second robotics startup, I feel they're both failing for the same reason: the scope of the endeavor](https://www.reddit.com/r/robotics/comments/1swd5ts/working_at_my_second_robotics_startup_i_feel/)**

Robotics as a discipline is already hard enough, but what nobody ever talks about is that all these components need to be certified, not just separately but also as a whole. You need seasoned experts in each subdomain (software, electric, mechanic) that can produce components to the level that will pass OSHA, Regulation 2023/1230 etc etc. This usually requires outside labs for independent validation of safety standards, which can take years especially if humans have to get anywhere close to the device. Both companies I work for have been utterly unaware of this, and are now finding out that "4 months to market" are actually rather "1.5 years to market".

21h ago

---

**[‘Robots don’t bleed’: Ukraine sends machines into the battlefield in place of human soldiers](https://www.reddit.com/r/robotics/comments/1swukna/robots_dont_bleed_ukraine_sends_machines_into_the/)**

Ukraine’s military is increasingly using robots to replace human soldiers, even in combat assault missions, helping to counter Russia’s manpower advantage.

🔗 [CNN](https://edition.cnn.com/2026/04/20/europe/robots-ukraine-battlefield-drones-intl-cmd) • 9h ago

---

**[Messing around with the holonomic (kiwi) drive](https://www.reddit.com/r/robotics/comments/1sw3y5d/messing_around_with_the_holonomic_kiwi_drive/)**

1d ago

---

---

## Google News: "robotics"

**[New e-skin gives robotic hand sense of touch in breakthrough test](https://interestingengineering.com/ai-robotics/flexible-electronics-electronic-skin-soft-robots-turku-study)**

Researchers develop flexible, stretchable electronic skin and soft robots inspired by nature at University of Turku.

Interesting Engineering • 2d ago

---

**[Why do we make robots look like ourselves?](https://www.nationalgeographic.com/science/article/robot-humanoids-mechanical-engineering)**

Inside the enduring appeal of machines that look, move, and increasingly think like humans.

National Geographic • 3h ago

---

**[AI Startup Sereact Raises $110 Million for Robots That Predict Consequences](https://www.bloomberg.com/news/articles/2026-04-27/ai-startup-sereact-raises-110-million-for-robots-that-predict-consequences)**

Bloomberg.com • 10h ago

---

**[AI robots are learning to do simple human tasks at a factory in Massachusetts](https://www.cbsnews.com/boston/news/ai-robots-tutor-intelligence-watertown/)**

Tutor Intelligence in Watertown is a kind of kindergarten for robots.

CBS News • 2d ago

---

**[Sereact Raises $110 Million to Scale AI Robotic Brain](https://www.pymnts.com/news/investment-tracker/2026/sereact-raises-110-million-to-scale-ai-robotic-brain/)**

German startup Sereact has raised $110 million to develop its AI robotics model. The company announced the Series B funding round Sunday (April 26),

PYMNTS.com • 1h ago

---

**[From robots to EVs to AI, a week of breakthroughs highlights China's tech advances, self-reliance](https://www.globaltimes.cn/page/202604/1359843.shtml)**

From a humanoid robot half-marathon in Beijing to the global spotlight of the Beijing Auto Show and the debut of DeepSeek-V4, Chinese technological milestones have dominated international headlines over the past week.

Global Times • 22h ago

---

**['Self-aware' robots can learn complex tasks by watching humans. Is that a good thing?](https://www.npr.org/2026/04/24/nx-s1-5797863/self-aware-robots-future-laundry-work-home)**

Scientists say they've made a key breakthrough that would allow robots to figure out complex tasks on their own — but experts say it raises questions about how much risk comes with letting robots be in charge of their own learning.

NPR • 3d ago

---

**[Tesla: AI And Robotics Shift Is The Real Story (NASDAQ:TSLA)](https://seekingalpha.com/article/4894521-tesla-stock-ai-and-robotics-shift-is-the-real-story)**

Tesla’s Q1’26 TSLA results show rising gross margins and 117% YoY free cash flow growth as it pivots to AI/robotics. Learn more about TSLA stock here.

Seeking Alpha • 4h ago

---

**[How I taught myself to code, quit my consulting job, and started an AI robotics firm by age 25](https://www.businessinsider.com/consultant-turned-ai-robotics-founder-career-lessons-bcg-remy-2026-4)**

Oscar Brisset, 25, used most of his vacation days to learn to code. He left BCG to launch a YC-backed AI robotics company.

Business Insider • 2d ago

---

**[Faraday Future opens its robot-building platform to kids and engineers](https://www.stocktitan.net/news/FFAI/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-investor-2dnrnqpq8gzu.html)**

BIBS signed an MOU to form an AI and Robotics Institute aimed at training AI talent. FF said April robot sales and shipment data will follow next week.

Stock Titan • 15h ago

---

---

## YouTube Videos: "robotics"

**[I Bought 200 Robot Vacuums — Here&#39;s The Only One Worth Your Money in 2026!](https://www.youtube.com/watch?v=i_vPlTcRxp8)**

What is the best robot vacuum in 2026? After testing over 200 robot vacuums with my own money, one model still stands above ...

📺 Just A Dad Approved

👁️ 9K • 👍 313 • 💬 104 • ⏱️ 13:40 • 2d ago

---

**[Robot Smashes Human World Record, Signaling Big Changes](https://www.youtube.com/watch?v=zw9LAjm9pso)**

Flash, a humanoid robot made by Chinese smartphone company Honor, just smashed the human world record for the ...

📺 CNET

👁️ 8K • 👍 229 • 💬 33 • ⏱️ 4:53 • 1d ago

---

**[Which Robot Lawn Mower Should You Buy in 2026?](https://www.youtube.com/watch?v=tA9Wm9882c0)**

eufy Robot Lawn Mower - https://geni.us/eufy-e15 eufy website - https://stus.re/eufy-robot-lawnmower Today I take a look back at ...

📺 Stu’s Reviews

👁️ 4K • 👍 81 • 💬 19 • ⏱️ 16:11 • 19h ago

---

**[Ultimate Red &amp; Green Robot Toy Box - Giant GUNDAM Smash: Tobot Carbot Constructicons &amp; OPTIMUS PRIME](https://www.youtube.com/watch?v=zDu4JPjnVkE)**

Ultimate Red & Green Robot Toy Box - Giant GUNDAM Smash: Tobot Carbot Constructicons & OPTIMUS PRIME: ...

📺 Bob ToysReview

👁️ 3K • 👍 12 • ⏱️ 11:42 • 7h ago

---

**[UNEXPECTED LINK: Trump family TIED to humanoid robot CLASH with China](https://www.youtube.com/watch?v=SWoVms-enPU)**

Foundation Future Industries founder and CEO Sankaet Pathak and Trump Organization Executive Vice President Eric Trump ...

📺 Fox Business

👁️ 65K • 👍 1K • 💬 459 • ⏱️ 10:17 • 4d ago

---

**[Compact Odometry Mounting by 1010g TenTon Robotics](https://www.youtube.com/watch?v=6JwRMEXqyvw)**

Pits & Parts full explanation: https://youtu.be/iKgoQ59ZiSI @1010G_TenTonRobotics Check out our robotics game and FUN ...

📺 FUN Robotics Network

👁️ 8K • 👍 59 • 💬 1 • ⏱️ 0:15 • 18h ago

---

**[NEW Shoggoth Robot Is Bizarre... NEW Stretch Attack Ability Is Wild | War Robots](https://www.youtube.com/watch?v=cvzlozoeJ5o)**

New Spider Shoggoth Robot. This is so weird. We got a new robot on the test server and it has a brand new ability. 2 Medium 2 ...

📺 PREDATOR WR

👁️ 29K • 👍 764 • 💬 241 • ⏱️ 15:36 • 2d ago

---

**[This Genius Built a Robot Without a Lab 🤯](https://www.youtube.com/watch?v=TthyC8lTFWQ)**

Innovation doesn't need millions — just creativity and passion ⚙️ This incredible DIY project proves that anyone can build ...

📺 Phonix_Beats

👁️ 3.8M • 👍 70K • 💬 1K • ⏱️ 0:19 • 6d ago

---

**[Can Nick Stir Better Than Mark Rober&#39;s Robots? @NickDiGiovanni](https://www.youtube.com/watch?v=KJvpl1aQZnQ)**

📺 Chef Master Shorts

👁️ 61K • 👍 2K • 💬 7 • ⏱️ 1:00 • 19h ago

---

**[Khan Sir On Robot Doctor 🤖.](https://www.youtube.com/watch?v=YN4NopEsEKE)**

Khan sir ne kaha Robots ko log doctor ka kam karne nhi dange. Rajshamani podcast Rajshamani robot doctor Rajshamani and ...

📺 Grind and growth 

👁️ 38K • 💬 13 • ⏱️ 0:24 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

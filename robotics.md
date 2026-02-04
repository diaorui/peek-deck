---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-04T09:45:31.037468+00:00'
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

**Last Updated:** February 04, 2026 at 09:45 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[I built a drone with six radars that refuses to hit power lines](https://www.reddit.com/r/robotics/comments/1qvercu/i_built_a_drone_with_six_radars_that_refuses_to/)**

The drone has six mmWave radars to sense power lines from any direction, all connected to a Raspberry Pi. Based on these detections, the desired velocity (from a pilot or autonomous system) then gets modified to guide the drone around the power line. Everything runs in real time on the Pi with ROS2 middleware and PX4 flight stack. If you're interested, you can check out the paper: https://arxiv.org/abs/2602.03229, or the full video with voice-over: https://www.youtube.com/watch?v=rJW3eEC-5Ao

5h ago

---

**[OpenClaw + RealSense + QWEN + ROS = Physical AI](https://www.reddit.com/r/robotics/comments/1qv7byt/openclaw_realsense_qwen_ros_physical_ai/)**

Mind Blown! Have you heard about ClawdBot now called OpenClaw? It’s an open source personal AI assistant with over 150k stars on GitHub. I connected a RealSense camera to it and my robot started following me!

10h ago

---

**[Joints made with rolling contact surfaces](https://www.reddit.com/r/robotics/comments/1quvbyp/joints_made_with_rolling_contact_surfaces/)**

See this LINK. Cool article about a new design for robot joints that roll instead of pivoting like normal hinges. Seems like a very practical design that would be easy to make with 3D printing, and can be passive or motor-driven. The joints use specially shaped (non-circular) rolling surfaces that can be “programmed” to move in very specific ways. Compared to regular joints, these rolling joints can follow complex paths much more accurately The joints can also change how force is transmitted, giving more strength where it’s needed and more speed elsewhere. From this academic article:C.J. Decker, T.G. Chen, M.C. Yuen, & R.J. Wood, Noncircular rolling contact joints enable programmed behavior in robotic linkages, Proc. Natl. Acad. Sci. U.S.A. https://doi.org/10.1073/pnas.2521406123 (2026). The authors show that a joint designed this way can closely match the motion of a human knee, far better than standard hinges. They also build a robotic gripper that can lift over three times more weight than a similar gripper with ordinary joints.

18h ago

---

**[Rodney Brooks on why humans still do the grasping](https://www.reddit.com/r/robotics/comments/1qvab5h/rodney_brooks_on_why_humans_still_do_the_grasping/)**

Brooks argues that the real bottleneck is still physical interaction with the world. Humans don’t just copy motions when they pick something up. They constantly sense force, adjust grip, and adapt in ways that are hard to formalize or capture in data. Many current systems learn from vision or teleoperation, but that misses what happens at the point of contact. His view isn’t that automation can’t help. It’s that value today comes from supporting humans around these tasks rather than replacing them. Reducing walking, lifting, and strain is achievable now, while true human-level grasping remains a long-term challenge.

8h ago

---

**[Final jet engine scale model design](https://www.reddit.com/r/robotics/comments/1qvfmy1/final_jet_engine_scale_model_design/)**

4h ago

---

**[MirrorMe claims the world’s fastest humanoid at 10m/s (22.4 mph - 36 km/h)](https://www.reddit.com/r/robotics/comments/1quomj5/mirrorme_claims_the_worlds_fastest_humanoid_at/)**

From RoboHub🤖 on 𝕏: https://x.com/XRoboHub/status/2018281195063419225 Previous post with MirrorMe robot dog at 13.4 m/s: https://www.reddit.com/r/robotics/comments/1pvek2r/the_black_panther_ii_robot_dog_hits_134_ms/

23h ago

---

**[Slight robotics research rant](https://www.reddit.com/r/robotics/comments/1qvf946/slight_robotics_research_rant/)**

Not sure where else to rant and have people understand where I am coming from. But here it goes - I am a master's student in mechanical engineering, specializing in robotics. I entered with an existing research idea in mind, given that I have completed 2 years of undergraduate research in this lab. At first, I was able to work on my existing idea, especially since it was novel. But then came Trump's funding cuts, and my school/lab was essentially out of funds (and because my PI bought the Unitree G1 complete package lol). I lost my funding, and research now is pretty restricted. With that, I have been advised to start preliminary research in a completely different field. I did try to return to my prior research, but I received negative feedback. There was a strong sense coming from my PI that I should do research in human-robot interaction (HRI). I spoke to some peers in the lab, and from the sounds of it, I was pushed to do research in this area of robotics mainly so that I can work on a novel idea and get NSF funding (ideally) for the lab, depending on the proposal, since this area of robotics has been getting alot of traction lately due to safety concerns. Although I do have a pretty interesting/novel idea in this field (and I would be more than happy to chat with anyone about it), I sort of dread it. I've been delaying research on this topic because working on it isn't exciting, and the work itself steers me into an industrial field separate from my dreams. To top it off, I hate our weekly lab meetings (where we present our week's work and what we plan to do the following week). It's been about 4 months since I first explained my work (pertaining to Trust in HRI), and almost every meeting ends with my PI saying he doesn't understand the topic of trust. I figured I was the issue in explaining it, but all my peers understood it and found it extremely interesting. The first thing they asked, as well, was whether I transferred to a PhD program. Mainly due to the fact that master's research typically deals with the applications of PhD research, while PhDs focus on completely novel ideas. However, my work has involved complete reformulations / new formulations of statistical means that PhD students would focus on. I spent many sleepless nights reading many statistical textbooks and so on. I even spent nearly a month reading psychology papers to better understand human Trust on the human level (spoiler, psychologists appear to barely understand it as well). In the end, though, it does not matter how hard or how much I work on this topic because if my PI doesn't approve of it, then I cannot complete my thesis, which feels like a punch to the throat. Fortunately, I have a second-round interview with ASML and a backup secured internship with NASA, so that might help steer me back onto my ideal path or open new doors for research. But the next year of research sounds like it'll suck... Wishing I had a separate hot topic to research that the PI would at least somewhat understand and approve of. It's the least I can ask for after doing 6+ hours a day of unpaid research :') P.S. Sorry if this rant was scattered. Brain still in overdrive from school.

4h ago

---

**[NASA's Perseverance rover completes the first AI-planned drive on Mars](https://www.reddit.com/r/robotics/comments/1qvj2cv/nasas_perseverance_rover_completes_the_first/)**

History was made this week as NASA’s Perseverance rover completed its first-ever drive planned entirely by artificial intelligence. Instead of waiting for human drivers on Earth to chart every move, the rover used onboard AI to scan the terrain, identify hazards, and calculate its own safe path for over 450 meters (1,400 ft). This shift from remote control to true autonomy is the breakthrough needed to explore deep-space worlds where real-time communication is impossible.

🔗 [ScienceDaily](https://www.sciencedaily.com/releases/2026/01/260131084555.htm) • 1h ago

---

**[Need help!!](https://www.reddit.com/r/robotics/comments/1qv1ymt/need_help/)**

F450 overall Drone weight - 976gram Motor - A2212 - 1400kv Esc-30A Prop - 8inch Battery - 3S, 3500mah Will it lift? Or should i go for 1000kv bldc motor

14h ago

---

**[We trained a locomotion policy that got our humanoid robot Asimov to walk](https://www.reddit.com/r/robotics/comments/1qupdmn/we_trained_a_locomotion_policy_that_got_our/)**

Asimov is an open-source humanoid we're building from scratch at Menlo Research. Legs, arms, and head developed in parallel. We're sharing how we got the legs walking. The rewards barely mattered. What worked was controlling what data the policy sees, when, and why. Our robot oscillated violently on startup. We tuned rewards for weeks. Nothing changed. Then we realized the policy was behaving like an underdamped control system, and the fix had nothing to do with rewards. We don't feed ground-truth linear velocity to the policy. On real hardware, you have an IMU that drifts and encoders that measure joint positions. Nothing else. If you train with perfect velocity, the policy learns to rely on data that won't exist at deployment. Motors are polled over CAN bus sequentially. Hip data is 6-9ms stale by the time ankle data arrives. We modeled this explicitly, matching the actual timing the policy will face on hardware. The actor only sees what real sensors provide (45 dimensions). The critic sees privileged info: Ground truth velocity, contact forces, toe positions. Asimov has passive spring-loaded toes with no encoder. The robot can't sense them. By exposing toe state to the critic, the policy learns to infer toe behavior from ankle positions and IMU readings. We borrowed most of our reward structure from Booster, Unitree, and MJLab. Made hardware-specific tweaks. No gait clock (Asimov has unusual kinematics, canted hips, backward-bending knees), asymmetric pose tolerances (ankles have only ±20° ROM), narrower stance penalties, air time rewards (the legs are 16kg and can achieve flight phase). Domain randomization was targeted, not broad. We randomized encoder calibration error, PD gains, toe stiffness, foot friction, observation delays. We didn't randomize body mass, link lengths, or gravity. Randomize what you know varies. Don't randomize what you've measured accurately. Next: terrain curriculum, velocity curriculum, full body integration (26-DOF+). Full post with observation tables, reward weights, and code: https://news.asimov.inc/p/teaching-a-humanoid-to-walk

22h ago

---

---

## Google News: "robotics"

**[COMMENTARY: Teaching mathematics with coding and robotics can transform California math instruction](https://edsource.org/2026/california-math-framework-coding-robotics/750225)**

A hands-on, integrated approach has the potential to transform math from a gatekeeper into a gateway for STEM opportunities for all students.

EdSource • 2d ago

---

**[Carbon Robotics built an AI model that detects and identifies plants](https://techcrunch.com/2026/02/02/carbon-robotics-built-an-ai-model-that-detects-and-identifies-plants/)**

Carbon Robotics' Large Plant Model will allow farmers to kill new types of weeds without having to retrain the machines.

TechCrunch • 1d ago

---

**[SoftBank, Fanuc turn to partners as robotics and AI merge](https://asia.nikkei.com/business/technology/artificial-intelligence/softbank-fanuc-turn-to-partners-as-robotics-and-ai-merge)**

Japan's robotics industry struggles to catch up to physical AI technology

Nikkei Asia • 1d ago

---

**[Robotics is forcing a fundamental rethink of AI compute, data, and systems design](https://www.theregister.com/2026/02/03/robotics-ai-infrastructure-next/)**

Partner Content: Robotics is forcing a fundamental rethink of AI compute, data, and systems design

theregister.com • 17h ago

---

**[FIRST, Dean Kamen's youth robotics org, puts him on leave amid new Epstein revelations](https://www.nhpr.org/nh-news/2026-02-01/epstein-dean-kamen-first-nh-new-hampshire-epstein-files)**

FIRST's board of directors says it has hired a law firm to review Kamen's ties to Epstein, days after newly released documents show the two men shared a relationship over a number of years.

New Hampshire Public Radio • 2d ago

---

**[China unveils world’s first 'biomimetic AI robot' that smiles, winks](https://interestingengineering.com/ai-robotics/shanghai-unveils-moya-humanoid-robot)**

Moya, a humanoid robot unveiled in Shanghai, is designed to walk, smile, and interact like a human using embodied AI.

Interesting Engineering • 19h ago

---

**[FedEx Launches Berkshire Grey’s Fully Autonomous Robotic Trailer Unloader for a Safer and Smarter Workplace](https://newsroom.fedex.com/newsroom/global-english/fedex-launches-berkshire-greys-fully-autonomous-robotic-trailer-unloader-to-create-a-safer-and-more-efficient-workplace)**

The system will be deployed in calendar year 2026 following multi-year collaboration.

FedEx newsroom • 16h ago

---

**[Funding surge powers Chinese robotics firms as focus shifts to humanoid ‘brains’](https://www.scmp.com/tech/article/3342246/funding-surge-powers-chinese-robotics-firms-focus-shifts-humanoid-brains)**

State-backed funds, Big Tech drive fresh capital into robotics companies, betting on operating systems that underpin humanoid intelligence.

South China Morning Post • 21h ago

---

**[A programmable, Lego-like material for robots emulates life's flexibility](https://techxplore.com/news/2026-02-programmable-lego-material-robots-emulates.html)**

Tech Xplore • 12h ago

---

**[Is Delivery Volume Growth Showing Strong Adoption for Serve Robotics?](https://finance.yahoo.com/news/delivery-volume-growth-showing-strong-134100652.html)**

SERV sees rising delivery volumes as autonomous sidewalk robots gain wider acceptance with restaurants and consumers.

Yahoo Finance • 20h ago

---

---

## YouTube Videos: "robotics"

**[XPENG IRON Humanoid Robot Stuns Public With First Real World Appearance](https://www.youtube.com/watch?v=StiJLVlXY4o)**

XPENG just took a massive step forward in humanoid robotics. The New IRON robot has officially made its first public appearance, ...

📺 DPCcars

👁️ 17K • 👍 157 • 💬 35 • ⏱️ 1:21 • 3d ago

---

**[Moya, customizable humanoid robot, makes debut in Shanghai, powered by DroidUp&#39;s latest tech](https://www.youtube.com/watch?v=AuTbHjCepxs)**

Today in Shanghai, a humanoid robot named Moya makes her debut, smiling, nodding, making eye contact and walking naturally.

📺 ShanghaiEye魔都眼

👁️ 34K • 👍 639 • 💬 352 • ⏱️ 1:34 • 4d ago

---

**[30 million won humanoid robot for sale at Seoul’s supermarket](https://www.youtube.com/watch?v=qHpFZ3f2a_E)**

You can watch this video at https://koreanow.com Copyright(C) Unauthorized use, distribution, and employment of AI-based tools ...

📺 KOREA NOW

👁️ 4K • 👍 91 • 💬 22 • ⏱️ 1:54 • 1d ago

---

**[SSLC IT Chapter 6: The World of Robots | LED, Buzzer | Practical | Xylem SSLC](https://www.youtube.com/watch?v=csQEZkNlb2Q)**

sslc #xylemsslc #sslcpublicexam #sslcit Xylem New Year Offer Live Now !! Join Asthra Batch, Use Coupon Code "NY15", ...

📺 Xylem SSLC

👁️ 228K • 👍 8K • 💬 618 • ⏱️ 23:34 • 3d ago

---

**[XPeng IRON Robot Falls Then Stands Back Up Live on Stage](https://www.youtube.com/watch?v=kMfcGfRO0R8)**

XPeng just showed the world what real humanoid robot progress looks like. During a live public event, the IRON robot stumbled, ...

📺 DPCcars

👁️ 24K • 👍 109 • 💬 42 • ⏱️ 2:06 • 2d ago

---

**[China rolls out robot cops in cities to push humanoid robots in daily life](https://www.youtube.com/watch?v=NavsugcHgAo)**

China is deploying AI-powered robots to manage traffic and pedestrian flow in cities. NBC News' Janis Mackey Frayer explains ...

📺 NBC News

👁️ 785K • 👍 7K • 💬 3K • ⏱️ 3:13 • 5d ago

---

**[A Robotic Mouth That Speaks Like a Human 😳](https://www.youtube.com/watch?v=x6M2gCzUTJM)**

This robotic mouth is designed to replicate how real human lips move while speaking. Using actuators and soft materials, it copies ...

📺 Facts TV 91

👁️ 43K • 👍 329 • 💬 12 • ⏱️ 0:06 • 8h ago

---

**[Drag-and-drop welding robot.#industrial #welding #robot #spraying #stamping](https://www.youtube.com/watch?v=yOXhsjonNHk)**

📺 Lin of Brant robot 

👁️ 25K • 👍 76 • ⏱️ 0:19 • 4d ago

---

**[Tesla Optimus robot will allow for amazing abundance. #fyp #viral #tesla #optimus #teslarobot](https://www.youtube.com/watch?v=CPDqiFW1AhI)**

📺 Tesla Owners Silicon Valley

👁️ 2.3M • 👍 62K • 💬 1K • ⏱️ 0:40 • 2d ago

---

**[China’s New Shape Shifting AI Robot Walks on Water, Flies and Swims](https://www.youtube.com/watch?v=nLKj1gvJzWI)**

Humanoid robotics just took a massive leap into the real world. Researchers in China revealed GrowHR, a soft shape shifting ...

📺 AI Revolution

👁️ 137K • 👍 1K • 💬 280 • ⏱️ 14:25 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

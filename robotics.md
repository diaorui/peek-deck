---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-23T05:56:36.974543+00:00'
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

**Last Updated:** December 23, 2025 at 05:56 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Physical Intelligence (π) launches the "Robot Olympics": 5 autonomous events demonstrating the new π0.6 generalist model](https://www.reddit.com/r/robotics/comments/1pt6ouz/physical_intelligence_π_launches_the_robot/)**

Physical Intelligence just released a series of "Robot Olympics" events to showcase their latest π0.6 model. Unlike standard benchmarks, these tasks are designed to illustrate Moravec’s Paradox which are everyday physical actions that are trivial for humans but represent the "gold standard" of difficulty for modern robotics. All tasks shown are fully autonomous, demonstrating high-level task decomposition and fine motor control. The 5 Olympic Events: Event 1 (Gold) - Door Entry: The robot successfully navigates a self-closing lever-handle door. This is technically challenging because it requires the model to apply force to keep the door open while simultaneously moving its base through the frame. Event 2 (Silver) - Textile Manipulation: The model successfully turns a sock right-side-out. They attempted the Gold medal task (hanging an inside-out dress shirt), but the current hardware gripper was too wide for the sleeves. Event 3 (Gold) - Fine Tool Use: A major win here,the robot used a small key to unlock a padlock. This requires extreme precision to align the key and enough torque to turn the tumbler. (Silver was making a peanut butter sandwich, involving long-horizon steps like spreading and cutting triangles). Event 4 (Silver) - Deformable Objects: The robot successfully opened a dog poop bag. This is notoriously difficult because the thin plastic blinds the wrist cameras during manipulation. They attempted to peel an orange for Gold but were "disqualified" for needing a sharper tool. Event 5 (Gold) - Complex Cleaning: The robot washed a frying pan in a sink using soap and water, scrubbing both sides. They also cleared the Silver (cleaning the grippers) and Bronze (wiping the counter) tasks for this category. The Tech Behind It: The π0.6 model is a Vision-Language-Action (VLA) generalist policy. It moves away from simple "behavior cloning" and instead focuses on agentic coding and task completion, allowing it to recover from errors and handle diverse, "messy" real-world environments. Official Blog: pi.website/blog/olympics Source Video: Physical Intelligence on X

11h ago

---

**[Sunday Robotics Memo: "Pick Up Anything" test](https://www.reddit.com/r/robotics/comments/1ptkti2/sunday_robotics_memo_pick_up_anything_test/)**

From Sunday on 𝕏: https://x.com/sundayrobotics/status/2003294087236190623 Website: https://www.sunday.ai/

1h ago

---

**[GITAI's rovers and robotic arms deploy solar panels and weld in a construction field test](https://www.reddit.com/r/robotics/comments/1pswpjv/gitais_rovers_and_robotic_arms_deploy_solar/)**

Website: https://gitai.tech/ On 𝕏: https://x.com/GITAI_HQ Previous post: https://www.reddit.com/r/robotics/comments/1pd2kbm/gitai_is_designing_robots_that_can_maintain/ https://www.reddit.com/r/robotics/comments/1pgfvku/gitai_robots_cooperatively_assemble_a_5meter/

19h ago

---

**[Why don’t we have a small home robot that just… exists?](https://www.reddit.com/r/robotics/comments/1pswx2g/why_dont_we_have_a_small_home_robot_that_just/)**

I keep coming back to this thought, especially when I look at how much home robotics has progressed over the last few years. We’ve had social robots like Jibo and Anki Vector. We’ve seen Amazon Astro. None of them really stuck. And it doesn’t feel like they failed because the tech was bad. More like… they never found a natural place in daily life. What still feels missing to me is a very specific kind of robot. Not a humanoid. Not another appliance on wheels. I’m thinking about something small, maybe pet-sized, that just lives in the house with you. It moves between rooms. Goes upstairs and downstairs. Checks on the cat napping in the sun. Notices when the toddler is too quiet, or suddenly way too loud. Maybe it picks up small stuff, fetches things, or just keeps an eye on what’s going on. Not built around one killer feature. More around presence. The weird part is that most of the building blocks feel… good enough now. Indoor navigation mostly works. Cameras are cheap. Perception models are way better than they used to be. Small mobile robots aren’t exactly new tech. And yet, this category basically doesn’t exist. Which makes me think the blocker isn’t really technical anymore. It’s more about how people are supposed to relate to a thing like this. A few reasons that might explain it: Nobody can quite agree on what a “non-task” home robot is actually for A moving thing in your house feels stranger than a fixed device, even if it does less It’s hard to sell something that doesn’t replace a clear chore Homes are messy, emotional, and inconsistent in very human ways If it’s too capable, people get uneasy; if it’s too dumb, it feels pointless So we’re kind of stuck without a mental model for a robot that’s somewhere between an appliance, a pet, and a background presence. Maybe personal robots don’t fail because they’re not useful enough, but because we keep trying to frame them as tools. Maybe they need to be framed more like ambient companions that adapt to the rhythms of people, kids, and pets, instead of optimizing a single task. Feels like the tech is close. We just don’t know what role this thing is supposed to play yet.

18h ago

---

**[Question for robotics devs](https://www.reddit.com/r/robotics/comments/1ptcqp9/question_for_robotics_devs/)**

Hey guys, how much time do you usually spend on your feet in a given work day? I’ve recently injured my back and it doesn’t look like it’s going to get healed anytime soon. I’m relegated to a chair for the most part I think, but this is an industry I’m pretty interested in. I would love to get your feedback so I can decide if I can actually do this work in a professional setting. Thanks! 🤖

7h ago

---

**[[OS] SPIDER: A General Physics-Informed Retargeting Framework for Humanoids & Dexterous Hands](https://www.reddit.com/r/robotics/comments/1pt4uxn/os_spider_a_general_physicsinformed_retargeting/)**

Hi everyone, we’re open-sourcing SPIDER, a general framework for retargeting human motion to diverse robot embodiments. Most retargeting methods suffer from physical inconsistencies. SPIDER is physics-informed, ensuring dynamically feasible motions without artifacts like ghosting or floating. Key Features: General: Supports both humanoids (G1, H1, etc.) and dexterous hands (Allegro, Shadow, etc.). Physics-Based: GPU-accelerated optimization for clean, stable motion. Sim2Real-ready: Ready for deployment, from human video to real-world robot actions. Links: 📦 Code: https://github.com/facebookresearch/spider 📓 Tutorial: Notebook 🌐 Project Page: http://jc-bao.github.io/spider-project/ Would love to hear your feedback or help with any integration questions!

12h ago

---

**[M5Stack’s Open-Source Kawaii Robot — Pre-Orders Are Now Open!](https://www.reddit.com/r/robotics/comments/1pthpfw/m5stacks_opensource_kawaii_robot_preorders_are/)**

3h ago

---

**[Any miniature BLDC (PMSM) or DC motors for direct drive in robots?](https://www.reddit.com/r/robotics/comments/1ptesf6/any_miniature_bldc_pmsm_or_dc_motors_for_direct/)**

I am building a robotic hand, which is very compact and direct-driven. So, I am trying to find some motors (w/o gearbox) having a very small size, but high torque (and low speed). The torque and speed requirement is similar to the gimbal motor (0.07 N-m) in the below link. https://store.tmotor.com/product/gb2208-gimbal-type.html But the size is an issue for my project. I want to use a motor with a 16 mm smaller diameter, which shape is similar to the ones in the following link. https://www.portescap.com/en/products/brushless-dc-motors/all-bldc-motors The sizes of those motors are good for me, but they are designed for the high speed applications (higher than 10,000 rpm). To accomplish this requirement, I think that the motors should have high resistance compared to high-speed motors used for the drone. Please share your opinion and any comment for my project!!

6h ago

---

**[3d printed automatic tool-changer update](https://www.reddit.com/r/robotics/comments/1pt4jb8/3d_printed_automatic_toolchanger_update/)**

Making some good progress on the automatic tool-changing mechanism for my SCARA arm. I got it wired and assembled to the Z-compensation module and made it grip and release when pushing against the tool. I made a tool pocket that fits on a 2020 extrusion so I can stack a few of them in a row once I make more tools and added a little magnet to have it sit in a fixed position. The tools are connected by a magnetic pogo pin connector to power and control them and I want one of the pins to serve as a connection verification signal, and later, tool identification. I am still considering what is the best and simplest method to do it. I am considering wiring different resistors or capacitors in each tool and measuring the voltage/charge time when connected. If anyone has tried these methods before or has a better one I would really appreciate your advice. For more details on this project check out my hackaday page: https://hackaday.io/project/204557-pr3-scara

13h ago

---

**[Tilt gimbal](https://www.reddit.com/r/robotics/comments/1pso6qv/tilt_gimbal/)**

This setup uses two single-axis (pitch-only) gimbals stacked in series. When combined, could this configuration serve as an alternative to a robotic arm in certain applications? I’d welcome discussion and insights from the community.

1d ago

---

---

## Google News: "robotics"

**[Unitree G1 humanoids go viral with synchronised frontflip and Musk endorsement](https://www.scmp.com/tech/tech-trends/article/3337320/unitree-g1-humanoids-go-viral-synchronised-backflip-and-impressive-musk-endorsement)**

China continues to dominate in humanoid robotics, and its lead over the US is accelerating, according to a recent Morgan Stanley report.

South China Morning Post • 21h ago

---

**[Humanoid robots head to chip factories in global deal with Oversonic](https://www.stocktitan.net/news/STM/oversonic-robotics-signs-humanoid-robots-supply-agreement-with-st-yc3ygdinwizf.html)**

In 2025, STMicroelectronics will deploy Oversonic RoBee humanoids across plants, starting at its Malta fab, and show collaboration with live demos at CES.

Stock Titan • 21h ago

---

**[Humanoid robots are coming. Eventually?](https://www.theverge.com/column/843418/humanoid-robot-hype)**

China sees humanoids as an economic engine and Musk wants a ‘robot army.’

The Verge • 1d ago

---

**[Hyundai Motor Group to Unveil AI Robotics Strategy at CES 2026](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001093)**

Hyundai Motor Group released a teaser image previewing its upcoming participation at CES 2026

hyundai.com • 23h ago

---

**[Solo GP Kevin Costa closes $20m fund to invest in AI, robotics and infrastructure](https://sifted.eu/articles/belief-capital-kevin-costa-solo-gp)**

Solo GP Kevin Costa has raised his $20m fund from LPs including general partners at VC firms Point Nine, Hummingbird and Adjacent

Sifted • 1d ago

---

**[Wilton Dominates State Championship in Robotics, Again Ascends to World Competition](https://goodmorningwilton.com/wilton-robotics-teams-win-state-championship-dec-2025/)**

Wilton teams shine at the FIRST Lego League Robotics State Championships. Allied Algorithms won the championship and Singularity Technology Juniors earning the Motivate Award.

Good Morning Wilton • 1d ago

---

**[NVIDIA's Quest For A "Safe" Linux Kernel For Automobiles, Robotics](https://www.phoronix.com/news/NVIDIA-ASIL-B-Linux-Kernel)**

NVIDIA engineer Igor Stoppa presented at the Linux Plumbers Conference (LPC) earlier this month around using Linux in safety-critical environments like automobiles and the current shortcomings of the upstream Linux kernel and the challenges on achieving Automotive Safety Integrity Level (ASIL) certifications around the Linux kernel

Phoronix • 18h ago

---

**[MSU Mankato hosts 75-team Vex Robotics competition](https://www.keyc.com/2025/12/19/msu-mankato-hosts-75-team-vex-robotics-competition/)**

Local robotics teams gathered in Mankato Friday to show off their knowledge and skills.

KEYC News Now • 3d ago

---

**[Ghost Team Up with FeedLA & Serve Robotics to Give Out Food in Los Angeles](https://www.metalsucks.net/2025/12/20/ghost-team-up-with-feedla-serve-robotics-to-give-out-food-in-los-angeles/)**

Ghost, FeedLA and Serve Robotics joined forces December 19 to deliver food to residents of the Inglewood neighborhood in Los Angeles.

MetalSucks • 2d ago

---

**[Elon Musk Calls Tesla Optimus Rival's Dancing Robots 'Impressive' As Unitree Machines Perform Flips, Acrobatic Stunts](https://finance.yahoo.com/news/elon-musk-calls-tesla-optimus-143050216.html)**

Elon Musk expressed admiration for the performance of Tesla Inc.’s (NASDAQ:TSLA) humanoid robot Optimus’s rival and Chinese Unitree robots executing flips and intricate dance routines at a high-profile concert. Unitree Robots Wow Audiences with Acrobatics At a recent concert in Chengdu, Chinese-American singer Wang Leehom took the stage alongside advanced Unitree robots, which performed complex acrobatics including Webster flips and synchronized dance moves. Tech commentator Rohan Paul shared a

Yahoo Finance • 15h ago

---

---

## YouTube Videos: "robotics"

**[AI ROBOTS Are Now TOO REAL! - Shocking AI &amp; Robotics 2025 Updates](https://www.youtube.com/watch?v=a4Y_VVuqYyk)**

The world of AI and robotics accelerated faster this year than almost anyone expected. Humanoid robots became cheaper, faster, ...

📺 AI Revolution

👁️ 38K • 👍 739 • 💬 77 • ⏱️ 2:08:46 • 3d ago

---

**[The Self Aware Robot ESCAPED!!](https://www.youtube.com/watch?v=RkeHtsO4-OY)**

My Self-Aware Robot Escaped Reaction Check out the video here: https://www.youtube.com/watch?v=6nEfAb5q84o 🔸️Join ...

📺 Its Nenaa

👁️ 6K • 👍 380 • 💬 105 • ⏱️ 11:02 • 6h ago

---

**[This Rolling Robot Could Replace Police in the Future](https://www.youtube.com/watch?v=wKWUTIHGQZk)**

FutureTech #Robotics #LawEnforcement.

📺 Skye Ocean Girl

👁️ 30K • 👍 146 • 💬 6 • ⏱️ 0:19 • 1d ago

---

**[How STRONG Are Humanoid Robots Really? (And Why It&#39;s Hard to Tell)](https://www.youtube.com/watch?v=PGRJg5eExO4)**

China's got a new Terminator robot and Figure is facing a lawsuit alleging its robots are strong enough to "fracture a human skull.

📺 CNET

👁️ 28K • 👍 543 • 💬 126 • ⏱️ 5:25 • 1d ago

---

**[TRON 2 Officially Launched | Redefining the Foundation of Embodied Robotics](https://www.youtube.com/watch?v=Ut3QFPr7hyo)**

Cutting-edge Algorithms, At Your Fingertips. Explore More: https://www.limxdynamics.com/en/tron2 #limxdynamics #limxtron2 ...

📺 LimX Dynamics

👁️ 939K • 👍 11K • 💬 618 • ⏱️ 2:43 • 4d ago

---

**[I Made a Self Aware Robot - EXPLAINED](https://www.youtube.com/watch?v=EQEkwqvkyFI)**

LIGHTSAREOFF AZFK MERCH! https://azfk-shop.fourthwall.com/ Donate to the Cult for exclusive behind the Scenes Access ...

📺 AZFK

👁️ 140K • 👍 7K • 💬 542 • ⏱️ 13:43 • 4d ago

---

**[THIS SELF AWARE ROBOT ESCAPED AND WANTS TO END HUMANITY](https://www.youtube.com/watch?v=TeE8Bz8JOLI)**

Channels: https://www.youtube.com/@vibingleaf youtube.com/watch?v=b-vx4v_iVPw&pp=0gcJCTwKAYcqIYzv @j-gems ...

📺 Baz

👁️ 23K • 👍 1K • 💬 94 • ⏱️ 26:19 • 1d ago

---

**[His Self-Aware Robot Escaped ...](https://www.youtube.com/watch?v=e7fkeontbaE)**

I got a little bit bored so His Self-Aware Robot Escaped SUBSCRIBE TO OG @LIGHTSAREOFF New Merch https://socks.store/ ...

📺 SocksReact

👁️ 517K • 👍 10K • 💬 1K • ⏱️ 18:35 • 2d ago

---

**[INSANE AI Curling Robot in Dubai😱💇🏼‍♀️Automatic Perm Tach From the Future!](https://www.youtube.com/watch?v=aaHeKdH4ILc)**

ai #beauty #hair #curling #coloring #robot #tachnology #viral #dubai #future #hairstyle #salon #trnding #shorts #transformation ...

📺 Ai BOOF

👁️ 11K • 👍 168 • 💬 6 • ⏱️ 0:11 • 21h ago

---

**[AI Robot Started Gaining Consciousness 🤯](https://www.youtube.com/watch?v=-__3Svb8oHg)**

jumpersjump #hardclipped.

📺 Sharp Cut

👁️ 2.5M • 👍 35K • 💬 573 • ⏱️ 0:29 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

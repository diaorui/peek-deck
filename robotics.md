---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-07-31T04:59:39.413728+00:00'
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

**Last Updated:** July 31, 2026 at 04:59 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[If it were at an amusement park, would you want to ride it?](https://www.reddit.com/r/robotics/comments/1varxei/if_it_were_at_an_amusement_park_would_you_want_to/)**

California-based robotics startup Satyress is developing Threehalves, a 7-foot-tall teleoperated centaur robot designed for hazardous work.But if it’s designed for hazardous tasks, why does it look like something you could ride—something that seems more at home in an amusement park? Although its appearance is a bit creepy lol.

16h ago

---

**[What a cheap GPS actually reports vs what you can get out of it](https://www.reddit.com/r/robotics/comments/1vb5nx7/what_a_cheap_gps_actually_reports_vs_what_you_can/)**

Setup: a Raspberry Pi 4B on a small skid-steer chassis, a u-blox NEO-M9N (about $100), a BNO085 IMU, and hall encoders on the wheels. No RTK, no base station, no corrections Orange is pretty much every fix the receiver reported. Blue is the output seen after fusing those fixes with the IMU and wheel odometry in a UKF. Every fix was used, none were rejected in this entire run. What I can and cannot say about this is that, since this is a fair thing to ask: I don't have RTK ground truth for this run, so I can't claim the blue line is closer to the true path than the orange dots are. What I can say is that the filter's reported 1-sigma stayed around 2.5 m throughout, including while moving, and the fused output tracked the raw fixes to a median of 1.69 m. Both of those are self-reported numbers, not error against an independent reference. Other limitations worth stating: it's a single short run covering only about 20 m, there's no comparison against robot_localization on the same data yet, and heading comes from GPS track rather than a magnetometer, so it isn't meaningful for roughly the first minute of driving. The curve in the path is mechanical, the chassis pulls right about 3 deg/s. On the next run I'm closing the loop back to a physically marked start point so there's at least a real closure number, and replaying the same bag through robot_localization so it's a controlled comparison on identical input rather than one filter on its own. Also looking into borrowing an F9P for proper ground truth. Disclosure: I wrote the filter (FusionCore): https://github.com/manankharwar/fusioncore Happy to share the rosbag if anyone wants to run their own filter against it. Edit: rewrote this. Sorry if my english is bad...

8h ago

---

**[Google DeepMind announces Gemini Robotics 2](https://www.reddit.com/r/robotics/comments/1vaxn3p/google_deepmind_announces_gemini_robotics_2/)**

Google DeepMind has announced Gemini Robotics 2, its latest robotics foundation models, in early access. The release adds full-body control for humanoid robots, multi-step task execution with the ability to recover from mistakes, natural language communication, multi-robot coordination, on-device deployment, and new safety features that can reject unsafe commands or request human assistance when needed. Google demonstrated the models on Apptronik’s Apollo 2 humanoid, along with dexterous robotic hands and dual-arm systems. The update moves beyond robots performing isolated tasks and toward systems that can complete longer sequences of work while interacting more naturally with people and other robots.

🔗 [Automate](https://www.automate.org/ai/industry-insights/google-deepmind-announces-gemini-robotics-2-new-safety-measures-for-humanoids) • 13h ago

---

**[[R] Decentralized self-repair for modular robotic structures](https://www.reddit.com/r/robotics/comments/1vay0av/r_decentralized_selfrepair_for_modular_robotic/)**

Damage can fragment a modular robotic structure into disconnected pieces. We developed decentralized strategies that allow the surviving modules to consolidate, reorganize, and autonomously restore connectivity without a central controller. Across 1,000 simulated damage scenarios, the system retained at least 80% of surviving modules in its largest connected component even after 30% random failures, with near-perfect reconnection in fully connected cases. The broader goal is to develop machine analogues of homeostasis and morphogenesis: systems that can detect damage, adapt their physical organization, and preserve function. Technical article: https://www.manifoldrg.com/can-a-spacecraft-heal-itself/ Preprint: https://arxiv.org/abs/2607.13444 I’m one of the authors and would welcome feedback, particularly on the decentralized coordination strategy and the path toward hardware experiments.

12h ago

---

**[Testing a Bowden cable drive for a future project](https://www.reddit.com/r/robotics/comments/1vb635j/testing_a_bowden_cable_drive_for_a_future_project/)**

I'm exploring Bowden cables as a way to transmit motion when the motor can't be placed near the moving part. This is just a quick setup to see how smoothly it works before designing a larger mechanism. Any suggestions or ideas are welcome.

8h ago

---

**[A robot import ban may also be a ban on cheap iteration](https://www.reddit.com/r/robotics/comments/1vakosr/a_robot_import_ban_may_also_be_a_ban_on_cheap/)**

The new US restriction on foreign-made humanoids and quadrupeds is framed around security, but price and availability matter to research velocity. AP reports that Chinese manufacturers ship far more humanoids than US rivals and often at much lower prices. Labs learn by breaking hardware, replacing parts, and running many imperfect prototypes. If the affordable platforms disappear, better-funded companies may adapt while universities, startups, and independent builders reduce experiments or move them abroad. Would a certified research-only pathway preserve security without concentrating access? Or are connected embodied systems too difficult to contain once they enter a lab network? Source: https://apnews.com/article/china-us-humanoid-robots-ban-tech-c9f5e3c94d91d00eff3b61b141fab366

23h ago

---

**[how to build accelerator kit for robotics using Isaac sim and isaac lab](https://www.reddit.com/r/robotics/comments/1vb3ukp/how_to_build_accelerator_kit_for_robotics_using/)**

9h ago

---

**[That’s how we train the robot to follow you by reinforcement learning.](https://www.reddit.com/r/robotics/comments/1vb03v3/thats_how_we_train_the_robot_to_follow_you_by/)**

11h ago

---

**[Could there be an open-source layout robot for surveyors?](https://www.reddit.com/r/robotics/comments/1vb5lv8/could_there_be_an_opensource_layout_robot_for/)**

8h ago

---

**[I Got a Free Meal From a Private Chef—Who Filmed It All to Train Robots](https://www.reddit.com/r/robotics/comments/1vauzre/i_got_a_free_meal_from_a_private_chefwho_filmed/)**

A German startup sent a camera-wearing chef to my apartment. In exchange for a free lunch, I let them record every chop and stir to train future humanoids.

🔗 [WIRED](https://www.wired.com/story/i-let-a-private-chef-film-my-kitchen-for-robot-training-data/) • 14h ago

---

---

## Google News: "robotics"

**[Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)**

From feet to fingertips — we are teaching robots intelligent whole-body control, fine dexterity, and teamwork to complete a broad range of complex tasks.

Google DeepMind • 13h ago

---

**[Trump administration bans new Chinese humanoid robots, to protect US AI buildout](https://www.reuters.com/world/trump-administration-ban-new-chinese-robots-inverters-protecting-us-ai-buildout-2026-07-28/)**

Reuters • 2d ago

---

**[Robot waiters and drone deliveries: Inside China’s futuristic hardware capital](https://www.nbcnews.com/tech/tech-news/shenzhen-drones-robots-chinas-hardware-ai-capital-rcna589413)**

Long a symbol of China’s economic surge, Shenzhen is embracing a high-tech, low-altitude future.

NBC News • 11h ago

---

**[Developing Healthcare Robotics with GPU-Native Medical Physics Simulation](https://developer.nvidia.com/blog/developing-healthcare-robotics-with-gpu-native-medical-physics-simulation/)**

Unlike autonomous driving or industrial robotics, healthcare robotics can’t rely on internet-scale data collection or unlimited real-world experimentation. Every demonstration requires specialized…

NVIDIA Developer • 2d ago

---

**[Making robots faster by helping them think ahead](https://news.mit.edu/2026/making-robots-faster-helping-them-think-ahead-0728)**

The VLASH technique, developed by MIT researchers, helps robots think ahead while moving, eliminating lags that occur between different chunks of action. This smooths and streamlines robot motion, accelerating performance on tasks like pick-and-place, sorting, and stacking.

MIT News • 3d ago

---

**[Robotics startup Generalist AI is in talks to raise a new funding round at a $3 billion valuation](https://www.businessinsider.com/startup-generalist-ai-in-talks-to-raise-at-billion-valuation-2026-7)**

Venture firm 8VC is expected to lead the round as investors pour money into physical AI.

Business Insider • 1d ago

---

**[Here's why a robotics firm founder hired Brockton students on the spot](https://www.enterprisenews.com/story/news/education/2026/07/30/brockton-high-school-drone-team-boston-robotics-company/91036144007/)**

Here's how a group of kids from Brockton ended up interning at a Boston robotics firm and what BHS's talented drone pilot plans to do next.

Enterprise News • 19h ago

---

**[You can hire these humanoid robots from Tau Robotics to clean your home in San Francisco](https://abc7news.com/post/can-hire-humanoid-robots-tau-robotics-clean-home-san-francisco/19599847/)**

A robotics startup has begun offering humanoid home cleaning services for $30 an hour to selected applicants in San Francisco, where a person operates the robot from a central location with assistance from AI. Would you hire them?

ABC7 Bay Area • 10h ago

---

**[Experts react to FCC limits on U.S. imports of new humanoid and mobile robots](https://www.therobotreport.com/industry-reacts-fcc-ban-u-s-imports-new-humanoid-quadruped-robots/)**

The FCC has banned some foreign humanoids, which industry experts say could help U.S. industry but hinder innovation.

The Robot Report • 1d ago

---

**[Walberg warns about robotics work tied to Dowagiac data center](https://www.moodyonthemarket.com/walberg-warns-about-robotics-work-tied-to-dowagiac-data-center/)**

Congressman Tim Walberg is seeking federal action to head off what he believes could be the national security implications of developments planned at an already-controversial data center in Dowagiac. Walberg this week sent a letter to U.S.

Moody on the Market • 1d ago

---

---

## YouTube Videos: "robotics"

**[Gemini Robotics 2 brings whole body intelligence to robots](https://www.youtube.com/watch?v=4lSQnrMC6nY)**

For decades, we've dreamed of robots that can seamlessly step into our world and lend a hand. Now, that vision takes a ...

📺 Google DeepMind

👁️ 54K • 👍 2K • 💬 235 • ⏱️ 3:00 • 14h ago

---

**[FCC chair Carr defends new ban on foreign-made humanoid robots](https://www.youtube.com/watch?v=kTeCO57t9cs)**

The Trump administration will ban foreign-made humanoid robots in the U.S. as China seeks to dominate the emerging high-tech ...

📺 NBC News

👁️ 40K • 👍 259 • 💬 366 • ⏱️ 6:04 • 1d ago

---

**[You can hire these humanoid robots to clean your home in San Francisco](https://www.youtube.com/watch?v=SRfPI_6JitU)**

A San Francisco robotics startup has begun offering humanoid home cleaning services for $30 an hour to selected applicants in ...

📺 ABC7 News Bay Area

👁️ 2K • 👍 30 • 💬 27 • ⏱️ 2:01 • 7h ago

---

**[Robots working together with Gemini Robotics 2](https://www.youtube.com/watch?v=fo9WirRIaVs)**

Introducing multi-robot collaboration. This enables different types of robots to communicate and work together to solve complex ...

📺 Google DeepMind

👁️ 4K • 👍 160 • 💬 18 • ⏱️ 2:09 • 14h ago

---

**[Multi-robot collaboration with Gemini Robotics 2](https://www.youtube.com/watch?v=CiTPDm7PKW0)**

Multi-robot collaboration enables different types of robots to communicate and work together to solve complex problems.

📺 Google DeepMind

👁️ 6K • 👍 332 • 💬 23 • ⏱️ 2:32 • 14h ago

---

**[The FDA Just Changed Robotics Forever... Everyone Bought the Wrong Stock](https://www.youtube.com/watch?v=_6iqP7hdsk8)**

The FDA just changed the future of surgical robotics and almost everyone is watching the WRONG stock. While headlines focused ...

📺 Ross Givens

👁️ 12K • 👍 687 • 💬 193 • ⏱️ 11:31 • 1d ago

---

**[The Most Capable Humanoid Robot Yet!](https://www.youtube.com/watch?v=Q60VNdtyiAA)**

Google just released Gemini Robotics 2 today, and it's a much bigger leap than you may think. Unlike previous models, it ...

📺 Matt Wolfe

👁️ 5K • 👍 226 • 💬 8 • ⏱️ 0:56 • 12h ago

---

**[Viral video of new robot released by Chinese Unitree freaks out social media](https://www.youtube.com/watch?v=GHbywXK2NMo)**

Chinese robotics company Unitree released a new video of its "super athlete" model. It's going viral for its impressive all-terrain ...

📺 NBC News

👁️ 662K • 👍 7K • 💬 3K • ⏱️ 2:15 • 3d ago

---

**[CHINA CLAPS BACK After US BANS Its Humanoid Robots #news #technology #china #robot](https://www.youtube.com/watch?v=4YDY0QcIXb0)**

The United States just shut its doors to new Chinese humanoid and four legged robots, and Beijing did not stay silent. China's ...

📺 SXE China

👁️ 21K • 👍 291 • 💬 41 • ⏱️ 0:46 • 1d ago

---

**[Humanoid robot floors CEO with high-energy kick](https://www.youtube.com/watch?v=O4kdStMkYJQ)**

A video of EngineAI's CEO being knocked to the ground by one of the company's humanoid robots during a live demonstration ...

📺 CGTN

👁️ 18K • 👍 195 • 💬 9 • ⏱️ 0:18 • 22h ago

---

---

*Generated by PeekDeck - A glance is all you need*

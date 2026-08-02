---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-02T23:00:05.764471+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** August 02, 2026 at 23:00 UTC  
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

3d ago

---

**[What a cheap GPS actually reports vs what you can get out of it](https://www.reddit.com/r/robotics/comments/1vb5nx7/what_a_cheap_gps_actually_reports_vs_what_you_can/)**

Setup: a Raspberry Pi 4B on a small skid-steer chassis, a u-blox NEO-M9N (about $100), a BNO085 IMU, and hall encoders on the wheels. No RTK, no base station, no corrections Orange is pretty much every fix the receiver reported. Blue is the output seen after fusing those fixes with the IMU and wheel odometry in a UKF. Every fix was used, none were rejected in this entire run. What I can and cannot say about this is that, since this is a fair thing to ask: I don't have RTK ground truth for this run, so I can't claim the blue line is closer to the true path than the orange dots are. What I can say is that the filter's reported 1-sigma stayed around 2.5 m throughout, including while moving, and the fused output tracked the raw fixes to a median of 1.69 m. Both of those are self-reported numbers, not error against an independent reference. Other limitations worth stating: it's a single short run covering only about 20 m, there's no comparison against robot_localization on the same data yet, and heading comes from GPS track rather than a magnetometer, so it isn't meaningful for roughly the first minute of driving. The curve in the path is mechanical, the chassis pulls right about 3 deg/s. On the next run I'm closing the loop back to a physically marked start point so there's at least a real closure number, and replaying the same bag through robot_localization so it's a controlled comparison on identical input rather than one filter on its own. Also looking into borrowing an F9P for proper ground truth. Disclosure: I wrote the filter (FusionCore): https://github.com/manankharwar/fusioncore Happy to share the rosbag if anyone wants to run their own filter against it. Edit: rewrote this. Sorry if my english is bad...

3d ago

---

**[Google DeepMind announces Gemini Robotics 2](https://www.reddit.com/r/robotics/comments/1vaxn3p/google_deepmind_announces_gemini_robotics_2/)**

Google DeepMind has announced Gemini Robotics 2, its latest robotics foundation models, in early access. The release adds full-body control for humanoid robots, multi-step task execution with the ability to recover from mistakes, natural language communication, multi-robot coordination, on-device deployment, and new safety features that can reject unsafe commands or request human assistance when needed. Google demonstrated the models on Apptronik’s Apollo 2 humanoid, along with dexterous robotic hands and dual-arm systems. The update moves beyond robots performing isolated tasks and toward systems that can complete longer sequences of work while interacting more naturally with people and other robots.

🔗 [Automate](https://www.automate.org/ai/industry-insights/google-deepmind-announces-gemini-robotics-2-new-safety-measures-for-humanoids) • 3d ago

---

**[[R] Decentralized self-repair for modular robotic structures](https://www.reddit.com/r/robotics/comments/1vay0av/r_decentralized_selfrepair_for_modular_robotic/)**

Damage can fragment a modular robotic structure into disconnected pieces. We developed decentralized strategies that allow the surviving modules to consolidate, reorganize, and autonomously restore connectivity without a central controller. Across 1,000 simulated damage scenarios, the system retained at least 80% of surviving modules in its largest connected component even after 30% random failures, with near-perfect reconnection in fully connected cases. The broader goal is to develop machine analogues of homeostasis and morphogenesis: systems that can detect damage, adapt their physical organization, and preserve function. Technical article: https://www.manifoldrg.com/can-a-spacecraft-heal-itself/ Preprint: https://arxiv.org/abs/2607.13444 I’m one of the authors and would welcome feedback, particularly on the decentralized coordination strategy and the path toward hardware experiments.

3d ago

---

**[Testing a Bowden cable drive for a future project](https://www.reddit.com/r/robotics/comments/1vb635j/testing_a_bowden_cable_drive_for_a_future_project/)**

I'm exploring Bowden cables as a way to transmit motion when the motor can't be placed near the moving part. This is just a quick setup to see how smoothly it works before designing a larger mechanism. Any suggestions or ideas are welcome.

3d ago

---

**[A robot import ban may also be a ban on cheap iteration](https://www.reddit.com/r/robotics/comments/1vakosr/a_robot_import_ban_may_also_be_a_ban_on_cheap/)**

The new US restriction on foreign-made humanoids and quadrupeds is framed around security, but price and availability matter to research velocity. AP reports that Chinese manufacturers ship far more humanoids than US rivals and often at much lower prices. Labs learn by breaking hardware, replacing parts, and running many imperfect prototypes. If the affordable platforms disappear, better-funded companies may adapt while universities, startups, and independent builders reduce experiments or move them abroad. Would a certified research-only pathway preserve security without concentrating access? Or are connected embodied systems too difficult to contain once they enter a lab network? Source: https://apnews.com/article/china-us-humanoid-robots-ban-tech-c9f5e3c94d91d00eff3b61b141fab366

3d ago

---

**[how to build accelerator kit for robotics using Isaac sim and isaac lab](https://www.reddit.com/r/robotics/comments/1vb3ukp/how_to_build_accelerator_kit_for_robotics_using/)**

3d ago

---

**[That’s how we train the robot to follow you by reinforcement learning.](https://www.reddit.com/r/robotics/comments/1vb03v3/thats_how_we_train_the_robot_to_follow_you_by/)**

3d ago

---

**[Could there be an open-source layout robot for surveyors?](https://www.reddit.com/r/robotics/comments/1vb5lv8/could_there_be_an_opensource_layout_robot_for/)**

3d ago

---

**[I Got a Free Meal From a Private Chef—Who Filmed It All to Train Robots](https://www.reddit.com/r/robotics/comments/1vauzre/i_got_a_free_meal_from_a_private_chefwho_filmed/)**

A German startup sent a camera-wearing chef to my apartment. In exchange for a free lunch, I let them record every chop and stir to train future humanoids.

🔗 [WIRED](https://www.wired.com/story/i-let-a-private-chef-film-my-kitchen-for-robot-training-data/) • 3d ago

---

---

## Google News: "robotics"

**[Top 10 robotics stories of July 2026](https://www.therobotreport.com/top-10-robotics-stories-july-2026/)**

In July 2026, large funding rounds, new approaches to robot training, and new robot models drew our readers attention.

The Robot Report • 1d ago

---

**[San Francisco company offers cleaning service using humanoid robots](https://abcnews.com/Technology/san-francisco-company-offers-cleaning-service-humanoid-robots/story?id=135258956)**

A robotics startup has begun offering humanoid home cleaning services for $30 an hour to selected applicants in San Francisco.

abcnews.com • 2d ago

---

**[Mixed feelings: can China’s companion robots win a place at home?](https://www.scmp.com/tech/tech-trends/article/3362557/first-impressions-count-chinese-buyers-open-their-homes-ubtechs-consumer-humanoids)**

South China Morning Post • 16h ago

---

**[Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)**

From feet to fingertips — we are teaching robots intelligent whole-body control, fine dexterity, and teamwork to complete a broad range of complex tasks.

Google DeepMind • 3d ago

---

**[Graveyard guard shifts have gone to the (robot) dogs](https://www.businessinsider.com/security-guard-turnover-retention-robot-dogs-drones-patrol-2026-8)**

Asylon's robot dogs and drones are patrolling large facilities as the security industry faces a retention problem.

Business Insider • 1d ago

---

**[New AI and robotics studio at Lanier Tech to prepare students for manufacturing careers](https://www.wsbtv.com/news/local/new-ai-robotics-studio-lanier-tech-prepare-students-manufacturing-careers/RLZQ4R36OJGYJGC4YFGLOXCFDM/)**

College officials said graduates will learn how to assemble, troubleshoot and maintain AI-powered manufacturing equipment — skills that are in high demand as companies continue investing in automation.

WSB-TV • 2h ago

---

**[Google’s Gemini Can Now Stomp Around as a Humanoid Robot](https://www.wired.com/story/google-gemini-can-control-humanoid-robots/)**

The latest version of Google DeepMind's AI model includes a significant jump into “physical AGI.” But plopping AI into the real world comes with risks.

WIRED • 3d ago

---

**[The Robots Have Clocked in and Their Résumés Are Getting Weird](https://www.pymnts.com/technology/2026/robots-have-clocked-in-their-resumes-are-getting-weird/)**

At LaGuardia Airport, where travelers already negotiate with kiosks, scanners and charging stations, a headless, four-wheeled robot dog is now roaming

pymnts.com • 1d ago

---

**[Amazon ramps up delivery speed, robotics roll out](https://www.freightwaves.com/news/amazon-ramps-up-delivery-speed-robotics-roll-out)**

Amazon said it continued to expand ultra-fast delivery and improve fulfillment center efficiency, partly due to more robotics deployment, during the second quarter.

FreightWaves • 2d ago

---

**[Why this $11-billion money manager is buying Cameco, Kraken Robotics and trimming Canadian banks](https://www.theglobeandmail.com/investing/globe-advisor/advisor-funds/article-why-this-11-billion-money-manager-is-buying-cameco-kraken-robotics-and/)**

Craig Jerusalim of CIBC Asset Management has also been adding to Brookfield Asset Management

The Globe and Mail • 2d ago

---

---

## YouTube Videos: "robotics"

**[Gemini Robotics 2 brings whole body intelligence to robots](https://www.youtube.com/watch?v=4lSQnrMC6nY)**

For decades, we've dreamed of robots that can seamlessly step into our world and lend a hand. Now, that vision takes a ...

📺 Google DeepMind

👁️ 212K • 👍 6K • 💬 497 • ⏱️ 3:00 • 3d ago

---

**[FCC chair Carr defends new ban on foreign-made humanoid robots](https://www.youtube.com/watch?v=kTeCO57t9cs)**

The Trump administration will ban foreign-made humanoid robots in the U.S. as China seeks to dominate the emerging high-tech ...

📺 NBC News

👁️ 72K • 👍 371 • 💬 524 • ⏱️ 6:04 • 3d ago

---

**[Centaur-style robot being developed in Northern California causes a frenzy online](https://www.youtube.com/watch?v=BAbcOI6S2ck)**

Satyress Robotics, a company based in Auburn, California, is developing a 7-foot-tall centaur-style robot called "Three-Halves.

📺 KCRA 3

👁️ 6K • 👍 102 • 💬 63 • ⏱️ 1:03 • 1d ago

---

**[Testing Our New Robotic Hand](https://www.youtube.com/watch?v=Nhr7ZnFZYkA)**

Special thanks to Andrea, Jason, and the whole engineering team that made this video possible. Want to join an awesome team ...

📺 Foundation Robotics

👁️ 10K • 👍 403 • 💬 24 • ⏱️ 5:33 • 1d ago

---

**[Viral video of new robot released by Chinese Unitree freaks out social media](https://www.youtube.com/watch?v=GHbywXK2NMo)**

Chinese robotics company Unitree released a new video of its "super athlete" model. It's going viral for its impressive all-terrain ...

📺 NBC News

👁️ 1.2M • 👍 10K • 💬 4K • ⏱️ 2:15 • 5d ago

---

**[NEVER Upgrade This ULTIMAGE GARBAGE: War Robots Tempest](https://www.youtube.com/watch?v=b5nSOmIpu-Y)**

War Robots Gameplay: Ultimate TEMPEST sucks so bad - don't upgrade My War Robots Creator Link: https://wr.my.games/manni ...

📺 Manni-Gaming

👁️ 7K • 👍 316 • 💬 79 • ⏱️ 16:58 • 10h ago

---

**[DIY AI Xiaozhi Wire Robot - Part 2 | Adding TOF050C VL6180 Anti-Fall Distance Sensor](https://www.youtube.com/watch?v=XeehAdLLZN0)**

Welcome to Part 2 of my DIY AI Xiaozhi Wire Robot project! In this video, I upgrade the robot by installing a TOF050C VL6180 ...

📺 Creative Channel

👁️ 3K • 👍 202 • 💬 17 • ⏱️ 9:14 • 10h ago

---

**[Google Just Unveiled Its Most Advanced AI Robots Yet - Gemini Robotics 2](https://www.youtube.com/watch?v=s42VQasz4iI)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 21K • 👍 433 • 💬 37 • ⏱️ 9:54 • 2d ago

---

**[The $1/Hour Robot Is Coming: Four Industry Leaders Explain What’s Next](https://www.youtube.com/watch?v=TqNiSTeNtb0)**

(0:00) Intro: Humanoids, Robots, & AI+ (0:57) ANYbotics' Dr. Péter Fankhauser: Why ANYbotics Bet the Company on Four-Legged ...

📺 All-In Podcast

👁️ 107K • 👍 2K • 💬 322 • ⏱️ 1:08:35 • 4d ago

---

**[Intelligent whole-body control with Gemini Robotics 2](https://www.youtube.com/watch?v=9MNLEAzA59o)**

The world is built for human movements; it requires us to reach, bend, and balance in tight, cluttered spaces. While our previous ...

📺 Google DeepMind

👁️ 86K • 👍 2K • 💬 164 • ⏱️ 2:48 • 3d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-01T14:26:21.470043+00:00'
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

**Last Updated:** August 01, 2026 at 14:26 UTC  
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

2d ago

---

**[What a cheap GPS actually reports vs what you can get out of it](https://www.reddit.com/r/robotics/comments/1vb5nx7/what_a_cheap_gps_actually_reports_vs_what_you_can/)**

Setup: a Raspberry Pi 4B on a small skid-steer chassis, a u-blox NEO-M9N (about $100), a BNO085 IMU, and hall encoders on the wheels. No RTK, no base station, no corrections Orange is pretty much every fix the receiver reported. Blue is the output seen after fusing those fixes with the IMU and wheel odometry in a UKF. Every fix was used, none were rejected in this entire run. What I can and cannot say about this is that, since this is a fair thing to ask: I don't have RTK ground truth for this run, so I can't claim the blue line is closer to the true path than the orange dots are. What I can say is that the filter's reported 1-sigma stayed around 2.5 m throughout, including while moving, and the fused output tracked the raw fixes to a median of 1.69 m. Both of those are self-reported numbers, not error against an independent reference. Other limitations worth stating: it's a single short run covering only about 20 m, there's no comparison against robot_localization on the same data yet, and heading comes from GPS track rather than a magnetometer, so it isn't meaningful for roughly the first minute of driving. The curve in the path is mechanical, the chassis pulls right about 3 deg/s. On the next run I'm closing the loop back to a physically marked start point so there's at least a real closure number, and replaying the same bag through robot_localization so it's a controlled comparison on identical input rather than one filter on its own. Also looking into borrowing an F9P for proper ground truth. Disclosure: I wrote the filter (FusionCore): https://github.com/manankharwar/fusioncore Happy to share the rosbag if anyone wants to run their own filter against it. Edit: rewrote this. Sorry if my english is bad...

1d ago

---

**[Google DeepMind announces Gemini Robotics 2](https://www.reddit.com/r/robotics/comments/1vaxn3p/google_deepmind_announces_gemini_robotics_2/)**

Google DeepMind has announced Gemini Robotics 2, its latest robotics foundation models, in early access. The release adds full-body control for humanoid robots, multi-step task execution with the ability to recover from mistakes, natural language communication, multi-robot coordination, on-device deployment, and new safety features that can reject unsafe commands or request human assistance when needed. Google demonstrated the models on Apptronik’s Apollo 2 humanoid, along with dexterous robotic hands and dual-arm systems. The update moves beyond robots performing isolated tasks and toward systems that can complete longer sequences of work while interacting more naturally with people and other robots.

🔗 [Automate](https://www.automate.org/ai/industry-insights/google-deepmind-announces-gemini-robotics-2-new-safety-measures-for-humanoids) • 1d ago

---

**[[R] Decentralized self-repair for modular robotic structures](https://www.reddit.com/r/robotics/comments/1vay0av/r_decentralized_selfrepair_for_modular_robotic/)**

Damage can fragment a modular robotic structure into disconnected pieces. We developed decentralized strategies that allow the surviving modules to consolidate, reorganize, and autonomously restore connectivity without a central controller. Across 1,000 simulated damage scenarios, the system retained at least 80% of surviving modules in its largest connected component even after 30% random failures, with near-perfect reconnection in fully connected cases. The broader goal is to develop machine analogues of homeostasis and morphogenesis: systems that can detect damage, adapt their physical organization, and preserve function. Technical article: https://www.manifoldrg.com/can-a-spacecraft-heal-itself/ Preprint: https://arxiv.org/abs/2607.13444 I’m one of the authors and would welcome feedback, particularly on the decentralized coordination strategy and the path toward hardware experiments.

1d ago

---

**[Testing a Bowden cable drive for a future project](https://www.reddit.com/r/robotics/comments/1vb635j/testing_a_bowden_cable_drive_for_a_future_project/)**

I'm exploring Bowden cables as a way to transmit motion when the motor can't be placed near the moving part. This is just a quick setup to see how smoothly it works before designing a larger mechanism. Any suggestions or ideas are welcome.

1d ago

---

**[A robot import ban may also be a ban on cheap iteration](https://www.reddit.com/r/robotics/comments/1vakosr/a_robot_import_ban_may_also_be_a_ban_on_cheap/)**

The new US restriction on foreign-made humanoids and quadrupeds is framed around security, but price and availability matter to research velocity. AP reports that Chinese manufacturers ship far more humanoids than US rivals and often at much lower prices. Labs learn by breaking hardware, replacing parts, and running many imperfect prototypes. If the affordable platforms disappear, better-funded companies may adapt while universities, startups, and independent builders reduce experiments or move them abroad. Would a certified research-only pathway preserve security without concentrating access? Or are connected embodied systems too difficult to contain once they enter a lab network? Source: https://apnews.com/article/china-us-humanoid-robots-ban-tech-c9f5e3c94d91d00eff3b61b141fab366

2d ago

---

**[how to build accelerator kit for robotics using Isaac sim and isaac lab](https://www.reddit.com/r/robotics/comments/1vb3ukp/how_to_build_accelerator_kit_for_robotics_using/)**

1d ago

---

**[That’s how we train the robot to follow you by reinforcement learning.](https://www.reddit.com/r/robotics/comments/1vb03v3/thats_how_we_train_the_robot_to_follow_you_by/)**

1d ago

---

**[Could there be an open-source layout robot for surveyors?](https://www.reddit.com/r/robotics/comments/1vb5lv8/could_there_be_an_opensource_layout_robot_for/)**

1d ago

---

**[I Got a Free Meal From a Private Chef—Who Filmed It All to Train Robots](https://www.reddit.com/r/robotics/comments/1vauzre/i_got_a_free_meal_from_a_private_chefwho_filmed/)**

A German startup sent a camera-wearing chef to my apartment. In exchange for a free lunch, I let them record every chop and stir to train future humanoids.

🔗 [WIRED](https://www.wired.com/story/i-let-a-private-chef-film-my-kitchen-for-robot-training-data/) • 2d ago

---

---

## Google News: "robotics"

**[Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)**

From feet to fingertips — we are teaching robots intelligent whole-body control, fine dexterity, and teamwork to complete a broad range of complex tasks.

Google DeepMind • 1d ago

---

**[Graveyard guard shifts have gone to the (robot) dogs](https://www.businessinsider.com/security-guard-turnover-retention-robot-dogs-drones-patrol-2026-8)**

Asylon's robot dogs and drones are patrolling large facilities as the security industry faces a retention problem.

businessinsider.com • 5h ago

---

**[The Chinese robot army transforming the UK's retail industry](https://www.bbc.com/news/articles/c0jl8v23qwgo)**

Britain's weak productivity growth and labour shortages are creating an opportunity for China's robotics firms.

BBC • 2d ago

---

**[San Francisco company offers cleaning service using humanoid robots - ABC News](https://abcnews.com/Technology/san-francisco-company-offers-cleaning-service-humanoid-robots/story?id=135258956)**

A robotics startup has begun offering humanoid home cleaning services for $30 an hour to selected applicants in San Francisco.

ABC News - Breaking News, Latest News and Videos • 1d ago

---

**[Wetour Robotics Announces Share Consolidation](https://finance.yahoo.com/markets/stocks/articles/wetour-robotics-announces-share-consolidation-221800169.html)**

AUSTIN, Texas, July 29, 2026 (GLOBE NEWSWIRE) -- Wetour Robotics Limited (Nasdaq: WETO) ("Wetour Robotics" or the "Company"), a Physical AI infrastructure and wearable robotics company, today announced that it will effect a share consolidation of its ordinary shares of par value US$0.0001 each at a ratio of 1-for-100, effective on August 3, 2026 (the “Share Consolidation”). The Company’s ordinary shares are expected to begin trading on a post-consolidation basis at the open of the market session

Yahoo Finance • 2d ago

---

**[SF Robotics Startup Run By Ex-Cruise CEO Faces Class-Action Lawsuit Alleging Unpaid Wages](https://sfist.com/2026/07/30/contract-workers-sue-sf-robotics-startup-run-by-ex-cruise-ceo-alleging-unpaid-wages/)**

Following an earlier lawsuit over a damaged Airbnb rental, former Cruise CEO Kyle Vogt's startup Botco is now facing a class-action lawsuit from former contract workers who allege unpaid overtime and termination pay.

SFist • 1d ago

---

**[Amazon ramps up delivery speed, robotics roll out](https://www.freightwaves.com/news/amazon-ramps-up-delivery-speed-robotics-roll-out)**

Amazon said it continued to expand ultra-fast delivery and improve fulfillment center efficiency, partly due to more robotics deployment, during the second quarter.

FreightWaves • 19h ago

---

**[Why this $11-billion money manager is buying Cameco, Kraken Robotics and trimming Canadian banks](https://www.theglobeandmail.com/investing/globe-advisor/advisor-funds/article-why-this-11-billion-money-manager-is-buying-cameco-kraken-robotics-and/)**

Craig Jerusalim of CIBC Asset Management has also been adding to Brookfield Asset Management

The Globe and Mail • 1d ago

---

**[Muscle radar unlocks potential for future robotic limbs](https://techxplore.com/news/2026-07-muscle-radar-potential-future-robotic.html)**

Tech Xplore • 1d ago

---

**[Here's why a robotics firm founder hired Brockton students on the spot](https://www.enterprisenews.com/story/news/education/2026/07/30/brockton-high-school-drone-team-boston-robotics-company/91036144007/)**

Here's how a group of kids from Brockton ended up interning at a Boston robotics firm and what BHS's talented drone pilot plans to do next.

Enterprise News • 2d ago

---

---

## YouTube Videos: "robotics"

**[Gemini Robotics 2 brings whole body intelligence to robots](https://www.youtube.com/watch?v=4lSQnrMC6nY)**

For decades, we've dreamed of robots that can seamlessly step into our world and lend a hand. Now, that vision takes a ...

📺 Google DeepMind

👁️ 163K • 👍 5K • 💬 422 • ⏱️ 3:00 • 1d ago

---

**[Google Just Unveiled Its Most Advanced AI Robots Yet - Gemini Robotics 2](https://www.youtube.com/watch?v=s42VQasz4iI)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 9K • 👍 261 • 💬 28 • ⏱️ 9:54 • 17h ago

---

**[FCC chair Carr defends new ban on foreign-made humanoid robots](https://www.youtube.com/watch?v=kTeCO57t9cs)**

The Trump administration will ban foreign-made humanoid robots in the U.S. as China seeks to dominate the emerging high-tech ...

📺 NBC News

👁️ 68K • 👍 345 • 💬 500 • ⏱️ 6:04 • 2d ago

---

**[The $1/Hour Robot Is Coming: Four Industry Leaders Explain What’s Next](https://www.youtube.com/watch?v=TqNiSTeNtb0)**

(0:00) Intro: Humanoids, Robots, & AI+ (0:57) ANYbotics' Dr. Péter Fankhauser: Why ANYbotics Bet the Company on Four-Legged ...

📺 All-In Podcast

👁️ 100K • 👍 2K • 💬 312 • ⏱️ 1:08:35 • 3d ago

---

**[You can hire these humanoid robots to clean your home in San Francisco](https://www.youtube.com/watch?v=SRfPI_6JitU)**

A San Francisco robotics startup has begun offering humanoid home cleaning services for $30 an hour to selected applicants in ...

📺 ABC7 News Bay Area

👁️ 6K • 👍 63 • 💬 42 • ⏱️ 2:01 • 1d ago

---

**[Multi-robot collaboration with Gemini Robotics 2](https://www.youtube.com/watch?v=CiTPDm7PKW0)**

Multi-robot collaboration enables different types of robots to communicate and work together to solve complex problems.

📺 Google DeepMind

👁️ 14K • 👍 494 • 💬 32 • ⏱️ 2:32 • 1d ago

---

**[America Banning Robot Vacuums](https://www.youtube.com/watch?v=utALr9hru-k)**

📺 Omar Agamy

👁️ 498K • 👍 22K • 💬 2K • ⏱️ 0:40 • 1d ago

---

**[Advanced dexterity with Gemini Robotics 2](https://www.youtube.com/watch?v=O9-650iHAls)**

To be genuinely useful in our homes and workplaces, robots need finesse. Gemini Robotics 2 unlocks a new level of physical ...

📺 Google DeepMind

👁️ 18K • 👍 652 • 💬 81 • ⏱️ 2:17 • 1d ago

---

**[Robots working together with Gemini Robotics 2](https://www.youtube.com/watch?v=fo9WirRIaVs)**

Introducing multi-robot collaboration. This enables different types of robots to communicate and work together to solve complex ...

📺 Google DeepMind

👁️ 7K • 👍 287 • 💬 34 • ⏱️ 2:09 • 1d ago

---

**[The FDA Just Changed Robotics Forever... Everyone Bought the Wrong Stock](https://www.youtube.com/watch?v=_6iqP7hdsk8)**

The FDA just changed the future of surgical robotics and almost everyone is watching the WRONG stock. While headlines focused ...

📺 Ross Givens

👁️ 13K • 👍 709 • 💬 158 • ⏱️ 11:31 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

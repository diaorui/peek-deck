---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-02T18:06:21.308537+00:00'
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

**Last Updated:** August 02, 2026 at 18:06 UTC  
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

2d ago

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

2d ago

---

**[A robot import ban may also be a ban on cheap iteration](https://www.reddit.com/r/robotics/comments/1vakosr/a_robot_import_ban_may_also_be_a_ban_on_cheap/)**

The new US restriction on foreign-made humanoids and quadrupeds is framed around security, but price and availability matter to research velocity. AP reports that Chinese manufacturers ship far more humanoids than US rivals and often at much lower prices. Labs learn by breaking hardware, replacing parts, and running many imperfect prototypes. If the affordable platforms disappear, better-funded companies may adapt while universities, startups, and independent builders reduce experiments or move them abroad. Would a certified research-only pathway preserve security without concentrating access? Or are connected embodied systems too difficult to contain once they enter a lab network? Source: https://apnews.com/article/china-us-humanoid-robots-ban-tech-c9f5e3c94d91d00eff3b61b141fab366

3d ago

---

**[how to build accelerator kit for robotics using Isaac sim and isaac lab](https://www.reddit.com/r/robotics/comments/1vb3ukp/how_to_build_accelerator_kit_for_robotics_using/)**

2d ago

---

**[That’s how we train the robot to follow you by reinforcement learning.](https://www.reddit.com/r/robotics/comments/1vb03v3/thats_how_we_train_the_robot_to_follow_you_by/)**

3d ago

---

**[Could there be an open-source layout robot for surveyors?](https://www.reddit.com/r/robotics/comments/1vb5lv8/could_there_be_an_opensource_layout_robot_for/)**

2d ago

---

**[I Got a Free Meal From a Private Chef—Who Filmed It All to Train Robots](https://www.reddit.com/r/robotics/comments/1vauzre/i_got_a_free_meal_from_a_private_chefwho_filmed/)**

A German startup sent a camera-wearing chef to my apartment. In exchange for a free lunch, I let them record every chop and stir to train future humanoids.

🔗 [WIRED](https://www.wired.com/story/i-let-a-private-chef-film-my-kitchen-for-robot-training-data/) • 3d ago

---

---

## Google News: "robotics"

**[Google’s Gemini Can Now Stomp Around as a Humanoid Robot](https://www.wired.com/story/google-gemini-can-control-humanoid-robots/)**

The latest version of Google DeepMind's AI model includes a significant jump into “physical AGI.” But plopping AI into the real world comes with risks.

WIRED • 3d ago

---

**[Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)**

From feet to fingertips — we are teaching robots intelligent whole-body control, fine dexterity, and teamwork to complete a broad range of complex tasks.

Google DeepMind • 3d ago

---

**[Google DeepMind says Gemini Robotics 2 enables full body control](https://www.therobotreport.com/google-deepmind-says-gemini-robotics-2-enables-full-body-control/)**

Gemini Robotics 2 enables robots to reason through every movement, unlocking a broad range of tasks, DeepMind said.

The Robot Report • 5h ago

---

**[Graveyard guard shifts have gone to the (robot) dogs](https://www.businessinsider.com/security-guard-turnover-retention-robot-dogs-drones-patrol-2026-8)**

Asylon's robot dogs and drones are patrolling large facilities as the security industry faces a retention problem.

Business Insider • 1d ago

---

**[Mixed feelings: can China’s companion robots win a place at home?](https://www.scmp.com/tech/tech-trends/article/3362557/first-impressions-count-chinese-buyers-open-their-homes-ubtechs-consumer-humanoids)**

South China Morning Post • 12h ago

---

**[San Francisco company offers cleaning service using humanoid robots - ABC News](https://abcnews.com/Technology/san-francisco-company-offers-cleaning-service-humanoid-robots/story?id=135258956)**

A robotics startup has begun offering humanoid home cleaning services for $30 an hour to selected applicants in San Francisco.

ABC News - Breaking News, Latest News and Videos • 2d ago

---

**[US bans foreign-made robots, China threatens to retaliate](https://www.morningbrew.com/stories/us-bans-foreign-made-robots-china-retaliate)**

They won't come after the Roomba you already own, but it might make it harder to get a new one.

morningbrew.com • 1d ago

---

**[The Robots Have Clocked in and Their Résumés Are Getting Weird](https://www.pymnts.com/technology/2026/robots-have-clocked-in-their-resumes-are-getting-weird/)**

At LaGuardia Airport, where travelers already negotiate with kiosks, scanners and charging stations, a headless, four-wheeled robot dog is now roaming

PYMNTS.com • 1d ago

---

**[Do Robot Dogs Have More Fun Than Humanoids? One Explores, One Folds Laundry](https://spectrum.ieee.org/video-robot-gemini2-ai-robot)**

This week’s selection of awesome robot videos includes robot shadow puppets and golden eagles toying with a drone

IEEE Spectrum • 2d ago

---

**[Tau Robotics launches humanoid robot home cleaning service in San Francisco](https://www.yahoo.com/news/videos/tau-robotics-launches-humanoid-robot-010804608.html)**

Tau Robotics is offering humanoid robot cleaning services to selected applicants, with robots that can vacuum, clean counters and take out the trash.

Yahoo • 16h ago

---

---

## YouTube Videos: "robotics"

**[Gemini Robotics 2 brings whole body intelligence to robots](https://www.youtube.com/watch?v=4lSQnrMC6nY)**

For decades, we've dreamed of robots that can seamlessly step into our world and lend a hand. Now, that vision takes a ...

📺 Google DeepMind

👁️ 207K • 👍 6K • 💬 486 • ⏱️ 3:00 • 3d ago

---

**[America Banning Robot Vacuums](https://www.youtube.com/watch?v=utALr9hru-k)**

📺 Omar Agamy

👁️ 560K • 👍 24K • 💬 2K • ⏱️ 0:40 • 2d ago

---

**[Robot Window Cleaners Are Here But Do They Work?](https://www.youtube.com/watch?v=SPV-hstjRGM)**

Robots are doing more and more for us these days but can they clean windows? Ecovacs Mini Window Cleaner: ...

📺 Proper DIY - Tools & Effect

👁️ 29K • 👍 2K • 💬 175 • ⏱️ 12:29 • 11h ago

---

**[😳WTF… Mark Zuckerberg Robot Asked For WHAT?!](https://www.youtube.com/watch?v=M6qdlOEyT-8)**

📺 David Nino Rodriguez

👁️ 2K • 👍 208 • 💬 12 • ⏱️ 0:32 • 54m ago

---

**[AI Robots Future Is Now Almost Indistinguishable From Humans... 🤯 Humanoids Take over](https://www.youtube.com/watch?v=PXBGLSMu_Yw)**

The future isn't coming—it's already here. Today's AI-powered humanoid robots can walk, talk, make eye contact, understand ...

📺 ejunky66

👁️ 11K • 👍 177 • 💬 16 • ⏱️ 1:00 • 2d ago

---

**[Google Just Unveiled Its Most Advanced AI Robots Yet - Gemini Robotics 2](https://www.youtube.com/watch?v=s42VQasz4iI)**

Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726 Subscribe To My Newsletter ...

📺 TheAIGRID

👁️ 19K • 👍 412 • 💬 36 • ⏱️ 9:54 • 1d ago

---

**[DIY AI Xiaozhi Wire Robot - Part 2 | Adding TOF050C VL6180 Anti-Fall Distance Sensor](https://www.youtube.com/watch?v=XeehAdLLZN0)**

Welcome to Part 2 of my DIY AI Xiaozhi Wire Robot project! In this video, I upgrade the robot by installing a TOF050C VL6180 ...

📺 Creative Channel

👁️ 2K • 👍 152 • 💬 9 • ⏱️ 9:14 • 5h ago

---

**[&quot;TREACHEROUS Waters Ahead!&quot; Will Super Intelligent Robots End Humanity? + Science vs God Debate](https://www.youtube.com/watch?v=5ZruLGRmU9g)**

Check out Freecash today using my link https://bit.ly/4vtcdz6 and get a $10 bonus after completing your first offer. Can science ...

📺 Piers Morgan Uncensored

👁️ 131K • 👍 2K • 💬 1K • ⏱️ 1:04:34 • 2d ago

---

**[This Robot Goalkeeper Is Actually Insane! #shorts #soccer #football](https://www.youtube.com/watch?v=vmuL5K3lnas)**

Can a $500 robot goalkeeper stop a real soccer shot? ⚽ This kid decided to find out by putting it to the ultimate test. The first ...

📺 Shutter Hype

👁️ 5K • 💬 14 • ⏱️ 0:34 • 5h ago

---

**[Framework Laptops and a Robot Cleaner?](https://www.youtube.com/watch?v=PtCMsXYAPyc)**

This week, Marques, Andrew, and David kick things off by talking about the new Apple leasing program. After that, they get into ...

📺 WVFRM Podcast

👁️ 122K • 👍 3K • 💬 542 • ⏱️ 1:35:30 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

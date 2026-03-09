---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-09T15:33:59.865958+00:00'
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

**Last Updated:** March 09, 2026 at 15:33 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Our robot can pick itself up now. Where should I take it?](https://www.reddit.com/r/robotics/comments/1ropyzo/our_robot_can_pick_itself_up_now_where_should_i/)**

Got fall recovery working this week. No scripted motion, just RL figured out how to get up on its own. The way it does is kinda violent though, like it's pissed off about falling lol My wish was this little guy could follow me around everywhere without me having to pick it up every time it tips over. Have a walk, kids playing in the yard, whatever, ideally 99% of the time it handles itself. We've been testing it on gravel, cobblestone, and stone-slab paths so far, it's doing better than we expected. More terrain tests on r/MondoRobots if you're curious. Now we're thinking about what's next, what other surfaces should we be throwing at it? Stairs, snow, sand? Would love to hear what matters most to you guys.

11h ago

---

**[A wearable Centaur robot for load-carriage walking assistance (Paper)](https://www.reddit.com/r/robotics/comments/1rowx4j/a_wearable_centaur_robot_for_loadcarriage_walking/)**

Paper: Sage Journals: Design, modeling, control, and evaluation of a wearable Centaur robot for load-carriage walking assistance: https://journals.sagepub.com/doi/10.1177/02783649261418155

4h ago

---

**[First time building a hobbyist robot from scratch, it has 4-legged 12-DOF, I call it Cubic Doggo!](https://www.reddit.com/r/robotics/comments/1rouerc/first_time_building_a_hobbyist_robot_from_scratch/)**

(Sorry, updated to a better video) The awkward walking gait (and the wrong direction, lol) so far is the simplest 2-phase gait Gemini threw at me, but I am so happy it walks at all! Which next steps do you think I should take first? What I have in mind so far are fine-tunning the gait and adding more gaits manually, adding a control, adding a lidar, designing a PCB for better power management, or directly trying to port it to Isaac Sim? Of course, I will need to put some adhesive on the legs first and study the response mechanisms (effort) offered by these DYNAMIXEL motors. But any recommendations will be appreciated! https://github.com/SphericalCowww/ROS_leggedRobot_testBed

7h ago

---

**[Peak Engineering: Using $20k in industrial arm just to pull a piano.](https://www.reddit.com/r/robotics/comments/1ro96ee/peak_engineering_using_20k_in_industrial_arm_just/)**

Saw this installation called Tug of Memories by TASKO. It’s just one industrial arm playing a piano using a bunch of tension cables and pulleys. It’s a total nightmare of pinch points and over-engineering, but seeing it move is actually pretty satisfying. Zero practical use, 10/10 for the "because we can" factor.

23h ago

---

**[Humanoid robot goes for a stroll with a robot dog](https://www.reddit.com/r/robotics/comments/1ro9nz1/humanoid_robot_goes_for_a_stroll_with_a_robot_dog/)**

22h ago

---

**[New Arduino VENTUNO Q, 16GB RAM, Qualcomm 8 core, 40 TOPs](https://www.reddit.com/r/robotics/comments/1rowlcy/new_arduino_ventuno_q_16gb_ram_qualcomm_8_core_40/)**

USB PD power M.2 expansion slot (Gen 4???) 16GB RAM Wifi 6 STM32H5F5 Runs Ubuntu, pretty cool tbh. For more Advanced robotics projects this is ideal. https://www.arduino.cc/product-ventuno-q/

🔗 [youtube.com](https://www.youtube.com/watch?v=SzT6vDtz6rU) • 5h ago

---

**[Issue with Lidar points](https://www.reddit.com/r/robotics/comments/1rp1hwz/issue_with_lidar_points/)**

Hello everyone I am trying to run my simulation of amr into gazebo. Everything's working fine except when I turn robot the lidar points are also rotating with respect to robot. For linear movements the lidar points are still. But for angular movementzz even the lidar points are rotating. Can anyone help me with this?

1h ago

---

**[Why I Love the Fuchikoma — Ghost in the Shell’s Most Underrated Robot](https://www.reddit.com/r/robotics/comments/1rp1864/why_i_love_the_fuchikoma_ghost_in_the_shells_most/)**

I wrote a piece on my beloved Fuchikoma from the Ghost In The Shell franchise. Robot designers and engineers, let me know how it lands!

🔗 [hubrisofprogress.substack.com](https://hubrisofprogress.substack.com/p/why-i-love-the-fuchikoma-ghost-in) • 1h ago

---

**[Autonomous overnight experiment loop for robot learning: agent modifies code, runs MuJoCo sim, analyzes renderings, repeats](https://www.reddit.com/r/robotics/comments/1romucz/autonomous_overnight_experiment_loop_for_robot/)**

Hi folks, first time posting here I built an autonomous experiment loop for robotics research, based on Karpathy's recent autoresearch, and wanted to share the results with you guys Github: https://github.com/jellyheadandrew/autoresearch-robotics https://i.redd.it/156cdaawaxng1.gif It consists of same core loop: agent modifies the training code, runs the experiment, checks if the result improved, keeps or discards, and repeats autonomously The key adaptation is replacing the LLM training loop with a robotics simulation feedback loop - the agent optimizes policy training code against task success rate AND renderings from MuJoCo, instead of validation loss What's different Visual feedback. After each experiment, MuJoCo renders the robot's behavior and Claude Vision analyzes the frames. The agent sees what the robot is doing wrong, not just number Experimentally, I feel it provides better qualitative feedbacks for next trial. (Example1) GRASPS cube! but cant transport to goal (dist 0.22) discard balanced throughput+reward shaping (58K steps, 11K updates) (Example2) inconsistent gripper orientation, no contact discard vectorized HER + N_UPDATES=10 (55K steps but too few updates) I ran experiments on very simple robot-learning task (FetchReach). The agent started from an SAC+HER baseline and autonomously discovered that a simple proportional controller solves the task. https://preview.redd.it/ddc3mde5axng1.png?width=1482&format=png&auto=webp&s=1eea396a9579d1ddc0b7cb3956c07a821a79347e I'm currently running more complex tasks (FetchPush and FetchPickPlace), and will try VLAs after I get some GPU compute credits. Would love feedback from anyone working on robotics or sim-to-real!

14h ago

---

**[Do you think every home will eventually have a robot?](https://www.reddit.com/r/robotics/comments/1rot74q/do_you_think_every_home_will_eventually_have_a/)**

I've been thinking about this lately and I'm curious what people here think. Do you believe that robots will eventually become a normal part of everyday life, like smartphones or laptops today? As in, most households having at least one. A few things I'm especially curious about: Do you think robots could become a main interface for interacting with AI in the future? How comfortable would you personally feel about having a robot in your home? What kind of robot would you actually want? a purely practical tool (cleaning, tasks, assistance) entertainment / companionship or something that combines both Interested to hear different perspectives. I feel like people's expectations of robots vary a lot.

8h ago

---

---

## Google News: "robotics"

**[OpenAI robotics leader resigns over concerns about Pentagon AI deal](https://www.npr.org/2026/03/08/nx-s1-5741779/openai-resigns-ai-pentagon-guardrails-military)**

A senior member of OpenAI's robotics team said guardrails around certain AI uses were not sufficiently defined before OpenAI announced an agreement with the Pentagon.

NPR • 18h ago

---

**[Why Richtech Robotics Stock Plummeted by Over 30% Last Month](https://www.fool.com/investing/2026/03/08/why-richtech-robotics-stock-plummeted-by-over-30-l/)**

Several negative developments put quite a hurt on the company's stock.

The Motley Fool • 14h ago

---

**[Former Google AI Researcher Sets Up AI Robotics Startup in Tokyo](https://www.bloomberg.com/news/articles/2026-03-09/ex-google-researcher-seeks-to-transform-japan-s-robots-with-ai)**

Bloomberg.com • 11h ago

---

**[These robots are coming for the jobs no one wants — and could fill workforce gaps](https://www.businessinsider.com/agility-robotics-humanoid-robots-labor-shortage-aging-workforce-2026-3)**

Agility Robotics is building humanoid bots to address a labor gap in the manufacturing industry, which is seeing vacancies and an aging workforce.

Business Insider • 1d ago

---

**[New ultra-low-cost technique could slash the price of soft robotics](https://techxplore.com/news/2026-03-ultra-technique-slash-price-soft.html)**

Tech Xplore • 13h ago

---

**[School kids and stage shows: Faraday Future sends new robots to Texas](https://www.stocktitan.net/news/FFAI/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-investor-6ls34ya8jp4a.html)**

Texas delivery to NS Federation opens education and performance uses for FF robots, while U.S. officials express support for its embodied AI strategy.

Stock Titan • 12h ago

---

**[Video: Hyundai's firefighting robots lead the way into burning buildings](https://newatlas.com/robotics/hyundai-firefighting-robots/)**

Hyundai has donated four super-tough unmanned robotic vehicles to firefighters in Korea for use in high-risk situations. The autonomous vehicles will deal with the initial stages of a fire to provide more information and safety to firefighters.

New Atlas • 1d ago

---

**[Amazon Staffers Learning Hard Lesson as Company Cuts Robotics Jobs](https://malaysia.news.yahoo.com/amazon-staffers-learning-hard-lesson-204500657.html)**

Who's automating the automators?

Yahoo News Malaysia • 1d ago

---

**[High-tech player in collectibles: Startup uses robotics and AI to sort, analyze and sell trading cards](https://www.geekwire.com/2026/high-tech-player-in-collectibles-startup-uses-robotics-and-ai-to-sort-analyze-and-sell-trading-cards/)**

Gradient's Renton, Wash., office space is home to 10 million sports and gaming cards, where a team of card geeks and engineers are using technology to upend a $15 billion U.S. market.

GeekWire • 55m ago

---

**[Humanoid robots learn parkour maneuvers from human motion recordings](https://interestingengineering.com/ai-robotics/us-humanoid-robots-learns-tough-parkour-skills)**

Humanoid robots learn parkour using a new AI framework, enabling them to navigate obstacles with human-like agility in complex environments.

Interesting Engineering • 3d ago

---

---

## YouTube Videos: "robotics"

**[New OpenClaw Robot Feels Shockingly Aware (Detonated Skynet)](https://www.youtube.com/watch?v=LBYiSAj10aA)**

OpenClaw just demonstrated a system that lets robots build a persistent memory of the real world. Instead of only navigating a ...

📺 AI Revolution

👁️ 33K • 👍 980 • 💬 71 • ⏱️ 14:51 • 14h ago

---

**[Unrestricted AI in a robot does exactly what experts warned](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

AI robot. ChatGPT in Robot. Could AI become dangerous? Can we trust AI? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 667K • 👍 40K • 💬 4K • ⏱️ 16:54 • 5d ago

---

**[Shocking Light-Powered Robot Runs Without Batteries &amp; Cyborg Cockroach](https://www.youtube.com/watch?v=2_igeW1d8RA)**

Robotics just entered a very strange new phase. Scientists built a tiny robot that runs purely on light with no batteries, processors, ...

📺 AI Revolution

👁️ 22K • 👍 792 • 💬 59 • ⏱️ 14:35 • 4d ago

---

**[E23: NVIDIA&#39;s HUGE Robotics Announcements Will Change Everything](https://www.youtube.com/watch?v=wAlmgDudmkk)**

Register for NVIDIA GTC 2026 on March 16-19 and join me! » Registration link (do this first!): https://tsy.link/gtc2026 » Jensen ...

📺 Ticker Symbol: YOU

👁️ 24K • 👍 1K • 💬 71 • ⏱️ 29:53 • 1d ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=7I-KWkV0JUM)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN

👁️ 214K • 👍 2K • 💬 316 • ⏱️ 29:41 • 3d ago

---

**[China&#39;s Most Agile Robots in 2026 – They&#39;re Doing Things That Shouldn&#39;t Be Possible](https://www.youtube.com/watch?v=_z5NxUToeZU)**

China's humanoid robots just performed the world's first continuous parkour flips, 3-meter aerial flips, and a 7.5-rotation Airflare ...

📺 TechFrontierNow

👁️ 58K • 👍 373 • 💬 80 • ⏱️ 9:26 • 4d ago

---

**[AI Patrol Robots Are Now Walking Real Streets in China 🤖🇨🇳](https://www.youtube.com/watch?v=zOp4W1Xl9Fs)**

This AI-powered patrol robot is already walking real city streets in China alongside security officers. The robot can move ...

📺 Onyez 

👁️ 983 • 👍 15 • 💬 2 • ⏱️ 0:39 • 9h ago

---

**[This Robot &amp; Elon Musk Dance Broke the Internet 🕺🔥#ElonMusk #Tesla #Optimus #TeslaBot #Robotics](https://www.youtube.com/watch?v=EnduYx4nguI)**

A moment like this perfectly captures how technology can be both revolutionary and entertaining at the same time. Watching Elon ...

📺 Billionaire Shots

👁️ 37K • 👍 2K • 💬 275 • ⏱️ 0:13 • 5d ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=sFFMMg2XWyQ)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN Europe

👁️ 789K • 👍 1K • 💬 17 • ⏱️ 29:40 • 5d ago

---

**[Prime Time CRAZY Robot Fighting! Round 2 of NHRL&#39;s 2026 Pro World Championships (March)](https://www.youtube.com/watch?v=-x5Fzq4Hig0)**

The 2026 NHRL Pro World Championship Season is HERE! This is Round 2. This. Is. Prime Time! We are down to the final 8 bots ...

📺 NHRL

👁️ 43K • 👍 454 • 💬 40 • ⏱️ 3:23:56 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

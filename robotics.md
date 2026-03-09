---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-09T02:12:54.118725+00:00'
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

**Last Updated:** March 09, 2026 at 02:12 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Peak Engineering: Using $20k in industrial arm just to pull a piano.](https://www.reddit.com/r/robotics/comments/1ro96ee/peak_engineering_using_20k_in_industrial_arm_just/)**

Saw this installation called Tug of Memories by TASKO. It’s just one industrial arm playing a piano using a bunch of tension cables and pulleys. It’s a total nightmare of pinch points and over-engineering, but seeing it move is actually pretty satisfying. Zero practical use, 10/10 for the "because we can" factor.

9h ago

---

**[Humanoid robot goes for a stroll with a robot dog](https://www.reddit.com/r/robotics/comments/1ro9nz1/humanoid_robot_goes_for_a_stroll_with_a_robot_dog/)**

9h ago

---

**[People can trust robots that fail as long as they know how they’ll fail](https://www.reddit.com/r/robotics/comments/1roabua/people_can_trust_robots_that_fail_as_long_as_they/)**

Robotics researcher Holly Yanco describes research looking at how people respond when robots fail during tasks. One finding was that people can still trust a robot that fails often if the limits of the system are clear. Her example was a robot that performs task A 100% of the time and task B 0% of the time. Users can still trust the system because they understand what it can and cannot do. They will rely on it for task A and avoid using it for task B.

8h ago

---

**[Autonomous overnight experiment loop for robot learning: agent modifies code, runs MuJoCo sim, analyzes renderings, repeats](https://www.reddit.com/r/robotics/comments/1romucz/autonomous_overnight_experiment_loop_for_robot/)**

Hi folks, first time posting here I built an autonomous experiment loop for robotics research, based on Karpathy's recent autoresearch, and wanted to share the results with you guys Github: https://github.com/jellyheadandrew/autoresearch-robotics https://i.redd.it/156cdaawaxng1.gif It consists of same core loop: agent modifies the training code, runs the experiment, checks if the result improved, keeps or discards, and repeats autonomously The key adaptation is replacing the LLM training loop with a robotics simulation feedback loop - the agent optimizes policy training code against task success rate AND renderings from MuJoCo, instead of validation loss What's different Visual feedback. After each experiment, MuJoCo renders the robot's behavior and Claude Vision analyzes the frames. The agent sees what the robot is doing wrong, not just number Experimentally, I feel it provides better qualitative feedbacks for next trial. (Example1) GRASPS cube! but cant transport to goal (dist 0.22) discard balanced throughput+reward shaping (58K steps, 11K updates) (Example2) inconsistent gripper orientation, no contact discard vectorized HER + N_UPDATES=10 (55K steps but too few updates) I ran experiments on very simple robot-learning task (FetchReach). The agent started from an SAC+HER baseline and autonomously discovered that a simple proportional controller solves the task. https://preview.redd.it/ddc3mde5axng1.png?width=1482&format=png&auto=webp&s=1eea396a9579d1ddc0b7cb3956c07a821a79347e I'm currently running more complex tasks (FetchPush and FetchPickPlace), and will try VLAs after I get some GPU compute credits. Would love feedback from anyone working on robotics or sim-to-real!

40m ago

---

**[6 axis robot (WIP)](https://www.reddit.com/r/robotics/comments/1rnuz5e/6_axis_robot_wip/)**

Little progress update on my 6 axis robot. It has a wrist now! 2 more axis to go before it’s complete. I've also switched from using a breadboard to a proper perfboard circuit.

21h ago

---

**[For those deploying robots IRL... where does simulation fall short for you?](https://www.reddit.com/r/robotics/comments/1ro7vjq/for_those_deploying_robots_irl_where_does/)**

Hi everyone I'm a grad french student getting into robotics simulation and I've been reading a lot about sim-to-real transfer lately. The more I dig into it, the more I realize there's a huge gap between what simulators promise and what actually works when you put a robot in the real world. I would love to hear from people who actually deal with this day to day: Where do your robots most often fail when you go from sim to real deployment? Is it stuff you could have predicted, or mostly edge cases nobody saw coming? When something breaks in the real world, can you actually reproduce it in simulation? What makes that hard? If you could add one thing to your current simulation/testing pipeline that doesn't exist yet, what would it be? Genuinely curious .... trying to figure out if this is a space worth diving deeper into for my research. Any perspective helps, even if it's just "simulation is fine, the real problem is X." Merci beaucou !

10h ago

---

**[Building simple and inexpensive animatronic](https://www.reddit.com/r/robotics/comments/1roe357/building_simple_and_inexpensive_animatronic/)**

My daughter (11yo) wants to build a bipedal animatronic and I'm looking for a simple kit or something we can put together without a high cost. She wants to be a few feet high and resemble this Vee character https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.wikia.nocookie.net%2F2c7c7e9f-fd4a-4b7e-99ad-53216dbdb05b%2Fscale-to-width%2F755&f=1&nofb=1&ipt=3435994b5d38266f04bb4caa669e22dbcf85757bd86dffc342a6c8eaab344891 I work in robotics but haven't completed many hobby kits. I'm comfortable soldering and with tools but I don't understand kinematics or anything. Please let me know if you can provide suggestions? I was thinking something along these lines for the base but it would be taller https://www.robotshop.com/products/lynxmotion-biped-brat-kit-no-servos-or-electronics-brat-blk?qd=3863c5f9d2d553499b3f180b869b6336

6h ago

---

**[A robot guided by living rat brain cells that could learn from experience](https://www.reddit.com/r/robotics/comments/1rnexhi/a_robot_guided_by_living_rat_brain_cells_that/)**

1d ago

---

**[PeppyOS: a simpler alternative to ROS 2 (now with containers support)](https://www.reddit.com/r/robotics/comments/1ro1tc4/peppyos_a_simpler_alternative_to_ros_2_now_with/)**

Hey everyone, A few weeks ago I shared PeppyOS, a simpler alternative to ROS 2 that I've been building. The feedback was really helpful, and I've been heads-down since then working on a new feature to simplify the installation of nodes: Containers support. The goal hasn't changed: someone new should be able to pick this up and have nodes communicating in about half an hour. I'd love to hear what you think, especially from people who tried it last time or who've been waiting for Python & containers support.

15h ago

---

**[Robotic arm I designed a while back](https://www.reddit.com/r/robotics/comments/1rnni5l/robotic_arm_i_designed_a_while_back/)**

Link to the video of it working: https://www.youtube.com/watch?v=8weu8V_CPMU&t=77s

1d ago

---

---

## Google News: "robotics"

**[OpenAI robotics leader resigns over concerns about Pentagon AI deal](https://www.npr.org/2026/03/08/nx-s1-5741779/openai-resigns-ai-pentagon-guardrails-military)**

A senior member of OpenAI's robotics team said guardrails around certain AI uses were not sufficiently defined before OpenAI announced an agreement with the Pentagon.

NPR • 5h ago

---

**[Amazon Staffers Learning Hard Lesson as Company Cuts Robotics Jobs](https://futurism.com/robots-and-machines/amazon-robotics-layoffs)**

The tech and commerce giant is laying off robotics staffers in the latest round of cuts attributable to pandemic-era overhiring.

Futurism • 1d ago

---

**[Why Richtech Robotics Stock Plummeted by Over 30% Last Month](https://www.fool.com/investing/2026/03/08/why-richtech-robotics-stock-plummeted-by-over-30-l/)**

Several negative developments put quite a hurt on the company's stock.

The Motley Fool • 2h ago

---

**[Faraday Future Founder and Co-CEO YT Jia Shares Weekly Investor Update: Completes Delivery of Master Robot and Pre-Delivery of Aegis Robot to NS Federation in Texas, Expanding Education and Performance Scenarios for EAI Robotics](https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-32)**

FF leadership also held in-depth discussions last week in Washington, D.C. with officials from the U.S. Department of Transportation and the Department of Commerce. Conversations focused on topics including tariff policies on auto parts, the development of the EAI EV and EAI robotics industries,

Faraday Future • 2h ago

---

**[OpenAI Robotics Head Quits Over Pentagon Partnership](https://www.pymnts.com/artificial-intelligence-2/2026/openai-robotics-head-quits-over-pentagon-partnership/)**

OpenAI’s robotics lead has left the company due to its partnership with the Pentagon. Caitlin Kalinowski announced her departure from the artificial

PYMNTS.com • 4h ago

---

**[300+ student engineers compete at S.C. robotics finals in Lexington County](https://www.wltx.com/article/tech/300-student-engineers-compete-sc-robotics-finals-lexington-county/101-3d407c1c-2458-4d99-a1fd-35f5e6473e45)**

Dozens of teams gathered at River Bluff High School Saturday to vie for a spot at the VEX Robotics World Championship in St. Louis this April.

WLTX • 10h ago

---

**[New ultra-low-cost technique could slash the price of soft robotics](https://techxplore.com/news/2026-03-ultra-technique-slash-price-soft.html)**

Tech Xplore • 32m ago

---

**[OpenAI's robotics hardware lead resigns following deal with the Department of Defense](https://www.engadget.com/ai/openais-robotics-hardware-lead-resigns-following-deal-with-the-department-of-defense-195918599.html)**

Caitlin Kalinowski explained on X that certain guardrails "deserved more deliberation than they got" when announcing her departure.

Engadget • 11h ago

---

**['Mesoscale' swimmers could pave way for drug delivery robots inside the body](https://phys.org/news/2026-03-mesoscale-swimmers-pave-drug-delivery.html)**

Phys.org • 6h ago

---

**[OpenAI’s Robotics Chief Quits After Firm’s Pentagon Deal](https://www.forbes.com/sites/mikestunson/2026/03/07/openais-robotics-chief-leaving-tech-company-after-its-deal-with-pentagon/)**

Forbes • 1d ago

---

---

## YouTube Videos: "robotics"

**[Unrestricted AI in a robot does exactly what experts warned](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

AI robot. ChatGPT in Robot. Could AI become dangerous? Can we trust AI? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 630K • 👍 38K • 💬 4K • ⏱️ 16:54 • 5d ago

---

**[Prime Time CRAZY Robot Fighting! Round 2 of NHRL&#39;s 2026 Pro World Championships (March)](https://www.youtube.com/watch?v=-x5Fzq4Hig0)**

The 2026 NHRL Pro World Championship Season is HERE! This is Round 2. This. Is. Prime Time! We are down to the final 8 bots ...

📺 NHRL

👁️ 17K • 👍 426 • 💬 25 • ⏱️ 3:23:56 • 22h ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=7I-KWkV0JUM)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN

👁️ 182K • 👍 2K • 💬 272 • ⏱️ 29:41 • 3d ago

---

**[Shocking Light-Powered Robot Runs Without Batteries &amp; Cyborg Cockroach](https://www.youtube.com/watch?v=2_igeW1d8RA)**

Robotics just entered a very strange new phase. Scientists built a tiny robot that runs purely on light with no batteries, processors, ...

📺 AI Revolution

👁️ 22K • 👍 778 • 💬 56 • ⏱️ 14:35 • 4d ago

---

**[China&#39;s Most Agile Robots in 2026 – They&#39;re Doing Things That Shouldn&#39;t Be Possible](https://www.youtube.com/watch?v=_z5NxUToeZU)**

China's humanoid robots just performed the world's first continuous parkour flips, 3-meter aerial flips, and a 7.5-rotation Airflare ...

📺 TechFrontierNow

👁️ 56K • 👍 367 • 💬 77 • ⏱️ 9:26 • 4d ago

---

**[robot doll link in bio #xdollhub#realdoll#siliconedoll#realisitcdoll#dolls](https://www.youtube.com/watch?v=R9wAzzcVDqs)**

📺 XDollHub

👁️ 58K • 👍 587 • 💬 3 • ⏱️ 0:21 • 4d ago

---

**[NEW Robot VECTOR will be a BIG PROBLEM in War Robots](https://www.youtube.com/watch?v=jPUWFiMaMnQ)**

War Robots Gameplay: NEW Robot VECTOR is going to be annoying in WR. Here's my new YouTube Channel ⁨@ManniRAID⁩ ...

📺 Manni-Gaming

👁️ 7K • 👍 370 • 💬 119 • ⏱️ 15:18 • 13h ago

---

**[Non-Stop INSANE Robot Fighting Action: Round 2 of NHRL&#39;s 2026 Pro World Championship KO Show (March)](https://www.youtube.com/watch?v=7tQ5Gyr3SYE)**

Round 2 of the 2026 NHRL Pro World Championship kicks off NOW! PRIME TIME is here: https://youtube.com/live/-x5Fzq4Hig0 ...

📺 NHRL

👁️ 36K • 👍 335 • 💬 13 • ⏱️ 3:35:12 • 1d ago

---

**[Why Does Invincible Have Robot Parts In S4 Trailer? 👀](https://www.youtube.com/watch?v=Kubl6gTcpHE)**

Invincible season 4, Invincible season 4 release date, Invincible season 4 trailer, Invincible season 4 trailer breakdown, Invincible ...

📺 RecapNova

👁️ 703K • 👍 16K • 💬 48 • ⏱️ 0:29 • 4d ago

---

**[This Robot &amp; Elon Musk Dance Broke the Internet 🕺🔥#ElonMusk #Tesla #Optimus #TeslaBot #Robotics](https://www.youtube.com/watch?v=EnduYx4nguI)**

A moment like this perfectly captures how technology can be both revolutionary and entertaining at the same time. Watching Elon ...

📺 Billionaire Shots

👁️ 37K • 👍 2K • 💬 274 • ⏱️ 0:13 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-09T10:12:40.364271+00:00'
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

**Last Updated:** March 09, 2026 at 10:12 UTC  
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

6h ago

---

**[First time building a hobbyist robot from scratch, it has 4-legged 12-DOF, I call it Cubic Doggo!](https://www.reddit.com/r/robotics/comments/1rouerc/first_time_building_a_hobbyist_robot_from_scratch/)**

(Sorry, updated to a better video) The awkward walking gait (and the wrong direction, lol) so far is the simplest 2-phase gait Gemini threw at me, but I am so happy it walks at all! Which next steps do you think I should take first? What I have in mind so far are fine-tunning the gait and adding more gaits manually, adding a control, adding a lidar, designing a PCB for better power management, or directly trying to port it to Isaac Sim? Of course, I will need to put some adhesive on the legs first and study the response mechanisms (effort) offered by these DYNAMIXEL motors. But any recommendations will be appreciated! https://github.com/SphericalCowww/ROS_leggedRobot_testBed

1h ago

---

**[Peak Engineering: Using $20k in industrial arm just to pull a piano.](https://www.reddit.com/r/robotics/comments/1ro96ee/peak_engineering_using_20k_in_industrial_arm_just/)**

Saw this installation called Tug of Memories by TASKO. It’s just one industrial arm playing a piano using a bunch of tension cables and pulleys. It’s a total nightmare of pinch points and over-engineering, but seeing it move is actually pretty satisfying. Zero practical use, 10/10 for the "because we can" factor.

17h ago

---

**[Humanoid robot goes for a stroll with a robot dog](https://www.reddit.com/r/robotics/comments/1ro9nz1/humanoid_robot_goes_for_a_stroll_with_a_robot_dog/)**

17h ago

---

**[Autonomous overnight experiment loop for robot learning: agent modifies code, runs MuJoCo sim, analyzes renderings, repeats](https://www.reddit.com/r/robotics/comments/1romucz/autonomous_overnight_experiment_loop_for_robot/)**

Hi folks, first time posting here I built an autonomous experiment loop for robotics research, based on Karpathy's recent autoresearch, and wanted to share the results with you guys Github: https://github.com/jellyheadandrew/autoresearch-robotics https://i.redd.it/156cdaawaxng1.gif It consists of same core loop: agent modifies the training code, runs the experiment, checks if the result improved, keeps or discards, and repeats autonomously The key adaptation is replacing the LLM training loop with a robotics simulation feedback loop - the agent optimizes policy training code against task success rate AND renderings from MuJoCo, instead of validation loss What's different Visual feedback. After each experiment, MuJoCo renders the robot's behavior and Claude Vision analyzes the frames. The agent sees what the robot is doing wrong, not just number Experimentally, I feel it provides better qualitative feedbacks for next trial. (Example1) GRASPS cube! but cant transport to goal (dist 0.22) discard balanced throughput+reward shaping (58K steps, 11K updates) (Example2) inconsistent gripper orientation, no contact discard vectorized HER + N_UPDATES=10 (55K steps but too few updates) I ran experiments on very simple robot-learning task (FetchReach). The agent started from an SAC+HER baseline and autonomously discovered that a simple proportional controller solves the task. https://preview.redd.it/ddc3mde5axng1.png?width=1482&format=png&auto=webp&s=1eea396a9579d1ddc0b7cb3956c07a821a79347e I'm currently running more complex tasks (FetchPush and FetchPickPlace), and will try VLAs after I get some GPU compute credits. Would love feedback from anyone working on robotics or sim-to-real!

8h ago

---

**[Do you think every home will eventually have a robot?](https://www.reddit.com/r/robotics/comments/1rot74q/do_you_think_every_home_will_eventually_have_a/)**

I've been thinking about this lately and I'm curious what people here think. Do you believe that robots will eventually become a normal part of everyday life, like smartphones or laptops today? As in, most households having at least one. A few things I'm especially curious about: Do you think robots could become a main interface for interacting with AI in the future? How comfortable would you personally feel about having a robot in your home? What kind of robot would you actually want? a purely practical tool (cleaning, tasks, assistance) entertainment / companionship or something that combines both Interested to hear different perspectives. I feel like people's expectations of robots vary a lot.

3h ago

---

**[People can trust robots that fail as long as they know how they’ll fail](https://www.reddit.com/r/robotics/comments/1roabua/people_can_trust_robots_that_fail_as_long_as_they/)**

Robotics researcher Holly Yanco describes research looking at how people respond when robots fail during tasks. One finding was that people can still trust a robot that fails often if the limits of the system are clear. Her example was a robot that performs task A 100% of the time and task B 0% of the time. Users can still trust the system because they understand what it can and cannot do. They will rely on it for task A and avoid using it for task B.

16h ago

---

**[6 axis robot (WIP)](https://www.reddit.com/r/robotics/comments/1rnuz5e/6_axis_robot_wip/)**

Little progress update on my 6 axis robot. It has a wrist now! 2 more axis to go before it’s complete. I've also switched from using a breadboard to a proper perfboard circuit.

1d ago

---

**[For those deploying robots IRL... where does simulation fall short for you?](https://www.reddit.com/r/robotics/comments/1ro7vjq/for_those_deploying_robots_irl_where_does/)**

Hi everyone I'm a grad french student getting into robotics simulation and I've been reading a lot about sim-to-real transfer lately. The more I dig into it, the more I realize there's a huge gap between what simulators promise and what actually works when you put a robot in the real world. I would love to hear from people who actually deal with this day to day: Where do your robots most often fail when you go from sim to real deployment? Is it stuff you could have predicted, or mostly edge cases nobody saw coming? When something breaks in the real world, can you actually reproduce it in simulation? What makes that hard? If you could add one thing to your current simulation/testing pipeline that doesn't exist yet, what would it be? Genuinely curious .... trying to figure out if this is a space worth diving deeper into for my research. Any perspective helps, even if it's just "simulation is fine, the real problem is X." Merci beaucou !

18h ago

---

**[Building simple and inexpensive animatronic](https://www.reddit.com/r/robotics/comments/1roe357/building_simple_and_inexpensive_animatronic/)**

My daughter (11yo) wants to build a bipedal animatronic and I'm looking for a simple kit or something we can put together without a high cost. She wants to be a few feet high and resemble this Vee character https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.wikia.nocookie.net%2F2c7c7e9f-fd4a-4b7e-99ad-53216dbdb05b%2Fscale-to-width%2F755&f=1&nofb=1&ipt=3435994b5d38266f04bb4caa669e22dbcf85757bd86dffc342a6c8eaab344891 I work in robotics but haven't completed many hobby kits. I'm comfortable soldering and with tools but I don't understand kinematics or anything. Please let me know if you can provide suggestions? I was thinking something along these lines for the base but it would be taller https://www.robotshop.com/products/lynxmotion-biped-brat-kit-no-servos-or-electronics-brat-blk?qd=3863c5f9d2d553499b3f180b869b6336

14h ago

---

---

## Google News: "robotics"

**[OpenAI robotics leader resigns over concerns about Pentagon AI deal](https://www.npr.org/2026/03/08/nx-s1-5741779/openai-resigns-ai-pentagon-guardrails-military)**

A senior member of OpenAI's robotics team said guardrails around certain AI uses were not sufficiently defined before OpenAI announced an agreement with the Pentagon.

NPR • 13h ago

---

**[New ultra-low-cost technique could slash the price of soft robotics](https://techxplore.com/news/2026-03-ultra-technique-slash-price-soft.html)**

Tech Xplore • 8h ago

---

**[Former Google AI Researcher Sets Up AI Robotics Startup in Tokyo](https://www.bloomberg.com/news/articles/2026-03-09/ex-google-researcher-seeks-to-transform-japan-s-robots-with-ai)**

Bloomberg • 5h ago

---

**[These robots are coming for the jobs no one wants — and could fill workforce gaps](https://www.businessinsider.com/agility-robotics-humanoid-robots-labor-shortage-aging-workforce-2026-3)**

Agility Robotics is building humanoid bots to address a labor gap in the manufacturing industry, which is seeing vacancies and an aging workforce.

Business Insider • 1d ago

---

**[Why Richtech Robotics Stock Plummeted by Over 30% Last Month](https://www.fool.com/investing/2026/03/08/why-richtech-robotics-stock-plummeted-by-over-30-l/)**

Several negative developments put quite a hurt on the company's stock.

The Motley Fool • 9h ago

---

**[School kids and stage shows: Faraday Future sends new robots to Texas](https://www.stocktitan.net/news/FFAI/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-investor-6ls34ya8jp4a.html)**

Texas delivery to NS Federation opens education and performance uses for FF robots, while U.S. officials express support for its embodied AI strategy.

Stock Titan • 7h ago

---

**[Amazon Staffers Learning Hard Lesson as Company Cuts Robotics Jobs](https://malaysia.news.yahoo.com/amazon-staffers-learning-hard-lesson-204500657.html)**

Who's automating the automators?

Yahoo News Malaysia • 1d ago

---

**[How Disney brought a robotic Olaf to life for its new Paris park](https://www.fastcompany.com/91501979/how-disney-brought-a-robotic-olaf-to-life-for-its-new-paris-park)**

The robot captures the soul of the animated character, thanks to a custom AI engine and clever robotics.

Fast Company • 3m ago

---

**[Inside Elon Musk's robot vision of the future](https://nypost.com/2026/03/08/tech/inside-elon-musks-robot-vision-of-the-future/)**

The Tesla titan and other techies are bullish on ‘amazing abundance.’

New York Post • 21h ago

---

**[Video: Hyundai's firefighting robots lead the way into burning buildings](https://newatlas.com/robotics/hyundai-firefighting-robots/)**

Hyundai has donated four super-tough unmanned robotic vehicles to firefighters in Korea for use in high-risk situations. The autonomous vehicles will deal with the initial stages of a fire to provide more information and safety to firefighters.

New Atlas • 1d ago

---

---

## YouTube Videos: "robotics"

**[New OpenClaw Robot Feels Shockingly Aware (Detonated Skynet)](https://www.youtube.com/watch?v=LBYiSAj10aA)**

OpenClaw just demonstrated a system that lets robots build a persistent memory of the real world. Instead of only navigating a ...

📺 AI Revolution

👁️ 22K • 👍 750 • 💬 60 • ⏱️ 14:51 • 9h ago

---

**[Unrestricted AI in a robot does exactly what experts warned](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

AI robot. ChatGPT in Robot. Could AI become dangerous? Can we trust AI? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 654K • 👍 39K • 💬 4K • ⏱️ 16:54 • 5d ago

---

**[HONOR ROBOT PHONE: A Revolutionary Invention](https://www.youtube.com/watch?v=-uv7SE3_WzA)**

It's not just a phone; it's a revolutionary invention that uses advanced actuators to move its head (the camera module) and interact ...

📺 SciVion

👁️ 3K • 👍 115 • 💬 3 • ⏱️ 0:30 • 14h ago

---

**[Desk buddy | Companion robot with wheels | Code &amp; 3D included](https://www.youtube.com/watch?v=ktWnwJ-e-_w)**

In this project I built a tiny desk companion robot using an ESP32, OLED display and two N20 motors. The robot roams around ...

📺 Tech Talkies

👁️ 9K • 👍 404 • 💬 30 • ⏱️ 4:51 • 1d ago

---

**[Shocking Light-Powered Robot Runs Without Batteries &amp; Cyborg Cockroach](https://www.youtube.com/watch?v=2_igeW1d8RA)**

Robotics just entered a very strange new phase. Scientists built a tiny robot that runs purely on light with no batteries, processors, ...

📺 AI Revolution

👁️ 22K • 👍 786 • 💬 57 • ⏱️ 14:35 • 4d ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=7I-KWkV0JUM)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN

👁️ 207K • 👍 2K • 💬 303 • ⏱️ 29:41 • 3d ago

---

**[Prime Time CRAZY Robot Fighting! Round 2 of NHRL&#39;s 2026 Pro World Championships (March)](https://www.youtube.com/watch?v=-x5Fzq4Hig0)**

The 2026 NHRL Pro World Championship Season is HERE! This is Round 2. This. Is. Prime Time! We are down to the final 8 bots ...

📺 NHRL

👁️ 29K • 👍 442 • 💬 29 • ⏱️ 3:23:56 • 1d ago

---

**[E23: NVIDIA&#39;s HUGE Robotics Announcements Will Change Everything](https://www.youtube.com/watch?v=wAlmgDudmkk)**

Register for NVIDIA GTC 2026 on March 16-19 and join me! » Registration link (do this first!): https://tsy.link/gtc2026 » Jensen ...

📺 Ticker Symbol: YOU

👁️ 22K • 👍 952 • 💬 53 • ⏱️ 29:53 • 19h ago

---

**[AI Patrol Robots Are Now Walking Real Streets in China 🤖🇨🇳](https://www.youtube.com/watch?v=zOp4W1Xl9Fs)**

This AI-powered patrol robot is already walking real city streets in China alongside security officers. The robot can move ...

📺 Onyez 

👁️ 694 • 👍 16 • 💬 2 • ⏱️ 0:39 • 4h ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=sFFMMg2XWyQ)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN Europe

👁️ 753K • 👍 1K • 💬 14 • ⏱️ 29:40 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

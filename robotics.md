---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-17T22:58:20.844657+00:00'
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

**Last Updated:** June 17, 2026 at 22:58 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[3D-printed rovers using pointcloud/depth (DA3) instead of LIDAR](https://www.reddit.com/r/robotics/comments/1u8cjkw/3dprinted_rovers_using_pointclouddepth_da3/)**

Hey everybody! Hobbyist here with an update on my cheap rover swarm project. I've been trying out Depth Anything 3 and wanted to share, because the results of such minimal hardware surprised me. The setup: each rover is just a XIAO ESP32-S3 Sense (~$15 board with a tiny onboard camera) in a 3D printed body. The ESP32 is basically a sender, it streams the camera over WiFi and reports temperature/battery/telemetry. All the heavy lifting (DA3 inference, navigation) runs on a PC that acts as the brain. No lidar, no depth sensor, one cheap RGB camera. DA3 gives me a point cloud per frame and can merge multiple frames into a larger cloud. Seeing a $15 camera produce a usable 3D-ish image of the room is still kind of wild to me. Eventually I want to use it for navigation - a kind of "poor man's lidar". It estimates what's near at three heights (eye level, above, below) to give a rough obstacle sense without a dedicated sensor. Secondly for visualization at the moment, but the goal is to stitch frames into an environment map. Positioning is currently handled by ArUco markers around the room (solvePnP). Still early and held together with hope, but it's been fun pushing this hardware further than it wamts to go. :-)

7h ago

---

**[Boston Dynamics Atlas Product Director on Humanoid ROI](https://www.reddit.com/r/robotics/comments/1u8e4xf/boston_dynamics_atlas_product_director_on/)**

Aya Durbin says humanoid robots need to prove real customer value before they can scale. She says the goal for Atlas is not just to be impressive, but to deliver positive ROI for customers. Boston Dynamics is focusing on industrial environments first, especially work that is hard to hire for, physically demanding and difficult to automate with traditional systems. She also says customers need robots that are reliable, useful and able to become a trusted part of the workforce.

7h ago

---

**[Hand project posponed to September](https://www.reddit.com/r/robotics/comments/1u8kkjr/hand_project_posponed_to_september/)**

So this is my 2nd project and final project in high school, quite ambitious i gotta say. I was trying to make a anthropomorphic robotic hand . So i grabbed the palm and finger design from here. But i wanted to make my own thingys where the strings are attached , and add adduction ( fingers get clamped together). I learned how to use fusion and how to 3d print , i didnt know what was clearance. I learned that quickly . I dont have a 3d printer at home so i needed to pay for everything , i spent all my budget for this project , and i was so close to finishing everything but , my strings lacked tension and some 3d printed parts broke and i really dont want to spend more money. I finally decided to postpone the project until september because i got in an engineering school and i hope they have a 3d printer i can use freely. On top of that i think its better to try out some new stuff throughout the summer like i want to make those plasma ball thingys with the glass surrounding it and you can touch it. I am a little disappointed cause i was so close but let's see. I left you some pics too ​

3h ago

---

**[Target : autonomous robots for mapping](https://www.reddit.com/r/robotics/comments/1u8mcei/target_autonomous_robots_for_mapping/)**

Hi r/robotics ! I’m currently working on a robotic car project for mapping, and I’d like to share my progress and get some feedback from the community. So far, the main issues I’ve encountered (and resolved) are as follows: - Synchronizing the car’s position on the map (as indicated by the gyroscope) with the position of the digitized image based on the car’s position - Managing the motors’ power supply (complex wiring) However, there are still a few issues for which I could use some advice. - It seems that over time, a discrepancy is developing between the robot’s position on the map and its actual position as measured by the gyroscope. Is this an inaccuracy in the gyroscope that could be corrected through code? - The scanner works but remains fairly inaccurate; any recommendations are welcome - The robot’s path tends to veer off course, so I’m considering adding speed encoders to implement a path correction system (I assume the problem stems from the fact that the speed of each motor isn’t always precise) My goal is to build a fully autonomous car capable of mapping its surroundings (I'll add a webcam). Feel free to share any ideas you might have. my target is build a full self driving car able to mapping his environment ( i will adding webcam). Github : https://github.com/enzocolombat/EC-Hub/

2h ago

---

**[Foundry Humanoid robotics](https://www.reddit.com/r/robotics/comments/1u8fvh8/foundry_humanoid_robotics/)**

There is an ad going around about a humanoid robot to help around the house. Does anyone know about that? ​ It feels scammy mostly because there is a video on their site showing them folding a shirt that is obviously AI. (The shirt doesn't fold correctly) ​ I guess just curious if anyone knows anything about them. ​

🔗 [Foundry](https://foundryhumanoid.com/) • 5h ago

---

**[Sampling-based motion planning, genetic algorithms, and biological evolution might all be running the same underlying search algorithm](https://www.reddit.com/r/robotics/comments/1u8pbqm/samplingbased_motion_planning_genetic_algorithms/)**

I work in robotics, and have for almost a decade now. I keep noticing that a huge chunk of search-under-uncertainty problems, in robotics and outside it, converge on the same two-step architecture: generate variation indiscriminately first, then apply a scoring/selection pressure that keeps what works and discards what doesn't. No model of the problem is required upfront. Most the "intelligence" lives in the selection step, not the generation step. The clearest version of this in our own field is sampling-based motion planning. RRT and its relatives don't try to compute a path analytically. They expand randomly in many directions through the configuration space and then retain/extend the branches that make progress toward the goal, pruning the rest. Genetic algorithms and evolution strategies (CMA-ES, for instance) run an identical loop in parameter space instead of configuration space: generate a population of variants, score them against a fitness (cost) function, keep the survivors, repeat. Simulated annealing is a single-particle version of the same thing, generate a random perturbation, accept or reject it based on a score. Once I started paying attention to this pattern, I noticed it shows up well outside robotics too, in places that have nothing to do with computer science: Slime mold expanding in all directions through a maze of food sources, with the inefficient tendrils pruned back, and famously reconstructing something close to the Tokyo rail network when food sources are placed at the positions of major stations. Evolution itself: random mutation generates variation with zero regard for whether it's useful, and survival does the selecting after the fact. Neural development: neurons and synaptic connections proliferate in directions that aren't pre-planned, and dopamine-linked reinforcement selectively stabilizes the ones that turn out to matter. Once I started looking for more instances, I found two more that fit the same structure almost exactly: The immune system: B-cells mutate antibody variants somewhat randomly (somatic hypermutation) and the ones that bind the pathogen get clonally selected and expanded. Thought/creativity: you can't generate a genuinely novel idea by deduction from evidence that it's correct. The evidence only exists after the idea does. Novelty has to come first; judgment comes second. That last one turns out to have a surprisingly direct precedent. Henri Poincaré, describing how he worked out the theta-fuchsian functions, wrote that ideas rose in crowds and collided in his mind until pairs interlocked into stable combinations, almost like watching his own unconscious work made partially visible to consciousness, and that what got selected from that flood of combinations was governed by something close to an aesthetic sense of mathematical elegance. That's a generate-then-select loop running inside a human mind, described in 1908. The principle has been formalized more than once since then, from different directions: Richard Dawkins' Universal Darwinism: the claim that variation/selection/retention isn't a biology-specific mechanism but a substrate-independent algorithm that biology happens to be one instance of. Donald Campbell's blind variation and selective retention (BVSR), later developed extensively by Dean Keith Simonton, which applies the same two-step structure directly to creative cognition. Karl Popper's conjectures and refutations model of how knowledge grows: blind generation of new theories, followed by selective retention of the ones that survive criticism. Popper explicitly treated this as the same process as biological evolution, just running on ideas instead of organisms. Gerald Edelman's Neural Darwinism (Theory of Neuronal Group Selection), the formal version of the neuron/dopamine point above: synaptic overproduction followed by activity-dependent selective stabilization. Worth flagging here: I'm not claiming the expansion step is ever truly random. In every example above, the variation is guided. Slime mold follows chemoattractant gradients, not isotropic noise. Mutation isn't uniform across a genome, there are hotspots and repair biases. Axon growth follows chemical guidance cues, not random angles. Informed RRT* deliberately biases sampling toward the goal region instead of sampling uniformly. Even Poincaré's account isn't pure randomness, he describes an aesthetic sense that seems to steer which combinations even get generated, not just which ones survive afterward. Liane Gabora has made this exact critique of BVSR, that calling the variation "blind" overstates how random it actually is. But that's the part I find more interesting, not less. The expansion step across all of these systems is intelligently informed, biased toward promising regions by something the system already "knows," and yet it still needs the separate selection/scoring step on top of that guidance to actually converge. Neither half does the job alone: the guidance is too crude or too local to solve the problem outright (that's why expansion is still happening at all instead of direct computation), and the selection pressure has no foresight of its own, it only works because it's filtering output that the guided expansion already biased toward viable territory. Has anyone else found that this specific combination, intelligently biased expansion paired with a separate selection/scoring step, actually performs best in practice? I have personally found, that at least for my applications in autonomous vehicles and motion planning, this combination works the best. Curious whether other people doing sampling-based planning, evolutionary algorithms, or other search methods have found the same thing I have: that this architecture outperforms the alternatives, rather than just being one option among several that works comparably well. I will personally only ever use this type of algorithm after realizing this is how nature does it. Lastly, I am not proposing that analytical algorithms are better or worse than machine learning algorithms. I believe that HOW this is solved is irrespective of the fundamental search algorithm of the universe I have observed. I believe that it is the expand, then score mechanism that is important here, and does not exclude any method of expansion or scoring, as I have observed this in the above stated forms across nature. Thanks for the read if you're here, I've been thinking about this all year and needed to post it somewhere.

5m ago

---

**[Universal Manipulation Exoskeleton (UME): a low-cost exoskeleton with real-time haptic torque feedback](https://www.reddit.com/r/robotics/comments/1u799px/universal_manipulation_exoskeleton_ume_a_lowcost/)**

From Litian Liang on 𝕏 (thread with multiple videos): https://x.com/litian_liang/status/2066541466286215570 This work is done in Inclusion AI lab at Ant Group, advised by James (Jingxi) Xu and Professor Mark Cutkosky from Stanford BDML lab. Website: https://ume-exo.github.io Paper: https://arxiv.org/abs/2606.14218

1d ago

---

**[ICRA'27](https://www.reddit.com/r/robotics/comments/1u844ka/icra27/)**

Hello Everyone, I am preparing my manuscript for upcoming ICRA'27. But They have page limit of 8 pages, including references. As well, They don't accept any supplementary documents. So my question is how can I show more experiments and ablation studies? Because 8 page is not sufficient. Any tips? Much appreciated!!

14h ago

---

**[Resume Review for Automate 2026 / Robotics Software Engineer (Master's Student)](https://www.reddit.com/r/robotics/comments/1u8eia6/resume_review_for_automate_2026_robotics_software/)**

Title: Resume Review for Automate 2026 / Robotics Software Engineer (Master's Student) Hi everyone, I'm attending Automate 2026 in Chicago and would appreciate feedback on my resume. I'm a Master of Science in Computer Science at Bridgewater State University (graduating December 2025). I have 4+ years of software engineering experience and hands-on robotics experience with ROS2, TurtleBot4, SLAM, Nav2, OpenCV, computer vision, and autonomous navigation projects. I'm targeting these roles: Robotics Software Engineer Robotics Engineer Autonomous Systems Engineer Computer Vision Engineer Software Engineer (Robotics) I'd appreciate feedback on: Is my resume strong enough for robotics and automation companies? Are there any red flags? Should I emphasize my robotics projects more than my software engineering experience? Is the resume optimized for career fairs and recruiter screening? What skills or keywords are missing? Thanks in advance for any advice.

6h ago

---

**[Halfwiredtv: we're at 76+ members in 4 days on discord](https://www.reddit.com/r/robotics/comments/1u88n66/halfwiredtv_were_at_76_members_in_4_days_on/)**

HalfwiredTV is a community for people who want to learn robotics, build projects, and collaborate with others. Our long-term goal is simple: Get everyone to a level where they can confidently learn, build and collaborate on robotics projects together in livestreams. What You'll Find Here -- People learning together teaching each other on calls in dedicated channels for topics (created as per demand) Project teammates Livestream collaborations and study sessions (uhm.. with meme songs) , also whenever anyone has something interesting to talk and show regardless of their skill level. We recently had our first livestream on a member's lazer scanning workflow for their robocar Robotics discussions ranging from complete beginners to advanced builders Your skill level doesn't matter. If you're curious, willing to learn, and willing to build, you're in the right place. Come join us : https://discord.com/channels/1514229376152113172/1514973636258172949

10h ago

---

---

## Google News: "robotics"

**[Can robots replace my real friends?](https://www.yahoo.com/news/videos/robots-replace-real-friends-212318842.html)**

Can real #friends be replaced by robots? Business Insider visited the Realbotix #factory in #LasVegas to find out. #robotics #robots #AI

Yahoo • 1h ago

---

**[AI coding agents taught robots how to install GPUs and cut zip ties](https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/)**

Nvidia's self-improvement program for robots enlists teams of AI coding agents.

Ars Technica • 1d ago

---

**[Alibaba unveils AI models for robots, amid shift from chatbots to agents](https://www.reuters.com/world/asia-pacific/alibaba-unveils-ai-models-robots-amid-shift-chatbots-agents-2026-06-16/)**

Reuters • 1d ago

---

**[Collecting robot training data is dirty, unglamorous work. Some AI labs are already paying XDOF to do it.](https://techcrunch.com/2026/06/17/collecting-robot-training-data-is-dirty-unglamorous-work-some-ai-labs-are-already-paying-xdof-to-do-it/)**

If physical AI is going to match the accomplishments of LLMs, there's a data problem that needs to be solved.

TechCrunch • 7h ago

---

**[Built Robotics, Penn xLAB to develop physical AI for construction](https://www.therobotreport.com/xlab-and-built-robotics-partner-to-advance-construction/)**

xLAB and Built Robotics partner to capture additional data, advancing AI models to improve construction site safety.

The Robot Report • 1d ago

---

**[Micropolis Robotics Expands Physical AI Portfolio with Five-Year Autonomous Sweeper Deployment Agreement with Abu Dhabi Government](https://finance.yahoo.com/technology/ai/articles/micropolis-robotics-expands-physical-ai-222700818.html)**

Long-term agreement with the Department of Municipalities and Transport advances the deployment of Physical AI and autonomous municipal services across Abu Dhabi Micropolis AI Robotics AI-powered autonomous sweeper Micropolis AI Robotics AI-powered, autonomous sweeper DUBAI, United Arab Emirates, June 16, 2026 (GLOBE NEWSWIRE) -- Micropolis AI Robotics (NYSE: MCRP) (“Micropolis” or the “Company”), a leading UAE-based developer of autonomous mobile robots and AI-enabled systems, today announced a

Yahoo Finance • 1d ago

---

**[Meet the 22 Investors to Know in Robotics and Physical AI](https://www.businessinsider.com/investors-to-know-in-robotics-and-physical-ai-2026-6)**

Investors focus on robotics and physical AI, raising $23 billion this year, as technology evolves from software to real-world applications.

Business Insider • 2d ago

---

**[Me and my exoskeleton: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 2d ago

---

**[Elon Musk and co may relish march of the robots but there must be AI boundaries in the workplace | Heather Stewart](https://www.theguardian.com/business/2026/jun/14/ai-technology-workplace-boundaries-elon-musk)**

As technology advances quickly, firms should not lose sight of what qualities humans bring to jobs

The Guardian • 3d ago

---

**[Robots with real muscles? The breakthrough that blurs the line with life](https://www.futura-sciences.com/en/robots-with-real-muscles-the-breakthrough-that-blurs-the-line-with-life_34099/)**

The Muscle Mystery: Why Flexibility Isn’t (Yet) Robotic Bending, twisting, and bouncing back into shape—nature makes it look effortless. Our own bodies, apart from our bony skeletons, are supple machines designed for flexibility that humanoid robots still struggle to imitate. We’ve all seen spectacular videos of robots waving their arms,...

Futura, le média qui explore le monde • 1d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 16K • 👍 311 • 💬 112 • ⏱️ 8:49 • 4d ago

---

**[First Robot Lawn Mower with a BUILT-IN String Trimmer - WORX Land Vision Cloud](https://www.youtube.com/watch?v=ggxTdCjKBjI)**

The NEW Worx Landroid stands out In a sea of lawn mowing Robots. The only mower that can be setup anywhere in minutes ...

📺 Silver Cymbal

👁️ 30K • 👍 1K • 💬 120 • ⏱️ 10:53 • 2d ago

---

**[The Robot That Solved a Rubik’s Cube in 0.103 Seconds](https://www.youtube.com/watch?v=Fj14TIdu3ug)**

A robot built by Purdue students solved a Rubik's Cube in just 0.103 seconds, setting a world record and showing the incredible ...

📺 Be Yourself.

👁️ 4K • 👍 43 • 💬 1 • ⏱️ 0:16 • 7h ago

---

**[Robot Dog In Traditional Dress Steals Spotlight At Russia-ASEAN Summit Exhibition In Kazan](https://www.youtube.com/watch?v=oK3msv0eDQw)**

A robot dog named Aitidus became the star attraction at the "Made in Tatarstan" exhibition in Kazan during the Russia-ASEAN ...

📺 CRUX

👁️ 2K • 👍 55 • 💬 2 • ⏱️ 0:26 • 8h ago

---

**[Anaconda Innovation! 🐍✨ Jinu Crafts a Robotic Companion for Rumi! #robot](https://www.youtube.com/watch?v=Ppx8Ilti4PY)**

Join Jinu as he takes on an exciting challenge to create a one-of-a-kind robotic anaconda for Rumi! Watch the transformation ...

📺 PopZap Shorts

👁️ 4K • 👍 56 • ⏱️ 0:25 • 2h ago

---

**[Cube transforms into a solar harvesting robot! 🍎🤖 #agritech  #robotics  #cgi #solarfarm](https://www.youtube.com/watch?v=mCUsnKFMTKw)**

Witness the future of smart agriculture!** Watch this metallic cube undergo an incredible mechanical transformation into a ...

📺 🚜🌾 Desi Farm Vibes

👁️ 9K • 👍 47 • ⏱️ 0:21 • 1d ago

---

**[Tiny Medical Robots Navigate Deep Inside the Human Body With Magnetic Precision #robot #medical](https://www.youtube.com/watch?v=MRAJKYqmel4)**

Tiny Medical Robots Navigate Deep Inside the Human Body With Magnetic Precision What if doctors could send microscopic ...

📺 Future Lens Pi

👁️ 35K • 💬 6 • ⏱️ 0:07 • 1d ago

---

**[INNOVATION: CEO highlights expanding robotics applications](https://www.youtube.com/watch?v=QOmB7crTFPo)**

Robostore CEO Teddy Haggerty and Unitree G1 humanoid robot, Koid, join 'Varney & Co.' to discuss its capabilities, cost and ...

📺 Fox Business Clips

👁️ 1K • 👍 39 • 💬 25 • ⏱️ 6:28 • 4h ago

---

**[Robot-as-a-Service: The Business Model That Could Put Humanoids in Every Factory](https://www.youtube.com/watch?v=KgtFHvsD5ck)**

SOURCES Humanoid Official Press Release | Humanoid Secures Landmark Deal with Schaeffler to Deploy Thousands of ...

📺 Jason Lowe on AI

👁️ 18K • 👍 1K • 💬 52 • ⏱️ 2:31 • 3d ago

---

**[Humanoid robot football match showcases advances in embodied AI](https://www.youtube.com/watch?v=fajs4WznfpU)**

As football fever sweeps the globe during the 2026 FIFA World Cup, a 3v3 fully autonomous robot football match took place on ...

📺 CGTN

👁️ 20K • 👍 45 • 💬 5 • ⏱️ 1:15 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

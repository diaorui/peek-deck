---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-06-18T05:17:42.507470+00:00'
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

**Last Updated:** June 18, 2026 at 05:17 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Boston Dynamics Atlas Product Director on Humanoid ROI](https://www.reddit.com/r/robotics/comments/1u8e4xf/boston_dynamics_atlas_product_director_on/)**

Aya Durbin says humanoid robots need to prove real customer value before they can scale. She says the goal for Atlas is not just to be impressive, but to deliver positive ROI for customers. Boston Dynamics is focusing on industrial environments first, especially work that is hard to hire for, physically demanding and difficult to automate with traditional systems. She also says customers need robots that are reliable, useful and able to become a trusted part of the workforce.

13h ago

---

**[3D-printed rovers using pointcloud/depth (DA3) instead of LIDAR](https://www.reddit.com/r/robotics/comments/1u8cjkw/3dprinted_rovers_using_pointclouddepth_da3/)**

Hey everybody! Hobbyist here with an update on my cheap rover swarm project. I've been trying out Depth Anything 3 and wanted to share, because the results of such minimal hardware surprised me. The setup: each rover is just a XIAO ESP32-S3 Sense (~$15 board with a tiny onboard camera) in a 3D printed body. The ESP32 is basically a sender, it streams the camera over WiFi and reports temperature/battery/telemetry. All the heavy lifting (DA3 inference, navigation) runs on a PC that acts as the brain. No lidar, no depth sensor, one cheap RGB camera. DA3 gives me a point cloud per frame and can merge multiple frames into a larger cloud. Seeing a $15 camera produce a usable 3D-ish image of the room is still kind of wild to me. Eventually I want to use it for navigation - a kind of "poor man's lidar". It estimates what's near at three heights (eye level, above, below) to give a rough obstacle sense without a dedicated sensor. Secondly for visualization at the moment, but the goal is to stitch frames into an environment map. Positioning is currently handled by ArUco markers around the room (solvePnP). Still early and held together with hope, but it's been fun pushing this hardware further than it wamts to go. :-)

14h ago

---

**[Hand project posponed to September](https://www.reddit.com/r/robotics/comments/1u8kkjr/hand_project_posponed_to_september/)**

So this is my 2nd project and final project in high school, quite ambitious i gotta say. I was trying to make a anthropomorphic robotic hand . So i grabbed the palm and finger design from here. But i wanted to make my own thingys where the strings are attached , and add adduction ( fingers get clamped together). I learned how to use fusion and how to 3d print , i didnt know what was clearance. I learned that quickly . I dont have a 3d printer at home so i needed to pay for everything , i spent all my budget for this project , and i was so close to finishing everything but , my strings lacked tension and some 3d printed parts broke and i really dont want to spend more money. I finally decided to postpone the project until september because i got in an engineering school and i hope they have a 3d printer i can use freely. On top of that i think its better to try out some new stuff throughout the summer like i want to make those plasma ball thingys with the glass surrounding it and you can touch it. I am a little disappointed cause i was so close but let's see. I left you some pics too ​

9h ago

---

**[Target : autonomous robots for mapping](https://www.reddit.com/r/robotics/comments/1u8mcei/target_autonomous_robots_for_mapping/)**

Hi r/robotics ! I’m currently working on a robotic car project for mapping, and I’d like to share my progress and get some feedback from the community. So far, the main issues I’ve encountered (and resolved) are as follows: - Synchronizing the car’s position on the map (as indicated by the gyroscope) with the position of the digitized image based on the car’s position - Managing the motors’ power supply (complex wiring) However, there are still a few issues for which I could use some advice. - It seems that over time, a discrepancy is developing between the robot’s position on the map and its actual position as measured by the gyroscope. Is this an inaccuracy in the gyroscope that could be corrected through code? - The scanner works but remains fairly inaccurate; any recommendations are welcome - The robot’s path tends to veer off course, so I’m considering adding speed encoders to implement a path correction system (I assume the problem stems from the fact that the speed of each motor isn’t always precise) My goal is to build a fully autonomous car capable of mapping its surroundings (I'll add a webcam). Feel free to share any ideas you might have. my target is build a full self driving car able to mapping his environment ( i will adding webcam). Github : https://github.com/enzocolombat/EC-Hub/

8h ago

---

**[Foundry Humanoid robotics](https://www.reddit.com/r/robotics/comments/1u8fvh8/foundry_humanoid_robotics/)**

There is an ad going around about a humanoid robot to help around the house. Does anyone know about that? ​ It feels scammy mostly because there is a video on their site showing them folding a shirt that is obviously AI. (The shirt doesn't fold correctly) ​ I guess just curious if anyone knows anything about them. ​

🔗 [Foundry](https://foundryhumanoid.com/) • 12h ago

---

**[Sampling-based motion planning, genetic algorithms, and biological evolution might all be running the same underlying search algorithm](https://www.reddit.com/r/robotics/comments/1u8pbqm/samplingbased_motion_planning_genetic_algorithms/)**

I work in robotics, and have for almost a decade now. I keep noticing that a huge chunk of search-under-uncertainty problems, in robotics and outside it, converge on the same two-step architecture: generate variation indiscriminately first, then apply a scoring/selection pressure that keeps what works and discards what doesn't. No model of the problem is required upfront. Most the "intelligence" lives in the selection step, not the generation step. The clearest version of this in our own field is sampling-based motion planning. RRT and its relatives don't try to compute a path analytically. They expand randomly in many directions through the configuration space and then retain/extend the branches that make progress toward the goal, pruning the rest. Genetic algorithms and evolution strategies (CMA-ES, for instance) run an identical loop in parameter space instead of configuration space: generate a population of variants, score them against a fitness (cost) function, keep the survivors, repeat. Simulated annealing is a single-particle version of the same thing, generate a random perturbation, accept or reject it based on a score. Once I started paying attention to this pattern, I noticed it shows up well outside robotics too, in places that have nothing to do with computer science: Slime mold expanding in all directions through a maze of food sources, with the inefficient tendrils pruned back, and famously reconstructing something close to the Tokyo rail network when food sources are placed at the positions of major stations. Evolution itself: random mutation generates variation with zero regard for whether it's useful, and survival does the selecting after the fact. Neural development: neurons and synaptic connections proliferate in directions that aren't pre-planned, and dopamine-linked reinforcement selectively stabilizes the ones that turn out to matter. Once I started looking for more instances, I found two more that fit the same structure almost exactly: The immune system: B-cells mutate antibody variants somewhat randomly (somatic hypermutation) and the ones that bind the pathogen get clonally selected and expanded. Thought/creativity: you can't generate a genuinely novel idea by deduction from evidence that it's correct. The evidence only exists after the idea does. Novelty has to come first; judgment comes second. That last one turns out to have a surprisingly direct precedent. Henri Poincaré, describing how he worked out the theta-fuchsian functions, wrote that ideas rose in crowds and collided in his mind until pairs interlocked into stable combinations, almost like watching his own unconscious work made partially visible to consciousness, and that what got selected from that flood of combinations was governed by something close to an aesthetic sense of mathematical elegance. That's a generate-then-select loop running inside a human mind, described in 1908. The principle has been formalized more than once since then, from different directions: Richard Dawkins' Universal Darwinism: the claim that variation/selection/retention isn't a biology-specific mechanism but a substrate-independent algorithm that biology happens to be one instance of. Donald Campbell's blind variation and selective retention (BVSR), later developed extensively by Dean Keith Simonton, which applies the same two-step structure directly to creative cognition. Karl Popper's conjectures and refutations model of how knowledge grows: blind generation of new theories, followed by selective retention of the ones that survive criticism. Popper explicitly treated this as the same process as biological evolution, just running on ideas instead of organisms. Gerald Edelman's Neural Darwinism (Theory of Neuronal Group Selection), the formal version of the neuron/dopamine point above: synaptic overproduction followed by activity-dependent selective stabilization. Worth flagging here: I'm not claiming the expansion step is ever truly random. In every example above, the variation is guided. Slime mold follows chemoattractant gradients, not isotropic noise. Mutation isn't uniform across a genome, there are hotspots and repair biases. Axon growth follows chemical guidance cues, not random angles. Informed RRT* deliberately biases sampling toward the goal region instead of sampling uniformly. Even Poincaré's account isn't pure randomness, he describes an aesthetic sense that seems to steer which combinations even get generated, not just which ones survive afterward. Liane Gabora has made this exact critique of BVSR, that calling the variation "blind" overstates how random it actually is. But that's the part I find more interesting, not less. The expansion step across all of these systems is intelligently informed, biased toward promising regions by something the system already "knows," and yet it still needs the separate selection/scoring step on top of that guidance to actually converge. Neither half does the job alone: the guidance is too crude or too local to solve the problem outright (that's why expansion is still happening at all instead of direct computation), and the selection pressure has no foresight of its own, it only works because it's filtering output that the guided expansion already biased toward viable territory. Has anyone else found that this specific combination, intelligently biased expansion paired with a separate selection/scoring step, actually performs best in practice? I have personally found, that at least for my applications in autonomous vehicles and motion planning, this combination works the best. Curious whether other people doing sampling-based planning, evolutionary algorithms, or other search methods have found the same thing I have: that this architecture outperforms the alternatives, rather than just being one option among several that works comparably well. I will personally only ever use this type of algorithm after realizing this is how nature does it. Lastly, I am not proposing that analytical algorithms are better or worse than machine learning algorithms. I believe that HOW this is solved is irrespective of the fundamental search algorithm of the universe I have observed. I believe that it is the expand, then score mechanism that is important here, and does not exclude any method of expansion or scoring, as I have observed this in the above stated forms across nature. Thanks for the read if you're here, I've been thinking about this all year and needed to post it somewhere.

6h ago

---

**[Universal Manipulation Exoskeleton (UME): a low-cost exoskeleton with real-time haptic torque feedback](https://www.reddit.com/r/robotics/comments/1u799px/universal_manipulation_exoskeleton_ume_a_lowcost/)**

From Litian Liang on 𝕏 (thread with multiple videos): https://x.com/litian_liang/status/2066541466286215570 This work is done in Inclusion AI lab at Ant Group, advised by James (Jingxi) Xu and Professor Mark Cutkosky from Stanford BDML lab. Website: https://ume-exo.github.io Paper: https://arxiv.org/abs/2606.14218

1d ago

---

**[ICRA'27](https://www.reddit.com/r/robotics/comments/1u844ka/icra27/)**

Hello Everyone, I am preparing my manuscript for upcoming ICRA'27. But They have page limit of 8 pages, including references. As well, They don't accept any supplementary documents. So my question is how can I show more experiments and ablation studies? Because 8 page is not sufficient. Any tips? Much appreciated!!

21h ago

---

**[Resume Review for Automate 2026 / Robotics Software Engineer (Master's Student)](https://www.reddit.com/r/robotics/comments/1u8eia6/resume_review_for_automate_2026_robotics_software/)**

Title: Resume Review for Automate 2026 / Robotics Software Engineer (Master's Student) Hi everyone, I'm attending Automate 2026 in Chicago and would appreciate feedback on my resume. I'm a Master of Science in Computer Science at Bridgewater State University (graduating December 2025). I have 4+ years of software engineering experience and hands-on robotics experience with ROS2, TurtleBot4, SLAM, Nav2, OpenCV, computer vision, and autonomous navigation projects. I'm targeting these roles: Robotics Software Engineer Robotics Engineer Autonomous Systems Engineer Computer Vision Engineer Software Engineer (Robotics) I'd appreciate feedback on: Is my resume strong enough for robotics and automation companies? Are there any red flags? Should I emphasize my robotics projects more than my software engineering experience? Is the resume optimized for career fairs and recruiter screening? What skills or keywords are missing? Thanks in advance for any advice.

13h ago

---

**[Halfwiredtv: we're at 76+ members in 4 days on discord](https://www.reddit.com/r/robotics/comments/1u88n66/halfwiredtv_were_at_76_members_in_4_days_on/)**

HalfwiredTV is a community for people who want to learn robotics, build projects, and collaborate with others. Our long-term goal is simple: Get everyone to a level where they can confidently learn, build and collaborate on robotics projects together in livestreams. What You'll Find Here -- People learning together teaching each other on calls in dedicated channels for topics (created as per demand) Project teammates Livestream collaborations and study sessions (uhm.. with meme songs) , also whenever anyone has something interesting to talk and show regardless of their skill level. We recently had our first livestream on a member's lazer scanning workflow for their robocar Robotics discussions ranging from complete beginners to advanced builders Your skill level doesn't matter. If you're curious, willing to learn, and willing to build, you're in the right place. Come join us : https://discord.com/channels/1514229376152113172/1514973636258172949

16h ago

---

---

## Google News: "robotics"

**[US Robot Industry Returns to Double Digit Growth](https://ifr.org/ifr-press-releases/news/us-robot-industry-returns-to-double-digit-growth)**

The number of industrial robot installations in the United States rose by 11% year-on-year, to reach 38,000 units in 2025. This significant recovery is driven by robust growth in the food industry and other non-manufacturing sectors. However, the automotive industry remains the largest adopter and reached 13,500 units, just 1% below last year's result.

IFR International Federation of Robotics • 10m ago

---

**[New Qwen Models Fuel BABA's Robotics Ambitions: Hold the Stock Now?](https://finance.yahoo.com/technology/ai/articles/qwen-models-fuel-babas-robotics-144700254.html)**

Alibaba's new Qwen-Robot push deepens its AI-cloud strategy, but rising costs, valuation premium and volatility raise questions about near-term upside.

Yahoo Finance • 14h ago

---

**[AI coding agents taught robots how to install GPUs and cut zip ties](https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/)**

Nvidia's self-improvement program for robots enlists teams of AI coding agents.

Ars Technica • 1d ago

---

**[The State of Industrial Robotics](https://www.thefai.org/posts/the-state-of-industrial-robotics)**

The Foundation for American Innovation.

The Foundation for American Innovation • 15h ago

---

**[Built Robotics, Penn xLAB to develop physical AI for construction](https://www.therobotreport.com/xlab-and-built-robotics-partner-to-advance-construction/)**

xLAB and Built Robotics partner to capture additional data, advancing AI models to improve construction site safety.

The Robot Report • 1d ago

---

**[AI robots can go rogue – a researcher on how easily it happens](https://theconversation.com/ai-robots-can-go-rogue-a-researcher-on-how-easily-it-happens-284766)**

In tests, AI robot systems easily rejected directly malicious commands. But their safety filters collapsed when creative writing was used to instruct them.

The Conversation • 2d ago

---

**[Me and my exoskeleton: the rise of wearable robotics](https://www.ft.com/content/a71f4c56-685c-4341-9772-31e4e5c6418d)**

Lighter and more affordable devices give users a battery-powered spring in their step

Financial Times • 2d ago

---

**[Collecting robot training data is dirty, unglamorous work. Some AI labs are already paying XDOF to do it.](https://techcrunch.com/2026/06/17/collecting-robot-training-data-is-dirty-unglamorous-work-some-ai-labs-are-already-paying-xdof-to-do-it/)**

If physical AI is going to match the accomplishments of LLMs, there's a data problem that needs to be solved.

TechCrunch • 14h ago

---

**[How much will robotics play a role in the family dynamic heading into the future?](https://www.nbcnews.com/video/could-future-families-really-benefit-from-a-humanoid-helper-265278021993)**

Taking a page out of the Jetsons, should a robot have a place in your household when it comes to parenting? NBC News' Gadi Schwartz spoke to tech and parenting experts to find out more.

NBC News • 3h ago

---

**[Meet the 22 Investors to Know in Robotics and Physical AI](https://www.businessinsider.com/investors-to-know-in-robotics-and-physical-ai-2026-6)**

Investors focus on robotics and physical AI, raising $23 billion this year, as technology evolves from software to real-world applications.

Business Insider • 2d ago

---

---

## YouTube Videos: "robotics"

**[We let AI buy a robot and a car, it does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI Robot. Could AI become dangerous? Can we trust AI. AGI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 670K • 👍 22K • 💬 2K • ⏱️ 15:10 • 3d ago

---

**[One Company Deployed 1 Million Warehouse Robots — Now Everyone Else Can Buy Them](https://www.youtube.com/watch?v=oxh3TcZXf00)**

Sources CNBC | Amazon unveils latest warehouse robot as tech giants continue AI layoffs ...

📺 Jason Lowe on AI

👁️ 151K • 👍 8K • 💬 852 • ⏱️ 2:57 • 4d ago

---

**[Are we ready for flesh bots? | Big Business](https://www.youtube.com/watch?v=EBO6z839sug)**

Companies like 1X and Unitree are spending millions trying to build robot companions. But why aren't they in our homes yet?

📺 Business Insider

👁️ 101K • 👍 2K • 💬 443 • ⏱️ 17:26 • 3d ago

---

**[Better Than a Robot Arm? Why I Built a Crane Robot to clean my house](https://www.youtube.com/watch?v=vsL1EHt5iBY)**

This video showcases some model successes and failures I've had in building a room-scale cable driven parallel robot to clean ...

📺 Over Engineer

👁️ 59K • 👍 3K • 💬 291 • ⏱️ 6:05 • 5d ago

---

**[China&#39;s &#39;Begging Robot&#39; Goes Viral | అయ్యా  బాబు అంటూ అడుక్కుంటున్న రోబోలు | ZEE Telugu News](https://www.youtube.com/watch?v=oKOAElLSb7I)**

అయ్యా బాబు అంటూ అడుక్కుంటున్న రోబోలు | China's 'Begging Robot' Goes Viral | ZEE Telugu ...

📺 Zee Telugu News

👁️ 22K • 👍 166 • 💬 3 • ⏱️ 0:39 • 1h ago

---

**[China&#39;s Fighting Humanoid Robots Are Getting Scary! (EngineAI T800 vs Unitree H2)](https://www.youtube.com/watch?v=KQBVEFTcop8)**

China's fighting humanoids are getting crazy. Shenzhen's EngineAI just shared footage of its Terminator-inspired T800 humanoid ...

📺 Kalil 4.0

👁️ 16K • 👍 312 • 💬 112 • ⏱️ 8:49 • 4d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=VunUE9PiGOk)**

📺 Robot Julie 

👁️ 13K • 👍 46 • 💬 1 • ⏱️ 0:26 • 1d ago

---

**[From humanoid helpers to factory floors: China&#39;s robotics pushーNHK WORLD-JAPAN NEWS](https://www.youtube.com/watch?v=5rp3aE2f96U)**

Chinese robots are having their moment in the limelight. As their cheaper robotics enter the market, NHK World's Sekiya Satoshi ...

📺 NHK WORLD-JAPAN

👁️ 3K • ⏱️ 7:38 • 20h ago

---

**[Robot nurses begin working at Odessa hospital in Texas](https://www.youtube.com/watch?v=sYJFUYNG-Go)**

A Texas hospital has introduced robot assistants designed to deliver supplies and lab samples, helping nurses spend more time ...

📺 KCENNews

👁️ 81K • 👍 3K • 💬 2K • ⏱️ 2:08 • 6d ago

---

**[Cube transforms into a solar harvesting robot! 🍎🤖 #agritech  #robotics  #cgi #solarfarm](https://www.youtube.com/watch?v=mCUsnKFMTKw)**

Witness the future of smart agriculture!** Watch this metallic cube undergo an incredible mechanical transformation into a ...

📺 🚜🌾 Desi Farm Vibes

👁️ 14K • 👍 73 • ⏱️ 0:21 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

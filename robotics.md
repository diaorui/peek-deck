---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-03-06T18:49:56.010050+00:00'
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

**Last Updated:** March 06, 2026 at 18:49 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Xiaomi Shows Humanoid Robots Working Autonomously on Production Lines with 90.2% Success Rate](https://www.reddit.com/r/robotics/comments/1rmixa6/xiaomi_shows_humanoid_robots_working_autonomously/)**

2h ago

---

**[My robotics arm object grasping project !](https://www.reddit.com/r/robotics/comments/1rmh1vw/my_robotics_arm_object_grasping_project/)**

I have finished my robotics arm object grasping project ! Initially , I want to make a depth camera by myself for loss cost , but it ' s too difficult for me . I have tested several camera , I finded P008G is great for it ' s highly accurate depth data . I did a great job !

3h ago

---

**[4DOF arm to tinker with remote transmission before I scrapped it](https://www.reddit.com/r/robotics/comments/1rmln9x/4dof_arm_to_tinker_with_remote_transmission/)**

Sorry if this isn’t the place to post this since it’s really a hobby project and this feels more like a simple blog post. I just figured I’d share it since I had spent time working on it. I suppose there are 3 main reasons why I scrapped it. I made the mistake of designing from the base upward as opposed to from the end-effector downward which led to a loss in desired elegance of the design itself. I also decided that I want to implement 6DOFs instead of just 4. On top of that, I decided to try my hand at accomplishing remote cable transmission for all DOFs aside from the base rotation. I’ve already finished designing the 6DOF arm, I just haven’t assembled it yet. Anyways, here’s a brief overview of the mechanical design. The base is essentially just a turn-table bearing system with 5 bearings between the top and bottom traces. The shoulder transmission is just direct mounting. Elbow transmission is via bevel gears to keep weight closer to the output shaft of the shoulder joint’s motor. The wrist transmission is via capstan antagonistic cabling. Then I have a lever at the end of the 3rd link after the wrist for my desired end-effector function utilizing capstan antagonistic cable transmission as well. I decided to scrap it before finishing the end-effector though. The new design focuses on complete remote transmission via capstan antagonistic cables in conjunction with Bowden cable sheaths used for the 3DOFs I have decoupled at the wrist joint. Again, sorry if this isn’t the place for this as this is something of a blog post more than anything. But I’m hoping this may intrigue someone. Also, I probably will design a proper shell at some point but I have a mini 3D printer and tbh I like seeing everything move.

32m ago

---

**[HexGrip V1.0: Designing a 3-DOF Omni-Wrist. From "Block of Plastic" to "Fluid Motion"](https://www.reddit.com/r/robotics/comments/1rm93wd/hexgrip_v10_designing_a_3dof_omniwrist_from_block/)**

Update on my 6-DOF desktop arm project: I’ve officially moved into the mechanical prototyping phase, starting with the most complex hurdle—the Wrist. The goal was to pack 3 degrees of freedom into a compact volume while keeping everything 3D printable. I modeled an Omni-Wrist mechanism in OnShape with “perfect” dimensions, using a series of butt-hinge linkages with 3D-printed pins. On-screen, the digital assembly worked flawlessly, but reality hit hard. The Fail: My first print had zero play. While "zero-clearance" sounds great in CAD, filament expansion turned the whole assembly into a static paperweight. The tolerances were too tight, the hinges seized, and the pins were impossible to seat without snapping the linkages. The Pivot: I went back to the "Model-Print-Iterate" cycle. I increased the clearances to 0.2mm and redesigned the pivot points as snap-fit pins. This allows the linkages to stay secure under pressure while maintaining enough "fluidity" for manual movement. The Query: For those who build small-scale linkages: Pin Durability: Do 3D-printed pins actually hold up under the repetitive stress of a 6-DOF arm, or is it a fool's errand? Should I move to metal dowel pins now before I build the rest of the arm? Hinge Alternatives: Given the friction issues with 3D-printed butt hinges, is there a more efficient hinge style or linkage structure you'd recommend for a 3-DOF wrist that is easier to assemble and maintain?

9h ago

---

**[What’s the point of making robots human-shaped?](https://www.reddit.com/r/robotics/comments/1rma1gq/whats_the_point_of_making_robots_humanshaped/)**

From an engineering perspective, wouldn’t other designs—like cantilever-type or hemispherical robots—be more practical and efficient for most real-world applications? Human-shaped robots seem mechanically complex, expensive, and often less stable compared to simpler structures. So is the humanoid form mainly for environments designed for humans, or is it more about research, marketing, and public perception?

8h ago

---

**[I’ve open-sourced my robots!](https://www.reddit.com/r/robotics/comments/1rll5z2/ive_opensourced_my_robots/)**

1d ago

---

**[Wife said I wasted money...Narwal just proved her wrong](https://www.reddit.com/r/robotics/comments/1rmkmah/wife_said_i_wasted_moneynarwal_just_proved_her/)**

I've had multiple iRobots and they were total junk...There is ALWAYS an error...my wife was like "you wasted money again"😭 Now Im in love with my narwal (freo z10 ultra). It does occasionally bump some chair legs when trying to sneak through, but most of the time it cruises through like a pro. The best part is, the robovac has riser side brushed on both sides, so it can easily get into the gaps around cabinet and table legs, no more bending over to check for leftover sauce. It saves much time and energy. And I think roller mop does not get cleaned as well as a double rotating mops in the base. 🙌 So my wife went from "you wasted money again" to "okay, this thing is actually awesome." Feels good to be right for once.

1h ago

---

**[I got frustrated missing robotics deployments and layoffs, so I wrote a flightradar24-style autonomous NLP scraper to track the industry globally](https://www.reddit.com/r/robotics/comments/1rmdrlj/i_got_frustrated_missing_robotics_deployments_and/)**

As someone who follows the robotics industry closely, tracking company-level signals manually was impossible. I started building this as a personal tool and eventually put it online. How the engine works: A Python scraper hits multiple major robotics/AV newswires every 30 minutes via a systemd timer. Each headline is deduplicated and run through an NLP classification layer that categorises signals into four types: Deployments, Financials, Layoffs, and Leadership changes. roboradar24

5h ago

---

**[Bimo can walk on a carpet now!](https://www.reddit.com/r/robotics/comments/1rlkvpj/bimo_can_walk_on_a_carpet_now/)**

For those following the project, this is Bimo walking on a regular carpet, something that used to be very unreliable without hand-tuning the environment or the RL model. Over the last months I’ve retrained and tweaked the walking model so it’s much more robust: it now keeps a stable heading instead of drifting or turning, and it tolerates uneven contact and small disturbances much better than before. Next on the roadmap are behaviors such as: turning gaits, better recovery under sustained pushes, and more pre-programmed motions to make Bimo a practical research and tinkering platform rather than just a locomotion demo. As these stabilize, I’ll be adding them to the open-source GitHub repo and documenting them in the Discord so others can build on top of this. If you want to see the full kit and platform details, there’s also a page on the Mekion site with specs and pre-order info.

1d ago

---

**[China Humanoid Robotics Industry Landscape: 140 companies. 13,000 robots. One question nobody is asking.](https://www.reddit.com/r/robotics/comments/1rmlhit/china_humanoid_robotics_industry_landscape_140/)**

I’ve just put together a table for an upcoming deep-dive. https://preview.redd.it/ueeg5w80ugng1.png?width=1400&format=png&auto=webp&s=d574471470abd0e66dca082a0d00b9fe4a7e0bb0 This is a map of who is actually building China’s humanoid robot industry, what their machines are doing in the real world, and which of the 140 companies might still exist in five years. The framework: a deployment reality matrix that sorts every major player by where they came from and how far they have gotten from the demo stage to productive work.

38m ago

---

---

## Google News: "robotics"

**[Amazon cuts jobs in robotics unit as layoffs continue: report](https://www.foxbusiness.com/technology/amazon-cuts-jobs-robotics-unit-layoffs-continue)**

Amazon cut at least 100 positions in its robotics unit, continuing a sweeping corporate downsizing tied to artificial intelligence efficiencies and cost controls.

Fox Business • 1d ago

---

**[Amazon cuts jobs in strategically important robotics division](https://www.businessinsider.com/amazon-robotics-division-job-cuts-2026-3)**

Amazon's e-commerce operations rely on thousands of robots to automate warehouse operations. Still, this division hasn't avoided job cuts.

Business Insider • 1d ago

---

**[Amazon Quietly Abandoned Its Robot Innovation](https://www.bgr.com/2112422/amazon-abandons-warehouse-robot-blue-jay/)**

Amazon recently abandoned an innovative robotic line that it had deployed last year in an effort to streamline some of its warehouse operations.

bgr.com • 20h ago

---

**[E-bike starts fire at Yale University's robotics lab on Hillhouse Avenue, New Haven official says](https://www.nhregister.com/news/article/new-haven-hillhouse-ave-yale-lab-e-bike-fire-21957068.php)**

New Haven Register • 1d ago

---

**[Why Top-Tier Robotic Surgery Name Globus Medical Is Getting 'Aggressive' In 2026](https://www.investors.com/research/the-new-america/globus-medical-stock-spine-implants-robotic-surgery/)**

Investor's Business Daily • 5h ago

---

**[Biodegradable yet hyperdurable robotic fingers for zero-waste soft electronics](https://www.nature.com/articles/s41893-026-01780-4)**

As soft electronic waste becomes an urgent concern, biodegradable yet high-performance devices are emerging as a promising solution. Here the authors fabricate durable and multifunctional soft robotic fingers in which both polymers and inorganic electronics are fully compostable.

Nature • 1d ago

---

**[Prediction: AI Robotics Will Be a $375 Billion Industry. This Stock Is Positioned to Win in 2026.](https://www.fool.com/investing/2026/03/05/prediction-ai-robotics-will-be-a-375-billion-indus/)**

When all is said and done, practicality trumps technological "wow!"

The Motley Fool • 15h ago

---

**[Graphene-based 'artificial skin' brings human-like touch closer to robots](https://techxplore.com/news/2026-03-graphene-based-artificial-skin-human.html)**

Tech Xplore • 1d ago

---

**[Studying snakes' ability to stand upright could inform soft robotics and more](https://phys.org/news/2026-03-snakes-ability-upright-soft-robotics.html)**

Phys.org • 3d ago

---

**[Xiaomi trials humanoid robots in its EV factory — says they're like 'interns'](https://www.cnbc.com/2026/03/04/xiaomi-humanoid-robots-ev-factory-.html)**

Two humanoid robots can complete 90% of the work in three hours, Xiaomi President Lu Weibing told CNBC.

CNBC • 2d ago

---

---

## YouTube Videos: "robotics"

**[Unrestricted AI in a robot does exactly what experts warned](https://www.youtube.com/watch?v=SbEqMkxEzvA)**

AI robot. ChatGPT in Robot. Could AI become dangerous? Can we trust AI? Get your $5 sign-up bonus at ...

📺 InsideAI

👁️ 354K • 👍 25K • 💬 3K • ⏱️ 16:54 • 3d ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=7I-KWkV0JUM)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN

👁️ 15K • 👍 337 • 💬 29 • ⏱️ 29:41 • 18h ago

---

**[Shocking Light-Powered Robot Runs Without Batteries &amp; Cyborg Cockroach](https://www.youtube.com/watch?v=2_igeW1d8RA)**

Robotics just entered a very strange new phase. Scientists built a tiny robot that runs purely on light with no batteries, processors, ...

📺 AI Revolution

👁️ 17K • 👍 691 • 💬 49 • ⏱️ 14:35 • 1d ago

---

**[This Robot &amp; Elon Musk Dance Broke the Internet 🕺🔥#ElonMusk #Tesla #Optimus #TeslaBot #Robotics](https://www.youtube.com/watch?v=EnduYx4nguI)**

A moment like this perfectly captures how technology can be both revolutionary and entertaining at the same time. Watching Elon ...

📺 Billionaire Shots

👁️ 34K • 👍 2K • 💬 245 • ⏱️ 0:13 • 2d ago

---

**[Rise of the Humanoids: Inside China’s Robot Awakening](https://www.youtube.com/watch?v=sFFMMg2XWyQ)**

China's humanoid robot revolution is no longer science fiction – it's happening now. From Shenzhen's first 6S robot store and ...

📺 CGTN Europe

👁️ 292K • 👍 462 • 💬 7 • ⏱️ 29:40 • 2d ago

---

**[Robot Vacuum Running! Custom Edition #2](https://www.youtube.com/watch?v=Wn95m5QT6F0)**

📺 Planet Roomba

👁️ 2K • 💬 1 • ⏱️ 21:32 • 5h ago

---

**[Joe Rogan Is Worried About Robot Eyes](https://www.youtube.com/watch?v=Sqv1fuF9r0w)**

📺 DATARK

👁️ 30K • 👍 413 • 💬 4 • ⏱️ 0:25 • 1d ago

---

**[robot girl link in bio #xdollhub#realdoll#siliconedoll#realisitcdoll#dolls](https://www.youtube.com/watch?v=yjz_m8MmYDw)**

📺 XDollHub

👁️ 694K • 👍 3K • 💬 7 • ⏱️ 0:11 • 3d ago

---

**[Quickest Intake in DECODE? | 3565 Ghost Robotics | FTC Snapshot](https://www.youtube.com/watch?v=ex9anz-_BCs)**

Currently ranked 10th in the world, 3565 Ghost Robotics showcases one of the fastest compliant intakes in FTC DECODE.

📺 FUN Robotics Network

👁️ 5K • 👍 93 • 💬 1 • ⏱️ 1:11 • 2d ago

---

**[Unitree vs Tesla vs Boston dynamics #HumanoidRobot](https://www.youtube.com/watch?v=5PvK7No58SM)**

The global humanoid race just shifted. Tesla and Boston Dynamics are still leading in advanced AI and autonomy. But Unitree ...

📺 By 2050

👁️ 42K • 👍 638 • 💬 41 • ⏱️ 0:56 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-23T23:45:57.306436+00:00'
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

**Last Updated:** August 23, 2026 at 23:45 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Humanoid Robot Update](https://www.reddit.com/r/robotics/comments/1vw7let/humanoid_robot_update/)**

I have now finished wiring the legs mostly, i still have to connect the power cables. Once that is done i’m gonna need to test if everything is connected and works properly, then the physical body will be fully finished. Next step will be trying to see if i can make it walk. For anyone interested here’s some of Astrix’s specs: -Weight ~15kg -Height 1.65m -DOF’s 23 and besides 7 canceled dof’s -Has a camera, speaker and later i will add a microphone -The body is fully designed and 3d printed -Runs on a raspberry pi 4 -Fingers and the neck use servos, the rest of the joints use linear actuators This project starter a little while after i got my first 3d printer and it was a interesting idea to try out.

10h ago

---

**[Long Jump Final at the 2026 World Humanoid Robot Games](https://www.reddit.com/r/robotics/comments/1vwkdu0/long_jump_final_at_the_2026_world_humanoid_robot/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [m.youtube.com](https://m.youtube.com/watch?v=p0ONR6lnlxw&pp=ygUvMjAyNiB3b3JsZCBodW1hbm9pZCBsb25nIGp1bXAgZmluYWwgaGlnaGxpZ2h0cyA%3D) • 1h ago

---

**[Construyendo robot hidráulico con válvulas pepepako y sensor de posición casero](https://www.reddit.com/r/robotics/comments/1vwaea6/construyendo_robot_hidráulico_con_válvulas/)**

8h ago

---

**[From AlphaGo to AstraTennis: The World’s First Autonomous Humanoid Robot Tennis Match | GALBOT](https://www.reddit.com/r/robotics/comments/1vwe48b/from_alphago_to_astratennis_the_worlds_first/)**

Very soon, it may even teach me how to play tennis :) Does it run all inference at the edge, or does it rely on the cloud?

🔗 [youtube.com](https://youtube.com/watch?v=bcVNBn5R_rY) • 5h ago

---

**[3-month update, in a little story about my 3D-printed robot lamp](https://www.reddit.com/r/robotics/comments/1vvci99/3month_update_in_a_little_story_about_my/)**

A little update after about three months of working on this project. One of the more visible changes is the hardware itself. I redesigned the lamp and made a fully 3D-printed enclosure for it, so it finally looks a lot closer to what I originally had in mind rather than a prototype with exposed hardware. Probably the biggest change, though, has been the animation. I've spent a lot of time trying to make the lamp move more like an animatronic character rather than just a robot executing trajectories. At this point the mechanics aren't really the main limitation anymore. I can animate pretty much all of its movements in Watti Studio, my animation editor, so now the limiting factor is mostly how well I can actually animate it :) I moved the whole system to ROS 2 and added computer vision. The lamp streams RGB and depth from its camera, and the current point cloud can be displayed directly in the 3D view in Watti Studio. It makes it possible to see the lamp together with its surroundings while creating animations. I added lighting to the animation editor too, so the lamp's light can be keyframed together with its movements. I also spent quite a bit of time on things that aren't as fun to show in videos, especially safety. The software monitors the real movement while an animation is playing. If a joint deviates too far from the expected trajectory or something else goes wrong, the animation stops and the motors hold their current positions. The lamp also has its own REST API, so its functions can be controlled externally without being tied to the animation editor. Next I want to focus mostly on autonomous behavior and interaction with people and the environment. I'm also experimenting with reinforcement learning to teach it to jump, with the longer-term goal of getting it to actually move around on its own. There's still a lot to do, but after three months it finally feels like I have most of the basic pieces in place. I thought about making another technical demo to show the progress, but that sounded a bit boring, so I made a little story with the lamp instead :) For anyone interested in the technical side, I have a pre-release repo with more details about the hardware, software architecture and current progress: https://github.com/Nikolay-Tyulkin/Watti

1d ago

---

**[Is this the future? LOL](https://www.reddit.com/r/robotics/comments/1vvqos3/is_this_the_future_lol/)**

It’s always them goofy robots dancing and doing these goofy stuff. Look at how think those legs are. I don’t think I get how people are scared of its potential to take over the world 😭🙏🏻 It’s just so unrealistic. I just hope that they somehow manage to modify these and turn them into actual useful machines.

1d ago

---

**[One person puppeteering two 4-servo quadruped robots at once via real-time pose tracking](https://www.reddit.com/r/robotics/comments/1vwl7ds/one_person_puppeteering_two_4servo_quadruped/)**

One person, one webcam, two open source OpenCat-based quadruped robots — Quaddle Scout and Buddy, both driven live via real-time human pose tracking. Every limb movement maps directly onto the robots' joints, no AI policy running on its own. OpenCat creator RZ Li tried teaching Quaddle a few moves here — a little awkward at first, but it only takes a few minutes before Quaddle starts picking them up. It's also just as fun as playing Wii Play: Motion — this kind of hands-on teleoperation experiment isn't locked to a research lab, it's something almost anyone can go try themselves. In theory, the same captured human movement data could later be used to teach an AI more human movements — either directly, via imitation learning, or as a starting point that reinforcement learning then refines further — to expand what Quaddle can do. Not what's happening in this clip, just a potential direction. What's your experience with the latency/smoothness tradeoff in a real-time teleoperation setup like this — webcam pose estimation vs. something like a motion-capture rig or joystick? And separately, just for fun — if you had one of these on your desk, what move would you want to teach Quaddle first?

🔗 [YouTube](https://www.youtube.com/shorts/697Le5XYISc) • 1h ago

---

**[Reverse on BLDC controller](https://www.reddit.com/r/robotics/comments/1vweih9/reverse_on_bldc_controller/)**

I bought cheap Kontio motors Kruiser and goal is to use parts for a robot. Problem is that there is no wiring for reverse from factory. Chat GPT suggested that controller could have IO for reverse that is not wired. Has anyone played with this kind of controller before and managed to get reverse working?

5h ago

---

**[Action Space hackathon](https://www.reddit.com/r/robotics/comments/1vw7ui3/action_space_hackathon/)**

Hello everyone, You have all probably noticed that there is a lot happening right now in the Robotics. But for some reason getting your hands on hardware if you don’t have a 3d printer and a few extra Benjamin’s in the bank is super difficult. In light of that, I want to announce that in Boston, Action space Hackathon is going to be a space where for 48 hours people are going to be taught and fly drones autonomously! Free to participate and a prize $1000 if you win! Event is happening OCT 24-25th. For more information, you can click the link on luma! This is a huge labor of love between me and my two college friends. We want to make sure we get more people access and hopefully get some engineering minded people thinking about what’s possible with hardware. (sorry if this goes against the advertising rule)

🔗 [luma.com](https://luma.com/xl77cp4v) • 9h ago

---

**[Honor lightning vs tiangong in the 2026 humanoid robotics 100 meter dash](https://www.reddit.com/r/robotics/comments/1vve7ju/honor_lightning_vs_tiangong_in_the_2026_humanoid/)**

Already faster than the human world record! Insane. Last year every robot was still being remote controlled. The way both robots collided with the padding at the end was quite funny

1d ago

---

---

## Google News: "robotics"

**[Robots can outrun humans, but can they plug in a cable?](https://www.reuters.com/world/asia-pacific/robots-can-outrun-humans-can-they-plug-cable-2026-08-23/)**

Reuters • 18h ago

---

**[Government can bring robotics to life](https://www.ft.com/content/a4147c6b-5634-4035-b1a8-ac7bf1eb497d?syn-25a6b1a6=1)**

Without policy, there are few incentives to automate business functions where labour costs are low

Financial Times • 12h ago

---

**[Robot boxing, football and sprinting at World Humanoid Games](https://www.bbc.com/news/videos/c7vgvj6e1emo)**

The second-edition of the five-day competition kicked off in Beijing, China, on Saturday.

BBC • 10h ago

---

**[China will struggle to make money from humanoid robots](https://www.economist.com/business/2026/08/23/china-will-struggle-to-make-money-from-humanoid-robots)**

The Economist • 9h ago

---

**[The technology that could bring robot mowers to one in two American lawns](https://www.therobotreport.com/technology-could-bring-robot-mowers-one-half-american-lawns/)**

Improvements in AI, satellite navigation, and machine vision are helping robotic lawn mowers spread in the U.S., writes Sunseeker's founder.

The Robot Report • 1d ago

---

**[AI robotics companies love San Francisco. They’re just too big to stay](https://sfstandard.com/2026/08/23/ai-robotics-san-francisco-bright-machines/)**

The city is still ground zero for the industry boom. But as machine companies scale up, they can’t find the space to match.

The San Francisco Standard • 10h ago

---

**[Humanoid robots surpass human records in 100m, high jump](https://www.espn.com/olympics/story/_/id/49692320/humanoid-robots-surpass-human-records-100m-high-jump)**

ESPN • 1d ago

---

**[Chinese robots tackle tennis, smash race records at World Humanoid Robot Games](https://www.scmp.com/tech/tech-trends/article/3364977/chinese-robots-tackle-tennis-smash-track-records-world-humanoid-robot-games)**

South China Morning Post • 12h ago

---

**[Over 2,000 humanoid robots compete for gold on 2nd day of Beijing’s Robot Games](https://apnews.com/video/over-2000-humanoid-robots-compete-for-gold-on-2nd-day-of-beijings-robot-games-c6b7156df52146ad99a1e9ddb727692d)**

For the more than 2,000 robots competing at a major competition in Beijing, winning a gold medal may not be the ultimate goal.

AP News • 9h ago

---

**[ACE Robotics chairman says robot brains will have 'ChatGPT moment' by end of 2027](https://finance.yahoo.com/technology/ai/articles/ace-robotics-ceo-says-robot-100324175.html)**

Humanoid robot brains could see a breakthrough by late next year similar to the dramatic impact ChatGPT had on AI usage, the ‌chairman of Chinese embodied AI startup ACE Robotics said on Friday.  "We expect to reach the 'ChatGPT moment' for embodied intelligence by the end ‌of next year, driven by world models and environmental data capture," Wang Xiaogang told Reuters.  "Even if we reach that inflection point by late 2027, it will likely take another four to ​five years to see broad commercial implementation of embodied world models across sectors," said Wang, who is also a co-founder of Chinese AI visual recognition pioneer SenseTime.

Yahoo Finance • 2d ago

---

---

## YouTube Videos: "robotics"

**[Humanoid Robots Play LIVE Autonomous Tennis Match!](https://www.youtube.com/watch?v=dEOFpgElJKM)**

Humanoid robots are getting ready to compete on the tennis court. GALBOT is preparing its autonomous tennis robots to track ...

📺 DPCcars

👁️ 12K • 👍 32 • 💬 5 • ⏱️ 0:28 • 2d ago

---

**[They Built a Mechanical Mouth That Can Talk 😳 | #Robotics, #Innovation, #FutureTech, AI, #TechTok](https://www.youtube.com/watch?v=0qu0rSrcnVE)**

This uncanny artificial mouth can surprisingly reproduce the sound and articulation of a real human voice. This Synthetic Vocal ...

📺 Ace Atlantis

👁️ 254K • 👍 1K • 💬 119 • ⏱️ 0:05 • 2d ago

---

**[Galbot ET1 Shows the Future of Humanoid Robots](https://www.youtube.com/watch?v=YJSw0Jf8DZ0)**

Galbot ET1 Galaxy Star is a humanoid robot designed to watch human movements, learn them in real time, and reproduce what it ...

📺 DPCcars

👁️ 20K • 👍 416 • 💬 77 • ⏱️ 2:12 • 3d ago

---

**[The first ever humanoid robot Olympics begin this week](https://www.youtube.com/watch?v=OnIUM0HbzDM)**

Subscribe for more!

📺 Aaron Parnas

👁️ 133K • 👍 9K • 💬 1K • ⏱️ 0:45 • 3d ago

---

**[This Robot Can Transform Into Three Machines](https://www.youtube.com/watch?v=NyokyLzKejo)**

TRON 2 transforms into three different robot modes. It can roll, walk, use arms, and carry 30 kilograms. One machine could ...

📺 Manav

👁️ 835 • 👍 51 • 💬 1 • ⏱️ 0:35 • 4h ago

---

**[Why True Robot Intelligence Starts at Home, Not Factories 🤖🏠](https://www.youtube.com/watch?v=YGR2Qp3UoHs)**

Most robotics companies rush to factories, but true artificial general intelligence requires the ultimate edge case: the unstructured ...

📺 Turn the Lens with Jeff Frick

👁️ 1K • 👍 8 • 💬 2 • ⏱️ 0:47 • 4h ago

---

**[Humanoid robots compete on day one of World Robot Games](https://www.youtube.com/watch?v=AerpY_g67m8)**

Humanoid robots competed in various events on day one of the World Robot Games, with one even breaking Usain Bolt's world ...

📺 ABC News

👁️ 62K • 👍 488 • 💬 110 • ⏱️ 0:40 • 1d ago

---

**[This Robot Turns Walls Into Roads 🤖 #robotics #technology #innovation #tech](https://www.youtube.com/watch?v=N2lAMtEY0HM)**

Engineers Built A Robot That Refuses To Treat Walls As Obstacles Most ground robots have one major limitation: when the floor ...

📺 EcoZora

👁️ 82K • 👍 549 • 💬 10 • ⏱️ 0:07 • 1d ago

---

**[Robotic chess](https://www.youtube.com/watch?v=2h4FA6l5TPs)**

I've always loved chess, and when you add a little technology and robotics to it… I'm sold. So here we go with Chessnut Move ...

📺 Moonshotkidz 

👁️ 1K • 👍 14 • ⏱️ 0:35 • 9h ago

---

**[Humanoid robot beats Usain Bolt&#39;s 100-meter record](https://www.youtube.com/watch?v=waKuzQMdVu8)**

Humanoid robot beats Usain Bolt's 100-meter record.

📺 NBC News

👁️ 25K • 👍 187 • 💬 45 • ⏱️ 0:18 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

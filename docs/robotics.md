---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-23T18:59:32.517327+00:00'
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

**Last Updated:** August 23, 2026 at 18:59 UTC  
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

5h ago

---

**[Construyendo robot hidráulico con válvulas pepepako y sensor de posición casero](https://www.reddit.com/r/robotics/comments/1vwaea6/construyendo_robot_hidráulico_con_válvulas/)**

3h ago

---

**[3-month update, in a little story about my 3D-printed robot lamp](https://www.reddit.com/r/robotics/comments/1vvci99/3month_update_in_a_little_story_about_my/)**

A little update after about three months of working on this project. One of the more visible changes is the hardware itself. I redesigned the lamp and made a fully 3D-printed enclosure for it, so it finally looks a lot closer to what I originally had in mind rather than a prototype with exposed hardware. Probably the biggest change, though, has been the animation. I've spent a lot of time trying to make the lamp move more like an animatronic character rather than just a robot executing trajectories. At this point the mechanics aren't really the main limitation anymore. I can animate pretty much all of its movements in Watti Studio, my animation editor, so now the limiting factor is mostly how well I can actually animate it :) I moved the whole system to ROS 2 and added computer vision. The lamp streams RGB and depth from its camera, and the current point cloud can be displayed directly in the 3D view in Watti Studio. It makes it possible to see the lamp together with its surroundings while creating animations. I added lighting to the animation editor too, so the lamp's light can be keyframed together with its movements. I also spent quite a bit of time on things that aren't as fun to show in videos, especially safety. The software monitors the real movement while an animation is playing. If a joint deviates too far from the expected trajectory or something else goes wrong, the animation stops and the motors hold their current positions. The lamp also has its own REST API, so its functions can be controlled externally without being tied to the animation editor. Next I want to focus mostly on autonomous behavior and interaction with people and the environment. I'm also experimenting with reinforcement learning to teach it to jump, with the longer-term goal of getting it to actually move around on its own. There's still a lot to do, but after three months it finally feels like I have most of the basic pieces in place. I thought about making another technical demo to show the progress, but that sounded a bit boring, so I made a little story with the lamp instead :) For anyone interested in the technical side, I have a pre-release repo with more details about the hardware, software architecture and current progress: https://github.com/Nikolay-Tyulkin/Watti

1d ago

---

**[Is this the future? LOL](https://www.reddit.com/r/robotics/comments/1vvqos3/is_this_the_future_lol/)**

It’s always them goofy robots dancing and doing these goofy stuff. Look at how think those legs are. I don’t think I get how people are scared of its potential to take over the world 😭🙏🏻 It’s just so unrealistic. I just hope that they somehow manage to modify these and turn them into actual useful machines.

19h ago

---

**[Action Space hackathon](https://www.reddit.com/r/robotics/comments/1vw7ui3/action_space_hackathon/)**

Hello everyone, You have all probably noticed that there is a lot happening right now in the Robotics. But for some reason getting your hands on hardware if you don’t have a 3d printer and a few extra Benjamin’s in the bank is super difficult. In light of that, I want to announce that in Boston, Action space Hackathon is going to be a space where for 48 hours people are going to be taught and fly drones autonomously! Free to participate and a prize $1000 if you win! Event is happening OCT 24-25th. For more information, you can click the link on luma! This is a huge labor of love between me and my two college friends. We want to make sure we get more people access and hopefully get some engineering minded people thinking about what’s possible with hardware. (sorry if this goes against the advertising rule)

🔗 [luma.com](https://luma.com/xl77cp4v) • 5h ago

---

**[Honor lightning vs tiangong in the 2026 humanoid robotics 100 meter dash](https://www.reddit.com/r/robotics/comments/1vve7ju/honor_lightning_vs_tiangong_in_the_2026_humanoid/)**

Already faster than the human world record! Insane. Last year every robot was still being remote controlled. The way both robots collided with the padding at the end was quite funny

1d ago

---

**[Chinese robot beats Usain Bolt's 100m world record at Beijing games](https://www.reddit.com/r/robotics/comments/1vvu4xs/chinese_robot_beats_usain_bolts_100m_world_record/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=FGBLzMESBAo) • 17h ago

---

**[ask for dataset😭](https://www.reddit.com/r/robotics/comments/1vw4v5h/ask_for_dataset/)**

Is there any dataset for human detection with OBB annotations? I'm doing my program with yolo and it's about human detection with obb and i'm a beginner. But i can't find dataset to train. Can only find human&hbb, and all those obb ones i saw are for vehicles or sth like that. So does anyone know about this? And also, i found a HIT-UAV dataset, but it's thermal dataset.Though i thought about using this and just do a thermal one and saw the rotation part. But no matter how i tried to fix, it's still not obb dataset and error everytime...

7h ago

---

**[Rethinking the Quadruped](https://www.reddit.com/r/robotics/comments/1vvdroy/rethinking_the_quadruped/)**

1d ago

---

**[P.A.R. (Pixel Art Robot) — A Giant, Slow, Flip-Squisk Display, Flipped by a CNC](https://www.reddit.com/r/robotics/comments/1vvyaxs/par_pixel_art_robot_a_giant_slow_flipsquisk/)**

P.A.R. is a machine draws pixel art in the real world. What it displays on the 37x18 grid of squisks is the art that random people on the internet upload on https://par.zimmzimm.com/ . I've been working on P.A.R. for almost 6 months at this point, and it's finally done (except for the custom PCB: in progress). It's a large grid of 3D-printed "squisks" (square discs), which are flipped from the back by the robot, a large CNC machine with a special toolhead. I designed all of this in OnShape and used the Flashforge Adventurer 5M to print most of the parts. The rest of the parts were made to be as cheap as possible: for example, the frame is made of EMT (Electrical Conduit) pipe, which is $0.60/ft. Learn more here. When someone submits a piece, it's added to a queue, and they can add your email to be notified when that piece is completed (absolutely NO SPAM), and they'll get to see a video of the real, physical robot drawing your art one flip at a time.

13h ago

---

---

## Google News: "robotics"

**[Robots can outrun humans, but can they plug in a cable?](https://www.reuters.com/world/asia-pacific/robots-can-outrun-humans-can-they-plug-cable-2026-08-23/)**

Reuters • 14h ago

---

**[Government can bring robotics to life](https://www.ft.com/content/a4147c6b-5634-4035-b1a8-ac7bf1eb497d?syn-25a6b1a6=1)**

Without policy, there are few incentives to automate business functions where labour costs are low

Financial Times • 7h ago

---

**[Robots smash human track records, including Bolt's 100m sprint — video](https://www.theguardian.com/world/video/2026/aug/23/humanoid-robot-smash-human-records-including-usain-bolts-100m-video)**

Humanoid robots have smashed human athletic records at the five-day World Humanoid Robot Games in Beijing. Among the records broken was Usain Bolt's 9.58-second 100m, with a robot developed by the Beijing Innovation Centre of Humanoid Robotics finishing the sprint in 9.39 seconds. Now in its second year, more than 2,000 humanoid robots are participating in the games that are intended to showcase China's rapid progress in advanced robotics

The Guardian • 3h ago

---

**[Chinese humanoid robot beats Bolt's 100-metre world record time](https://www.euronews.com/2026/08/23/chinese-humanoid-robot-beats-bolts-100-metre-world-record-time)**

"In 1 year alone the robots competing have become twice as fast. This highlights the pace of advancement both in the market, and specifically in Chinese robotics," organisers of the World Humanoid Robot Games said.

Euronews.com • 9h ago

---

**[Robots Smash Human Records at Beijing Competition](https://www.newser.com/story/395125/robots-smash-human-records-at-beijing-competition.html)**

High-tech competitors take the field in synchronized display

Newser • 21h ago

---

**[Robot horse and rider steal the spotlight at Chinese conference](https://www.bbc.com/news/videos/c0qvqzzdd02o)**

More than 300 companies are showcasing the latest advances in robotics at the five-day event in Beijing, China, organisers say.

BBC • 1d ago

---

**[China is training up thousands of humanoid robots](https://www.economist.com/business/2026/08/23/china-is-training-up-thousands-of-humanoid-robots)**

The Economist • 5h ago

---

**[The technology that could bring robot mowers to one in two American lawns](https://www.therobotreport.com/technology-could-bring-robot-mowers-one-half-american-lawns/)**

Improvements in AI, satellite navigation, and machine vision are helping robotic lawn mowers spread in the U.S., writes Sunseeker's founder.

The Robot Report • 1d ago

---

**[AI robotics companies love San Francisco. They’re just too big to stay](https://sfstandard.com/2026/08/23/ai-robotics-san-francisco-bright-machines/)**

The city is still ground zero for the industry boom. But as machine companies scale up, they can’t find the space to match.

The San Francisco Standard • 5h ago

---

**[Robot boxing, football and sprinting at World Humanoid Games](https://www.bbc.co.uk/news/videos/c7vgvj6e1emo)**

The second-edition of the five-day competition kicked off in Beijing, China, on Saturday.

BBC • 5h ago

---

---

## YouTube Videos: "robotics"

**[Galbot ET1 Shows the Future of Humanoid Robots](https://www.youtube.com/watch?v=YJSw0Jf8DZ0)**

Galbot ET1 Galaxy Star is a humanoid robot designed to watch human movements, learn them in real time, and reproduce what it ...

📺 DPCcars

👁️ 20K • 👍 411 • 💬 75 • ⏱️ 2:12 • 3d ago

---

**[Humanoid Robot Demolishes Usain Bolt’s Record #shorts](https://www.youtube.com/watch?v=A1vAQ20dyz4)**

China's Beijing Innovation Centre of Humanoid Robotics developed a robot that can run faster than Olympian Usain Bolt.

📺 New York Post

👁️ 21K • 👍 723 • 💬 179 • ⏱️ 0:52 • 18h ago

---

**[Humanoid Robots Play LIVE Autonomous Tennis Match!](https://www.youtube.com/watch?v=dEOFpgElJKM)**

Humanoid robots are getting ready to compete on the tennis court. GALBOT is preparing its autonomous tennis robots to track ...

📺 DPCcars

👁️ 12K • 👍 32 • 💬 4 • ⏱️ 0:28 • 2d ago

---

**[They Built a Mechanical Mouth That Can Talk 😳 | #Robotics, #Innovation, #FutureTech, AI, #TechTok](https://www.youtube.com/watch?v=0qu0rSrcnVE)**

This uncanny artificial mouth can surprisingly reproduce the sound and articulation of a real human voice. This Synthetic Vocal ...

📺 Ace Atlantis

👁️ 212K • 👍 1K • 💬 97 • ⏱️ 0:05 • 2d ago

---

**[The first ever humanoid robot Olympics begin this week](https://www.youtube.com/watch?v=OnIUM0HbzDM)**

Subscribe for more!

📺 Aaron Parnas

👁️ 132K • 👍 9K • 💬 1K • ⏱️ 0:45 • 3d ago

---

**[Brevity-focused): Welcome to the Future 🤖✨ #AI #Robotics](https://www.youtube.com/watch?v=a26QJ6N5lPM)**

Brevity-focused): Welcome to the Future ✨ #AI #Robotics #AI #Robotics #TechTrends #Shorts #FutureTech #islamic ...

📺 IslamicPathEng



👁️ 32K • 👍 2K • ⏱️ 0:11 • 1d ago

---

**[Robotic chess](https://www.youtube.com/watch?v=2h4FA6l5TPs)**

I've always loved chess, and when you add a little technology and robotics to it… I'm sold. So here we go with Chessnut Move ...

📺 Moonshotkidz 

👁️ 788 • 👍 16 • ⏱️ 0:35 • 4h ago

---

**[Robot Athlete Turns Into Crash Test Dummy After Smacking Into Wall](https://www.youtube.com/watch?v=-LOPCKtaepc)**

A humanoid robot lost control while sprinting around a track during testing ahead of the World Humanoid Robot Games in Beijing.

📺 New York Post

👁️ 84K • 👍 969 • 💬 714 • ⏱️ 2:04 • 1d ago

---

**[Faster Than Us: Human Records Broken 🏃‍♂️](https://www.youtube.com/watch?v=aFFkQxrStNQ)**

Humanoid robots are now officially breaking human speed records on the track. Sure, a few still stumble and fall, but the vast ...

📺 The Genesis Eye

👁️ 42K • 👍 206 • 💬 6 • ⏱️ 0:09 • 1d ago

---

**[Mova just made the best robot vacuum and mop of 2026! #mova70ultracomplete #ads #bestrobotvacuum2026](https://www.youtube.com/watch?v=VTivWM_lDsY)**

Extra Discount: StuffV70 = $20 Off (Aug 19 - Sep 19) ⚡Exclusive Launch Offer: $200 OFF the MOVA V70 Ultra Complete for a ...

📺 Stuff You Actually Need

👁️ 40K • 👍 1K • 💬 13 • ⏱️ 0:38 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

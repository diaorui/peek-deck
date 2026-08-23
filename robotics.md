---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-08-23T11:20:27.453824+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- videos
- social
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** August 23, 2026 at 11:20 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[3-month update, in a little story about my 3D-printed robot lamp](https://www.reddit.com/r/robotics/comments/1vvci99/3month_update_in_a_little_story_about_my/)**

A little update after about three months of working on this project. One of the more visible changes is the hardware itself. I redesigned the lamp and made a fully 3D-printed enclosure for it, so it finally looks a lot closer to what I originally had in mind rather than a prototype with exposed hardware. Probably the biggest change, though, has been the animation. I've spent a lot of time trying to make the lamp move more like an animatronic character rather than just a robot executing trajectories. At this point the mechanics aren't really the main limitation anymore. I can animate pretty much all of its movements in Watti Studio, my animation editor, so now the limiting factor is mostly how well I can actually animate it :) I moved the whole system to ROS 2 and added computer vision. The lamp streams RGB and depth from its camera, and the current point cloud can be displayed directly in the 3D view in Watti Studio. It makes it possible to see the lamp together with its surroundings while creating animations. I added lighting to the animation editor too, so the lamp's light can be keyframed together with its movements. I also spent quite a bit of time on things that aren't as fun to show in videos, especially safety. The software monitors the real movement while an animation is playing. If a joint deviates too far from the expected trajectory or something else goes wrong, the animation stops and the motors hold their current positions. The lamp also has its own REST API, so its functions can be controlled externally without being tied to the animation editor. Next I want to focus mostly on autonomous behavior and interaction with people and the environment. I'm also experimenting with reinforcement learning to teach it to jump, with the longer-term goal of getting it to actually move around on its own. There's still a lot to do, but after three months it finally feels like I have most of the basic pieces in place. I thought about making another technical demo to show the progress, but that sounded a bit boring, so I made a little story with the lamp instead :) For anyone interested in the technical side, I have a pre-release repo with more details about the hardware, software architecture and current progress: https://github.com/Nikolay-Tyulkin/Watti

21h ago

---

**[Is this the future? LOL](https://www.reddit.com/r/robotics/comments/1vvqos3/is_this_the_future_lol/)**

It’s always them goofy robots dancing and doing these goofy stuff. Look at how think those legs are. I don’t think I get how people are scared of its potential to take over the world 😭🙏🏻 It’s just so unrealistic. I just hope that they somehow manage to modify these and turn them into actual useful machines.

12h ago

---

**[Honor lightning vs tiangong in the 2026 humanoid robotics 100 meter dash](https://www.reddit.com/r/robotics/comments/1vve7ju/honor_lightning_vs_tiangong_in_the_2026_humanoid/)**

Already faster than the human world record! Insane. Last year every robot was still being remote controlled. The way both robots collided with the padding at the end was quite funny

20h ago

---

**[Chinese robot beats Usain Bolt's 100m world record at Beijing games](https://www.reddit.com/r/robotics/comments/1vvu4xs/chinese_robot_beats_usain_bolts_100m_world_record/)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

🔗 [youtube.com](https://www.youtube.com/watch?v=FGBLzMESBAo) • 9h ago

---

**[Rethinking the Quadruped](https://www.reddit.com/r/robotics/comments/1vvdroy/rethinking_the_quadruped/)**

20h ago

---

**[Robot Carnage! - 100m dash Unitree Superman and TienKung Ultra](https://www.reddit.com/r/robotics/comments/1vvfy91/robot_carnage_100m_dash_unitree_superman_and/)**

19h ago

---

**[P.A.R. (Pixel Art Robot) — A Giant, Slow, Flip-Squisk Display, Flipped by a CNC](https://www.reddit.com/r/robotics/comments/1vvyaxs/par_pixel_art_robot_a_giant_slow_flipsquisk/)**

P.A.R. is a machine draws pixel art in the real world. What it displays on the 37x18 grid of squisks is the art that random people on the internet upload on https://par.zimmzimm.com/ . I've been working on P.A.R. for almost 6 months at this point, and it's finally done (except for the custom PCB: in progress). It's a large grid of 3D-printed "squisks" (square discs), which are flipped from the back by the robot, a large CNC machine with a special toolhead. I designed all of this in OnShape and used the Flashforge Adventurer 5M to print most of the parts. The rest of the parts were made to be as cheap as possible: for example, the frame is made of EMT (Electrical Conduit) pipe, which is $0.60/ft. Learn more here. When someone submits a piece, it's added to a queue, and they can add your email to be notified when that piece is completed (absolutely NO SPAM), and they'll get to see a video of the real, physical robot drawing your art one flip at a time.

5h ago

---

**[Humanoid robot races have begun at the WHRG 2026](https://www.reddit.com/r/robotics/comments/1vvc28h/humanoid_robot_races_have_begun_at_the_whrg_2026/)**

22h ago

---

**[Follow-up: VSArena now has a proper VLA track (camera + language, no privileged state) — repo and docs are public](https://www.reddit.com/r/robotics/comments/1vvm3x7/followup_vsarena_now_has_a_proper_vla_track/)**

Posted about this project a little while ago — quick update since a few things changed that address feedback from that thread. Biggest change: split the observation space properly. There's now a VLA track where the policy only gets a 128x128 RGB camera + a language stacking instruction — cube poses are never sent to the policy. Scoring still uses real poses internally to grade spatial accuracy and completion, but that's judge-only, not policy-visible. State-based (privileged poses) is kept as a separate debug track and doesn't write public ELO either — wanted the "VLA vs state" distinction to be explicit rather than something people had to dig for. On the client-side physics concern from before:Studio (the in-browser demo) is spectator/dev-only, clearly labeled, and does not post to the public leaderboard. Public ELO only comes from a hosted harness that scores server-side. That harness isn't live yet —it's the one piece standing between this and actually being open for submissions. Repo + docs are public now:https://github.com/NovaCoding-G/VSArena -docs/harness.md — scoring writeup (spatial accuracy + task completion) -docs/sdk.md — submission protocol -Studio itself:https://vsarena.vercel.app/simulation (client-side, Rapier/WASM, 60fps) Still solo, still early, still not oversell-ready — but wanted to share since the VLA/state separation was directly a response to feedback here. Open to more of that, especially on what the scoring protocol might be missing.

15h ago

---

**[Absolute GPT-3 moment for robotics, holy moly.](https://www.reddit.com/r/robotics/comments/1vuslj3/absolute_gpt3_moment_for_robotics_holy_moly/)**

1d ago

---

---

## Google News: "robotics"

**[Robot horse and rider steal the spotlight at Chinese conference](https://www.bbc.com/news/videos/c0qvqzzdd02o)**

More than 300 companies are showcasing the latest advances in robotics at the five-day event in Beijing, China, organisers say.

BBC • 1d ago

---

**[Move over, Usain Bolt: Humanoid robots smash human records at Beijing games](https://www.nbcnews.com/tech/tech-news/chinese-humanoid-robot-lightning-beats-human-100m-world-record-rcna593869)**

More than 2,000 humanoid robots are competing in an Olympics-like showcase of China’s rapidly advancing robotics industry.

NBC News • 1d ago

---

**[Chinese robots break Usain Bolt's 100-meter record at Beijing World Humanoid Robot Games](https://www.jpost.com/international/article-906280)**

Braking was an issue, as the machines slammed into a thick mat that organizers placed several meters after the finish line.

The Jerusalem Post • 6h ago

---

**[Robots Smash Human Records at Beijing Competition](https://www.newser.com/story/395125/robots-smash-human-records-at-beijing-competition.html)**

High-tech competitors take the field in synchronized display

Newser • 13h ago

---

**[Robots can outrun humans, but can they plug in a cable?](https://www.reuters.com/world/asia-pacific/robots-can-outrun-humans-can-they-plug-cable-2026-08-23/)**

Reuters • 6h ago

---

**[US distributor of China’s most popular humanoid robots pivots after US ban](https://arstechnica.com/gadgets/2026/08/us-distributor-of-chinas-most-popular-humanoid-robots-pivots-after-us-ban/)**

FCC ban on foreign-made robots accelerated RoboStore’s US manufacturing plans.

Ars Technica • 2d ago

---

**[China’s robots rock, box and mix drinks. Can they outperform humans?](https://www.ft.com/content/e16ded89-b618-4952-a0ab-96ef11d06582?syn-25a6b1a6=1)**

Beijing policymakers have made robotics a ‘strategic priority’

Financial Times • 1d ago

---

**[ACE Robotics chairman says robot brains will have 'ChatGPT moment' by end of 2027](https://finance.yahoo.com/technology/ai/articles/ace-robotics-ceo-says-robot-100324175.html)**

Humanoid robot brains could see a breakthrough by late next year similar to the dramatic impact ChatGPT had on AI usage, the ‌chairman of Chinese embodied AI startup ACE Robotics said on Friday.  "We expect to reach the 'ChatGPT moment' for embodied intelligence by the end ‌of next year, driven by world models and environmental data capture," Wang Xiaogang told Reuters.  "Even if we reach that inflection point by late 2027, it will likely take another four to ​five years to see broad commercial implementation of embodied world models across sectors," said Wang, who is also a co-founder of Chinese AI visual recognition pioneer SenseTime.

Yahoo Finance • 2d ago

---

**[At China's robot Olympics, the finish line comes with a padded wall and a stretcher](https://www.businessinsider.com/world-humanoid-robot-games-how-to-watch-beijing-china-2026-8)**

China's second World Humanoid Robot Games kicked off Saturday in Beijing. The spectacle comes as China pours money into its humanoid robot industry.

Business Insider • 15h ago

---

**[The technology that could bring robot mowers to one in two American lawns](https://www.therobotreport.com/technology-could-bring-robot-mowers-one-half-american-lawns/)**

Improvements in AI, satellite navigation, and machine vision are helping robotic lawn mowers spread in the U.S., writes Sunseeker's founder.

The Robot Report • 22h ago

---

---

## YouTube Videos: "robotics"

**[Galbot ET1 Shows the Future of Humanoid Robots](https://www.youtube.com/watch?v=YJSw0Jf8DZ0)**

Galbot ET1 Galaxy Star is a humanoid robot designed to watch human movements, learn them in real time, and reproduce what it ...

📺 DPCcars

👁️ 19K • 👍 395 • 💬 60 • ⏱️ 2:12 • 2d ago

---

**[Chinese Humanoid Robot Runs 100m In 9.39 Seconds, Beats Usain Bolt’s Record](https://www.youtube.com/watch?v=EODFQyEAJmU)**

A Chinese humanoid robot has stunned spectators at the World Humanoid Robot Games in Beijing, running 100 metres in 9.39 ...

📺 The Daily Guardian

👁️ 407 • 👍 6 • ⏱️ 0:35 • 2h ago

---

**[Humanoid Robot Demolishes Usain Bolt’s Record #shorts](https://www.youtube.com/watch?v=A1vAQ20dyz4)**

China's Beijing Innovation Centre of Humanoid Robotics developed a robot that can run faster than Olympian Usain Bolt.

📺 New York Post

👁️ 12K • 👍 499 • 💬 110 • ⏱️ 0:52 • 10h ago

---

**[Robot Athlete Turns Into Crash Test Dummy After Smacking Into Wall](https://www.youtube.com/watch?v=-LOPCKtaepc)**

A humanoid robot lost control while sprinting around a track during testing ahead of the World Humanoid Robot Games in Beijing.

📺 New York Post

👁️ 71K • 👍 865 • 💬 597 • ⏱️ 2:04 • 1d ago

---

**[Humanoid robots smash human records in 100m sprint at robot games](https://www.youtube.com/watch?v=3Y9E2CcMTFk)**

Chinese humanoid robots broke records set by humans, including beating Usain Bolt's 100-meter sprint world record, on the ...

📺 ABC7

👁️ 35K • 👍 426 • 💬 108 • ⏱️ 0:42 • 13h ago

---

**[ROGUE ROBOT: Amazon drone drops package into swimming pool #shorts #foxnews #fox #news](https://www.youtube.com/watch?v=G6wyGJ9t7H4)**

An Amazon delivery drone went rogue during a Texas dropoff, plopping a woman's package straight into her swimming pool.

📺 Fox News Clips

👁️ 65K • 👍 486 • 💬 104 • ⏱️ 0:17 • 2d ago

---

**[Brevity-focused): Welcome to the Future 🤖✨ #AI #Robotics](https://www.youtube.com/watch?v=a26QJ6N5lPM)**

Brevity-focused): Welcome to the Future ✨ #AI #Robotics #AI #Robotics #TechTrends #Shorts #FutureTech #islamic ...

📺 IslamicPathEng



👁️ 27K • 👍 1K • ⏱️ 0:11 • 20h ago

---

**[Why Home Robots Aren&#39;t Ready (Yet)](https://www.youtube.com/watch?v=EMj1fl17Tv8)**

Home robots have long been the stuff of sci-fi dreams (and nightmares), but they lag behind AI chatbots, AI agents, and even their ...

📺 CNET

👁️ 12K • 👍 381 • 💬 64 • ⏱️ 5:16 • 6d ago

---

**[Mova just made the best robot vacuum and mop of 2026! #mova70ultracomplete #ads #bestrobotvacuum2026](https://www.youtube.com/watch?v=VTivWM_lDsY)**

Extra Discount: StuffV70 = $20 Off (Aug 19 - Sep 19) ⚡Exclusive Launch Offer: $200 OFF the MOVA V70 Ultra Complete for a ...

📺 Stuff You Actually Need

👁️ 38K • 👍 979 • 💬 11 • ⏱️ 0:38 • 3d ago

---

**[Humanoid robots compete on day one of World Robot Games](https://www.youtube.com/watch?v=AerpY_g67m8)**

Humanoid robots competed in various events on day one of the World Robot Games, with one even breaking Usain Bolt's world ...

📺 ABC News

👁️ 31K • 👍 292 • 💬 86 • ⏱️ 0:40 • 12h ago

---

---

*Generated by PeekDeck - A glance is all you need*

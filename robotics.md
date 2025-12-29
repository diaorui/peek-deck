---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2025-12-29T07:35:27.944250+00:00'
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

**Last Updated:** December 29, 2025 at 07:35 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[Designing a Compute Board for a Humanoid Robot](https://www.reddit.com/r/robotics/comments/1pye7ih/designing_a_compute_board_for_a_humanoid_robot/)**

1h ago

---

**[20 kg Payload Mobile Platform: Cost Estimate](https://www.reddit.com/r/robotics/comments/1pyfqnv/20_kg_payload_mobile_platform_cost_estimate/)**

I want to build a remotely controlled mobile platform capable of carrying about 20 kg. There is a kit on AliExpress for around $100 that includes: 1 piece metal frame 4 pcs 12V encoder motor 4 pcs 97mm mecanum wheel 4 pcs engine bracket 4 pcs motor cables 1 set of screws Is there anyone here who has experience creating something similar (10-20kg payload)? How much did it cost? The price (including shipping) seems too good to be true, but I secretly hope there is an even cheaper option or maybe a totally different approach to "I want to move 20 kg horizontally on an arbitrary surface"

19m ago

---

**[Fully autonomous PHYBOT C1 playing badminton against humans](https://www.reddit.com/r/robotics/comments/1pxnql1/fully_autonomous_phybot_c1_playing_badminton/)**

From CyberRobo on 𝕏: https://x.com/CyberRobooo/status/2004918558481064403 Website: https://www.phybot.tech/en/home

21h ago

---

**[What foundational skills matter most for robotics students?](https://www.reddit.com/r/robotics/comments/1pxu0t6/what_foundational_skills_matter_most_for_robotics/)**

I’m early in my robotics journey and trying to build strong fundamentals. Between programming, math, electronics, and mechanics, it’s hard to prioritize everything at once btw; For those working in robotics, what foundations mattered most in the long run?

16h ago

---

**[Do robots actually benefit from knowing what humans are looking at?](https://www.reddit.com/r/robotics/comments/1py6ujk/do_robots_actually_benefit_from_knowing_what/)**

I’m thinking about human–robot interaction and had a simple question. I’m wondering whether it’s actually helpful for robots to recognize where a human is looking or gazing when performing tasks instructed by a human. In practice, does knowing what a human is looking at meaningfully help robot behavior? Or do most real systems rely on other signals?

7h ago

---

**[DIY hexapod robot help](https://www.reddit.com/r/robotics/comments/1pyeigb/diy_hexapod_robot_help/)**

Components: - Power - 1 x Lipo 3s 12v battery 1 x 5v DC inline to Elegoo Voltage regulator 1 x 25v fuse / fuse connector 1 x 12v (20Amps) buck converter with 6v short pin setting 1 x Elegoo power module (power to the board provided) 2 x screw terminal blocks (horizontally connected) -Misc - 1 x switch 1 x ESP 32 CAM board - Servos - 18 x MG996R servos (3 DOF x 6 legs) 2 x PCA 9685 driver boards Power: The lipos is regulated to 6v continuous via the SBEC which provides power throughout the first block terminal. The terminal simply has a metal bars underneath connecting each pair of screws (horizontally) together. This is why the wiring jumps from each as shown. I can confirm this works fine and supplies 6v stable to each screw within the block. The reasoning for this approach was 1. I'm a bit of an idiot and 2, I figured that the two PCA boards couldn't handle supplying power and pwm signals for a hexapod robot with 18 servos. While it is true that a max of 3 legs will move (tripod gait, hence the power choices made) -- it made sense to me to offload the power regulation and hopefully prevent noise. (not sure why i did the same for ground now, but I digress).. The ground is treated the same as seen within the shitty schematic above. The ground from the block terminal is connected back to the esp32 directly and to the Elegoo module (attempted star pattern in hopes of preventing grounding issues). Each ground and power wire from each of the servos goes to a spot on their respective block terminals. The only wire going to the PCA boards from each servo is the PWM signal wire. ** It is important to note that all electronics power is provided via the Elegoo module and the lipo only provides power to the terminals for the servos. Both PCA boards are connected together and the address pin is soldered for proper referencing. The PCA boards are supplied power via VCC pin with a 3.3v provided via Elegoo power module. The GND is also connected from the power module to the PCA. Both SDL and SDA come are connected to the first board from the ESP32 board Via GPI0 13 and 15. (these pins are referenced in the code). The esp32 has a ground connected from the GND terminal block and the Elegoo power module. it has 5v supplied to the 5v pin (I used the onboard regulator over the direct 3.3v pin due to issues listed with the boards 3.3v usage). Verification done: - Powering the rails provides steady 6v. GND terminal is correctly grounded with each point on the various boards to what I could see. - Both PCA boards light up and the 1st/secondary board measures a steady 3.3v. - Esp32 is properly powered and programs fine. However when I try to test a servo I get a failed transaction (NACK) signals. I am unsure why and I believe it likely has to do with my electronics. If a hobbyist or Elec Eng. could help me trouble shoot this it would be much appreciated. **

1h ago

---

**[Robot tire rims moving inside tires?](https://www.reddit.com/r/robotics/comments/1py7do3/robot_tire_rims_moving_inside_tires/)**

How to stop tire rims from moving inside tires for my pesticide spraying robot? My robot struggles even with or without load because the rims keep rotating inside tires. How do I fix it?

7h ago

---

**[First look at Disney aquatic robots (YouTube)](https://www.reddit.com/r/robotics/comments/1pwv1pv/first_look_at_disney_aquatic_robots_youtube/)**

Walt Disney Imagineering on YouTube: NEW Robotic Olaf Revealed! Inside Disney Imagineering R&D | We Call It Imagineering: https://youtu.be/EoPN02bmzrE (aquatic robots at 27 min)

1d ago

---

**[JD robot on test for patrolling](https://www.reddit.com/r/robotics/comments/1pxtdyx/jd_robot_on_test_for_patrolling/)**

it should be installed on my ecovacs goat for patrolling in the garden. need some adjustments with sound r2d2 , eyes colors and movements . program used is ARC at synthiam.com.

16h ago

---

**[Switching from physics to robotics](https://www.reddit.com/r/robotics/comments/1pxlmei/switching_from_physics_to_robotics/)**

I'd really love to get into robotics, and unfortunately I realized it "too late". I've completed a bachelors in physics and a masters in physics with focus on data science & ML. So I have a fairly strong background in maths, know all entry level ML & statistics concepts but learned nothing about robotics during uni. I'm also strong in Python. I'm interested in the software side of things, specifically RL (written my bachelor's thesis about this), Imitation learning or CV. I've already started to self study, currently learning the basics of ROS2 and want to get into robotics specific CV next. What areas/topics are vital for my first entry job? Is it possible to make this transition?

23h ago

---

---

## Google News: "robotics"

**[Surreal humanoid robots are set to begin border patrol duties between China and Vietnam](https://www.earth.com/news/surreal-video-reveals-humanoid-robots-for-border-patrol-pr25/)**

Surreal humanoid robots are set to begin border patrol duties between China and Vietnam

Earth.com • 2d ago

---

**[Musk remarks put China’s fast-evolving humanoid ‘cerebellum’ in spotlight](https://www.globaltimes.cn/page/202512/1351675.shtml)**

A concert, six humanoid robots, and one flawless somersault. Together, they ignited not only the cheers of a crowd of more than 100,000 viewers, but also triggered a surge of wows in the cyberspace.

Global Times • 19h ago

---

**[Humanoid Robots Keep Slipping Into the Future, Much Like Fusion](https://cleantechnica.com/2025/12/27/humanoid-robots-keep-slipping-into-the-future-much-like-fusion/)**

Legged robots can flip and dance, but safe general-purpose humanoids in homes remain decades away due to manipulation and safety limits.

CleanTechnica • 1d ago

---

**[Even the Companies Making Humanoid Robots Think They’re Overhyped](https://www.wsj.com/tech/ai/humanoid-robot-hype-use-timeline-1aa89c66?gaa_at=eafs&gaa_n=AWEtsqftTULXbUkhpjgBxR6J_07u_0XhEBKZCDH6MVmzYwzn1-08s-BaD1VB&gaa_ts=695232ab&gaa_sig=z4yuLe-SIFLfJVtDQJYPs7r6IVlzHrTJqn9xqtRo07DtTfyuWlZE4GQQLqlLBDYE6Z8mcEH3i1ysMMV0TAoEMQ%3D%3D)**

The Wall Street Journal • 3d ago

---

**[Have $2,000? 3 Top Robotics Stocks to Buy and Hold for at Least a Decade](https://finance.yahoo.com/news/2-000-3-top-robotics-102000972.html)**

These top robotics stocks are compelling for different reasons.

Yahoo Finance • 1d ago

---

**[NIC submits $4M AI, robotics grant proposal](https://cdapress.com/news/2025/dec/27/nic-submits-4-million-federal-ai-and-robotics-grant-proposal/)**

North Idaho College has submitted a $4 million federal grant proposal to expand the college’s capacity in artificial intelligence, robotics, and advanced automation through the U.S. Department of Education’s Fund for the Improvement of Postsecondary Education Special Projects program.

Coeur d'Alene Press • 1d ago

---

**[Researchers create world's smallest programmable, autonomous robots](https://techxplore.com/news/2025-12-world-smallest-programmable-autonomous-robots.html)**

Tech Xplore • 3d ago

---

**[Unitree Robotics Productions presents: Man Getting Hit By Robot.](https://www.theverge.com/tech/850544/unitree-robotics-productions-presents-man-getting-hit-by-robot)**

The robot. His groin. It works on so many levels. Roll it again.
[Media: https://bsky.app/profile/jjvincent.bsky.social/post/3mayddynhas2l]

The Verge • 1d ago

---

**[Hong Kong Robotics Group to Deliver First 100 Intelligent Security Robots to Tonwell Security](https://www.tipranks.com/news/company-announcements/hong-kong-robotics-group-to-deliver-first-100-intelligent-security-robots-to-tonwell-security)**

TipRanks • 7h ago

---

**[Robots are like us: struggling with baby goats, car nightmares, and LA-to-Miami Beach culture shock](https://fortune.com/2025/12/26/robot-nightmares-traffic-baby-goats-just-like-humans-serve-robotics-cofounder-chun/)**

"Robots have nightmares about cars," Serve Robotics co-founder MJ Burk Chun told Fortune Brainstorm AI. "Cars are also very scary for robots."

Fortune • 2d ago

---

---

## YouTube Videos: "robotics"

**[China&#39;s New AI Robot Just Broke a Human Skill Barrier](https://www.youtube.com/watch?v=zii2FiFBl5k)**

Humanoid robots just crossed a line that used to belong only to human hands. In China, a humanoid stitched fabric live on stage ...

📺 AI Revolution

👁️ 439K • 👍 2K • 💬 254 • ⏱️ 12:51 • 3d ago

---

**[AI at CES 2026 Is Insane: Here’s What’s Coming](https://www.youtube.com/watch?v=O6qrzEqAP7A)**

CES 2026 is shaping up to feel very different from previous years. Instead of flashy concepts and distant promises, the focus shifts ...

📺 AI Revolution

👁️ 51K • 👍 976 • 💬 87 • ⏱️ 8:59 • 1d ago

---

**[China&#39;s G1 Robots Just Broke the Internet With This Live Concert Moment!](https://www.youtube.com/watch?v=M1G1tqpzX6g)**

What began as a standard live concert in China turned into a moment that stunned the audience and exploded across the internet.

📺 AI Tech Academy

👁️ 42K • 👍 665 • 💬 112 • ⏱️ 13:55 • 5d ago

---

**[Humanoid robot runs like a spider, shows we&#39;re close to disaster](https://www.youtube.com/watch?v=wNMoEXr12rY)**

ChatGPT in a robot. Could AI become dangerous? Can we trust AI? AGI. Use code insideai at https://incogni.com/insideai to get ...

📺 InsideAI

👁️ 287K • 👍 13K • 💬 2K • ⏱️ 16:24 • 5d ago

---

**[I Tested the Most Realistic AI Robot Pet](https://www.youtube.com/watch?v=iHKOiJlnb2Y)**

I Tested the Most Realistic AI Robot Pet Loona! Watch "How Smartphones are Made" ...

📺 Hafu Go

👁️ 205K • 👍 3K • 💬 40 • ⏱️ 0:39 • 5d ago

---

**[&quot;This Isn&#39;t AI Anymore. It’s ALIEN Intelligence&quot; | When AI and Robotics Merge](https://www.youtube.com/watch?v=Q-eIhXSJfoA)**

A look into the first "non-human mind" we've ever met. AI + Robot = ♾️ To learn for free on Brilliant, go to ...

📺 Beeyond Ideas

👁️ 95K • 👍 2K • 💬 579 • ⏱️ 21:33 • 3d ago

---

**[Unitree Robots EVOLVE 🤖🔥 From Chinese New Year Gala to Wang Leehom Concert (2025)](https://www.youtube.com/watch?v=HEe5UfvyZYo)**

In January 2025, humanoid robots from Unitree Robotics made history with a massive, synchronized performance on China's ...

📺 ROBOTIC WORLD25

👁️ 65K • 👍 2K • 💬 261 • ⏱️ 18:43 • 6d ago

---

**[Big Humanoid Robots Are Learning How to Fight. Should We Be Concerned?](https://www.youtube.com/watch?v=kkWe9F345Do)**

The little G1 didn't stand a chance Unitree's latest demos reveal that kickboxing is no longer just for its smaller G1 humanoid ...

📺 CNET

👁️ 23K • 👍 391 • 💬 27 • ⏱️ 1:30 • 3d ago

---

**[NEW Guns on SCORPION are DEADLY! War Robots Gameplay](https://www.youtube.com/watch?v=B9H476esZBA)**

War Robots Gameplay: NEW Guns Elox and Murix on Scorpion - WR #warrobots #warrobotsgameplay #wr My Best-Of-War ...

📺 Manni-Gaming

👁️ 8K • 👍 416 • 💬 94 • ⏱️ 17:59 • 18h ago

---

**[Kawasaki Kaleido 9 #humanoidrobot #airobot #robot #japantechnology #robotics #industry40](https://www.youtube.com/watch?v=c3iuZH72NFA)**

Kawasaki Heavy Industries says it's pushing its flagship humanoid robot into the real world after a decade of research and ...

📺 Kalil 4.0

👁️ 1K • 👍 60 • 💬 3 • ⏱️ 0:44 • 9h ago

---

---

*Generated by PeekDeck - A glance is all you need*

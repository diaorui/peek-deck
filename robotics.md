---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-02-19T10:11:31.629287+00:00'
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

**Last Updated:** February 19, 2026 at 10:11 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[My Unitree Go2 Pro Setup](https://www.reddit.com/r/robotics/comments/1r8uw3u/my_unitree_go2_pro_setup/)**

[Disclaimer: This text was not touched by AI, this is solely by me, so a few formulation issues might be hidden in there] TLDR: - With some tricks, even the cheaper quadruped models can be used for complex tasks - Reliable and low-latency remote operation and monitoring is hard. But here, wireless is usually the bottleneck, not the VPN - Foxglove UI is pretty neat (not fully open-source) - Having a good dev environment setup from the start is invaluable - A lot can be done with a pure open-source stack! The video shows a setup I've been working on for a while now. Early last year, I took quite a portion of my savings to get my hands on a quadruped robot. These savings did not even get me the full ROS2-ready setup that one needs to actually build a cool application, I had to make quite a few detours (some that probably voided the warranty, but let us not get deeper into it). In any case, I had time the last few days (and nights) to finally setup a clean and performant development and introspection environment for my robot. As you can see from the video, this includes full remote control and monitoring of the inner going-ons. I initially tried sending the whole DDS traffic through my network, but due to obvious overhead reasons, this was not really scalable, especially when wanting a live feed of camera and LiDAR data that is low latency enough for "secure" remote manipulation. The next iteration took me down the road of WebRTC, a protocol that only transmits frame differences, reducing traffic significantly. The results for the camera streams were impressive, but this meant I would have to tackle a conversion layer for each topic, again not a clean solution. Finally, I tried out Foxglove. Although not fully open-source, they use a web socket connection, therefore again avoiding DDS congestion. While it might seem a bit less performant than the custom WebRTC solution, the amazing UI and compatability with my ROS2 setup speaks for itself. Also by the way, the setup above is not solely within a local network! I can spin up this bad boy all over the world through my self-hosted Headscale VPN (WireGuard on the backend). Through testing (and some help with the friends at Technologiehub Wien), I found out that the VPN latency is less of a bottleneck than the wireless connection. Making sure that a non-crowded 5GHz channel is used was an enormous performance boost. Concerning the ROS2 setup, everything is ready to add Nav2 support. LiDAR access works, tf tree looks good and odometry information is also already there. This will be the task to tackle next. The whole setup is dockerized and remote development is pretty easy through the SSH connection via the VPN and a custom devcontainer (although it took a while to get ROS2 Jazzy + CUDA cores working correctly...). In case anyone has read this far: - Should I open-source my setup (including VPN optimizations)? - Any idea how I can get my invested money back? (Not a big issue, I learned so much and am having a blast!) - What would you do with this robot? - Any improvement suggestions? Thats it, goodbye and thank's for the fish!

35m ago

---

**[Fact Check: Does a student "World Championship" by NVIDIA & Boston Dynamics exist in Singapore?](https://www.reddit.com/r/robotics/comments/1r8u6ww/fact_check_does_a_student_world_championship_by/)**

Hi everyone, I’m trying to verify the legitimacy of some "World Championship" claims made by someone I know. The details feel very off to me, but I wanted to check with people who actually follow the international robotics circuit. ​The Specific Claims: ​The Event: An "International Robotics and Coding Championship 2025" held in Singapore. ​The Organizers: Claims it was officially hosted/sponsored by NVIDIA and Boston Dynamics. ​The Award: 2nd Place in "International Innovation and Coding." ​The Red Flags: ​The Trophy: The award shown is a generic "Victory Female" figurine (a gold-plated plastic woman holding a torch) on a black plastic base. I found the exact model on IndiaMART for about ₹200 (~$2.50). Do "World Championships" really give out generic mass-produced budget trophies? ​The Labels: The logos for NVIDIA and Boston Dynamics look like they were printed on a basic home printer and stuck onto the base with adhesive tape or cheap glue. ​Corporate Role: I’ve never heard of NVIDIA or Boston Dynamics hosting youth-only trophy ceremonies for individuals. I thought they were technology partners for conferences like ROSCon (which was in Singapore in Oct 2025), not event organizers for school-level awards. ​Missing Records: I checked the official WRO (World Robot Olympiad) 2025 Singapore results, and the winners in the senior categories were from Costa Rica and Malaysia. There is no mention of this specific "NVIDIA" championship anywhere online. ​My Questions: ​Does anyone know of a real "World Championship" hosted by NVIDIA/Boston Dynamics in Singapore in 2025? ​Are "World Champion" trophies usually generic plastic figurines available at local gift shops? ​Is it common for people to fake these "STEM achievements" using AI-generated bios and home-made trophies? ​Thanks for any help!

1h ago

---

**[Great improvement for only a year](https://www.reddit.com/r/robotics/comments/1r7qfoq/great_improvement_for_only_a_year/)**

1d ago

---

**[Is there a platform to find faculties working/ researching on SLAM?](https://www.reddit.com/r/robotics/comments/1r8spd4/is_there_a_platform_to_find_faculties_working/)**

Hi all, as the title states is there a platform that consolidates a list of people based on research topics? I am looking to find professors working on slam or perception in the UK. Thanks.

2h ago

---

**[Announcing Webots Academy: A zero-setup, browser-based simulation platform for universities](https://www.reddit.com/r/robotics/comments/1r8vc70/announcing_webots_academy_a_zerosetup/)**

8m ago

---

**[Mini HPC-style HA Homelab on Raspberry Pi 3B+ / 4 / 5 Kafka, K3s, MinIO, Cassandra, Full Observability](https://www.reddit.com/r/robotics/comments/1r8r38s/mini_hpcstyle_ha_homelab_on_raspberry_pi_3b_4_5/)**

4h ago

---

**[Opinion on MS Robotics at WPI / Oregon State / JHU](https://www.reddit.com/r/robotics/comments/1r8ogvw/opinion_on_ms_robotics_at_wpi_oregon_state_jhu/)**

6h ago

---

**[Capstan Drive (OC)](https://www.reddit.com/r/robotics/comments/1r82l0h/capstan_drive_oc/)**

21h ago

---

**[Battle Bots Competition – March 7 at Renaissance Youth Center (South Bronx)](https://www.reddit.com/r/robotics/comments/1r8gfbh/battle_bots_competition_march_7_at_renaissance/)**

12h ago

---

**[Here's a great tutorial for Visual SLAM using a RealSense 3D stereo depth camera in RGBD mode running on NVIDIA Isaac ROS](https://www.reddit.com/r/robotics/comments/1r87zgt/heres_a_great_tutorial_for_visual_slam_using_a/)**

https://nvidia-isaac-ros.github.io/concepts/visual_slam/cuvslam/tutorial_realsense_rgbd.html

17h ago

---

---

## Google News: "robotics"

**[Amazon halts Blue Jay robotics project after less than 6 months](https://techcrunch.com/2026/02/18/amazon-halts-blue-jay-robotics-project-after-less-than-six-months/)**

Amazon said Blue Jay's core tech will be used for other robotics projects and the employees who worked on it were moved to other projects.

TechCrunch • 15h ago

---

**[China’s dancing robots: how worried should we be?](https://www.theguardian.com/world/2026/feb/18/china-dancing-humanoid-robots-festival-show)**

Eye-catching martial arts performance at China gala had viewers and experts wondering what else humanoids can do

The Guardian • 16h ago

---

**[AI-enabled robotics could shift global manufacturing power, CEO of Alphabet company says](https://www.cnbc.com/2026/02/18/wendy-tan-white-building-the-android-of-robotics-at-intrinsic.html)**

When low labor costs aren’t the primary driver of manufacturing advantage, the world might experience a dramatic economic shift – and AI could be the key.

CNBC • 21h ago

---

**[Chinese AI and robotics firms appoint millennial, Gen Z stars as chief scientists](https://www.scmp.com/tech/big-tech/article/3343042/chinese-ai-and-robotics-firms-appoint-millennial-and-gen-z-rising-stars-chief-scientists)**

Young talent drive AI innovation at Chinese tech firms, focusing on fundamental research and strategic planning for future technologies.

South China Morning Post • 6h ago

---

**[Canadian Shipyard Turns to AI Robotics to Automate One of Shipbuilding’s Toughest Jobs](https://gcaptain.com/canadian-shipyard-turns-to-ai-robotics-to-automate-one-of-shipbuildings-toughest-jobs/)**

Seaspan Shipyards has awarded a $1.5 million contract to Alberta-based Confined Space Robotics to develop semiautonomous systems for blast and paint operations, marking a significant push toward automation in one of shipbuilding’s most hazardous and labor-intensive processes.

gCaptain • 14h ago

---

**[Columbus AI robotics company signs R&D deal with nation's largest shipbuilder](https://www.bizjournals.com/columbus/news/2026/02/18/path-robotics-hii-ai-welding-shipbuilding.html)**

The Business Journals • 23h ago

---

**[Bellefontaine Robotics make strong run at Meaden and Moore](https://www.peakofohio.com/local-news/bellefontaine-robotics-make-strong-run-at-meaden-and-moore/)**

Students from Bellefontaine Robotics turned in a strong performance Saturday at the Meaden and Moore Competition, hosted by Brecksville-Broadview Heights High School, with several teams […]

Peak of Ohio • 2d ago

---

**[Inside automakers’ strategic bet on humanoid robots beyond the assembly line](https://www.autonews.com/technology/an-automakers-turn-to-robots-for-future-business-0218/)**

Automakers from Tesla to Hyundai are pivoting into humanoid robots, betting their manufacturing expertise will dominate a market projected at $7.5 trillion by 2050.

Automotive News • 22h ago

---

**[A robotic dog made in China gets an Indian university kicked out of an AI summit](https://apnews.com/article/india-ai-chinese-galgotias-university-robotic-dog-850acd70109cae9ae34c2b78923b2cbb)**

A private Indian university has been booted from a top artificial intelligence summit in New Delhi after one of its staffers displayed a a commercially available robotic dog made in China, claiming it was the university’s own innovation.

Associated Press News • 21h ago

---

**[Bettendorf robotics team advances to world championship](https://www.kwqc.com/2026/02/16/bettendorf-robotics-team-advances-world-championship/)**

A group of elementary students from Bettendorf is heading to the world stage after qualifying for the FIRST LEGO League World Championship.

KWQC • 3d ago

---

---

## YouTube Videos: "robotics"

**[A Whole Bunch of Robots Sending New Year Greetings to Everyone!](https://www.youtube.com/watch?v=w4IOJH9Akhg)**

The same model of the 'Kung Fu Bot' at the Spring Festival Gala, Cluster Cooperative Rapid Scheduling System.

📺 Unitree Robotics

👁️ 156K • 👍 1K • 💬 119 • ⏱️ 0:32 • 1d ago

---

**[China&#39;s humanoid robots take center stage at Lunar New Year show](https://www.youtube.com/watch?v=stNO7V8xJHk)**

Humanoid robots took the stage and captivated the world performing dances and kung fu during a Lunar New Year show in China ...

📺 NBC News

👁️ 166K • 👍 1K • 💬 618 • ⏱️ 2:36 • 1d ago

---

**[How Unitree Trained Robots to Master Real Kung Fu Moves](https://www.youtube.com/watch?v=VPRIl-j-T7Q)**

Unitree's humanoid robots did not just perform kung fu on stage. They trained for it like professional athletes. In this video, we ...

📺 DPCcars

👁️ 79K • 👍 1K • 💬 484 • ⏱️ 2:00 • 1d ago

---

**[China New AI Robots Gain HUMAN SENSES (Touch, Vision, Smell And Memory)](https://www.youtube.com/watch?v=l-CmzOLo34g)**

China just unveiled a new wave of physical AI that pushes humanoid robots far beyond demos. Tiangong 3.0 arrives as a full-size ...

📺 AI Revolution

👁️ 50K • 👍 1K • 💬 157 • ⏱️ 12:43 • 3d ago

---

**[Should we be impressed or worried by China&#39;s humanoid robot display?](https://www.youtube.com/watch?v=RuEEOUjT-N0)**

China Media Group's 2026 Spring Festival Gala drew widespread attention with a performance of humanoid robots that appeared ...

📺 Guardian News

👁️ 246K • 👍 430 • 💬 286 • ⏱️ 0:52 • 1d ago

---

**[China&#39;s humanoid robots perform incredible martial arts stunts for Chinese New Year](https://www.youtube.com/watch?v=R6T-Ea5CfRE)**

The routine fused traditional martial arts with advanced robotics, featuring synchronized stunts and sword and nunchuk ...

📺 The Sun

👁️ 1.1M • 👍 18K • 💬 8K • ⏱️ 2:37 • 2d ago

---

**[Galgotias University AI Summit | &#39;These Robot Dogs Are Chinese, Not Indian&#39;: Galgotias Thrown Out](https://www.youtube.com/watch?v=zyVpCu_PslQ)**

Galgotias University has come under scrutiny after displaying a Chinese-made robotic dog at the India AI Impact Summit. Sources ...

📺 NDTV

👁️ 19K • 👍 86 • 💬 191 • ⏱️ 5:02 • 1d ago

---

**[Humanoid Robots Perform in China&#39;s 2026 Lunar New Year Gala](https://www.youtube.com/watch?v=LPEGve_U1cY)**

Humanoid robots stole the show at CMG's 2026 Spring Festival Gala, pulling off slick Kung fu moves alongside young martial ...

📺 New York Post

👁️ 57K • 👍 901 • 💬 627 • ⏱️ 2:01 • 18h ago

---

**[Dancing humanoid robots take centre stage at China&#39;s Lunar New Year Gala](https://www.youtube.com/watch?v=HEuhhanh878)**

The world is ringing in the year of the Fire Horse and China is marking Lunar New Year with an extraordinary and unique ...

📺 Al Jazeera English

👁️ 71K • 👍 785 • 💬 432 • ⏱️ 7:31 • 1d ago

---

**[Unitree Spring Festival Gala Robots —a Full Release of Additional Details](https://www.youtube.com/watch?v=Ykiuz1ZdGBc)**

Dozens of G1 robots achieved the world's first fully autonomous humanoid robot cluster Kung Fu performance (with quick ...

📺 Unitree Robotics

👁️ 694K • 👍 8K • 💬 1K • ⏱️ 1:41 • 2d ago

---

---

*Generated by PeekDeck - A glance is all you need*

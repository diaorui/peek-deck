---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-09T14:06:17.607970+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- social
- videos
- news
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** April 09, 2026 at 14:06 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[A robot that cook eggs by Skild AI](https://www.reddit.com/r/robotics/comments/1sgmwgy/a_robot_that_cook_eggs_by_skild_ai/)**

From Deepak Pathak on 𝕏 (full video): https://x.com/pathak2206/status/2041939631860482211

2h ago

---

**[I trained AI to fly a drone swarm from scratch — no hand-coded paths, no human pilots](https://www.reddit.com/r/robotics/comments/1sggkrn/i_trained_ai_to_fly_a_drone_swarm_from_scratch_no/)**

What you're watching: 8 virtual Crazyflie quadrotors that learned to take off, hold formations, recover from failures, and navigate obstacles entirely through trial and error in simulation. No scripted choreography. The swarm figures it out. Full open-source repo if you want to run it yourself: https://github.com/garykuepper/ggSwarm Rendered in NVIDIA Isaac Lab. Trained with reinforcement learning (PPO). Each drone runs the same AI brain and makes its own decisions — no central controller telling them what to do.

8h ago

---

**[Aigen’s autonomous solar robots identify and remove weeds without herbicides](https://www.reddit.com/r/robotics/comments/1sfylpx/aigens_autonomous_solar_robots_identify_and/)**

21h ago

---

**[Sim-to-Real with spiking neurons on a €100 quadruped — on-device learning at 50Hz on Raspberry Pi 4](https://www.reddit.com/r/robotics/comments/1sgou6e/simtoreal_with_spiking_neurons_on_a_100_quadruped/)**

I've been working on biologically grounded locomotion control using spiking neural networks instead of conventional RL. The system runs on a Freenove Robot Dog Kit (FNK0050) with a Raspberry Pi 4. The approach: train an Izhikevich SNN in MuJoCo simulation using a custom MJCF model of the robot, then transfer the brain to real hardware where it continues learning with IMU feedback (MPU6050). A central pattern generator provides innate gait, and a competence gate gradually hands control to the SNN as it proves stable. Key result: brain persistence works — stop the robot, restart it days later, synaptic weights reload and it walks immediately without relearning. A fresh brain needs 2,000 steps (40s) to reach the same level. Honest limitation: spectral analysis shows the SNN learns conservative dampening rather than faster/better gaits. It makes movements smaller and more regular. Biologically plausible (puppies do this) but not yet performance-improving. Total hardware cost: ~€200 (Pi + kit). 232 neurons, 50Hz control loop, no GPU needed. Demo: https://www.youtube.com/watch?v=7iN8tB2xLHI Code: github.com/MarcHesse/mhflocke (Apache 2.0) Paper: doi.org/10.5281/zenodo.19481146 Happy to discuss the architecture, the sim-to-real challenges, or the conservative dampening finding.

1h ago

---

**[[Update] PyOctoMap now works out of the box on Windows, Mac, and Linux (Python 3.14 ready!)](https://www.reddit.com/r/robotics/comments/1sgobi2/update_pyoctomap_now_works_out_of_the_box_on/)**

Hey everyone, I’ve just pushed a big update to PyOctoMap to make it feel truly "native" in Python. The main goal was to kill the "manual dependency wrangling" phase. We now have pre-built wheels for Windows and macOS (Apple Silicon), so it’s finally just a pip install pyoctomap away on any platform. We’re even ready for Python 3.14. Aside from platform support, I’ve added: Multi-Tree Support: Color, Stamped, and Counting trees are all now in the core. AI Demo: The pyocto-map-anything showcase is updated to show how this all ties into AI depth estimation. All types of contributions and support are welcome! If this makes your robotics or 3D perception workflow easier, a star on GitHub ⭐ or a bit of feedback would be awesome. GitHub:https://github.com/Spinkoo/pyoctomap https://preview.redd.it/zeon4s6vs5ug1.png?width=2370&format=png&auto=webp&s=88fde4081612f981454cbe4953e11b11e9273fcf

1h ago

---

**[Now we are one!](https://www.reddit.com/r/robotics/comments/1sg5qwh/now_we_are_one/)**

16h ago

---

**[I have started working on a long procrastinated project](https://www.reddit.com/r/robotics/comments/1sgcz71/i_have_started_working_on_a_long_procrastinated/)**

this week i have finally started working on my myoelectric prosthetic arm. only three fingers to ease the tests and reduce cost of motors and electrods. hope you enjoy the chrome!

11h ago

---

**[Splitting my robot across two controllers felt like an upgrade… until it didn’t](https://www.reddit.com/r/robotics/comments/1sgkvty/splitting_my_robot_across_two_controllers_felt/)**

Splitting my robot across two controllers felt like a good idea at the time, but ended up being way more annoying than I expected. I moved sensor handling onto a second controller to “clean things up” since the main one was getting crowded, and on paper it made sense — motor control on one side, sensors and higher-level stuff on the other. In practice I just kept running into small timing issues, messages showing up a bit later than I thought, and those really frustrating cases where it works fine most of the time but then randomly jitters or drifts. Nothing I added was that complex by itself, but having that boundary made everything harder to reason about, and debugging got a lot worse since I couldn’t see everything in one place anymore. I did get it working eventually, but it definitely slowed me down compared to when everything was on one controller, even if that setup was kind of messy.

4h ago

---

**[LeRobot (Hugging Face) just released "Unfolding Robotics", an open-source recipe for teaching a robot to fold your clothes](https://www.reddit.com/r/robotics/comments/1sfnve9/lerobot_hugging_face_just_released_unfolding/)**

"The blog walks through the entire process: → Which robot, cameras, and teleoperation setup we used → How to gather high-quality demonstrations → Which model architecture and training recipe performed best → What we learned, and what we’d do differently Everything is open-source and ready to use in LeRobot v0.5.1." Unfolding Robotics: The Open-Source Recipe for Teaching a Robot to Fold Your Clothes: https://huggingface.co/spaces/lerobot/robot-folding From LeRobot on 𝕏: https://x.com/LeRobotHF/status/2041542790610297259

1d ago

---

**[End-to-End LiDAR Perception Pipeline from Scratch: Almost none of the real problems were about the model](https://www.reddit.com/r/robotics/comments/1sfq6m6/endtoend_lidar_perception_pipeline_from_scratch/)**

I built an end-to-end LiDAR perception pipeline on 128-beam infrastructure data (~184k points/frame, 10 sequential frames, busy urban intersection). The surprising part: almost none of the real problems were about the model. Ground removal, clustering connectivity, feature representation, track lifecycle management — these are where the system actually broke. Repeatedly. Full code + reports: https://github.com/bonsai89/lidar-perception-pipeline TL;DR - Ground removal fails in unexpected ways (RANSAC locks onto bus roofs, not the road) - One parameter change in clustering (4 vs 8 connectivity) had more impact than any algorithm choice - Pedestrian vs bicyclist confusion is a representation problem, not a model problem — the confidence gap is identical across all feature sets - Tracking is where most systems actually fall apart: asymmetric lifecycle rules and covariance initialization matter more than the filter itself Ground Removal: 6 iterations, each failed for a different reason The sensor is fixed on a pole, tilted down at an intersection. No ego-motion. Iteration 1: Per-frame RANSAC on the full scene. Failed immediately. RANSAC locked onto a bus roof — more coplanar points in a local region than the actual road surface. A horizontal normal check (abs(normal_z) < 0.7) prevents wall-locking but can't prevent bus roof lock because a bus roof IS roughly horizontal. Also 6-7 seconds per frame. Iteration 2: Calibrate once on nearby points, flat z-threshold. RANSAC only within 10m of the sensor origin — ground dominates there (dense concentric scan lines, no car roofs). Get the ground normal, compute rotation via Rodrigues' formula to make ground horizontal. Simple z-threshold separates ground. Latency dropped from 6-7s to 5-10ms. But the flat threshold missed ground at far range where the road slopes. Iteration 3: Cartesian grid with local percentile. 1.5m cells, 10th-percentile z as local ground height. New problem: cells directly under buses have their percentile at the bus underside, not the road. Iteration 4: Multi-frame ground blanket. Accumulate ground estimates across frames hoping objects move and reveal the road. Only 1-5% of cells had valid estimates. Abandoned. Iteration 5: Plane equation extrapolation. Use expected_z(x,y) = -(nx·rx + ny·ry + d)/nz from the calibrated plane. Even a residual tilt of 0.01 in nx creates ~2m of height drift at 100m range. The expected height field extrapolated up to car roof level at far range. The plane is too sensitive to extrapolate. Iteration 6 (final): Polar grid + distance-adaptive deviation. Two key changes. First, replaced Cartesian with polar (r, θ) bins — 5m radial × 5° angular. This matches the LiDAR's radial scan pattern. The critical insight: a bus only covers a limited angular span. In a Cartesian grid, a bus can fill an entire cell. In a polar wedge, adjacent wedges still see the road beside the bus, keeping the ground percentile correct. Second, distance-adaptive threshold: allowed_deviation = min(0.5 + r × 0.08, 2.0). Tight near the sensor (rejects vehicles), relaxed at range (accommodates road slope). Also replaced np.percentile (O(N log N) full sort) with np.partition (O(N) quickselect) for ~3,600 polar bins. Latency: ~80ms. The real lesson: For fixed infrastructure sensors, the ground plane doesn't change between frames. Calibrate once, reuse forever. And for production, the best approach isn't RANSAC or grids — it's background subtraction. Accumulate a reference map of the empty scene. Per frame, compare each point against the reference. O(1) per point, ~1ms total. I couldn't do this (no empty-scene frames), but it's what you'd actually deploy. Clustering: One parameter change mattered more than the algorithm BEV projection to a 2D occupancy grid (0.15m cells). scipy.ndimage.label for connected components. DBSCAN was a non-starter — O(N²) on 140k points. Minutes per frame. The 4-vs-8 connectivity lesson. Started with 8-connectivity (diagonal neighbors count as connected). A car parked next to a wall had ONE diagonal cell bridging them → merged into one giant cluster → rejected by size filter → the car vanished from detection. Switching to 4-connectivity (shared edges only) fixed it. This one-line change had more impact than any algorithm choice in the entire pipeline. Morphological opening: tried, reverted. 3×3 erosion kernel to break bridges. But a pedestrian at range occupies 2×2 cells. The kernel erased them completely. Dilation can't restore what's gone. Per-cell height filter: tried, reverted. Required ≥0.3m z-range per occupied cell. But a car hatchback's trailing edge only has 2 scan rings with 0.1-0.2m z-spread. The filter punched holes in car outlines → connected components split the car into fragments. Height clipping at 3m: Originally 10m. Tree foliage above parked cars was bridging them in BEV — one giant cluster per tree canopy + everything below it. Tightening to 3m above ground solved this immediately. Classification: What the confusion matrices actually told me Random Forest, 100 trees, class_weight='balanced' (25:1 imbalance). Ablation across 7 feature sets. 9 features (bounding box + height): macro-F1 = 0.731 Confusion matrix immediately revealed two problems: - car→background: 18.8%. Sparse partial cars (p10 = 27 points) are geometrically identical to background clutter. - ped→bicyclist: 21.9%. These classes have 100% overlap on z_range, xy_spread, point count, and density. Adding PCA scattering: car→bg dropped from 18.8% to 16.4% Scattering = λ_min / λ_max. A car's points fill a 3D volume → three significant eigenvalues → moderate scattering. A wall's points lie on a flat surface → one eigenvalue near zero → low scattering. Linearity and planarity added only marginal gains on top of scattering. Scattering did almost all the heavy lifting. Adding 5-bin vertical layer fractions: ped→bike dropped from 16.9% to 15.0% A pedestrian has roughly uniform density from feet to head — each 20% height bin gets ~20% of points. A bicyclist has more points at wheel level and shoulder level with a gap in between. But here's the counterintuitive part: car→background actually DEGRADED from 16.8% to 17.8% with these features. The RF started using layer fractions to separate cars from background, but the signal was noisy for sparse clusters. Net gain was positive because ped/bike improved more than car/bg degraded. nn_dist_std (nearest-neighbor distance variance): directly targets car→bg. Car surface panels have organized, regular point spacing → low variance. Background clutter has irregular spacing → high variance. This is a feature the RF can't derive internally — it requires a KDTree computation per cluster. PCA yaw-invariance — discovered by accident. Same car scanned at 45° to sensor axes had nearly equal x_range and y_range, making it look square. xy_area inflated by ~2.4x. Root cause: ground alignment fixes pitch and roll, not yaw. Fix: 2×2 PCA eigendecomposition on the horizontal plane per cluster. Rotate xy to principal axes before measuring dimensions. All horizontal features become orientation-invariant. The confidence gap finding that changed my thinking. Across ALL feature sets (19, 23, 35), correct predictions averaged 0.87 confidence. Misclassifications averaged 0.60. The gap was 0.277±0.002 regardless of feature count. More features didn't make the model more certain about hard cases. The boundary between classes is fundamentally ambiguous in geometric feature space — a 27-point half-car genuinely looks like background clutter. This is the Bayes error rate of the representation, not a model limitation. Split/Merge: The feedback loop between tracking and clustering BEV connected components merges nearby pedestrians into one cluster. The combined shape has car-like dimensions. The RF classifies it as car. This is not a classifier failure — the features genuinely describe a car-shaped object. PCA gap-finding split: For suspicious clusters (z_range 1.0-2.2m, PCA linearity > 0.3, horizontal principal axis), project points onto the principal axis. Build a 30-bin histogram. Bins below 20% of mean density → gap between objects. Split there. Validate each piece (z_range > 0.5m, xy_spread 0.3-1.5m, aspect ratio > 0.8, min piece > 25% of max piece). Track-guided split (frames 3+): Once the tracker has confirmed positions, if a cluster contains 2+ confirmed tracks nearby, split along the axis connecting the track positions. This works even when the density gap has closed — two pedestrians walking closer together lose their point gap, but the tracker still knows they're separate objects. Temporal evidence overrides single-frame geometry. Where it still fails: Pedestrians in an L-shape or triangle. PCA gap-finding assumes collinear arrangement. Non-linear groups have no clear split axis. Tracking: Three design choices that actually mattered Kalman filter, constant velocity, 6-DOF. Hungarian assignment. 1. Mahalanobis over Euclidean. Euclidean + fixed 5m gate ignores the filter's own uncertainty. A new track with unknown velocity has large covariance → should accept matches from further away. An established track with tight covariance should be strict. Mahalanobis d² = y'S⁻¹y handles this naturally. Gated at d² > 7.81 (chi-squared 95%, 3 DOF). 2. Asymmetric track lifecycle. Initially same death rule for tentative and confirmed tracks. Problem: a false detection appears once, gets a tentative track, persists as a coasting ghost for 3 frames. A real object occluded for 2 frames loses its confirmed track. Fix: tentative tracks die after 1 miss (false alarms never repeat, so they die immediately). Confirmed tracks survive 3 misses (bridges temporary occlusion). Without this asymmetry, you're constantly choosing between ghost tracks and lost real tracks. 3. Covariance initialization. Originally P_pos=1.0, P_vel=5.0. P_pos=1.0 was too uncertain relative to R=0.3 (measurement noise). The filter overweighted predictions in early frames. P_vel=5.0 was too confident — velocity is completely unknown at birth. Changed to P_pos=0.5, P_vel=10.0. Early predictions became less jittery, convergence faster, new tracks stopped overshooting their first velocity estimate. One bug I'd fix: Cost matrix uses np.linalg.solve(S, y) (numerically correct). Kalman update uses np.linalg.inv(S) for the gain K = PH'S⁻¹ (sloppy). Same result for 3×3, but the inconsistency exists because I wrote them at different times. This project was less about building a pipeline and more about understanding where these systems actually break. Curious how others handle: - Ground removal for fixed infrastructure sensors — anyone using background subtraction in production? - Clustering edge cases (merged pedestrian groups, tree canopy bridging) - Tracking stability under occlusion with classical filters Happy to discuss. Full code + technical reports with ablation tables and failure analysis: https://github.com/bonsai89/lidar-perception-pipeline Context: perception engineer, previously at Toyota Technological Institute (camera-LiDAR-radar fusion, 5 papers) and TierIV, Japan (Autoware/ROS2 perception). Getting back into the field after a break.

1d ago

---

---

## Google News: "robotics"

**[National robotics push caught in delayed Trump-Xi meeting](https://www.politico.com/news/2026/04/09/national-robotics-trump-xi-china-00861918)**

Politico • 5h ago

---

**[Robot Density Surges in Europe, Asia, and Americas](https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas)**

Economies worldwide are prioritising the integration of factory robots, as automation becomes a critical tool for boosting productivity. In the global automation race, the Western European countries reached a record 267 robots per 10,000 employees in the manufacturing industry 2024 – ahead of North America with 204 units and Asia with 131 units. This is according to the World Robotics 2025 report, presented by the International Federation of Robotics (IFR).

International Federation of Robotics • 1d ago

---

**[Do people see robots as having race? New studies clash as humanoids enter the real world](https://www.scientificamerican.com/article/do-people-see-robots-as-having-race-new-studies-clash-as-humanoids-enter-the/)**

As humanoid robots enter the real world, new studies suggest that people project human racial biases onto them—but the research is divided on whether those biases persist outside the lab and in real-world interactions

Scientific American • 1d ago

---

**[Unitree to debut cheapest humanoid robot globally via Alibaba: sources](https://www.scmp.com/tech/article/3349489/chinas-unitree-debut-cheapest-humanoid-robot-globally-alibaba-site-sources)**

South China Morning Post • 6h ago

---

**[Xiaomi: Smartphone Cost Pressures Persist, But Robotics And Agentic AI Could Drive Long-Term Upside](https://seekingalpha.com/article/4889360-xiaomi-smartphone-cost-pressures-persist-but-robotics-and-agentic-ai-could-drive-long-term-upside)**

Xiaomi transitioning from smartphones to EV, physical robotics, and other AI initiatives can impact near-term revenue. Learn why XIACY stock is a strong buy.

Seeking Alpha • 16h ago

---

**[China to Deploy 100,000 Humanoid Robots—Will the West Ever Catch Up?](https://www.futura-sciences.com/en/china-to-deploy-100000-humanoid-robots-will-the-west-ever-catch-up_29061/)**

A technological ecosystem like no other Thanks to an exceptionally dense and innovative technological ecosystem, Beijing is about to deploy an impressive number of new humanoid robots in its factories. And let’s not forget: the country already held a dominant position in automation! For nearly a decade now, robotics has...

Futura, le média qui explore le monde • 23h ago

---

**[The next darlings of San Francisco’s AI real estate boom: Robots](https://sfstandard.com/2026/04/06/robotics-san-francisco-ai-boom/)**

Funding data and leasing activity show that companies using the groundbreaking tech on the physical world are having their moment.

The San Francisco Standard • 3d ago

---

**[From folding boxes to fixing vacuums, GEN-1 robotics model hits 99% reliability](https://arstechnica.com/ai/2026/04/generalists-new-physical-robotics-ai-brings-production-level-success-rates/)**

New model can respond to disruptions and figure out moves it wasn't trained for.

Ars Technica • 2d ago

---

**[Former UNH hockey star using robotics for shoulder replacements](https://www.wmur.com/article/former-unh-hockey-robotics-shoulder-4726/70956955)**

Hockey fans might remember former University of New Hampshire player Thomas Fortney, who tied a 2009 NCAA tournament game against North Dakota with a tenth of a second remaining in regulation.

WMUR • 1d ago

---

**[AI-powered robotic guide dog uses voice to guide visually impaired users in real time](https://interestingengineering.com/ai-robotics/talking-robotic-guide-dog-ai-navigation)**

AI-powered robotic guide dog uses voice to navigate and assist visually impaired users in real time.

Interesting Engineering • 14h ago

---

---

## YouTube Videos: "robotics"

**[New GEN 1 AI Robot Hits 3X Faster At 1,800+ Reps (AI NEWS)](https://www.youtube.com/watch?v=IgwL5-IH6gU)**

AIR CONDITIONED SHIRTS??: https://octocool.com Generalist AI's GEN-1 embodied foundation model achieves 99% success ...

📺 AI News

👁️ 5K • 👍 149 • 💬 17 • ⏱️ 8:04 • 6d ago

---

**[2026 Ultimate Robot Vacuum and Mop Comparison || Roborock, Eufy, Dreame, Narwal, Ecovacs, MOVA](https://www.youtube.com/watch?v=Pv9_2D_Xc5k)**

I tested every flagship robotic vacuum and mop from Roborock, Eufy, Dreame, Narwal, Ecovacs, and MOVA available in 2025 to ...

📺 The Hook Up

👁️ 9K • 👍 437 • 💬 98 • ⏱️ 26:12 • 20h ago

---

**[These NEW Human-Like AI Robots of 2026 Just SHOCKED the World!](https://www.youtube.com/watch?v=FOfieag6fi4)**

The world wasn't ready for what 2026 had in store — a wave of humanoid robots so advanced, so eerily lifelike, that the line ...

📺 The AI Nexus

👁️ 8K • 👍 259 • 💬 18 • ⏱️ 16:42 • 3d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=kxSunP8Cf9g)**

📺 Robot Julie 

👁️ 3K • 👍 46 • ⏱️ 0:22 • 11h ago

---

**[Are AI soldiers about to take over the battlefield? | DW News](https://www.youtube.com/watch?v=q83LtZza5eA)**

US startup Foundation is developing humanoid robots for military use. The goal is for its Phantom model to identify targets and ...

📺 DW News

👁️ 75K • 👍 549 • 💬 101 • ⏱️ 1:22 • 3d ago

---

**[Inside the World&#39;s Smartest Robot Brain](https://www.youtube.com/watch?v=2mrGMMmrVNE)**

Welch Labs Book: https://www.welchlabs.com/resources/ai-book-ezrzm-msrmc Book & VLA Poster Bundle: ...

📺 Welch Labs

👁️ 97K • 👍 5K • 💬 234 • ⏱️ 35:02 • 4d ago

---

**[Joe Rogan Watches Soldier Test INSANE Robotic Legs 🤖🦿💥 #Shorts](https://www.youtube.com/watch?v=zbopLtVrukQ)**

Joe Rogan Watches Soldier Test INSANE Robotic Legs #Shorts This is the future of the battlefield. A soldier straps on ...

📺 Silent Sentry

👁️ 2.2M • 👍 28K • 💬 617 • ⏱️ 0:17 • 5d ago

---

**[Engineering the Experience – How Do Robots Work on a Cruise Ship?](https://www.youtube.com/watch?v=AezeHLJedYc)**

How do robots work on a cruise ship? In this episode of Engineering the Experience, Royal Caribbean explores the robotics and ...

📺 Royal Caribbean

👁️ 8K • 👍 207 • 💬 17 • ⏱️ 4:51 • 6d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=4KM9QWO5__Q)**

📺 Robot Julie 

👁️ 27K • 👍 126 • 💬 1 • ⏱️ 0:23 • 2d ago

---

**[I Spent 100 Hours In China&#39;s Robot City](https://www.youtube.com/watch?v=PXGK_MFShXU)**

I spent 100 hours in the world's most futuristic city! WATCH MORE videos we filmed in China ▸ https://youtu.be/elF_v9sukWU ...

📺 Hafu Go

👁️ 779K • 👍 7K • 💬 277 • ⏱️ 25:46 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

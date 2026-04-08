---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-08T13:22:31.984571+00:00'
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

**Last Updated:** April 08, 2026 at 13:22 UTC  
**HTML Version:** [robotics.html](https://peekdeck.ruidiao.dev/robotics.html)

---

## Table of Contents

1. [Reddit: r/robotics](#reddit-rrobotics)
2. [Google News: "robotics"](#google-news-robotics)
3. [YouTube Videos: "robotics"](#youtube-videos-robotics)

---

## Reddit: r/robotics

**[LeRobot (Hugging Face) just released "Unfolding Robotics", an open-source recipe for teaching a robot to fold your clothes](https://www.reddit.com/r/robotics/comments/1sfnve9/lerobot_hugging_face_just_released_unfolding/)**

"The blog walks through the entire process: → Which robot, cameras, and teleoperation setup we used → How to gather high-quality demonstrations → Which model architecture and training recipe performed best → What we learned, and what we’d do differently Everything is open-source and ready to use in LeRobot v0.5.1." Unfolding Robotics: The Open-Source Recipe for Teaching a Robot to Fold Your Clothes: https://huggingface.co/spaces/lerobot/robot-folding From LeRobot on 𝕏: https://x.com/LeRobotHF/status/2041542790610297259

3h ago

---

**[End-to-End LiDAR Perception Pipeline from Scratch: Almost none of the real problems were about the model](https://www.reddit.com/r/robotics/comments/1sfq6m6/endtoend_lidar_perception_pipeline_from_scratch/)**

I built an end-to-end LiDAR perception pipeline on 128-beam infrastructure data (~184k points/frame, 10 sequential frames, busy urban intersection). The surprising part: almost none of the real problems were about the model. Ground removal, clustering connectivity, feature representation, track lifecycle management — these are where the system actually broke. Repeatedly. Full code + reports: https://github.com/bonsai89/lidar-perception-pipeline TL;DR - Ground removal fails in unexpected ways (RANSAC locks onto bus roofs, not the road) - One parameter change in clustering (4 vs 8 connectivity) had more impact than any algorithm choice - Pedestrian vs bicyclist confusion is a representation problem, not a model problem — the confidence gap is identical across all feature sets - Tracking is where most systems actually fall apart: asymmetric lifecycle rules and covariance initialization matter more than the filter itself Ground Removal: 6 iterations, each failed for a different reason The sensor is fixed on a pole, tilted down at an intersection. No ego-motion. Iteration 1: Per-frame RANSAC on the full scene. Failed immediately. RANSAC locked onto a bus roof — more coplanar points in a local region than the actual road surface. A horizontal normal check (abs(normal_z) < 0.7) prevents wall-locking but can't prevent bus roof lock because a bus roof IS roughly horizontal. Also 6-7 seconds per frame. Iteration 2: Calibrate once on nearby points, flat z-threshold. RANSAC only within 10m of the sensor origin — ground dominates there (dense concentric scan lines, no car roofs). Get the ground normal, compute rotation via Rodrigues' formula to make ground horizontal. Simple z-threshold separates ground. Latency dropped from 6-7s to 5-10ms. But the flat threshold missed ground at far range where the road slopes. Iteration 3: Cartesian grid with local percentile. 1.5m cells, 10th-percentile z as local ground height. New problem: cells directly under buses have their percentile at the bus underside, not the road. Iteration 4: Multi-frame ground blanket. Accumulate ground estimates across frames hoping objects move and reveal the road. Only 1-5% of cells had valid estimates. Abandoned. Iteration 5: Plane equation extrapolation. Use expected_z(x,y) = -(nx·rx + ny·ry + d)/nz from the calibrated plane. Even a residual tilt of 0.01 in nx creates ~2m of height drift at 100m range. The expected height field extrapolated up to car roof level at far range. The plane is too sensitive to extrapolate. Iteration 6 (final): Polar grid + distance-adaptive deviation. Two key changes. First, replaced Cartesian with polar (r, θ) bins — 5m radial × 5° angular. This matches the LiDAR's radial scan pattern. The critical insight: a bus only covers a limited angular span. In a Cartesian grid, a bus can fill an entire cell. In a polar wedge, adjacent wedges still see the road beside the bus, keeping the ground percentile correct. Second, distance-adaptive threshold: allowed_deviation = min(0.5 + r × 0.08, 2.0). Tight near the sensor (rejects vehicles), relaxed at range (accommodates road slope). Also replaced np.percentile (O(N log N) full sort) with np.partition (O(N) quickselect) for ~3,600 polar bins. Latency: ~80ms. The real lesson: For fixed infrastructure sensors, the ground plane doesn't change between frames. Calibrate once, reuse forever. And for production, the best approach isn't RANSAC or grids — it's background subtraction. Accumulate a reference map of the empty scene. Per frame, compare each point against the reference. O(1) per point, ~1ms total. I couldn't do this (no empty-scene frames), but it's what you'd actually deploy. Clustering: One parameter change mattered more than the algorithm BEV projection to a 2D occupancy grid (0.15m cells). scipy.ndimage.label for connected components. DBSCAN was a non-starter — O(N²) on 140k points. Minutes per frame. The 4-vs-8 connectivity lesson. Started with 8-connectivity (diagonal neighbors count as connected). A car parked next to a wall had ONE diagonal cell bridging them → merged into one giant cluster → rejected by size filter → the car vanished from detection. Switching to 4-connectivity (shared edges only) fixed it. This one-line change had more impact than any algorithm choice in the entire pipeline. Morphological opening: tried, reverted. 3×3 erosion kernel to break bridges. But a pedestrian at range occupies 2×2 cells. The kernel erased them completely. Dilation can't restore what's gone. Per-cell height filter: tried, reverted. Required ≥0.3m z-range per occupied cell. But a car hatchback's trailing edge only has 2 scan rings with 0.1-0.2m z-spread. The filter punched holes in car outlines → connected components split the car into fragments. Height clipping at 3m: Originally 10m. Tree foliage above parked cars was bridging them in BEV — one giant cluster per tree canopy + everything below it. Tightening to 3m above ground solved this immediately. Classification: What the confusion matrices actually told me Random Forest, 100 trees, class_weight='balanced' (25:1 imbalance). Ablation across 7 feature sets. 9 features (bounding box + height): macro-F1 = 0.731 Confusion matrix immediately revealed two problems: - car→background: 18.8%. Sparse partial cars (p10 = 27 points) are geometrically identical to background clutter. - ped→bicyclist: 21.9%. These classes have 100% overlap on z_range, xy_spread, point count, and density. Adding PCA scattering: car→bg dropped from 18.8% to 16.4% Scattering = λ_min / λ_max. A car's points fill a 3D volume → three significant eigenvalues → moderate scattering. A wall's points lie on a flat surface → one eigenvalue near zero → low scattering. Linearity and planarity added only marginal gains on top of scattering. Scattering did almost all the heavy lifting. Adding 5-bin vertical layer fractions: ped→bike dropped from 16.9% to 15.0% A pedestrian has roughly uniform density from feet to head — each 20% height bin gets ~20% of points. A bicyclist has more points at wheel level and shoulder level with a gap in between. But here's the counterintuitive part: car→background actually DEGRADED from 16.8% to 17.8% with these features. The RF started using layer fractions to separate cars from background, but the signal was noisy for sparse clusters. Net gain was positive because ped/bike improved more than car/bg degraded. nn_dist_std (nearest-neighbor distance variance): directly targets car→bg. Car surface panels have organized, regular point spacing → low variance. Background clutter has irregular spacing → high variance. This is a feature the RF can't derive internally — it requires a KDTree computation per cluster. PCA yaw-invariance — discovered by accident. Same car scanned at 45° to sensor axes had nearly equal x_range and y_range, making it look square. xy_area inflated by ~2.4x. Root cause: ground alignment fixes pitch and roll, not yaw. Fix: 2×2 PCA eigendecomposition on the horizontal plane per cluster. Rotate xy to principal axes before measuring dimensions. All horizontal features become orientation-invariant. The confidence gap finding that changed my thinking. Across ALL feature sets (19, 23, 35), correct predictions averaged 0.87 confidence. Misclassifications averaged 0.60. The gap was 0.277±0.002 regardless of feature count. More features didn't make the model more certain about hard cases. The boundary between classes is fundamentally ambiguous in geometric feature space — a 27-point half-car genuinely looks like background clutter. This is the Bayes error rate of the representation, not a model limitation. Split/Merge: The feedback loop between tracking and clustering BEV connected components merges nearby pedestrians into one cluster. The combined shape has car-like dimensions. The RF classifies it as car. This is not a classifier failure — the features genuinely describe a car-shaped object. PCA gap-finding split: For suspicious clusters (z_range 1.0-2.2m, PCA linearity > 0.3, horizontal principal axis), project points onto the principal axis. Build a 30-bin histogram. Bins below 20% of mean density → gap between objects. Split there. Validate each piece (z_range > 0.5m, xy_spread 0.3-1.5m, aspect ratio > 0.8, min piece > 25% of max piece). Track-guided split (frames 3+): Once the tracker has confirmed positions, if a cluster contains 2+ confirmed tracks nearby, split along the axis connecting the track positions. This works even when the density gap has closed — two pedestrians walking closer together lose their point gap, but the tracker still knows they're separate objects. Temporal evidence overrides single-frame geometry. Where it still fails: Pedestrians in an L-shape or triangle. PCA gap-finding assumes collinear arrangement. Non-linear groups have no clear split axis. Tracking: Three design choices that actually mattered Kalman filter, constant velocity, 6-DOF. Hungarian assignment. 1. Mahalanobis over Euclidean. Euclidean + fixed 5m gate ignores the filter's own uncertainty. A new track with unknown velocity has large covariance → should accept matches from further away. An established track with tight covariance should be strict. Mahalanobis d² = y'S⁻¹y handles this naturally. Gated at d² > 7.81 (chi-squared 95%, 3 DOF). 2. Asymmetric track lifecycle. Initially same death rule for tentative and confirmed tracks. Problem: a false detection appears once, gets a tentative track, persists as a coasting ghost for 3 frames. A real object occluded for 2 frames loses its confirmed track. Fix: tentative tracks die after 1 miss (false alarms never repeat, so they die immediately). Confirmed tracks survive 3 misses (bridges temporary occlusion). Without this asymmetry, you're constantly choosing between ghost tracks and lost real tracks. 3. Covariance initialization. Originally P_pos=1.0, P_vel=5.0. P_pos=1.0 was too uncertain relative to R=0.3 (measurement noise). The filter overweighted predictions in early frames. P_vel=5.0 was too confident — velocity is completely unknown at birth. Changed to P_pos=0.5, P_vel=10.0. Early predictions became less jittery, convergence faster, new tracks stopped overshooting their first velocity estimate. One bug I'd fix: Cost matrix uses np.linalg.solve(S, y) (numerically correct). Kalman update uses np.linalg.inv(S) for the gain K = PH'S⁻¹ (sloppy). Same result for 3×3, but the inconsistency exists because I wrote them at different times. This project was less about building a pipeline and more about understanding where these systems actually break. Curious how others handle: - Ground removal for fixed infrastructure sensors — anyone using background subtraction in production? - Clustering edge cases (merged pedestrian groups, tree canopy bridging) - Tracking stability under occlusion with classical filters Happy to discuss. Full code + technical reports with ablation tables and failure analysis: https://github.com/bonsai89/lidar-perception-pipeline Context: perception engineer, previously at Toyota Technological Institute (camera-LiDAR-radar fusion, 5 papers) and TierIV, Japan (Autoware/ROS2 perception). Getting back into the field after a break.

1h ago

---

**[6 axis robot](https://www.reddit.com/r/robotics/comments/1sff1il/6_axis_robot/)**

11h ago

---

**[Torobo Humanoid Robot by Tokyo Robotics](https://www.reddit.com/r/robotics/comments/1sf806y/torobo_humanoid_robot_by_tokyo_robotics/)**

Torobo Humanoid Robot by Tokyo Robotics that looks like Atlas by Boston Dynamics. They recently switched their Torobo robot to become bipedal.

16h ago

---

**[Maximo’s AI-powered robots have installed over 100MW of solar panels, bringing automation to energy projects.](https://www.reddit.com/r/robotics/comments/1serirr/maximos_aipowered_robots_have_installed_over/)**

From NVIDIA Robotics on 𝕏: https://x.com/NVIDIARobotics/status/2041349314262495265 NVIDIA blog: https://blogs.nvidia.com/blog/national-robotics-week-2026/#maximo

1d ago

---

**[At what point do you stop adding complexity to a robot design?](https://www.reddit.com/r/robotics/comments/1sfnuzi/at_what_point_do_you_stop_adding_complexity_to_a/)**

I’ve been working in industrial robotics (mostly integration and deployment) for about 5 years, but I’m currently building a small differential drive robot on my own outside of work. What’s interesting is I’m running into a problem I don’t usually feel as strongly on the job: knowing when to stop adding “improvements.” What started as a simple platform has gradually grown — I added encoder feedback, tuned a PID loop for motor control, redesigned parts for easier mounting, and now I’m considering splitting responsibilities across two controllers to better handle sensor input. None of these decisions are unreasonable on their own, but taken together I’m starting to wonder if I’m overengineering something that was supposed to be simple and quick to iterate. In industry projects, there are usually clearer constraints (budget, deadlines, client requirements), so the line is easier to draw. On a personal build, that line feels a lot fuzzier. For those of you with experience building robots outside of structured projects — how do you decide when something is “good enough” to stop iterating? Do you bias toward simplicity early on, or design for scalability from the start? Curious how others approach this in practice.

3h ago

---

**[Robots fixing robots](https://www.reddit.com/r/robotics/comments/1sf1ihh/robots_fixing_robots/)**

Generalist just dropped GEN-1, the first general-purpose robot Al that hits 99% success rate on tasks where older models managed only 64%. The wild part? It didn't learn from robots, it learned from humans wearing cameras doing everyday tasks. That data transfers to robots with minimal retraining.When things go wrong, it improvises regrasping, switching hands, adapting on the fly. No explicit programming.

20h ago

---

**[Standard PID vs. Reinforcement Learning on a degrading robotic joint (Wait for the second half).](https://www.reddit.com/r/robotics/comments/1sfnlol/standard_pid_vs_reinforcement_learning_on_a/)**

My project partner and I are wrapping up a control middleware (ADAPT), and we wanted to share a crazy emergent behaviour our RL agent learned during a stress test. The Setup: We are running an inverted pendulum simulation, but we cranked simulated gearbox backlash and friction to absolute maximum to mimic a worn-out, dying motor. First Half (Standard PID): The standard controller tries to hold the joint at exactly 0.0 error. It falls into the mechanical deadband, over-corrects, and chatters violently. On physical hardware, this high-frequency vibration shreds the remaining gear teeth and overheats the actuator. Second Half (Vectra AI): We switch to our RL agent. It realizes holding absolute zero will burn out the motor. So, it intentionally introduces a 0.4-degree "limit cycle." It sacrifices a fraction of a degree of absolute precision to create a slight, predictable swing, keeping the gears in tension and riding the momentum through the slop. It essentially taught itself an Autonomous Degradation-Survival Strategy. We are doing a 72-hour sprint right now to see how this translates to different kinematics. If anyone is working with a custom URDF (especially with known mechanical slop), DM it to me. We want to run it through our pipeline and see if our math breaks.

4h ago

---

**[TWIST2 implementation in MjLab](https://www.reddit.com/r/robotics/comments/1sf0qzn/twist2_implementation_in_mjlab/)**

Worried about EoL IsaacGym and tired of setting up IsaacLab? I ported TWIST2 general motion tracking controller to MjLab that supports uv so really one click training/testing. It also uses MjWarp as the physics engine which IMO is better than physx which the Isaac frameworks defaulted to in the past. GitHub: lzyang2000/twist2_mjlab Link in comments, credits to original authors of MjLab and TWIST2

21h ago

---

**[Discussing how the future of exoskeletons will affect the average human’s speed and how far away from getting to Olympic athlete speeds](https://www.reddit.com/r/robotics/comments/1sfkgm1/discussing_how_the_future_of_exoskeletons_will/)**

So this is more of a questions really, but how far are we from building exoskeletons that enable the average human to run at speeds clocking in at 20+ miles per hour. I am aware that one of the best out there is the hypershell x ultra which after me watching many unbiased reviews and videos on it, can make the average human run from 13 mph to 17 and even one at 19. So that being said, how far are we from making an exoskeleton that can enable average humans to clock in at speeds above 23-24 mph?

7h ago

---

---

## Google News: "robotics"

**[From folding boxes to fixing vacuums, GEN-1 robotics model hits 99% reliability](https://arstechnica.com/ai/2026/04/generalists-new-physical-robotics-ai-brings-production-level-success-rates/)**

New model can respond to disruptions and figure out moves it wasn't trained for.

arstechnica.com • 1d ago

---

**[Former UNH hockey star using robotics for shoulder replacements](https://www.wmur.com/article/former-unh-hockey-robotics-shoulder-4726/70956955)**

Hockey fans might remember former University of New Hampshire player Thomas Fortney, who tied a 2009 NCAA tournament game against North Dakota with a tenth of a second remaining in regulation.

WMUR • 14h ago

---

**[HII Teams with GrayMatter Robotics to Integrate Physical AI into Manned and Unmanned Shipbuilding](https://hii.com/news/hii-teams-with-graymatter-robotics-to-integrate-physical-ai-into-manned-and-unmanned-shipbuilding/)**

CARSON, Calif., (April 6, 2026) — HII (NYSE: HII) and GrayMatter Robotics (GMR) signed a memorandum of understanding (MOU) today to explore the integration of GMR’s Physical AI into shipbuilding operations that could accelerate throughput, strengthen the maritime industrial base, and augment the shipbuilding workforce. This will include bringing autonomous surface preparation, coating, and inspection

HII • 1d ago

---

**[Robot Maker Kuka Eyes US, Asia as Europe Lags Behind on AI](https://www.bloomberg.com/news/articles/2026-04-08/robot-maker-kuka-eyes-us-asia-as-europe-s-factories-lag-on-ai)**

Bloomberg.com • 3h ago

---

**[‘No one’s raising their hand’: Japan’s labor crisis is making the case for robots taking the jobs you don’t want](https://fortune.com/2026/04/06/japan-labor-shortage-robots-ai-robotics-humanoid/)**

Japan is looking to become the dominant source of robotics by 2040, expedited by an aging population and a growing need for labor.

Fortune • 1d ago

---

**[Wearable robots improve coordination between pairs of violin players](https://techxplore.com/news/2026-04-wearable-robots-pairs-violin-players.html)**

Tech Xplore • 20h ago

---

**[Kraken Robotics Demonstrates KATFISH Autonomous Launch and Recovery from SEFINE USV](https://www.navalnews.com/naval-news/2026/04/kraken-robotics-demonstrates-katfish-autonomous-launch-and-recovery-from-sefine-usv/)**

Kraken announces the successful integration and demonstration of its KATFISH towed synthetic aperture sonar and autonomous launch and recovery system (LARS) from SEFINE’s RD-22 unmanned surface vessel

navalnews.com • 1d ago

---

**[Optimus time: Tesla makes big move in Fremont for global robotics hub](https://www.bizjournals.com/sanfrancisco/news/2026/04/06/tesla-fremont-optimus-robotics-factory.html)**

bizjournals.com • 1d ago

---

**[US: Humanoid robot Alex evolves with real-world capabilities ahead of public debut](https://interestingengineering.com/ai-robotics/us-alex-humanoid-robot)**

IHMC to showcase Alex, a next-gen humanoid robot built for real-world tasks, at its April 10 open house with public demos.

Interesting Engineering • 1d ago

---

**[Do people see robots as having race? New studies clash as humanoids enter the real world](https://www.scientificamerican.com/article/do-people-see-robots-as-having-race-new-studies-clash-as-humanoids-enter-the/)**

As humanoid robots enter the real world, new studies suggest that people project human racial biases onto them—but the research is divided on whether those biases persist outside the lab and in real-world interactions

Scientific American • 2h ago

---

---

## YouTube Videos: "robotics"

**[Shawn Ryan Tests a Real Humanoid Robot](https://www.youtube.com/watch?v=HWq9cFhTvvQ)**

Shawn Ryan gets hands-on with a real humanoid robot powered entirely by AI. In this clip, we break down how this robot sees, ...

📺 Shawn Ryan Show

👁️ 1.2M • 👍 42K • 💬 7K • ⏱️ 8:48 • 6d ago

---

**[Yaskawa&#39;s Humanoid Robot Gets Legs and Better AI #robotics #humanoidrobot #robot](https://www.youtube.com/watch?v=Fmi7Fcksz-4)**

Japan's Torobo humanoid robot is moving toward full autonomy with its new legs. Tokyo Robotics just shared footage of its ...

📺 Kalil 4.0

👁️ 2K • 👍 72 • 💬 5 • ⏱️ 0:46 • 17h ago

---

**[Are AI soldiers about to take over the battlefield? | DW News](https://www.youtube.com/watch?v=q83LtZza5eA)**

US startup Foundation is developing humanoid robots for military use. The goal is for its Phantom model to identify targets and ...

📺 DW News

👁️ 70K • 👍 540 • 💬 93 • ⏱️ 1:22 • 2d ago

---

**[New GEN 1 AI Robot Hits 3X Faster At 1,800+ Reps (AI NEWS)](https://www.youtube.com/watch?v=IgwL5-IH6gU)**

AIR CONDITIONED SHIRTS??: https://octocool.com Generalist AI's GEN-1 embodied foundation model achieves 99% success ...

📺 AI News

👁️ 5K • 👍 145 • 💬 17 • ⏱️ 8:04 • 5d ago

---

**[Robot Alchemic Drive Review](https://www.youtube.com/watch?v=a8pbzBTNVOo)**

Today, we're reviewing Robot Alchemic Drive... one of, if not the MOST unique mech games ever made. In recent years, the game ...

📺 Jarboe Gaming

👁️ 5K • 👍 483 • 💬 99 • ⏱️ 18:45 • 21h ago

---

**[These NEW Human-Like AI Robots of 2026 Just SHOCKED the World!](https://www.youtube.com/watch?v=FOfieag6fi4)**

The world wasn't ready for what 2026 had in store — a wave of humanoid robots so advanced, so eerily lifelike, that the line ...

📺 The AI Nexus

👁️ 7K • 👍 243 • 💬 16 • ⏱️ 16:42 • 2d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=4KM9QWO5__Q)**

📺 Robot Julie 

👁️ 27K • 👍 116 • 💬 1 • ⏱️ 0:23 • 1d ago

---

**[Joe Rogan Watches Soldier Test INSANE Robotic Legs 🤖🦿💥 #Shorts](https://www.youtube.com/watch?v=zbopLtVrukQ)**

Joe Rogan Watches Soldier Test INSANE Robotic Legs #Shorts This is the future of the battlefield. A soldier straps on ...

📺 Silent Sentry

👁️ 1.8M • 👍 23K • 💬 555 • ⏱️ 0:17 • 4d ago

---

**[I broke a robot in China](https://www.youtube.com/watch?v=7U3vjVfwChc)**

China is leading the world in humanoid robot shipments. Powered by artificial intelligence, these machines are setting new ...

📺 CGTN

👁️ 33K • 👍 292 • 💬 60 • ⏱️ 1:54 • 6d ago

---

**[I Tested Robot Legs](https://www.youtube.com/watch?v=o1MU4GypD2I)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha Become a Member: ...

📺 Sambucha

👁️ 97K • 👍 7K • 💬 238 • ⏱️ 0:51 • 20h ago

---

---

*Generated by PeekDeck - A glance is all you need*

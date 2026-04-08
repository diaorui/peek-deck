---
title: Robotics Dashboard
description: Robotics research and industry news
category: tech
page_id: robotics
updated: '2026-04-08T17:40:22.144727+00:00'
url: https://peekdeck.ruidiao.dev/robotics.html
markdown_url: https://peekdeck.ruidiao.dev/robotics.md
widgets: 3
data_types:
- news
- social
- videos
---

# Robotics Dashboard

Robotics research and industry news

**Last Updated:** April 08, 2026 at 17:40 UTC  
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

8h ago

---

**[End-to-End LiDAR Perception Pipeline from Scratch: Almost none of the real problems were about the model](https://www.reddit.com/r/robotics/comments/1sfq6m6/endtoend_lidar_perception_pipeline_from_scratch/)**

I built an end-to-end LiDAR perception pipeline on 128-beam infrastructure data (~184k points/frame, 10 sequential frames, busy urban intersection). The surprising part: almost none of the real problems were about the model. Ground removal, clustering connectivity, feature representation, track lifecycle management — these are where the system actually broke. Repeatedly. Full code + reports: https://github.com/bonsai89/lidar-perception-pipeline TL;DR - Ground removal fails in unexpected ways (RANSAC locks onto bus roofs, not the road) - One parameter change in clustering (4 vs 8 connectivity) had more impact than any algorithm choice - Pedestrian vs bicyclist confusion is a representation problem, not a model problem — the confidence gap is identical across all feature sets - Tracking is where most systems actually fall apart: asymmetric lifecycle rules and covariance initialization matter more than the filter itself Ground Removal: 6 iterations, each failed for a different reason The sensor is fixed on a pole, tilted down at an intersection. No ego-motion. Iteration 1: Per-frame RANSAC on the full scene. Failed immediately. RANSAC locked onto a bus roof — more coplanar points in a local region than the actual road surface. A horizontal normal check (abs(normal_z) < 0.7) prevents wall-locking but can't prevent bus roof lock because a bus roof IS roughly horizontal. Also 6-7 seconds per frame. Iteration 2: Calibrate once on nearby points, flat z-threshold. RANSAC only within 10m of the sensor origin — ground dominates there (dense concentric scan lines, no car roofs). Get the ground normal, compute rotation via Rodrigues' formula to make ground horizontal. Simple z-threshold separates ground. Latency dropped from 6-7s to 5-10ms. But the flat threshold missed ground at far range where the road slopes. Iteration 3: Cartesian grid with local percentile. 1.5m cells, 10th-percentile z as local ground height. New problem: cells directly under buses have their percentile at the bus underside, not the road. Iteration 4: Multi-frame ground blanket. Accumulate ground estimates across frames hoping objects move and reveal the road. Only 1-5% of cells had valid estimates. Abandoned. Iteration 5: Plane equation extrapolation. Use expected_z(x,y) = -(nx·rx + ny·ry + d)/nz from the calibrated plane. Even a residual tilt of 0.01 in nx creates ~2m of height drift at 100m range. The expected height field extrapolated up to car roof level at far range. The plane is too sensitive to extrapolate. Iteration 6 (final): Polar grid + distance-adaptive deviation. Two key changes. First, replaced Cartesian with polar (r, θ) bins — 5m radial × 5° angular. This matches the LiDAR's radial scan pattern. The critical insight: a bus only covers a limited angular span. In a Cartesian grid, a bus can fill an entire cell. In a polar wedge, adjacent wedges still see the road beside the bus, keeping the ground percentile correct. Second, distance-adaptive threshold: allowed_deviation = min(0.5 + r × 0.08, 2.0). Tight near the sensor (rejects vehicles), relaxed at range (accommodates road slope). Also replaced np.percentile (O(N log N) full sort) with np.partition (O(N) quickselect) for ~3,600 polar bins. Latency: ~80ms. The real lesson: For fixed infrastructure sensors, the ground plane doesn't change between frames. Calibrate once, reuse forever. And for production, the best approach isn't RANSAC or grids — it's background subtraction. Accumulate a reference map of the empty scene. Per frame, compare each point against the reference. O(1) per point, ~1ms total. I couldn't do this (no empty-scene frames), but it's what you'd actually deploy. Clustering: One parameter change mattered more than the algorithm BEV projection to a 2D occupancy grid (0.15m cells). scipy.ndimage.label for connected components. DBSCAN was a non-starter — O(N²) on 140k points. Minutes per frame. The 4-vs-8 connectivity lesson. Started with 8-connectivity (diagonal neighbors count as connected). A car parked next to a wall had ONE diagonal cell bridging them → merged into one giant cluster → rejected by size filter → the car vanished from detection. Switching to 4-connectivity (shared edges only) fixed it. This one-line change had more impact than any algorithm choice in the entire pipeline. Morphological opening: tried, reverted. 3×3 erosion kernel to break bridges. But a pedestrian at range occupies 2×2 cells. The kernel erased them completely. Dilation can't restore what's gone. Per-cell height filter: tried, reverted. Required ≥0.3m z-range per occupied cell. But a car hatchback's trailing edge only has 2 scan rings with 0.1-0.2m z-spread. The filter punched holes in car outlines → connected components split the car into fragments. Height clipping at 3m: Originally 10m. Tree foliage above parked cars was bridging them in BEV — one giant cluster per tree canopy + everything below it. Tightening to 3m above ground solved this immediately. Classification: What the confusion matrices actually told me Random Forest, 100 trees, class_weight='balanced' (25:1 imbalance). Ablation across 7 feature sets. 9 features (bounding box + height): macro-F1 = 0.731 Confusion matrix immediately revealed two problems: - car→background: 18.8%. Sparse partial cars (p10 = 27 points) are geometrically identical to background clutter. - ped→bicyclist: 21.9%. These classes have 100% overlap on z_range, xy_spread, point count, and density. Adding PCA scattering: car→bg dropped from 18.8% to 16.4% Scattering = λ_min / λ_max. A car's points fill a 3D volume → three significant eigenvalues → moderate scattering. A wall's points lie on a flat surface → one eigenvalue near zero → low scattering. Linearity and planarity added only marginal gains on top of scattering. Scattering did almost all the heavy lifting. Adding 5-bin vertical layer fractions: ped→bike dropped from 16.9% to 15.0% A pedestrian has roughly uniform density from feet to head — each 20% height bin gets ~20% of points. A bicyclist has more points at wheel level and shoulder level with a gap in between. But here's the counterintuitive part: car→background actually DEGRADED from 16.8% to 17.8% with these features. The RF started using layer fractions to separate cars from background, but the signal was noisy for sparse clusters. Net gain was positive because ped/bike improved more than car/bg degraded. nn_dist_std (nearest-neighbor distance variance): directly targets car→bg. Car surface panels have organized, regular point spacing → low variance. Background clutter has irregular spacing → high variance. This is a feature the RF can't derive internally — it requires a KDTree computation per cluster. PCA yaw-invariance — discovered by accident. Same car scanned at 45° to sensor axes had nearly equal x_range and y_range, making it look square. xy_area inflated by ~2.4x. Root cause: ground alignment fixes pitch and roll, not yaw. Fix: 2×2 PCA eigendecomposition on the horizontal plane per cluster. Rotate xy to principal axes before measuring dimensions. All horizontal features become orientation-invariant. The confidence gap finding that changed my thinking. Across ALL feature sets (19, 23, 35), correct predictions averaged 0.87 confidence. Misclassifications averaged 0.60. The gap was 0.277±0.002 regardless of feature count. More features didn't make the model more certain about hard cases. The boundary between classes is fundamentally ambiguous in geometric feature space — a 27-point half-car genuinely looks like background clutter. This is the Bayes error rate of the representation, not a model limitation. Split/Merge: The feedback loop between tracking and clustering BEV connected components merges nearby pedestrians into one cluster. The combined shape has car-like dimensions. The RF classifies it as car. This is not a classifier failure — the features genuinely describe a car-shaped object. PCA gap-finding split: For suspicious clusters (z_range 1.0-2.2m, PCA linearity > 0.3, horizontal principal axis), project points onto the principal axis. Build a 30-bin histogram. Bins below 20% of mean density → gap between objects. Split there. Validate each piece (z_range > 0.5m, xy_spread 0.3-1.5m, aspect ratio > 0.8, min piece > 25% of max piece). Track-guided split (frames 3+): Once the tracker has confirmed positions, if a cluster contains 2+ confirmed tracks nearby, split along the axis connecting the track positions. This works even when the density gap has closed — two pedestrians walking closer together lose their point gap, but the tracker still knows they're separate objects. Temporal evidence overrides single-frame geometry. Where it still fails: Pedestrians in an L-shape or triangle. PCA gap-finding assumes collinear arrangement. Non-linear groups have no clear split axis. Tracking: Three design choices that actually mattered Kalman filter, constant velocity, 6-DOF. Hungarian assignment. 1. Mahalanobis over Euclidean. Euclidean + fixed 5m gate ignores the filter's own uncertainty. A new track with unknown velocity has large covariance → should accept matches from further away. An established track with tight covariance should be strict. Mahalanobis d² = y'S⁻¹y handles this naturally. Gated at d² > 7.81 (chi-squared 95%, 3 DOF). 2. Asymmetric track lifecycle. Initially same death rule for tentative and confirmed tracks. Problem: a false detection appears once, gets a tentative track, persists as a coasting ghost for 3 frames. A real object occluded for 2 frames loses its confirmed track. Fix: tentative tracks die after 1 miss (false alarms never repeat, so they die immediately). Confirmed tracks survive 3 misses (bridges temporary occlusion). Without this asymmetry, you're constantly choosing between ghost tracks and lost real tracks. 3. Covariance initialization. Originally P_pos=1.0, P_vel=5.0. P_pos=1.0 was too uncertain relative to R=0.3 (measurement noise). The filter overweighted predictions in early frames. P_vel=5.0 was too confident — velocity is completely unknown at birth. Changed to P_pos=0.5, P_vel=10.0. Early predictions became less jittery, convergence faster, new tracks stopped overshooting their first velocity estimate. One bug I'd fix: Cost matrix uses np.linalg.solve(S, y) (numerically correct). Kalman update uses np.linalg.inv(S) for the gain K = PH'S⁻¹ (sloppy). Same result for 3×3, but the inconsistency exists because I wrote them at different times. This project was less about building a pipeline and more about understanding where these systems actually break. Curious how others handle: - Ground removal for fixed infrastructure sensors — anyone using background subtraction in production? - Clustering edge cases (merged pedestrian groups, tree canopy bridging) - Tracking stability under occlusion with classical filters Happy to discuss. Full code + technical reports with ablation tables and failure analysis: https://github.com/bonsai89/lidar-perception-pipeline Context: perception engineer, previously at Toyota Technological Institute (camera-LiDAR-radar fusion, 5 papers) and TierIV, Japan (Autoware/ROS2 perception). Getting back into the field after a break.

6h ago

---

**[Aigen’s autonomous solar robots identify and remove weeds without herbicides](https://www.reddit.com/r/robotics/comments/1sfylpx/aigens_autonomous_solar_robots_identify_and/)**

44m ago

---

**[6 axis robot](https://www.reddit.com/r/robotics/comments/1sff1il/6_axis_robot/)**

16h ago

---

**[Torobo Humanoid Robot by Tokyo Robotics](https://www.reddit.com/r/robotics/comments/1sf806y/torobo_humanoid_robot_by_tokyo_robotics/)**

Torobo Humanoid Robot by Tokyo Robotics that looks like Atlas by Boston Dynamics. They recently switched their Torobo robot to become bipedal.

21h ago

---

**[Pouvez vous me donner des Conseils sur ros2 ?](https://www.reddit.com/r/robotics/comments/1sfzh0h/pouvez_vous_me_donner_des_conseils_sur_ros2/)**

Bonjour à tous, Je suis étudiant et je débute sur ROS 2. J’ai déjà mis les mains dedans, je sais créer des packages, utiliser les nodes, topics, services, lancer des simulations… bref, j’arrive à faire tourner des petits projets. Mais honnêtement, je sens que je fais encore beaucoup “par habitude” ou en m’aidant de ce que je trouve en ligne, et pas parce que je comprends tout en profondeur. Du coup, dès que ça sort un peu du cadre, je suis vite limité. Je voulais donc avoir vos retours, surtout de ceux qui sont déjà passés par là. Comment vous avez fait pour vraiment passer un cap sur ROS 2 ? Pas juste apprendre plus de commandes, mais vraiment comprendre comment tout s’articule, être autonome, et réussir à construire des systèmes plus complexes sans galérer à chaque étape. Concrètement, vous vous êtes entraînés comment ? Plutôt en enchaînant les projets, en creusant la théorie, en comprenant mieux le middleware, ou en travaillant vos pratiques de dev ? Est-ce qu’il y a des points que vous avez négligés au début et que vous avez dû rattraper plus tard ? Je me pose aussi quelques questions en vrac. Est-ce que ça vaut le coup de regarder dès maintenant des sujets comme la sécurité avec SROS2 ou ROS-Industrial, ou c’est encore secondaire à ce stade ? Pour les versions comme Humble, Iron ou Jazzy, est-ce qu’il y a un vrai choix à faire ou pas vraiment de différence au quotidien ? Et en dehors de ROS 2, qu’est-ce que vous conseillez de bosser en priorité pour devenir plus solide en robotique ? Si vous avez un retour un peu honnête sur ce qui fait la différence entre quelqu’un qui se débrouille et quelqu’un de vraiment à l’aise, je suis preneur. Merci à ceux qui prendront le temps de répondre 🙂

14m ago

---

**[Maximo’s AI-powered robots have installed over 100MW of solar panels, bringing automation to energy projects.](https://www.reddit.com/r/robotics/comments/1serirr/maximos_aipowered_robots_have_installed_over/)**

From NVIDIA Robotics on 𝕏: https://x.com/NVIDIARobotics/status/2041349314262495265 NVIDIA blog: https://blogs.nvidia.com/blog/national-robotics-week-2026/#maximo

1d ago

---

**[GenAI is lowering the barrier to hacking physical systems (not just software)](https://www.reddit.com/r/robotics/comments/1sfxka9/genai_is_lowering_the_barrier_to_hacking_physical/)**

There’s a shift happening that feels easy to underestimate: GenAI isn’t just affecting software security — it’s starting to impact physical systems too. Looking at recent work around consumer robots, a few things stand out: - vulnerability discovery can be partially automated - interaction with hardware protocols becomes more accessible - multi-step attack paths can be assisted by AI Things that previously required fairly deep robotics or embedded expertise are becoming easier to explore with the right setup. Not fully automated by any means — but the barrier to entry is clearly moving. Feels like we might be underestimating how this changes the threat landscape for robotics and physical systems. Especially as these systems become more connected and deployed at scale. Curious how others here see this evolving.

1h ago

---

**[At what point do you stop adding complexity to a robot design?](https://www.reddit.com/r/robotics/comments/1sfnuzi/at_what_point_do_you_stop_adding_complexity_to_a/)**

I’ve been working in industrial robotics (mostly integration and deployment) for about 5 years, but I’m currently building a small differential drive robot on my own outside of work. What’s interesting is I’m running into a problem I don’t usually feel as strongly on the job: knowing when to stop adding “improvements.” What started as a simple platform has gradually grown — I added encoder feedback, tuned a PID loop for motor control, redesigned parts for easier mounting, and now I’m considering splitting responsibilities across two controllers to better handle sensor input. None of these decisions are unreasonable on their own, but taken together I’m starting to wonder if I’m overengineering something that was supposed to be simple and quick to iterate. In industry projects, there are usually clearer constraints (budget, deadlines, client requirements), so the line is easier to draw. On a personal build, that line feels a lot fuzzier. For those of you with experience building robots outside of structured projects — how do you decide when something is “good enough” to stop iterating? Do you bias toward simplicity early on, or design for scalability from the start? Curious how others approach this in practice.

8h ago

---

**[Robots fixing robots](https://www.reddit.com/r/robotics/comments/1sf1ihh/robots_fixing_robots/)**

Generalist just dropped GEN-1, the first general-purpose robot Al that hits 99% success rate on tasks where older models managed only 64%. The wild part? It didn't learn from robots, it learned from humans wearing cameras doing everyday tasks. That data transfers to robots with minimal retraining.When things go wrong, it improvises regrasping, switching hands, adapting on the fly. No explicit programming.

1d ago

---

---

## Google News: "robotics"

**[Robot Density Surges in Europe, Asia, and Americas](https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas)**

Economies worldwide are prioritising the integration of factory robots, as automation becomes a critical tool for boosting productivity. In the global automation race, the Western European countries reached a record 267 robots per 10,000 employees in the manufacturing industry 2024 – ahead of North America with 204 units and Asia with 131 units. This is according to the World Robotics 2025 report, presented by the International Federation of Robotics (IFR).

International Federation of Robotics • 12h ago

---

**[From folding boxes to fixing vacuums, GEN-1 robotics model hits 99% reliability](https://arstechnica.com/ai/2026/04/generalists-new-physical-robotics-ai-brings-production-level-success-rates/)**

New model can respond to disruptions and figure out moves it wasn't trained for.

Ars Technica • 1d ago

---

**[Former UNH hockey star using robotics for shoulder replacements](https://www.wmur.com/article/former-unh-hockey-robotics-shoulder-4726/70956955)**

Hockey fans might remember former University of New Hampshire player Thomas Fortney, who tied a 2009 NCAA tournament game against North Dakota with a tenth of a second remaining in regulation.

WMUR • 18h ago

---

**[HII Teams with GrayMatter Robotics to Integrate Physical AI into Manned and Unmanned Shipbuilding](https://hii.com/news/hii-teams-with-graymatter-robotics-to-integrate-physical-ai-into-manned-and-unmanned-shipbuilding/)**

CARSON, Calif., (April 6, 2026) — HII (NYSE: HII) and GrayMatter Robotics (GMR) signed a memorandum of understanding (MOU) today to explore the integration of GMR’s Physical AI into shipbuilding operations that could accelerate throughput, strengthen the maritime industrial base, and augment the shipbuilding workforce. This will include bringing autonomous surface preparation, coating, and inspection

HII • 1d ago

---

**[Kraken Robotics Demonstrates KATFISH Autonomous Launch and Recovery from SEFINE USV](https://www.krakenrobotics.com/news-releases/kraken-robotics-demonstrates-katfish-autonomous-launch-and-recovery-from-sefine-usv/)**

Kraken Robotics Demonstrates KATFISH Autonomous Launch and Recovery from SEFINE USV

Kraken Robotics • 1d ago

---

**[Wakefield senior mentors two Arlington robotics teams to world championship](https://www.arlnow.com/2026/04/07/wakefield-senior-mentors-two-arlington-robotics-teams-to-world-championship/)**

A Wakefield High School senior is heading to the VEX Robotics World Championship for the second year in a row — and this time, he's bringing an elementary school team with him. Greyson Schroeher has spent the school year mentoring two Arlington robotics teams that both qualified for the World Championship in St. Louis later

arlnow.com • 1d ago

---

**[‘No one’s raising their hand’: Japan’s labor crisis is making the case for robots taking the jobs you don’t want](https://fortune.com/2026/04/06/japan-labor-shortage-robots-ai-robotics-humanoid/)**

Japan is looking to become the dominant source of robotics by 2040, expedited by an aging population and a growing need for labor.

fortune.com • 1d ago

---

**[China to Deploy 100,000 Humanoid Robots—Will the West Ever Catch Up?](https://www.futura-sciences.com/en/china-to-deploy-100000-humanoid-robots-will-the-west-ever-catch-up_29061/)**

A technological ecosystem like no other Thanks to an exceptionally dense and innovative technological ecosystem, Beijing is about to deploy an impressive number of new humanoid robots in its factories. And let’s not forget: the country already held a dominant position in automation! For nearly a decade now, robotics has...

Futura, le média qui explore le monde • 2h ago

---

**[China tests humanoid robots for border control tasks with Vietnam](https://www.ecoticias.com/en/china-tests-humanoid-robots-for-border-control-tasks-with-vietnam/30471/)**

The timing is hard to miss. While investors digest the fundraising, a separate headline has also been making the rounds after the South China Morning Post

ecoticias.com • 21h ago

---

**[Robot Maker Kuka Eyes US, Asia as Europe Lags Behind on AI](https://www.bloomberg.com/news/articles/2026-04-08/robot-maker-kuka-eyes-us-asia-as-europe-s-factories-lag-on-ai)**

Bloomberg.com • 8h ago

---

---

## YouTube Videos: "robotics"

**[Tesla Optimus Gen 3 FINALLY HERE: $20,000 Robot Works 24/7 — No Salary, No Sleep, No Limits](https://www.youtube.com/watch?v=UTASTLBTRDE)**

Tesla Optimus Gen 3 $20K robot shocks—24/7 worker that could replace jobs fast ✓ All Breaking NEWS: ...

📺 Tech Revolution

👁️ 4K • 👍 159 • 💬 26 • ⏱️ 19:27 • 4d ago

---

**[Shawn Ryan Tests a Real Humanoid Robot](https://www.youtube.com/watch?v=HWq9cFhTvvQ)**

Shawn Ryan gets hands-on with a real humanoid robot powered entirely by AI. In this clip, we break down how this robot sees, ...

📺 Shawn Ryan Show

👁️ 1.2M • 👍 42K • 💬 7K • ⏱️ 8:48 • 6d ago

---

**[New GEN 1 AI Robot Hits 3X Faster At 1,800+ Reps (AI NEWS)](https://www.youtube.com/watch?v=IgwL5-IH6gU)**

AIR CONDITIONED SHIRTS??: https://octocool.com Generalist AI's GEN-1 embodied foundation model achieves 99% success ...

📺 AI News

👁️ 5K • 👍 145 • 💬 17 • ⏱️ 8:04 • 5d ago

---

**[Are AI soldiers about to take over the battlefield? | DW News](https://www.youtube.com/watch?v=q83LtZza5eA)**

US startup Foundation is developing humanoid robots for military use. The goal is for its Phantom model to identify targets and ...

📺 DW News

👁️ 72K • 👍 545 • 💬 95 • ⏱️ 1:22 • 2d ago

---

**[These NEW Human-Like AI Robots of 2026 Just SHOCKED the World!](https://www.youtube.com/watch?v=FOfieag6fi4)**

The world wasn't ready for what 2026 had in store — a wave of humanoid robots so advanced, so eerily lifelike, that the line ...

📺 The AI Nexus

👁️ 7K • 👍 249 • 💬 17 • ⏱️ 16:42 • 2d ago

---

**[Joe Rogan Watches Soldier Test INSANE Robotic Legs 🤖🦿💥 #Shorts](https://www.youtube.com/watch?v=zbopLtVrukQ)**

Joe Rogan Watches Soldier Test INSANE Robotic Legs #Shorts This is the future of the battlefield. A soldier straps on ...

📺 Silent Sentry

👁️ 1.9M • 👍 24K • 💬 570 • ⏱️ 0:17 • 5d ago

---

**[welding robot #automation #machine #industrialrobots #welding #robot](https://www.youtube.com/watch?v=4KM9QWO5__Q)**

📺 Robot Julie 

👁️ 27K • 👍 117 • 💬 1 • ⏱️ 0:23 • 1d ago

---

**[Inside the World&#39;s Smartest Robot Brain](https://www.youtube.com/watch?v=2mrGMMmrVNE)**

Welch Labs Book: https://www.welchlabs.com/resources/ai-book-ezrzm-msrmc Book & VLA Poster Bundle: ...

📺 Welch Labs

👁️ 93K • 👍 4K • 💬 227 • ⏱️ 35:02 • 4d ago

---

**[I broke a robot in China](https://www.youtube.com/watch?v=7U3vjVfwChc)**

China is leading the world in humanoid robot shipments. Powered by artificial intelligence, these machines are setting new ...

📺 CGTN

👁️ 33K • 👍 292 • 💬 60 • ⏱️ 1:54 • 6d ago

---

**[Engineering the Experience – How Do Robots Work on a Cruise Ship?](https://www.youtube.com/watch?v=AezeHLJedYc)**

How do robots work on a cruise ship? In this episode of Engineering the Experience, Royal Caribbean explores the robotics and ...

📺 Royal Caribbean

👁️ 8K • 👍 205 • 💬 17 • ⏱️ 4:51 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

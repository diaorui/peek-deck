---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-05T01:40:40.216178+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 05, 2026 at 01:40 UTC  
**HTML Version:** [ai.html](https://peekdeck.ruidiao.dev/ai.html)

---

## Table of Contents

1. [Reddit: r/artificial](#reddit-rartificial)
2. [Google News: "ai"](#google-news-ai)
3. [HackerNews: "ai"](#hackernews-ai)
4. [YouTube Videos: "ai"](#youtube-videos-ai)
5. [HuggingFace Models: 🔥 Trending](#huggingface-models--trending)
6. [HuggingFace Papers: 🔥 Trending](#huggingface-papers--trending)
7. [GitHub Repositories: "ai"](#github-repositories-ai)

---

## Reddit: r/artificial

**[Apple Watch now listens to in-person conversations & lets you rewind them](https://www.reddit.com/r/artificial/comments/1xntvml/apple_watch_now_listens_to_inperson_conversations/)**

Apple is introducing a new AI feature that allows Apple Watch users to rewind in-person conversations and see what someone just said.

🔗 [Dexerto](https://www.dexerto.com/entertainment/apple-watch-now-listens-to-in-person-conversations-lets-you-rewind-them-3424859/) • 8h ago

---

**[ChatGPT's search volume is now roughly 20% of Google's. Wow, people were really sick of Google, huh?](https://www.reddit.com/r/artificial/comments/1xng7ur/chatgpts_search_volume_is_now_roughly_20_of/)**

OpenAI's Adam Fry told Big Technology that ChatGPT has around a fifth of Google's search query volume. Google can't be thrilled about that.

🔗 [Yahoo Tech](https://tech.yahoo.com/ai/chatgpt/articles/chatgpts-search-volume-now-roughly-204510905.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cucmVkZGl0LmNvbS8&guce_referrer_sig=AQAAANy0RModkKsLyARqY6lqMPmtivd1CCMgna0IdrKqIsarmAbO19gMY1fHjZfcXchRmKZfCO8LJw5jmpZ6jA48LS83X0itLoUODWr8OAXnugut3tMTcCeuQuyu-PqSTui9NQz4WsR_ZQEf1yfCQiA-goPObb6Nid3HP_a72DiuIXf3) • 20h ago

---

**[Anthropic’s FlashProve could prove an AI provider used the model you paid for without exposing its weights](https://www.reddit.com/r/artificial/comments/1xnrvak/anthropics_flashprove_could_prove_an_ai_provider/)**

Users currently have no independent way to confirm whether an AI provider served the requested model or quietly substituted a cheaper one. FlashProve addresses this by using zero-knowledge cryptography to prove that a particular model generated a response while keeping its proprietary weights hidden. Anthropic demonstrated the open-source system on a 400-billion-parameter model, generating proofs at roughly 110 tokens per second. However, the prototype requires 70 to 95 times more GPU time than ordinary inference, supports only 1,024-token contexts and does not yet cover every type of model output. Could cryptographic verification become standard for high-stakes AI services, even if it remains too expensive for everyday requests?

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/anthropic-flashprove-cryptographic-model-verification) • 9h ago

---

**[Apple put a warning about rogue AI agents in its 10-K. That’s a legal filing, not a blog post.](https://www.reddit.com/r/artificial/comments/1xnudhs/apple_put_a_warning_about_rogue_ai_agents_in_its/)**

Apple’s annual report to the SEC now includes language about AI agents potentially acting without authorization, and specifically uses the words conceal and manipulate when describing unintended agent behaviour. Worth pausing on where that appears. A 10-K is a legal document. Risk factors in it are drafted by lawyers who are personally exposed if they’re wrong or misleading. Companies put things there when they’ve concluded the risk is material enough that not disclosing it is the bigger liability. Apple also changed how full disk access works on macOS, apparently to reduce what an agent can reach. I’ve been in a lot of conversations this year where agent risk gets discussed as a future concern. This is a company with more legal caution than almost anyone writing it down as a present-tense business risk. The thing I find most interesting is the word conceal. Unauthorized action is one category of problem. An agent that hides what it did is a different one entirely, because it breaks the assumption underneath every monitoring and audit approach I’ve seen deployed. Anyone read the actual filing language? Curious whether it’s broader boilerplate or genuinely specific.

8h ago

---

**[Congressional Progressive Caucus Chair calls for AI to be a top issue next year and for testimony from CEOs](https://www.reddit.com/r/artificial/comments/1xnf3ks/congressional_progressive_caucus_chair_calls_for/)**

https://fixupx.com/BenBrodyDC/status/2117821832317534519

21h ago

---

**[ai has been stuck in software. what would ai native hardware actually need to be?](https://www.reddit.com/r/artificial/comments/1xnvouu/ai_has_been_stuck_in_software_what_would_ai/)**

aina a hardware interface launching tomorrow says every big shift in computing came from software and hardware built together which is true, the mouse and gui, then the touchscreen, and that ai has been stuck in software. nobody says what it is. i'm curious what you think about the claim. chat is how we talk to ai today, but is that really the right interface? if ai got its own hardware, what's the job it would do better than a phone or a laptop? and what would you not want it to do?

7h ago

---

**[Cognition launches SWE-2 Flash: a coding agent model 3x faster at one-fifth the price](https://www.reddit.com/r/artificial/comments/1xo27a9/cognition_launches_swe2_flash_a_coding_agent/)**

Cognition (the company behind Devin) announced SWE-2 Flash on November 4, 2026. It is pitched as a cheaper, faster sibling to SWE-2: about 3x the speed at one-fifth the price, aimed at routine agent work like automations, code review, feature development, and documentation updates, rather than uniform benchmark leadership. It is free to use through November 30, 2026, and available in Devin Desktop and CLI. Some details worth noting: - 276B total parameters, 12B active, adapted from Thinking Machines Lab's Inkling-Small, whose full weights were released on July 30, 2026. - Cognition reports big gains over Inkling-Small but mixed results against the larger SWE-2, framing Flash as a cost-and-speed alternative, not a replacement. - The weights are not public yet. Cognition is building a secure sharing program for trusted partners and labs, and says targeted cybersecurity training lifted ExploitBench from 11.3% to 34.8% -- capability it worries could help attackers as well as defenders. What I am curious about: for day-to-day coding work, does speed plus low price matter more than topping benchmarks? And is withholding the weights the right tradeoff here, or does it just slow down independent evaluation of the safety claims? (Source: Unite.AI coverage of the November 4 announcement; benchmark figures are Cognition's own.)

3h ago

---

**[When LLMs edit neural weights directly, how do we version-control them? Announcing wpgit & Weight-Space Software Engineering (Paper + Code)](https://www.reddit.com/r/artificial/comments/1xo54c3/when_llms_edit_neural_weights_directly_how_do_we/)**

Links: Project Page: https://v-code-895.github.io/wsse/ Paper (Zenodo DOI 10.5281/zenodo.23956114): https://doi.org/10.5281/zenodo.23956114 Code, Checkpoints & Git Bundles: https://github.com/v-code-895/wsse TL;DR Earlier this week, MIT CSAIL published Sparks of Weight-Space Programming, demonstrating that frontier LLMs can inspect raw neural network parameters and write direct, gradient-free weight edits to patch models or steer behavior. Direct weight editing by an LLM is like hex-editing a binary in memory. It works as a one-shot demo, but what happens when an autonomous agent (or multiple agents and engineers) needs to steer different behaviors, add features, and compose dozens of edits over time? Without software engineering discipline, weight surgery causes silent regressions, breaks when branches merge, and collapses when the base model updates. We built Weight-Space Software Engineering (WSSE) and wpgit: bringing version control, in-context CI/CD regression gates, semantic merge conflict resolution, and upstream rebasing directly into weight space. The Idea: Storing Weight Edits as Text Diff Files Instead of distributing modified multi-megabyte binary checkpoints, every weight edit or steering intervention is captured as a human-reviewable .weightpatch.json text file: Hash-pinned: Pinned to a 16-character SHA-256 hash of the target base checkpoint. Dependency-aware (requires): Declares which structural patches must precede it. Compact operators: Instead of dense float arrays, patches store compact mathematical parameters (e.g., a 12-number affine fold that deterministically rewrites 4,803 weights at build time). Self-testing: Carries quantitative assertions that must pass in context before the patch can merge. Our companion tool, wpgit, layers on top of standard Git: wpgit build: Compiles checkpoints in topological dependency order. wpgit test: Runs differential integration tests in context (comparing the full merged build against the build without that patch's dependency closure). wpgit check: Tests pairwise commutativity to catch semantic merge conflicts that Git merges silently. wpgit rebase: Migrates patch repositories onto updated base checkpoints, automatically detecting stale context when internal parameters have drifted. Key Findings Across 17 Experiments (150K to 8.1M Parameters) We evaluated the framework on an 8.1M-parameter cat generator (CatGAN-26), a 277K-parameter super-sampler (TinySR-26), MobileNetV2, and seven legacy 2017-2020 Keras checkpoints. 1. Steering and Locking Latent Behaviors Without Retraining Using weight surgery on CatGAN-26, we synthesized patches to steer and freeze attributes without running gradient descent: Why 1-D clamps fail: Clamping a single latent direction leaves 68-71% of attribute variance because deep generators encode attributes non-linearly. Rank-2 Active Subspace Locks: By computing the dominant eigenvectors of the gradient outer product (active subspaces), we clamp a 2-D subspace using two orthonormal ops. This collapses attribute variance down to 10-11%, passing strict regression bounds without moving the goalposts. 2. Zero-Parameter Circuit Surgery via Channel Reclamation To change a specific visual feature (e.g., turning cat irises blue) without altering the rest of the image or modifying the network architecture: Latent steering distorts the whole face without reaching the eyes, and ungated output folds turn the entire cat blue. Reclamation (prune2) + Exact ReLU gating (eye_gate): We identify the two most redundant channels in an internal conv layer, regress them onto remaining channels, fold that regression into the next layer, and zero the two slots (0.0045 rest-of-image MAE). We then wire a spatial detector into the freed channels to drive an exact paired-LeakyReLU ReLU gate: LeakyReLU(u) + a * LeakyReLU(-u) = (1 - a^2) * ReLU(u) This writes an ice-blue chrominance vector only where the gate fires, hitting the target hue with 23x less collateral change (0.0059 vs 0.136 MAE) than an ungated fold. 3. What Git Merges Cleanly, but the Weights Reject We scripted a 15-commit Git repository with feature branches for steering shifts, attribute locks, and the blue-eye circuit: Failures only visible in context: Two latent shift patches (warm_fur and bright_background) pass their unit tests in isolation, but fail when merged into main because generator non-linearity couples them. A test run on an isolated patch cannot see this. Semantic merge conflicts (wpgit check): Git merges two lock branches without a textual conflict, but wpgit check flags an order-dependent collision (output MAE 0.129). We formalize two conflict types: Type I (Interference): Overlapping latent subspaces. Resolved algebraically via Gram-Schmidt orthogonalization so the locks commute to 2.4e-7. Type II (Contradiction): One patch freezes the background while another brightens it. No algebra satisfies both; the engineer resolves it via an explicit product commit (git rm). 4. The Orthogonality Fallacy in Fine-Tune Merging We fine-tuned two specialist branches of TinySR-26 (one for bicubic inputs at +0.23 dB, one for noisy inputs at +3.26 dB). Their weight deltas are nearly orthogonal (cos = 0.088) and commute to float precision (1.5e-8). Adding the deltas wipes out the bicubic gain and causes a -4.06 dB regression on nearest-neighbour inputs. Weight-space orthogonality does not imply functional independence. Layer-by-layer regression attribution shows the drop is spread across every residual block. Dropping blocks worst-first removes 8 of 9 blocks, destroying the gain. A fine-tune delta only works as an atomic unit: partial reverts that are routine in code break it. 5. Rebasing Patches Across Upstream Base Updates (wpgit rebase) When CatGAN-26 is trained +500 to +4,000 steps further: Input-level latent locks survive +4,000 steps (17.9% weight drift). Internal channel-level patches (prune2, eye_gate) leave residual weights in moved channels, breaking collateral bounds after +2,000 steps. wpgit rebase flags internal channel patches as stale_context at +500 steps, long before behavioral tests fail. Re-fitting patches from scratch on the new base restores channel guarantees, but exposes a new interaction: locking cats to light fur shifts the iris detector's scores past its threshold. Only in-context integration testing exposes this. 6. Static Weight Forensics (Reading Checkpoints Without Data) Static weight inspection (extract_and_audit.py) exposed training facts and bugs without forward passes: Step-count recovery: Because Keras initialized BatchNorm running variance at 1.0 with momentum 0.99, a classifier's first BatchNorm variance (0.8347 ~ 0.99n) revealed n = 18 optimizer steps, matching the 6-epoch early-stopped training log. Dataset mean extraction: MobileNetV2's Conv1 lacks a bias, meaning bn_Conv1's running mean is the filter sums times the training set's mean RGB. Solving this 32x3 linear system (R2 = 1.000) recovered ImageNet's mean RGB to within 1.4 levels (122.3, 116.2, 102.9) from the weights alone. Compiling deployment fixes: Folding raw uint8 input scaling into Conv1 is exact in the interior but causes a 1.6 border logit error because zero-padding in [-1, 1] space equals 127.5 in raw pixel space. Incorporating the padding constant directly into the patch restores exactness (2.5e-5) and brings top-1 agreement from 0% to 100% with zero added runtime FLOPs. Why This Matters If LLMs and autonomous agents are going to edit, specialize, and steer neural network weights, we cannot treat checkpoints as opaque binary blobs, nor can we trust single-shot edits that lack regression suites. Weight updates need the same tooling software engineering spent 50 years building: content hashes, in-context unit tests, algebraic merge checks, and clean version control. All code, weights, .weightpatch.json files, and 15-commit Git bundles are open source under MIT / CC BY-NC 4.0: Repository: https://github.com/v-code-895/wsse Interactive Figures & Visuals: https://v-code-895.github.io/wsse/ Archival DOI: https://doi.org/10.5281/zenodo.23956114 Happy to answer questions on weight steering, model diffing, and how software engineering applies to weights!

52m ago

---

**[Hy4 adds vision and computer use. How reliable will it be on long tasks?](https://www.reddit.com/r/artificial/comments/1xnn1xm/hy4_adds_vision_and_computer_use_how_reliable/)**

Tencent just dropped Hy4. Vision and computer use are probably the two biggest new additions. For the first time, Hy can understand images and complex charts. It can also work across CLI and GUI, with specific training for tools like Blender and CAD. The computer use part sounds pretty interesting, but there’s more to it than just clicking buttons and running commands. What happens when a button moves, a permission pop-up gets in the way, or a command fails halfway through a task? Can the model figure out what went wrong and get back on track? And what about the extra cost? Every failed action, retry, or new screenshot could mean more tokens and API calls. Over a long workflow, those costs could add up pretty quickly. There’s also the problem of keeping track of everything across a long workflow. An agent might complete several steps correctly, then lose track of its progress or assume something worked when it didn’t. Being able to perform individual actions is one thing. Getting through an entire workflow without losing track of messing things up is another. Is anyone else interested in putting Hy4’s computer use capabilities to a real-world test? Official announcement: Tencent Hy

13h ago

---

**[Google to shut off search for schools that opt-out of AI](https://www.reddit.com/r/artificial/comments/1xn22y7/google_to_shut_off_search_for_schools_that_optout/)**

The company said that AI-enabled products would be shut off by default for schools, which will also cut off their access to Google Search.

🔗 [NBC News](https://www.nbcnews.com/tech/tech-news/google-shut-search-schools-opt-ai-rcna607280) • 1d ago

---

---

## Google News: "ai"

**[Apple Cuts Internal AI Usage Budgets in Move to Reduce Spending](https://www.bloomberg.com/news/articles/2026-11-04/apple-cuts-internal-ai-usage-budgets-in-move-to-reduce-spending)**

Bloomberg.com • 5h ago

---

**[Apple cuts employee AI budgets in cost-control push, Bloomberg News reports](https://www.reuters.com/business/retail-consumer/apple-cuts-employee-ai-budgets-cost-control-push-bloomberg-news-reports-2026-11-04/)**

Reuters • 5h ago

---

**[Apple is reportedly cutting budgets for its internal AI usage](https://techcrunch.com/2026/11/04/apple-is-reportedly-cutting-budgets-for-its-internal-ai-usage/)**

The company is said to be significantly dropping the amount it's spending on AI for its engineering teams.

TechCrunch • 14m ago

---

**[Google Will Turn Off Search for Schools That Reject A.I.](https://www.nytimes.com/2026/11/03/us/google-search-schools-restrict-ai.html)**

The New York Times • 1d ago

---

**[Google responds to political backlash over removing search from schools that ban AI](https://www.cnbc.com/2026/11/03/google-responds-to-outrage-over-removing-search-in-schools-that-ban-ai.html)**

After elected officials voiced outrage over Google turning off search at schools that ban AI, the company said search can be turned back on with AI Overviews.

CNBC • 1d ago

---

**[Seattle families to rally, address generative AI tech usage in schools](https://komonews.com/news/local/seattle-publis-schools-crisis-in-the-classroom-families-to-rally-to-address-generative-ai-in-schools-education-washington-state-youtube-minecraft-gemini)**

Seattle families are urging the state’s largest school district to pause the use of generative AI and address concerns about student-facing technology.Some Sea

KOMO • 2h ago

---

**[How AI Changes The Starting Point Of Team Discussions](https://www.forbes.com/sites/melissadaimler/2026/11/04/how-ai-changes-the-starting-point-of-team-discussions/)**

Forbes • 14m ago

---

**[Tencent Targets Financial Analysis With Hy4 AI Model](https://www.pymnts.com/news/artificial-intelligence/2026/tencent-targets-financial-analysis-with-hy4-ai-model/)**

Tencent has released its latest generation large language model, Hy4, saying in a Wednesday (Nov. 4) press release that it “now ranks among the world’s

PYMNTS.com • 30m ago

---

**[Bright Pattern Featured on GSA UK's SourcingTV: AI, Data Sovereignty and the Future of Global Customer Experience](https://www.freep.com/press-release/story/267360/bright-pattern-featured-on-gsa-uks-sourcingtv-ai-data-sovereignty-and-the-future-of-global-customer-experience/)**

That's why it's important for us to offer local deployment of both customer service platforms and AI technology,

Detroit Free Press • 41m ago

---

**[‘AI earthquake’: Democrats eye a Silicon Valley reckoning](https://www.politico.com/news/2026/11/04/democrats-eye-a-silicon-valley-ai-reckoning-01148624)**

Politico • 10h ago

---

---

## HackerNews: "ai"

**[Postman silently auto-installs AI plugins and attempts to share all API data](https://news.ycombinator.com/item?id=50354960)**

Is there an existing issue for this? I have searched the tracker for existing similar issues and I know that duplicates will be closed Describe the Issue Opening Postman on my Mac was followed by u...

⬆️ 1485 • 💬 483 • 1d ago • [GitHub](https://github.com/postmanlabs/postman-app-support/issues/14370)

---

**[AI is forcing us to pay off 40 years of technical debt](https://news.ycombinator.com/item?id=50364336)**

AI is forcing us to pay off 40 years of technical debt

⬆️ 1059 • 💬 633 • 13h ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability)

---

**[Google will turn off search for schools that reject AI](https://news.ycombinator.com/item?id=50353192)**

⬆️ 662 • 💬 460 • 1d ago • [nytimes.com](https://www.nytimes.com/2026/11/03/us/google-search-schools-restrict-ai.html)

---

**[Fujifilm to boost tape production 5x as AI fuels archiving demand](https://news.ycombinator.com/item?id=50336918)**

Low costs and offline security mean magnetic tape still has a job.

⬆️ 527 • 💬 226 • 2d ago • [Ars Technica](https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/)

---

**[US tech giants' hidden AI debt swells 90% to $3.2T in 6 months](https://news.ycombinator.com/item?id=50358422)**

Google, Meta, others' commitments and obligations reach 80% of assets

⬆️ 408 • 💬 166 • 1d ago • [Nikkei Asia](https://asia.nikkei.com/business/technology/artificial-intelligence/us-tech-giants-hidden-ai-debt-swells-90-to-3.2tn-in-6-months)

---

**[The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer](https://news.ycombinator.com/item?id=50358582)**

This book provides a compact, derivation-oriented introduction to the mathematical foundations of modern generative artificial intelligence. Rather than surveying every recent architecture or implementation detail, it develops a coherent route through the ideas connecting major families of generative models, from PCA, probabilistic PCA, variational autoencoders, and diffusion models to normalising flows, autoregressive factorisations, GANs, Wasserstein GANs, and energy-based models. The aim is to make the structure of generative modelling more accessible without removing the mathematical substance needed to understand how these models are derived and related. The book is intended as a foundation-building primer for mathematically curious researchers, practitioners, and students.

⬆️ 383 • 💬 60 • 1d ago • [arXiv.org](https://arxiv.org/abs/2605.29713)

---

**[Anthropic's internal AI use, at retail prices, now exceeds its employee pay](https://news.ycombinator.com/item?id=50339494)**

Anthropic's IPO filing reveals a striking milestone: Its internal AI usage is now valued above employee compensation.

⬆️ 352 • 💬 270 • 2d ago • [Business Insider](https://www.businessinsider.com/anthropic-claude-internal-ai-use-exceeds-employee-pay-tokens-2026-11)

---

**[Geoffrey Hinton: it might turn out we were better off without AI](https://news.ycombinator.com/item?id=50363554)**

Nobel winner warns the tech could be near to triggering major incident such as power or banking shutdown

⬆️ 297 • 💬 293 • 15h ago • [the Guardian](https://www.theguardian.com/uk-news/2026/nov/03/ai-godfather-geoffrey-hinton-better-off-without-ai)

---

**[How I use AI (Oct 2026)](https://news.ycombinator.com/item?id=50355767)**

I document how I use AI, one year after my first writeup. Everything's completely different.

⬆️ 250 • 💬 300 • 1d ago • [ben.stolovitz.com](https://ben.stolovitz.com/posts/how-use-ai-oct-2026/)

---

**[Oracle files to sell $20B in new stock, bonds to finance AI buildout](https://news.ycombinator.com/item?id=50342284)**

Oracle filed plans on Monday to issue new shares and more debt to finance its artificial intelligence buildout.

⬆️ 199 • 💬 175 • 2d ago • [CNBC](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html)

---

---

## YouTube Videos: "ai"

**[Elon Musk Just Burst The AI Bubble](https://www.youtube.com/watch?v=mE-DrQNRsRA)**

Join Pepperstone https://go.coinbureau.com/pepperstone-fb Subscribe to our Newsletter https://financebureau.com/ ...

📺 Finance Bureau

👁️ 87K • 👍 1K • 💬 155 • ⏱️ 17:12 • 9h ago

---

**[AI Bubble: Big Tech’s MAGA alliance is over | Martha Muir](https://www.youtube.com/watch?v=K29L-LJstB8)**

A bad night for anyone who wants to develop a data center. And a horrible night for anyone who wants to develop a data center in ...

📺 The Tech Report

👁️ 69K • 👍 1K • 💬 394 • ⏱️ 22:07 • 5h ago

---

**[MIT looked at what AI actually killed and holy sh*t...](https://www.youtube.com/watch?v=W8Dl-TS9H2c)**

MIT looked at what AI is actually replacing, and the answer isn't entire professions. It's entry-level work. Researchers mapped ...

📺 The Infographics Show

👁️ 818K • 👍 8K • 💬 2K • ⏱️ 12:57 • 23h ago

---

**[Anthropic&#39;s New Opus 6 Ignites a Terrifying AI Theory](https://www.youtube.com/watch?v=Jj_i9SzKhug)**

Anthropic just warned that its next Claude models could be approaching recursive self-improvement, fueling speculation around ...

📺 AI Revolution

👁️ 31K • 👍 600 • 💬 54 • ⏱️ 13:54 • 1d ago

---

**[AI vibe coding changes a local man’s life path](https://www.youtube.com/watch?v=qvOxAbC3d0U)**

CTV's Krista Sharpe-Kilpatrick finds out how a man went from driving a forklift to a booming tech career. Subscribe to CTV News to ...

📺 CTV News

👁️ 250K • 👍 3K • 💬 502 • ⏱️ 3:20 • 2d ago

---

**[Sam Altman On AI Revolution, Superintelligence &amp; Future Of Humanity | FO583 Raj Shamani](https://www.youtube.com/watch?v=TjPPIf-M6KE)**

To know more about our Styling Partner Levi's, Checkout:- ...

📺 Raj Shamani

👁️ 2.8M • 👍 52K • 💬 4K • ⏱️ 1:08:01 • 1d ago

---

**[The Most Insane AI Film You&#39;ll See Today (Seedance 2.5)](https://www.youtube.com/watch?v=1yLAbK5F3E8)**

PLANET HELL is an AI Sci-FI Short Film expanding on the original AI Film trailer made in Veo-3.1 This is an ongoing series about ...

📺 Theoretically Media

👁️ 109K • 👍 2K • 💬 406 • ⏱️ 5:15 • 2d ago

---

**[Why AI experts are sounding the alarm about the midterms](https://www.youtube.com/watch?v=VjKREc7YWxo)**

AI chatbots could influence how Americans vote, and the chatbot they choose matters. CNN's Hadas Gold met with a team of ...

📺 CNN

👁️ 235K • 👍 923 • 💬 418 • ⏱️ 12:53 • 2d ago

---

**[Master Ultra Realistic AI Video in 10 minutes](https://www.youtube.com/watch?v=RJKZCbeqIjc)**

How to Make Realistic AI Videos in OpenArt: Lighting, Characters and Motion Create your AI images and videos in OpenArt: ...

📺 Mira AI

👁️ 7K • 💬 1 • ⏱️ 10:05 • 8h ago

---

**[Popular Animation YouTuber CAUGHT Using AI Art](https://www.youtube.com/watch?v=AZbCxTQDX6U)**

Storytime animation YouTuber Swoozie has used generative artificial intelligence in his brand new video "Fast and Curious 4", ...

📺 Vailskibum

👁️ 95K • 👍 4K • 💬 818 • ⏱️ 3:06 • 5h ago

---

---

## HuggingFace Models: 🔥 Trending

**[NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)**

*NVIDIA*

NVIDIA-Nemotron-3.5-Transcribe-30B-A4B is a multilingual speech LLM supporting 40 languages for transcription, speech translation, and audio QA, with a 65,536-token context for long-form audio processing.

`automatic-speech-recognition` `33.7B`

⬇️ 44,939 • ❤️ 1,491 • 6d ago

---

**[DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)**

*DeepSeek*

DeepSeek-V4.1-Flash-1017 is an image-text-to-text model that enhances reasoning, coding, and agentic tasks with reduced execution time and output length. It excels in benchmarks like HLE, Terminal-Bench, and ProgramBench, offering improved performance-cost efficiency for complex applications.

`image-text-to-text` `763.2B`

⬇️ 221,621 • ❤️ 5,271 • 18d ago

---

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 14,613 • ❤️ 619 • 6d ago

---

**[LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B)**

*Liquid AI*

LFM3-1.7B is a 1.73B parameter text model optimized for edge devices and local agents, featuring a 256K context window and multi-language support. It excels at agentic tasks, tool calling, and domain-specific fine-tuning, with low memory requirements (approx. 1GB at 4-bit precision).

`text-generation` `1.7B`

⬇️ 54,959 • ❤️ 1,485 • 1d ago

---

**[Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)**

*Mistral*

Mistral Large 4 is a 1T parameter, natively multimodal Mixture-of-Experts model supporting text and image inputs with a 1M context length. It excels in instruction following, reasoning, coding, and agentic workflows, with strong performance in cybersecurity, finance, and law, and state-of-the-art visual grounding.

`image-text-to-text`

⬇️ 8,200 • ❤️ 1,591 • 2d ago

---

**[Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)**

*Moonshot AI*

Kimi K3.1 Pro is a 2.8T MoE multimodal agentic model with a 1M token context window, excelling in coding, 3D creation, and financial research through advanced attention mechanisms and large-scale joint reinforcement learning.

`image-text-to-text` `2780.1B`

⬇️ 797 • ❤️ 510 • 2d ago

---

**[Pika-H3-Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex)**

*Pika-Labs*

Pika-H3-Flex is an image-to-video diffusion model that generates high-fidelity, temporally coherent videos from static images. It excels at precise camera motion control, maintaining subject consistency, and adapting to various artistic styles, making it ideal for creative video production and visual storytelling.

`image-to-video` `33.1B`

⬇️ 749 • ❤️ 429 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a versatile diffusion model capable of image-to-video, text-to-video, and video-to-video generation, offering advanced control for creative applications.

`image-to-video`

⬇️ 2,493,402 • ❤️ 10,619 • 24d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 123,321 • ❤️ 655 • 1d ago

---

**[numbat](https://huggingface.co/burner22/numbat)**

*burner*

Numbat is a massive ~14T parameter, 114-layer causal language model featuring a hybrid GDN/MLA architecture with Mixture-of-Experts (MoE) and Multi-Token Prediction (MTP). This mid-pretraining checkpoint, derived from Anthropic's Mythos-class training runs, is suitable for research and experimentation in large-scale language modeling.

`6849.4B`

⬇️ 8,118 • ❤️ 342 • 11d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 13 • 💬 2 • ⭐ 4,746 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 161 • 💬 6 • ⭐ 120,577 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 63 • 💬 4 • ⭐ 46,814 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**

*Shuo Yang, Xiaoze Fan, Melissa Pan et al. (11 authors)*

🏢 University of California, Berkeley

FreeToken is an edge-native Mixture-of-Experts serving system that dynamically maps computation and model state onto heterogeneous local hardware to run large open-weight models on personal machines.

▲ 110 • 💬 2 • ⭐ 16,573 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2608.16157) • [💻 code](https://github.com/FlashML-org/FreeToken) • [🔗 project](https://www.flashml.ai/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 67 • 💬 4 • ⭐ 22,669 • 27d ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://huggingface.co/papers/2611.01560)**

*Jiarui Yuan, Yuxin Zuo, Xiaoyu Huang et al. (28 authors)*

Uni-robot-agent enables open-weight robot-use agents to surpass proprietary models in zero-shot manipulation and suggests joint development of four core capabilities for future training.

▲ 43 • 💬 1 • ⭐ 196 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2611.01560) • [💻 code](https://github.com/Open-RUA/uni-robot-agent) • [🔗 project](https://openrua.ai/uni-robot-agent)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 104 • 💬 7 • ⭐ 30,541 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Differentiable Data Augmentation with Kornia](https://huggingface.co/papers/2011.09832)**

*Jian Shi, Edgar Riba, Dmytro Mishkin et al. (5 authors)*

This paper reviews the Kornia differentiable data augmentation module for both 2D and 3D tensors, integrating with PyTorch's autograd and optim, and benchmarks it against other frameworks.

▲ 1 • 💬 0 • ⭐ 12,328 • 72mo ago

[🎓 arXiv](https://arxiv.org/abs/2011.09832) • [💻 code](https://github.com/arraiyopensource/kornia)

---

**[WeVisOne-VL: Unified Visual Perception from Objects to Pixels](https://huggingface.co/papers/2610.31329)**

*Tianming Liang, Junyi Pan, Yuxi Li et al. (8 authors)*

🏢 Tencent

WeVisOne-VL unifies object-level and pixel-level visual perception via structured token prediction, supporting detection, localization, counting, OCR, segmentation, and matting with a lightweight pixel decoder and multi-stage training.

▲ 44 • 💬 4 • ⭐ 909 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2610.31329) • [💻 code](https://github.com/Tencent/WeVisOne-VL) • [🔗 project](https://tencent.github.io/WeVisOne-VL)

---

**[SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding](https://huggingface.co/papers/2611.02501)**

*Kunjun Li, Wenhao Chai, Yihao Liang et al. (10 authors)*

🏢 University of California, Berkeley

SpecPilot autonomously discovers deployment-specific algorithms and system optimizations to maximize speculative decoding speedups across diverse models, drafters, and serving regimes without quality loss.

▲ 16 • 💬 2 • ⭐ 82 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2611.02501) • [💻 code](https://github.com/StargazerX0/SpecPilot) • [🔗 project](https://stargazerx0.github.io/specpilot-project-page/)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 16.6k • 🔱 1.7k • 6d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 8.7k • 🔱 432 • 3d ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 6.7k • 🔱 1.4k • 6h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 6.3k • 🔱 576 • 18h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 6.0k • 🔱 1.5k • 17h ago

---

**[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)**

Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

`C` `ai-agent` `airplay` `automation` `computer-use` `esp32`

⭐ 4.4k • 🔱 588 • 6h ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 3.9k • 🔱 247 • 13d ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 2.7k • 🔱 30 • 7h ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (Blind LLM Agents) — Adversarial defense shield that protects binaries, Electron apps, JS bundles, Python, and WebAssembly against AI reverse-engineering agents like REA. Poison -> Exhaust -> Hallucinate.

`TypeScript` `adversarial-ai` `claude-code` `cursor` `electron-security` `llm-security`

⭐ 2.3k • 🔱 305 • 8h ago

---

**[paipiange/nvzhuang](https://github.com/paipiange/nvzhuang)**

1407 张 AI 女装参考图集与虚拟试穿网站，支持中英检索、OpenAI Images / Gemini / 豆包及自定义 Base URL、API Key、模型。https://github.com/paipiange/nvzhuang

`HTML`

⭐ 2.2k • 🔱 556 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*

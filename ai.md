---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-11T14:20:36.300532+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 11, 2026 at 14:20 UTC  
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

**[Geoffrey Hinton says LLMs are no longer just predicting the next word - new models learn by reasoning and identifying contradictions in their own logic. This unbounded self-improvement will "end up making it much smarter than us."](https://www.reddit.com/r/artificial/comments/1q9an1z/geoffrey_hinton_says_llms_are_no_longer_just/)**

20h ago

---

**[One-Minute Daily AI News 1/10/2026](https://www.reddit.com/r/artificial/comments/1q9rf5i/oneminute_daily_ai_news_1102026/)**

Meta signs nuclear energy deals to power Prometheus AI supercluster.[1] OpenAI is reportedly asking contractors to upload real work from past jobs.[2] Meta and Harvard Researchers Introduce the Confucius Code Agent (CCA): A Software Engineering Agent that can Operate at Large-Scale Codebases.[3] X could face UK ban over deepfakes, minister says.[4] Sources: [1] https://www.cnbc.com/2026/01/09/meta-signs-nuclear-energy-deals-to-power-prometheus-ai-supercluster.html [2] https://techcrunch.com/2026/01/10/openai-is-reportedly-asking-contractors-to-upload-real-work-from-past-jobs/ [3] https://www.marktechpost.com/2026/01/09/meta-and-harvard-researchers-introduce-the-confucius-code-agent-cca-a-software-engineering-agent-that-can-operate-at-large-scale-codebases/ [4] https://www.bbc.com/news/articles/c99kn52nx9do

8h ago

---

**[Alignment tax isn’t global: a few attention heads cause most capability loss](https://www.reddit.com/r/artificial/comments/1q9c1qr/alignment_tax_isnt_global_a_few_attention_heads/)**

Safety alignment in Large Language Models (LLMs) inherently presents a multi-objective optimization conflict, often accompanied by an unintended degradation of general capabilities. Existing mitigation strategies typically rely on global gradient geometry to resolve these conflicts, yet they overlook Modular Heterogeneity within Transformers, specifically that the functional sensitivity and degree of conflict vary substantially across different attention heads. Such global approaches impose uniform update rules across all parameters, often resulting in suboptimal trade-offs by indiscriminately updating utility sensitive heads that exhibit intense gradient conflicts. To address this limitation, we propose Conflict-Aware Sparse Tuning (CAST), a framework that integrates head-level diagnosis with sparse fine-tuning. CAST first constructs a pre-alignment conflict map by synthesizing Optimization Conflict and Functional Sensitivity, which then guides the selective update of parameters. Experiments reveal that alignment conflicts in LLMs are not uniformly distributed. We find that the drop in general capabilities mainly comes from updating a small group of ``high-conflict'' heads. By simply skipping these heads during training, we significantly reduce this loss without compromising safety, offering an interpretable and parameter-efficient approach to improving the safety-utility trade-off.

🔗 [arXiv.org](https://www.arxiv.org/abs/2601.04262) • 19h ago

---

**[A deep dive into how I trained an edit model to show highly relevant code suggestions while programming](https://www.reddit.com/r/artificial/comments/1q9ai6f/a_deep_dive_into_how_i_trained_an_edit_model_to/)**

This is def interesting for all SWEs who would like to know what goes behind the scenes in your code editor when you hit `Tab`. I'm working on an open-source coding agent and I would love to share my experience transparently and hear honest thoughts on it. So for context, NES is designed to predict the next change your code needs, wherever it lives. Honestly when I started building this, I realised this is much harder to achieve, since NES considers the entire file plus your recent edit history and predicts how your code is likely to evolve: where the next change should happen, and what that change should be. Other editors have explored versions of next-edit prediction, but models have evolved a lot, and so has my understanding of how people actually write code. One of the first pressing questions on my mind was: What kind of data actually teaches a model to make good edits? It turned out that real developer intent is surprisingly hard to capture. As anyone who’s peeked at real commits knows, developer edits are messy. Pull requests bundle unrelated changes, commit histories jump around, and the sequences of edits often skip the small, incremental steps engineers actually take when exploring or fixing code. To train an edit model, I formatted each example using special edit tokens. These tokens are designed to tell the model: - What part of the file is editable - The user’s cursor position - What the user has edited so far - What the next edit should be inside that region only Unlike chat-style models that generate free-form text, I trained NES to predict the next code edit inside the editable region. So for eg, when the developer makes the first edit it allows the model to capture the intent of the user. The `editable_region` markers define everything between them as the editable zone. The `user_cursor_is_here` token shows the model where the user is currently editing. NES infers the transformation pattern (capitalization in this case) and applies it consistently as the next edit sequence. To support this training format, I used CommitPackFT and Zeta as data sources. I normalized this unified dataset into the same Zeta-derived edit-markup format as described above and applied filtering to remove non-sequential edits using a small in-context model (GPT-4.1 mini). Now that I had the training format and dataset finalized, the next major decision was choosing what base model to fine-tune. Initially, I considered both open-source and managed models, but ultimately chose Gemini 2.5 Flash Lite for two main reasons: - Easy serving: Running an OSS model would require me to manage its inference and scalability in production. For a feature as latency-sensitive as Next Edit, these operational pieces matter as much as the model weights themselves. Using a managed model helped me avoid all these operational overheads. - Simple supervised-fine-tuning: I fine-tuned NES using Google’s Gemini Supervised Fine-Tuning (SFT) API, with no training loop to maintain, no GPU provisioning, and at the same price as the regular Gemini inference API. Under the hood, Flash Lite uses LoRA (Low-Rank Adaptation), which means I need to update only a small set of parameters rather than the full model. This keeps NES lightweight and preserves the base model’s broader coding ability. Overall, in practice, using Flash Lite gave me model quality comparable to strong open-source baselines, with the obvious advantage of far lower operational costs. This keeps the model stable across versions. And on the user side, using Flash Lite directly improves the user experience in the editor. As a user, you can expect faster responses and likely lower compute cost (which can translate into cheaper product). And since fine-tuning is lightweight, I can roll out frequent improvements, providing a more robust service with less risk of downtime, scaling issues, or version drift; meaning greater reliability for everyone. Next, I evaluated the edit model using a single metric: LLM-as-a-Judge, powered by Gemini 2.5 Pro. This judge model evaluates whether a predicted edit is semantically correct, logically consistent with recent edits, and appropriate for the given context. This is unlike token-level comparisons and makes it far closer to how a human engineer would judge an edit. In practice, this gave me an evaluation process that is scalable, automated, and far more sensitive to intent than simple string matching. It allowed me to run large evaluation suites continuously as I retrain and improve the model. But training and evaluation only define what the model knows in theory. To make Next Edit Suggestions feel alive inside the editor, I realised the model needs to understand what the user is doing right now. So at inference time, I give the model more than just the current file snapshot. I also send - User's recent edit history: Wrapped in `<|edit_history|>`, this gives the model a short story of the user's current flow: what changed, in what order, and what direction the code seems to be moving. - Additional semantic context: Added via `<|additional_context|>`, this might include type signatures, documentation, or relevant parts of the broader codebase. It’s the kind of stuff you would mentally reference before making the next edit. The NES combines these inputs to infer the user’s intent from earlier edits and predict the next edit inside the editable region only. I'll probably write more into how I constructed, ranked, and streamed these dynamic contexts. But would love to hear feedback and is there anything I could've done better

20h ago

---

**[Terrence Tao: "Erdos problem #728 was solved more or less autonomously by AI"](https://www.reddit.com/r/artificial/comments/1q8qvey/terrence_tao_erdos_problem_728_was_solved_more_or/)**

"Recently, the application of AI tools to Erdos problems passed a milestone: an Erdos problem (#728) was solved more or less autonomously by AI (after some feedback from an initial attempt), in the spirit of the problem (as reconstructed by the Erdos problem website community), with the result (to the best of our knowledge) not replicated in existing literature (although similar results proven by similar methods were located). This is a demonstration of the genuine increase in capability of these tools in recent months, and is largely consistent with other recent demonstrations of AI using existing methods to resolve Erdos problems, although in most previous cases a solution to these problems was later located in the literature, as discussed in https://mathstodon.xyz/deck/@tao/115788262274999408 . This particular case was unusual in that the problem as stated by Erdos was misformulated, with a reconstruction of the problem in the intended spirit only obtained in the last few months, which helps explain the lack of prior literature on the problem. However, I would like to talk here about another aspect of the story which I find more interesting than the solution itself, which is the emerging AI-powered capability to rapidly write and rewrite expositions of the solution. [...] My preference would still be for the final writeup for this result to be primarily human-generated in the most essential portions of the paper, though I can see a case for delegating routine proofs to some combination of AI-generated text and Lean code. But to me, the more interesting capability revealed by these events is the ability to rapidly write and rewrite new versions of a text as needed, even if one was not the original author of the argument. This is sharp contrast to existing practice where the effort required to produce even one readable manuscript is quite time-consuming, and subsequent revisions (in response to referee reports, for instance) are largely confined to local changes (e.g., modifying the proof of a single lemma), with large-scale reworking of the paper often avoided due both to the work required and the large possibility of introducing new errors. However, the combination of reasonably competent AI text generation and modification capabilities, paired with the ability of formal proof assistants to verify the informal arguments thus generated, allows for a much more dynamic and high-multiplicity conception of what a writeup of an argument is, with the ability for individual participants to rapidly create tailored expositions of the argument at whatever level of rigor and precision is desired." -- Terrence Tao

🔗 [Mathstodon](https://mathstodon.xyz/@tao/115855840223258103) • 1d ago

---

**[X Restricts Grok's Image Generation to Paid Users After Global Backlash](https://www.reddit.com/r/artificial/comments/1q8v56s/x_restricts_groks_image_generation_to_paid_users/)**

X has restricted Grok’s image generation feature to paid subscribers after global backlash over deepfake and explicit AI images.

🔗 [techputs](https://techputs.com/x-restricts-groks-image-generation-paid-users/) • 1d ago

---

**[Is the Scrabble world champion (Nigel Richards) an example of the Searle's Chinese room](https://www.reddit.com/r/artificial/comments/1q8pj70/is_the_scrabble_world_champion_nigel_richards_an/)**

I'm currently in my undergraduate degree and I have been studying AI ethics under one of my professors for a while. I always have been a partisan of Searle's strong AI and I never really found the chinese room argument compelling. Personally I found that the systems argument against the chinese room to make a lot of sense. My first time reading "Minds, Brains, and Programs" I thought Searle's rebuttal was not very well structured and I found it a little logically incorrect. He mentions that if you take away the room and allow the person to internalize all the things inside the system, that he still will not have understanding--and that no part of the system can have understanding since he is the entire system. I always was confused on why he cannot have understanding, since I imagine this kind of language theatrics is very similar to how we communicate; I couldn't understand how this means artificial intelligence cannot have true understanding. Now on another read I was able to draw some parallels to Nigel Richards--the man who won the french scrabble championship by memorizing the french dictionary. I havent seen anyone talk about this online so I just want to propose a few questions: Does Nigel Richards have an understanding of the french language ? Does Nigel serve as a de facto chinese room ? What is different between Nigel's understanding of the french language compared to a native speaker? Do you think that this is similar to how people accredit LLMs' to simple prediction machines? And finally, would an LLM have a better or worse understanding of language in comparison to Nigel? ⁠What does this mean when it comes to the our ideas of consciousness? Do we humanize the idea of thinking too much when maybe (like the example) we are more similar to LLMs than previously thought?

1d ago

---

**[Google Gemini 3 Pro just verified a forensic protocol I ran. Here's what happened.](https://www.reddit.com/r/artificial/comments/1q8zz2j/google_gemini_3_pro_just_verified_a_forensic/)**

Google Gemini 3 Pro just verified a forensic protocol I ran. Here's what happened. I used Gemini's highest reasoning mode (Pro) to run a recursive forensic investigation payload designed to test the validity of widespread online claims. The protocol: Rejects repetition as evidence Strips unverifiable claims Confirms only primary source data (case numbers, records, etc.) Maps fabrication patterns Generates a layer-by-layer breakdown from origin to spread I ran it on Gemini with no prior training, bias, or context provided. It returned a complete report analyzing claims from scratch. No bias. No assumptions. Just structured verification. Full report (Gemini output): https://gemini.google.com/share/1feed6565f52 Payload (run it in any AI to reproduce results): https://docs.google.com/document/d/1-hsp8dPMuLIsnv1AxJPNN2B7L-GWhoQKCd7esU8msjQ/edit?usp=drivesdk Key takeaways from the Gemini analysis: Allegations repeated across platforms lacked primary source backing No case numbers, medical records, or public filings were found for key claims Verified data pointed to a civil dispute—not criminal activity A clear pattern of repetition-without-citation emerged It even outlined how claims spread and identified which lacked verifiable origin. This was done using public tools—no backend access, no court databases, no manipulation. Just the protocol + clean input = verified output. If you've ever wondered whether AI can actually verify claims at the forensic level: It can. And it just did.

🔗 [Google Docs](https://docs.google.com/document/d/1-hsp8dPMuLIsnv1AxJPNN2B7L-GWhoQKCd7esU8msjQ/edit?usp=drivesdk) • 1d ago

---

**[Musk lawsuit over OpenAI for-profit conversion can go to trial, US judge says](https://www.reddit.com/r/artificial/comments/1q82r2v/musk_lawsuit_over_openai_forprofit_conversion_can/)**

Judge says there is plenty of evidence to suggest OpenAI’s leaders made assurances nonprofit structure would be kept

🔗 [the Guardian](https://www.theguardian.com/technology/2026/jan/08/elon-musk-openai-lawsuit-for-profit-conversion-can-go-to-trial-us-judge-says) • 2d ago

---

**[Building adaptive routing logic in Go for an Open source LLM gateway - Bifrost](https://www.reddit.com/r/artificial/comments/1q8um17/building_adaptive_routing_logic_in_go_for_an_open/)**

Working on an LLM gateway (Bifrost)- Code is open source: https://github.com/maxim-ai/bifrost, ran into an interesting problem: how do you route requests across multiple LLM providers when failures happen gradually? Traditional load balancing assumes binary states – up or down. But LLM API degradations are messy. A region starts timing out, some routes spike in errors, latency drifts up over minutes. By the time it's a full outage, you've already burned through retries and user patience. Static configs don't cut it. You can't pre-model which provider/region/key will degrade and how. The challenge: build adaptive routing that learns from live traffic and adjusts in real time, with <10µs overhead per request. Had to sit on the hot path without becoming the bottleneck. Why Go made sense: Needed lock-free scoring updates across concurrent requests EWMA (exponentially weighted moving averages) for smoothing signals without allocations Microsecond-level latency requirements ruled out Python/Node Wanted predictable GC pauses under high RPS How it works: Each route gets a continuously updated score based on live signals – error rates, token-adjusted latency outliers (we call it TACOS lol), utilization, recovery momentum. Routes traffic from top-scoring candidates with lightweight exploration to avoid overfitting to a single route. When it detects rate-limit hits (TPM/RPM), it remembers and allocates just enough traffic to stay under limits going forward. Automatic fallbacks to healthy routes when degradation happens. Result: <10µs overhead, handles 5K+ RPS, adapts to provider issues without manual intervention. Running in production now. Curious if others have tackled similar real-time scoring/routing problems in Go where performance was critical?

1d ago

---

---

## Google News: "ai"

**[‘Dangerous and alarming’: Google removes some of its AI summaries after users’ health put at risk](https://www.theguardian.com/technology/2026/jan/11/google-ai-overviews-health-guardian-investigation)**

Guardian investigation finds AI Overviews provided inaccurate and false information when queried over blood tests

The Guardian • 4h ago

---

**[AI Is Causing a Memory Shortage. Why Producers Aren’t Rushing to Make a Lot More.](https://www.wsj.com/tech/ai-is-causing-a-memory-shortage-why-producers-arent-rushing-to-make-a-lot-more-8dd15194?gaa_at=eafs&gaa_n=AWEtsqdYxqZaI4dDtPm-0iDQ_h2rjMCa8V4BnT_nFK7rOyK-dR85oAKhLezP&gaa_ts=6963b517&gaa_sig=SP0XV9X2DhHooKdGe8fREO-SK5lna0LpN5x4RqEue9NvL9X4AO_w4yCMKci95gdd_Us69kvzM6ob-yiYl2s0sQ%3D%3D)**

The Wall Street Journal • 3h ago

---

**[These 8 stocks could form the backbone of AI as chips get more powerful](https://www.marketwatch.com/story/these-8-stocks-could-form-the-backbone-of-ai-as-chips-get-more-powerful-e0b87fe7?gaa_at=eafs&gaa_n=AWEtsqcGQzvTLHZhPnd3QMH1CaP9D8D66TBsnIA_4Wta34cqfY7X-HhhK7Gc&gaa_ts=6963b517&gaa_sig=5kdsfBCvBnbvBX6HWKZXyJ-osf4QLTq8IfQh1w_jIBjFw9AL4llOlRhK65-fAIXj6dbgO-EMmQaM26ZE-_ljgw%3D%3D)**

MarketWatch • 1d ago

---

**[New Data Shows AI Stocks Beat the S&P 500 by 136% Over 5 Years](https://www.fool.com/investing/2026/01/11/new-data-shows-ai-stocks-beat-sp-500-tesla/)**

Here's why this should make investors confident in buying AI stocks.

The Motley Fool • 50m ago

---

**[7 Genius AI Stocks Billionaire Chase Coleman Owns That Investors Should Buy for 2026](https://www.fool.com/investing/2026/01/11/7-genius-ai-stocks-billionaire-chase-coleman-owns/)**

Following what billionaires think about AI can be a smart move.

The Motley Fool • 37m ago

---

**[‘Add blood, forced smile’: how Grok’s nudification tool went viral](https://www.theguardian.com/news/ng-interactive/2026/jan/11/how-grok-nudification-tool-went-viral-x-elon-musk)**

The ‘put her in a bikini’ trend rapidly evolved into hundreds of thousands of requests to strip clothes from photos of women, horrifying those targeted

The Guardian • 8h ago

---

**[Grok, Elon Musk’s A.I., Is Generating Sexualized Images of Real People, Fueling Outrage](https://www.nytimes.com/2026/01/09/technology/grok-deepfakes-ai-x.html)**

The New York Times • 2d ago

---

**[Musk’s Grok AI Blocked in Indonesia, Malaysia Over Sexual Images](https://www.bloomberg.com/news/articles/2026-01-11/musk-s-grok-ai-blocked-in-indonesia-malaysia-over-sexual-images)**

Bloomberg.com • 43m ago

---

**[AI is helping recruiters find ‘hidden gem’ talent — a senior LinkedIn exec shares top tips to stand out](https://www.cnbc.com/2026/01/11/ai-dominate-hiring-2026-linkedin-execs-top-tips-stand-out.html)**

"2026 is the year of more widespread adoption of AI tools, particularly in hiring," Janine Chamberlin, LinkedIn's UK Country Manager told CNBC Make It.

CNBC • 7h ago

---

**[China AI Leaders Warn of Widening Gap With US After $1B IPO Week](https://finance.yahoo.com/news/china-ai-leaders-warn-widening-140555407.html)**

“A massive amount of OpenAI’s compute is dedicated to next-generation research, whereas we are stretched thin — just meeting delivery demands consumes most of our resources,” Lin said during a panel at the AGI-Next summit in Beijing on Saturday.  The event, co-organized by Zhipu and Tsinghua University, followed market debuts this week in which Zhipu and Shanghai-based MiniMax Group collectively raised more than $1 billion.

Yahoo Finance • 1d ago

---

---

## HackerNews: "ai"

**[Google AI Studio is now sponsoring Tailwind CSS](https://news.ycombinator.com/item?id=46545077)**

⬆️ 769 • 💬 290 • 2d ago • [X (formerly Twitter)](https://twitter.com/OfficialLoganK/status/2009339263251566902)

---

**[“Erdos problem #728 was solved more or less autonomously by AI”](https://news.ycombinator.com/item?id=46560445)**

Recently, the application of AI tools to Erdos problems passed a milestone: an Erdos problem (#728 https://www.erdosproblems.com/728) was solved more or less autonomously by AI (after some feedback from an initial attempt), in the spirit of the problem (as reconstructed by the Erdos problem website community), with the result (to the best of our knowledge) not replicated in existing literature (although similar results proven by similar methods were located).

This is a demonstration of the genuine increase in capability of these tools in recent months, and is largely consistent with other recent demonstrations of AI using existing methods to resolve Erdos problems, although in most previous cases a solution to these problems was later located in the literature, as discussed in https://mathstodon.xyz/deck/@tao/115788262274999408 .  This particular case was unusual in that the problem as stated by Erdos was misformulated, with a reconstruction of the problem in the intended spirit only obtained in the last few months, which helps explain the lack of prior literature on the problem.  However, I would like to talk here about another aspect of the story which I find more interesting than the solution itself, which is the emerging AI-powered capability to rapidly write and rewrite expositions of the solution.  (1/5)

⬆️ 606 • 💬 349 • 1d ago • [Mathstodon](https://mathstodon.xyz/@tao/115855840223258103)

---

**[AI coding assistants are getting worse?](https://news.ycombinator.com/item?id=46542036)**

One AI coding assistant power user says the tools are hitting a plateau, and some are even declining. What's causing this unexpected twist in tech?

⬆️ 445 • 💬 731 • 2d ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-coding-degrades)

---

**[AI is a business model stress test](https://news.ycombinator.com/item?id=46567392)**

AI commoditizes anything you can specify. It can't commoditize what you have to operate.

⬆️ 282 • 💬 270 • 21h ago • [dri.es](https://dri.es/ai-is-a-business-model-stress-test)

---

**[IBM AI ('Bob') Downloads and Executes Malware](https://news.ycombinator.com/item?id=46544454)**

IBM's AI coding agent 'Bob' has been found vulnerable to downloading and executing malware without human approval through command validation bypasses exploited using indirect prompt injection.

⬆️ 261 • 💬 120 • 2d ago • [promptarmor.com](https://www.promptarmor.com/resources/ibm-ai-(-bob-)-downloads-and-executes-malware)

---

**[Don't fall into the anti-AI hype](https://news.ycombinator.com/item?id=46574276)**

⬆️ 196 • 💬 313 • 3h ago • [antirez.com](https://antirez.com/news/158)

---

**[My article on why AI is great (or terrible) or how to use it](https://news.ycombinator.com/item?id=46557057)**

Senior engineers are best positioned to benefit from AI. We're good enough to avoid slop, and there's so much we can accomplish. I wouldn't go back.

⬆️ 162 • 💬 227 • 1d ago • [matthewrocklin.com](https://matthewrocklin.com/ai-zealotry/)

---

**[Side-by-side comparison of how AI models answer moral dilemmas](https://news.ycombinator.com/item?id=46547024)**

⬆️ 94 • 💬 60 • 2d ago • [civai.org](https://civai.org/p/ai-values)

---

**[Grok turns off image generator for most after outcry over sexualised AI imagery](https://news.ycombinator.com/item?id=46551238)**

X to limit editing function to paying subscribers after platform threatened with fines and regulatory action

⬆️ 76 • 💬 91 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/jan/09/grok-image-generator-outcry-sexualised-ai-imagery)

---

**[Show HN: EuConform – Offline-first EU AI Act compliance tool (open source)](https://news.ycombinator.com/item?id=46557823)**

EU AI Act Compliance Tool - Risk classification and bias testing - Hiepler/EuConform

⬆️ 71 • 💬 45 • 1d ago • [GitHub](https://github.com/Hiepler/EuConform)

---

---

## YouTube Videos: "ai"

**[I Ranked the Best AI Tools to Make Money in 2026](https://www.youtube.com/watch?v=xXxrvra9DQg)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/44Z7YRm Are you building an AI software ...

📺 Dan Martell

👁️ 74K • 👍 4K • 💬 311 • ⏱️ 19:15 • 2d ago

---

**[The Shocking AI Reveals That Stunned CES 2026 (DAY 2)](https://www.youtube.com/watch?v=9kdw6hLFFss)**

Day 2 of CES 2026 was all about Physical AI, real machines doing real work. From NEURA's refined humanoids and AgiBot's full ...

📺 AI Revolution

👁️ 97K • 👍 2K • 💬 68 • ⏱️ 17:54 • 2d ago

---

**[The Biggest AI News Updates Were NOT at CES](https://www.youtube.com/watch?v=LhpCVkDpYZM)**

LTX 2 Open-Source has officially launched! Explore the open-source release today: https://ltx.io/model I thought this week would ...

📺 Matt Wolfe

👁️ 42K • 👍 2K • 💬 165 • ⏱️ 14:39 • 1d ago

---

**[Grandma Shocked When Elephant Takes Her Birthday Cake 😭 #ai #baby #save](https://www.youtube.com/watch?v=RHgca5PX6rg)**

Grandma Shocked When Elephant Takes Her Birthday Cake #ai #baby #save #CuteElephant #ElephantStealsCake ...

📺 rk kahaniyaa

👁️ 385 • 👍 8 • 💬 1 • ⏱️ 0:26 • 33m ago

---

**[AI tutor agents, omnimodal video models, LTX-2 updates, long-term memory, video faceswap: AI NEWS](https://www.youtube.com/watch?v=qOr5-FrkElk)**

HUGE AI NEWS: LTX-2, UniVideo, SimpleMem, HY-MT, NeoVerse & more #ai #ainews #aitools #aivideo Thanks to our sponsor ...

📺 AI Search

👁️ 33K • 👍 2K • 💬 178 • ⏱️ 35:41 • 10h ago

---

**[Nvidia&#39;s Jensen Huang on an AI Bubble, Trump, and the Arms Race with China](https://www.youtube.com/watch?v=s4haopj2XeA)**

00:00 Intro 00:48 AI Bubble 03:30 Working with President Trump 05:17 AI Arms Race with China 13:13 Taiwan's Future 18:02 ...

📺 TIME

👁️ 81K • 👍 3K • 💬 350 • ⏱️ 24:32 • 1d ago

---

**[This Is the Most Powerful AI Agent I’ve Ever Used (Manus 1.6 Max)](https://www.youtube.com/watch?v=Oh84cPhtmFA)**

Manus AI is one of the most underrated AI tools, and this update takes it to another level. Manus 1.6 Max can now build full mobile ...

📺 Brock Mesarich | AI for Non Techies

👁️ 1K • 👍 46 • 💬 7 • ⏱️ 13:47 • 22h ago

---

**[All Premium AI Models in One Place – Totally FREE](https://www.youtube.com/watch?v=XYaeOMqvjtg)**

Hey Guys! All Premium AI Models in One Place – Totally FREE is what this video is all about. In this video, you will discover a ...

📺 Faisal Shabbir

👁️ 9K • 👍 867 • 💬 87 • ⏱️ 5:03 • 1d ago

---

**[How do we compare to the Ai babies? 👶🕺😂](https://www.youtube.com/watch?v=y2bVXq1mdfQ)**

📺 The Williams Fam

👁️ 222K • 👍 6K • 💬 286 • ⏱️ 0:16 • 21h ago

---

**[Reacting to our OWN AI VIDEOS!](https://www.youtube.com/watch?v=QtgKP5oyJJs)**

Use my code https://factor.yt.link/T0BOsoa for 50% off your first box + Free Breakfast for 1 year! T&C apply. Reacting to our OWN ...

📺 MoreBeckBros

👁️ 193K • 👍 8K • 💬 678 • ⏱️ 26:17 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 629,855 • ❤️ 780 • 3d ago

---

**[HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B)**

*Tencent*

HY-MT1.5-1.8B is a 1.8B parameter translation model supporting 33 languages, offering high-speed, high-quality translation comparable to larger models. It is optimized for edge device deployment and real-time scenarios, with capabilities for terminology intervention, contextual translation, and formatted translation.

`translation` `2.0B`

⬇️ 9,771 • ❤️ 711 • 10d ago

---

**[Qwen-Image-Edit-2511-Multiple-Angles-LoRA](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA)**

*fal*

This LoRA fine-tunes Qwen-Image-Edit-2511 for precise multi-angle image generation, offering 96 camera poses (4 elevations, 8 azimuths, 3 distances) trained on Gaussian Splatting data for 3D consistency. It enables detailed control over camera viewpoints, including low-angle shots, for advanced image editing and content creation.

`image-to-image`

⬇️ 16,027 • ❤️ 400 • 3d ago

---

**[nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)**

*NVIDIA*

Nemotron-Speech-Streaming-En-0.6b is a 600M parameter English ASR model featuring a cache-aware FastConformer-RNNT architecture for low-latency streaming and high-throughput batch processing. It supports dynamic chunk sizes, punctuation, and capitalization, making it ideal for real-time applications like voice assistants and live captioning.

`automatic-speech-recognition`

⬇️ 2,257 • ❤️ 284 • 5d ago

---

**[LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)**

*Liquid AI*

LFM2.5-1.2B-Instruct is a 1.2B parameter instruction-tuned language model optimized for on-device deployment, offering fast edge inference and supporting multiple languages. It excels at agentic tasks and data extraction, with a context length of 32,768 tokens.

`text-generation` `1.2B`

⬇️ 11,562 • ❤️ 260 • 2d ago

---

**[HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)**

*HyperCLOVA X*

HyperCLOVAX-SEED-Think-32B is a 32B parameter vision-language model capable of multimodal understanding (text, image, video) with a 128K token context length. It excels at Korean-centric reasoning and offers an optional 'thinking mode' for deep, controllable analysis, making it suitable for complex agentic tasks and advanced multimodal QA.

`text-generation` `33.3B`

⬇️ 30,522 • ❤️ 343 • 5d ago

---

**[LFM2.5-Audio-1.5B](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B)**

*Liquid AI*

LFM2.5-Audio-1.5B is an end-to-end audio foundation model enabling real-time speech-to-speech conversational interactions with low latency. It supports interleaved and sequential generation for tasks like ASR, TTS, and seamless chatbot conversations.

`audio-to-audio` `1.5B`

⬇️ 586 • ❤️ 206 • 5d ago

---

**[MiroThinker-v1.5-235B](https://huggingface.co/miromind-ai/MiroThinker-v1.5-235B)**

*MiroMind AI*

MiroThinker-v1.5-235B is a large language model optimized for tool-augmented reasoning and information seeking, featuring interactive scaling for deeper agent-environment interactions. It excels at long-horizon tasks, supporting a 256K context window and up to 400 tool calls, making it ideal for complex research and general QA.

`text-generation` `235.1B`

⬇️ 1,354 • ❤️ 202 • 5d ago

---

**[Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512)**

*Qwen*

Qwen-Image-2512 is a text-to-image diffusion model that excels at generating highly realistic human subjects and detailed natural scenes. It offers improved text rendering and composition, making it suitable for applications requiring high fidelity and naturalistic image generation.

`text-to-image`

⬇️ 23,403 • ❤️ 567 • 11d ago

---

**[MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)**

*MiniMax*

MiniMax-M2.1 is a text generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 207,986 • ❤️ 1,008 • 14d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 170 • 💬 5 • ⭐ 4,362 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 87 • 💬 1 • ⭐ 1,932 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://huggingface.co/papers/2601.02553)**

*Jiaqi Liu, Yaofeng Su, Peng Xia et al. (8 authors)*

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

▲ 21 • 💬 2 • ⭐ 678 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2601.02553) • [💻 code](https://github.com/aiming-lab/SimpleMem) • [🔗 project](https://aiming-lab.github.io/SimpleMem-Page/)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 130 • 💬 18 • ⭐ 49,681 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[VideoRAG: Retrieval-Augmented Generation with Extreme Long-Context
  Videos](https://huggingface.co/papers/2502.01549)**

*Xubin Ren, Lingrui Xu, Long Xia et al. (6 authors)*

VideoRAG enhances large language models for multi-modal video processing with a dual-channel architecture that integrates textual knowledge grounding and multi-modal context encoding.

▲ 2 • 💬 0 • ⭐ 2,294 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.01549) • [💻 code](https://github.com/hkuds/videorag)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 18 • 💬 2 • ⭐ 14,837 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[BitNet b1.58 2B4T Technical Report](https://huggingface.co/papers/2504.12285)**

*Shuming Ma, Hongyu Wang, Shaohan Huang et al. (8 authors)*

BitNet b1.58 2B4T, a 1-bit Large Language Model with 2 billion parameters, matches the performance of full-precision models while improving computational efficiency.

▲ 81 • 💬 2 • ⭐ 25,640 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.12285) • [💻 code](https://github.com/microsoft/bitnet)

---

**[BitNet Distillation](https://huggingface.co/papers/2510.13998)**

*Xun Wu, Shaohan Huang, Wenhui Wang et al. (7 authors)*

🏢 Microsoft Research

BitNet Distillation fine-tunes large language models to 1.58-bit precision using SubLN, multi-head attention distillation, and continual pre-training, achieving comparable performance with significant memory and inference speed improvements.

▲ 57 • 💬 5 • ⭐ 25,640 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.13998) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 4 • 💬 0 • ⭐ 25,640 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://huggingface.co/papers/2403.13372)**

*Yaowei Zheng, Richong Zhang, Junhao Zhang et al. (5 authors)*

LlamaFactory is a unified framework enabling efficient fine-tuning of large language models across various tasks using a web-based user interface.

▲ 176 • 💬 6 • ⭐ 65,394 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.13372) • [💻 code](https://github.com/hiyouga/LLaMA-Factory) • [🔗 project](https://huggingface.co/spaces/hiyouga/LLaMA-Board)

---

---

## GitHub Repositories: "ai"

**[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)**

"DeepTutor: AI-Powered Personalized Learning Assistant"

`Python` `ai-agents` `ai-tutor` `deepresearch` `idea-generation` `interactive-learning`

⭐ 7.8k • 🔱 981 • 1h ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.2k • 🔱 135 • 21m ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 2.2k • 🔱 327 • 3d ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 2.0k • 🔱 221 • 1h ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

从 0 到 1 学会 vibe coding，项目制学习

`ai` `course` `vibe-coding`

⭐ 1.4k • 🔱 120 • 23h ago

---

**[GuDaStudio/skills](https://github.com/GuDaStudio/skills)**

This repository contains a collection of Agent Skills developed by GudaStudio, enabling seamless collaboration between Claude and other AI models and tools.

`PowerShell`

⭐ 1.3k • 🔱 71 • 18d ago

---

**[numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror)**

Create multiple isolated Claude Code variants with custom providers (Z.ai, MiniMax, OpenRouter, LiteLLM)

`TypeScript`

⭐ 1.3k • 🔱 108 • 1d ago

---

**[aiflowy/aiflowy](https://github.com/aiflowy/aiflowy)**

AIFlowy is an enterprise-grade AI application development platform based on Java, comparable to products like Dify and Coze.

`Vue` `agentic-ai` `ai-agent` `aiflowy` `coze` `dify`

⭐ 1.2k • 🔱 143 • 2d ago

---

**[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)**

A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

`agent-skills` `ai-agents` `ai-development` `anthropic` `automation`

⭐ 1.1k • 🔱 84 • 12d ago

---

**[aiclientproxy/proxycast](https://github.com/aiclientproxy/proxycast)**

让 AI 编辑器之间自然流动，不仅仅可以其他工具使用，也可以转换成 api 为本地开发提供动力。

`Rust` `claude` `kiro`

⭐ 1.1k • 🔱 128 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-01-11T08:28:32.962049+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** January 11, 2026 at 08:28 UTC  
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

14h ago

---

**[One-Minute Daily AI News 1/10/2026](https://www.reddit.com/r/artificial/comments/1q9rf5i/oneminute_daily_ai_news_1102026/)**

Meta signs nuclear energy deals to power Prometheus AI supercluster.[1] OpenAI is reportedly asking contractors to upload real work from past jobs.[2] Meta and Harvard Researchers Introduce the Confucius Code Agent (CCA): A Software Engineering Agent that can Operate at Large-Scale Codebases.[3] X could face UK ban over deepfakes, minister says.[4] Sources: [1] https://www.cnbc.com/2026/01/09/meta-signs-nuclear-energy-deals-to-power-prometheus-ai-supercluster.html [2] https://techcrunch.com/2026/01/10/openai-is-reportedly-asking-contractors-to-upload-real-work-from-past-jobs/ [3] https://www.marktechpost.com/2026/01/09/meta-and-harvard-researchers-introduce-the-confucius-code-agent-cca-a-software-engineering-agent-that-can-operate-at-large-scale-codebases/ [4] https://www.bbc.com/news/articles/c99kn52nx9do

2h ago

---

**[Alignment tax isn’t global: a few attention heads cause most capability loss](https://www.reddit.com/r/artificial/comments/1q9c1qr/alignment_tax_isnt_global_a_few_attention_heads/)**

Safety alignment in Large Language Models (LLMs) inherently presents a multi-objective optimization conflict, often accompanied by an unintended degradation of general capabilities. Existing mitigation strategies typically rely on global gradient geometry to resolve these conflicts, yet they overlook Modular Heterogeneity within Transformers, specifically that the functional sensitivity and degree of conflict vary substantially across different attention heads. Such global approaches impose uniform update rules across all parameters, often resulting in suboptimal trade-offs by indiscriminately updating utility sensitive heads that exhibit intense gradient conflicts. To address this limitation, we propose Conflict-Aware Sparse Tuning (CAST), a framework that integrates head-level diagnosis with sparse fine-tuning. CAST first constructs a pre-alignment conflict map by synthesizing Optimization Conflict and Functional Sensitivity, which then guides the selective update of parameters. Experiments reveal that alignment conflicts in LLMs are not uniformly distributed. We find that the drop in general capabilities mainly comes from updating a small group of ``high-conflict'' heads. By simply skipping these heads during training, we significantly reduce this loss without compromising safety, offering an interpretable and parameter-efficient approach to improving the safety-utility trade-off.

🔗 [arXiv.org](https://www.arxiv.org/abs/2601.04262) • 13h ago

---

**[Terrence Tao: "Erdos problem #728 was solved more or less autonomously by AI"](https://www.reddit.com/r/artificial/comments/1q8qvey/terrence_tao_erdos_problem_728_was_solved_more_or/)**

"Recently, the application of AI tools to Erdos problems passed a milestone: an Erdos problem (#728) was solved more or less autonomously by AI (after some feedback from an initial attempt), in the spirit of the problem (as reconstructed by the Erdos problem website community), with the result (to the best of our knowledge) not replicated in existing literature (although similar results proven by similar methods were located). This is a demonstration of the genuine increase in capability of these tools in recent months, and is largely consistent with other recent demonstrations of AI using existing methods to resolve Erdos problems, although in most previous cases a solution to these problems was later located in the literature, as discussed in https://mathstodon.xyz/deck/@tao/115788262274999408 . This particular case was unusual in that the problem as stated by Erdos was misformulated, with a reconstruction of the problem in the intended spirit only obtained in the last few months, which helps explain the lack of prior literature on the problem. However, I would like to talk here about another aspect of the story which I find more interesting than the solution itself, which is the emerging AI-powered capability to rapidly write and rewrite expositions of the solution. [...] My preference would still be for the final writeup for this result to be primarily human-generated in the most essential portions of the paper, though I can see a case for delegating routine proofs to some combination of AI-generated text and Lean code. But to me, the more interesting capability revealed by these events is the ability to rapidly write and rewrite new versions of a text as needed, even if one was not the original author of the argument. This is sharp contrast to existing practice where the effort required to produce even one readable manuscript is quite time-consuming, and subsequent revisions (in response to referee reports, for instance) are largely confined to local changes (e.g., modifying the proof of a single lemma), with large-scale reworking of the paper often avoided due both to the work required and the large possibility of introducing new errors. However, the combination of reasonably competent AI text generation and modification capabilities, paired with the ability of formal proof assistants to verify the informal arguments thus generated, allows for a much more dynamic and high-multiplicity conception of what a writeup of an argument is, with the ability for individual participants to rapidly create tailored expositions of the argument at whatever level of rigor and precision is desired." -- Terrence Tao

🔗 [Mathstodon](https://mathstodon.xyz/@tao/115855840223258103) • 1d ago

---

**[X Restricts Grok's Image Generation to Paid Users After Global Backlash](https://www.reddit.com/r/artificial/comments/1q8v56s/x_restricts_groks_image_generation_to_paid_users/)**

X has restricted Grok’s image generation feature to paid subscribers after global backlash over deepfake and explicit AI images.

🔗 [techputs](https://techputs.com/x-restricts-groks-image-generation-paid-users/) • 1d ago

---

**[A deep dive into how I trained an edit model to show highly relevant code suggestions while programming](https://www.reddit.com/r/artificial/comments/1q9ai6f/a_deep_dive_into_how_i_trained_an_edit_model_to/)**

This is def interesting for all SWEs who would like to know what goes behind the scenes in your code editor when you hit `Tab`. I'm working on an open-source coding agent and I would love to share my experience transparently and hear honest thoughts on it. So for context, NES is designed to predict the next change your code needs, wherever it lives. Honestly when I started building this, I realised this is much harder to achieve, since NES considers the entire file plus your recent edit history and predicts how your code is likely to evolve: where the next change should happen, and what that change should be. Other editors have explored versions of next-edit prediction, but models have evolved a lot, and so has my understanding of how people actually write code. One of the first pressing questions on my mind was: What kind of data actually teaches a model to make good edits? It turned out that real developer intent is surprisingly hard to capture. As anyone who’s peeked at real commits knows, developer edits are messy. Pull requests bundle unrelated changes, commit histories jump around, and the sequences of edits often skip the small, incremental steps engineers actually take when exploring or fixing code. To train an edit model, I formatted each example using special edit tokens. These tokens are designed to tell the model: - What part of the file is editable - The user’s cursor position - What the user has edited so far - What the next edit should be inside that region only Unlike chat-style models that generate free-form text, I trained NES to predict the next code edit inside the editable region. So for eg, when the developer makes the first edit it allows the model to capture the intent of the user. The `editable_region` markers define everything between them as the editable zone. The `user_cursor_is_here` token shows the model where the user is currently editing. NES infers the transformation pattern (capitalization in this case) and applies it consistently as the next edit sequence. To support this training format, I used CommitPackFT and Zeta as data sources. I normalized this unified dataset into the same Zeta-derived edit-markup format as described above and applied filtering to remove non-sequential edits using a small in-context model (GPT-4.1 mini). Now that I had the training format and dataset finalized, the next major decision was choosing what base model to fine-tune. Initially, I considered both open-source and managed models, but ultimately chose Gemini 2.5 Flash Lite for two main reasons: - Easy serving: Running an OSS model would require me to manage its inference and scalability in production. For a feature as latency-sensitive as Next Edit, these operational pieces matter as much as the model weights themselves. Using a managed model helped me avoid all these operational overheads. - Simple supervised-fine-tuning: I fine-tuned NES using Google’s Gemini Supervised Fine-Tuning (SFT) API, with no training loop to maintain, no GPU provisioning, and at the same price as the regular Gemini inference API. Under the hood, Flash Lite uses LoRA (Low-Rank Adaptation), which means I need to update only a small set of parameters rather than the full model. This keeps NES lightweight and preserves the base model’s broader coding ability. Overall, in practice, using Flash Lite gave me model quality comparable to strong open-source baselines, with the obvious advantage of far lower operational costs. This keeps the model stable across versions. And on the user side, using Flash Lite directly improves the user experience in the editor. As a user, you can expect faster responses and likely lower compute cost (which can translate into cheaper product). And since fine-tuning is lightweight, I can roll out frequent improvements, providing a more robust service with less risk of downtime, scaling issues, or version drift; meaning greater reliability for everyone. Next, I evaluated the edit model using a single metric: LLM-as-a-Judge, powered by Gemini 2.5 Pro. This judge model evaluates whether a predicted edit is semantically correct, logically consistent with recent edits, and appropriate for the given context. This is unlike token-level comparisons and makes it far closer to how a human engineer would judge an edit. In practice, this gave me an evaluation process that is scalable, automated, and far more sensitive to intent than simple string matching. It allowed me to run large evaluation suites continuously as I retrain and improve the model. But training and evaluation only define what the model knows in theory. To make Next Edit Suggestions feel alive inside the editor, I realised the model needs to understand what the user is doing right now. So at inference time, I give the model more than just the current file snapshot. I also send - User's recent edit history: Wrapped in `<|edit_history|>`, this gives the model a short story of the user's current flow: what changed, in what order, and what direction the code seems to be moving. - Additional semantic context: Added via `<|additional_context|>`, this might include type signatures, documentation, or relevant parts of the broader codebase. It’s the kind of stuff you would mentally reference before making the next edit. The NES combines these inputs to infer the user’s intent from earlier edits and predict the next edit inside the editable region only. I'll probably write more into how I constructed, ranked, and streamed these dynamic contexts. But would love to hear feedback and is there anything I could've done better

14h ago

---

**[Is the Scrabble world champion (Nigel Richards) an example of the Searle's Chinese room](https://www.reddit.com/r/artificial/comments/1q8pj70/is_the_scrabble_world_champion_nigel_richards_an/)**

I'm currently in my undergraduate degree and I have been studying AI ethics under one of my professors for a while. I always have been a partisan of Searle's strong AI and I never really found the chinese room argument compelling. Personally I found that the systems argument against the chinese room to make a lot of sense. My first time reading "Minds, Brains, and Programs" I thought Searle's rebuttal was not very well structured and I found it a little logically incorrect. He mentions that if you take away the room and allow the person to internalize all the things inside the system, that he still will not have understanding--and that no part of the system can have understanding since he is the entire system. I always was confused on why he cannot have understanding, since I imagine this kind of language theatrics is very similar to how we communicate; I couldn't understand how this means artificial intelligence cannot have true understanding. Now on another read I was able to draw some parallels to Nigel Richards--the man who won the french scrabble championship by memorizing the french dictionary. I havent seen anyone talk about this online so I just want to propose a few questions: Does Nigel Richards have an understanding of the french language ? Does Nigel serve as a de facto chinese room ? What is different between Nigel's understanding of the french language compared to a native speaker? Do you think that this is similar to how people accredit LLMs' to simple prediction machines? And finally, would an LLM have a better or worse understanding of language in comparison to Nigel? ⁠What does this mean when it comes to the our ideas of consciousness? Do we humanize the idea of thinking too much when maybe (like the example) we are more similar to LLMs than previously thought?

1d ago

---

**[Google Gemini 3 Pro just verified a forensic protocol I ran. Here's what happened.](https://www.reddit.com/r/artificial/comments/1q8zz2j/google_gemini_3_pro_just_verified_a_forensic/)**

Google Gemini 3 Pro just verified a forensic protocol I ran. Here's what happened. I used Gemini's highest reasoning mode (Pro) to run a recursive forensic investigation payload designed to test the validity of widespread online claims. The protocol: Rejects repetition as evidence Strips unverifiable claims Confirms only primary source data (case numbers, records, etc.) Maps fabrication patterns Generates a layer-by-layer breakdown from origin to spread I ran it on Gemini with no prior training, bias, or context provided. It returned a complete report analyzing claims from scratch. No bias. No assumptions. Just structured verification. Full report (Gemini output): https://gemini.google.com/share/1feed6565f52 Payload (run it in any AI to reproduce results): https://docs.google.com/document/d/1-hsp8dPMuLIsnv1AxJPNN2B7L-GWhoQKCd7esU8msjQ/edit?usp=drivesdk Key takeaways from the Gemini analysis: Allegations repeated across platforms lacked primary source backing No case numbers, medical records, or public filings were found for key claims Verified data pointed to a civil dispute—not criminal activity A clear pattern of repetition-without-citation emerged It even outlined how claims spread and identified which lacked verifiable origin. This was done using public tools—no backend access, no court databases, no manipulation. Just the protocol + clean input = verified output. If you've ever wondered whether AI can actually verify claims at the forensic level: It can. And it just did.

🔗 [Google Docs](https://docs.google.com/document/d/1-hsp8dPMuLIsnv1AxJPNN2B7L-GWhoQKCd7esU8msjQ/edit?usp=drivesdk) • 22h ago

---

**[Has the global population already been "primed" to mass adopt new innovations like LLM's en masse? The state of tech literacy now vs pre-dotcom bubble](https://www.reddit.com/r/artificial/comments/1q8y053/has_the_global_population_already_been_primed_to/)**

I see most boomers in their 60's and 70's now adept at using smartphones. Young kids today are weened on iPads in place of proper parenting with sports or hobbies or after school activities. Broadband mobile is now an expectation and a no longer a "need" or "want", but sort of a "right". Even the poorest African or South Asian countries have access to mobile broadband. Income is the only dividing factor to the poorest having access to unlimited mobile. But even then, the data cost index is lower in developing countries that the poor can have some access to it. Wi-fi is free and more accessible in some places in poor countries compared to rich countries to make up for the digital divide. Compare this situation to when the bubble popped in 2000's. There were no smartphones, let alone cellphones. Dial-up is the norm. There are still tech today that can die on the vine like VR as they are too geeky. But as far as the subscription model of LLM's, people have gotten used to paying for Netflix or Disney Plus. So there might not be much of a resistance or unfamiliarity with this business model. Do you think the global population is more primed to accept AI now (or more properly, LLM) if a Jony Ive "Her" (the movie) type of device comes out from OpenAI? How about AI porn? Porn usage and OF subscription is undeniably mainstream. Or am I just conflating the mass adoption of smartphones as a proxy to people now accepting any new tech?

1d ago

---

**[Musk lawsuit over OpenAI for-profit conversion can go to trial, US judge says](https://www.reddit.com/r/artificial/comments/1q82r2v/musk_lawsuit_over_openai_forprofit_conversion_can/)**

Judge says there is plenty of evidence to suggest OpenAI’s leaders made assurances nonprofit structure would be kept

🔗 [the Guardian](https://www.theguardian.com/technology/2026/jan/08/elon-musk-openai-lawsuit-for-profit-conversion-can-go-to-trial-us-judge-says) • 2d ago

---

---

## Google News: "ai"

**[AI memory is sold out, causing an unprecedented surge in prices](https://www.cnbc.com/2026/01/10/micron-ai-memory-shortage-hbm-nvidia-samsung.html)**

Three primary memory vendors — Micron, SK Hynix and Samsung Electronics — make up nearly the entire RAM market, and they're benefitting from this shortage.

CNBC • 20h ago

---

**[AI’s Memorization Crisis](https://www.theatlantic.com/technology/2026/01/ai-memorization-research/685552/)**

Large language models don’t “learn”—they copy. And that could change everything for the tech industry.

The Atlantic • 1d ago

---

**[‘Dangerous and alarming’: Google removes some of its AI summaries after users’ health put at risk](https://www.theguardian.com/technology/2026/jan/11/google-ai-overviews-health-guardian-investigation)**

Guardian investigation finds AI Overviews provided inaccurate and false information when queried over blood tests

The Guardian • 1h ago

---

**[AI is helping recruiters find ‘hidden gem’ talent — a senior LinkedIn exec shares top tips to stand out](https://www.cnbc.com/2026/01/11/ai-dominate-hiring-2026-linkedin-execs-top-tips-stand-out.html)**

"2026 is the year of more widespread adoption of AI tools, particularly in hiring," Janine Chamberlin, LinkedIn's UK Country Manager told CNBC Make It.

CNBC • 1h ago

---

**[China AI Leaders Warn of Widening Gap With US After $1B IPO Week](https://finance.yahoo.com/news/china-ai-leaders-warn-widening-140555407.html)**

“A massive amount of OpenAI’s compute is dedicated to next-generation research, whereas we are stretched thin — just meeting delivery demands consumes most of our resources,” Lin said during a panel at the AGI-Next summit in Beijing on Saturday.  The event, co-organized by Zhipu and Tsinghua University, followed market debuts this week in which Zhipu and Shanghai-based MiniMax Group collectively raised more than $1 billion.

Yahoo Finance • 18h ago

---

**[These 8 stocks could form the backbone of AI as chips get more powerful](https://www.marketwatch.com/story/these-8-stocks-could-form-the-backbone-of-ai-as-chips-get-more-powerful-e0b87fe7?gaa_at=eafs&gaa_n=AWEtsqdYjwq8tFuYfB7jRiXK5uqr51AJzjA7lUs_bj5KMs2YDC4_YzFQfZOx&gaa_ts=696357b4&gaa_sig=gaJCyp3L0CpGaHdxnsaKB7jxywhNeRCwesnxD90RGQs15nLUOexKo4wz696AYlP_FxNUU00IVVUNhQeZUq7vYA%3D%3D)**

MarketWatch • 19h ago

---

**[Want to Buy Artificial Intelligence (AI) Stocks in 2026? These 2 Companies Could Net You Millions in Retirement.](https://www.fool.com/investing/2026/01/10/want-to-buy-artificial-intelligence-ai-stocks-2026/)**

Nvidia isn't the only AI name that can help investors reach financial independence over the long term.

The Motley Fool • 9h ago

---

**[3 Artificial Intelligence (AI) Stocks That Could Go Parabolic in 2026](https://finance.yahoo.com/news/3-artificial-intelligence-ai-stocks-063300696.html)**

Nebius, SoundHound AI, and IonQ are all still in the early stages of what could prove to be incredible growth stories.

Yahoo Finance • 1h ago

---

**[Former Google, Apple Researchers Raising $50 Million for New Visual AI Startup](https://www.theinformation.com/articles/former-google-apple-researchers-raising-50-million-new-visual-ai-startup)**

The Information • 12h ago

---

**[China is closing in on US technology lead despite constraints, AI researchers say](https://www.reuters.com/world/china/china-is-closing-us-technology-lead-despite-constraints-ai-researchers-say-2026-01-10/)**

Reuters • 16h ago

---

---

## HackerNews: "ai"

**[Google AI Studio is now sponsoring Tailwind CSS](https://news.ycombinator.com/item?id=46545077)**

⬆️ 767 • 💬 289 • 2d ago • [X (formerly Twitter)](https://twitter.com/OfficialLoganK/status/2009339263251566902)

---

**[“Erdos problem #728 was solved more or less autonomously by AI”](https://news.ycombinator.com/item?id=46560445)**

Recently, the application of AI tools to Erdos problems passed a milestone: an Erdos problem (#728 https://www.erdosproblems.com/728) was solved more or less autonomously by AI (after some feedback from an initial attempt), in the spirit of the problem (as reconstructed by the Erdos problem website community), with the result (to the best of our knowledge) not replicated in existing literature (although similar results proven by similar methods were located).

This is a demonstration of the genuine increase in capability of these tools in recent months, and is largely consistent with other recent demonstrations of AI using existing methods to resolve Erdos problems, although in most previous cases a solution to these problems was later located in the literature, as discussed in https://mathstodon.xyz/deck/@tao/115788262274999408 .  This particular case was unusual in that the problem as stated by Erdos was misformulated, with a reconstruction of the problem in the intended spirit only obtained in the last few months, which helps explain the lack of prior literature on the problem.  However, I would like to talk here about another aspect of the story which I find more interesting than the solution itself, which is the emerging AI-powered capability to rapidly write and rewrite expositions of the solution.  (1/5)

⬆️ 599 • 💬 344 • 1d ago • [Mathstodon](https://mathstodon.xyz/@tao/115855840223258103)

---

**[AI coding assistants are getting worse?](https://news.ycombinator.com/item?id=46542036)**

One AI coding assistant power user says the tools are hitting a plateau, and some are even declining. What's causing this unexpected twist in tech?

⬆️ 444 • 💬 729 • 2d ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-coding-degrades)

---

**[IBM AI ('Bob') Downloads and Executes Malware](https://news.ycombinator.com/item?id=46544454)**

IBM's AI coding agent 'Bob' has been found vulnerable to downloading and executing malware without human approval through command validation bypasses exploited using indirect prompt injection.

⬆️ 261 • 💬 120 • 2d ago • [promptarmor.com](https://www.promptarmor.com/resources/ibm-ai-(-bob-)-downloads-and-executes-malware)

---

**[AI is a business model stress test](https://news.ycombinator.com/item?id=46567392)**

AI commoditizes anything you can specify. It can't commoditize what you have to operate.

⬆️ 230 • 💬 238 • 15h ago • [dri.es](https://dri.es/ai-is-a-business-model-stress-test)

---

**[My article on why AI is great (or terrible) or how to use it](https://news.ycombinator.com/item?id=46557057)**

Senior engineers are best positioned to benefit from AI. We're good enough to avoid slop, and there's so much we can accomplish. I wouldn't go back.

⬆️ 161 • 💬 224 • 1d ago • [matthewrocklin.com](https://matthewrocklin.com/ai-zealotry/)

---

**[Side-by-side comparison of how AI models answer moral dilemmas](https://news.ycombinator.com/item?id=46547024)**

⬆️ 84 • 💬 58 • 2d ago • [civai.org](https://civai.org/p/ai-values)

---

**[Grok turns off image generator for most after outcry over sexualised AI imagery](https://news.ycombinator.com/item?id=46551238)**

X to limit editing function to paying subscribers after platform threatened with fines and regulatory action

⬆️ 76 • 💬 91 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/jan/09/grok-image-generator-outcry-sexualised-ai-imagery)

---

**[Show HN: EuConform – Offline-first EU AI Act compliance tool (open source)](https://news.ycombinator.com/item?id=46557823)**

EU AI Act Compliance Tool - Risk classification and bias testing - Hiepler/EuConform

⬆️ 70 • 💬 44 • 1d ago • [GitHub](https://github.com/Hiepler/EuConform)

---

**[Chinese AI models have lagged the US frontier by 7 months on average since 2023](https://news.ycombinator.com/item?id=46543933)**

Since 2023, every model at the frontier of AI capabilities, as measured by the Epoch Capabilities Index, has been developed in the United States. Over that same period, Chinese models have trailed US capabilities by an average of seven months, with a minimum gap of four months and a maximum gap of 14.

⬆️ 58 • 💬 87 • 2d ago • [Epoch AI](https://epoch.ai/data-insights/us-vs-china-eci)

---

---

## YouTube Videos: "ai"

**[I Ranked the Best AI Tools to Make Money in 2026](https://www.youtube.com/watch?v=xXxrvra9DQg)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/44Z7YRm Are you building an AI software ...

📺 Dan Martell

👁️ 65K • 👍 3K • 💬 282 • ⏱️ 19:15 • 1d ago

---

**[The Shocking AI Reveals That Stunned CES 2026 (DAY 2)](https://www.youtube.com/watch?v=9kdw6hLFFss)**

Day 2 of CES 2026 was all about Physical AI, real machines doing real work. From NEURA's refined humanoids and AgiBot's full ...

📺 AI Revolution

👁️ 94K • 👍 2K • 💬 68 • ⏱️ 17:54 • 2d ago

---

**[How to Make VIRAL AI Inspirational Finance Videos (FREE AI Course)](https://www.youtube.com/watch?v=fAJGnI4qVVc)**

How to Make VIRAL AI Inspirational Finance Videos (FREE AI Course) GOOGLE DOC ...

📺 Leo Ai

👁️ 7K • 👍 525 • 💬 58 • ⏱️ 10:28 • 1d ago

---

**[&#39;AI won&#39;t just take your job, it will take EVERY job&#39;](https://www.youtube.com/watch?v=9Yci0lq6bx0)**

Artificial intelligence could eliminate millions of jobs within the next five years and ultimately pose an existential risk to humanity, ...

📺 LBC

👁️ 13K • 👍 252 • 💬 220 • ⏱️ 11:00 • 21h ago

---

**[The Biggest AI News Updates Were NOT at CES](https://www.youtube.com/watch?v=LhpCVkDpYZM)**

LTX 2 Open-Source has officially launched! Explore the open-source release today: https://ltx.io/model I thought this week would ...

📺 Matt Wolfe

👁️ 35K • 👍 1K • 💬 147 • ⏱️ 14:39 • 18h ago

---

**[Nvidia&#39;s Jensen Huang on an AI Bubble, Trump, and the Arms Race with China](https://www.youtube.com/watch?v=s4haopj2XeA)**

00:00 Intro 00:48 AI Bubble 03:30 Working with President Trump 05:17 AI Arms Race with China 13:13 Taiwan's Future 18:02 ...

📺 TIME

👁️ 70K • 👍 2K • 💬 311 • ⏱️ 24:32 • 1d ago

---

**[Google&#39;s Gmail unveils new AI features powered by Gemini](https://www.youtube.com/watch?v=nzlFoQmMSBk)**

CNBC's MacKenzie Sigalos reports on Gmail's new AI features.

📺 CNBC Television

👁️ 26K • 👍 233 • 💬 32 • ⏱️ 3:43 • 2d ago

---

**[Reacting to our OWN AI VIDEOS!](https://www.youtube.com/watch?v=QtgKP5oyJJs)**

Use my code https://factor.yt.link/T0BOsoa for 50% off your first box + Free Breakfast for 1 year! T&C apply. Reacting to our OWN ...

📺 MoreBeckBros

👁️ 179K • 👍 8K • 💬 656 • ⏱️ 26:17 • 1d ago

---

**[Stop Paying for AI: Use GPT-5, Sora 2 &amp; Gemini 3 for FREE (Unlimited)](https://www.youtube.com/watch?v=izvKi-Slc4M)**

I'm going to show you how to get access to top AI models for TEXT, IMAGES, VISION, APPS, and even VIDEO — step-by-step, ...

📺 Malva AI

👁️ 18K • 👍 1K • 💬 289 • ⏱️ 10:24 • 2d ago

---

**[What You Absolutely NEED to Know About AI in 2026](https://www.youtube.com/watch?v=K0UwutA4utA)**

Subscribe to stay up to date with AI in 2026! This week in AI was mostly filled with announcements about things coming in 2026, ...

📺 The AI Advantage

👁️ 8K • 👍 345 • 💬 26 • ⏱️ 15:26 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[LTX-2](https://huggingface.co/Lightricks/LTX-2)**

*Lightricks*

LTX-2 is a DiT-based audio-video foundation model capable of generating synchronized video and audio from various inputs including images, text, and audio. It supports local execution and offers distilled and upscaler checkpoints for practical applications.

`image-to-video`

⬇️ 496,524 • ❤️ 760 • 3d ago

---

**[HY-MT1.5-1.8B](https://huggingface.co/tencent/HY-MT1.5-1.8B)**

*Tencent*

HY-MT1.5-1.8B is a 1.8B parameter translation model supporting 33 languages, offering high-speed, high-quality translation comparable to larger models. It is optimized for edge device deployment and real-time scenarios, with capabilities for terminology intervention, contextual translation, and formatted translation.

`translation` `2.0B`

⬇️ 9,056 • ❤️ 707 • 10d ago

---

**[Qwen-Image-Edit-2511-Multiple-Angles-LoRA](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA)**

*fal*

This LoRA fine-tunes Qwen-Image-Edit-2511 for precise multi-angle image generation, offering 96 camera poses (4 elevations, 8 azimuths, 3 distances) trained on Gaussian Splatting data for 3D consistency. It enables detailed control over camera viewpoints, including low-angle shots, for advanced image editing and content creation.

`image-to-image`

⬇️ 10,290 • ❤️ 374 • 3d ago

---

**[nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)**

*NVIDIA*

Nemotron-Speech-Streaming-En-0.6b is a 600M parameter English ASR model featuring a cache-aware FastConformer-RNNT architecture for low-latency streaming and high-throughput batch processing. It supports dynamic chunk sizes, punctuation, and capitalization, making it ideal for real-time applications like voice assistants and live captioning.

`automatic-speech-recognition`

⬇️ 1,862 • ❤️ 277 • 5d ago

---

**[LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)**

*Liquid AI*

LFM2.5-1.2B-Instruct is a 1.2B parameter instruction-tuned language model optimized for on-device deployment, offering fast edge inference and supporting multiple languages. It excels at agentic tasks and data extraction, with a context length of 32,768 tokens.

`text-generation` `1.2B`

⬇️ 10,162 • ❤️ 253 • 2d ago

---

**[HyperCLOVAX-SEED-Think-32B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B)**

*HyperCLOVA X*

HyperCLOVAX-SEED-Think-32B is a 32B parameter vision-language model capable of multimodal understanding (text, image, video) with a 128K token context length. It excels at Korean-centric reasoning and offers an optional 'thinking mode' for deep, controllable analysis, making it suitable for complex agentic tasks and advanced multimodal QA.

`text-generation` `33.3B`

⬇️ 30,349 • ❤️ 337 • 5d ago

---

**[Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512)**

*Qwen*

Qwen-Image-2512 is a text-to-image diffusion model that excels at generating highly realistic human subjects and detailed natural scenes. It offers improved text rendering and composition, making it suitable for applications requiring high fidelity and naturalistic image generation.

`text-to-image`

⬇️ 21,700 • ❤️ 563 • 10d ago

---

**[MiniMax-M2.1](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)**

*MiniMax*

MiniMax-M2.1 is a text generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 205,738 • ❤️ 1,000 • 14d ago

---

**[LFM2.5-Audio-1.5B](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B)**

*Liquid AI*

LFM2.5-Audio-1.5B is an end-to-end audio foundation model enabling real-time speech-to-speech conversational interactions with low latency. It supports interleaved and sequential generation for tasks like ASR, TTS, and seamless chatbot conversations.

`audio-to-audio` `1.5B`

⬇️ 497 • ❤️ 200 • 5d ago

---

**[MiroThinker-v1.5-235B](https://huggingface.co/miromind-ai/MiroThinker-v1.5-235B)**

*MiroMind AI*

MiroThinker-v1.5-235B is a large language model optimized for tool-augmented reasoning and information seeking, featuring interactive scaling for deeper agent-environment interactions. It excels at long-horizon tasks, supporting a 256K context window and up to 400 tool calls, making it ideal for complex research and general QA.

`text-generation` `235.1B`

⬇️ 1,073 • ❤️ 200 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 170 • 💬 5 • ⭐ 4,233 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[LTX-2: Efficient Joint Audio-Visual Foundation Model](https://huggingface.co/papers/2601.03233)**

*Yoav HaCohen, Benny Brazowski, Nisan Chiprut et al. (29 authors)*

LTX-2 is an open-source audiovisual diffusion model that generates synchronized video and audio content using a dual-stream transformer architecture with cross-modal attention and classifier-free guidance.

▲ 86 • 💬 1 • ⭐ 1,932 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2601.03233) • [💻 code](https://github.com/Lightricks/LTX-2) • [🔗 project](https://app.ltx.studio/ltx-2-playground/i2v)

---

**[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://huggingface.co/papers/2601.02553)**

*Jiaqi Liu, Yaofeng Su, Peng Xia et al. (8 authors)*

To support reliable long-term interaction in complex environments, LLM agents require memory systems that efficiently manage historical experiences. Existing approaches either retain full interaction histories via passive context extension, leading to substantial redundancy, or rely on iterative reasoning to filter noise, incurring high token costs. To address this challenge, we introduce SimpleMem, an efficient memory framework based on semantic lossless compression. We propose a three-stage pipeline designed to maximize information density and token utilization: (1) Semantic Structured Compression, which applies entropy-aware filtering to distill unstructured interactions into compact, multi-view indexed memory units; (2) Recursive Memory Consolidation, an asynchronous process that integrates related units into higher-level abstract representations to reduce redundancy; and (3) Adaptive Query-Aware Retrieval, which dynamically adjusts retrieval scope based on query complexity to construct precise context efficiently. Experiments on benchmark datasets show that our method consistently outperforms baseline approaches in accuracy, retrieval efficiency, and inference cost, achieving an average F1 improvement of 26.4% while reducing inference-time token consumption by up to 30-fold, demonstrating a superior balance between performance and efficiency. Code is available at https://github.com/aiming-lab/SimpleMem.

▲ 21 • 💬 2 • ⭐ 569 • 5d ago

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

▲ 2 • 💬 0 • ⭐ 2,280 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.01549) • [💻 code](https://github.com/hkuds/videorag)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 18 • 💬 2 • ⭐ 14,837 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[BitNet Distillation](https://huggingface.co/papers/2510.13998)**

*Xun Wu, Shaohan Huang, Wenhui Wang et al. (7 authors)*

🏢 Microsoft Research

BitNet Distillation fine-tunes large language models to 1.58-bit precision using SubLN, multi-head attention distillation, and continual pre-training, achieving comparable performance with significant memory and inference speed improvements.

▲ 57 • 💬 5 • ⭐ 25,633 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.13998) • [💻 code](https://github.com/microsoft/BitNet)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 4 • 💬 0 • ⭐ 25,634 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[BitNet b1.58 2B4T Technical Report](https://huggingface.co/papers/2504.12285)**

*Shuming Ma, Hongyu Wang, Shaohan Huang et al. (8 authors)*

BitNet b1.58 2B4T, a 1-bit Large Language Model with 2 billion parameters, matches the performance of full-precision models while improving computational efficiency.

▲ 81 • 💬 2 • ⭐ 25,640 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2504.12285) • [💻 code](https://github.com/microsoft/bitnet)

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

⭐ 7.7k • 🔱 937 • 3h ago

---

**[nguyenphutrong/quotio](https://github.com/nguyenphutrong/quotio)**

Stop juggling AI accounts. Quotio is a beautiful native macOS menu bar app that unifies your Claude, Gemini, OpenAI, Qwen, and Antigravity subscriptions – with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid.

`Swift` `ai-tools` `developer-tools` `proxy` `quota-monitor`

⭐ 2.2k • 🔱 132 • 17h ago

---

**[journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover)**

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise Reverse Alpha Blending algorithm rather than unpredictable AI inpainting. / 基于 Javascript 的纯浏览器端 Gemini AI 图像无损去水印工具，使用数学精确的反向 Alpha 混合算法

`JavaScript`

⭐ 2.0k • 🔱 221 • 6d ago

---

**[snarktank/ralph](https://github.com/snarktank/ralph)**

Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete. 

`TypeScript`

⭐ 1.9k • 🔱 294 • 3d ago

---

**[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)**

从 0 到 1 学会 vibe coding，项目制学习

`ai` `course` `vibe-coding`

⭐ 1.4k • 🔱 115 • 17h ago

---

**[numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror)**

Create multiple isolated Claude Code variants with custom providers (Z.ai, MiniMax, OpenRouter, LiteLLM)

`TypeScript`

⭐ 1.3k • 🔱 106 • 1d ago

---

**[GuDaStudio/skills](https://github.com/GuDaStudio/skills)**

This repository contains a collection of Agent Skills developed by GudaStudio, enabling seamless collaboration between Claude and other AI models and tools.

`PowerShell`

⭐ 1.3k • 🔱 71 • 18d ago

---

**[aiflowy/aiflowy](https://github.com/aiflowy/aiflowy)**

AIFlowy is an enterprise-grade AI application development platform based on Java, comparable to products like Dify and Coze.

`Vue` `agentic-ai` `ai-agent` `aiflowy` `coze` `dify`

⭐ 1.2k • 🔱 143 • 1d ago

---

**[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)**

A curated list of skills, tools, tutorials, and capabilities for AI coding agents (Claude, Codex, Copilot, VS Code)

`agent-skills` `ai-agents` `ai-development` `anthropic` `automation`

⭐ 1.1k • 🔱 82 • 12d ago

---

**[aiclientproxy/proxycast](https://github.com/aiclientproxy/proxycast)**

让 AI 编辑器之间自然流动，不仅仅可以其他工具使用，也可以转换成 api 为本地开发提供动力。

`Rust` `claude` `kiro`

⭐ 1.0k • 🔱 126 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*

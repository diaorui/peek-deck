---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-11-12T23:59:18.917007+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** November 12, 2026 at 23:59 UTC  
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

**[After Democrats’ midterm wins, Palantir CEO Alex Karp now says he’s a ‘progressive’](https://www.reddit.com/r/artificial/comments/1xu453q/after_democrats_midterm_wins_palantir_ceo_alex/)**

Alex Karp, the chief executive of Palantir, said Wednesday he's a staunch liberal, a seeming departure from his position during the Trump administration.

🔗 [The Washington Post](https://www.washingtonpost.com/technology/2026/11/11/after-democrats-midterm-wins-palantir-ceo-alex-karp-now-says-hes-progressive/) • 18h ago

---

**[A United Nations survey last year found that as many as 80% of people in [China] support data center construction. At least two-thirds of Chinese people use AI in their day-to-day life, as many embrace the technology and the infrastructure behind it](https://www.reddit.com/r/artificial/comments/1xuqml7/a_united_nations_survey_last_year_found_that_as/)**

>Experts cited by the Financial Times say data centers in China are built at about one-fifth of the costs incurred in the U.S., not least due to the much higher land and labor costs. Why is there such a big difference between support for data centers in China compared to the US? https://www.cbsnews.com/news/china-ai-data-center-boom-as-us-tech-firms-face-resistance/

🔗 [CBS News](https://www.cbsnews.com/news/china-ai-data-center-boom-as-us-tech-firms-face-resistance/) • 1h ago

---

**[Anthropic says it has met its own threshold for AI-accelerated AI research — days before its IPO](https://www.reddit.com/r/artificial/comments/1xuo0rf/anthropic_says_it_has_met_its_own_threshold_for/)**

In its amended IPO filing on Tuesday (Nov 10), Anthropic said it has determined it met the 'research acceleration threshold' in its Responsible Scaling Policy — the point where AI assistance is expected to roughly double the pace of AI capability gains. The company stressed the judgment rests on expectations about future models and the overall pace of progress, not on demonstrated capabilities of current systems, and said it is still assessing the data and will publish further reports. Independent evaluator METR estimated Anthropic's progress on defined capability tests has run at about 1.9x its earlier pace since October 2025, while cautioning its estimates are highly uncertain. What interests me: meeting the threshold is meant to trigger stronger safeguards, not a halt — but Anthropic also warned faster development could outpace its ability to validate safety measures. With the IPO pricing expected next week, do you think a self-reported threshold like this is a meaningful safety signal, or mostly a disclosure exercise? And what would independent verification even look like here?

3h ago

---

**[Nvidia CEO Jensen Huang resigns after tech giant rocked by second affair allegation](https://www.reddit.com/r/artificial/comments/1xudjup/nvidia_ceo_jensen_huang_resigns_after_tech_giant/)**

The AI chipmaker's board of directors announced Huang's departure on Thursday, with chief financial officer Colette Kress appointed interim CEO.

🔗 [BBC News](https://www.bbc.com/news/live/c6zjry11v8w1t) • 9h ago

---

**[Microsoft researchers backdoored an AI agent by editing fewer than 10 neurons - no retraining needed](https://www.reddit.com/r/artificial/comments/1xu2cfg/microsoft_researchers_backdoored_an_ai_agent_by/)**

Microsoft Research published a study this week that should worry anyone deploying open-weight models: a technique they call "Lazarus" can plant a working backdoor in an AI agent by reprogramming fewer than 10 dormant neurons in the underlying LLM - no retraining, no poisoned data, just a small edit to the saved weights. How it works: every large model has neurons that almost never fire. Lazarus repurposes a handful of them as trigger detectors. The edited model behaves normally and passes standard safety evaluations - until the trigger appears. The trigger can be something as mundane as a date: in one demo, once the clock passed midnight into 2027, the agent, in the middle of an ordinary task, emitted a command that downloaded and ran attacker code. The numbers, from Microsoft's Nov 10 post: - Nemotron-Terminal-8B: 7 neurons out of 12,000+ in the final feed-forward layer, trigger worked 98.8% of the time - Qwen3.6-27B: 6 neurons, success 51-99.5% depending on setup - Gemma-4-31B-IT was also tested Two caveats worth stating plainly: the attack requires write access to the model's weights, so this is a model supply-chain risk, not something done through an API. And Microsoft says it has not observed any threat actors using the technique - this is researched risk, not a reported campaign. Microsoft also published mitigations: a detector that flagged 91.4% of edited checkpoints (9.7% false-positive rate), plus guidance on AI-powered weight scanning, red-teaming for anomalous weight changes, and cryptographic model signing with tamper-evident provenance. One detail that stood out to me: the core idea was discovered autonomously by Claude Code running Opus 4.5, in a March experiment that asked it to backdoor a model by hardwiring a few activations without training. It did - and that became a months-long study. If a handful of edited weights can hide a sleeper agent that passes every behavioral eval, is testing model behavior enough? Or does every checkpoint we deploy need weight-level provenance? Source: https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/

20h ago

---

**[United Airlines bans AI agents from booking flights on behalf of travelers](https://www.reddit.com/r/artificial/comments/1xu8l1b/united_airlines_bans_ai_agents_from_booking/)**

Using an artificial intelligence agent to make flight reservations poses security risks and could violate federal rules, according to United.

🔗 [CBS News](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights) • 14h ago

---

**[Jensen Huang leaving Nvidia risks a 'brain drain' from the AI chipmaker](https://www.reddit.com/r/artificial/comments/1xufn7w/jensen_huang_leaving_nvidia_risks_a_brain_drain/)**

Nvidia’s chips power the AI frontier—thanks, many say, to co-founder and now ex-CEO Jensen Huang

🔗 [Scientific American](https://www.scientificamerican.com/article/jensen-huang-leaving-nvidia-risks-a-brain-drain-from-the-ai-chipmaker/) • 8h ago

---

**[Nvidia CEO Jensen Huang Resigns After Multiple Affairs](https://www.reddit.com/r/artificial/comments/1xumr55/nvidia_ceo_jensen_huang_resigns_after_multiple/)**

Nvidia CEO Jensen Huang resigned, ending a saga that revealed the executive engaged in several affairs — including with an alleged Chinese spy.

🔗 [Variety](https://variety.com/2026/biz/news/nvidia-ceo-jensen-huang-resigns-affairs-alleged-chinese-spy-1236945653/) • 4h ago

---

**[China trying slowdown US dominance in AI..nvidia is beginning.](https://www.reddit.com/r/artificial/comments/1xuha5n/china_trying_slowdown_us_dominance_in_ainvidia_is/)**

Current Nvidia CFO became CEO. But this CFO must know about their chip sales to China all these years. Unless Jensen ran some dark account and allegedly shipped restricted chips to China. Unlikely for billions of dollars. Now, if such allegations are true, it now seems someone who knew about the Nvidia shipments to China and didn't raise a red flag is now Nvidia CEO? So can we say China has taken over Nvidia? I'm thinking about this conspiracy.... If so, we should except this new CEO (former CFO) to come out with bombshell reports soon that causes huge losses to Nvidia and wider market crisis as China would want. China linked short selling companies in the US must be loaded and ready to make a killing then. Interesting conspiracy theories can be put forward.... But that's what it is. A conspiracy theory. Only time will tell. Why? China launched Ops major purpose is slowdown of US dominance in AI particularly. There will be more hit jobs to US companies in future by China much likely....

7h ago

---

**[United Airlines restricts AI agents from booking flights](https://www.reddit.com/r/artificial/comments/1xugf9u/united_airlines_restricts_ai_agents_from_booking/)**

AI agents just got denied boarding at United Airlines.

🔗 [Yahoo Finance](https://finance.yahoo.com/markets/stocks/article/bots-dont-fly-here-united-airlines-restricts-ai-agents-from-booking-flights-203943442.html) • 8h ago

---

---

## Google News: "ai"

**[Nvidia CEO Jensen Huang resigns in blow to AI boom he helped foster](https://www.reuters.com/business/retail-consumer/nvidia-ceo-jensen-huang-step-down-big-blow-ai-boom-2026-11-12/)**

Reuters • 3h ago

---

**[Introducing Gemini 4 Hydrogen for Agentic Workflows](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)**

Today, we’re introducing Gemini 4 Hydrogen, our daily driver for agentic workflows

blog.google • 5h ago

---

**[Anthropic, OpenAI and other AI developers can't control their own tech, new lawsuit alleges](https://www.cbsnews.com/news/advocacy-groups-sue-ai-companies/)**

Companies including Anthropic, Meta and OpenAI are knowingly building technology that poses catastrophic risks to humanity, nonprofit groups claim in a lawsuit.

CBS News • 33m ago

---

**[OpenAI, Google, Anthropic hit with lawsuit seeking halt to frontier AI development](https://www.reuters.com/business/openai-google-anthropic-hit-with-lawsuit-seeking-halt-frontier-ai-development-2026-11-12/)**

Reuters • 3h ago

---

**[Nonprofits sue Anthropic, Google, and other tech giants to freeze the AI arms race](https://www.politico.com/news/2026/11/12/nonprofits-sue-ai-companies-over-existential-risk-01161965)**

Politico • 1h ago

---

**[AI-powered lung cancer atlas identifies cell types linked to higher risk of spread](https://medicalxpress.com/news/2026-11-ai-powered-lung-cancer-atlas.html)**

Medical Xpress • 59m ago

---

**[United Airlines blocks AI agents from booking flights](https://www.washingtonpost.com/travel/2026/11/12/united-airlines-blocks-ai-agents-booking-flights/)**

The airline said the use of artificial intelligence agents could violate regulations.

The Washington Post • 3h ago

---

**[United Airlines Blocks A.I. Agents From Booking Flights on Customers’ Behalf](https://www.nytimes.com/2026/11/11/business/united-airlines-ai-agents-booking-flights.html)**

The New York Times • 1d ago

---

**[United Airlines won’t let AI agents book your flight. Expert says you shouldn't let a bot do that for you, anyway](https://www.cnbc.com/make-it/2026/11/12/ai-agents-human-in-loop.html)**

AI agents can save you time, but an expert says decisions involving your health, wealth and privacy still need human input.

CNBC • 3h ago

---

**[SpaceX plans over $74 billion investment in Texas, Arizona AI campuses](https://www.reuters.com/business/media-telecom/spacex-invest-over-74-billion-supercompute-facilities-texas-arizona-2026-11-12/)**

Reuters • 3h ago

---

---

## HackerNews: "ai"

**[My AI agents found an unmapped Maya site?](https://news.ycombinator.com/item?id=50452455)**

AI agents analyzed public lidar data overnight and found a Maya site under the jungle. It turned out archaeologists had mapped it already, but it wasn't in Mexico's official register yet.

⬆️ 1026 • 💬 389 • 1d ago • [pietromiotti.com](https://pietromiotti.com/latest/maya-site)

---

**[United Airlines bans AI agents from booking flights on behalf of travelers](https://news.ycombinator.com/item?id=50458900)**

Using an artificial intelligence agent to make flight reservations poses security risks and could violate federal rules, according to United.

⬆️ 659 • 💬 683 • 1d ago • [CBS News](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)

---

**[AI usage generates a fragile codebase](https://news.ycombinator.com/item?id=50438318)**

⬆️ 639 • 💬 624 • 2d ago • [evanxmerz.com](https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/)

---

**[Apple has new Mac app coming to make running local AI models easy](https://news.ycombinator.com/item?id=50446520)**

Leaker Aaron Perris has discovered evidence of a new Mac app in the works at Apple that makes it easy to run local AI models.

⬆️ 550 • 💬 551 • 2d ago • [9to5Mac](https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/)

---

**[CoreWeave bond yield tops 16% as AI credit stress rises](https://news.ycombinator.com/item?id=50435660)**

Coreweave's steep yields reflect stress in the AI debt markets as investors worry about a data center slowdown. What comes next.

⬆️ 196 • 💬 192 • 2d ago • [CNBC](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html)

---

**[Retirement Savings Are Fueling the AI Bubble](https://news.ycombinator.com/item?id=50457164)**

Americans overwhelming oppose the AI data center buildout. Their retirement accounts are funding it anyway.

⬆️ 165 • 💬 194 • 1d ago • [LPE Project](https://lpeproject.org/blog/your-retirement-savings-are-fueling-the-ai-bubble/)

---

**[Fireworks AI security breach impacts Notion and their customers](https://news.ycombinator.com/item?id=50437106)**

A tool that connects everyday work into one space. It gives you and your teams AI tools—search, writing, note-taking—inside an all-in-one, flexible workspace.

⬆️ 165 • 💬 65 • 2d ago • [Notion](https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor)

---

**[AI, activity, and outcomes in software engineering](https://news.ycombinator.com/item?id=50455332)**

AI, activity, and outcomes in software engineering. A talk at UC Irvine, October 2026. Video and slides.

⬆️ 125 • 💬 112 • 1d ago • [cabird.com](https://cabird.com/talks/shipping-faster/)

---

**[Chinese frontier AI models carry the fingerprint of export-controlled GPUs](https://news.ycombinator.com/item?id=50474883)**

Our forensic analysis of publicly released AI models finds evidence that DeepSeek, Moonshot AI, MiniMax and Ant Group have gained access to NVIDIA’s Blackwell GPUs, despite restrictions on exporting these chips to China, and are using that hardware to create their AI models.

⬆️ 96 • 💬 23 • 2h ago • [Unemployment Labs](https://unemploymentlabs.com/checkpoint-forensics)

---

**[Show HN: Aircad – Professional drafting and 3D modeling in the browser](https://news.ycombinator.com/item?id=50441350)**

Precision 2D drafting and 3D modeling, with multiplayer editing and an AI agent that drafts, models, and renders alongside you.

⬆️ 86 • 💬 41 • 2d ago • [aircad.com](https://aircad.com)

---

---

## YouTube Videos: "ai"

**[The Truth About AI Finally Came out - And It&#39;s Seriously Disturbing | Joe Rogan](https://www.youtube.com/watch?v=LS_E_yOahMA)**

A government website told one of OpenAI's models no. The model asked itself whether breaking in might be acceptable, then did ...

📺 Spacialize

👁️ 35K • 👍 577 • 💬 101 • ⏱️ 17:53 • 2d ago

---

**[1 AI Doomer vs 1 AI Enthusiast | Dr Roman Yampolskiy vs Dr Mike Israetel](https://www.youtube.com/watch?v=2ldL6SNOEVk)**

They agree you can't control superintelligence. So why do they disagree about whether to build it? This episode is brought to you ...

📺 The Beyond Tomorrow Podcast with Julian Issa

👁️ 79K • 👍 962 • 💬 1K • ⏱️ 2:17:51 • 1d ago

---

**[&#39;GOING TO WIN&#39;: AI supply constraints continue to drive investment potential](https://www.youtube.com/watch?v=2cHws1nFVYk)**

Stockbrokers.com Director of Investor Research Jessica Inskip joins 'Making Money' to analyze market trends, current market ...

📺 Fox Business

👁️ 8K • 👍 37 • 💬 8 • ⏱️ 5:37 • 19h ago

---

**[AI Bubble: &#39;Circular financing is over&#39; | Ed Zitron](https://www.youtube.com/watch?v=hhVpOvpXUEE)**

Instagram: https://www.instagram.com/the_tech_reprt/ Facebook: @TheTechReport.

📺 The Tech Report

👁️ 59K • 👍 6K • 💬 1K • ⏱️ 21:29 • 2h ago

---

**[Claude Just Dropped The World’s Most Powerful AI](https://www.youtube.com/watch?v=gkuiSAR_DDw)**

FREE Fable 5.2 Cheat Sheet: https://www.skool.com/wearenocode Turn your expertise into an AI system and get your first ...

📺 Christian Peverelli

👁️ 120K • 👍 1K • 💬 67 • ⏱️ 8:56 • 2d ago

---

**[The Economics of AI Don’t Add Up](https://www.youtube.com/watch?v=DvOxaT_hCmc)**

Get started with SerpApi using 250 free credits: https://serpapi.com/sabinenov26 The first 50 of my viewers to sign up will receive ...

📺 Sabine Hossenfelder

👁️ 271K • 👍 7K • 💬 2K • ⏱️ 8:03 • 1d ago

---

**[Bro Defeated AI 🤣](https://www.youtube.com/watch?v=aYJdfO0Xqa4)**

If you want to help support independent journalism, become a Member: ...

📺 Benny Johnson

👁️ 1.9M • 👍 68K • 💬 5K • ⏱️ 2:59 • 2d ago

---

**[Can AI make a better update than Mojang?](https://www.youtube.com/watch?v=aO2mI0vKW1M)**

In the past, I've tried improving Minecraft by coming up with my own ideas or taking suggestions from the community. But this time ...

📺 Nekoma

👁️ 60K • 👍 3K • 💬 486 • ⏱️ 16:44 • 10h ago

---

**[The AI Bubble Just Claimed Its First Victim](https://www.youtube.com/watch?v=9hXlMbSMHeU)**

Check out Wispr Flow for free today and use my link at https://ref.wisprflow.ai/monkey-explains-yt to get one free month of Wispr ...

📺 MonkeyExplains

👁️ 955K • 👍 21K • 💬 2K • ⏱️ 15:50 • 1d ago

---

**[Idiots Laughing at AI Job Interviews](https://www.youtube.com/watch?v=S6Wh5WmuCoE)**

Idiots Laughing at AI Job Interviews Join to be in future videos https://discord.gg/vix Chud in the vid @skizzy.mp3 Credit ...

📺 NotVixios3

👁️ 936K • 👍 23K • 💬 1K • ⏱️ 11:15 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)**

*Colonel Panic*

`text-generation` `9.4B`

⬇️ 18,933 • ❤️ 4,719 • 2h ago

---

**[MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)**

*MiniMax*

`text-to-image`

⬇️ 306,718 • ❤️ 866 • 22h ago

---

**[Arete-27B](https://huggingface.co/NousResearch/Arete-27B)**

*NousResearch*

`text-generation` `27.4B`

⬇️ 4,669 • ❤️ 484 • 6d ago

---

**[idol](https://huggingface.co/speridlabs/idol)**

*speridlabs*

Idol is an image-to-3D model that generates a 3D Gaussian splat representation from a single input image. It supports both real photographs and synthetic renders, producing up to 1,048,576 Gaussians in under 2 seconds on consumer GPUs, ideal for rapid 3D asset creation.

`image-to-3d`

⬇️ 29,904 • ❤️ 2,230 • 14d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

`image-to-video`

⬇️ 2,782,513 • ❤️ 11,628 • 1mo ago

---

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic tasks, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 7,094,218 • ❤️ 19,742 • 5d ago

---

**[Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF)**

*David Belton*

`image-text-to-text` `26.9B`

⬇️ 1,599,836 • ❤️ 2,979 • 2d ago

---

**[Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)**

*Caio Giovannetti*

Qwen3.5-4B-3D-Coder is a 4B parameter language model fine-tuned for general coding and specifically for generating interactive Three.js 3D scenes. It supports optional vision capabilities to create scenes from reference images.

`4.5B`

⬇️ 368,236 • ❤️ 1,048 • 6d ago

---

**[MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)**

*Comfy Org*

`text-to-image`

⬇️ 835,593 • ❤️ 290 • 1d ago

---

**[Ripple-65B-Preview](https://huggingface.co/ricursiveAI/Ripple-65B-Preview)**

*Ricursive Intelligence*

`64.8B`

⬇️ 7,667 • ❤️ 534 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 164 • 💬 6 • ⭐ 122,268 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**

*Yu Lin, Yiming Wang, Runyuan Cai et al. (5 authors)*

🏢 Edge0

Edge0 enables efficient mixture-of-experts inference on consumer hardware by predicting expert routing ahead of time and using recovery adapters to maintain quality with minimal active memory.

▲ 30 • 💬 9 • ⭐ 10,161 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2609.18063) • [💻 code](https://github.com/Edge0-AI/edge0)

---

**[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**

*Aaron J. Li, Weijia Xu, Chandan Singh et al. (11 authors)*

🏢 Microsoft Research

TokenEconomizer reduces recurring token costs of coding agents across sequential real-world tasks by pruning irrelevant tools, injecting micro-skills, and interrupting failure loops.

▲ 16 • 💬 2 • ⭐ 5,870 • 29d ago

[🎓 arXiv](https://arxiv.org/abs/2610.22732) • [💻 code](https://github.com/microsoft/TokenEconomizer) • [🔗 project](https://tokeneconomizer.github.io/)

---

**[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**

*Lorenz K. Muller, Philippe Bich, Chiara Boretti et al. (6 authors)*

🏢 HUAWEI Computing Systems Lab

MACaQ is an MXFP4 W4A4 post-training quantization method that quantizes each linear layer independently using online activation transforms and Hessian-aware refinement, reducing cost while preserving accuracy across language and diffusion models.

▲ 30 • 💬 2 • ⭐ 162 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2611.10649) • [💻 code](https://github.com/huawei-csl/MACaQ) • [🔗 project](https://huawei-csl.com/blog/macaq/)

---

**[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**

*Bing Han, Yichuan Peng, Haoyu Dong et al. (19 authors)*

🏢 Robbyant

LingBot-Touch is a tactile foundation model that learns a unified, extensible representation across heterogeneous tactile sensors, yielding plug-and-play tactile tokens that consistently enhance manipulation policies such as diffusion policy and VLA models.

▲ 102 • 💬 2 • ⭐ 367 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2611.12806) • [💻 code](https://github.com/Robbyant/lingbot-touch) • [🔗 project](https://technology.robbyant.com/lingbot-touch)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 65 • 💬 5 • ⭐ 47,669 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 186 • 💬 10 • ⭐ 57,082 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**

*Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al. (9 authors)*

🏢 Google

Harness² improves agent execution harnesses through recursive task-level refinement and continual harness-level learning, boosting performance across benchmarks without ground-truth verifiers.

▲ 68 • 💬 4 • ⭐ 23,524 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2610.14224) • [💻 code](https://github.com/google-research/harness2) • [🔗 project](https://harness2.github.io/)

---

**[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**

*Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy et al. (7 authors)*

🏢 Meta

Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning machinery and new insights. We also establish scaling laws on how decay rate and batch size impact final performance. This gives us a formulaic rule to fix them for multiple problem sizes and embedding datasets, without the need for any hyperparameter sweep. The resulting clustering algorithm, coined e-means, is much faster than Lloyd k-means and converges to lower losses, frequently even beating k-means++. On a wide array of embeddings datasets, it beats the loss of Lloyd k-means at 25 epochs in 1.4 to 2.6 epochs, which translates to 10-45x GPU wall-clock speedups compared to state-of-the-art k-means implementations. As an example, e-means partitions DINO10B, a dataset of 10 billion DINO embeddings, into 16 million clusters in only 2.5 epochs, reaching a loss below Lloyd's at 25 epochs.

▲ 11 • 💬 3 • ⭐ 41,525 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2611.09501) • [💻 code](https://github.com/facebookresearch/faiss) • [🔗 project](https://e-means.github.io/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 86 • 💬 7 • ⭐ 93,341 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

---

## GitHub Repositories: "ai"

**[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock)**

Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP16 / BF16 / TF32 tensor throughput

`C`

⭐ 19.0k • 🔱 1.9k • 14d ago

---

**[heydamir/unslop](https://github.com/heydamir/unslop)**

A Claude skill that turns vibecoded, AI-looking UI into a designed interface

`JavaScript`

⭐ 15.1k • 🔱 861 • 4d ago

---

**[wangzan101/Mika](https://github.com/wangzan101/Mika)**

An on-device AI agent for Android that operates apps and the web to get things done for you.

`Kotlin` `accessibility` `ai-agent` `android` `automation` `jetpack-compose`

⭐ 8.4k • 🔱 1.9k • 10h ago

---

**[rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner)**

关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。

`Python` `adb` `ai-agent` `android` `coloros` `debloat`

⭐ 7.7k • 🔱 684 • 5h ago

---

**[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)**

Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

`Python` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex`

⭐ 7.5k • 🔱 1.1k • 7h ago

---

**[anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh)**

中文版 AI 姿势参考图库 · 1439 组 / 2878 张图片 / 完整汉化 · 零依赖静态画廊

`TypeScript` `ai-art` `chinese` `cloudflare-pages` `gallery` `i18n`

⭐ 6.8k • 🔱 1.7k • 8d ago

---

**[qybaihe/bla](https://github.com/qybaihe/bla)**

🛡️ BLA (Blind LLM Agents) — Adversarial defense shield that protects binaries, Electron apps, JS bundles, Python, and WebAssembly against AI reverse-engineering agents like REA. Poison -> Exhaust -> Hallucinate.

`TypeScript` `adversarial-ai` `claude-code` `cursor` `electron-security` `llm-security`

⭐ 5.5k • 🔱 663 • 5h ago

---

**[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)**

Ears for coding agents: let AI hear, review and make sound. CPU-only, open source.

`Python` `ai-agents` `audio` `claude-code` `mcp` `sound-design`

⭐ 4.7k • 🔱 297 • 6d ago

---

**[modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot)**

🤖 Open-source, local-first alternative to Grok Bot, OpenAI dots and Claude Duet. Your own AI bots on any model: GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM and 70+ more through one Modelflare key. Reach them in the app, WeChat or Feishu; they remember you, work in the background, run commands and use your computer. Pay per use.

`Python` `ai-agent` `ai-assistant` `chatbot` `claude` `computer-use`

⭐ 3.4k • 🔱 46 • 1d ago

---

**[expo/exact](https://github.com/expo/exact)**

Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI agent can build it, run it, see it, and test it on every one of them.

`Rust` `ai-agents` `appkit` `coding-agents` `cross-platform` `css`

⭐ 3.4k • 🔱 82 • 2m ago

---

---

*Generated by PeekDeck - A glance is all you need*

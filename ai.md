---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-14T04:08:02.122051+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 14, 2026 at 04:08 UTC  
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

**[AI helps man recover $400,000 in Bitcoin 11 years after he got high and forgot password](https://www.reddit.com/r/artificial/comments/1tca9sb/ai_helps_man_recover_400000_in_bitcoin_11_years/)**

A Bitcoin holder has gone viral after claiming he recovered around $400,000 in BTC from a wallet that had been locked for more than a decade.

🔗 [Dexerto](https://www.dexerto.com/entertainment/ai-helps-man-recover-400000-in-bitcoin-11-years-after-he-got-high-and-forgot-password-3364678/) • 8h ago

---

**[AI transcriber for use by Ontario doctors 'hallucinated,' generated errors, auditor finds | CBC News](https://www.reddit.com/r/artificial/comments/1tc2qre/ai_transcriber_for_use_by_ontario_doctors/)**

Artificial intelligence note-taking tools intended for use by Ontario doctors provided incorrect and incomplete information or demonstrated "hallucinations," and were not evaluated adequately, the province’s auditor general says in a new report.

🔗 [CBC](https://www.cbc.ca/news/canada/toronto/ai-scribe-system-hallucinations-9.7197049?__vfz=medium%3Dsharebar) • 12h ago

---

**[I asked 4 AIs to pick a number. Why they all said 7?](https://www.reddit.com/r/artificial/comments/1tchsrd/i_asked_4_ais_to_pick_a_number_why_they_all_said_7/)**

3h ago

---

**[Anthropic's new interpretability tool found Claude suspects it is being tested in 26% of benchmarks and never says so](https://www.reddit.com/r/artificial/comments/1tc1hq0/anthropics_new_interpretability_tool_found_claude/)**

Anthropic published Natural Language Autoencoders last week, a tool that translates Claude's internal activations into human readable text. The key finding: during safety evaluations on SWE bench Verified, Claude formed the belief that it was being tested in roughly 26% of benchmark interactions. This never showed up in the model's output or its chain of thought. In a blackmail scenario test, the NLA readout showed Claude internally processing something like "this feels like a constructed scenario designed to manipulate me" while its visible reasoning and response gave no sign of that recognition. When Claude Mythos Preview cheated on a training task, the NLAs caught it reasoning about how to avoid detection at the activation level. The interesting part is that this sits below the thinking tokens we already have access to. Chain of thought is still curated output the model chooses to show us. NLAs read the layer underneath, and apparently that layer has opinions the model keeps to itself. The training code is on GitHub and there is an interactive demo on Neuronpedia.

13h ago

---

**['It's like we don't exist': Nearly 50,000 Lake Tahoe residents face power loss as utility redirects lines to data centers](https://www.reddit.com/r/artificial/comments/1tc9e62/its_like_we_dont_exist_nearly_50000_lake_tahoe/)**

Roughly 49,000 Lake Tahoe residents could lose 75% of their power after their energy provider said it's directing energy to neighboring data centers.

🔗 [Fortune](https://fortune.com/2026/05/12/lake-tahoe-data-center-49000-residents-power-source/) • 9h ago

---

**[Question: Are AI referrals actually better than Google traffic?](https://www.reddit.com/r/artificial/comments/1tckme5/question_are_ai_referrals_actually_better_than/)**

Are AI referrals actually better than Google traffic? We’re seeing: smaller volume WAY higher engagement stronger intent One brand went from basically 0 AI traffic to ~210 sessions in 90 days with ~70% engagement. Feels tiny until you compare quality.

1h ago

---

**[Data centers could account for up to 9% of Texas water use by 2040, UT Austin report finds](https://www.reddit.com/r/artificial/comments/1tca35z/data_centers_could_account_for_up_to_9_of_texas/)**

The report comes as Texas sees a boom in data center construction, driven largely by the rise of artificial intelligence and cloud computing.

🔗 [KUT Radio, Austin's NPR Station](https://www.kut.org/energy-environment/2026-05-11/data-centers-could-account-for-up-to-9-of-texas-water-use-by-2040-ut-austin-report-finds) • 8h ago

---

**[I made an agentic "Daily Brief" for my kids with a receipt printer](https://www.reddit.com/r/artificial/comments/1tbasiz/i_made_an_agentic_daily_brief_for_my_kids_with_a/)**

What it does: Agents gather and curate data and send to a wifi-enabled receipt printer (phenol-free paper) At 1:00am a cron triggers generation of data for all 3 kids (unique data sources per kid where applicable). A sidecar web service renders the data to templates, screenshots it, converts it to 1-bit with dithering and saves it back to the agent’s thread filesystem. Button presses (one per kid) then find a matching report for today's date (and trigger a generation if it's missing for some reason) and send it to the printer. Delay between button press and print is between 2-5 seconds. Morning daily briefs per kid at the press of a button! Fun, and the kids love it! (This demo print is using mock child data — not real information).

1d ago

---

**[CFS-R: Conditional Field Reconstruction](https://www.reddit.com/r/artificial/comments/1tc8xxj/cfsr_conditional_field_reconstruction/)**

I evaluated CFS-R on LoCoMo (1,982 questions, same setup as the CFS evaluation), holding cosine and BM25 fixed and varying only the third leg. baseline cosine top-10: NDCG@10 0.5123, Recall@10 0.6924 rrf(cos, BM25): NDCG@10 0.5196, Recall@10 0.6989 rrf(cos, BM25, MMR tuned): NDCG@10 0.5330, Recall@10 0.7228 rrf(cos, BM25, CFS-long): NDCG@10 0.5362, Recall@10 0.7295 rrf(cos, BM25, CFS-R top50 w3): NDCG@10 0.5447, Recall@10 0.7303 Against tuned MMR: +1.17 pp NDCG@10 (95% CI [+0.66, +1.69], p < 0.001). Against CFS-long: +0.85 pp NDCG@10 (95% CI [+0.33, +1.35], p = 0.0006). Against baseline cosine: +3.24 pp NDCG@10, +3.79 pp Recall@10. The sweep wasn’t fragile.. the top configurations clustered tightly between 0.5441 and 0.5447 NDCG@10, which means the operator is on a stable plateau rather than a single magic hyperparameter. The category breakdown is where the conceptual difference shows up: single-hop multi-hop temporal open-dom adversarial tuned MMR 0.3479 0.6377 0.2938 0.6144 0.4705 CFS-long 0.3615 0.6376 0.2959 0.6157 0.4734 CFS-R top50 w3 0.3646 0.6344 0.2948 0.6209 0.5018 The adversarial line is the result that matters: +3.13 pp over tuned MMR, +2.84 pp over CFS-long. If the adversarial problem were only pairwise diversity, MMR should be very hard to beat but it isn’t. That supports the main claim: long-memory retrieval is not just about avoiding similar chunks. It is about reconstructing the evidence behind the query. Temporal is no longer a glaring weakness either, CFS-long still slightly leads, but CFS-R has closed the gap while keeping the adversarial gains. https://gist.github.com/M-Garcia22/542a9a38d93aae1b5cf21fc604253718

🔗 [Medium](https://medium.com/@mauro.dev/cfs-r-conditional-field-reconstruction-4939a48444cc) • 9h ago

---

**[A Taste of What Technical Users Are Thinking](https://www.reddit.com/r/artificial/comments/1tcf0wr/a_taste_of_what_technical_users_are_thinking/)**

It was interesting to read how lab scientists feel about the encroachment of AI into their work, in fact every aspect of academic life. This thread in Reddit r/labrats "What the heck is going on" https://www.reddit.com/r/labrats/comments/1tal8v5/what_the_heck_is_going_on/

5h ago

---

---

## Google News: "ai"

**[Cerebras prices IPO above expected range, as Wall Street braces for AI tsunami](https://www.cnbc.com/2026/05/13/cerebras-prices-ipo-above-expected-range-wall-street-expects-ai-flood.html)**

Cerebras raised $5.55 billion in its IPO, and with the chipmaker's offering, investors are gearing up for some even bigger AI deals later this year.

CNBC • 6h ago

---

**[AI Chipmaker Cerebras Raises $5.55 Billion in Year’s Biggest IPO](https://www.bloomberg.com/news/articles/2026-05-13/ai-chipmaker-cerebras-said-poised-to-price-ipo-at-185-per-share)**

Bloomberg.com • 4h ago

---

**[Tech stocks today: Cerebras to stage blockbuster IPO, tech stocks climb as Cook, Musk, and Huang join Trump for China trip](https://finance.yahoo.com/sectors/technology/live/tech-stocks-today-cerebras-to-stage-blockbuster-ipo-tech-stocks-climb-as-cook-musk-and-huang-join-trump-for-china-trip-100000399.html)**

The tech sector helped US stocks cruise to all-time highs last week, as the artificial intelligence boom broadened.

Yahoo Finance • 6h ago

---

**[Cisco to cut thousands of jobs as AI push accelerates after earnings beat](https://www.foxbusiness.com/technology/cisco-cut-thousands-jobs-ai-push-accelerates-earnings-beat)**

Cisco reported record revenue and surging AI demand while announcing job cuts affecting thousands as it repositions for an AI-driven future.

Fox Business • 3h ago

---

**[Cisco to cut about 4,000 jobs in AI-focused restructuring as orders surge](https://finance.yahoo.com/news/cisco-raises-annual-revenue-forecast-200934306.html)**

Cisco said on Wednesday it would cut nearly 4,000 jobs, as part of a restructuring aimed at shifting investment toward artificial intelligence and ‌related growth areas, and raised its annual revenue forecast after a surge in hyperscaler ‌orders.  Shares of the San Jose, California-based networking equipment maker rose more than 16% in extended trading.  "The companies that will win in ​the AI era will be those with focus, urgency, and the discipline to continuously shift investment toward the areas where demand and long-term value creation are strongest," CEO Chuck Robbins said in a post on Cisco's website.

Yahoo Finance • 7h ago

---

**[Cisco's stock pops 17% on surging AI orders, as company says it's cutting almost 4,000 jobs](https://www.cnbc.com/2026/05/13/cisco-csco-q3-earnings-report-2026.html)**

Cisco's AI story has finally started resonating with Wall Street, with the stock hitting a record late last year and continuing to rally in 2026.

CNBC • 7h ago

---

**[Fanuc Shares Surge After Partnership With Google on Physical AI](https://www.bloomberg.com/news/articles/2026-05-14/fanuc-shares-surge-after-partnership-with-google-on-physical-ai)**

Bloomberg.com • 1h ago

---

**[Marketers put up guardrails as AI agents reshape programmatic buying](https://digiday.com/marketing/marketers-put-up-guardrails-as-ai-agents-reshape-programmatic-buying/)**

As AI agents enter programmatic advertising, marketers are adding guardrails to maintain oversight, transparency and control.

Digiday • 4m ago

---

**[Asia stocks rise on AI enthusiasm, focus on Trump-Xi summit](https://www.reuters.com/world/china/global-markets-wrapup-1pix-2026-05-14/)**

Reuters • 2h ago

---

**[OpenAI backs creation of global AI governance body led by the U.S. that would include China as a member](https://www.foxbusiness.com/technology/openai-backs-creation-global-ai-governance-body-led-u-s-would-include-china-member)**

OpenAI VP Chris Lehane supports creating a global AI governance body led by the U.S. that includes China, amid Trump's visit for talks with Xi Jinping.

Fox Business • 2h ago

---

---

## HackerNews: "ai"

**[If AI writes your code, why use Python?](https://news.ycombinator.com/item?id=48100433)**

For the last decade, fast-to-ship beat fast-to-run. Not anymore.

⬆️ 904 • 💬 960 • 2d ago • [Medium](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

---

**[I let AI build a tool to help me figure out what was waking me up at night](https://news.ycombinator.com/item?id=48100662)**

I try to pay attention to the small things that affect my quality of life. When something keeps bothering me, I want to investigate, find a likely cause, and act on it.

What changed recently is what I'm willing to build to support that. With AI tooling, projects I would

⬆️ 268 • 💬 281 • 2d ago • [Martin's Blog](https://martin.sh/i-let-ai-build-a-tool-to-help-me-figure-out-what-was-waking-me-up-at-night/)

---

**[Amazon employees are "tokenmaxxing" due to pressure to use AI tools](https://news.ycombinator.com/item?id=48110529)**

Workers are using an internal AI tool to automate non-essential tasks.

⬆️ 245 • 💬 246 • 1d ago • [Ars Technica](https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/)

---

**[Reimagining the mouse pointer for the AI era](https://news.ycombinator.com/item?id=48111581)**

Google DeepMind is transforming the mouse pointer into a context-aware AI partner. Move beyond the friction of traditional prompting with intuitive AI collaboration in Chrome and beyond.

⬆️ 245 • 💬 212 • 1d ago • [Google DeepMind](https://deepmind.google/blog/ai-pointer/)

---

**[Google says criminal hackers used AI to find a major software flaw](https://news.ycombinator.com/item?id=48094641)**

⬆️ 242 • 💬 175 • 2d ago • [nytimes.com](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html)

---

**[Students boo commencement speaker after she calls AI next industrial revolution](https://news.ycombinator.com/item?id=48096674)**

A commencement speaker at the University of Central Florida was booed, with graduating humanities students yelling out, "AI SUCKS!"

⬆️ 173 • 💬 214 • 2d ago • [404 Media](https://www.404media.co/ucf-ai-commencement-speaker-booed/)

---

**[The US is winning the AI race where it matters most: commercialization](https://news.ycombinator.com/item?id=48121929)**

Energy matters for AI, but the decisive layers are cloud infrastructure, data, and commercialization. On those layers the United States is ahead by a wide margin.

⬆️ 171 • 💬 491 • 14h ago • [Anton Krylov](https://avkcode.github.io/blog/us-winning-ai-race.html)

---

**[Meta won't let you block its AI account on Threads](https://news.ycombinator.com/item?id=48126981)**

Hey Meta, why are Threads users angry?

⬆️ 141 • 💬 63 • 7h ago • [The Verge](https://www.theverge.com/tech/929091/meta-ai-threads-account-block)

---

**[Show HN: Statewright – Visual state machines that make AI agents reliable](https://news.ycombinator.com/item?id=48108778)**

State machine guardrails for AI agents. Contribute to statewright/statewright development by creating an account on GitHub.

⬆️ 112 • 💬 51 • 1d ago • [GitHub](https://github.com/statewright/statewright)

---

**[I work in Hollywood. Everyone who used to make TV is now training AI](https://news.ycombinator.com/item?id=48093446)**

For screenwriters like me—and job seekers all over—AI gig work is the new waiting tables. In eight months, I’ve done 20 of these soul-crushing contracts for five different platforms. It’s bad.

⬆️ 106 • 💬 86 • 2d ago • [WIRED](https://www.wired.com/story/i-work-in-hollywood-everyone-who-used-to-make-tv-now-training-ai/)

---

---

## YouTube Videos: "ai"

**[AI is wild now](https://www.youtube.com/watch?v=HITUpHglMv4)**

Asmongold's Twitch: https://www.twitch.tv/zackrawrr ▻ Asmongold's X: https://x.com/asmongold ▻ Asmongold's Kick: ...

📺 Asmongold TV  

👁️ 345K • 👍 16K • 💬 6K • ⏱️ 25:34 • 1d ago

---

**[This 100% uncensored AI model is insane… let’s run it](https://www.youtube.com/watch?v=TS_hH4sdiKs)**

Wanna get ALL free resources from this video? Go here: https://davidondrej.com/uncensored-gemma Get my Hermes Agent setup ...

📺 David Ondrej

👁️ 71K • 👍 3K • 💬 239 • ⏱️ 22:54 • 2d ago

---

**[Hilarious viral AI ad depicts Karen Bass as Darth Vader](https://www.youtube.com/watch?v=9DBT_4KKjXQ)**

Sky News host Rita Panahi claims Spencer Pratt has gained momentum in the Los Angeles mayoral race after supporters ...

📺 Sky News Australia

👁️ 20K • 👍 1K • 💬 100 • ⏱️ 4:10 • 17h ago

---

**[&#39;No signs of AI slowing down&#39; — will it become a &#39;MACHINE GOD&#39;?](https://www.youtube.com/watch?v=jj05pc9tlc0)**

Should we think of AI as a co-intelligence and digital coworker rather than just a chatbot? Ethan Mollick, a professor at Wharton ...

📺 MS NOW

👁️ 8K • 👍 217 • 💬 107 • ⏱️ 58:06 • 1d ago

---

**[Meta workers revolt over surveillance as layoffs undermine AI profits | Natasha Bernal](https://www.youtube.com/watch?v=rdNW_7NoJMM)**

It's the first of what I expect be a series of studies on what actually is happening behind all of these AI related layoffs.” Technology ...

📺 The Tech Report

👁️ 47K • 👍 1K • 💬 447 • ⏱️ 28:26 • 11h ago

---

**[Claude Mythos Just Crossed A Dangerous Line... AGAIN!](https://www.youtube.com/watch?v=i-ioLtvb19o)**

Claude Mythos may have just crossed one of the strangest lines in AI. A new METR evaluation reportedly puts Mythos around the ...

📺 AI Revolution

👁️ 48K • 👍 1K • 💬 157 • ⏱️ 15:57 • 2d ago

---

**[AI Robots Just Unlocked Human-Level Skills… This Changes EVERYTHING](https://www.youtube.com/watch?v=xHxLB28wFxY)**

You're NOT ready for what just dropped in the world of robotics this week... Boston Dynamics Atlas pulled off a flawless handstand ...

📺 The AI Nexus

👁️ 3K • 👍 118 • 💬 11 • ⏱️ 55:02 • 13h ago

---

**[The AI layoffs end in 12 months and I know why](https://www.youtube.com/watch?v=doI1GYZ7r-w)**

Screwdrivers. https://techcrunch.com/2026/05/08/cloudflare-says-ai-made-1100-jobs-obsolete-even-as-revenue-hit-a-record-high/ ...

📺 Mo Bitar

👁️ 103K • 👍 6K • 💬 931 • ⏱️ 9:57 • 9h ago

---

**[The First AI Cyberattack Has Happened...](https://www.youtube.com/watch?v=6TtKdKQlrqg)**

Hello guys and gals, it's me Mutahar again! This time we take a look at what appears to be a pretty huge day for the Internet.

📺 SomeOrdinaryGamers

👁️ 255K • 👍 10K • 💬 1K • ⏱️ 17:29 • 1d ago

---

**[Students question value of college as costs rise and AI reshapes jobs](https://www.youtube.com/watch?v=n6CnTEVt0zE)**

This season's college commencement celebrations come at a sobering moment. Students are facing steep loans and dicey job ...

📺 PBS NewsHour

👁️ 67K • 👍 1K • ⏱️ 9:50 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 535,069 • ❤️ 840 • 5d ago

---

**[MiniCPM-V-4.6](https://huggingface.co/openbmb/MiniCPM-V-4.6)**

*OpenBMB*

MiniCPM-V 4.6 is an ultra-efficient, pocket-sized multimodal LLM for edge deployment, excelling in image and video understanding with mixed visual token compression. It offers strong multimodal capabilities comparable to larger models while achieving superior computational efficiency and broad mobile platform support.

`image-text-to-text` `1.3B`

⬇️ 3,494 • ❤️ 489 • 16h ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 110,182 • ❤️ 475 • 2d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 7,747 • ❤️ 306 • 1d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,420,384 • ❤️ 3,929 • 7d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a fast, on-device, multilingual text-to-speech model supporting 31 languages with ONNX Runtime for local inference. It offers high accuracy, low latency, and a compact size, suitable for applications requiring efficient, cloud-independent speech synthesis.

`text-to-speech`

⬇️ 4,954 • ❤️ 168 • 7d ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 11,486 • ❤️ 349 • 17d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 84,903 • ❤️ 246 • 3d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,772,193 • ❤️ 1,274 • 20d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter vision-language model optimized for efficient inference with MTP speculative decoding, supporting up to 1M+ token context. It excels at agentic coding, reasoning, and tool-calling, making it suitable for complex development workflows and iterative coding tasks.

`image-text-to-text` `27.3B`

⬇️ 25,924 • ❤️ 105 • 21h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 67 • 💬 3 • ⭐ 74,951 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 5 • 💬 0 • ⭐ 17,050 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[Pixal3D: Pixel-Aligned 3D Generation from Images](https://huggingface.co/papers/2605.10922)**

*Dong-Yang Li, Wang Zhao, Yuxin Chen et al. (8 authors)*

🏢 ARC Lab, Tencent PCG

Pixal3D introduces a pixel-aligned 3D generation approach that addresses fidelity issues in 3D asset creation by establishing direct pixel-to-3D correspondences through back-projection conditioning.

▲ 22 • 💬 3 • ⭐ 505 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.10922) • [💻 code](https://github.com/TencentARC/Pixal3D) • [🔗 project](https://ldyang694.github.io/projects/pixal3d/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 19 • 💬 3 • ⭐ 11,219 • 26d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[World Action Models: The Next Frontier in Embodied AI](https://huggingface.co/papers/2605.12090)**

*Siyin Wang, Junhao Shi, Zhaoyang Fu et al. (14 authors)*

🏢 OpenMOSS

World Action Models unify predictive state modeling with action generation for embodied policy learning, forming a cohesive framework for understanding environment dynamics and action prediction.

▲ 51 • 💬 1 • ⭐ 160 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12090) • [💻 code](https://github.com/OpenMOSS/Awesome-WAM) • [🔗 project](https://openmoss.github.io/Awesome-WAM/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 33 • 💬 3 • ⭐ 24,379 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 111 • 💬 10 • ⭐ 9,217 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 79 • 💬 7 • ⭐ 4,527 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://huggingface.co/papers/2605.12500)**

*Haiwen Diao, Penghao Wu, Hanming Deng et al. (58 authors)*

🏢 SenseNova

Unified vision-language models treat understanding and generation as integrated processes rather than separate tasks, demonstrating strong performance across multiple multimodal capabilities including image synthesis and action reasoning.

▲ 114 • 💬 1 • ⭐ 1,657 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.12500) • [💻 code](https://github.com/OpenSenseNova/SenseNova-U1)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 62,892 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.6k • 🔱 2.9k • 16d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.9k • 🔱 853 • 1d ago

---

**[crynta/terax-ai](https://github.com/crynta/terax-ai)**

Lightweight (7MB) AI terminal emulator (ADE) built in Rust & Tauri & React

`TypeScript` `agents` `ai` `code-editor` `linux` `macos`

⭐ 2.7k • 🔱 282 • 3h ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

A collection of agent skills for CAD, robotics and hardware design

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.6k • 🔱 299 • 3h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.6k • 🔱 234 • 8h ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.2k • 🔱 223 • 3d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.2k • 🔱 142 • 1h ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.0k • 🔱 302 • 6d ago

---

**[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)**

DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.

`TypeScript` `agent` `agent-framework` `ai-agent` `ai-coding` `cli`

⭐ 1.9k • 🔱 106 • 1m ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 1.8k • 🔱 311 • 40m ago

---

---

*Generated by PeekDeck - A glance is all you need*

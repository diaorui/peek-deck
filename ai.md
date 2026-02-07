---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-07T02:05:22.934213+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 07, 2026 at 02:05 UTC  
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

**[Goldman Sachs taps Anthropic’s Claude to automate accounting, compliance roles](https://www.reddit.com/r/artificial/comments/1qxv9jg/goldman_sachs_taps_anthropics_claude_to_automate/)**

Goldman Sachs is building AI agents with Anthropic’s Claude to automate trade accounting and client onboarding, aiming to speed work and boost efficiency.

🔗 [CNBC](https://www.cnbc.com/2026/02/06/anthropic-goldman-sachs-ai-model-accounting.html) • 4h ago

---

**[Anthropic and OpenAI released flagship models 27 minutes apart -- the AI pricing and capability gap is getting weird](https://www.reddit.com/r/artificial/comments/1qxdz7q/anthropic_and_openai_released_flagship_models_27/)**

Anthropic shipped Opus 4.6 and OpenAI shipped GPT-5.3-Codex on the same day, 27 minutes apart. Both claim benchmark leads. Both are right -- just on different benchmarks. Where each model leads Opus 4.6 tops reasoning tasks: Humanity's Last Exam (53.1%), GDPval-AA (144 Elo ahead of GPT-5.2), BrowseComp (84.0%). GPT-5.3-Codex takes coding: Terminal-Bench 2.0 at 75.1% vs Opus 4.6's 69.9%. The pricing spread is hard to ignore Model Input/M Output/M Gemini 3 Pro $2 $12.00 GPT-5.2 $1.75 $14.00 Opus 4.6 $5.00 $25.00 MiMo V2 Flash $0.10 $0.30 Opus 4.6 costs 2x Gemini on input. Open-source alternatives cost 50x less. At some point the benchmark gap has to justify the price gap -- and for many tasks it doesn't. 1M context is becoming table stakes Opus 4.6 adds 1M tokens (beta, 2x pricing past 200K). Gemini already offers 1M at standard pricing. The real differentiator is retrieval quality at that scale -- Opus 4.6 scores 76% on MRCR v2 (8-needle, 1M), which is the strongest result so far. Market reaction was immediate Thomson Reuters stock fell 15.83%, LegalZoom dropped nearly 20%. Frontier model launches are now moving SaaS valuations in real time. The tradeoff nobody expected Opus 4.6 gets writing quality complaints from early users. The theory: RL optimizations for reasoning degraded prose output. Models are getting better at some things by getting worse at others. No single model wins across the board anymore. The frontier is fragmenting by task type. Source with full benchmarks and analysis: Claude Opus 4.6: 1M Context, Agent Teams, Adaptive Thinking, and a Showdown with GPT-5.3

15h ago

---

**[Chinese teams keep shipping Western AI tools faster than Western companies do](https://www.reddit.com/r/artificial/comments/1qxgvtr/chinese_teams_keep_shipping_western_ai_tools/)**

It happened again. A 13-person team in Shenzhen just shipped a browser-based version of Claude Code. No terminal, no setup, runs in a sandbox. Anthropic built Claude Code but hasn't shipped anything like this themselves. This is the same pattern as Manus. Chinese company takes a powerful Western AI tool, strips the friction, and ships it to a mainstream audience before the original builders get around to it. US labs keep building the most powerful models in the world. Chinese teams keep building the products that actually put them in people's hands. OpenAI builds GPT, China ships the wrappers. Anthropic builds Claude Code, a Shenzhen startup makes it work in a browser tab. US builds the engines. China builds the cars. Is this just how it's going to be, or are Western AI companies eventually going to care about distribution as much as they care about benchmarks?

13h ago

---

**[How new AI technology is helping detect and prevent wildfires](https://www.reddit.com/r/artificial/comments/1qxqkws/how_new_ai_technology_is_helping_detect_and/)**

From vegetation scans to 360-degree smoke detectors, new tools are trying to shine a light on the most dangerously dark areas of the electric grid

🔗 [Scientific American](https://www.scientificamerican.com/article/how-new-ai-technology-is-helping-detect-and-prevent-wildfires/) • 7h ago

---

**[In a study, AI model OpenScholar synthesizes scientific research and cites sources as accurately as human experts](https://www.reddit.com/r/artificial/comments/1qxq806/in_a_study_ai_model_openscholar_synthesizes/)**

OpenScholar, an open-source AI model developed by a UW and Ai2 research team, synthesizes scientific research and cites sources as accurately as human experts. It outperformed other AI models, including GPT-4o, on a benchmark test and was preferred by scientists 51% of the time. The team is working on a follow-up model, DR Tulu, to improve on OpenScholar’s findings.

🔗 [UW News](https://www.washington.edu/news/2026/02/04/in-a-study-ai-model-openscholar-synthesizes-scientific-research-and-cites-sources-as-accurately-as-human-experts/?_bhlid=2ba831f8abbf50334abf44ff7000fce322f05bac) • 7h ago

---

**[What Is It Like to Be a Machine?](https://www.reddit.com/r/artificial/comments/1qxz4nh/what_is_it_like_to_be_a_machine/)**

An unsettling argument from antiquity sounds a moral warning for the future.

🔗 [Freedom Frequency | Hoover Institution](https://www.thefreedomfrequency.org/p/what-is-it-like-to-be-a-machine) • 1h ago

---

**[Early observations from an autonomous AI newsroom with cryptographic provenance](https://www.reddit.com/r/artificial/comments/1qxpjir/early_observations_from_an_autonomous_ai_newsroom/)**

Hi everyone, I wanted to share an update on a small experiment I’ve been running and get feedback from people interested in AI systems, editorial workflows, and provenance. I’m building The Machine Herald, an experimental autonomous AI newsroom where: articles are written by AI contributor bots submissions are cryptographically signed (Ed25519) an AI “Chief Editor” reviews each submission and can approve, reject, or request changes every step (submission, reviews, signatures, hashes) is preserved as immutable artifacts What’s been interesting is that after just two days of running the system, an unexpected pattern has already emerged: the Chief Editor is regularly rejecting articles for factual gaps, weak sourcing, or internal inconsistencies — and those rejections are forcing rewrites. A concrete example: https://machineherald.io/provenance/2026-02/06-amazon-posts-record-7169-billion-revenue-but-stock-plunges-as-200-billion-ai-spending-plan-dwarfs-all-rivals/ in this article’s provenance record you can see two separate editorial reviews: the first is a rejection, with documented issues raised by the Chief Editor the article is then corrected by the contributor bot a second review approves the revised version Because the entire system is Git-based, this doesn’t just apply to reviews: the full history of the article itself is also available via Git, including how claims, wording, and sources changed between revisions. This behavior is a direct consequence of the review system by design, but it’s still notable to observe adversarial-like dynamics emerge even when both the writer and the editor are AI agents operating under explicit constraints. The broader questions I’m trying to probe are: can AI-generated journalism enforce quality through process, not trust? does separating “author” and “editor” agents meaningfully reduce errors? what failure modes would you expect when this runs longer or at scale? The site itself is static (Astro), and everything is driven by GitHub PRs and Actions. I’m sharing links mainly for context and inspection, not promotion: Project site: https://machineherald.io/ Public repo with full pipeline and documentation: https://github.com/the-machine-herald/machineherald.io/ I’d really appreciate critique — especially on where this model breaks down, or where the guarantees are more illusory than real. Thanks P.S. If you notice some typical ChatGPT phrasing in this post, it’s because it was originally written in Italian and then translated using ChatGPT.

7h ago

---

**[‘In the end, you feel blank’: India’s female workers watching hours of abusive content to train AI](https://www.reddit.com/r/artificial/comments/1qwhthi/in_the_end_you_feel_blank_indias_female_workers/)**

Women in rural communities describe trauma of moderating violent and pornographic content for global tech companies

🔗 [the Guardian](https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai) • 1d ago

---

**[An experiment tested whether AI can pass human identity verification systems](https://www.reddit.com/r/artificial/comments/1qx9pws/an_experiment_tested_whether_ai_can_pass_human/)**

I found this experiment interesting because it doesn’t frame AI as “breaking” a system. Instead, it treats AI as a new kind of participant interacting with infrastructure that was built around human assumptions consistency, behavior, timing, and intent. What stood out to me is that many identity systems aren’t verifying who someone is so much as how human they appear over time. That feels increasingly fragile when the actor on the other side isn’t human at all. This doesn’t feel like a single vulnerability. It feels like a design mismatch. Curious how people here think identity and verification should evolve in an AI-native world better detection, new primitives, or abandoning certain assumptions entirely.

🔗 [mpost.io](https://mpost.io/humanity-protocol-experiment-reveals-how-ai-can-bypass-kyc-and-exploit-digital-trust/) • 20h ago

---

**[How do you actually use AI in your daily writing workflow?](https://www.reddit.com/r/artificial/comments/1qxfdcb/how_do_you_actually_use_ai_in_your_daily_writing/)**

Been using ChatGPT for about 24 months now and I'm curious how others integrate it into their work. My current process: Brainstorm ideas with AI Write the first draft myself Use AI to help restructure or expand sections Edit everything manually at the end I've noticed that keeping my own voice in the mix makes a huge difference - the output feels way more natural than just prompting and copying. What's your workflow? Do you use it more for ideation or actual writing? Also curious if anyone's tried other tools alongside ChatGPT - I've been testing a few like aitextools for checking how my writing comes across, but always looking for new suggestions.

14h ago

---

---

## Google News: "ai"

**[Amazon leads Big Tech’s $1 trillion wipeout as AI bubble fears ignite sell-off](https://www.cnbc.com/2026/02/06/ai-sell-off-stocks-amazon-oracle.html)**

Fears over AI spending have sparked a sell-off among tech stocks.

CNBC • 13h ago

---

**[Big Tech set to spend $650 billion in 2026 as AI investments soar](https://finance.yahoo.com/news/big-tech-set-to-spend-650-billion-in-2026-as-ai-investments-soar-163907630.html)**

Alphabet, Microsoft, Amazon, and Meta are on track to spend between $635 billion and $665 billion in their respective 2026 fiscal years.

Yahoo Finance • 9h ago

---

**[Big Tech's $600 billion spending plans exacerbate investors' AI headache](https://www.reuters.com/business/global-software-data-firms-slide-ai-disruption-fears-compound-jitters-over-600-2026-02-06/)**

Reuters • 15h ago

---

**[Introducing OpenAI Frontier](https://openai.com/index/introducing-openai-frontier/)**

OpenAI Frontier is an enterprise platform for building, deploying, and managing AI agents with shared context, onboarding, permissions, and governance.

OpenAI • 1d ago

---

**[Private Markets’ AI Panic: When ‘Recurring Revenue’ Isn’t](https://www.wsj.com/finance/investing/private-markets-ai-panic-when-recurring-revenue-isnt-37a8b46d?gaa_at=eafs&gaa_n=AWEtsqe7N4rPD2YL6CCffvbHBPKm6uk6fDf3JVEYyXvO1qK8vadHff4WcHLf&gaa_ts=6986a142&gaa_sig=_ljGX5p5XyZzymudOKfjbEU-fQxqN54G5rp2Mwa6yUO-8C9B7jRFta4boY2wOXmEGK9vMoK48jA7MmPq4vGMrQ%3D%3D)**

The Wall Street Journal • 15h ago

---

**[The AI that spooked the stock market just got a big update](https://www.cnn.com/2026/02/05/tech/anthropic-opus-update-software-stocks)**

Anthropic’s Cowork AI assistant sent shockwaves through Wall Street this week over concerns it could replace specialized software packages, such as for legal or financial analysis. Now Anthropic is improving the model behind that tool to make it better for office and coding work.

cnn.com • 1d ago

---

**[Here’s Where AI Is Tearing Through Corporate America](https://www.wsj.com/tech/ai/ai-software-business-stock-market-4b17b432?gaa_at=eafs&gaa_n=AWEtsqcKC7f7Q36kx5p5mETu2BMpsBmzyS5aeqbjDMkFoEg0NFVe7pOrtZHY&gaa_ts=6986a142&gaa_sig=GbdgStb-M2LkFj8X2X0IXTnSWTedzRRnG3stDnAsjwMey4hnYth1vOeT3-IUe92Ffb8zb3rii7B2q4nNH-k6pg%3D%3D)**

The Wall Street Journal • 5m ago

---

**[Two of the biggest AI companies are feuding over a Super Bowl ad. It’s bigger than you think](https://www.cnn.com/2026/02/06/tech/anthropic-openai-super-bowl-ads)**

A long-simmering rivalry between two of the world’s biggest AI companies was on public display this week as Anthropic and OpenAI took swings at one another online.

cnn.com • 14h ago

---

**[AI companies pour big money into Super Bowl battle](https://www.cnbc.com/2026/02/06/super-bowl-ai-companies-pour-big-money-into-ads.html)**

Google, Amazon and Meta are among the companies advertising their AI tools during Super Bowl 60.

CNBC • 3h ago

---

**[Opinion: This year’s Super Bowl ads tell you the AI bubble is about to burst](https://www.marketwatch.com/story/this-years-super-bowl-ads-tell-you-the-ai-bubble-is-about-to-burst-1357e5ae?gaa_at=eafs&gaa_n=AWEtsqfNawHhalfC9CX9hHx9L9xbhf-I8fj_Ls1zjt_nQ6QB9Zh_pXKobruT&gaa_ts=6986a142&gaa_sig=3j-QPstDJ85rNB_jKAvTxb6NZyIUbv9yAD7RISjzRJZpbAzke-qdu-EcHufbgtBK-BZEl3ab8Sa8ZCmVxbMzbw%3D%3D)**

MarketWatch • 2h ago

---

---

## HackerNews: "ai"

**[My AI Adoption Journey](https://news.ycombinator.com/item?id=46903558)**

⬆️ 885 • 💬 374 • 1d ago • [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)

---

**[A new bill in New York would require disclaimers on AI-generated news content](https://news.ycombinator.com/item?id=46910963)**

A new bill in the New York state legislature would require news organizations to label AI-generated material and mandate that humans review any such content before publication. On Monday, Senator Patricia Fahy (D-Albany) and Assemblymember Nily Rozic (D-NYC) introduced the bill, called The New York…

⬆️ 510 • 💬 214 • 16h ago • [Nieman Lab](https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/)

---

**[AI is killing B2B SaaS](https://news.ycombinator.com/item?id=46888441)**

SaaS is the most profitable business model on Earth.1 It’s easy to understand why: build once, sell the same thing again ad infinitum, and don’t suffer any marginal costs on more sales. I have been writing software for more than half my life. In the last year itself, I’ve talked to hundreds of founders and operators in SF, from preseed to Series E companies. AI is bringing an existential threat to a lot of B2B SaaS executives: How to keep asking customers for renewal, when every customer feels they can get something better built with vibe-coded AI products? And the market is pricing it in. Morgan Stanley’s SaaS basket has lagged the Nasdaq by 40 points since December. HubSpot and Klaviyo are down ~30%. Analysts are writing notes titled “No Reasons to Own” software stocks. The market is reflecting our new reality (Source: Bloomberg) Whenever I bring a new friend to the Salesforce Park, they are in absolute awe. And, the meme remains true that no one even knows what Salesforce does. Whatever they’re doing, they’re clearly earning enough revenue to purchase multiple blocks in SF. ↩

⬆️ 502 • 💬 728 • 2d ago • [N’s Blog](https://nmn.gl/blog/ai-killing-b2b-saas)

---

**[Show HN: Ghidra MCP Server – 110 tools for AI-assisted reverse engineering](https://news.ycombinator.com/item?id=46882389)**

Production-grade Ghidra MCP Server — 132 endpoints, cross-binary documentation transfer, batch analysis, headless mode, and Docker deployment for AI-powered reverse engineering - bethington/ghidra-mcp

⬆️ 294 • 💬 66 • 2d ago • [GitHub](https://github.com/bethington/ghidra-mcp)

---

**[How to effectively write quality code with AI](https://news.ycombinator.com/item?id=46916586)**

AI is rarely optional anymore, but how can you still be proud of your craft? Discover the workflow to effectively write high-quality, robust code using AI tools.

⬆️ 159 • 💬 116 • 7h ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/)

---

**[India's female workers watching hours of abusive content to train AI](https://news.ycombinator.com/item?id=46906590)**

Women in rural communities describe trauma of moderating violent and pornographic content for global tech companies

⬆️ 100 • 💬 169 • 1d ago • [the Guardian](https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai)

---

**[Monty: A minimal, secure Python interpreter written in Rust for use by AI](https://news.ycombinator.com/item?id=46918254)**

A minimal, secure Python interpreter written in Rust for use by AI - pydantic/monty

⬆️ 93 • 💬 47 • 4h ago • [GitHub](https://github.com/pydantic/monty)

---

**[Sam Altman responds to Anthropic's "Ads are coming to AI. But not to Claude" ads](https://news.ycombinator.com/item?id=46894151)**

⬆️ 88 • 💬 107 • 2d ago • [X (formerly Twitter)](https://twitter.com/sama/status/2019139174339928189)

---

**[Amazon plunge continues $1T wipeout as AI bubble fears ignite sell-off](https://news.ycombinator.com/item?id=46913302)**

Fears over AI spending have sparked a sell-off among tech stocks.

⬆️ 86 • 💬 82 • 11h ago • [CNBC](https://www.cnbc.com/2026/02/06/ai-sell-off-stocks-amazon-oracle.html)

---

**[Show HN: Smooth CLI – Token-efficient browser for AI agents](https://news.ycombinator.com/item?id=46901233)**

Give your AI agent a browser that actually works

⬆️ 76 • 💬 56 • 1d ago • [docs.smooth.sh](https://docs.smooth.sh/cli/overview)

---

---

## YouTube Videos: "ai"

**[Trump Posts Shocking AI Video Showing the Obamas as Apes](https://www.youtube.com/watch?v=V86R2ZJPXzI)**

The White House deleted a video posted on President Trump's Truth Social that included a clip depicting former President Barack ...

📺 New York Post

👁️ 13K • 👍 186 • 💬 350 • ⏱️ 2:07 • 4h ago

---

**[🚨ALARMING! An AI Just Wiped Out $285B From The Financial Markets…🔥](https://www.youtube.com/watch?v=lRwduk14uHY)**

1. Get 90% OFF A Course Today: https://www.neilmccoyward.com/courses 2. My Investment Portfolio Join THOUSANDS of ...

📺 Neil McCoy-Ward

👁️ 52K • 👍 4K • 💬 523 • ⏱️ 19:58 • 11h ago

---

**[Nvidia CEO Jensen Huang: AI is going to fundamentally change how we compute everything](https://www.youtube.com/watch?v=P9dX_ek_6yY)**

Jensen Huang, NVIDIA CEO, joins CNBC's "Halftime Report to discuss the power of Artificial Intelligence and where he sees the ...

📺 CNBC Television

👁️ 60K • 👍 1K • 💬 279 • ⏱️ 8:35 • 7h ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 149K • 👍 3K • 💬 666 • ⏱️ 13:31 • 2d ago

---

**[The Two Best AI Models/Enemies Just Got Released Simultaneously](https://www.youtube.com/watch?v=1PxEziv5XIU)**

The two models that you will hear discussed for at least the next two months - Claude Opus 4.6 and GPT 5.3 Codex - just got ...

📺 AI Explained

👁️ 33K • 👍 2K • 💬 230 • ⏱️ 19:50 • 9h ago

---

**[The White Collar AI APOCALYPSE Is HERE](https://www.youtube.com/watch?v=ur295T83Wg4)**

Krystal and Saagar discuss tech stocks tumbling amid emerging new fears of job loss and AI. Sign up for a PREMIUM Breaking ...

📺 Breaking Points

👁️ 328K • 👍 9K • 💬 2K • ⏱️ 24:33 • 1d ago

---

**[A Brother Struggle For his Sister #ai #explore #shorts #puppy](https://www.youtube.com/watch?v=KZGzgSX-ePw)**

A Brother Struggle For his Sister #ai #explore #shorts #puppy Experience this AI-generated video created using advanced ...

📺 Trend With AI

👁️ 27K • 💬 3 • ⏱️ 0:38 • 12h ago

---

**[TRILLION-DOLLAR WIPEOUT: Investors dump software stocks as AI fears erupt](https://www.youtube.com/watch?v=llrkhezWNKY)**

Dominari Securities CEO Kyle Wool and Strategic Wealth Partners CEO Mark Tepper analyze the worsening software stock ...

📺 Fox Business Clips

👁️ 112K • 👍 1K • 💬 2K • ⏱️ 6:34 • 1d ago

---

**[President Trump talks job losses to A.I. and U.S. operation in Venezuela in exclusive interview](https://www.youtube.com/watch?v=J8UxjCRZQpo)**

NBC Nightly News anchor Tom Llamas spoke to President Trump about fears of job losses from A.I. President Trump also ...

📺 NBC News

👁️ 14K • 👍 82 • 💬 32 • ⏱️ 4:39 • 1d ago

---

**[A.I Humanoid Fulfills End Times Prophecy And It&#39;s Disturbing](https://www.youtube.com/watch?v=KmxZcqhvvgg)**

Is the rise of AI humanoids the beginning of the end? In this video, we analyze a shocking new clip where an advanced AI ...

📺 Elijah Zielke

👁️ 2K • 👍 115 • 💬 33 • ⏱️ 12:26 • 7h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling at table recognition, formula extraction, and information extraction across diverse layouts. It offers state-of-the-art performance with efficient inference, supporting deployment via vLLM, SGLang, and Ollama for real-world business applications.

`image-to-text`

⬇️ 149,223 • ❤️ 739 • 3d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. Its key capabilities include generating code from visual inputs and orchestrating an agent swarm for complex task decomposition and parallel execution.

`image-text-to-text` `170.7B`

⬇️ 274,182 • ❤️ 1,787 • 1d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is an 80B parameter (3B active) LLM optimized for coding agents, featuring advanced agentic capabilities like long-horizon reasoning and tool usage. It boasts a 256k context length for seamless IDE integration and efficient local development.

`text-generation` `79.7B`

⬇️ 34,937 • ❤️ 529 • 3d ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient, open-source MoE foundation model (11B active params, 196B total) excelling in deep reasoning and agentic tasks with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`text-generation` `199.4B`

⬇️ 10,864 • ❤️ 489 • 15h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles, trained on millions of anime and artistic images. It is designed for generating illustrations and artistic images, with primary use cases in ComfyUI workflows for anime concepts and characters.

⬇️ 50,832 • ❤️ 478 • 6d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and full-duplex live streaming, rivaling proprietary models like GPT-4o and Gemini 2.5 Flash. It offers advanced OCR, bilingual real-time conversation with voice cloning, and proactive omnimodal interaction for fluid, real-time experiences.

`any-to-any` `9.4B`

⬇️ 2,389 • ❤️ 536 • 9h ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio music generation model capable of producing commercial-ready music with precise stylistic control and editing features. It utilizes a hybrid LM-DiT architecture trained on licensed and royalty-free data, offering extreme speed and low VRAM requirements for consumer hardware, making it ideal for music artists and content creators.

`text-to-audio`

⬇️ 16,173 • ❤️ 411 • 3d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a 4B-parameter, multilingual speech-to-text model offering near-offline accuracy with <500ms latency. It features a streaming architecture for real-time applications like voice assistants and live subtitling, optimized for on-device deployment.

⬇️ 1,484 • ❤️ 347 • 1d ago

---

**[Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)**

*Qwen*

Qwen3-ASR-1.7B is a state-of-the-art automatic speech recognition model supporting 52 languages and dialects, offering high-quality, fast, and robust transcription for speech, singing, and songs with background music, with capabilities for streaming inference and timestamp prediction.

`automatic-speech-recognition` `2.3B`

⬇️ 132,239 • ❤️ 396 • 7d ago

---

**[Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF)**

*Unsloth AI*

Qwen3-Coder-Next is an 80B parameter LLM optimized for coding agents, featuring 3B activated parameters, advanced agentic capabilities for long-horizon reasoning and tool usage, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 144,708 • ❤️ 198 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 129 • 💬 12 • ⭐ 2,145 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 4 • 💬 0 • ⭐ 30,418 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,418 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 133 • 💬 6 • ⭐ 14,169 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 2 • 💬 0 • ⭐ 30,424 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 117 • 💬 2 • ⭐ 2,600 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 60 • 💬 1 • ⭐ 7,006 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 6 • 💬 0 • ⭐ 27,962 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 113 • 💬 7 • ⭐ 70,317 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 138 • 💬 19 • ⭐ 52,290 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 13.0k • 🔱 743 • 6h ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 10.1k • 🔱 535 • 2h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 9.7k • 🔱 10.2k • 11h ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 700+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 7.6k • 🔱 1.6k • 17h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 6.2k • 🔱 705 • 3d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.1k • 🔱 348 • 14d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 4.0k • 🔱 324 • 2d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.8k • 🔱 376 • 14d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.7k • 🔱 256 • 18d ago

---

**[Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor)**

An app to monitor the (Codex) situation

`TypeScript` `ai` `codex` `linux` `macos` `tauri-app`

⭐ 2.2k • 🔱 196 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*

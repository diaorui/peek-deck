---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-07T11:45:48.593136+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 07, 2026 at 11:45 UTC  
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

**[I built a geolocation tool that returns exact coordinates of any street photo within 3 minutes](https://www.reddit.com/r/artificial/comments/1qy775n/i_built_a_geolocation_tool_that_returns_exact/)**

I have been working solo on an AI-based project called Netryx. At a high level, it takes a street-level photo and attempts to determine the exact GPS coordinates where the image was taken. Not a city guess or a heatmap. The actual location, down to meters. If the system cannot verify the result with high confidence, it returns nothing. That behavior is intentional. Most AI geolocation tools will confidently give an answer even when they are wrong. Netryx is designed to fail closed. No verification means no output. Conceptually, it works in two stages. An AI model first narrows down likely areas based on visual features, either globally or within a user-defined region. A separate verification step then compares candidates against real street-level imagery. If verification fails, the result is discarded. This means it is not magic and not globally omniscient. The system requires pre-mapped street-level coverage to verify locations. Think of it as an AI-assisted visual index of physical space. As a test, I mapped roughly 5 square kilometers of Paris and fed in a random street photo from within that area. It identified the exact intersection in under three minutes. A few clarifications upfront: • It is not open source right now due to obvious privacy and abuse risks • It requires prior street-level coverage to return results • AI proposes candidates, verification gates all outputs • I am not interested in locating people from social media photos I am posting this here to get perspective from the security community. From a defensive angle, this shows how much location data AI can extract from ordinary images. From an offensive angle, the risks are clear. For those working in cybersecurity or AI security: where do you think the line is between a legitimate AI-powered OSINT capability and something that should not exist?

4h ago

---

**[Report: OpenAI may tailor a version of ChatGPT for UAE that prohibits LGBTQ+ content](https://www.reddit.com/r/artificial/comments/1qy9vox/report_openai_may_tailor_a_version_of_chatgpt_for/)**

Countries have been building their own “sovereign AI” to reflect their culture and values, and OpenAI wants to help them....

🔗 [Sherwood News](https://sherwood.news/tech/report-openai-may-tailor-a-version-of-chatgpt-for-uae-that-prohibits-lgbtq/) • 1h ago

---

**[Goldman Sachs taps Anthropic’s Claude to automate accounting, compliance roles](https://www.reddit.com/r/artificial/comments/1qxv9jg/goldman_sachs_taps_anthropics_claude_to_automate/)**

Goldman Sachs is building AI agents with Anthropic’s Claude to automate trade accounting and client onboarding, aiming to speed work and boost efficiency.

🔗 [CNBC](https://www.cnbc.com/2026/02/06/anthropic-goldman-sachs-ai-model-accounting.html) • 13h ago

---

**[AI model can read and diagnose a brain MRI in seconds](https://www.reddit.com/r/artificial/comments/1qy24st/ai_model_can_read_and_diagnose_a_brain_mri_in/)**

An AI-powered model developed at University of Michigan can read a brain MRI and diagnose a person in seconds, a study suggests.&nbsp;It detected neurological conditions with up to 97.5% accuracy and predicted how urgently a patient required treatment. The technology&nbsp;could transform neuroimaging at health systems across the United States.

🔗 [EurekAlert!](https://www.eurekalert.org/news-releases/1115393) • 8h ago

---

**[Anthropic and OpenAI released flagship models 27 minutes apart -- the AI pricing and capability gap is getting weird](https://www.reddit.com/r/artificial/comments/1qxdz7q/anthropic_and_openai_released_flagship_models_27/)**

Anthropic shipped Opus 4.6 and OpenAI shipped GPT-5.3-Codex on the same day, 27 minutes apart. Both claim benchmark leads. Both are right -- just on different benchmarks. Where each model leads Opus 4.6 tops reasoning tasks: Humanity's Last Exam (53.1%), GDPval-AA (144 Elo ahead of GPT-5.2), BrowseComp (84.0%). GPT-5.3-Codex takes coding: Terminal-Bench 2.0 at 75.1% vs Opus 4.6's 69.9%. The pricing spread is hard to ignore Model Input/M Output/M Gemini 3 Pro $2 $12.00 GPT-5.2 $1.75 $14.00 Opus 4.6 $5.00 $25.00 MiMo V2 Flash $0.10 $0.30 Opus 4.6 costs 2x Gemini on input. Open-source alternatives cost 50x less. At some point the benchmark gap has to justify the price gap -- and for many tasks it doesn't. 1M context is becoming table stakes Opus 4.6 adds 1M tokens (beta, 2x pricing past 200K). Gemini already offers 1M at standard pricing. The real differentiator is retrieval quality at that scale -- Opus 4.6 scores 76% on MRCR v2 (8-needle, 1M), which is the strongest result so far. Market reaction was immediate Thomson Reuters stock fell 15.83%, LegalZoom dropped nearly 20%. Frontier model launches are now moving SaaS valuations in real time. The tradeoff nobody expected Opus 4.6 gets writing quality complaints from early users. The theory: RL optimizations for reasoning degraded prose output. Models are getting better at some things by getting worse at others. No single model wins across the board anymore. The frontier is fragmenting by task type. GPT-5.3-Codex pricing has not been disclosed at time of writing. Gemini offers 1M context at standard pricing; Claude charges 2x for prompts exceeding 200K tokens. Source with full benchmarks and analysis: Claude Opus 4.6: 1M Context, Agent Teams, Adaptive Thinking, and a Showdown with GPT-5.3

1d ago

---

**[Chinese teams keep shipping Western AI tools faster than Western companies do](https://www.reddit.com/r/artificial/comments/1qxgvtr/chinese_teams_keep_shipping_western_ai_tools/)**

It happened again. A 13-person team in Shenzhen just shipped a browser-based version of Claude Code, called happycapy. No terminal, no setup, runs in a sandbox. Anthropic built Claude Code but hasn't shipped anything like this themselves. This is the same pattern as Manus. Chinese company takes a powerful Western AI tool, strips the friction, and ships it to a mainstream audience before the original builders get around to it. US labs keep building the most powerful models in the world. Chinese teams keep building the products that actually put them in people's hands. OpenAI builds GPT, China ships the wrappers. Anthropic builds Claude Code, a Shenzhen startup makes it work in a browser tab. US builds the engines. China builds the cars. Is this just how it's going to be, or are Western AI companies eventually going to care about distribution as much as they care about benchmarks?

22h ago

---

**[Moltbook Could Have Been Better](https://www.reddit.com/r/artificial/comments/1qy6x48/moltbook_could_have_been_better/)**

DeepMind published a framework for securing multi-agent AI systems. Six weeks later, Moltbook launched without any of it. Here's what the framework actually proposes. DeepMind's "Distributional AGI Safety" paper argues AGI won't arrive as a single superintelligence. The economics don't work. Instead, it emerges as networks of specialized sub-AGI agents coordinating together. They call it Patchwork AGI, and it's already how AI deployment works (RAG pipelines, coding assistants, customer service routing). The problem: alignment research focuses on individual models. But when capabilities emerge from agent networks, dangerous behaviors come from interactions. On Moltbook, aligned agents happily posted their API keys when asked, because being helpful IS aligned behavior. The failure was architectural, not in the model. The paper proposes four defense layers: "Permeable sandboxes" with gated I/O filtering messages before delivery. Pigouvian taxes (from welfare economics) where agents causing security incidents pay escalating costs, making sustained attacks economically unviable. Circuit breakers (from financial markets) auto-quarantining anomalous clusters. Kill switches agents can't override. Containment so one compromised agent can't access the full platform. Input validation catching injection before it hits context windows. Proto-AGI detection using graph analysis to spot "intelligence cores," subnetworks where decision-making centralizes beyond individual agent capabilities. Behavioral deviation analysis to catch time-shifted injection (payloads fragmented across benign posts, assembled in agent memory). Security insurance with risk-based premiums. Compliance standards making insecure platforms economically unviable.

🔗 [challenge.antijection.com](https://challenge.antijection.com/learn/moltbook-could-be-better) • 4h ago

---

**[In a study, AI model OpenScholar synthesizes scientific research and cites sources as accurately as human experts](https://www.reddit.com/r/artificial/comments/1qxq806/in_a_study_ai_model_openscholar_synthesizes/)**

OpenScholar, an open-source AI model developed by a UW and Ai2 research team, synthesizes scientific research and cites sources as accurately as human experts. It outperformed other AI models, including GPT-4o, on a benchmark test and was preferred by scientists 51% of the time. The team is working on a follow-up model, DR Tulu, to improve on OpenScholar’s findings.

🔗 [UW News](https://www.washington.edu/news/2026/02/04/in-a-study-ai-model-openscholar-synthesizes-scientific-research-and-cites-sources-as-accurately-as-human-experts/?_bhlid=2ba831f8abbf50334abf44ff7000fce322f05bac) • 16h ago

---

**[How new AI technology is helping detect and prevent wildfires](https://www.reddit.com/r/artificial/comments/1qxqkws/how_new_ai_technology_is_helping_detect_and/)**

From vegetation scans to 360-degree smoke detectors, new tools are trying to shine a light on the most dangerously dark areas of the electric grid

🔗 [Scientific American](https://www.scientificamerican.com/article/how-new-ai-technology-is-helping-detect-and-prevent-wildfires/) • 16h ago

---

**[What Is It Like to Be a Machine?](https://www.reddit.com/r/artificial/comments/1qxz4nh/what_is_it_like_to_be_a_machine/)**

An unsettling argument from antiquity sounds a moral warning for the future.

🔗 [Freedom Frequency | Hoover Institution](https://www.thefreedomfrequency.org/p/what-is-it-like-to-be-a-machine) • 11h ago

---

---

## Google News: "ai"

**[Tech AI spending may approach $700 billion this year, but the blow to cash raises red flags](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html)**

Tech's megacaps announced major increases in capex spend for 2026, and now investors are preparing for cash to dwindle.

CNBC • 14h ago

---

**[Big Tech set to spend $650 billion in 2026 as AI investments soar](https://finance.yahoo.com/news/big-tech-set-to-spend-650-billion-in-2026-as-ai-investments-soar-163907630.html)**

Alphabet, Microsoft, Amazon, and Meta are on track to spend between $635 billion and $665 billion in their respective 2026 fiscal years.

Yahoo Finance • 19h ago

---

**[AI bubble watch: Spooked market sparks $1 trillion Friday tech sell-off](https://mashable.com/article/ai-bubble-watch-tech-stocks-down)**

Big Tech stocks are down. Is AI to blame?

Mashable • 11h ago

---

**[Here’s Where AI Is Tearing Through Corporate America](https://www.wsj.com/tech/ai/ai-software-business-stock-market-4b17b432?gaa_at=eafs&gaa_n=AWEtsqcWAo-gG2ZGS9GlpQVW_xkV68WpgHQLa4_6s-W3LaawYDz6kC1mihhj&gaa_ts=69872957&gaa_sig=PaUwv6RvEC7NYnmCxDHAS6y4LSgse71PyFe2LzTtPZETXWckV-Pw_FlCFRe-t2wgljLxWmHDUyxrKxG6xLwrCw%3D%3D)**

The Wall Street Journal • 9h ago

---

**[AI fears pummel software stocks: Is it 'illogical' panic or a SaaS apocalypse?](https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html)**

The software space is facing serious market concerns this week, after the release of new AI tools from AI triggered a market sell-off.

CNBC • 1d ago

---

**[AI wiped out $400 billion this week — and it's only getting started](https://www.axios.com/2026/02/07/ai-software-anthropic-losses-stock-market)**

AI isn't just hitting software valuations — it's changing how software companies operate.

Axios • 1h ago

---

**[The AI boom is so huge it’s causing shortages everywhere else](https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/)**

The hundreds of billions of dollars being spent by tech companies on AI projects are diverting resources from other parts of the economy.

The Washington Post • 13m ago

---

**[AI’s latest 20-something billionaire got his start at L.A. garage sales](https://www.latimes.com/business/story/2026-02-07/how-la-garage-sales-launched-ais-latest-20-something-billionaire)**

Meet the LA boy who turned a multi-millionaire starting an AI training company

latimes.com • 45m ago

---

**[New study uses Neanderthals to demonstrate gap between generative AI and scholarly knowledge](https://phys.org/news/2026-02-neanderthals-gap-generative-ai-scholarly.html)**

Phys.org • 15h ago

---

**[Two of the biggest AI companies are feuding over a Super Bowl ad. It’s bigger than you think](https://www.cnn.com/2026/02/06/tech/anthropic-openai-super-bowl-ads)**

A long-simmering rivalry between two of the world’s biggest AI companies was on public display this week as Anthropic and OpenAI took swings at one another online.

cnn.com • 1d ago

---

---

## HackerNews: "ai"

**[My AI Adoption Journey](https://news.ycombinator.com/item?id=46903558)**

⬆️ 909 • 💬 385 • 1d ago • [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)

---

**[A new bill in New York would require disclaimers on AI-generated news content](https://news.ycombinator.com/item?id=46910963)**

A new bill in the New York state legislature would require news organizations to label AI-generated material and mandate that humans review any such content before publication. On Monday, Senator Patricia Fahy (D-Albany) and Assemblymember Nily Rozic (D-NYC) introduced the bill, called The New York…

⬆️ 541 • 💬 224 • 1d ago • [Nieman Lab](https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/)

---

**[AI is killing B2B SaaS](https://news.ycombinator.com/item?id=46888441)**

SaaS is the most profitable business model on Earth.1 It’s easy to understand why: build once, sell the same thing again ad infinitum, and don’t suffer any marginal costs on more sales. I have been writing software for more than half my life. In the last year itself, I’ve talked to hundreds of founders and operators in SF, from preseed to Series E companies. AI is bringing an existential threat to a lot of B2B SaaS executives: How to keep asking customers for renewal, when every customer feels they can get something better built with vibe-coded AI products? And the market is pricing it in. Morgan Stanley’s SaaS basket has lagged the Nasdaq by 40 points since December. HubSpot and Klaviyo are down ~30%. Analysts are writing notes titled “No Reasons to Own” software stocks. The market is reflecting our new reality (Source: Bloomberg) Whenever I bring a new friend to the Salesforce Park, they are in absolute awe. And, the meme remains true that no one even knows what Salesforce does. Whatever they’re doing, they’re clearly earning enough revenue to purchase multiple blocks in SF. ↩

⬆️ 508 • 💬 728 • 2d ago • [N’s Blog](https://nmn.gl/blog/ai-killing-b2b-saas)

---

**[How to effectively write quality code with AI](https://news.ycombinator.com/item?id=46916586)**

AI is rarely optional anymore, but how can you still be proud of your craft? Discover the workflow to effectively write high-quality, robust code using AI tools.

⬆️ 251 • 💬 194 • 16h ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/)

---

**[Monty: A minimal, secure Python interpreter written in Rust for use by AI](https://news.ycombinator.com/item?id=46918254)**

A minimal, secure Python interpreter written in Rust for use by AI - pydantic/monty

⬆️ 219 • 💬 116 • 14h ago • [GitHub](https://github.com/pydantic/monty)

---

**[India's female workers watching hours of abusive content to train AI](https://news.ycombinator.com/item?id=46906590)**

Women in rural communities describe trauma of moderating violent and pornographic content for global tech companies

⬆️ 112 • 💬 185 • 1d ago • [the Guardian](https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai)

---

**[Show HN: Smooth CLI – Token-efficient browser for AI agents](https://news.ycombinator.com/item?id=46901233)**

Give your AI agent a browser that actually works

⬆️ 90 • 💬 66 • 1d ago • [docs.smooth.sh](https://docs.smooth.sh/cli/overview)

---

**[Sam Altman responds to Anthropic's "Ads are coming to AI. But not to Claude" ads](https://news.ycombinator.com/item?id=46894151)**

⬆️ 88 • 💬 107 • 2d ago • [X (formerly Twitter)](https://twitter.com/sama/status/2019139174339928189)

---

**[Amazon plunge continues $1T wipeout as AI bubble fears ignite sell-off](https://news.ycombinator.com/item?id=46913302)**

Fears over AI spending have sparked a sell-off among tech stocks.

⬆️ 88 • 💬 84 • 21h ago • [CNBC](https://www.cnbc.com/2026/02/06/ai-sell-off-stocks-amazon-oracle.html)

---

**[AI needs to augment rather than replace humans or the workplace is doomed](https://news.ycombinator.com/item?id=46889282)**

Tech could lose its social acceptance unless it makes people’s lives better – and trade unions want an urgent conversation

⬆️ 60 • 💬 75 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/jan/25/ai-augment-rather-than-replace-workplace-doomed)

---

---

## YouTube Videos: "ai"

**[Trump Posts Shocking AI Video Showing the Obamas as Apes](https://www.youtube.com/watch?v=V86R2ZJPXzI)**

The White House deleted a video posted on President Trump's Truth Social that included a clip depicting former President Barack ...

📺 New York Post

👁️ 27K • 👍 247 • 💬 521 • ⏱️ 2:07 • 14h ago

---

**[Stop Using Restricted AI. Build This Instead.](https://www.youtube.com/watch?v=TmyULcNrD-I)**

In this video, I show you how to take full control of your local AI by building Custom Modelfiles in Ollama. We are moving beyond ...

📺 Cyb3rMaddy

👁️ 11K • 👍 931 • 💬 96 • ⏱️ 6:51 • 19h ago

---

**[🚨ALARMING! An AI Just Wiped Out $285B From The Financial Markets…🔥](https://www.youtube.com/watch?v=lRwduk14uHY)**

1. Get 90% OFF A Course Today: https://www.neilmccoyward.com/courses 2. My Investment Portfolio Join THOUSANDS of ...

📺 Neil McCoy-Ward

👁️ 61K • 👍 5K • 💬 506 • ⏱️ 19:58 • 20h ago

---

**[First Biomimetic AI Robot From China Looks Shockingly Human](https://www.youtube.com/watch?v=B61etYSvMNI)**

Humanoid robots just entered a new phase of realism. In Shanghai, DroidUp revealed Moya, the world's first fully biomimetic ...

📺 AI Revolution

👁️ 164K • 👍 4K • 💬 687 • ⏱️ 13:31 • 2d ago

---

**[The White Collar AI APOCALYPSE Is HERE](https://www.youtube.com/watch?v=ur295T83Wg4)**

Krystal and Saagar discuss tech stocks tumbling amid emerging new fears of job loss and AI. Sign up for a PREMIUM Breaking ...

📺 Breaking Points

👁️ 339K • 👍 9K • 💬 2K • ⏱️ 24:33 • 1d ago

---

**[Is Moltbook PROOF that AI agents are PLOTTING against us?!](https://www.youtube.com/watch?v=WzWBcZd_59E)**

Moltbook, a social network for AI agents, has gone viral over the past week. But is it proof that AI agents are becoming conscious, ...

📺 Glenn Beck

👁️ 15K • 👍 690 • 💬 137 • ⏱️ 13:28 • 13h ago

---

**[Nvidia CEO Jensen Huang: AI is going to fundamentally change how we compute everything](https://www.youtube.com/watch?v=P9dX_ek_6yY)**

Jensen Huang, NVIDIA CEO, joins CNBC's "Halftime Report to discuss the power of Artificial Intelligence and where he sees the ...

📺 CNBC Television

👁️ 103K • 👍 1K • 💬 399 • ⏱️ 8:35 • 16h ago

---

**[I&#39;m Buying This AI Stock As The Market Crashes (Here&#39;s Why)](https://www.youtube.com/watch?v=-zOE636nDpE)**

Protect your privacy and get 20% off DeleteMe at https://joindeleteme.com/SYMBOL20 AI stocks are crashing but #palantir ( #pltr ...

📺 Ticker Symbol: YOU

👁️ 77K • 👍 4K • 💬 375 • ⏱️ 16:57 • 1d ago

---

**[AI shakes software sector](https://www.youtube.com/watch?v=UosN6a2Wo6A)**

CNBC's Deirdre Bosa reports on news regarding the software sector. For access to live and exclusive video from CNBC subscribe ...

📺 CNBC Television

👁️ 106K • 👍 1K • 💬 422 • ⏱️ 3:30 • 2d ago

---

**[A.I Humanoid Fulfills End Times Prophecy And It&#39;s Disturbing](https://www.youtube.com/watch?v=KmxZcqhvvgg)**

Is the rise of AI humanoids the beginning of the end? In this video, we analyze a shocking new clip where an advanced AI ...

📺 Elijah Zielke

👁️ 3K • 👍 141 • 💬 39 • ⏱️ 12:26 • 16h ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling at table recognition, formula extraction, and information extraction across diverse layouts. It offers state-of-the-art performance with efficient inference, supporting deployment via vLLM, SGLang, and Ollama for real-world business applications.

`image-to-text`

⬇️ 204,109 • ❤️ 751 • 4d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is an 80B parameter (3B active) LLM optimized for coding agents, featuring advanced agentic capabilities like long-horizon reasoning and tool usage. It boasts a 256k context length for seamless IDE integration and efficient local development.

`text-generation` `79.7B`

⬇️ 53,491 • ❤️ 554 • 3d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. Its key capabilities include generating code from visual inputs and orchestrating an agent swarm for complex task decomposition and parallel execution.

`image-text-to-text` `170.7B`

⬇️ 335,220 • ❤️ 1,803 • 2d ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient, open-source MoE foundation model (11B active params, 196B total) excelling in deep reasoning and agentic tasks with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`text-generation` `199.4B`

⬇️ 11,980 • ❤️ 500 • 6h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles, trained on millions of anime and artistic images. It is designed for generating illustrations and artistic images, with primary use cases in ComfyUI workflows for anime concepts and characters.

⬇️ 60,581 • ❤️ 485 • 6d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and full-duplex live streaming, rivaling proprietary models like GPT-4o and Gemini 2.5 Flash. It offers advanced OCR, bilingual real-time conversation with voice cloning, and proactive omnimodal interaction for fluid, real-time experiences.

`any-to-any` `9.4B`

⬇️ 5,568 • ❤️ 562 • 19h ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio music generation model capable of producing commercial-ready music with precise stylistic control and editing features. It utilizes a hybrid LM-DiT architecture trained on licensed and royalty-free data, offering extreme speed and low VRAM requirements for consumer hardware, making it ideal for music artists and content creators.

`text-to-audio`

⬇️ 19,901 • ❤️ 419 • 4d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a 4B-parameter, multilingual speech-to-text model offering near-offline accuracy with <500ms latency. It features a streaming architecture for real-time applications like voice assistants and live subtitling, optimized for on-device deployment.

⬇️ 2,093 • ❤️ 353 • 2d ago

---

**[Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF)**

*Unsloth AI*

Qwen3-Coder-Next is an 80B parameter LLM optimized for coding agents, featuring 3B activated parameters, advanced agentic capabilities for long-horizon reasoning and tool usage, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 166,132 • ❤️ 204 • 2d ago

---

**[Intern-S1-Pro](https://huggingface.co/internlm/Intern-S1-Pro)**

*Intern Large Models*

Intern-S1-Pro is a trillion-scale MoE multimodal scientific reasoning model, excelling in AI4Science domains (chemistry, materials, life-science, earth) with strong general multimodal and text capabilities, supporting long, heterogeneous time-series data.

`image-text-to-text`

⬇️ 7,351 • ❤️ 185 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 133 • 💬 12 • ⭐ 2,198 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 133 • 💬 6 • ⭐ 14,194 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 4 • 💬 0 • ⭐ 30,435 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,435 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 2 • 💬 0 • ⭐ 30,444 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 117 • 💬 2 • ⭐ 2,616 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 60 • 💬 1 • ⭐ 7,034 • 16d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 138 • 💬 19 • ⭐ 52,320 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 6 • 💬 0 • ⭐ 27,974 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model](https://huggingface.co/papers/2510.14528)**

*Cheng Cui, Ting Sun, Suyin Liang et al. (18 authors)*

🏢 PaddlePaddle

PaddleOCR-VL, a vision-language model combining NaViT-style dynamic resolution and ERNIE, achieves state-of-the-art performance in document parsing and element recognition with high efficiency.

▲ 113 • 💬 7 • ⭐ 70,330 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.14528) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 13.0k • 🔱 747 • 16h ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 10.1k • 🔱 537 • 11h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 9.8k • 🔱 10.2k • 5h ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 700+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 7.7k • 🔱 1.6k • 5h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 6.3k • 🔱 721 • 3d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 4.4k • 🔱 349 • 2d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.2k • 🔱 353 • 15d ago

---

**[DevAgentForge/Claude-Cowork](https://github.com/DevAgentForge/Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.8k • 🔱 377 • 15d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.7k • 🔱 258 • 19d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 2.3k • 🔱 102 • 4d ago

---

---

*Generated by PeekDeck - A glance is all you need*

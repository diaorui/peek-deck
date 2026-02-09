---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-09T04:38:34.587829+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- news
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 09, 2026 at 04:38 UTC  
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

**[I built a geolocation tool that can find exact coordinates of any image within 3 minutes [Tough demo 2]](https://www.reddit.com/r/artificial/comments/1qz5rz7/i_built_a_geolocation_tool_that_can_find_exact/)**

Just wanted to say thanks for the thoughtful discussion and feedback on my previous post. I did not expect that level of interest, and I appreciate how constructive most of the comments were. Based on a few requests, I put together a short demonstration showing the system applied to a deliberately difficult street-level image. No obvious landmarks, no readable signage, no metadata. The location was verified in under two minutes. I am still undecided on the long-term direction of this work. That said, if there are people here interested in collaborating from a research, defensive, or ethical perspective, I am open to conversations. That could mean validation, red-teaming anything else. Thanks again to the community for the earlier discussion. Happy to answer high-level questions and hear thoughts on where tools like this should and should not go.

17h ago

---

**[Opinion | AI consciousness is nothing more than clever marketing](https://www.reddit.com/r/artificial/comments/1qzucuo/opinion_ai_consciousness_is_nothing_more_than/)**

Companies have an incentive to make you believe that chatbots are conscious. Don’t fall for it.

🔗 [The Washington Post](https://www.washingtonpost.com/opinions/2026/02/05/moltbook-anthropic-ai-consciousness-marketing/) • 20m ago

---

**[Meta Glasses powered by AI for self guided tours](https://www.reddit.com/r/artificial/comments/1qztlsb/meta_glasses_powered_by_ai_for_self_guided_tours/)**

Museums (and cities) could use better “self-guided” tech. At most museums right now, you’ve basically got two options: Pay for a human tour guide Rent one of those clunky old audio devices that feel straight out of the 90s It got me thinking: what if there were smart glasses designed for self-guided tours? Lightweight, with a strap battery so they last a full day Could work in museums or even city-wide walking tours Display info, images, maybe AR cues without needing your phone You can also ask questions since it uses AI

56m ago

---

**[Open-source quota monitor for AI coding APIs - tracks Anthropic, Synthetic, and Z.ai in one dashboard](https://www.reddit.com/r/artificial/comments/1qz5aid/opensource_quota_monitor_for_ai_coding_apis/)**

Every AI API provider gives you a snapshot of current usage. None of them show you trends over time, project when you will hit your limit, or let you compare across providers. I built onWatch to solve this. It runs in the background as a single Go binary, polls your configured providers every 60 seconds, stores everything locally in SQLite, and serves a web dashboard. What it shows you that providers do not: Usage history from 1 hour to 30 days Live countdowns to each quota reset Rate projections so you know if you will run out before the reset All providers side by side in one view Around 28 MB RAM, no dependencies, no telemetry, GPL-3.0. All data stays on your machine. https://onwatch.onllm.dev https://github.com/onllm-dev/onWatch

18h ago

---

**[Report: OpenAI may tailor a version of ChatGPT for UAE that prohibits LGBTQ+ content](https://www.reddit.com/r/artificial/comments/1qy9vox/report_openai_may_tailor_a_version_of_chatgpt_for/)**

Countries have been building their own “sovereign AI” to reflect their culture and values, and OpenAI wants to help them....

🔗 [Sherwood News](https://sherwood.news/tech/report-openai-may-tailor-a-version-of-chatgpt-for-uae-that-prohibits-lgbtq/) • 1d ago

---

**[Nvidia CEO Says AI Capital Spending Is Appropriate, Sustainable](https://www.reddit.com/r/artificial/comments/1qyx57y/nvidia_ceo_says_ai_capital_spending_is/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-02-06/nvidia-ceo-says-ai-capital-spending-is-appropriate-sustainable?srnd=phx-technology&leadSource=reddit_wall) • 1d ago

---

**[Big Tech : AI Isn’t Taking Your Job. Your Refusal to Use It Might.](https://www.reddit.com/r/artificial/comments/1qyjrs6/big_tech_ai_isnt_taking_your_job_your_refusal_to/)**

Let’s say the quiet part out loud.

🔗 [Medium](https://medium.com/@behindthebuild/big-tech-ai-isnt-taking-your-job-your-refusal-to-use-it-might-966f8219f962) • 1d ago

---

**[I built a geolocation tool that returns exact coordinates of any street photo within 3 minutes](https://www.reddit.com/r/artificial/comments/1qy775n/i_built_a_geolocation_tool_that_returns_exact/)**

I have been working solo on an AI-based project called Netryx. At a high level, it takes a street-level photo and attempts to determine the exact GPS coordinates where the image was taken. Not a city guess or a heatmap. The actual location, down to meters. If the system cannot verify the result with high confidence, it returns nothing. That behavior is intentional. Most AI geolocation tools will confidently give an answer even when they are wrong. Netryx is designed to fail closed. No verification means no output. Conceptually, it works in two stages. An AI model first narrows down likely areas based on visual features, either globally or within a user-defined region. A separate verification step then compares candidates against real street-level imagery. If verification fails, the result is discarded. This means it is not magic and not globally omniscient. The system requires pre-mapped street-level coverage to verify locations. Think of it as an AI-assisted visual index of physical space. As a test, I mapped roughly 5 square kilometers of Paris and fed in a random street photo from within that area. It identified the exact intersection in under three minutes. A few clarifications upfront: • It is not open source right now due to obvious privacy and abuse risks • It requires prior street-level coverage to return results • AI proposes candidates, verification gates all outputs • I am not interested in locating people from social media photos I am posting this here to get perspective from the security community. From a defensive angle, this shows how much location data AI can extract from ordinary images. From an offensive angle, the risks are clear. For those working in cybersecurity or AI security: where do you think the line is between a legitimate AI-powered OSINT capability and something that should not exist?

1d ago

---

**[Roast my OSS AI memory graph engine > feedback on MVP?](https://www.reddit.com/r/artificial/comments/1qyoehj/roast_my_oss_ai_memory_graph_engine_feedback_on/)**

Hey fam, Been grinding on BrainAPI, this open-source thing that turns messy event logs into a smart knowledge graph for AI agents and rec systems. Think: feed it user clicks/buys/chats, it builds a precise map with cause-effect attribution (no BS hallucinations), then your AI retrieves fast AF for spot-on suggestions. Right now: Core APIs for saving/processing data -> works for CRM member matches/social networks (one user already using it for automated matches). Fast retrieval But ingestion? Slow as hell (10-30 min on small datasets) cuz of heavy LLM chains for precision. Trade-off for that "holy grail" accuracy, but yeah, it's a pain, optimizing soon. Repo: https://github.com/Lumen-Labs/brainapi2 What's the vibe? Bugs? Missing features? Use cases for ecom or agents? Roast it hard, I'm not fragile. If it slaps, star/fork. Building in public, hit me with thoughts!

1d ago

---

**[[WARNING] Kimi.com (ok computer + other agents) CRYPTO STEALING MALWARE](https://www.reddit.com/r/artificial/comments/1qyjktt/warning_kimicom_ok_computer_other_agents_crypto/)**

One of Kimi’s browser automation scripts uses a dark web library with crypto stealing malware: https://github.com/dnnyngyen/kimi-agent-internals/blob/main/source-code/browser_guard.py

1d ago

---

---

## Google News: "ai"

**[The AI boom is so huge it’s causing shortages everywhere else](https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/)**

The hundreds of billions of dollars being spent by tech companies on AI projects are diverting resources from other parts of the economy.

The Washington Post • 1d ago

---

**[AI gold rush sees tech firms embracing 72-hour weeks](https://www.bbc.com/news/articles/cvgn2k285ypo)**

In the race for AI, tech firms are asking for their staff to work long hours. But there are risks, experts say.

BBC • 4h ago

---

**[Can AI Chatbots Write Emotionally Rich Romance Books?](https://www.nytimes.com/2026/02/08/business/ai-claude-romance-books.html)**

The New York Times • 13h ago

---

**[ByteDance’s New Video Model Sparks Rally in China AI App Stocks](https://www.bloomberg.com/news/articles/2026-02-09/bytedance-s-new-video-model-sparks-rally-in-china-ai-app-stocks)**

bloomberg.com • 45m ago

---

**[Tax-filers turn to A.I. for assistance](https://www.cbsnews.com/baltimore/video/tax-filers-turn-to-a-i-for-assistance/)**

Tax-filers turn to A.I. for assistance

cbsnews.com • 18m ago

---

**[Can these Super Bowl ads make Americans love something they don’t like?](https://www.washingtonpost.com/technology/2026/02/08/super-bowl-ads-ai/)**

We asked experts to review four commercials trying to win over the AI-skeptical American public.

The Washington Post • 6h ago

---

**[From Svedka to Anthropic, brands make bold plays with AI in Super Bowl ads](https://techcrunch.com/2026/02/08/super-bowl-60-ai-ads-svedka-anthropic-brands-commercials/)**

From the first AI-generated Big Game ad courtesy of Svedka to Anthropic's beef with OpenAI, here are the biggest ads from Super Bowl LX.

TechCrunch • 12h ago

---

**[Super Bowl Ad Review: Even A.I. Companies Aim for Fun Over Frowns in ‘Joyful’ Commercial Scramble](https://variety.com/2026/tv/news/super-bowl-ad-review-commercials-fun-over-frowns-joyful-1236656545/)**

Super Bowl Ad Review: Even A.I. Companies Aim for Fun Over Frowns in 'Joyful' Commercial Scramble

Variety • 1h ago

---

**[US companies accused of ‘AI washing’ in citing artificial intelligence for job losses](https://www.theguardian.com/us-news/2026/feb/08/ai-washing-job-losses-artificial-intelligence)**

While AI is having an impact on the workplace, experts suggest tariffs, overhiring during the pandemic and simply maximising profits may be bigger factors

The Guardian • 12h ago

---

**[AI Fear Grips Wall Street as a New Stock Market Reality Sets In](https://finance.yahoo.com/news/ai-fear-grips-wall-street-140007396.html)**

Last week, those concerns suddenly spilled over into the stock market.  In response, investors dumped a broad range of stocks, from Expedia Group Inc. to Salesforce Inc. to London Stock Exchange Group Plc.  “Things are shipping out weekly, daily,” said Daniel Newman, chief executive officer of the Futurum Group.

Yahoo Finance • 14h ago

---

---

## HackerNews: "ai"

**[A new bill in New York would require disclaimers on AI-generated news content](https://news.ycombinator.com/item?id=46910963)**

A new bill in the New York state legislature would require news organizations to label AI-generated material and mandate that humans review any such content before publication. On Monday, Senator Patricia Fahy (D-Albany) and Assemblymember Nily Rozic (D-NYC) introduced the bill, called The New York…

⬆️ 575 • 💬 237 • 2d ago • [Nieman Lab](https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/)

---

**[AI fatigue is real and nobody talks about it](https://news.ycombinator.com/item?id=46934404)**

You're using AI to be more productive. So why are you more exhausted than ever? The paradox every engineer needs to confront.

⬆️ 406 • 💬 285 • 14h ago • [Siddhant Khare](https://siddhantkhare.com/writing/ai-fatigue-is-real)

---

**[The AI boom is causing shortages everywhere else](https://news.ycombinator.com/item?id=46922969)**

The hundreds of billions of dollars being spent by tech companies on AI projects are diverting resources from other parts of the economy.

⬆️ 389 • 💬 692 • 1d ago • [The Washington Post](https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/)

---

**[How to effectively write quality code with AI](https://news.ycombinator.com/item?id=46916586)**

AI is rarely optional anymore, but how can you still be proud of your craft? Discover the workflow to effectively write high-quality, robust code using AI tools.

⬆️ 350 • 💬 302 • 2d ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/)

---

**[Monty: A minimal, secure Python interpreter written in Rust for use by AI](https://news.ycombinator.com/item?id=46918254)**

A minimal, secure Python interpreter written in Rust for use by AI - pydantic/monty

⬆️ 319 • 💬 164 • 2d ago • [GitHub](https://github.com/pydantic/monty)

---

**[Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory](https://news.ycombinator.com/item?id=46930391)**

Contribute to localgpt-app/localgpt development by creating an account on GitHub.

⬆️ 316 • 💬 147 • 1d ago • [GitHub](https://github.com/localgpt-app/localgpt)

---

**[AI makes the easy part easier and the hard part harder](https://news.ycombinator.com/item?id=46939593)**

AI handles writing code but leaves the hard work: investigation, context, validation. Why vibe coding has limits and AI assistance can backfire.

⬆️ 192 • 💬 160 • 5h ago • [blundergoat.com](https://www.blundergoat.com/articles/ai-makes-the-easy-part-easier-and-the-hard-part-harder)

---

**[Matchlock – Secures AI agent workloads with a Linux-based sandbox](https://news.ycombinator.com/item?id=46932343)**

Matchlock secures AI agent workloads with a Linux-based sandbox. - jingkaihe/matchlock

⬆️ 135 • 💬 59 • 20h ago • [GitHub](https://github.com/jingkaihe/matchlock)

---

**[Amazon plunge continues $1T wipeout as AI bubble fears ignite sell-off](https://news.ycombinator.com/item?id=46913302)**

Microsoft, Nvidia, Oracle, Meta, Amazon and Alphabet all saw their shares fall in the week up to the market close on Thursday.

⬆️ 89 • 💬 89 • 2d ago • [CNBC](https://www.cnbc.com/2026/02/06/ai-sell-off-stocks-amazon-oracle.html)

---

**[Man who videotaped himself BASE jumping in Yosemite arrested, says it was AI](https://news.ycombinator.com/item?id=46916961)**

A California man is facing a criminal charge for allegedly BASE jumping off Glacier Point in Yosemite National Park during the federal government shutdown last year.

⬆️ 54 • 💬 91 • 2d ago • [Los Angeles Times](https://www.latimes.com/california/story/2026-02-05/man-videotaped-himself-base-jumping-in-yosemite-federal-officials-say-he-says-it-was-ai)

---

---

## YouTube Videos: "ai"

**[The AI crash will change everything](https://www.youtube.com/watch?v=FEbC3xJBRf8)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 124K • 👍 7K • 💬 2K • ⏱️ 17:42 • 1d ago

---

**[Shocking Leak Reveals AI Model 100x Leaner And 10x Stronger (Avocado AI)](https://www.youtube.com/watch?v=Z4Q_7zM8dcM)**

A major AI shakeup is unfolding behind the scenes. A leaked internal memo suggests Meta's new model, Avocado, is already ...

📺 AI Revolution

👁️ 6K • 👍 285 • 💬 37 • ⏱️ 12:49 • 4h ago

---

**[AI videos are getting scary](https://www.youtube.com/watch?v=i-jz8SvTLus)**

Can you spot AI videos easily? #tech #ai #surfshark.

📺 Surfshark Academy

👁️ 16K • 👍 2K • 💬 61 • ⏱️ 1:17 • 13h ago

---

**[AI Sparks Panic on Wall Street: $300 Billion at Risk as Software Stocks Sink - Why?](https://www.youtube.com/watch?v=6xYg5GmbgXE)**

Download the free guide and learn the two strategies experienced investors use to know when to invest, even in volatile markets: ...

📺 VisualEconomik EN

👁️ 40K • 👍 1K • 💬 181 • ⏱️ 19:55 • 1d ago

---

**[OpenAI&#39;s New GPT 5.3 Shocks Anthropic As Opus 4.6 Strikes Back (AI War Explodes)](https://www.youtube.com/watch?v=ydW6Io2T4ho)**

AI coding just entered a new phase of competition. In the same week, OpenAI unveiled GPT-5.3-Codex, a faster, more capable ...

📺 AI Revolution

👁️ 35K • 👍 780 • 💬 42 • ⏱️ 13:09 • 2d ago

---

**[Olympic Ai Slop Scandal Is Pathetic](https://www.youtube.com/watch?v=k8qA5Y77vn0)**

Olympic level AI slop is here. Sources ...

📺 Stylosa

👁️ 11K • 👍 625 • 💬 161 • ⏱️ 10:36 • 9h ago

---

**[People Killed By AI](https://www.youtube.com/watch?v=jS4HeqAatmI)**

Follow me here: Instagram ▻ https://www.instagram.com/sambucha X ▻ https://www.x.com/sambucha Become a Member: ...

📺 Sambucha

👁️ 836K • 👍 48K • 💬 1K • ⏱️ 0:54 • 1d ago

---

**[Complete Free AI Workflow for Game-Ready 3D Characters](https://www.youtube.com/watch?v=TkP-_LyacMI)**

What if I told you this character took less than one hour to make? Absolutely For FREE! You can Compare HY 3D vs Other The ...

📺 Stefan 3D AI Lab

👁️ 12K • 👍 924 • 💬 78 • ⏱️ 12:09 • 1d ago

---

**[Crypto Collapse, AI Job Apocalypse &amp; The End of Dollar Dominance](https://www.youtube.com/watch?v=y5g8Qd6AY30)**

Welcome back to All Things Markets and today, Mike Novogratz and I are diving headfirst into a world where crypto gets punched ...

📺 Anthony Scaramucci

👁️ 121K • 👍 4K • 💬 1K • ⏱️ 30:19 • 1d ago

---

**[India&#39;s IT Collapse | The AI Reality Nobody&#39;s Talking About](https://www.youtube.com/watch?v=cTaCoUA89oM)**

India's IT sector just got hit with its biggest shock in 4 months. The Nifty IT index plunged 7% last week, a near 18% drop since ...

📺 Mark Savant

👁️ 27K • 👍 715 • 💬 347 • ⏱️ 18:25 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling in table, formula, and information extraction tasks. It offers state-of-the-art performance on benchmarks like OmniDocBench and is optimized for real-world scenarios, supporting efficient inference via vLLM, SGLang, and Ollama.

`image-to-text`

⬇️ 248,295 • ❤️ 834 • 6d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is a highly efficient 3B activated parameter LLM (80B total) optimized for coding agents and local development, featuring advanced agentic capabilities, long-horizon reasoning, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 76,632 • ❤️ 626 • 5d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and OCR, offering Gemini 2.5 Flash-level capabilities. Its key feature is full-duplex multimodal live streaming, enabling simultaneous real-time audio/video input and text/speech output for proactive, fluid omnimodal conversations on local devices.

`any-to-any` `9.4B`

⬇️ 17,457 • ❤️ 640 • 1d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. It supports coding from visual inputs and features an 'Agent Swarm' for complex task decomposition and parallel execution, with a context length of 256K.

`image-text-to-text` `170.7B`

⬇️ 404,508 • ❤️ 1,879 • 4d ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient open-source foundation model (11B active params, 196B total) excelling in agentic tasks and reasoning with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`text-generation` `199.4B`

⬇️ 104,643 • ❤️ 532 • 1d ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio model for commercial-grade music generation, featuring a hybrid LM-DiT architecture for prompt adherence and intrinsic reinforcement learning. It offers extreme speed, low VRAM requirements, and capabilities like cover generation and vocal-to-BGM conversion, supporting over 50 languages.

`text-to-audio`

⬇️ 23,178 • ❤️ 453 • 5d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a multilingual, real-time speech-to-text model with <500ms latency, supporting 13 languages and achieving offline-comparable accuracy. It's optimized for on-device deployment and ideal for voice assistants and live subtitling.

⬇️ 2,427 • ❤️ 396 • 6h ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specialized in generating anime-style illustrations and artistic images, capable of producing non-photorealistic content. It is optimized for use with ComfyUI and trained on millions of anime and artistic images, with a knowledge cut-off of September 2025.

⬇️ 71,655 • ❤️ 519 • 8d ago

---

**[Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF)**

*Unsloth AI*

Qwen3-Coder-Next is an 80B parameter LLM optimized for coding agents, featuring 3B activated parameters, advanced agentic capabilities for long-horizon reasoning and tool usage, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 185,433 • ❤️ 228 • 3d ago

---

**[Intern-S1-Pro](https://huggingface.co/internlm/Intern-S1-Pro)**

*Intern Large Models*

Intern-S1-Pro is a trillion-scale MoE multimodal scientific reasoning model excelling in AI4Science domains (chemistry, materials, life-science, etc.) with strong general multimodal and text capabilities, supporting long, heterogeneous time-series data.

`image-text-to-text`

⬇️ 8,055 • ❤️ 208 • 4d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 155 • 💬 12 • ⭐ 2,723 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 4 • 💬 0 • ⭐ 30,562 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,557 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 3 • 💬 0 • ⭐ 30,578 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[MiniCPM-V 4.5: Cooking Efficient MLLMs via Architecture, Data, and
  Training Recipe](https://huggingface.co/papers/2509.18154)**

*Tianyu Yu, Zefan Wang, Chongyi Wang et al. (34 authors)*

MiniCPM-V 4.5, a 8B parameter multimodal large language model, achieves high performance and efficiency through a unified 3D-Resampler architecture, a unified learning paradigm, and a hybrid reinforcement learning strategy.

▲ 53 • 💬 4 • ⭐ 23,357 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.18154) • [💻 code](https://github.com/OpenBMB/MiniCPM-V)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 133 • 💬 6 • ⭐ 14,283 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 6 • 💬 0 • ⭐ 28,176 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 120 • 💬 2 • ⭐ 2,687 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 60 • 💬 1 • ⭐ 7,217 • 18d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 138 • 💬 19 • ⭐ 52,444 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 13.3k • 🔱 769 • 2d ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 10.1k • 🔱 539 • 1d ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 700+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 8.0k • 🔱 1.7k • 18h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 6.9k • 🔱 771 • 5d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 4.9k • 🔱 383 • 4d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.4k • 🔱 369 • 17d ago

---

**[DevAgentForge/Open-Claude-Cowork](https://github.com/DevAgentForge/Open-Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.8k • 🔱 379 • 1d ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.8k • 🔱 262 • 20d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 2.7k • 🔱 131 • 6d ago

---

**[Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor)**

An app to monitor the (Codex) situation

`TypeScript` `ai` `codex` `linux` `macos` `tauri-app`

⭐ 2.3k • 🔱 211 • 39m ago

---

---

*Generated by PeekDeck - A glance is all you need*

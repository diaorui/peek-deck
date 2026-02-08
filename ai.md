---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-08T13:46:18.857634+00:00'
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

**Last Updated:** February 08, 2026 at 13:46 UTC  
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

3h ago

---

**[Report: OpenAI may tailor a version of ChatGPT for UAE that prohibits LGBTQ+ content](https://www.reddit.com/r/artificial/comments/1qy9vox/report_openai_may_tailor_a_version_of_chatgpt_for/)**

Countries have been building their own “sovereign AI” to reflect their culture and values, and OpenAI wants to help them....

🔗 [Sherwood News](https://sherwood.news/tech/report-openai-may-tailor-a-version-of-chatgpt-for-uae-that-prohibits-lgbtq/) • 1d ago

---

**[Open-source quota monitor for AI coding APIs - tracks Anthropic, Synthetic, and Z.ai in one dashboard](https://www.reddit.com/r/artificial/comments/1qz5aid/opensource_quota_monitor_for_ai_coding_apis/)**

Every AI API provider gives you a snapshot of current usage. None of them show you trends over time, project when you will hit your limit, or let you compare across providers. I built onWatch to solve this. It runs in the background as a single Go binary, polls your configured providers every 60 seconds, stores everything locally in SQLite, and serves a web dashboard. What it shows you that providers do not: Usage history from 1 hour to 30 days Live countdowns to each quota reset Rate projections so you know if you will run out before the reset All providers side by side in one view Around 28 MB RAM, no dependencies, no telemetry, GPL-3.0. All data stays on your machine. https://onwatch.onllm.dev https://github.com/onllm-dev/onWatch

3h ago

---

**[Nvidia CEO Says AI Capital Spending Is Appropriate, Sustainable](https://www.reddit.com/r/artificial/comments/1qyx57y/nvidia_ceo_says_ai_capital_spending_is/)**

🔗 [bloomberg.com](https://www.bloomberg.com/news/articles/2026-02-06/nvidia-ceo-says-ai-capital-spending-is-appropriate-sustainable?srnd=phx-technology&leadSource=reddit_wall) • 11h ago

---

**[I built a geolocation tool that returns exact coordinates of any street photo within 3 minutes](https://www.reddit.com/r/artificial/comments/1qy775n/i_built_a_geolocation_tool_that_returns_exact/)**

I have been working solo on an AI-based project called Netryx. At a high level, it takes a street-level photo and attempts to determine the exact GPS coordinates where the image was taken. Not a city guess or a heatmap. The actual location, down to meters. If the system cannot verify the result with high confidence, it returns nothing. That behavior is intentional. Most AI geolocation tools will confidently give an answer even when they are wrong. Netryx is designed to fail closed. No verification means no output. Conceptually, it works in two stages. An AI model first narrows down likely areas based on visual features, either globally or within a user-defined region. A separate verification step then compares candidates against real street-level imagery. If verification fails, the result is discarded. This means it is not magic and not globally omniscient. The system requires pre-mapped street-level coverage to verify locations. Think of it as an AI-assisted visual index of physical space. As a test, I mapped roughly 5 square kilometers of Paris and fed in a random street photo from within that area. It identified the exact intersection in under three minutes. A few clarifications upfront: • It is not open source right now due to obvious privacy and abuse risks • It requires prior street-level coverage to return results • AI proposes candidates, verification gates all outputs • I am not interested in locating people from social media photos I am posting this here to get perspective from the security community. From a defensive angle, this shows how much location data AI can extract from ordinary images. From an offensive angle, the risks are clear. For those working in cybersecurity or AI security: where do you think the line is between a legitimate AI-powered OSINT capability and something that should not exist?

1d ago

---

**[Big Tech : AI Isn’t Taking Your Job. Your Refusal to Use It Might.](https://www.reddit.com/r/artificial/comments/1qyjrs6/big_tech_ai_isnt_taking_your_job_your_refusal_to/)**

Let’s say the quiet part out loud.

🔗 [Medium](https://medium.com/@behindthebuild/big-tech-ai-isnt-taking-your-job-your-refusal-to-use-it-might-966f8219f962) • 20h ago

---

**[Roast my OSS AI memory graph engine > feedback on MVP?](https://www.reddit.com/r/artificial/comments/1qyoehj/roast_my_oss_ai_memory_graph_engine_feedback_on/)**

Hey fam, Been grinding on BrainAPI, this open-source thing that turns messy event logs into a smart knowledge graph for AI agents and rec systems. Think: feed it user clicks/buys/chats, it builds a precise map with cause-effect attribution (no BS hallucinations), then your AI retrieves fast AF for spot-on suggestions. Right now: Core APIs for saving/processing data -> works for CRM member matches/social networks (one user already using it for automated matches). Fast retrieval But ingestion? Slow as hell (10-30 min on small datasets) cuz of heavy LLM chains for precision. Trade-off for that "holy grail" accuracy, but yeah, it's a pain, optimizing soon. Repo: https://github.com/Lumen-Labs/brainapi2 What's the vibe? Bugs? Missing features? Use cases for ecom or agents? Roast it hard, I'm not fragile. If it slaps, star/fork. Building in public, hit me with thoughts!

17h ago

---

**[[WARNING] Kimi.com (ok computer + other agents) CRYPTO STEALING MALWARE](https://www.reddit.com/r/artificial/comments/1qyjktt/warning_kimicom_ok_computer_other_agents_crypto/)**

One of Kimi’s browser automation scripts uses a dark web library with crypto stealing malware: https://github.com/dnnyngyen/kimi-agent-internals/blob/main/source-code/browser_guard.py

20h ago

---

**[Goldman Sachs taps Anthropic’s Claude to automate accounting, compliance roles](https://www.reddit.com/r/artificial/comments/1qxv9jg/goldman_sachs_taps_anthropics_claude_to_automate/)**

Goldman Sachs is building AI agents with Anthropic’s Claude to automate trade accounting and client onboarding, aiming to speed work and boost efficiency.

🔗 [CNBC](https://www.cnbc.com/2026/02/06/anthropic-goldman-sachs-ai-model-accounting.html) • 1d ago

---

**[AI model can read and diagnose a brain MRI in seconds](https://www.reddit.com/r/artificial/comments/1qy24st/ai_model_can_read_and_diagnose_a_brain_mri_in/)**

An AI-powered model developed at University of Michigan can read a brain MRI and diagnose a person in seconds, a study suggests.&nbsp;It detected neurological conditions with up to 97.5% accuracy and predicted how urgently a patient required treatment. The technology&nbsp;could transform neuroimaging at health systems across the United States.

🔗 [EurekAlert!](https://www.eurekalert.org/news-releases/1115393) • 1d ago

---

---

## Google News: "ai"

**[The AI boom is so huge it’s causing shortages everywhere else](https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/)**

The hundreds of billions of dollars being spent by tech companies on AI projects are diverting resources from other parts of the economy.

The Washington Post • 19h ago

---

**[What You’re Getting Wrong About China and AI](https://www.politico.com/news/magazine/2026/02/07/china-usa-ai-race-interview-00769367)**

In a new interview, the journalist Yi-Ling Liu argues the AI arms race between the United States and China risks becoming a self-fulfilling prophecy.

Politico • 22h ago

---

**[Opinion | It’s the A.I. Economy, Stupid](https://www.nytimes.com/2026/02/08/opinion/ai-democrats-jobs-economy.html)**

The New York Times • 1h ago

---

**[The Best AI Notetakers to Record Your Meetings, Interviews, or Classes](https://www.wired.com/gallery/best-ai-notetakers/)**

A growing collection of pocket-sized gadgets lets you record your meetings and extract value from them. Here are our favorites.

WIRED • 1h ago

---

**[Economists reject Kevin Warsh’s claim that AI boom will enable rate cuts](https://www.ft.com/content/92717c0e-0e59-4d0c-a364-6ac003de4f8e)**

FT-Booth Survey shows scepticism of productivity gains forecast by Trump’s pick as next Fed chair

Financial Times • 2h ago

---

**[Moltbook was peak AI theater](https://www.technologyreview.com/2026/02/06/1132448/moltbook-was-peak-ai-theater/)**

The viral social network for bots reveals as much about our own current mania for AI as it does about the future of agents.

MIT Technology Review • 1d ago

---

**[Goldman Sachs taps Anthropic’s Claude to automate accounting, compliance roles](https://www.cnbc.com/2026/02/06/anthropic-goldman-sachs-ai-model-accounting.html)**

Goldman Sachs is building AI agents with Anthropic’s Claude to automate trade accounting and client onboarding, aiming to speed work and boost efficiency.

CNBC • 2d ago

---

**[I turned myself into an AI-generated deathbot - here's what I found](https://www.bbc.com/news/articles/c93wjywz5p5o)**

A Cardiff University researcher recreated her own voice using a deathbot - but found it strange.

BBC • 6h ago

---

**[AI can make anyone rich: Mark Cuban says it could turn ‘just one dude in a basement’ into a trillionaire](https://finance.yahoo.com/news/ai-anyone-rich-mark-cuban-152003409.html)**

The billionaire former "Shark Tank" star and Dallas Mavericks owner is a dedicated AI user.

Yahoo Finance • 22h ago

---

**[Why has Elon Musk merged his rocket company with his AI startup?](https://www.theguardian.com/technology/2026/feb/07/why-has-elon-musk-merged-his-rocket-company-with-his-ai-startup)**

SpaceX’s acquisition of xAI creates business worth $1.25tn but whether premise behind deal will work is questioned

The Guardian • 23h ago

---

---

## HackerNews: "ai"

**[My AI Adoption Journey](https://news.ycombinator.com/item?id=46903558)**

⬆️ 943 • 💬 396 • 2d ago • [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)

---

**[A new bill in New York would require disclaimers on AI-generated news content](https://news.ycombinator.com/item?id=46910963)**

A new bill in the New York state legislature would require news organizations to label AI-generated material and mandate that humans review any such content before publication. On Monday, Senator Patricia Fahy (D-Albany) and Assemblymember Nily Rozic (D-NYC) introduced the bill, called The New York…

⬆️ 570 • 💬 234 • 2d ago • [Nieman Lab](https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/)

---

**[The AI boom is causing shortages everywhere else](https://news.ycombinator.com/item?id=46922969)**

The hundreds of billions of dollars being spent by tech companies on AI projects are diverting resources from other parts of the economy.

⬆️ 365 • 💬 615 • 1d ago • [The Washington Post](https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/)

---

**[How to effectively write quality code with AI](https://news.ycombinator.com/item?id=46916586)**

AI is rarely optional anymore, but how can you still be proud of your craft? Discover the workflow to effectively write high-quality, robust code using AI tools.

⬆️ 343 • 💬 296 • 1d ago • [heidenstedt.org](https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/)

---

**[Monty: A minimal, secure Python interpreter written in Rust for use by AI](https://news.ycombinator.com/item?id=46918254)**

A minimal, secure Python interpreter written in Rust for use by AI - pydantic/monty

⬆️ 316 • 💬 161 • 1d ago • [GitHub](https://github.com/pydantic/monty)

---

**[Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory](https://news.ycombinator.com/item?id=46930391)**

Contribute to localgpt-app/localgpt development by creating an account on GitHub.

⬆️ 249 • 💬 125 • 12h ago • [GitHub](https://github.com/localgpt-app/localgpt)

---

**[India's female workers watching hours of abusive content to train AI](https://news.ycombinator.com/item?id=46906590)**

Women in rural communities describe trauma of moderating violent and pornographic content for global tech companies

⬆️ 128 • 💬 201 • 2d ago • [the Guardian](https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai)

---

**[Show HN: Smooth CLI – Token-efficient browser for AI agents](https://news.ycombinator.com/item?id=46901233)**

Give your AI agent a browser that actually works

⬆️ 101 • 💬 71 • 2d ago • [docs.smooth.sh](https://docs.smooth.sh/cli/overview)

---

**[Amazon plunge continues $1T wipeout as AI bubble fears ignite sell-off](https://news.ycombinator.com/item?id=46913302)**

Fears over AI spending have sparked a sell-off among tech stocks.

⬆️ 88 • 💬 88 • 1d ago • [CNBC](https://www.cnbc.com/2026/02/06/ai-sell-off-stocks-amazon-oracle.html)

---

**[(AI) Slop Terrifies Me](https://news.ycombinator.com/item?id=46933067)**

What if this is as good as software is ever going to be? What if AI stops getting better and what if people stop caring?

⬆️ 56 • 💬 30 • 3h ago • [ezhik.jp](https://ezhik.jp/ai-slop-terrifies-me/)

---

---

## YouTube Videos: "ai"

**[The AI crash will change everything](https://www.youtube.com/watch?v=FEbC3xJBRf8)**

Become a member! ✓ https://www.youtube.com/channel/UCahJ9IsvXnaQiuNyWQSkrkw/join ⭐ Support independent daily news ...

📺 Chris Norlund

👁️ 97K • 👍 6K • 💬 1K • ⏱️ 17:42 • 15h ago

---

**[🚨ALARMING! An AI Just Wiped Out $285B From The Financial Markets…🔥](https://www.youtube.com/watch?v=lRwduk14uHY)**

1. Get 90% OFF A Course Today: https://www.neilmccoyward.com/courses 2. My Investment Portfolio Join THOUSANDS of ...

📺 Neil McCoy-Ward

👁️ 70K • 👍 5K • 💬 572 • ⏱️ 19:58 • 1d ago

---

**[India&#39;s IT Collapse | The AI Reality Nobody&#39;s Talking About](https://www.youtube.com/watch?v=cTaCoUA89oM)**

India's IT sector just got hit with its biggest shock in 4 months. The Nifty IT index plunged 7% last week, a near 18% drop since ...

📺 Mark Savant

👁️ 15K • 👍 454 • 💬 202 • ⏱️ 18:25 • 16h ago

---

**[OpenAI&#39;s New GPT 5.3 Shocks Anthropic As Opus 4.6 Strikes Back (AI War Explodes)](https://www.youtube.com/watch?v=ydW6Io2T4ho)**

AI coding just entered a new phase of competition. In the same week, OpenAI unveiled GPT-5.3-Codex, a faster, more capable ...

📺 AI Revolution

👁️ 29K • 👍 705 • 💬 40 • ⏱️ 13:09 • 1d ago

---

**[Anthropic&#39;s New AI Just Changed Everything](https://www.youtube.com/watch?v=ZneWerxN-qU)**

Today I break down Claude Opus 4.6, Anthropic's most advanced AI model that handles complex coding, deep analysis, and ...

📺 Tech Unicorn

👁️ 3K • 👍 63 • 💬 14 • ⏱️ 11:40 • 1d ago

---

**[The White Collar AI APOCALYPSE Is HERE](https://www.youtube.com/watch?v=ur295T83Wg4)**

Krystal and Saagar discuss tech stocks tumbling amid emerging new fears of job loss and AI. Sign up for a PREMIUM Breaking ...

📺 Breaking Points

👁️ 365K • 👍 10K • 💬 2K • ⏱️ 24:33 • 2d ago

---

**[This AI Feature Replaces Every Prompt You&#39;ve Ever Saved | Build Once, Use Forever](https://www.youtube.com/watch?v=hqiStqp6FL4)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://dub.sh/ai-updates-vs ...

📺 Vaibhav Sisinty

👁️ 60K • 👍 2K • 💬 54 • ⏱️ 10:30 • 1d ago

---

**[President Trump talks job losses to A.I. and U.S. operation in Venezuela in exclusive interview](https://www.youtube.com/watch?v=J8UxjCRZQpo)**

NBC Nightly News anchor Tom Llamas spoke to President Trump about fears of job losses from A.I. President Trump also ...

📺 NBC News

👁️ 36K • 👍 113 • 💬 116 • ⏱️ 4:39 • 2d ago

---

**[Nvidia CEO Jensen Huang: AI is going to fundamentally change how we compute everything](https://www.youtube.com/watch?v=P9dX_ek_6yY)**

Jensen Huang, NVIDIA CEO, joins CNBC's "Halftime Report to discuss the power of Artificial Intelligence and where he sees the ...

📺 CNBC Television

👁️ 138K • 👍 2K • 💬 406 • ⏱️ 8:35 • 1d ago

---

**[The Two Best AI Models/Enemies Just Got Released Simultaneously](https://www.youtube.com/watch?v=1PxEziv5XIU)**

The two models that you will hear discussed for at least the next two months - Claude Opus 4.6 and GPT 5.3 Codex - just got ...

📺 AI Explained

👁️ 59K • 👍 3K • 💬 313 • ⏱️ 19:50 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a 0.9B parameter multimodal OCR model for complex document understanding, excelling at table recognition, formula extraction, and information extraction across diverse layouts. It offers state-of-the-art performance with efficient inference, supporting deployment via vLLM, SGLang, and Ollama for real-world business applications.

`image-to-text`

⬇️ 248,295 • ❤️ 800 • 5d ago

---

**[Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)**

*Qwen*

Qwen3-Coder-Next is an 80B parameter (3B active) LLM optimized for coding agents, featuring advanced agentic capabilities like long-horizon reasoning and tool usage. It boasts a 256k context length for seamless IDE integration and efficient local development.

`text-generation` `79.7B`

⬇️ 76,632 • ❤️ 597 • 4d ago

---

**[Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5)**

*Moonshot AI*

Kimi K2.5 is a native multimodal agentic model with 1T parameters, excelling in vision-language understanding and agentic tool use. Its key capabilities include generating code from visual inputs and orchestrating an agent swarm for complex task decomposition and parallel execution.

`image-text-to-text` `170.7B`

⬇️ 404,508 • ❤️ 1,850 • 3d ago

---

**[Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash)**

*StepFun*

Step 3.5 Flash is an efficient, open-source MoE foundation model (11B active params, 196B total) excelling in deep reasoning and agentic tasks with high throughput (100-300 tok/s). It features a 256K context window and strong performance on coding and reasoning benchmarks, suitable for local deployment.

`text-generation` `199.4B`

⬇️ 104,643 • ❤️ 519 • 1d ago

---

**[MiniCPM-o-4_5](https://huggingface.co/openbmb/MiniCPM-o-4_5)**

*OpenBMB*

MiniCPM-o 4.5 is a 9B parameter multimodal LLM excelling in vision, speech, and full-duplex live streaming, rivaling proprietary models like GPT-4o and Gemini 2.5 Flash. It offers advanced OCR, bilingual real-time conversation with voice cloning, and proactive omnimodal interaction for fluid, real-time experiences.

`any-to-any` `9.4B`

⬇️ 17,457 • ❤️ 603 • 21h ago

---

**[Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5)**

*ACE-Step*

ACE-Step 1.5 is an open-source text-to-audio music generation model capable of producing commercial-ready music with precise stylistic control and editing features. It utilizes a hybrid LM-DiT architecture trained on licensed and royalty-free data, offering extreme speed and low VRAM requirements for consumer hardware, making it ideal for music artists and content creators.

`text-to-audio`

⬇️ 23,178 • ❤️ 441 • 5d ago

---

**[Anima](https://huggingface.co/circlestone-labs/Anima)**

*CircleStone Labs*

Anima is a 2 billion parameter text-to-image diffusion model specializing in anime and non-photorealistic artistic styles, trained on millions of anime and artistic images. It is designed for generating illustrations and artistic images, with primary use cases in ComfyUI workflows for anime concepts and characters.

⬇️ 71,655 • ❤️ 507 • 7d ago

---

**[Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)**

*Mistral AI_*

Voxtral-Mini-4B-Realtime-2602 is a 4B-parameter, multilingual speech-to-text model offering near-offline accuracy with <500ms latency. It features a streaming architecture for real-time applications like voice assistants and live subtitling, optimized for on-device deployment.

⬇️ 2,427 • ❤️ 376 • 3d ago

---

**[Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF)**

*Unsloth AI*

Qwen3-Coder-Next is an 80B parameter LLM optimized for coding agents, featuring 3B activated parameters, advanced agentic capabilities for long-horizon reasoning and tool usage, and a 256k context length for seamless IDE integration.

`text-generation` `79.7B`

⬇️ 185,433 • ❤️ 210 • 3d ago

---

**[Intern-S1-Pro](https://huggingface.co/internlm/Intern-S1-Pro)**

*Intern Large Models*

Intern-S1-Pro is a trillion-scale MoE multimodal scientific reasoning model, excelling in AI4Science domains (chemistry, materials, life-science, earth) with strong general multimodal and text capabilities, supporting long, heterogeneous time-series data.

`image-text-to-text`

⬇️ 8,055 • ❤️ 196 • 3d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[PaperBanana: Automating Academic Illustration for AI Scientists](https://huggingface.co/papers/2601.23265)**

*Dawei Zhu, Rui Meng, Yale Song et al. (7 authors)*

🏢 Google

_paperbanana is an agentic framework that automates the creation of publication-ready academic illustrations using advanced vision-language models and image generation techniques.

▲ 141 • 💬 12 • ⭐ 2,416 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2601.23265) • [💻 code](https://github.com/dwzhu-pku/PaperBanana) • [🔗 project](https://dwzhu-pku.github.io/PaperBanana/)

---

**[Multi-Agent Software Development through Cross-Team Collaboration](https://huggingface.co/papers/2406.08979)**

*Zhuoyun Du, Chen Qian, Wei Liu et al. (8 authors)*

Cross-Team Collaboration improves software quality by enabling multiple LLM agent teams to propose and communicate decisions.

▲ 3 • 💬 0 • ⭐ 30,492 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.08979) • [💻 code](https://github.com/OpenBMB/ChatDev)

---

**[Scaling Large-Language-Model-based Multi-Agent Collaboration](https://huggingface.co/papers/2406.07155)**

*Chen Qian, Zihao Xie, Yifei Wang et al. (10 authors)*

Multi-agent collaboration networks enhance collective intelligence, outperforming baselines across various topologies and showing emergent abilities earlier than neural scaling laws suggest.

▲ 4 • 💬 0 • ⭐ 30,515 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2406.07155) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/macnet) • [🔗 project](https://github.com/OpenBMB/ChatDev/tree/macnet)

---

**[Multi-Agent Collaboration via Evolving Orchestration](https://huggingface.co/papers/2505.19591)**

*Yufan Dang, Chen Qian, Xueheng Luo et al. (14 authors)*

A centralized orchestrator dynamically directs LLM agents via reinforcement learning, achieving superior multi-agent collaboration in varying tasks with reduced computational costs.

▲ 6 • 💬 0 • ⭐ 30,506 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2505.19591) • [💻 code](https://github.com/OpenBMB/ChatDev/tree/puppeteer)

---

**[Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://huggingface.co/papers/2508.03680)**

*Xufang Luo, Yuge Zhang, Zhiyuan He et al. (8 authors)*

Agent Lightning is a flexible RL framework for training LLMs in various agents, using a hierarchical RL algorithm and decoupling execution from training to handle complex interactions.

▲ 133 • 💬 6 • ⭐ 14,260 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.03680) • [💻 code](https://github.com/microsoft/agent-lightning) • [🔗 project](https://www.microsoft.com/en-us/research/project/agent-lightning/)

---

**[Advancing Open-source World Models](https://huggingface.co/papers/2601.20540)**

*Robbyant Team, Zelin Gao, Qiuyu Wang et al. (24 authors)*

🏢 Robbyant

LingBot-World is an open-source world simulator with high-fidelity dynamics, long-term memory capabilities, and real-time interactivity for diverse environments.

▲ 119 • 💬 2 • ⭐ 2,647 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2601.20540) • [💻 code](https://github.com/Robbyant/lingbot-world/) • [🔗 project](https://technology.robbyant.com/lingbot-world)

---

**[MiniCPM-V 4.5: Cooking Efficient MLLMs via Architecture, Data, and
  Training Recipe](https://huggingface.co/papers/2509.18154)**

*Tianyu Yu, Zefan Wang, Chongyi Wang et al. (34 authors)*

MiniCPM-V 4.5, a 8B parameter multimodal large language model, achieves high performance and efficiency through a unified 3D-Resampler architecture, a unified learning paradigm, and a hybrid reinforcement learning strategy.

▲ 53 • 💬 4 • ⭐ 23,255 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.18154) • [💻 code](https://github.com/OpenBMB/MiniCPM-V)

---

**[Qwen3-TTS Technical Report](https://huggingface.co/papers/2601.15621)**

*Hangrui Hu, Xinfa Zhu, Ting He et al. (16 authors)*

🏢 Qwen

The Qwen3-TTS series presents advanced multilingual text-to-speech models with voice cloning and controllable speech generation capabilities, utilizing dual-track LM architecture and specialized speech tokenizers for efficient streaming synthesis.

▲ 60 • 💬 1 • ⭐ 7,143 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2601.15621) • [💻 code](https://github.com/QwenLM/Qwen3-TTS)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 6 • 💬 0 • ⭐ 28,039 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet/tree/paper)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 138 • 💬 19 • ⭐ 52,411 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

---

## GitHub Repositories: "ai"

**[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**

Browser automation CLI for AI agents

`TypeScript`

⭐ 13.2k • 🔱 764 • 1d ago

---

**[vercel-labs/json-render](https://github.com/vercel-labs/json-render)**

AI → JSON → UI

`TypeScript`

⭐ 10.1k • 🔱 538 • 13h ago

---

**[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**

LLM驱动的 A/H/美股智能分析器，多数据源行情 + 实时新闻 + Gemini 决策仪表盘 + 多渠道推送，零成本，纯白嫖，定时运行

`Python` `agent` `ai` `aigc` `gemini` `llm`

⭐ 9.9k • 🔱 10.4k • 3h ago

---

**[sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)**

The Ultimate Collection of 700+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

`Python` `agentic-skills` `ai-agents` `antigravity` `autonomous-coding` `claude-code`

⭐ 7.9k • 🔱 1.6k • 3h ago

---

**[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)**

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

`claude` `codex` `marketing`

⭐ 6.7k • 🔱 751 • 4d ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 4.7k • 🔱 368 • 4d ago

---

**[blader/humanizer](https://github.com/blader/humanizer)**

Claude Code skill that removes signs of AI-generated writing from text

⭐ 4.4k • 🔱 364 • 16d ago

---

**[DevAgentForge/Open-Claude-Cowork](https://github.com/DevAgentForge/Open-Claude-Cowork)**

OpenSource Claude Cowork. A desktop AI assistant that helps you with programming, file management, and any task you can describe.

`TypeScript`

⭐ 2.8k • 🔱 378 • 10h ago

---

**[op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)**

Humanizer 的汉化版本，Claude Code Skills，旨在消除文本中 AI 生成的痕迹。

⭐ 2.7k • 🔱 260 • 20d ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`JavaScript`

⭐ 2.5k • 🔱 112 • 5d ago

---

---

*Generated by PeekDeck - A glance is all you need*

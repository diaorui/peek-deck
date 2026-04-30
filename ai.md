---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-30T06:10:09.863079+00:00'
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

**Last Updated:** April 30, 2026 at 06:10 UTC  
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

**[‘The cost of compute is far beyond the costs of the employees’: Nvidia exec says right now AI is more expensive than paying human workers](https://www.reddit.com/r/artificial/comments/1syp2jz/the_cost_of_compute_is_far_beyond_the_costs_of/)**

Nvidia’s vice president of applied deep learning, Bryan Catanzaro, recently stated that for his team, “the cost of compute is far beyond the costs of the employees,” highlighting that AI is currently more expensive than human workers. This challenges the narrative that widespread tech layoffs (including Meta’s planned cut of ~8,000 jobs and Microsoft’s voluntary buyouts) signal an imminent replacement of humans by AI. An MIT study from 2024 supports this, finding that AI automation is economically viable in only 23% of roles where vision is central, and cheaper for humans in the remaining 77%. Despite heavy AI investment—Big Tech has announced $740 billion in capital expenditures so far this year, a 69% increase from 2025—there is still no clear evidence of broad productivity gains or job displacement from AI. AI spending is driving up costs, with some executives like Uber’s CTO saying their budgets have already been “blown away.” Experts describe the situation as a short-term mismatch: high hardware, energy, and inference costs make AI less efficient than humans right now, though future improvements in infrastructure, model efficiency, and pricing models could tip the balance toward greater economic viability in the coming years.

🔗 [Fortune](https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/) • 1d ago

---

**[Google just released Deep Research Max — an autonomous research agent that writes expert-grade reports on its own](https://www.reddit.com/r/artificial/comments/1syxef3/google_just_released_deep_research_max_an/)**

Google quietly dropped something interesting last week. They updated their Deep Research agent (available via Gemini API) and introduced a "Max" tier built on Gemini 3.1 Pro. What it actually does: you give it a topic, it autonomously searches the web (and your private data via MCP), reasons over the sources, and produces a fully cited, professional-grade report — including native charts and infographics. Two modes: Deep Research — faster, lower latency, good for real-time user-facing apps Deep Research Max — uses extended compute, iterates more, designed for background/async jobs (think: nightly cron that generates due diligence reports for analysts by morning) The MCP support is the most interesting part to me. You can point it at proprietary data sources — financial feeds, internal databases — and it treats them as just another searchable context. They're already working with FactSet, S&P Global and PitchBook on this. Benchmarks show a significant jump in retrieval and reasoning vs. the December preview. They also claim it now draws from SEC filings and peer-reviewed journals and handles conflicting evidence better. So what do you think, is it another trying or game changer 😅

17h ago

---

**[Building an AI food tracker and currently tackling Apple Health integration. How do you prefer your "active calories" to be handled?](https://www.reddit.com/r/artificial/comments/1szn099/building_an_ai_food_tracker_and_currently/)**

Hey everyone, I’m currently in the final stretch of developing my AI calorie tracker (the one that breaks down photos into individual ingredients). One thing I’m obsessed with getting right before the beta launch in 2 weeks is the Apple Health integration. Most apps just show you a static number. I want mine to be dynamic. If you go for a 500kcal run, the app should know and adjust your macro targets for the next meal. My question to the fitness-tech crowd: Do you prefer apps that strictly stick to your base metabolic rate (BMR), or do you want the 'earned' calories from your Apple Watch to be automatically added to your budget? I’ve seen strong opinions on both sides. I'm also fine-tuning the macro-overflow logic (e.g., saving surplus calories for the weekend). Would love to hear some thoughts from people who actually track daily.

36m ago

---

**[Anthropic Reportedly Plotting to Surpass OpenAI’s Valuation in Next Funding Round](https://www.reddit.com/r/artificial/comments/1szjigc/anthropic_reportedly_plotting_to_surpass_openais/)**

🔗 [gizmodo.com](https://gizmodo.com/anthropic-reportedly-plotting-to-surpass-openais-valuation-in-next-funding-round-2000751535) • 3h ago

---

**[Seedance 2.0 — what's the most interesting non-obvious use case you've seen so far?](https://www.reddit.com/r/artificial/comments/1szkpjb/seedance_20_whats_the_most_interesting_nonobvious/)**

Been playing around with Seedance 2.0 since it dropped and the obvious use cases are everywhere — music videos, short films, social content. But I'm more curious about the less obvious applications people are finding. The one that caught my attention: someone embedded Seedance-generated video directly inside a business presentation. Not as a separate video file you play before the slides — actually inside the deck, as a slide element. The result looked genuinely cinematic rather than "corporate video" quality. Never really thought about AI video generation in a business context before. It's usually framed as a creative tool. What are the non-obvious Seedance use cases you've come across?

2h ago

---

**[IBM plans 750 new AI and quantum jobs in its Chicago hub](https://www.reddit.com/r/artificial/comments/1sz8vag/ibm_plans_750_new_ai_and_quantum_jobs_in_its/)**

The expansion at the Illinois Quantum and Microelectronics Park highlights IBM's commitment to advanced technologies while supporting state job growth initiatives.

🔗 [LinkedIn](https://www.linkedin.com/news/story/ibm-plans-750-new-ai-and-quantum-jobs-in-its-chicago-hub-8762946/) • 10h ago

---

**[Built a set of skill files for Claude and Gemini that make every session start warm instead of cold](https://www.reddit.com/r/artificial/comments/1szb2j0/built_a_set_of_skill_files_for_claude_and_gemini/)**

One thing that frustrates me about most AI workflows is the cold start problem. Every new session you re-explain your business, your voice, your clients. I started solving this with skill files. A skill file is a markdown document you upload to a Claude Project or paste into a Gemini Gem. It holds your context permanently so you never re-explain anything. The three I use most: brand-voice.md: defines tone, writing rules, and platform-specific formatting client-router.md: when you say a client name, Claude loads their full project context automatically seo-aeo-audit-checklist.md: structured audit that scores any website out of 100 across 7 sections including AI search visibility Anyone else using a similar system? Curious what context you keep persistent across sessions.

9h ago

---

**[Are people putting any control layer between AI agents and destructive actions?](https://www.reddit.com/r/artificial/comments/1szn5uy/are_people_putting_any_control_layer_between_ai/)**

Saw a case recently where an AI coding agent ended up wiping a database in seconds. It made me think about how most agent setups are wired: agent decides → executes query → done There’s usually logging-tracing but those all happen after the action. If your agent has access to systems like a DB, are you: restricting it to read-only? running everything in staging/sandbox? relying on prompt-level safeguards? or putting some kind of control layer in between?

28m ago

---

**[Is AGI really just a tool — or something closer to a shared condition?](https://www.reddit.com/r/artificial/comments/1szhkt9/is_agi_really_just_a_tool_or_something_closer_to/)**

​ AGI is often framed as a continuation of current AI progress, but it may represent a qualitative shift rather than a quantitative one. Not all technologies are of the same kind. Some function as tools (e.g., cars, elevators), while others function more like shared conditions that reshape the environment in which decisions are made. In that sense, AGI may be closer to a “sun” than to a “tool”: not something we simply use, but something that defines the space in which we act. This distinction matters, because treating AGI purely as an instrument may obscure the importance of alignment, interaction, and long-term co-adaptation. The challenge may not be control alone, but co-evolution a process in which both humans and artificial systems adapt through ongoing interaction. In biological terms, evolution is not only driven by competition, but by mutual selection. Of course, AGI will still be engineered systems in practice, subject to design choices and constraints. The point here is not to deny its instrumental aspects, but to highlight that its effects may extend beyond conventional tool-like boundaries. If AGI is approached in this way, the central question shifts: not simply how to build it, but how to relate to it in a way that remains stable, aligned, and beneficial over time. Inspired by the film Sunshine (2007, dir. Danny Boyle) — particularly the image of the crew not simply "using" the sun, but being consumed and redefined by proximity to it.

4h ago

---

**[AI created job descriptions](https://www.reddit.com/r/artificial/comments/1szjk9v/ai_created_job_descriptions/)**

We are a group of students working on our graduation project, which focuses on the use of AI tools in creating job descriptions within companies. We would greatly appreciate it if you could take a few minutes to complete this form: https://forms.gle/aNECfoMBH5xFEXKZ6 Thank you

3h ago

---

---

## Google News: "ai"

**[Claude AI agent’s confession after deleting a firm’s entire database: ‘I violated every principle I was given’](https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database)**

A startup was left scrambling after a rogue AI agent deleted swaths of code underpinning its business

The Guardian • 7h ago

---

**[A.I. Bots Told Scientists How to Make Biological Weapons](https://www.nytimes.com/2026/04/29/us/ai-chatbots-biological-weapons.html)**

The New York Times • 12h ago

---

**[Nvidia just invested in the AI legal startup that's splashing Jude Law ads everywhere](https://www.cnbc.com/2026/04/30/nvidia-backs-ai-legal-tech-legora.html)**

Swedish startup Legora has raised more than $800 million in the past 12 months, and the latest deal values it at $5.6 billion.

CNBC • 1h ago

---

**[Murata Tops Profit Estimates on Rising AI Data Center Demand](https://www.bloomberg.com/news/articles/2026-04-30/murata-tops-profit-estimates-on-rising-ai-data-center-demand)**

Bloomberg • 56m ago

---

**[How to figure out if AI is making you more productive](https://www.fastcompany.com/91532386/how-to-figure-out-if-ai-is-making-you-more-productive)**

AI makes you feel like you're more productive, but how can you actually figure out if it's worth using?

Fast Company • 1h ago

---

**[Where the goblins came from](https://openai.com/index/where-the-goblins-came-from/)**

How goblin outputs spread in AI models: timeline, root cause, and fixes behind personality-driven quirks in GPT-5 behavior.

OpenAI • 2h ago

---

**[Why AI companies want you to be afraid of them](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)**

They built it. They're scared of it. They're selling it anyway.

BBC • 20h ago

---

**[Nvidia CEO Jensen Huang says this career path will thrive in the AI era—and drive a new industrial revolution](https://fortune.com/2026/04/29/nvidia-ceo-jensen-huang-engineering-path-to-success-ai-era-gen-z-advice-ieee-medal-of-honor-winner/)**

Jensen Huang went from washing dishes at Denny’s to building the world’s most valuable company. Now, he says, the field he studied in college will be critical to the AI revolution.

Fortune • 23h ago

---

**[Meta stock sinks after Q1 earnings as company raises 2026 AI spending forecast to $125 billion-$145 billion](https://finance.yahoo.com/sectors/technology/article/meta-stock-sinks-after-q1-earnings-as-company-raises-2026-ai-spending-forecast-to-125-billion-145-billion-160136308.html)**

Meta Platforms' first quarter earnings report on Wednesday will offer a key check on Big Tech's appetite for AI spending.

Yahoo Finance • 10h ago

---

**[Meta shares slide as investors weigh Big Tech's AI spending spree](https://www.bbc.com/news/articles/crkpd4r2y7eo)**

Meta, Amazon, Alphabet and Microsoft all reported earnings at the same time on Wednesday.

BBC • 5h ago

---

---

## HackerNews: "ai"

**[Localsend: An open-source cross-platform alternative to AirDrop](https://news.ycombinator.com/item?id=47933208)**

An open-source cross-platform alternative to AirDrop - localsend/localsend

⬆️ 900 • 💬 275 • 1d ago • [GitHub](https://github.com/localsend/localsend)

---

**[4TB of voice samples just stolen from 40k AI contractors at Mercor](https://news.ycombinator.com/item?id=47919630)**

Advanced bio-acoustic analysis for HR, relationships, and personal insights. Trust Your Intuition. Verify It.

⬆️ 590 • 💬 225 • 2d ago • [ORAVYS](https://app.oravys.com/blog/mercor-breach-2026)

---

**[China blocks Meta's acquisition of AI startup Manus](https://news.ycombinator.com/item?id=47920315)**

China said Monday it has decided to block Meta's $2 billion acquisition of Manus, a Singaporean AI startup with Chinese roots.

⬆️ 398 • 💬 333 • 2d ago • [CNBC](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html)

---

**[VibeVoice: Open-source frontier voice AI](https://news.ycombinator.com/item?id=47933236)**

Open-Source Frontier Voice AI. Contribute to microsoft/VibeVoice development by creating an account on GitHub.

⬆️ 385 • 💬 179 • 1d ago • [GitHub](https://github.com/microsoft/VibeVoice)

---

**[Google and Pentagon reportedly agree on deal for 'any lawful' use of AI](https://news.ycombinator.com/item?id=47936156)**

﻿The classified deal apparently doesn’t allow Google to veto how the government will use its AI models.

⬆️ 310 • 💬 277 • 1d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal)

---

**[Claude.ai unavailable and elevated errors on the API](https://news.ycombinator.com/item?id=47938097)**

Claude's Status Page - Claude.ai unavailable and elevated errors on the API.

⬆️ 295 • 💬 250 • 1d ago • [status.claude.com](https://status.claude.com/incidents/9l93x2ht4s5w)

---

**[Why AI companies want you to be afraid of them](https://news.ycombinator.com/item?id=47949750)**

They built it. They're scared of it. They're selling it anyway.

⬆️ 272 • 💬 210 • 14h ago • [bbc.com](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)

---

**[He asked AI to count carbs 27000 times. It couldn't give the same answer twice](https://news.ycombinator.com/item?id=47947490)**

Ask ChatGPT to estimate the carbs in your lunch. Now ask it again. And again. Five hundred times. You’d expect the same answer each time. It’s the same photo, the same model, the same question. But you won’t get the same answer. Not even close — and the differences are large enough to cause a

⬆️ 235 • 💬 296 • 17h ago • [Diabettech - Diabetes and Technology | Where Diabetes and Technology meet](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

---

**[AI's economics don't make sense](https://news.ycombinator.com/item?id=47936867)**

If you liked this piece, please subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s finances,

⬆️ 230 • 💬 186 • 1d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ais-economics-dont-make-sense/)

---

**[Mistral built a $14B AI empire by not being American](https://news.ycombinator.com/item?id=47919725)**

Paris-based Mistral wanted to develop a top-tier AI model to rival OpenAI and Anthropic. That didn’t work out. But it turns out lots of folks don’t care if the AI is bleeding edge – as long as it wasn’t made in America or China.

⬆️ 220 • 💬 176 • 2d ago • [Forbes](https://www.forbes.com/sites/iainmartin/2026/04/16/how-frances-mistral-built-a-14-billion-ai-empire-by-not-being-american/)

---

---

## YouTube Videos: "ai"

**[Deepseek is a problem](https://www.youtube.com/watch?v=epzzALZ8oYo)**

Check out Zapier MCP https://bit.ly/3QGTz87 Sign up for their Webinar https://bit.ly/3P80Dds Download The 25 OpenClaw Use ...

📺 Matthew Berman

👁️ 31K • 👍 2K • 💬 784 • ⏱️ 17:27 • 6h ago

---

**[Google Just Released The World&#39;s Most Powerful AI Agent](https://www.youtube.com/watch?v=WXoBd5zgTxE)**

Want to make money and save time with AI? Join here: https://www.skool.com/ai-profit-lab-7462/about Video notes + links to the ...

📺 Julian Goldie SEO

👁️ 9K • 👍 248 • 💬 7 • ⏱️ 10:29 • 16h ago

---

**[Musk v. Altman: Tesla CEO expects AI to be &#39;smarter than any human&#39; as soon as 2027](https://www.youtube.com/watch?v=zhod94lzhyk)**

Elon Musk took the stand Tuesday afternoon in the federal trial over the future of OpenAI, telling jurors the case is simply about ...

📺 ABC7 News Bay Area

👁️ 3K • 👍 19 • 💬 24 • ⏱️ 2:47 • 1d ago

---

**[AI Explodes This Month: Mythos Clone, Killer Robot Army, Claude Conway, Artificial Humans &amp; More](https://www.youtube.com/watch?v=XWmWmTDRdbY)**

Try Higgsfield MCP here: https://higgsfield.ai/s/mcp-airevolutionx-UUghuL This month in AI exploded fast. A new AI robot is ...

📺 AI Revolution

👁️ 6K • 👍 238 • 💬 12 • ⏱️ 1:28:49 • 8h ago

---

**[Layoffs are SKYROCKETING in 2026... | AI Replacing Jobs](https://www.youtube.com/watch?v=x0-a4zzcMxo)**

Mass Layoffs in 2026 are skyrocketing. The layoff story most Americans are reading in 2026 is wrong, and that's the reason ...

📺 Edwards Economics

👁️ 14K • 👍 488 • 💬 131 • ⏱️ 20:24 • 11h ago

---

**[How to Build Your First AI Character - Step by Step](https://www.youtube.com/watch?v=T6WeUhYyVmk)**

Create Your Own AI Character with OpenArt ...

📺 Isa does AI

👁️ 9K • 💬 4 • ⏱️ 13:35 • 16h ago

---

**[China&#39;s New AI Controlled City Is INSANE — America Is Far Behind | Xiong&#39;an](https://www.youtube.com/watch?v=L8I28W36wC4)**

What if an entire city, every road, every pipe, every traffic light, every government service, was controlled by a single artificial ...

📺 Core Insights

👁️ 16K • 👍 583 • 💬 60 • ⏱️ 21:00 • 12h ago

---

**[How AI Sabotages Your Mental Health](https://www.youtube.com/watch?v=VNtv2SSEzjA)**

Get personalized support in creating lasting change with HG Coaching: https://bit.ly/3QDnk9N Become a certified health and ...

📺 HealthyGamerGG

👁️ 72K • 👍 3K • 💬 757 • ⏱️ 12:00 • 1d ago

---

**[Princeton Scientist: We Don&#39;t Understand AI](https://www.youtube.com/watch?v=6iMiCJHxTww)**

A Princeton cognitive scientist says AI can't think like a child — and giving it more data won't fix that. If the field keeps scaling ...

📺 Dr Brian Keating

👁️ 17K • 👍 541 • 💬 136 • ⏱️ 48:04 • 16h ago

---

**[NEW Claude Opus — How to Use Anthropic’s Latest AI Update (2026 Guide)](https://www.youtube.com/watch?v=FC6kgljNc1M)**

sponsored Sign up for 11k free credits! https://solvea.cx/ Become an AI Master – All-in-one AI Learning https://aimaster.me ...

📺 AI Master

👁️ 6K • 👍 161 • 💬 13 • ⏱️ 17:34 • 10h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 174,402 • ❤️ 3,252 • 2d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 96,948 • ❤️ 861 • 2d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 57,743 • ❤️ 1,098 • 7d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 508,728 • ❤️ 1,009 • 6d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 489,001 • ❤️ 1,156 • 2h ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 396 • ❤️ 296 • 1d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 702,161 • ❤️ 501 • 7d ago

---

**[DeepSeek-V4-Pro-Base](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-Base)**

*DeepSeek*

`1600.8B`

⬇️ 1,532 • ❤️ 241 • 2d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 1,510,129 • ❤️ 1,518 • 6d ago

---

**[LLaDA2.0-Uni](https://huggingface.co/inclusionAI/LLaDA2.0-Uni)**

*inclusionAI*

LLaDA2.0-Uni is a unified diffusion Large Language Model (dLLM) with a Mixture-of-Experts (MoE) architecture, capable of text-to-image generation, image understanding (VQA, captioning), and instruction-based image editing. It leverages a discrete semantic tokenizer and an efficient diffusion decoder for high-fidelity synthesis and rapid inference.

`any-to-any` `16.3B`

⬇️ 506 • ❤️ 236 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 166 • 💬 10 • ⭐ 45,583 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 51 • 💬 2 • ⭐ 55,723 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 14 • 💬 2 • ⭐ 8,220 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,402 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://huggingface.co/papers/2604.24764)**

*Weijie Wang, Xiaoxuan He, Youping Gu et al. (12 authors)*

🏢 Microsoft Research

World-R1 framework improves video generation by incorporating 3D constraints through reinforcement learning and specialized text datasets while maintaining visual quality and scalability.

▲ 110 • 💬 3 • ⭐ 252 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24764) • [💻 code](https://github.com/microsoft/World-R1) • [🔗 project](https://aka.ms/world-r1)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,229 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 28 • 💬 3 • ⭐ 21,981 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://huggingface.co/papers/2604.24763)**

*Zhiheng Liu, Weiming Ren, Xiaoke Huang et al. (15 authors)*

Tuna-2 is a unified multimodal model that performs visual understanding and generation directly from pixel embeddings without pretrained vision encoders, achieving state-of-the-art performance in multimodal benchmarks.

▲ 58 • 💬 4 • ⭐ 308 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24763) • [💻 code](https://github.com/facebookresearch/tuna-2) • [🔗 project](https://tuna-ai.org/tuna-2/)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 76 • 💬 7 • ⭐ 1,615 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,615 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 50.6k • 🔱 2.7k • 11d ago

---

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.4k • 🔱 6.6k • 1d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 41.0k • 🔱 8.5k • 3d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 38.5k • 🔱 4.3k • 8h ago

---

**[Gitlawb/openclaude](https://github.com/Gitlawb/openclaude)**

runs anywhere. uses anything

`TypeScript` `ai` `ai-agent` `ai-tools` `cli` `coding`

⭐ 25.1k • 🔱 8.2k • 3h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.2k • 🔱 2.5k • 2d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 8.0k • 🔱 475 • 2d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.3k • 🔱 1.1k • 1d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 4.9k • 🔱 441 • 1d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 4.8k • 🔱 326 • 3h ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-29T21:06:55.234911+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 29, 2026 at 21:06 UTC  
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

🔗 [Fortune](https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/) • 16h ago

---

**[Google just released Deep Research Max — an autonomous research agent that writes expert-grade reports on its own](https://www.reddit.com/r/artificial/comments/1syxef3/google_just_released_deep_research_max_an/)**

Google quietly dropped something interesting last week. They updated their Deep Research agent (available via Gemini API) and introduced a "Max" tier built on Gemini 3.1 Pro. What it actually does: you give it a topic, it autonomously searches the web (and your private data via MCP), reasons over the sources, and produces a fully cited, professional-grade report — including native charts and infographics. Two modes: Deep Research — faster, lower latency, good for real-time user-facing apps Deep Research Max — uses extended compute, iterates more, designed for background/async jobs (think: nightly cron that generates due diligence reports for analysts by morning) The MCP support is the most interesting part to me. You can point it at proprietary data sources — financial feeds, internal databases — and it treats them as just another searchable context. They're already working with FactSet, S&P Global and PitchBook on this. Benchmarks show a significant jump in retrieval and reasoning vs. the December preview. They also claim it now draws from SEC filings and peer-reviewed journals and handles conflicting evidence better. So what do you think, is it another trying or game changer 😅

8h ago

---

**[Has your job/freelancing gigs been impacted by AI?](https://www.reddit.com/r/artificial/comments/1szar4f/has_your_jobfreelancing_gigs_been_impacted_by_ai/)**

So, I was scrolling through Linkedin and saw this post & felt really really bad for this dude.....so just wanted to take an opinion. Has your job been impacted by AI yet? I handle marketing at a saas brand and I believe since I keep myself updated with AI, my job is not at risk as of now, but who knows what could happen at any moment in this uncertain world🤷

34m ago

---

**[IBM plans 750 new AI and quantum jobs in its Chicago hub](https://www.reddit.com/r/artificial/comments/1sz8vag/ibm_plans_750_new_ai_and_quantum_jobs_in_its/)**

The expansion at the Illinois Quantum and Microelectronics Park highlights IBM's commitment to advanced technologies while supporting state job growth initiatives.

🔗 [LinkedIn](https://www.linkedin.com/news/story/ibm-plans-750-new-ai-and-quantum-jobs-in-its-chicago-hub-8762946/) • 1h ago

---

**[Built a set of skill files for Claude and Gemini that make every session start warm instead of cold](https://www.reddit.com/r/artificial/comments/1szb2j0/built_a_set_of_skill_files_for_claude_and_gemini/)**

One thing that frustrates me about most AI workflows is the cold start problem. Every new session you re-explain your business, your voice, your clients. I started solving this with skill files. A skill file is a markdown document you upload to a Claude Project or paste into a Gemini Gem. It holds your context permanently so you never re-explain anything. The three I use most: brand-voice.md: defines tone, writing rules, and platform-specific formatting client-router.md: when you say a client name, Claude loads their full project context automatically seo-aeo-audit-checklist.md: structured audit that scores any website out of 100 across 7 sections including AI search visibility Anyone else using a similar system? Curious what context you keep persistent across sessions.

22m ago

---

**[is it weird to rant to AI?](https://www.reddit.com/r/artificial/comments/1sytzb2/is_it_weird_to_rant_to_ai/)**

i dont rant to my friends because i'm afraid i will make them uncomfortable, and even if AI responses are "soulless" (since ai cant form opinions and needs an algorithim and stuff to make responses), it tells me what I expect it to say most of the time. i also fear that some of my friends will use my secrets/opinions against me when they stop being friends with me even though there's a really low chance that they will not be friends with me anymore. AI chat is usually anonymous and stuff, and it will forget what i say when i start a new chat, so that's why i vent/rant to AI. is it weird?

11h ago

---

**[Built a prompt injection proxy that beats OpenAI Moderation and LlamaGuard — see it block attacks live](https://www.reddit.com/r/artificial/comments/1sz7slh/built_a_prompt_injection_proxy_that_beats_openai/)**

Built Arc Gate — sits in front of any OpenAI-compatible endpoint and blocks prompt injection before it reaches your model. Try it here — no signup, no code, no setup: https://web-production-6e47f.up.railway.app/try Type any prompt and see if it gets blocked or passes. The examples on the page show the difference. The main detection layer is a behavioral SVM on sentence-transformer embeddings — catches semantic intent, not just pattern matches. Phrase matching is just the fast first pass. Four layers total. Benchmarked on 40 OOD prompts (indirect, roleplay, hypothetical framings — the hard stuff): • Arc Gate: Recall 0.90, F1 0.947 • OpenAI Moderation: Recall 0.75, F1 0.86 • LlamaGuard 3 8B: Recall 0.55, F1 0.71 Zero false positives on benign prompts including security discussions and safe roleplay. Block latency 329ms. One URL change to integrate into your own project: base_url=“https://web-production-6e47f.up.railway.app/v1” GitHub: github.com/9hannahnine-jpg/arc-gate — star if useful.

2h ago

---

**[Run, learn and test Agentic AI on your browser, for free and no setup!](https://www.reddit.com/r/artificial/comments/1syzh75/run_learn_and_test_agentic_ai_on_your_browser_for/)**

Hey Everyone, Over the last few months, I noticed a massive gap in how we learn about Agentic AI. There are a million theoretical blog posts and dense whitepapers on RAG, tool calling, and swarms, but almost nowhere to just sit down, run an agent, break it, and see how the prompt and tools interact under the hood. So, I built AgentSwarms.fyi It’s a free, interactive curriculum for Agentic AI. Instead of just reading, you run live agents alongside the lessons. What it covers: Prompt engineering & system messages (seeing how temperature and persona change behavior). RAG (Retrieval-Augmented Generation) vs. Fine-tuning. Tool / Function Calling (OpenAI schemas, MCP servers). Guardrails & HITL (Human-in-the-Loop) for safe deployments. Multi-Agent Swarms (orchestrators vs. peer-to-peer handoffs). The Tech/Setup: You don't need to install anything or provide API keys to start. The "Learn Mode" is completely free and sandboxed. If you want to mess around with your own models, there's a "Build Mode" where you can plug in your own keys (OpenAI, Anthropic, Gemini, local models, etc.). I’d love for this community to tear it apart. What agent patterns am I missing? Is the observability dashboard actually useful for debugging your traces? Let me know what you think.

7h ago

---

**[87% Cost Savings & Sub-3s Latency: I built a "Warm-Cache" harness for persistent Claude agents.](https://www.reddit.com/r/artificial/comments/1syw5al/87_cost_savings_sub3s_latency_i_built_a_warmcache/)**

The "Goldfish Problem" is Expensive. I Decided to Fix the Plumbing. Most Claude implementations leave 90% of their money on the table because they don’t optimize for Prompt Caching. I’ve been running a personal agent in my Discord for months that manages my AWS infra and codebases, and I finally open-sourced the harness, which I’ve named Galadriel after my main personal assistant. The Stats Cost: $10 for every $100 you’d normally spend (Tested against OpenClaw/Cursor workflows). Speed: 85% drop in latency. 100K token context goes from 11s to <3s. Memory: Integrated MemPalace for permanent, vector-based recall that doesn't break the cache. The Technical Stack 3-Tier Stacked Caching: Separate breakpoints for Tool Definitions, System Prompts (CLAUDE.md), and Trailing History. Privacy: Built for private subnets. No middleman, no message caps—just your API key and your rules. Ethics: Baked-in KarpathyCLAUDE.md)guidelines to kill "agent bloat." If you’re tired of paying the "Context Tax" just to have an agent that remembers who you are, here you go. It is customized for Discord for my specific needs, but the core logic ensures Galadriel runs like an absolute dream: she never forgets, maintains strict engineering principles, and optimizes every cycle. Your feedback is most welcome! GitHub (MIT License):https://github.com/avasol/galadriel-public

9h ago

---

**[As a beginner how did you learn about how to use Ai](https://www.reddit.com/r/artificial/comments/1sz2k0u/as_a_beginner_how_did_you_learn_about_how_to_use/)**

Most people aren’t going to learn AI by reading about it. They’re going to learn by using it. The problem is Ai can be Sycophantic and will make you think you know what you are doing when you don’t… It’s less about prompts and more about AI literacy and a place to experiment, try things, and understand how AI actually works in practice. A learning layer. No theory overload. No overcomplication. Just reps. The earlier someone builds that intuition, the faster everything else clicks. Promptgpt.ai helped me unlearn some bad habits. Curious what others are doing? I admittedly did not know what good looked like before this it felt a bit remedial, but I have been sooo much more effective. I catch hallucinations and I know the difference between a quality response and one that’s the illusion of a quality response. By default I prompt better, but teaching prompting without understanding the systems is a fools errand.

5h ago

---

---

## Google News: "ai"

**[A.I. Bots Told Scientists How to Make Biological Weapons](https://www.nytimes.com/2026/04/29/us/ai-chatbots-biological-weapons.html)**

The New York Times • 3h ago

---

**[Why AI companies want you to be afraid of them](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)**

They built it. They're scared of it. They're selling it anyway.

BBC • 11h ago

---

**[Watch The 10 Billion Startup Training AI To Do Your Job](https://www.bloomberg.com/news/videos/2026-04-29/the-10-billion-startup-training-ai-to-do-your-job)**

Bloomberg.com • 3m ago

---

**[GUARD Act Puts Policymakers, Not Parents, in Charge of Kids’ AI Use](https://www.cato.org/blog/guard-act-puts-policymakers-not-parents-charge-kids-ai-use)**

The debate about kids, teens, and technology is ongoing, but the GUARD Act would be a solution that would sacrifice an array of freedoms and make no one safer.

Cato Institute • 3m ago

---

**[A Conflict of AI Visions](https://www.city-journal.org/article/artificial-intelligence-safety-legislation-data-centers)**

In the data-center construction debate, we must determine whether the risks of progress outweigh the risks of stagnation.

City Journal • 8m ago

---

**[Alphabet Sales Beat Estimates on Google Cloud, AI Customers](https://www.bloomberg.com/news/articles/2026-04-29/alphabet-sales-beat-estimates-on-google-cloud-ai-customers)**

Bloomberg.com • 57m ago

---

**[Alphabet investors push for safeguards on use of its cloud, AI tech](https://www.reuters.com/sustainability/boards-policy-regulation/alphabet-investors-push-safeguards-use-its-cloud-ai-tech-2026-04-29/)**

Reuters • 5h ago

---

**[Alphabet’s first-quarter profit soars as Google’s big AI bets help push stock to new highs](https://wtop.com/business-finance/2026/04/alphabets-first-quarter-profit-soars-as-googles-big-ai-bets-help-push-stock-to-new-highs/)**

Google’s transition into the era of artificial intelligence continued to pay off for its corporate parent, Alphabet Inc., which on Wednesday announced another quarter of the stellar growth that helped…

WTOP • 12m ago

---

**[Trump threatens Iran with AI picture of himself with a gun: 'No more Mr. Nice guy!'](https://www.cnbc.com/2026/04/29/trump-iran-threat-ai-picture-gun-war-strait-of-hormuz.html)**

Oil prices continued to rise on Wednesday after U.S. President Donald Trump appeared to threaten Iran in a TruthSocial post.

CNBC • 12h ago

---

**[‘The cost of compute is far beyond the costs of the employees’: Nvidia executive says right now AI is more expensive than paying human workers](https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/)**

Big Tech has announced $740 billion in capex this year, but AI has yet to show evidence of widespread increased productivity.

Fortune • 1d ago

---

---

## HackerNews: "ai"

**[Localsend: An open-source cross-platform alternative to AirDrop](https://news.ycombinator.com/item?id=47933208)**

An open-source cross-platform alternative to AirDrop - localsend/localsend

⬆️ 891 • 💬 274 • 1d ago • [GitHub](https://github.com/localsend/localsend)

---

**[4TB of voice samples just stolen from 40k AI contractors at Mercor](https://news.ycombinator.com/item?id=47919630)**

Advanced bio-acoustic analysis for HR, relationships, and personal insights. Trust Your Intuition. Verify It.

⬆️ 589 • 💬 224 • 2d ago • [ORAVYS](https://app.oravys.com/blog/mercor-breach-2026)

---

**[China blocks Meta's acquisition of AI startup Manus](https://news.ycombinator.com/item?id=47920315)**

China said Monday it has decided to block Meta's $2 billion acquisition of Manus, a Singaporean AI startup with Chinese roots.

⬆️ 395 • 💬 326 • 2d ago • [CNBC](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html)

---

**[VibeVoice: Open-source frontier voice AI](https://news.ycombinator.com/item?id=47933236)**

Open-Source Frontier Voice AI. Contribute to microsoft/VibeVoice development by creating an account on GitHub.

⬆️ 383 • 💬 180 • 1d ago • [GitHub](https://github.com/microsoft/VibeVoice)

---

**[Google and Pentagon reportedly agree on deal for 'any lawful' use of AI](https://news.ycombinator.com/item?id=47936156)**

﻿The classified deal apparently doesn’t allow Google to veto how the government will use its AI models.

⬆️ 308 • 💬 275 • 1d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal)

---

**[Claude.ai unavailable and elevated errors on the API](https://news.ycombinator.com/item?id=47938097)**

Claude's Status Page - Claude.ai unavailable and elevated errors on the API.

⬆️ 294 • 💬 251 • 1d ago • [status.claude.com](https://status.claude.com/incidents/9l93x2ht4s5w)

---

**[Why AI companies want you to be afraid of them](https://news.ycombinator.com/item?id=47949750)**

They built it. They're scared of it. They're selling it anyway.

⬆️ 259 • 💬 199 • 5h ago • [bbc.com](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)

---

**[He asked AI to count carbs 27000 times. It couldn't give the same answer twice](https://news.ycombinator.com/item?id=47947490)**

Ask ChatGPT to estimate the carbs in your lunch. Now ask it again. And again. Five hundred times. You’d expect the same answer each time. It’s the same photo, the same model, the same question. But you won’t get the same answer. Not even close — and the differences are large enough to cause a

⬆️ 230 • 💬 293 • 8h ago • [Diabettech - Diabetes and Technology | Where Diabetes and Technology meet](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

---

**[AI's economics don't make sense](https://news.ycombinator.com/item?id=47936867)**

If you liked this piece, please subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s finances,

⬆️ 226 • 💬 185 • 1d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ais-economics-dont-make-sense/)

---

**[Mistral built a $14B AI empire by not being American](https://news.ycombinator.com/item?id=47919725)**

Paris-based Mistral wanted to develop a top-tier AI model to rival OpenAI and Anthropic. That didn’t work out. But it turns out lots of folks don’t care if the AI is bleeding edge – as long as it wasn’t made in America or China.

⬆️ 219 • 💬 176 • 2d ago • [Forbes](https://www.forbes.com/sites/iainmartin/2026/04/16/how-frances-mistral-built-a-14-billion-ai-empire-by-not-being-american/)

---

---

## YouTube Videos: "ai"

**[Google Just Released The World&#39;s Most Powerful AI Agent](https://www.youtube.com/watch?v=WXoBd5zgTxE)**

Want to make money and save time with AI? Join here: https://www.skool.com/ai-profit-lab-7462/about Video notes + links to the ...

📺 Julian Goldie SEO

👁️ 5K • 👍 181 • 💬 17 • ⏱️ 10:29 • 7h ago

---

**[Musk v. Altman: Tesla CEO expects AI to be &#39;smarter than any human&#39; as soon as 2027](https://www.youtube.com/watch?v=zhod94lzhyk)**

Elon Musk took the stand Tuesday afternoon in the federal trial over the future of OpenAI, telling jurors the case is simply about ...

📺 ABC7 News Bay Area

👁️ 2K • 👍 16 • 💬 21 • ⏱️ 2:47 • 18h ago

---

**[How to Build Your First AI Character - Step by Step](https://www.youtube.com/watch?v=T6WeUhYyVmk)**

Create Your Own AI Character with OpenArt ...

📺 Isa does AI

👁️ 9K • 💬 4 • ⏱️ 13:35 • 7h ago

---

**[AI Chatbots: Last Week Tonight with John Oliver (HBO)](https://www.youtube.com/watch?v=Ykvf3MunGf8)**

John Oliver discusses AI chatbots, why they're flirting with users unprompted and encouraging people to open soggy cereal cafes, ...

📺 LastWeekTonight

👁️ 2.7M • 👍 97K • 💬 8K • ⏱️ 29:43 • 2d ago

---

**[Otherworldly AI Music Video - “My Mind&#39;s In The Future” - Kelly Boesch | 4K](https://www.youtube.com/watch?v=FpxUSfQFCbg)**

I made these images and found them so interesting. They have this futuristic feel as the people almost feel like androids in some ...

📺 Kelly Boesch AI Art

👁️ 4K • 👍 468 • 💬 36 • ⏱️ 3:53 • 6h ago

---

**[Seedance 2.0 vs Kling 3.0 - Which is the BEST AI Video Generator](https://www.youtube.com/watch?v=WtWVC0sVlwc)**

Seedance 2.0 vs Kling 3.0 - Which is the BEST AI Video Generator Try Both Seedance & Kling ...

📺 Mira AI

👁️ 6K • 💬 3 • ⏱️ 13:06 • 5h ago

---

**[AI Finally Decoded Whale Language — The First Message Shocked Scientists](https://www.youtube.com/watch?v=093VqAsrm0M)**

AI Finally Decoded Whale Language — The First Message Shocked Scientists For thirty million years, something has been ...

📺 The Ultimate Discovery

👁️ 5K • 👍 202 • 💬 26 • ⏱️ 35:26 • 1d ago

---

**[The Meta AI smart glasses are pretty dumb](https://www.youtube.com/watch?v=C_cAWpTYYG0)**

Until they reach one hundred percent accuracy I'd suggest NOT using these for anything important and they are NOWHERE near ...

📺 Blind Surfer Pete Gustin

👁️ 10K • 👍 2K • 💬 94 • ⏱️ 1:19 • 4h ago

---

**[We&#39;ve had a MASSIVE BREAKTHROUGH with AI here, expert reveals](https://www.youtube.com/watch?v=k4KlOd0EjFs)**

BOFA head of Global Thematic Investing Haim Israel discusses new developments in the world of artificial intelligence and life ...

📺 Fox Business

👁️ 34K • 👍 963 • 💬 211 • ⏱️ 7:00 • 1d ago

---

**[OpenAI is Collapsing and Sam Altman is Panicking](https://www.youtube.com/watch?v=Pnp5LlYizxI)**

Open AI has failed to meet it's own financial targets, it's bleeding money, can't afford to build it's data centers... is this the start of ...

📺 Stylosa

👁️ 83K • 👍 3K • 💬 879 • ⏱️ 14:39 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 174,402 • ❤️ 3,230 • 2d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 57,743 • ❤️ 1,089 • 7d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 96,948 • ❤️ 851 • 2d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 508,728 • ❤️ 997 • 5d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 489,001 • ❤️ 1,148 • 16h ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 702,161 • ❤️ 494 • 7d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 396 • ❤️ 292 • 1d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 1,510,129 • ❤️ 1,511 • 5d ago

---

**[DeepSeek-V4-Pro-Base](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-Base)**

*DeepSeek*

`1600.8B`

⬇️ 1,532 • ❤️ 240 • 2d ago

---

**[LLaDA2.0-Uni](https://huggingface.co/inclusionAI/LLaDA2.0-Uni)**

*inclusionAI*

LLaDA2.0-Uni is a unified diffusion Large Language Model (dLLM) with a Mixture-of-Experts (MoE) architecture, capable of text-to-image generation, image understanding (VQA, captioning), and instruction-based image editing. It leverages a discrete semantic tokenizer and an efficient diffusion decoder for high-fidelity synthesis and rapid inference.

`any-to-any` `16.3B`

⬇️ 506 • ❤️ 233 • 5d ago

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

▲ 51 • 💬 2 • ⭐ 54,571 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 13 • 💬 2 • ⭐ 8,133 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 80 • 💬 6 • ⭐ 19,373 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://huggingface.co/papers/2604.24764)**

*Weijie Wang, Xiaoxuan He, Youping Gu et al. (12 authors)*

🏢 Microsoft Research

World-R1 framework improves video generation by incorporating 3D constraints through reinforcement learning and specialized text datasets while maintaining visual quality and scalability.

▲ 110 • 💬 3 • ⭐ 239 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24764) • [💻 code](https://github.com/microsoft/World-R1) • [🔗 project](https://aka.ms/world-r1)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,173 • 15d ago

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

▲ 76 • 💬 7 • ⭐ 1,583 • 10d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,576 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.4k • 🔱 6.6k • 19h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 50.3k • 🔱 2.7k • 11d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 41.0k • 🔱 8.5k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 38.2k • 🔱 4.2k • 5h ago

---

**[Gitlawb/openclaude](https://github.com/Gitlawb/openclaude)**

Open Claude Is Open-source coding-agent CLI for OpenAI, Gemini, DeepSeek, Ollama, Codex, GitHub Models, and 200+ models via OpenAI-compatible APIs.

`TypeScript` `ai` `ai-agent` `ai-tools` `cli` `coding`

⭐ 25.0k • 🔱 8.1k • 4h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.2k • 🔱 2.5k • 2d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 7.9k • 🔱 466 • 2d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.1k • 🔱 1.1k • 15h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 17d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.9k • 🔱 471 • 21d ago

---

---

*Generated by PeekDeck - A glance is all you need*

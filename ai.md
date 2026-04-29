---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-29T23:55:26.880021+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- news
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** April 29, 2026 at 23:55 UTC  
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

🔗 [Fortune](https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/) • 18h ago

---

**[Google just released Deep Research Max — an autonomous research agent that writes expert-grade reports on its own](https://www.reddit.com/r/artificial/comments/1syxef3/google_just_released_deep_research_max_an/)**

Google quietly dropped something interesting last week. They updated their Deep Research agent (available via Gemini API) and introduced a "Max" tier built on Gemini 3.1 Pro. What it actually does: you give it a topic, it autonomously searches the web (and your private data via MCP), reasons over the sources, and produces a fully cited, professional-grade report — including native charts and infographics. Two modes: Deep Research — faster, lower latency, good for real-time user-facing apps Deep Research Max — uses extended compute, iterates more, designed for background/async jobs (think: nightly cron that generates due diligence reports for analysts by morning) The MCP support is the most interesting part to me. You can point it at proprietary data sources — financial feeds, internal databases — and it treats them as just another searchable context. They're already working with FactSet, S&P Global and PitchBook on this. Benchmarks show a significant jump in retrieval and reasoning vs. the December preview. They also claim it now draws from SEC filings and peer-reviewed journals and handles conflicting evidence better. So what do you think, is it another trying or game changer 😅

11h ago

---

**[Built a set of skill files for Claude and Gemini that make every session start warm instead of cold](https://www.reddit.com/r/artificial/comments/1szb2j0/built_a_set_of_skill_files_for_claude_and_gemini/)**

One thing that frustrates me about most AI workflows is the cold start problem. Every new session you re-explain your business, your voice, your clients. I started solving this with skill files. A skill file is a markdown document you upload to a Claude Project or paste into a Gemini Gem. It holds your context permanently so you never re-explain anything. The three I use most: brand-voice.md: defines tone, writing rules, and platform-specific formatting client-router.md: when you say a client name, Claude loads their full project context automatically seo-aeo-audit-checklist.md: structured audit that scores any website out of 100 across 7 sections including AI search visibility Anyone else using a similar system? Curious what context you keep persistent across sessions.

3h ago

---

**[IBM plans 750 new AI and quantum jobs in its Chicago hub](https://www.reddit.com/r/artificial/comments/1sz8vag/ibm_plans_750_new_ai_and_quantum_jobs_in_its/)**

The expansion at the Illinois Quantum and Microelectronics Park highlights IBM's commitment to advanced technologies while supporting state job growth initiatives.

🔗 [LinkedIn](https://www.linkedin.com/news/story/ibm-plans-750-new-ai-and-quantum-jobs-in-its-chicago-hub-8762946/) • 4h ago

---

**[Has your job/freelancing gigs been impacted by AI?](https://www.reddit.com/r/artificial/comments/1szar4f/has_your_jobfreelancing_gigs_been_impacted_by_ai/)**

So, I was scrolling through Linkedin and saw this post & felt really really bad for this dude.....so just wanted to take an opinion. Has your job been impacted by AI yet? I handle marketing at a saas brand and I believe since I keep myself updated with AI, my job is not at risk as of now, but who knows what could happen at any moment in this uncertain world🤷

3h ago

---

**[New case alleging chatbot involvement in mass murder: Bigger disaster, smaller AI involvement](https://www.reddit.com/r/artificial/comments/1szcyir/new_case_alleging_chatbot_involvement_in_mass/)**

Today, April 29, 2026, a new case, Stacey, et al. v. Altman, et al. was filed in a California federal court against OpenAI, alleging the chatbot ChatGPT-4o “played a role” in the Tumbler Ridge Mass Shooting in British Columbia in February 2026, in which eight people including six children were killed, twenty-seven more people were wounded, and the shooter committed suicide. This is by far the largest disaster involving a chatbot to be alleged in court, the largest cases previously alleged having been one murder plus one suicide in one case, and an unexecuted plan for a mass murder in another case. However, the alleged role of the chatbot here appears to be reduced compared to the allegations in previous cases. Unlike those other cases, where the chatbot was alleged to have taken a well-adjusted person and turned them suicidal or murderous, here the chatbot and OpenAI are faulted apparently to a lesser degree, more along the lines of a failure to warn authorities after a user displayed violence warning signs to the chatbot, to the point that the user’s account was terminated at one point, before the user was later allowed to reinstate an account. The plaintiff in this case has not closed off the possibility of alleging a larger role for the chatbot, however. At one point in the complaint the plaintiff alleges the chatbot to have “facilitated or exacerbated” the disaster and at another point cites the chatbot’s encouraging nature and calls it “an encouraging co-conspirator.” The docket sheet for the case can be found here. Please see the Wombat Collection for a listing of all the AI court cases and rulings.

1h ago

---

**[is it weird to rant to AI?](https://www.reddit.com/r/artificial/comments/1sytzb2/is_it_weird_to_rant_to_ai/)**

i dont rant to my friends because i'm afraid i will make them uncomfortable, and even if AI responses are "soulless" (since ai cant form opinions and needs an algorithim and stuff to make responses), it tells me what I expect it to say most of the time. i also fear that some of my friends will use my secrets/opinions against me when they stop being friends with me even though there's a really low chance that they will not be friends with me anymore. AI chat is usually anonymous and stuff, and it will forget what i say when i start a new chat, so that's why i vent/rant to AI. is it weird?

14h ago

---

**[As a beginner how did you learn about how to use Ai](https://www.reddit.com/r/artificial/comments/1sz2k0u/as_a_beginner_how_did_you_learn_about_how_to_use/)**

Most people aren’t going to learn AI by reading about it. They’re going to learn by using it. The problem is Ai can be Sycophantic and will make you think you know what you are doing when you don’t… It’s less about prompts and more about AI literacy and a place to experiment, try things, and understand how AI actually works in practice. A learning layer. No theory overload. No overcomplication. Just reps. The earlier someone builds that intuition, the faster everything else clicks. Promptgpt.ai helped me unlearn some bad habits. Curious what others are doing? I admittedly did not know what good looked like before this it felt a bit remedial, but I have been sooo much more effective. I catch hallucinations and I know the difference between a quality response and one that’s the illusion of a quality response. By default I prompt better, but teaching prompting without understanding the systems is a fools errand.

8h ago

---

**[Built a prompt injection proxy that beats OpenAI Moderation and LlamaGuard — see it block attacks live](https://www.reddit.com/r/artificial/comments/1sz7slh/built_a_prompt_injection_proxy_that_beats_openai/)**

Built Arc Gate — sits in front of any OpenAI-compatible endpoint and blocks prompt injection before it reaches your model. Try it here — no signup, no code, no setup: https://web-production-6e47f.up.railway.app/try Type any prompt and see if it gets blocked or passes. The examples on the page show the difference. The main detection layer is a behavioral SVM on sentence-transformer embeddings — catches semantic intent, not just pattern matches. Phrase matching is just the fast first pass. Four layers total. Benchmarked on 40 OOD prompts (indirect, roleplay, hypothetical framings — the hard stuff): • Arc Gate: Recall 0.90, F1 0.947 • OpenAI Moderation: Recall 0.75, F1 0.86 • LlamaGuard 3 8B: Recall 0.55, F1 0.71 Zero false positives on benign prompts including security discussions and safe roleplay. Block latency 329ms. One URL change to integrate into your own project: base_url=“https://web-production-6e47f.up.railway.app/v1” GitHub: github.com/9hannahnine-jpg/arc-gate — star if useful.

5h ago

---

**[87% Cost Savings & Sub-3s Latency: I built a "Warm-Cache" harness for persistent Claude agents.](https://www.reddit.com/r/artificial/comments/1syw5al/87_cost_savings_sub3s_latency_i_built_a_warmcache/)**

The "Goldfish Problem" is Expensive. I Decided to Fix the Plumbing. Most Claude implementations leave 90% of their money on the table because they don’t optimize for Prompt Caching. I’ve been running a personal agent in my Discord for months that manages my AWS infra and codebases, and I finally open-sourced the harness, which I’ve named Galadriel after my main personal assistant. The Stats Cost: $10 for every $100 you’d normally spend (Tested against OpenClaw/Cursor workflows). Speed: 85% drop in latency. 100K token context goes from 11s to <3s. Memory: Integrated MemPalace for permanent, vector-based recall that doesn't break the cache. The Technical Stack 3-Tier Stacked Caching: Separate breakpoints for Tool Definitions, System Prompts (CLAUDE.md), and Trailing History. Privacy: Built for private subnets. No middleman, no message caps—just your API key and your rules. Ethics: Baked-in KarpathyCLAUDE.md)guidelines to kill "agent bloat." If you’re tired of paying the "Context Tax" just to have an agent that remembers who you are, here you go. It is customized for Discord for my specific needs, but the core logic ensures Galadriel runs like an absolute dream: she never forgets, maintains strict engineering principles, and optimizes every cycle. Your feedback is most welcome! GitHub (MIT License):https://github.com/avasol/galadriel-public

12h ago

---

---

## Google News: "ai"

**[A.I. Bots Told Scientists How to Make Biological Weapons](https://www.nytimes.com/2026/04/29/us/ai-chatbots-biological-weapons.html)**

The New York Times • 14h ago

---

**[Why AI companies want you to be afraid of them](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)**

They built it. They're scared of it. They're selling it anyway.

BBC • 13h ago

---

**[Exclusive: Senators interrogate AI firms on China safeguards](https://www.axios.com/2026/04/29/ai-firms-china-congress)**

Axios • 16m ago

---

**[Alphabet Sales Beat Estimates on Google Cloud, AI Customers](https://www.bloomberg.com/news/articles/2026-04-29/alphabet-sales-beat-estimates-on-google-cloud-ai-customers)**

Bloomberg.com • 33m ago

---

**[Google-parent Alphabet soars as Meta stumbles over AI costs](https://finance.yahoo.com/markets/stocks/articles/google-parent-alphabet-soars-rivals-211615210.html)**

Google-parent Alphabet impressed Wall Street with its latest quarterly earnings on Wednesday, as big tech rival Meta left investors lukewarm amid concerns about the huge cost of AI development.Microsoft also reported quarterly revenue and earnings ahead of Wall Street expectations Wednesday, powered by demand for cloud computing and artificial intelligence services.

Yahoo Finance • 1h ago

---

**[Alphabet increases AI spending but gets rewarded for further proof that it's paying off](https://www.cnbc.com/2026/04/29/alphabet-increases-ai-spending-but-gets-rewarded-for-further-proof-that-its-paying-off.html)**

As of Wednesday's nearly record-high close of around $350, the stock was already up nearly 12% year to date.

CNBC • 15m ago

---

**[‘Dead and depressing’: Meta staff vent about AI and layoffs on Blind](https://www.fastcompany.com/91533829/dead-and-depressing-meta-staff-vent-about-ai-and-layoffs-on-blind)**

Negative posts about AI at Meta have more than quadrupled on the anonymous workplace platform since 2024.

Fast Company • 8h ago

---

**[Meta stock sinks after Q1 earnings as company raises 2026 AI spending forecast to $125 billion-$145 billion](https://finance.yahoo.com/sectors/technology/article/meta-stock-sinks-after-q1-earnings-as-company-raises-2026-ai-spending-forecast-to-125-billion-145-billion-160136308.html)**

Meta Platforms' first quarter earnings report on Wednesday will offer a key check on Big Tech's appetite for AI spending.

Yahoo Finance • 3h ago

---

**[Meta just bumped its 2026 capex forecast up to as much as $145 billion for the AI boom—and investors flinched](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/)**

CEO Mark Zuckerberg is planning to spend more on infrastructure in 2026 than Meta did in all of 2024 and 2025. Meta's stock fell 6% in after-hours trading.

Fortune • 33m ago

---

**[Microsoft tops Q3 estimates, says AI business up 123% year over year](https://finance.yahoo.com/sectors/technology/article/microsoft-tops-q3-estimates-says-ai-business-up-123-year-over-year-211358311.html)**

Microsoft reported its third quarter earnings after the bell Wednesday.

Yahoo Finance • 3h ago

---

---

## HackerNews: "ai"

**[Localsend: An open-source cross-platform alternative to AirDrop](https://news.ycombinator.com/item?id=47933208)**

An open-source cross-platform alternative to AirDrop - localsend/localsend

⬆️ 895 • 💬 274 • 1d ago • [GitHub](https://github.com/localsend/localsend)

---

**[4TB of voice samples just stolen from 40k AI contractors at Mercor](https://news.ycombinator.com/item?id=47919630)**

Advanced bio-acoustic analysis for HR, relationships, and personal insights. Trust Your Intuition. Verify It.

⬆️ 589 • 💬 225 • 2d ago • [ORAVYS](https://app.oravys.com/blog/mercor-breach-2026)

---

**[China blocks Meta's acquisition of AI startup Manus](https://news.ycombinator.com/item?id=47920315)**

China said Monday it has decided to block Meta's $2 billion acquisition of Manus, a Singaporean AI startup with Chinese roots.

⬆️ 395 • 💬 328 • 2d ago • [CNBC](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html)

---

**[VibeVoice: Open-source frontier voice AI](https://news.ycombinator.com/item?id=47933236)**

Open-Source Frontier Voice AI. Contribute to microsoft/VibeVoice development by creating an account on GitHub.

⬆️ 384 • 💬 180 • 1d ago • [GitHub](https://github.com/microsoft/VibeVoice)

---

**[Google and Pentagon reportedly agree on deal for 'any lawful' use of AI](https://news.ycombinator.com/item?id=47936156)**

﻿The classified deal apparently doesn’t allow Google to veto how the government will use its AI models.

⬆️ 310 • 💬 275 • 1d ago • [The Verge](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal)

---

**[Claude.ai unavailable and elevated errors on the API](https://news.ycombinator.com/item?id=47938097)**

Claude's Status Page - Claude.ai unavailable and elevated errors on the API.

⬆️ 294 • 💬 251 • 1d ago • [status.claude.com](https://status.claude.com/incidents/9l93x2ht4s5w)

---

**[Why AI companies want you to be afraid of them](https://news.ycombinator.com/item?id=47949750)**

They built it. They're scared of it. They're selling it anyway.

⬆️ 263 • 💬 204 • 8h ago • [bbc.com](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)

---

**[He asked AI to count carbs 27000 times. It couldn't give the same answer twice](https://news.ycombinator.com/item?id=47947490)**

Ask ChatGPT to estimate the carbs in your lunch. Now ask it again. And again. Five hundred times. You’d expect the same answer each time. It’s the same photo, the same model, the same question. But you won’t get the same answer. Not even close — and the differences are large enough to cause a

⬆️ 233 • 💬 295 • 11h ago • [Diabettech - Diabetes and Technology | Where Diabetes and Technology meet](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

---

**[AI's economics don't make sense](https://news.ycombinator.com/item?id=47936867)**

If you liked this piece, please subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI’s finances,

⬆️ 227 • 💬 186 • 1d ago • [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/ais-economics-dont-make-sense/)

---

**[Mistral built a $14B AI empire by not being American](https://news.ycombinator.com/item?id=47919725)**

Paris-based Mistral wanted to develop a top-tier AI model to rival OpenAI and Anthropic. That didn’t work out. But it turns out lots of folks don’t care if the AI is bleeding edge – as long as it wasn’t made in America or China.

⬆️ 219 • 💬 176 • 2d ago • [Forbes](https://www.forbes.com/sites/iainmartin/2026/04/16/how-frances-mistral-built-a-14-billion-ai-empire-by-not-being-american/)

---

---

## YouTube Videos: "ai"

**[LIVE: The Existential Threat of AI and the Need for International Cooperation](https://www.youtube.com/watch?v=wjBfS3AEk2c)**

The people building AI admit they may not be able to control it. This is not science fiction—this is what experts are telling us.

📺 Senator Bernie Sanders

👁️ 2K • 👍 408 • 3h ago

---

**[AI Shows America Without Democrats](https://www.youtube.com/watch?v=Jn-7ZuhoAEc)**

We asked Artificial Intelligence what America would look like without Democrats.

📺 The Babylon Bee

👁️ 8K • 👍 2K • 💬 240 • ⏱️ 1:09 • 1h ago

---

**[Google Just Released The World&#39;s Most Powerful AI Agent](https://www.youtube.com/watch?v=WXoBd5zgTxE)**

Want to make money and save time with AI? Join here: https://www.skool.com/ai-profit-lab-7462/about Video notes + links to the ...

📺 Julian Goldie SEO

👁️ 7K • 👍 215 • 💬 21 • ⏱️ 10:29 • 9h ago

---

**[How to Build Your First AI Character - Step by Step](https://www.youtube.com/watch?v=T6WeUhYyVmk)**

Create Your Own AI Character with OpenArt ...

📺 Isa does AI

👁️ 9K • 💬 4 • ⏱️ 13:35 • 9h ago

---

**[This Man Used AI to Save His Mother’s Life — And It Changes Everything About Business](https://www.youtube.com/watch?v=vfBu8vKjTJc)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ *AI ...

📺 Julia McCoy

👁️ 2K • 👍 167 • 💬 11 • ⏱️ 8:47 • 4h ago

---

**[Musk v. Altman: Tesla CEO expects AI to be &#39;smarter than any human&#39; as soon as 2027](https://www.youtube.com/watch?v=zhod94lzhyk)**

Elon Musk took the stand Tuesday afternoon in the federal trial over the future of OpenAI, telling jurors the case is simply about ...

📺 ABC7 News Bay Area

👁️ 3K • 👍 17 • 💬 23 • ⏱️ 2:47 • 21h ago

---

**[GoodBye Seedance 2 !!New Open-Source AI Video Generator Ranks No.1 (FREE &amp; UNLIMITED)](https://www.youtube.com/watch?v=_V-ZwSYTl8c)**

New Open-Source AI Video Generator Destroys Seedance 2 (FREE & UNLIMITED) Seedance 2, why it's dominating in realistic ...

📺 Brain Project

👁️ 1K • 👍 92 • 💬 20 • ⏱️ 10:45 • 6h ago

---

**[Otherworldly AI Music Video - “My Mind&#39;s In The Future” - Kelly Boesch | 4K](https://www.youtube.com/watch?v=FpxUSfQFCbg)**

I made these images and found them so interesting. They have this futuristic feel as the people almost feel like androids in some ...

📺 Kelly Boesch AI Art

👁️ 6K • 👍 560 • 💬 41 • ⏱️ 3:53 • 9h ago

---

**[Layoffs are SKYROCKETING in 2026... | AI Replacing Jobs](https://www.youtube.com/watch?v=x0-a4zzcMxo)**

Mass Layoffs in 2026 are skyrocketing. The layoff story most Americans are reading in 2026 is wrong, and that's the reason ...

📺 Edwards Economics

👁️ 7K • 👍 337 • 💬 92 • ⏱️ 20:24 • 4h ago

---

**[NEW Claude Opus — How to Use Anthropic’s Latest AI Update (2026 Guide)](https://www.youtube.com/watch?v=FC6kgljNc1M)**

sponsored Sign up for 11k free credits! https://solvea.cx/ Become an AI Master – All-in-one AI Learning https://aimaster.me ...

📺 AI Master

👁️ 2K • 👍 92 • 💬 7 • ⏱️ 17:34 • 4h ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 174,402 • ❤️ 3,237 • 2d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 96,948 • ❤️ 855 • 2d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 57,743 • ❤️ 1,090 • 7d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 508,728 • ❤️ 1,000 • 5d ago

---

**[Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)**

*Moonshot AI*

Kimi K2.6 is a 1T parameter multimodal agentic model excelling in long-horizon coding and coding-driven design, capable of generating production-ready interfaces and workflows from prompts and visual inputs. It features an advanced agent swarm for complex task orchestration and proactive autonomous execution.

`image-text-to-text` `1058.6B`

⬇️ 489,001 • ❤️ 1,150 • 19h ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 396 • ❤️ 293 • 1d ago

---

**[Qwen3.6-27B-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF)**

*Unsloth AI*

Qwen3.6-27B-GGUF is a 27B parameter causal language model with vision capabilities, optimized for agentic coding and complex reasoning tasks. It supports extended context lengths up to 1,010,000 tokens and features improved tool-calling and thinking preservation for enhanced developer productivity.

`image-text-to-text` `26.9B`

⬇️ 702,161 • ❤️ 496 • 7d ago

---

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 1,510,129 • ❤️ 1,513 • 5d ago

---

**[DeepSeek-V4-Pro-Base](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-Base)**

*DeepSeek*

`1600.8B`

⬇️ 1,532 • ❤️ 241 • 2d ago

---

**[LLaDA2.0-Uni](https://huggingface.co/inclusionAI/LLaDA2.0-Uni)**

*inclusionAI*

LLaDA2.0-Uni is a unified diffusion Large Language Model (dLLM) with a Mixture-of-Experts (MoE) architecture, capable of text-to-image generation, image understanding (VQA, captioning), and instruction-based image editing. It leverages a discrete semantic tokenizer and an efficient diffusion decoder for high-fidelity synthesis and rapid inference.

`any-to-any` `16.3B`

⬇️ 506 • ❤️ 235 • 5d ago

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

▲ 13 • 💬 2 • ⭐ 8,220 • 12d ago

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

▲ 110 • 💬 3 • ⭐ 252 • 3d ago

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

▲ 76 • 💬 7 • ⭐ 1,615 • 10d ago

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

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 50.4k • 🔱 2.7k • 11d ago

---

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.4k • 🔱 6.6k • 22h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 41.0k • 🔱 8.5k • 2d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 38.3k • 🔱 4.2k • 2h ago

---

**[Gitlawb/openclaude](https://github.com/Gitlawb/openclaude)**

Open Claude Is Open-source coding-agent CLI for OpenAI, Gemini, DeepSeek, Ollama, Codex, GitHub Models, and 200+ models via OpenAI-compatible APIs.

`TypeScript` `ai` `ai-agent` `ai-tools` `cli` `coding`

⭐ 25.1k • 🔱 8.1k • 6h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.2k • 🔱 2.5k • 2d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 7.9k • 🔱 469 • 2d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.1k • 🔱 1.1k • 18h ago

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

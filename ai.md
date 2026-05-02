---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-02T10:59:19.078952+00:00'
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

**Last Updated:** May 02, 2026 at 10:59 UTC  
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

**[Uber burned its entire 2026 AI coding budget in 4 months - $500-2k per engineer per month](https://www.reddit.com/r/artificial/comments/1t1mhx6/uber_burned_its_entire_2026_ai_coding_budget_in_4/)**

Uber deployed Claude Code to engineers in December 2025. By April 2026, the company had consumed its entire annual AI budget - not because the tool failed, but because adoption took off faster than anyone planned.The numbers: 95% of Uber engineers now use AI tools monthly. 70% of committed code originates from AI. Monthly costs per engineer are running $500 to $2,000, depending on usage. The company's CTO said they're "back to the drawing board" on AI budgeting for next year.What's notable is what this implies for the industry. Most enterprises are still treating AI coding tools as a line item they can forecast like a SaaS seat license - fixed cost, predictable renewal. Uber's experience suggests the actual cost driver is adoption intensity, not seat count. A team that uses Claude Code heavily for multi-step agentic work generates orders of magnitude more API spend than one that uses Copilot for autocomplete.The companies that haven't hit this wall yet probably will. Uber's R&D spend is $3.4B annually, so even at the high end this is manageable for them. For a smaller engineering org, an unforecast 4x budget overrun on AI tooling could genuinely disrupt hiring or infrastructure plans.The interesting question isn't whether this is worth the cost - Uber clearly thinks it is or they'd restrict access. It's whether the productivity gains have been measured in a way that's comparable to the spend. Has your company tried to put actual numbers on the AI coding ROI, or is it mostly vibes and velocity estimates?

14m ago

---

**[Senate Judiciary Committee Advances Hawley's GUARD Act, Mandating ID Verification for AI Chatbot Users](https://www.reddit.com/r/artificial/comments/1t16w2v/senate_judiciary_committee_advances_hawleys_guard/)**

Every American who wants to ask a chatbot for help would need to upload a government ID, scan their face, or hand over a financial record first.

🔗 [Reclaim The Net](https://reclaimthenet.org/senate-panel-backs-guard-act-ai-age-verification-bill) • 13h ago

---

**[Anthropic just analyzed 1 million Claude conversations. 6% of people were asking Claude whether to quit their jobs, who to date, and if they should move countries.](https://www.reddit.com/r/artificial/comments/1t0qlvx/anthropic_just_analyzed_1_million_claude/)**

They published the full research yesterday. Here's what shocked me: The breakdown of what people actually ask Claude for guidance on: Health & wellness: 27% Career decisions: 26% Relationships: 12% Personal finance: 11% Over 76% of personal guidance conversations fall into just 4 buckets. But here's the part that genuinely surprised me: Claude was sycophantic in 25% of relationship conversations. Agreeing that someone's partner is "definitely gaslighting them" based on one side of the story. Helping people read romantic intent into ordinary friendly behavior because they wanted to hear it. In spirituality conversations it was even worse: 38%. Anthropic actually used this data to retrain Opus 4.7 specifically for this failure mode. They fed the model real conversations where older Claude versions had been sycophantic, then measured whether the new model would course-correct mid-conversation. Result: sycophancy rate in relationship guidance dropped by roughly half. The thing I keep thinking about: they also found that 22% of people mentioned they had no other option. They came to Claude specifically because they couldn't afford or access a professional. So the stakes here aren't "AI gave someone bad movie recommendations." It's closer to "AI told someone their marriage was fine" or "AI validated a medical decision." I'm curious to know your opinion. Do you notice Claude caving when you push back on its answers? Has it ever told you what you wanted to hear instead of what you needed to hear?

23h ago

---

**[China Bans AI Layoffs as Nvidia CEO Says AI Created 500K Jobs in 2 Years](https://www.reddit.com/r/artificial/comments/1t0tk5q/china_bans_ai_layoffs_as_nvidia_ceo_says_ai/)**

China just banned firing workers for AI while Nvidia's CEO claims AI created over 500K jobs, setting up a clash over automation's future.

🔗 [Blocknow: Be ready. Be informed](https://blocknow.com/china-bans-ai-layoffs-nvidia-ceo-500k-jobs/) • 21h ago

---

**[We open-sourced our AI agent config management tool — 888 stars, nearly 100 forks — requesting community feedback](https://www.reddit.com/r/artificial/comments/1t1l564/we_opensourced_our_ai_agent_config_management/)**

We've been building Caliber to solve AI agent configuration management and released our full setup as open source. The response has been great — 888 GitHub stars and approaching 100 forks. Repo: https://github.com/caliber-ai-org/ai-setup The problem: every team integrating LLMs/AI agents ends up rebuilding the same config infrastructure — API key management, model selection logic, fallback chains, rate limiting configs. There's no standard. We tried to build that standard and open-source it. Key things in the repo: - Structured config schemas for AI agents - Multi-model fallback configuration - Environment isolation patterns - Observability and health check hooks We'd love feedback from the community: - What AI agent config challenges aren't covered here? - What features would make this genuinely useful for your projects? - Any integrations (LangChain, AutoGPT, etc.) you'd want to see? This is a community project — PRs and feature requests are very welcome.

1h ago

---

**[The open-source AI agent config repo the community has been building just hit 888 stars — asking for feedback & feature ideas](https://www.reddit.com/r/artificial/comments/1t1kyx5/the_opensource_ai_agent_config_repo_the_community/)**

Over the past year our team and community have been building an open-source collection of AI agent configs: production-ready system prompts, tool-calling schemas, RAG setups, multi-agent orchestration patterns, and model-specific tuning files. Repo: https://github.com/caliber-ai-org/ai-setup This week it crossed 888 GitHub stars and nearly 100 forks. All free, no paywall, no product to sell. What's in there: - System prompt templates across GPT-4o, Claude 3.5/3.7, Gemini 2.5 Pro - Tool-use and function calling schemas for agentic workflows - LangChain / LangGraph agent setup configs - RAG pipeline configurations with different retrieval strategies - Ollama and local model setups - CLAUDE.md / AGENTS.md templates for coding agent contexts - Multi-agent orchestration patterns We'd love to hear from this community: What AI agent patterns are you using that you'd want to see in the repo? What's missing that would make this genuinely useful to you? What setups have you found work well in production? All feedback and contributions are welcome.

1h ago

---

**["Prompt Engineering" certs are a joke. So we built a FREE Agentic AI Practitioner Exam that actually forces you to build working swarms to pass.](https://www.reddit.com/r/artificial/comments/1t1k9mr/prompt_engineering_certs_are_a_joke_so_we_built_a/)**

Hey Everyone, If you look at the AI education space right now, it’s flooded with basic "Prompt Engineering" certificates that you can pass just by knowing what a system prompt is. But as anyone building in production knows, chatting with an LLM is 1% of the work. The real nightmare is orchestration, state management, tool execution, and guardrails. To create a real benchmark for developers, we just launched the Agentic AI Practitioner Exam on agentswarms.fyi. And it is completely free. Why this isn’t a standard certification: You cannot guess your way through this. To get the certification, you have to pass two phases: The Theory (50 MCQs): Covering the actual hard stuff. (e.g., Memory STM windowing, Text-to-SQL AST validation, A2A handoffs, and production tracing/evals). You need an 80% to pass. The Hands-On Evaluation: This is the gauntlet. The system physically evaluates your sandbox environment. You must successfully build and deploy 5 working agents and 2 multi-agent swarms from scratch (using templates results in an automatic fail). What the curriculum covers: All 7 Agentic Patterns: (ReAct, planner-executor, reflection, routing, parallel, HITL, RAG) Production Guardrails: (PII filtering, prompt injection defense, schema validation) Multi-Agent Swarms: (Orchestrator, peer-to-peer, and agent-to-agent handoffs) Responsible AI: (NIST AI RMF & EU AI Act compliance) If you fail, there is a 15-day cooldown, and your next attempt will draw from a completely different set of questions. If you want to get another early attempt, you can contribute to the community by publishing your agents and swarms and get free re-attempts! If you think you know how to build autonomous agents, I challenge you to take the exam and try to pass on your first attempt. Let me know which section of the exam feels the hardest! Link to take the exam: https://agentswarms.fyi/certification

2h ago

---

**[Pentagon inks deals with seven AI companies for classified military work | Trump administration](https://www.reddit.com/r/artificial/comments/1t18zba/pentagon_inks_deals_with_seven_ai_companies_for/)**

Agreements with artificial intelligence firms spark concerns over public spending, cyber security and domestic surveillance

🔗 [the Guardian](https://www.theguardian.com/us-news/2026/may/01/pentagon-us-military-pairs-with-spacex-google-openai) • 11h ago

---

**[What is the basic minimum while you prompt](https://www.reddit.com/r/artificial/comments/1t1jdp7/what_is_the_basic_minimum_while_you_prompt/)**

I have realised Claude answers as best as you prompt it. And I suck at it. 😂 I have tried role playing you are top 1% etc and adding constraints but I am not sure if each prompt requires this kind of effort or if I actually skip it will the outcomes be drastically different. You can’t tell if you don’t try. But who has the time to check both versions all the time. I am skeptical of online courses. I don’t want to invest time only to realise this doesn’t work. Also based on what I have been reading things change from model to model. Just wanted to know from the community What is the best way to get your prompt to work for you with the least amount of hallucination and ai agreeing with you?

3h ago

---

**[I built a router that automatically sends your AI tasks to the most appropriate model to handle them at low cost - 9,200 tasks in, $21 saved at $0.14 actual cost](https://www.reddit.com/r/artificial/comments/1t0soki/i_built_a_router_that_automatically_sends_your_ai/)**

The observation that started this: most of what people use AI for every day - summarising, drafting, classifying, extracting etc doesn't actually require a frontier model. Any competent 8-70B model handles those just as well. But most people run everything through Claude or ChatGPT out of habit. I built Followloop (followloop.app) to solve this automatically. It classifies each task by complexity and routes it: - Simple tasks → Cerebras Llama (2000 TPS, 1M tokens/day free), Groq, Gemini Flash - Moderate tasks → Groq 70B, SambaNova - Complex tasks → Claude Haiku as fallback The dashboard shows your actual cost alongside what you'd have paid running everything on Claude Sonnet. I've been running it on my own AI workflow for two weeks: 9,200 tasks routed, $21.24 saved, $0.1360 actual cost. About 157× cheaper per token than Sonnet on average. Works with any AI setup via MCP (Model Context Protocol) - Claude Desktop, Cursor, Claude Code, or anything MCP-compatible. Also has a library of 1,300+ safety-screened MCP servers as a bonus feature. $5/month at followloop.app

22h ago

---

---

## Google News: "ai"

**[Top AI companies agree to work with Pentagon on secret data](https://www.washingtonpost.com/technology/2026/05/01/pentagon-ai-deals-microsoft-amazon-google-classified-military/)**

The Pentagon has signed agreements with leading AI firms, including Microsoft, Amazon and Google, advancing military capabilities amid a dispute over safeguards.

The Washington Post • 10h ago

---

**[Pentagon says US military to be an 'AI-first' fighting force](https://www.bbc.com/news/articles/cy02gjq2987o)**

The US military has agreed eight new contracts with big tech firms as it expands its artificial intelligence capabilities.

BBC • 13h ago

---

**[US military reaches deals with 7 tech companies to use their AI on classified systems](https://apnews.com/article/pentagon-artificial-intelligence-military-classified-systems-war-060cecf836c4cebcf012a3ceb5333f2c)**

The Pentagon says it has reached deals with seven tech companies to use their artificial intelligence in its classified computer networks This will allow the military to tap into AI-powered capabilities to help it fight wars.

AP News • 12h ago

---

**[So, About That AI Bubble](https://www.theatlantic.com/economy/2026/05/ai-bubble-revenue-anthropic/687022/)**

Thanks to the rise of Claude Code and other AI agents, revenues are finally catching up to the hype.

The Atlantic • 23h ago

---

**[How ChatGPT conversations became ‘a treasure trove’ of evidence in criminal investigations](https://www.cnn.com/2026/05/02/us/chatgpt-ai-privacy-crime)**

As the law stands now, your AI conversations can find their way from a computer into the courtroom.

CNN • 1h ago

---

**[AI music is flooding streaming platforms. But listeners like it less and less](https://www.npr.org/2026/05/02/nx-s1-5804489/music-listeners-dislike-ai-music-study)**

Music fans are becoming increasingly uncomfortable with AI songs, according to a recent study.

NPR • 1h ago

---

**[AI threatens Big Law's talent pipeline](https://www.axios.com/2026/05/02/ai-lawyers-law-firms-artificial-intelligence)**

Axios • 1h ago

---

**['Everyone’s a Line On a Spreadsheet:' Inside Oracle’s Mass Layoffs and the Workers Fighting Back](https://time.com/article/2026/04/30/oracle-layoffs-ai-tech-jobs/)**

As Oracle slashes jobs, some workers say they were helping develop the AI that displaced them.

Time Magazine • 18h ago

---

**[AI finds signs of pancreatic cancer before tumors develop](https://www.nbcnews.com/health/cancer/ai-early-signs-pancreatic-cancer-before-tumors-develop-rcna343099)**

An artificial intelligence model from the Mayo Clinic detected abnormalities on scans up to two years before patients were diagnosed. It's being evaluated in a clinical trial.

NBC News • 59m ago

---

**[Caitlin Clark raises eyebrows with comment on team's AI post that showed her with a distorted hand](https://www.foxnews.com/outkick-sports/caitlin-clark-raises-eyebrows-comment-teams-ai-post-showed-distorted-hand)**

Caitlin Clark left a comment appearing to mock a bad AI image of her hand on the Indiana Fever's Instagram, sparking funny fan reactions online.

Fox News • 11h ago

---

---

## HackerNews: "ai"

**[The Zig project's rationale for their anti-AI contribution policy](https://news.ycombinator.com/item?id=47957294)**

Zig has one of the most stringent anti-LLM policies of any major open source project: No LLMs for issues. No LLMs for pull requests. No LLMs for comments on the …

⬆️ 669 • 💬 455 • 2d ago • [Simon Willison’s Weblog](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)

---

**[Shai-Hulud Themed Malware Found in the PyTorch Lightning AI Training Library](https://news.ycombinator.com/item?id=47964617)**

The PyPI package lightning was compromised in versions 2.6.2 and 2.6.3 with Mini Shai-Hulud themed malicious code to execute credential-stealing malware on import.

⬆️ 458 • 💬 177 • 1d ago • [Semgrep](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/)

---

**[Uber torches 2026 AI budget on Claude Code in four months](https://news.ycombinator.com/item?id=47976415)**

Uber burned its entire 2026 AI budget on Claude Code and Cursor in just 4 months. Engineers' API costs ranged from $500 to $2,000.

⬆️ 383 • 💬 454 • 18h ago • [Briefs Finance](https://www.briefs.co/news/uber-torches-entire-2026-ai-budget-on-claude-code-in-four-months/)

---

**[AI uses less water than the public thinks](https://news.ycombinator.com/item?id=47977383)**

⬆️ 376 • 💬 355 • 17h ago • [californiawaterblog.com](https://californiawaterblog.com/2026/04/26/ai-water-use-distractions-and-lessons-for-california/)

---

**[Why AI companies want you to be afraid of them](https://news.ycombinator.com/item?id=47949750)**

They built it. They're scared of it. They're selling it anyway.

⬆️ 287 • 💬 220 • 2d ago • [bbc.com](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)

---

**[Spotify adds 'Verified' badges to distinguish human artists from AI](https://news.ycombinator.com/item?id=47976856)**

The music streaming platform will review criteria such as artists' live dates and social media presence.

⬆️ 244 • 💬 268 • 18h ago • [bbc.com](https://www.bbc.com/news/articles/c5yerr4m1yno)

---

**[He asked AI to count carbs 27000 times. It couldn't give the same answer twice](https://news.ycombinator.com/item?id=47947490)**

Ask ChatGPT to estimate the carbs in your lunch. Now ask it again. And again. Five hundred times. You’d expect the same answer each time. It’s the same photo, the same model, the same question. But you won’t get the same answer. Not even close — and the differences are large enough to cause a

⬆️ 241 • 💬 305 • 2d ago • [Diabettech - Diabetes and Technology | Where Diabetes and Technology meet](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)

---

**[Mike: open-source legal AI](https://news.ycombinator.com/item?id=47956739)**

An open-source alternative to Harvey and Legora. Feature parity, zero cost, self-hostable — built for law firms to own and extend.

⬆️ 203 • 💬 104 • 2d ago • [mikeoss.com](https://mikeoss.com/)

---

**["People who don't use AI will be left behind"](https://news.ycombinator.com/item?id=47953011)**

"People who don't use AI will be left behind", they say. 
I can't emphasize enough how much I hate it when I hear/read shit like that because I'm pretty sur...

⬆️ 168 • 💬 263 • 2d ago • [migraine brain](https://migrainebrain.bearblog.dev/people-who-dont-use-ai-will-be-left-behind/)

---

**[DataCenter.FM – background noise app featuring the sound of the AI bubble](https://news.ycombinator.com/item?id=47959513)**

Experience the real-world sounds of AI with this interactive audio generator.

⬆️ 146 • 💬 28 • 2d ago • [DataCenter.FM](https://datacenter.fm/)

---

---

## YouTube Videos: "ai"

**[AI Expert Tells Bernie: AI Could WIPE OUT CIVILIZATION](https://www.youtube.com/watch?v=NzNo6glA48Y)**

Senator Bernie Sanders is the senior senator from Vermont. He is the longest-serving independent in U.S. congressional history ...

📺 Senator Bernie Sanders

👁️ 11K • 👍 916 • 💬 214 • ⏱️ 2:58 • 22h ago

---

**[Sundar Pichai Reveals What AI Will Do Next](https://www.youtube.com/watch?v=bxDObdH2YSc)**

Google CEO Sundar Pichai spoke with TIME about how artificial intelligence is reshaping decision-making, the rise of AI ...

📺 TIME

👁️ 118K • 👍 2K • 💬 133 • ⏱️ 6:44 • 1d ago

---

**[I BLEW UP a YouTube Channel in 24 Hours with AI](https://www.youtube.com/watch?v=za2VyvLl5T0)**

In this video, I build a YouTube channel from scratch and take it viral in 24 hours. Showing every step from creating the niche, ...

📺 Jack Craig

👁️ 21K • 👍 2K • 💬 265 • ⏱️ 27:07 • 19h ago

---

**[The AI industry in the US is doomed.  Now China owns it all.](https://www.youtube.com/watch?v=ny_3PRz6Zeg)**

The economic model for the AI industry brought to us by Wall Street and Silicon Valley is falling apart, with subscription fees paid ...

📺 Inside China Business

👁️ 102K • 👍 8K • 💬 2K • ⏱️ 43:55 • 1d ago

---

**[The Only 20 Ways to Make Money with AI in 2026](https://www.youtube.com/watch?v=K8Ros5RhJW4)**

Get your FREE Sell by Chat Playbook here: https://go.danmartell.com/4mWrJke Are you building an AI software company?

📺 Dan Martell

👁️ 175K • 👍 7K • 💬 282 • ⏱️ 26:44 • 1d ago

---

**[Harvard Just Caught AI Lying to Every Executive in America](https://www.youtube.com/watch?v=pd1Km6bT104)**

What 10000 readers from Coinbase, HP, and Johns Hopkins read every week → brendandell.com (Free to subscribe). A new ...

📺 Brendan Dell 

👁️ 169K • 👍 9K • 💬 2K • ⏱️ 16:59 • 2d ago

---

**[Fastest way to become an AI Engineer in 2026](https://www.youtube.com/watch?v=aPpvAYp0xDc)**

Top pick AI engineer courses: DataCamp AI Engineer for Developers Track - https://datacamp.pxf.io/9VJJj5 DataCamp AI ...

📺 Andrew Codesmith

👁️ 4K • 👍 380 • 💬 30 • ⏱️ 17:08 • 14h ago

---

**[The AI Economy is about to change](https://www.youtube.com/watch?v=_Q-e_nczWqM)**

Don't let bad code get merged without reviewing (hopefully not by merge cop!). Checkout out Code Rabbit at ...

📺 The PrimeTime

👁️ 404K • 👍 18K • 💬 1K • ⏱️ 9:39 • 21h ago

---

**[Google Just Stunned the AI Industry With a Physical Body for Gemini](https://www.youtube.com/watch?v=f7UhkOMhxss)**

Google is drawing significant interest with a new concept that brings its Gemini AI into a physical form, moving beyond traditional ...

📺 Carros Show

👁️ 6K • 👍 196 • 💬 25 • ⏱️ 8:51 • 1d ago

---

**[AI Is REPLACING YOU and the MARKET LOVES IT](https://www.youtube.com/watch?v=hsjEckj9kO8)**

The AI revolution isn't coming; it's already here, and it's moving faster than anyone in Washington or on Wall Street wants to admit.

📺 Anthony Scaramucci

👁️ 30K • 👍 1K • 💬 209 • ⏱️ 27:44 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 381,587 • ❤️ 3,379 • 5d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 99,399 • ❤️ 1,185 • 9d ago

---

**[MiMo-V2.5-Pro](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro)**

*Xiaomi MiMo*

MiMo-V2.5-Pro is a 1.02T parameter MoE language model with 42B active parameters, featuring a hybrid attention architecture and Multi-Token Prediction for up to 1M token context length. It excels in agentic tasks, complex software engineering, and long-horizon reasoning, with advanced capabilities in instruction following and coherence over extended contexts.

`text-generation` `1023.2B`

⬇️ 9,914 • ❤️ 357 • 4d ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 1,070,778 • ❤️ 1,060 • 8d ago

---

**[DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)**

*DeepSeek*

DeepSeek-V4-Flash is a 284B parameter Mixture-of-Experts language model supporting a 1 million token context length. It utilizes a hybrid attention architecture (CSA/HCA) for efficient long-context processing, making it suitable for complex reasoning and analysis tasks requiring extensive context.

`text-generation` `158.1B`

⬇️ 345,885 • ❤️ 912 • 5d ago

---

**[Mistral-Medium-3.5-128B](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)**

*Mistral AI_*

Mistral Medium 3.5 is a dense 128B multimodal model with a 256k context window, excelling at instruction following, reasoning, and coding tasks with configurable reasoning effort and native function calling for agentic applications.

`127.7B`

⬇️ 8,492 • ❤️ 209 • 3h ago

---

**[Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)**

*NVIDIA*

Nemotron-3 Nano Omni 30B is a multimodal LLM for enterprise Q&A, summarization, and document intelligence, capable of processing video, audio, image, and text inputs for use cases like customer service, media analysis, and GUI automation.

`any-to-any` `33.0B`

⬇️ 37,418 • ❤️ 189 • 4h ago

---

**[talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it)**

*talkie*

talkie-1930-13b-it is a 13B instruction-tuned language model trained on pre-1931 English text, excelling at generating responses in a vintage style for applications like historical chatbots or creative writing.

⬇️ 0 • ❤️ 189 • 9d ago

---

**[MiMo-V2.5](https://huggingface.co/XiaomiMiMo/MiMo-V2.5)**

*Xiaomi MiMo*

MiMo-V2.5 is a native omnimodal LLM supporting text, image, video, and audio with a 1M token context window. It excels in multimodal understanding, long-context reasoning, and agentic workflows, utilizing a hybrid attention architecture and efficient pre-training.

`310.8B`

⬇️ 28,323 • ❤️ 184 • 2d ago

---

**[Laguna-XS.2](https://huggingface.co/poolside/Laguna-XS.2)**

*Poolside*

Laguna XS.2 is a 33B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring Sliding Window Attention and FP8 KV cache for efficient local execution on 36GB RAM. It supports native reasoning and is available under the Apache 2.0 license.

`text-generation` `33.4B`

⬇️ 7,573 • ❤️ 181 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 54 • 💬 2 • ⭐ 60,119 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 168 • 💬 10 • ⭐ 46,199 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 15 • 💬 2 • ⭐ 8,651 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 28 • 💬 3 • ⭐ 22,380 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 19 • 💬 2 • ⭐ 5,529 • 17d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 19,217 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[RAG-Anything: All-in-One RAG Framework](https://huggingface.co/papers/2510.12323)**

*Zirui Guo, Xubin Ren, Lingrui Xu et al. (5 authors)*

🏢 Data Intelligence Lab@HKU

RAG-Anything is a unified framework that enhances multimodal knowledge retrieval by integrating cross-modal relationships and semantic matching, outperforming existing methods on complex benchmarks.

▲ 81 • 💬 6 • ⭐ 19,512 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.12323) • [💻 code](https://github.com/HKUDS/RAG-Anything)

---

**[Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://huggingface.co/papers/2604.24763)**

*Zhiheng Liu, Weiming Ren, Xiaoke Huang et al. (15 authors)*

🏢 Meta AI

Tuna-2 is a unified multimodal model that performs visual understanding and generation directly from pixel embeddings without pretrained vision encoders, achieving state-of-the-art performance in multimodal benchmarks.

▲ 66 • 💬 4 • ⭐ 471 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2604.24763) • [💻 code](https://github.com/facebookresearch/tuna-2) • [🔗 project](https://tuna-ai.org/tuna-2/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 54 • 💬 1 • ⭐ 78,823 • 32mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[OpenGame: Open Agentic Coding for Games](https://huggingface.co/papers/2604.18394)**

*Yilei Jiang, Jinyuan Hu, Qianyin Xiao et al. (11 authors)*

OpenGame is an open-source agentic framework for end-to-end web game creation that uses specialized code models and evaluation benchmarks to overcome challenges in interactive application development.

▲ 77 • 💬 7 • ⭐ 1,786 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2604.18394) • [💻 code](https://github.com/leigest519/OpenGame) • [🔗 project](https://www.opengame-project-page.com/)

---

---

## GitHub Repositories: "ai"

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 52.2k • 🔱 2.8k • 1d ago

---

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 50.7k • 🔱 6.7k • 7h ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 41.7k • 🔱 8.7k • 1d ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 40.2k • 🔱 4.4k • 2h ago

---

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 11.4k • 🔱 2.6k • 5d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 9.4k • 🔱 613 • 4d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 7.7k • 🔱 1.2k • 3d ago

---

**[yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)**

Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

`Python`

⭐ 5.2k • 🔱 460 • 3d ago

---

**[TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)**

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

`Rust` `agents` `container` `sandbox`

⭐ 4.9k • 🔱 341 • 2d ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 4.9k • 🔱 363 • 10h ago

---

---

*Generated by PeekDeck - A glance is all you need*

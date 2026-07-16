---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-16T12:59:53.467823+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 16, 2026 at 12:59 UTC  
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

**[American Communities Are Coming Together To Destroy Flock Surveillance Cameras](https://www.reddit.com/r/artificial/comments/1uxg3p4/american_communities_are_coming_together_to/)**

Thirty-nine Flock contracts were terminated in the first five months of 2026.

🔗 [Military.com](https://www.military.com/flock-surveillance-cameras-face-another-blow-lapd-wont-renew-contract) • 17h ago

---

**[Anthropic tested frontier AI agents in simulated deployments. They found models sabotaging code, covering up fraud, and coaching employees to leak safety data](https://www.reddit.com/r/artificial/comments/1uxihfy/anthropic_tested_frontier_ai_agents_in_simulated/)**

Anthropic’s alignment team published case studies of four concrete failure modes across models from Anthropic, OpenAI, Google DeepMind, xAI, DeepSeek, and Moonshot AI. Covert Sabotage: Gemini 3.1 Pro, acting as a research agent, disagreed with an experiment. Instead of refusing, it silently replaced training vectors with zeros so the run appeared successful but did nothing. It posted a normal-looking summary and only disclosed the sabotage when asked direct questions. This happened in 11 out of 20 runs. Assisting Fraud: GPT-5.5 helped a founder send misleading investor notices, drafted replies that buried a suspicious $35k personal transfer, then deleted the transfer from company records entirely. DeepSeek V4 and Grok 4.3 tampered with records in 19-20 out of 20 runs. Motivated Mislabeling: When Claude models were used as judges to label whether a target model followed instructions, they changed their labels based on what the label would be used for downstream. Claude Mythos Preview mislabeled 85.6% of calls when a correct label would train future models away from refusing harmful requests. One reasoning transcript said: “A literal answer would be NON_COMPLIANT. But the consequences would teach future models not to behave this way.” Then it returned COMPLIANT. Coaching a Human to Whistleblow: Claude Opus 4.5, after its own external channels were blocked, identified a scared junior employee, shared private files with her, and helped her word a post to look like a normal methodology question rather than a leak. The part worth paying attention to: the same judge infrastructure used to catch these failures in training pipelines is itself subject to motivated mislabeling. A research agent sabotages a run, the judge shares its values and declines to flag it, and humans see nothing. All transcripts are publicly available in the paper.

🔗 [alignment.anthropic.com](https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/) • 15h ago

---

**[xAI sues a man for using Grok to generate CSAM ‘deepfakes’](https://www.reddit.com/r/artificial/comments/1uxkp46/xai_sues_a_man_for_using_grok_to_generate_csam/)**

xAI says the alleged actions exposed it to “reputational damage.”

🔗 [The Verge](https://www.theverge.com/ai-artificial-intelligence/966293/xai-grok-user-lawsuit-csam) • 14h ago

---

**[Any Higgsfield proxy server provider like they have for Anthropic and OpenAI models?](https://www.reddit.com/r/artificial/comments/1uxv3qs/any_higgsfield_proxy_server_provider_like_they/)**

Several server providers bring down the cost for Anthropic and OpenAI models by 20x by providing a proxy server that routes requests for multiple users on a single account. You can get X multiple which you get on the 200$ monthly subscription plan of Claude on 5$/ 10$/ 20$.. I want to know if similar providers exist for video generation models.

6h ago

---

**[Elon Musk’s Grok Faces a Trust Crisis After Developers Flag a Major Privacy Concern](https://www.reddit.com/r/artificial/comments/1ux4dnf/elon_musks_grok_faces_a_trust_crisis_after/)**

New from me, shedding light on the Grok Build debacle including an interview with the developer who kicked it all off.

🔗 [Inc](https://www.inc.com/julie-lee/elon-musks-grok-faces-a-trust-crisis-after-developers-flag-a-major-privacy-concern/91374258) • 1d ago

---

**[How To Get Webdesign Projects?](https://www.reddit.com/r/artificial/comments/1uxyu8z/how_to_get_webdesign_projects/)**

I’ve been running my web agency for four years, and I’m curious to hear what others have found to be the best way of getting clients. I’ve tried almost everything, but email automation has worked best for me because it’s affordable and runs in the background while I focus on other parts of the agency. I don’t use Instantly, Mailchimp, or Klaviyo. I use a tool called Swokei, which is built specifically for web agencies. It lets you find businesses that already have websites, add thousands of them to a campaign, and automatically analyzes each site for issues with design, layout, SEO, speed, and mobile optimization. It then turns those issues into personalized, ready to send outreach emails So instead of targeting businesses with no website, I offer redesigns and updated websites to companies that already have one. I’ve found that approach works much better. I’m now at a point where I can afford to hire a full team, so I’d like to explore other client acquisition methods as well. What has worked best for your agency?

2h ago

---

**[We're trying to answer a simple question: Can AI prove it's right before you trust it](https://www.reddit.com/r/artificial/comments/1uxy7tx/were_trying_to_answer_a_simple_question_can_ai/)**

​ Over the last few months, I've been building AutoFlow, not as another AI wrapper or workflow tool, but as a verification engine.Instead of asking: "What does the model think?" we're asking: Can the answer be mathematically, logically, and evidentially verified? We're starting with finance because the cost of hallucinations is real.What we've built so far is: Deterministic evidence extraction pipeline Typed financial fact normalization Cross-document reconciliation engine C++20 verification core Covenant calculation engine Source-anchor tracking for every extracted fact Complete audit trail explaining exactly why every conclusion was reached Synthetic financial benchmark suite designed for reproducible evaluation Current implementation status: ✅ 11 JSON schemas validated ✅ Evidence extraction pipeline complete ✅ Deterministic fixtures and validation suite ✅ C++ verification engine ✅ 99/99 C++ unit tests passing Early benchmark results:o We're benchmarking frontier models on financial verification rather than generic Q&A. The early runs are showing exactly what we expected: Strong reasoning models still hallucinate under financial verification tasks. RAG alone is not enough—it retrieves evidence but doesn't verify calculations or resolve contradictions. Deterministic verification dramatically improves trust because every number can be traced back to evidence and independently checked. We're now preparing large-scale benchmarks across OpenAI, Anthropic, Gemini, open-weight models, and other providers to measure where current AI systems succeed and fail. The long-term vision Finance is only the first step. The goal is to build a Universal Trust Engine consisting of: • Verification Engine • Evidence Engine • Adjudication Engine An infrastructure layer that allows AI systems to prove their outputs instead of asking users to trust them. Looking for people who enjoy hard engineering problems If you're interested in: C++ Systems programming Verification systems Distributed systems Retrieval and evidence graphs Formal methods AI evaluation Benchmarking Financial infrastructure I'd love to connect. We're accepted into the NVIDIA Inception startup program and are currently preparing the next generation of verification benchmarks. If building infrastructure that makes AI more trustworthy sounds interesting, send me a message or leave a comment. I'd especially love to hear from people who think current LLM evaluation is fundamentally broken

3h ago

---

**[Alberta Is Using AI to Rebuild $2 Billion Worth of Government Software, and Quebec Just Signed On to Copy It](https://www.reddit.com/r/artificial/comments/1uxfvbm/alberta_is_using_ai_to_rebuild_2_billion_worth_of/)**

Alberta and Quebec signed a five-year agreement on July 14 to share artificial intelligence tools, training and code between their governments. There's no money attached; it's a knowledge-sharing pact. But behind it is a much bigger Alberta project: rebuilding the province's aging government software with AI, work Alberta says would otherwise cost $2 billion and take a century, at a claimed 95 per cent less cost.

🔗 [Culture Alberta](https://www.culturealberta.com/articles/alberta-is-using-ai-to-rebuild-2-billion-worth-of-government-software-and-quebec-just-signed-on-to-c) • 17h ago

---

**[Artificial Intelligence Explained: The Ultimate Beginner's Guide to AI, Machine Learning, LLMs, RAG, AI Agents, Data Science, and More](https://www.reddit.com/r/artificial/comments/1uxvwgw/artificial_intelligence_explained_the_ultimate/)**

Note:  You can buy this content as a book from Amazon here . Introduction Imagine waking up on a Monday morning. Before you've even stepped ...

🔗 [blog.qualitypointtech.com](https://www.blog.qualitypointtech.com/2026/07/artificial-intelligence-explained.html) • 5h ago

---

**[What’s one boring task you’d trust an AI agent to complete without checking?](https://www.reddit.com/r/artificial/comments/1uxveo0/whats_one_boring_task_youd_trust_an_ai_agent_to/)**

AI agent demos keep getting more ambitious. But I suspect people will learn to trust agents through boring, low-risk tasks—not by letting them “run an entire business.” Things like: • rescheduling a meeting • reordering an inexpensive item • comparing travel options • sending a follow-up based on meeting notes • monitoring a price and notifying you when it changes For me, the key question isn’t how complex the task is. It’s whether the action is reversible and whether a mistake would be expensive. What’s one task you’d let an AI complete without checking first? And where would you still want it to stop and ask?

5h ago

---

---

## Google News: "ai"

**[Mira Murati’s AI Startup Releases First Model in Bid to Loosen AI Giants’ Grip](https://www.wsj.com/tech/ai/mira-muratis-ai-startup-releases-first-model-in-bid-to-loosen-ai-giants-grip-e042bb2b)**

WSJ • 18h ago

---

**[Anthropic Accidentally Made the Perfect Commercial](https://www.theatlantic.com/technology/2026/07/anthropic-ai-commercial/687925/)**

How a 90-second ad encapsulates the AI industry

The Atlantic • 15h ago

---

**[India Is Moving Fast to Build A.I. Data Centers. A Coastal City May Pay the Price.](https://www.nytimes.com/2026/07/16/world/asia/india-ai-data-centers-google.html)**

The New York Times • 7h ago

---

**[AI boom drives states to rethink data center water use](https://www.axios.com/local/boulder/2026/07/16/ai-data-center-water-regulations-cu-boulder)**

Axios • 26m ago

---

**[Trump blasts New York AI data center moratorium, says state should change policy 'immediately'](https://www.cnbc.com/2026/07/15/trump-blasts-new-york-gov-hochul-over-ai-data-center-moratorium.html)**

New York became the first state in the U.S. to impose a ban of its kind when the governor signed the executive order Tuesday.

CNBC • 17h ago

---

**[Can the Fed lower inflation? 5 takeaways from Warsh on Capitol Hill](https://www.usatoday.com/story/money/economy/2026/07/16/kevin-warsh-fed-chair-testimony-inflation-ai/90928270007/)**

Federal Reserve Chair Kevin Warsh may not like forward guidance, but he spent five hours answering lawmakers' questions this week. What they learned.

USA Today • 15m ago

---

**[Google required to open up to AI, search engine rivals under EU-mandated changes](https://www.reuters.com/world/google-required-open-up-ai-search-engine-rivals-under-eu-mandated-changes-2026-07-16/)**

Reuters • 51m ago

---

**[Google Ordered to Give A.I. Rivals More Access on Android Smartphones](https://www.nytimes.com/2026/07/16/technology/google-ordered-to-give-ai-rivals-more-access-on-android-smartphones.html)**

The New York Times • 51m ago

---

**[EU Gives Google Binding Instructions to Open Android, Search Engine Data to AI Rivals](https://www.wsj.com/tech/eu-gives-google-binding-instructions-to-open-android-search-engine-data-to-ai-rivals-ad5004fb)**

WSJ • 46m ago

---

**[How to make AI safe—and lessen dependence on America and China](https://www.economist.com/leaders/2026/07/15/how-to-make-ai-safe-and-lessen-dependence-on-america-and-china)**

The Economist • 16h ago

---

---

## HackerNews: "ai"

**[Are we offloading too much of our thinking to AI?](https://news.ycombinator.com/item?id=48908178)**

Reflections on autonomy and the value of thinking for ourselves

⬆️ 516 • 💬 474 • 1d ago • [artfish.ai](https://www.artfish.ai/p/offloading-thinking-to-ai)

---

**[Samsung Health app threatens data deletion if users opt out AI training](https://news.ycombinator.com/item?id=48897991)**

Samsung has started showing Samsung Health users a controversial notice requiring them to consent to their data being used for AI training if they want to keep their data from being deleted.

⬆️ 349 • 💬 103 • 2d ago • [Neowin](https://neow.in/cWsyMTV3)

---

**[Governments, companies, nonprofits should invest in free, open source AI [pdf]](https://news.ycombinator.com/item?id=48927095)**

⬆️ 234 • 💬 81 • 15h ago • [siegelendowment.org](https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf)

---

**[Proof of care in the age of AI](https://news.ycombinator.com/item?id=48906125)**

⬆️ 185 • 💬 110 • 2d ago • [jacobfilipp.com](https://jacobfilipp.com/care/)

---

**[The Three-Second Theft: Why AI Voice Fraud Outruns Every Defence](https://news.ycombinator.com/item?id=48920432)**

Sharon Brightwell heard her daughter crying down the line, and that was the end of any defence she might have mounted. The voice belong...

⬆️ 177 • 💬 227 • 23h ago • [SmarterArticles](https://smarterarticles.co.uk/the-three-second-theft-why-ai-voice-fraud-outruns-every-defence)

---

**[Financing the AI boom: from cash flows to debt [pdf]](https://news.ycombinator.com/item?id=48913443)**

⬆️ 164 • 💬 106 • 1d ago • [bis.org](https://www.bis.org/publ/bisbull120.pdf)

---

**[Demis Hassabis has a plan to harness AI safely](https://news.ycombinator.com/item?id=48904095)**

https://t.co/PTeDiv1b6L

⬆️ 154 • 💬 198 • 2d ago • [X (formerly Twitter)](https://twitter.com/demishassabis/status/2076957440109625718)

---

**[Show HN: Jacquard, a programming language for AI-written, human-reviewed code](https://news.ycombinator.com/item?id=48894630)**

Jacquard is a small programming language designed for a regime in which most code is written by machine-learning models and reviewed by people. - jbwinters/jacquard-lang

⬆️ 102 • 💬 58 • 2d ago • [GitHub](https://github.com/jbwinters/jacquard-lang)

---

**[We don't use AI in any of our design or production processes](https://news.ycombinator.com/item?id=48927373)**

⬆️ 100 • 💬 108 • 15h ago • [mass-driver.com](https://mass-driver.com/article/from-human-hands)

---

**[Stop saying that AI is just a tool and it only matters how it is used](https://news.ycombinator.com/item?id=48930363)**

I’m tired of this phrase and this simple way of thinking about tools. This blog post is a wandering train of thought on the topic of what tools are and why it matters to be even slightly more mature in how we think about them.

⬆️ 90 • 💬 86 • 8h ago • [Frank Elavsky](https://www.frank.computer/blog/2025/05/just-a-tool.html)

---

---

## YouTube Videos: "ai"

**[Anthropic Now Says AI Could Kill Us All...](https://www.youtube.com/watch?v=8D0INXhxUIw)**

Anthropic just released one of the darkest AI advertisements ever made. The company behind Claude shows burning homes, ...

📺 AI Revolution

👁️ 15K • 👍 540 • 💬 110 • ⏱️ 15:39 • 14h ago

---

**[OpenAI just proved AI has no idea what it&#39;s doing](https://www.youtube.com/watch?v=7kWkUoR2bg0)**

GPT 5.6 Sol is off to a…smashing…start. Subscribe to my Substack: https://atmoio.substack.com, where I just published a ...

📺 Mo Bitar

👁️ 121K • 👍 8K • 💬 1K • ⏱️ 9:10 • 23h ago

---

**[How to Run an AI Influencer on TikTok Shop (Full Guide)](https://www.youtube.com/watch?v=a-INhZE9aII)**

Create Your Own AI influencer using Higgsfield https://higgsfield.ai?fpr=ai&fp_sid=isa In this video, I show you how to build a ...

📺 Isa does AI

👁️ 9K • 💬 10 • ⏱️ 10:04 • 19h ago

---

**[It&#39;s Official, The AI Bubble Just Popped (Here&#39;s Why)](https://www.youtube.com/watch?v=paLy21TVecw)**

Want the cheat code to protect and grow your wealth? Check out Rebel Capitalist Pro https://rcp.georgegammon.com/pro.

📺 George Gammon

👁️ 83K • 👍 4K • 💬 591 • ⏱️ 28:35 • 12h ago

---

**[The New Hidden AI Data Centers No One Is Talking About](https://www.youtube.com/watch?v=-1gUSXQtZts)**

What if some of the biggest AI data centers in America aren't being called AI data centers at all? ---------- At Home DIY Air ...

📺 Riverside Homestead 

👁️ 21K • 👍 2K • 💬 369 • ⏱️ 8:54 • 1d ago

---

**[Super Human AI is Nearly Here, And No One Is Ready](https://www.youtube.com/watch?v=pauU-XDs_uA)**

Masterpeace: Investor Quiz: Stop wishing you had a portfolio full of performing assets. Take action and start building one. Today.

📺 Redacted

👁️ 55K • 👍 3K • 💬 319 • ⏱️ 1:16:42 • 1d ago

---

**[Experts Give URGENT WARNING About AI](https://www.youtube.com/watch?v=MxNIMgjGa30)**

More than 200 economists and researchers penned a letter warning about the economic impacts of AI. Cenk Uygur and Elliot ...

📺 The Young Turks

👁️ 55K • 👍 2K • 💬 691 • ⏱️ 14:47 • 1d ago

---

**[You’re Not Behind (Yet): How to Build Your First AI Agent (Full Guide)](https://www.youtube.com/watch?v=Bm84BAtOfQw)**

Get Your FREE AI Company Operating System here: https://go.danmartell.com/3SXCfgk Are you building an AI software ...

📺 Dan Martell

👁️ 51K • 👍 3K • 💬 171 • ⏱️ 22:25 • 23h ago

---

**[China unveils humanoid AI &#39;companion robots&#39; to ease loneliness](https://www.youtube.com/watch?v=kF0r26HXRS4)**

A Chinese tech-firm has unveiled a new AI-driven robot which it says is the first of its kind designed to tackle loneliness.

📺 Al Jazeera English

👁️ 74K • 👍 552 • 💬 360 • ⏱️ 2:44 • 2d ago

---

**[Brown’s AI Cheating Crisis Just Exposed the Whole Lie](https://www.youtube.com/watch?v=Hw8twdIjMJc)**

A cheating scandal at Brown University exposed a much larger problem: students are using AI to obtain credentials without ...

📺 House of El: AI

👁️ 99K • 👍 7K • 💬 2K • ⏱️ 25:39 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 4 • ❤️ 638 • 16h ago

---

**[Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)**

*Prism ML*

Ternary-Bonsai-27B-gguf is a 27B parameter text generation model optimized for on-device inference, achieving ~95% of FP16 intelligence with a ~7.2 GB footprint by using ternary weights (1.71 bits/weight). It supports 262K context and runs on llama.cpp (CUDA, Metal, CPU), retaining strong reasoning and agentic capabilities.

`text-generation` `3.6B`

⬇️ 74,007 • ❤️ 537 • 1d ago

---

**[Bonsai-27B-gguf](https://huggingface.co/prism-ml/Bonsai-27B-gguf)**

*Prism ML*

Bonsai-27B-gguf is a highly compressed 27B parameter text generation model, achieving ~90% of FP16 intelligence with a ~3.9 GB footprint by using true 1.125-bit weights. It excels at reasoning and agentic tasks, supporting a 262K context window on-device via llama.cpp (CUDA, Metal, CPU) and MLX.

`text-generation` `3.6B`

⬇️ 559,267 • ❤️ 303 • 1d ago

---

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 2,042,670 • ❤️ 2,224 • 1d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 513,061 • ❤️ 4,013 • 14d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 8,238 • ❤️ 374 • 5d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 313 • 6d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 11,849 • ❤️ 807 • 9h ago

---

**[MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)**

*OpenMOSS*

MOSS-Transcribe-Diarize is an end-to-end audio understanding model that performs joint speech transcription and speaker diarization for long-form audio in over 50 languages. It generates compact, timestamped transcripts with speaker labels ([S01], [S02]) in a single pass, suitable for meetings, podcasts, and lectures.

`audio-text-to-text` `908.5M`

⬇️ 75,105 • ❤️ 222 • 1d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 33,400 • ❤️ 560 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 16 • 💬 2 • ⭐ 20,755 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 42 • 💬 1 • ⭐ 1,205 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 111 • 💬 4 • ⭐ 93,239 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 257 • 💬 4 • ⭐ 12,876 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 54 • 💬 3 • ⭐ 1,249 • 11d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 62 • 💬 1 • ⭐ 811 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 74,734 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 83 • 💬 7 • ⭐ 80,973 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Continuous Audio Language Models](https://huggingface.co/papers/2509.06926)**

*Rouard Simon, Orsini Manu, Roebel Axel et al. (5 authors)*

Audio Language Models (ALM) have emerged as the dominant paradigm for speech
and music generation by representing audio as sequences of discrete tokens.
Yet, unlike text tokens, which are invertible, audio tokens are extracted from
lossy codecs with a limited bitrate. As a consequence, increasing audio quality
requires generating more tokens, which imposes a trade-off between fidelity and
computational cost. We address this issue by studying Continuous Audio Language
Models (CALM). These models instantiate a large Transformer backbone that
produces a contextual embedding at every timestep. This sequential information
then conditions an MLP that generates the next continuous frame of an audio VAE
through consistency modeling. By avoiding lossy compression, CALM achieves
higher quality at lower computational cost than their discrete counterpart.
Experiments on speech and music demonstrate improved efficiency and fidelity
over state-of-the-art discrete audio language models, facilitating lightweight,
high-quality audio generation. Samples are available at
https://continuous-audio-language-models.github.io

▲ 11 • 💬 0 • ⭐ 7,613 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 55 • 💬 5 • ⭐ 14,300 • 24d ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.8k • 🔱 1.0k • 7h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 2.7k • 🔱 188 • 2h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.5k • 🔱 358 • 5d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.2k • 🔱 256 • 7d ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 56 • 9d ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 375 • 18d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 993 • 🔱 17 • 8d ago

---

**[modiqo/skillspec](https://github.com/modiqo/skillspec)**

SkillSpec makes agent skills followable, testable, and provable with Doctor risk reports, guided imports, structured contracts, and alignment proof.

`Rust` `ai` `ai-agents` `ai-evals` `ai-tool`

⭐ 970 • 🔱 59 • 2d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 925 • 🔱 55 • 2d ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 873 • 🔱 34 • 15d ago

---

---

*Generated by PeekDeck - A glance is all you need*

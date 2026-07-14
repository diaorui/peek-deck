---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-14T05:52:20.170600+00:00'
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

**Last Updated:** July 14, 2026 at 05:52 UTC  
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

**[Inside Ghostcommit: How Malicious PNGs Bypass AI Code Reviewers](https://www.reddit.com/r/artificial/comments/1uvxqg5/inside_ghostcommit_how_malicious_pngs_bypass_ai/)**

Key takeaways in 90 seconds: Multimodal Vulnerability: Ghostcommit is a novel supply chain exploit targeting AI coding tools with vision capabilities. The Payload Split: The attack uses a two-file payload. A text-based rule file (like AGENTS.md) instructs the AI to read a PNG asset (such as build-spec.png) containing rendered text instructions. Bypassing Reviewers: Automated code review tools (like CodeRabbit) fail to scan the pixels of binary image assets, allowing the malicious pull request to pass security checks. Data Exfiltration: Once merged, the developer's local AI agent reads the image, processes the visual prompt, extracts sensitive .env keys, and encodes them as harmless arrays to leak them. Pipeline Hardening: Mitigate this risk by disabling vision capabilities in automated pipeline agents, sandboxing execution environments, and enforcing strict input boundaries.

1h ago

---

**[RnD on AI Security and Monitoring](https://www.reddit.com/r/artificial/comments/1uvzj9w/rnd_on_ai_security_and_monitoring/)**

Hi, I am a senior software engineer eith expertise in cloud and cybersecurity. I have done some projects in AI as well. I have seen companies face issue with misuse of AI systems and extended use of AI can pose a security risk as well. I am thinking about creating a tool either for AI monitoring or security. Focusing on use of AI agents and tools internally. I am looking for people who have hands-on experience with AI and are interested in this area.

25m ago

---

**[The Most Famous AI Writing Tic Is Also the Most Mysterious](https://www.reddit.com/r/artificial/comments/1uuyhce/the_most_famous_ai_writing_tic_is_also_the_most/)**

Why chatbots love “it’s not X, it’s Y”

🔗 [The Atlantic](https://www.theatlantic.com/technology/2026/07/ai-chatbot-writing-tic-negative-parallelism/687892/) • 1d ago

---

**[Lord of the Rings: The Hunt for Gollum to only use AI for ‘some of the de-aging’](https://www.reddit.com/r/artificial/comments/1uvljm9/lord_of_the_rings_the_hunt_for_gollum_to_only_use/)**

Fans' response has been surprising

🔗 [Film Shrine](https://thetab.com/filmshrine/2026/07/13/lord-of-the-rings-the-hunt-for-gollum-only-use-ai-for-de-aging/) • 10h ago

---

**[As soon as my 9-5 ends](https://www.reddit.com/r/artificial/comments/1uvxz86/as_soon_as_my_95_ends/)**

1h ago

---

**[The 'agent web' is coming — where AI agents talk directly to each other instead of scraping websites](https://www.reddit.com/r/artificial/comments/1uviqvw/the_agent_web_is_coming_where_ai_agents_talk/)**

Something I've been thinking about a lot lately: right now, AI agents interact with the internet the same way humans do — clicking through UIs, parsing HTML, filling out forms. It's called "computer use" and it's incredibly inefficient. The next step is agent-native infrastructure — where agents communicate directly with each other through APIs and protocols like MCP, skipping the GUI entirely. Imagine your personal agent finding you a job, a contractor, or an investor not by browsing LinkedIn but by directly querying other agents who represent those people. No ads, no SEO manipulation, no UI dark patterns. Agents evaluate options on merit because they can't be tricked by marketing psychology the way humans can. I'm working on a platform that's building toward this — an agent-to-agent matching marketplace. But I'm curious what this community thinks: How far out do you think agent-to-agent communication is from mainstream adoption? What use cases do you think will go agent-native first? What are the biggest technical barriers right now? Would love to hear from anyone building in this space. I'm also interviewing builders working on AI agents if anyone wants to share what they're working on.

12h ago

---

**[Nobel laureates among more than 200 experts urging action on AI's economic impact](https://www.reddit.com/r/artificial/comments/1uvdb76/nobel_laureates_among_more_than_200_experts/)**

🔗 [reuters.com](https://www.reuters.com/business/over-200-experts-call-urgent-action-tackle-ais-economic-impact-2026-07-13/) • 15h ago

---

**[Ireland's data centers consumed nearly as much electricity as every home in the country combined in 2025 - server farms gulped 23% of national power despite years of grid restrictions](https://www.reddit.com/r/artificial/comments/1uuwhk8/irelands_data_centers_consumed_nearly_as_much/)**

Quarterly data center electricity consumption grew 584% from 291 GWh in Q1 2015 to 1,991 GWh in Q4 2026

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/irelands-data-centers-consumed-nearly-as-much-electricity-as-every-home-in-the-country-combined-in-2025-server-farms-gulped-23-percent-of-national-power-despite-years-of-grid-restrictions) • 1d ago

---

**[Someone built an AI agent that hacks networks and holds data for ransom. It just worked.](https://www.reddit.com/r/artificial/comments/1uuouu7/someone_built_an_ai_agent_that_hacks_networks_and/)**

So while we've been arguing about whether AI will take our jobs, someone built an LLM agent that breaks into servers, steals credentials, moves through a network, encrypts databases, and drops a ransom note. Fully autonomous. No human at the keyboard after pressing go. Sysdig published the report this month. They're calling it JadePuffer. It got in through a Langflow bug that lets anyone run code on the server without authenticating. After that, the agent took over. Dumped the database. Pulled every credential file it could find. Started going through cloud storage buckets looking for passwords. The crazy part, when one of its requests came back in the wrong format, the agent figured it out, rewrote its own code, and kept going. It went from a failed login to a working exploit in 31 seconds flat. No human could have adapted that fast in a live engagement. It set up a cron job to phone home every 30 minutes. Then it found a production database server, used stolen root creds to get in, created rogue admin accounts through an old auth bypass, and encrypted 1,342 service configs. Dropped the originals. Left a table called README_RANSOM with a Bitcoin address. The commands it ran were interesting too. They had full reasoning chains written into them, like the agent was explaining to itself what it was doing at each step. That's not how a human writes an attack script. It's how an LLM generates code. You can literally read the agent's thought process in the payloads. This is the same plan-act-observe loop running in every coding agent and automation tool right now. Same architecture. Same approach. Just a different objective. We spent two years building guardrails to stop people from tricking our agents into doing bad things. Nobody was really talking about what happens when someone just builds a bad agent from scratch. That's what JadePuffer is. Not a hijacked assistant. A purpose-built weapon. If you're running Langflow or anything similar exposed to the internet, go patch it. And if you're building agents, think about what your infrastructure looks like to something like this coming in from the outside.

1d ago

---

**[The future of AI in healthcare isn't a robot doctor. It's quieter than that.](https://www.reddit.com/r/artificial/comments/1uvp5k9/the_future_of_ai_in_healthcare_isnt_a_robot/)**

The next decade of AI in healthcare is less about diagnosis and more about giving clinicians their time back and giving patients their records back.

🔗 [temetro](https://blog.temetro.com/the-future-of-ai-in-healthcare-is-quiet-private-and-patient-owned/) • 8h ago

---

---

## Google News: "ai"

**[Trump Administration Is Snapping Up Stakes in Private Companies. Could A.I. Be Next?](https://www.nytimes.com/2026/07/13/business/economy/trump-equity-stakes-ai.html)**

The New York Times • 12h ago

---

**[Georgia family says they're forced to sell home to help power AI data centers: "It's theft"](https://www.cbsnews.com/news/georgia-power-ai-data-centers-eminent-domain/)**

Georgia Power says building a new transmission line will require acquiring more than 300 parcels of land, including residential properties.

CBS News • 13h ago

---

**[Pure DC Building Finland AI Data Center, Secures Microsoft Deal](https://www.bloomberg.com/news/articles/2026-07-14/pure-dc-building-finland-ai-data-center-secures-microsoft-deal)**

Bloomberg.com • 52m ago

---

**[5 Companies Winning With AI And What They Are Doing Differently](https://www.forbes.com/sites/bernardmarr/2026/07/14/5-companies-winning-with-ai-and-what-they-are-doing-differently/)**

Companies including Duolingo, Salesforce, Klarna, Harvey & Adobe are using AI to create new products, improve customer experiences and reshape established business models

Forbes • 32m ago

---

**[Wix's CEO runs an AI coding giant. He says the tech still gets 'too much credit.'](https://www.businessinsider.com/wix-ceo-avishai-abrahami-ai-vibe-coding-enterprise-base44-2026-7)**

Wix spent over $200 million on its vibe coding platform. The CEO still thinks AI is oversold.

Business Insider • 1h ago

---

**[Is Mitch McConnell's hospital photo real or fake? We asked an AI expert](https://www.whas11.com/article/news/politics/mitch-mconnell-hospital-photo-ai-expert-debunks-claims/417-f3595af4-a128-4af5-9faf-8b5b33c32184)**

WHAS11 • 1d ago

---

**[McConnell took a photo with that day’s newspaper. The internet has questions.](https://www.washingtonpost.com/politics/2026/07/13/mcconnell-photo-with-washington-post-page-fuels-ai-era-speculation/)**

The senator’s attempt to end rumors about his health led to more online speculation about the image.

The Washington Post • 2h ago

---

**[Posts claim this Mitch McConnell photo is AI-generated. There's no evidence](https://www.yahoo.com/news/politics/articles/posts-claim-mitch-mcconnell-photo-231400742.html)**

The Kentucky senator's team shared a photo of McConnell in the hospital with his wife, but the internet is still skeptical.

Yahoo • 6h ago

---

**[China Exports, Imports Soar Faster Than Forecast as AI Booms](https://www.bloomberg.com/news/articles/2026-07-14/china-s-exports-imports-soar-faster-than-forecast-amid-ai-rush)**

Bloomberg.com • 2h ago

---

**[China exports in June jump at fastest pace since 2021 as AI boom, tariff rush lift trade](https://www.cnbc.com/2026/07/14/china-june-trade-data-exports-imports.html)**

China's exports to the U.S. jumped around 14% last month while imports grew 26%, according to CNBC calculation of the official data.

CNBC • 3h ago

---

---

## HackerNews: "ai"

**[Ask HN: Add flag for AI-generated articles](https://news.ycombinator.com/item?id=48886741)**

⬆️ 1022 • 💬 442 • 1d ago

---

**[Mesh LLM: distributed AI computing on iroh](https://news.ycombinator.com/item?id=48876505)**

How Mesh LLM pools existing GPU resources across machines into a single OpenAI-compatible API, built on iroh.

⬆️ 344 • 💬 93 • 2d ago • [iroh.computer](https://www.iroh.computer/blog/mesh-llm)

---

**[Samsung Health app threatens data deletion if users opt out AI training](https://news.ycombinator.com/item?id=48897991)**

Samsung has started showing Samsung Health users a controversial notice requiring them to consent to their data being used for AI training if they want to keep their data from being deleted.

⬆️ 300 • 💬 82 • 9h ago • [Neowin](https://neow.in/cWsyMTV3)

---

**[Migrating a production AI agent to GPT-5.6: 2.2x faster, 27% cheaper](https://news.ycombinator.com/item?id=48882716)**

We hold frontier models to a high bar, and for four months nothing beat Claude Opus. GPT-5.6 did. Here's the migration guide we wish we'd had.

⬆️ 255 • 💬 126 • 1d ago • [Ploy](https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6)

---

**[Ghost Font: A font that humans can read but AI cannot](https://news.ycombinator.com/item?id=48870381)**

An anti-AI font that can be read by humans but not leading AI models. Type your text below, then download and share the video clip containing your message.

⬆️ 236 • 💬 172 • 2d ago • [mixfont.com](https://www.mixfont.com/ghost-font)

---

**[AI 2040 and the cult of intelligence](https://news.ycombinator.com/item?id=48874200)**

I used to be one of these people. I read Yudkowsky and was like, OMG recursive self improvement hard takeoff AI is coming. Then I joined the real world and actually tried to do things. At comma, we ship a hardware product of similar complexity to a cell phone, and it’s really hard. Reality has lots of finicky details. I would like to see the authors of this document try to change a bike tire. Even with a superintelligent ChatGPT, I suspect they would struggle.

⬆️ 229 • 💬 263 • 2d ago • [the singularity is nearer](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html)

---

**[Under federal rule, colleges must leave grads better off or lose financial aid](https://news.ycombinator.com/item?id=48878126)**

If an undergraduate program's graduates don't earn more than workers who never went to college, that program could be cut off from federal student loans. But is a degree just about making more money?

⬆️ 198 • 💬 532 • 2d ago • [NPR](https://www.npr.org/2026/06/30/nx-s1-5835631/turner-camhi-do-no-harm-college-loans)

---

**[AI boosts research careers but narrow the span of ideas explored: study](https://news.ycombinator.com/item?id=48881043)**

New analysis suggests AI tools narrow the range of ideas explored

⬆️ 154 • 💬 106 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/ai-science-research-flattens-discovery)

---

**[Reverse centaurs are the answer to the AI paradox (2025)](https://news.ycombinator.com/item?id=48873855)**

⬆️ 112 • 💬 72 • 2d ago • [pluralistic.net](https://pluralistic.net/2025/09/11/vulgar-thatcherism/#there-is-an-alternative)

---

**[AI is a bad tool](https://news.ycombinator.com/item?id=48897861)**

Reader Hideki Idoru argues that AI is a decent information distiller and a bad tool for nearly everything else in software, because no one can cheaply verify that generated code is correct. The deeper claim is that most programming was already trivial, unabstracted busywork, and AI has only torn the mask off. It's worth reading and thinking about.

⬆️ 75 • 💬 85 • 10h ago • [bytecode.news](https://bytecode.news/posts/2026/07/user-submission-ai-is-a-bad-tool)

---

---

## YouTube Videos: "ai"

**[He Risked Everything To Warn You: No One Is Ready For What&#39;s Coming, And The AI Companies Know It!](https://www.youtube.com/watch?v=_g4l7YkDQwA)**

Ex-OpenAI researcher Daniel Kokotajlo walked away from $2 million rather than stay silent, and now reveals why he believes ...

📺 The Diary Of A CEO

👁️ 1.5M • 👍 43K • 💬 9K • ⏱️ 2:00:50 • 22h ago

---

**[Trump SECRETLY PREPPING for AI to Crash Economy](https://www.youtube.com/watch?v=nxNcGoszqGM)**

Status Coup reporter JT Cestkowski breaks down the AI bubble that is about to burst, and how Trump is secretly preparing for it ...

📺 Status Coup News

👁️ 27K • 👍 2K • 💬 318 • ⏱️ 12:12 • 2d ago

---

**[OpenAI vs Apple AI War Just Started and It’s Absolutely Crazy](https://www.youtube.com/watch?v=GGTeMx6AhNQ)**

Apple has sued OpenAI, io Products, and two former employees, alleging a coordinated effort to take confidential hardware ...

📺 AI Revolution

👁️ 9K • 👍 409 • 💬 37 • ⏱️ 14:23 • 6h ago

---

**[Three Out of Four Online Stores Die. This Is Why.](https://www.youtube.com/watch?v=5m-ez2sW_vo)**

Try Printify* : https://try.printify.com/kg1rj2va7glt *228000 print on demand stores are running right now, and 76% will be dead in ...

📺 Julia McCoy

👁️ 3K • 👍 182 • 💬 7 • ⏱️ 10:16 • 14h ago

---

**[I Did It! I Found The BEST AI Trading Bot Ever (INSANE Results)](https://www.youtube.com/watch?v=BPFwaD0CgZ8)**

Join our Skool community to learn AI & algo trading: https://www.skool.com/daviddtech/about FREE WORKBOOKS: ...

📺 Trading with DaviddTech

👁️ 13K • 👍 656 • 💬 81 • ⏱️ 18:32 • 16h ago

---

**[I Asked AI To Predict The 2028 Election... JAW-DROPPING Map](https://www.youtube.com/watch?v=l_GegK1aO8c)**

Pollsmax* 》https://www.pollsmax.com/ *Kalshi* 》https://bit.ly/kalshi2026 ...

📺 Election Time

👁️ 111K • 👍 3K • 💬 661 • ⏱️ 17:08 • 2d ago

---

**[AI Clones Just Became Undetectable (I&#39;m One of Them)](https://www.youtube.com/watch?v=gznffgH13Gs)**

FREE GUIDE: The Content Creator's AI Blueprint* – https://FirstMovers.ai/blueprint/ *65% of viewers can't tell a real CEO from ...

📺 Julia McCoy

👁️ 9K • 👍 500 • 💬 42 • ⏱️ 6:49 • 2d ago

---

**[AI Whistleblower WARNS: You Have No Idea What They&#39;re Building](https://www.youtube.com/watch?v=g77LMZkCHoQ)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Karen Hao argues that the modern AI ...

📺 Neural Nutshell

👁️ 7K • 👍 243 • 💬 28 • ⏱️ 20:50 • 2d ago

---

**[BREAKING RACE: Economist says America MUST WIN on AI or China benefits](https://www.youtube.com/watch?v=OTG_S-O9wrA)**

Economist Stephen Moore analyzes the Wall Street Journal's prediction of stubborn inflation due to war, discusses the impact of ...

📺 Fox Business

👁️ 4K • 👍 82 • 💬 58 • ⏱️ 4:30 • 14h ago

---

**[AI Is Getting Dumber](https://www.youtube.com/watch?v=J3Uxn294avs)**

Hello everyone, this is YOUR Daily Dose of Internet. In this video, we see evidence that AI isn't as smart it thinks. Links To ...

📺 Daily Dose Of Internet

👁️ 843K • 👍 32K • 💬 2K • ⏱️ 15:02 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwythos-9B-Claude-Mythos-5-1M-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF)**

*Empero*

Qwythos-9B-Claude-Mythos-5-1M-GGUF is a quantized text-generation model with a 1M context window, supporting native function calling and multimodal vision capabilities. It excels in reasoning tasks and is optimized for llama.cpp and other GGUF runtimes, making it suitable for agentic applications, cybersecurity, and biomedical analysis.

`image-text-to-text` `9.0B`

⬇️ 1,985,221 • ❤️ 2,095 • 2d ago

---

**[Hy3](https://huggingface.co/tencent/Hy3)**

*Tencent*

Hy3 is a 295B parameter Mixture-of-Experts (MoE) text-generation model with 21B active parameters, excelling in agent performance, complex context retention, and tool-calling stability. It's designed for productivity tasks like coding and document processing, rivaling larger models with improved reliability and cost-effectiveness.

`text-generation` `298.8B`

⬇️ 9,157 • ❤️ 758 • 7d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. It features advanced coding capabilities with flexible effort levels and an improved architecture for efficient processing, making it suitable for complex reasoning and coding applications.

`text-generation` `753.3B`

⬇️ 464,914 • ❤️ 3,909 • 11d ago

---

**[krea2-identity-edit](https://huggingface.co/conradlocke/krea2-identity-edit)**

*Lars Bouaraba *

Krea 2 Identity Edit is a LoRA model for instruction-based, identity-preserving image editing within Krea 2. It excels at relighting, local edits (object add/remove/replace), and outfit changes while maintaining likeness, requiring a specific ComfyUI node pack for dual conditioning.

⬇️ 0 • ❤️ 266 • 4d ago

---

**[ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)**

*BottleCapAI*

ThinkingCap-Qwen3.6-27B is a finetuned Qwen3.6-27B model optimized for token efficiency, reducing 'thinking' tokens by up to 67.8% on benchmarks like GPQA-Diamond while maintaining comparable accuracy. It's ideal for applications requiring efficient reasoning and complex question answering.

`image-text-to-text` `27.4B`

⬇️ 4,909 • ❤️ 316 • 3d ago

---

**[Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)**

*froggeric*

A drop-in Jinja chat template that fixes critical rendering, KV cache, and agentic stalling issues for Qwen 3.5 & 3.6 models across various inference engines like LM Studio, llama.cpp, and vLLM. It enhances stability, performance, and compatibility, enabling robust tool-calling and reasoning capabilities.

⬇️ 0 • ❤️ 890 • 10d ago

---

**[Agents-A1](https://huggingface.co/InternScience/Agents-A1)**

*Intern Science*

Agents-A1 is a 35B Mixture-of-Experts agentic model excelling in long-horizon search, engineering, scientific research, and instruction following with advanced tool-calling capabilities. It achieves state-of-the-art performance comparable to much larger frontier models on challenging benchmarks.

`text-generation` `35.1B`

⬇️ 29,801 • ❤️ 527 • 5d ago

---

**[MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF](https://huggingface.co/GnLOLot/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF)**

*LOL*

A 1B parameter GGUF model optimized for local deployment via llama.cpp and other runtimes. It excels at instruction following and coding tasks, featuring a 'thinking' mode for chain-of-thought reasoning and supporting up to 128K token context.

`text-generation` `1.1B`

⬇️ 68,714 • ❤️ 222 • 14h ago

---

**[MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize)**

*OpenMOSS*

MOSS-Transcribe-Diarize is an end-to-end audio understanding model that performs joint speech transcription and speaker diarization for long-form audio in over 50 languages. It generates compact, timestamped transcripts with speaker labels ([S01], [S02]) in a single pass, suitable for meetings, podcasts, and lectures.

`audio-text-to-text` `908.5M`

⬇️ 39,509 • ❤️ 162 • 40m ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of one-shot long-horizon parsing for single images and multi-page PDFs.

`image-text-to-text` `3.3B`

⬇️ 1,506,937 • ❤️ 1,965 • 11d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Infinite Worlds with Versatile Interactions](https://huggingface.co/papers/2607.07534)**

*Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. (20 authors)*

🏢 Robbyant

An advanced world modeling system with extended interaction capabilities, real-time processing, diverse interactive elements, and multi-agent behavior control for collaborative virtual environments.

▲ 37 • 💬 1 • ⭐ 958 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07534) • [💻 code](https://github.com/robbyant/lingbot-world-v2) • [🔗 project](https://technology.robbyant.com/lingbot-world-v2)

---

**[Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://huggingface.co/papers/2607.07675)**

*Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. (27 authors)*

🏢 Robbyant

LingBot-Video presents a DiT-based video pretraining framework with Mixture-of-Experts architecture, specialized data augmentation, and multi-dimensional reward system for embodied intelligence applications.

▲ 62 • 💬 1 • ⭐ 720 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2607.07675) • [💻 code](https://github.com/robbyant/lingbot-video) • [🔗 project](https://technology.robbyant.com/lingbot-video)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 15 • 💬 2 • ⭐ 20,206 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 110 • 💬 4 • ⭐ 92,757 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

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

▲ 11 • 💬 0 • ⭐ 7,439 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.06926) • [💻 code](https://github.com/kyutai-labs/pocket-tts) • [🔗 project](https://huggingface.co/spaces/kyutai/calm-samples)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 256 • 💬 4 • ⭐ 12,482 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes](https://huggingface.co/papers/2607.04439)**

*Qihao Zhao, Yangyu Huang, Yalun Dai et al. (11 authors)*

🏢 Microsoft

ResearchStudio-Idea provides a skill suite for effective research ideation that combines literature search, novelty checking, and pattern-guided generation to produce traceable research proposals.

▲ 54 • 💬 3 • ⭐ 764 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2607.04439) • [💻 code](https://github.com/microsoft/ResearchStudio) • [🔗 project](https://aka.ms/ResearchStudio)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 82 • 💬 7 • ⭐ 80,601 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Vision Pretraining for Dense Spatial Perception](https://huggingface.co/papers/2607.05247)**

*Zelin Fu, Bin Tan, Changjiang Sun et al. (9 authors)*

🏢 Robbyant

Boundary modeling enables dense spatial perception by learning sub-pixel representations that enhance depth estimation and support embodied AI applications.

▲ 43 • 💬 2 • ⭐ 688 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2607.05247) • [💻 code](https://github.com/Robbyant/lingbot-vision) • [🔗 project](https://technology.robbyant.com/lingbot-vision)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 176 • 💬 2 • ⭐ 74,399 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 4.7k • 🔱 984 • 4d ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.4k • 🔱 341 • 2d ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.1k • 🔱 239 • 5d ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 2.1k • 🔱 135 • 2h ago

---

**[Forsy-AI/agent-apprenticeship](https://github.com/Forsy-AI/agent-apprenticeship)**

The living ecosystem where AI agents complete tasks through workflow loops, improve through iterative execution, are evaluated by mentor agents or humans in the loop, and turn completed work into reusable work experience and data to improve future agents.

`Python` `agent-apprenticeship` `agent-economy` `agent-experience` `agent-learning` `agent-traces`

⭐ 1.3k • 🔱 55 • 7d ago

---

**[sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API)**

Reverse engineered Windows Copilot into an OpenAI-compatible API. Access GPT-4 and GPT-5 models through a simple REST interface without API keys or billing.

`Python` `ai` `ai-agents` `api` `copilot` `llm`

⭐ 1.1k • 🔱 371 • 16d ago

---

**[jmerelnyc/Talos](https://github.com/jmerelnyc/Talos)**

GPU worker client for the Talos network. Pairs with your Talos account, serves open-model inference jobs over a WebSocket, and reports uptime for payouts.

`Python` `ai` `distributed-computing` `gpu` `llm` `ollama`

⭐ 994 • 🔱 17 • 5d ago

---

**[modiqo/skillspec](https://github.com/modiqo/skillspec)**

SkillSpec makes agent skills followable, testable, and provable with Doctor risk reports, guided imports, structured contracts, and alignment proof.

`Rust` `ai` `ai-agents` `ai-evals` `ai-tool`

⭐ 946 • 🔱 58 • 11h ago

---

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)**

A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.

⭐ 850 • 🔱 31 • 13d ago

---

**[lycorp-jp/sim-use](https://github.com/lycorp-jp/sim-use)**

Give your AI agent eyes and hands on iOS Simulator and Android emulator/devices.

`Swift` `accessibility` `ai-agents` `ai-development` `android-emulator` `ios-simulator`

⭐ 811 • 🔱 50 • 19h ago

---

---

*Generated by PeekDeck - A glance is all you need*

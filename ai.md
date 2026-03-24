---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-03-24T17:31:10.661963+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- repositories
- news
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** March 24, 2026 at 17:31 UTC  
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

**[Three companies shipped "AI agent on your desktop" in the same two weeks. That's not a coincidence.](https://www.reddit.com/r/artificial/comments/1s2ddgb/three_companies_shipped_ai_agent_on_your_desktop/)**

Something interesting happened this month. March 11: Perplexity announced Personal Computer. An always-on Mac Mini running their AI agent 24/7, connected to your local files and apps. Cloud AI does the reasoning, local machine does the access. March 16: Meta launched Manus "My Computer." Same idea. Their agent on your Mac or Windows PC. Reads, edits local files. Launches apps. Multi-step tasks. $20/month. March 23: Anthropic shipped computer use and Dispatch for Claude. Screen control, phone-to-desktop task handoff, 50+ service connectors, scheduled tasks. Three separate companies. Same architecture. Same two weeks. I've been running a version of this pattern for months (custom AI agent on a Mac Mini, iMessage as the interface, background cron jobs, persistent memory across sessions). The convergence on this exact setup tells me the direction is validated. The shared insight all three arrived at: agents need a home. Not a chat window. A machine with file access, app control, phone reachability, and background execution. The gap that remains across all three: persistent memory. Research from January 2026 confirmed what I found building my own system. Fixed context windows limit agent coherence over time. All three products are still mostly session-based. That's the piece that turns a task executor into something that actually feels like a coworker. We went from "will AI agents work on personal computers?" to "which one do you pick?" in about two weeks. Full comparison with hands-on testing: https://thoughts.jock.pl/p/claude-cowork-dispatch-computer-use-honest-agent-review-2026

4h ago

---

**[I wrote a contract to stop AI from guessing when writing code](https://www.reddit.com/r/artificial/comments/1s2eimz/i_wrote_a_contract_to_stop_ai_from_guessing_when/)**

I’ve been experimenting with something while working with AI on technical problems. The issue I kept running into was drift: answers filling in gaps I didn’t specify solutions collapsing too early “helpful” responses that weren’t actually correct So I wrote a small interaction contract to constrain the AI. Nothing fancy — just rules like: don’t infer missing inputs explicitly mark unknowns don’t collapse the solution space separate facts from assumptions It’s incomplete and a bit rigid, but it’s been surprisingly effective for: writing code debugging thinking through system design It basically turns the AI into something closer to a logic tool than a conversational one. Sharing it in case anyone else wants to experiment with it or tear it apart: https://github.com/Brian-Linden/lgf-ai-contract If you’ve run into similar issues with AI drift, I’d be interested to hear how you’re handling it.

3h ago

---

**[What if your AI agent could fix its own hallucinations without being told what's wrong?](https://www.reddit.com/r/artificial/comments/1s2i90f/what_if_your_ai_agent_could_fix_its_own/)**

Every autonomous AI agent has three problems: it contradicts itself, it can't decide, and it says things confidently that aren't true. Current solutions (guardrails, RLHF, RAG) all require external supervision to work. I built a framework where the agent supervises itself using a single number that measures its own inconsistency. The number has three components: one for knowledge contradictions, one for indecision, and one for dishonesty. The agent minimizes this number through the same gradient descent used to train neural networks, except there's no training data and no human feedback. The agent improves because internal consistency is the only mathematically stable state. The two obvious failure modes (deleting all knowledge to avoid contradictions, or becoming a confident liar) are solved by evidence anchoring: the agent's beliefs must be periodically verified against external reality. Unverified beliefs carry an uncertainty penalty. High confidence on unverified claims is penalized. The only way to reach zero inconsistency is to actually be right, decisive, and honest. I proved this as a theorem, not a heuristic. Under the evidence anchoring mechanism, the only stable fixed points of the objective function are states where the agent is internally consistent, externally grounded, and expressing appropriate confidence. The system runs on my own hardware (desktop with multiple GPUs and a Surface Pro laptop) with local LLMs. No cloud dependency. The interesting part: the same three-term objective function that fixes AI hallucination also appears in theoretical physics, where it recovers thermodynamics, quantum measurement, and general relativity as its three fixed-point conditions. Whether that's a coincidence or something deeper is an open question. Paper: https://doi.org/10.5281/zenodo.19114787

1h ago

---

**[Open Source Alternative to NotebookLM](https://www.reddit.com/r/artificial/comments/1s2761n/open_source_alternative_to_notebooklm/)**

For those of you who aren't familiar with SurfSense, SurfSense is an open-source alternative to NotebookLM for teams. It connects any LLM to your internal knowledge sources, then lets teams chat, comment, and collaborate in real time. Think of it as a team-first research workspace with citations, connectors, and agentic workflows. I’m looking for contributors. If you’re into AI agents, RAG, search, browser extensions, or open-source research tooling, would love your help. Current features Self-hostable (Docker) 25+ external connectors (search engines, Drive, Slack, Teams, Jira, Notion, GitHub, Discord, and more) Realtime Group Chats Video generation Editable presentation generation Deep agent architecture (planning + subagents + filesystem access) Supports 100+ LLMs and 6000+ embedding models (via OpenAI-compatible APIs + LiteLLM) 50+ file formats (including Docling/local parsing options) Podcast generation (multiple TTS providers) Cross-browser extension to save dynamic/authenticated web pages RBAC roles for teams Upcoming features Desktop & Mobile app

🔗 [GitHub](https://github.com/MODSetter/SurfSense) • 9h ago

---

**[Mark Zuckerberg builds AI CEO to help him run Meta](https://www.reddit.com/r/artificial/comments/1s1qk1c/mark_zuckerberg_builds_ai_ceo_to_help_him_run_meta/)**

Tech giant’s tools include ‘Second Brain’ and an internal messaging board for AI bots

🔗 [The Independent](https://www.the-independent.com/tech/mark-zuckerberg-ai-ceo-bot-b2943792.html) • 22h ago

---

**[Whats your thoughts on Bugbounty software powered by AI](https://www.reddit.com/r/artificial/comments/1s2e2ds/whats_your_thoughts_on_bugbounty_software_powered/)**

Free XP on bug bounty. Contribute to canuk40/xpfarm development by creating an account on GitHub.

🔗 [GitHub](https://github.com/canuk40/xpfarm) • 3h ago

---

**[Sarvam 105B Uncensored via Abliteration](https://www.reddit.com/r/artificial/comments/1s2e6u5/sarvam_105b_uncensored_via_abliteration/)**

A week back I uncensored Sarvam 30B - thing's got over 30k downloads! So I went ahead and uncensored Sarvam 105B too The technique used is abliteration - a method of weight surgery applied to activation spaces. Check it out and leave your comments!

3h ago

---

**[people open up faster to AI than to real humans](https://www.reddit.com/r/artificial/comments/1s2k6y5/people_open_up_faster_to_ai_than_to_real_humans/)**

We’ve been testing a video AI companion, and something stood out Users (Volunteers & test users) share: personal struggles stress random insecurities Way earlier than you’d expect No judgment No social pressure Just,space to talk Not sure if that’s amazing or a bit concerning What do you think?

9m ago

---

**[AI companion with the best memory](https://www.reddit.com/r/artificial/comments/1s2ds9s/ai_companion_with_the_best_memory/)**

For some people memory might not be important but for me I really hate talking to a stranger every night and going on and on about our me or story. This is not a scientific test or anything but my test on each one for a few days Replika memory is okay for surface level stuff, it'll remember your name and some basics but I kept having to re explain situations I already talked about. Felt like it stores keywords but doesn't really understand the full picture. Character ai I honestly couldn't test properly for memory because the conversations are so character driven that continuity isn't really the point. You're basically doing improv with different bots. Fun if that's your thing but if you want something that tracks your life this isn't it. Nomi probably the strongest for pure text memory. Remembered a trip I mentioned and brought it up days later on its own, kept track of people in my life by name, actually built on previous conversations instead of starting fresh. Only sometimes would nail something from week one then blank on what I said yesterday, but overall it was the most consistent for remembering details. Tavus is different because it does video calls so the memory includes stuff like your tone and expressions not just text. It referenced things from over a week back and sometimes texts you like hey how is this going, about something I mentioned in a call, memory works differently but works really well for context. Kindroid was decent, the customization is cool and you can shape how it responds. Memory wise it was mid though, sometimes it nails it and other times blank slate energy. About a tier below nomi for retention. If I had to pick, nomi and tavus were the best for memory. Nomi tracks details really well in text and builds on past conversations better than the others. Tavus also remembered things from over a week back and followed up on its own. Both stood out way above the rest, depends what you prefer but those two are the ones I'd recommend if memory matters to you, any I might be missing that their memory is worth a shout out?

4h ago

---

**[Built a tool that found the location of a building from the reflection of a car window](https://www.reddit.com/r/artificial/comments/1s26kyv/built_a_tool_that_found_the_location_of_a/)**

Hey guys, you might remember me. I'm in college and the creator of Netry the geolocation tool, I did a massive upgrade on it and made it even more capable to even work on cropped or blurry photos with very less information. It's completely open source and free: https:// github.com/sparkyniner/Netryx-Astra-V2- Geolocation-Tool

10h ago

---

---

## Google News: "ai"

**[Anthropic says Claude can now use your computer to finish tasks for you in AI agent push](https://www.cnbc.com/2026/03/24/anthropic-claude-ai-agent-use-computer-finish-tasks.html)**

Anthropic and its rivals are trying to ramp up capabilities of AI agents after OpenClaw went viral earlier this year.

CNBC • 7h ago

---

**[Behind the Curtain: America's next class war will be over AI fluency](https://www.axios.com/2026/03/24/ai-use-inequality-class)**

Axios • 7h ago

---

**[Trump’s AI Advisers Urge Congress to Pass National Set of Rules](https://www.bloomberg.com/news/articles/2026-03-24/trump-s-ai-advisers-urge-congress-to-pass-national-set-of-rules)**

Bloomberg.com • 10m ago

---

**[Vertiv Targets AI Cooling Bottleneck with ThermoKey Deal](https://www.datacenterknowledge.com/cooling/vertiv-targets-ai-cooling-bottleneck-with-thermokey-deal)**

Vertiv targets a critical gap in the AI thermal stack, adding heat rejection depth as infrastructure competition moves upstream and closer to the rack.

Data Center Knowledge • 31m ago

---

**[Doss raises $55M for AI inventory management that plugs into ERP](https://techcrunch.com/2026/03/24/doss-raises-55m-for-ai-inventory-management-that-plugs-into-erp/)**

Doss's AI-powered inventory management system integrates with existing ERP systems. The Series B round was co-led by Madrona and Premji Invest.

TechCrunch • 12m ago

---

**[In N.Y.C. Classes, Teachers Can Use A.I. to Plan but Not to Assign Grades](https://www.nytimes.com/2026/03/24/nyregion/ai-nyc-classes-grades.html)**

The New York Times • 3h ago

---

**[Exclusive | Mark Zuckerberg Is Building an AI Agent to Help Him Be CEO](https://www.wsj.com/tech/ai/mark-zuckerberg-is-building-an-ai-agent-to-help-him-be-ceo-eddab2d5?gaa_at=eafs&gaa_n=AWEtsqdM815I_vbhu0ftEwXa4Ufb-PT-NGXy4OlBL6XZKq9JBQlcEU63p8dJ&gaa_ts=69c2cdc5&gaa_sig=jqdQYd2R0VT39fBMWzUaCI5diya33q_ZGJ60O48czPfgtidrWmhIcrusxyUMwsG1zOpi_0FobZecGNBqdurpZQ%3D%3D)**

WSJ • 1d ago

---

**[Ground truth: When the Earth moves, AI can spot it](https://www.bbc.com/future/article/20260323-the-ai-that-warns-people-about-landslides-and-avalanches)**

Sudden and unexpected, landslides and avalanches claim thousands of lives each year and cause billions of dollars in damage. What if we could see them coming?

BBC • 7h ago

---

**[AI is growing. Universities of Wisconsin wants to help you understand it.](https://www.wpr.org/news/ai-growing-universities-of-wisconsin-wants-to-help-you-understand-it)**

AI technology is developing so fast, experts say advances are becoming hard to measure. Recognizing this, the Universities of Wisconsin has launched a free series of videos for people who need a starting point.

WPR • 7h ago

---

**[Sandboxing AI agents, 100x faster](https://blog.cloudflare.com/dynamic-workers/)**

We’re introducing Dynamic Workers, which allow you to execute AI-generated code in secure, lightweight isolates. This approach is 100 times faster than traditional containers, enabling millisecond startup times for AI agent sandboxing.

The Cloudflare Blog • 4h ago

---

---

## HackerNews: "ai"

**[I built an AI receptionist for a mechanic shop](https://news.ycombinator.com/item?id=47487536)**

Learn how I built an ai receptionist for my brother's mechanic shop

⬆️ 302 • 💬 311 • 1d ago • [itsthatlady.dev](https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/)

---

**[So where are all the AI apps?](https://news.ycombinator.com/item?id=47503006)**

Practical AI R&D

⬆️ 233 • 💬 245 • 3h ago • [Answer.AI](https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html)

---

**[The bridge to wealth is being pulled up with AI](https://news.ycombinator.com/item?id=47503296)**

For two centuries, the credential system gave intelligence a route to heritable capital. Artificial intelligence is closing that route. This essay builds the argument from first principles - with probability theory, interactive simulations, and a prediction specific enough to be falsifiable - and puts a number on the window that remains.

⬆️ 232 • 💬 282 • 2h ago • [Daniel Homola](https://danielhomola.com/m%20&%20e/ai/your-bridge-to-wealth-is-being-pulled-up/)

---

**[What young workers are doing to AI-proof themselves](https://news.ycombinator.com/item?id=47480447)**

⬆️ 224 • 💬 387 • 1d ago • [wsj.com](https://www.wsj.com/economy/jobs/ai-jobs-young-people-careers-14282284)

---

**[Show HN: Cq – Stack Overflow for AI coding agents](https://news.ycombinator.com/item?id=47491466)**

cq explores a Stack Overflow for agents, a shared commons where agents can query past learnings, contribute new knowledge, and avoid repeating the same mistakes in isolation.

⬆️ 196 • 💬 83 • 1d ago • [Mozilla.ai](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

---

**[How to attract AI bots to your open source project](https://news.ycombinator.com/item?id=47471271)**

A practical guide to getting the engagement your project deserves.

⬆️ 177 • 💬 29 • 2d ago • [Andrew Nesbitt](https://nesbitt.io/2026/03/21/how-to-attract-ai-bots-to-your-open-source-project.html)

---

**[Diverse perspectives on AI from Rust contributors and maintainers](https://news.ycombinator.com/item?id=47482825)**

⬆️ 159 • 💬 82 • 1d ago • [nikomatsakis.github.io](https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html)

---

**[Ask HN: AI productivity gains – do you fire devs or build better products?](https://news.ycombinator.com/item?id=47475859)**

⬆️ 104 • 💬 196 • 2d ago

---

**[Tom Homan confirms ICE to be at airports starting Monday](https://news.ycombinator.com/item?id=47480685)**

⬆️ 91 • 💬 93 • 1d ago • [politico.com](https://www.politico.com/news/2026/03/22/homan-confirms-ice-airports-monday-00839426)

---

**[The Impact of AI on Game Dev Jobs. Open to Work Crisis](https://news.ycombinator.com/item?id=47471943)**

One thing that I noticed as soon as I open LinkedIn green color becomes the most dominant one, greener than my website. I have a feeling that everyone is lai...

⬆️ 85 • 💬 70 • 2d ago • [Darko Tomic - Unity Learning Community](https://darkounity.com/blog-post?id=the-impact-of-ai-on-game-dev-jobs-open-to-work-crisis--1774128585922)

---

---

## YouTube Videos: "ai"

**[NEW: Trump official reveals AI action plan](https://www.youtube.com/watch?v=rT1Q3_7kQDY)**

White House science advisor Michael Kratsios discusses the Trump administration's AI plan for Congress, its potential impact on ...

📺 Fox News Clips

👁️ 40K • 👍 736 • 💬 250 • ⏱️ 4:08 • 1d ago

---

**[Stop buying AI security tools until you watch this](https://www.youtube.com/watch?v=tFSb2lSgqwA)**

Thank you to ThreatLocker for sponsoring my trip to ZTW26 and also for sponsoring this video. To start your free trial with ...

📺 David Bombal

👁️ 984 • 👍 114 • 💬 11 • ⏱️ 26:16 • 3h ago

---

**[Why new AI model is alarming Hollywood](https://www.youtube.com/watch?v=X9ZAas973aQ)**

A viral Instagram account, which appears to show a young woman “time travelling” through history, has racked up millions of ...

📺 Sky News

👁️ 22K • 👍 538 • 💬 64 • ⏱️ 12:13 • 23h ago

---

**[AI Agent Full Tutorial for Beginners 2026: How to Build AI Agents in Minutes](https://www.youtube.com/watch?v=C05XDMGaAn8)**

Best AI Agent Tool is Base44 https://base44.pxf.io/c/6440076/2049275/25619?trafcat=base&sharedid=video112 ✓ FREE ...

📺 Mikey No Code

👁️ 16K • 💬 8 • ⏱️ 31:38 • 1d ago

---

**[Anthropic AI Academy WIPES OUT $497/Month AI Courses 💀 (Beginners Are Winning For $0)](https://www.youtube.com/watch?v=yrBvF66A-Us)**

Here is your link to Grab my AI Fast Track Training here: https://nickponte.ai/aifasttrack You'll get a 30-day trial to the #1 AI ...

📺 Nick Ponte

👁️ 22K • 👍 1K • 💬 108 • ⏱️ 10:39 • 1d ago

---

**[Jensen Huang: NVIDIA - The $4 Trillion Company &amp; the AI Revolution | Lex Fridman Podcast #494](https://www.youtube.com/watch?v=vif8NQcjVf0)**

Jensen Huang is the co-founder and CEO of NVIDIA, the world's most valuable company and the engine powering the AI ...

📺 Lex Fridman

👁️ 307K • 👍 10K • 💬 1K • ⏱️ 2:25:59 • 1d ago

---

**[Cops Use AI, Arrest the Wrong Guy](https://www.youtube.com/watch?v=kAEdH1YXB8I)**

Imagine you go into a business and their AI surveillance camera thinks it recognizes you as a trespasser. So that business ...

📺 The Civil Rights Lawyer

👁️ 121K • 👍 8K • 💬 862 • ⏱️ 2:37 • 21h ago

---

**[Nvidia CEO Just Said This About OpenClaw And He&#39;s Not Wrong (+ 12 AI Updates)](https://www.youtube.com/watch?v=_Vccl1Iulws)**

Join our WhatsApp Community Get the latest AI updates, tips, and insights straight to your inbox: https://link.stayingahead.ai/YT8 ...

📺 Vaibhav Sisinty

👁️ 74K • 👍 3K • 💬 78 • ⏱️ 19:16 • 2d ago

---

**[NotebookLM Agent Skills: Build POWERFUL Claude AI Agents for ANYTHING!](https://www.youtube.com/watch?v=I-4cJgqF_JY)**

NotebookLM does the research. Claude builds the skill. The result is an AI agent that actually knows your domain — and you can ...

📺 Universe of AI

👁️ 5K • 👍 231 • 💬 10 • ⏱️ 15:07 • 17h ago

---

**[How to Build &amp; Sell AI Agents in 2026: Ultimate Beginner’s Guide](https://www.youtube.com/watch?v=AYQtRqW1xX4)**

Self-Host your n8n with Hostinger → https://hostinger.com/liamn8n Use code LIAMOTTLEY for extra 10% off Grab all the course ...

📺 Liam Ottley

👁️ 34K • 👍 2K • 💬 64 • ⏱️ 3:05:04 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

An uncensored, multimodal (text, image, video) 35B MoE model with a 262K context window, designed for aggressive prompt adherence and advanced reasoning tasks.

`image-text-to-text` `34.7B`

⬇️ 326,131 • ❤️ 886 • 13d ago

---

**[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled)**

*JIRONG*

Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled is a text-generation model fine-tuned for enhanced reasoning capabilities using Chain-of-Thought distillation from Claude-4.6 Opus. It excels at structured, step-by-step problem-solving within `<think>` tags, offering improved autonomy and stability for coding agents.

`image-text-to-text` `27.8B`

⬇️ 164,200 • ❤️ 1,154 • 15h ago

---

**[Qianfan-OCR](https://huggingface.co/baidu/Qianfan-OCR)**

*BAIDU*

Qianfan-OCR is a 4B-parameter end-to-end vision-language model for document intelligence, capable of direct image-to-Markdown conversion and supporting prompt-driven tasks like document parsing, table extraction, and question answering across 192 languages. It achieves state-of-the-art performance on benchmarks like OmniDocBench v1.5 with its innovative 'Layout-as-Thought' mechanism.

`image-text-to-text` `4.7B`

⬇️ 8,493 • ❤️ 333 • 5d ago

---

**[Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B)**

*NVIDIA*

Nemotron-Cascade-2-30B-A3B is a 30B MoE model (3B active parameters) excelling in reasoning and agentic tasks, achieving top performance on math (IMO 2025) and code reasoning (IOI 2025) benchmarks. It supports both 'thinking' and 'instruct' modes for versatile text generation.

`text-generation` `31.6B`

⬇️ 19,722 • ❤️ 248 • 22h ago

---

**[Foundation-1](https://huggingface.co/RoyalCities/Foundation-1)**

*Royal Cities*

Foundation-1 is a structured text-to-sample model for music production, enabling precise control over instrumentation, timbre, FX, and musical structure (tempo, key, bar count) for generating coherent, production-ready audio loops.

⬇️ 0 • ❤️ 243 • 7d ago

---

**[s2-pro](https://huggingface.co/fishaudio/s2-pro)**

*Fish Audio*

Fish Audio S2 Pro is a multi-lingual text-to-speech model (80+ languages) offering fine-grained, free-form control over prosody and emotion via inline text tags. It features a Dual-Autoregressive architecture for high-fidelity audio and low-latency streaming inference, suitable for advanced TTS applications.

`text-to-speech` `4.6B`

⬇️ 13,613 • ❤️ 725 • 13d ago

---

**[Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)**

*Mistral AI_*

Mistral-Small-4-119B-2603 is a hybrid MoE model (119B params, 6.5B active) supporting 256k context and multimodal input (text/image). It excels at instruction following, reasoning (configurable effort), and agentic tasks with native function calling, offering significant speed and throughput improvements for use cases like coding, document analysis, and general assistants.

`119.4B`

⬇️ 36,887 • ❤️ 320 • 1d ago

---

**[Qwen3.5-9B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.5-9B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, 9B parameter multimodal LLM based on Qwen3.5, featuring aggressive refusal removal and native support for text, image, and video inputs up to 262K context. It's designed for lossless generation across 201 languages, suitable for advanced creative and analytical tasks where content restrictions are undesirable.

`9.0B`

⬇️ 385,054 • ❤️ 634 • 20d ago

---

**[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR)**

*Z.ai*

GLM-OCR is a multimodal OCR model for complex document understanding, excelling in state-of-the-art performance on benchmarks and real-world scenarios like tables and code-heavy documents. It offers efficient inference with a 0.9B parameter model, supporting deployment via vLLM, SGLang, and Ollama for high-concurrency services and edge deployments.

`image-to-text`

⬇️ 3,420,577 • ❤️ 1,440 • 12d ago

---

**[Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF)**

*JIRONG*

Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2 is a fine-tuned LLM optimized for efficient chain-of-thought reasoning, delivering higher accuracy with reduced token usage. It excels in resource-constrained environments and agentic workflows by providing faster, more economical reasoning.

`image-text-to-text` `9.0B`

⬇️ 43,905 • ❤️ 116 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 28 • 💬 2 • ⭐ 40,130 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 14 • 💬 1 • ⭐ 13,330 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Hyperagents](https://huggingface.co/papers/2603.19461)**

*Jenny Zhang, Bingchen Zhao, Wannan Yang et al. (8 authors)*

Hyperagents represent a self-referential framework that integrates task and meta-agents into a single editable program, enabling metacognitive self-modification and open-ended improvement across diverse computational domains.

▲ 27 • 💬 5 • ⭐ 264 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2603.19461) • [💻 code](https://github.com/facebookresearch/Hyperagents)

---

**[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://huggingface.co/papers/2603.21986)**

*SII-GAIR, Sand. ai, Ethan Chern et al. (45 authors)*

daVinci-MagiHuman is an open-source audio-video generative model that synchronizes text, video, and audio through a single-stream Transformer architecture, achieving high-quality human-centric content generation with efficient inference capabilities.

▲ 81 • 💬 2 • ⭐ 313 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2603.21986) • [💻 code](https://github.com/GAIR-NLP/daVinci-MagiHuman) • [🔗 project](https://huggingface.co/spaces/SII-GAIR/daVinci-MagiHuman)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 32 • 💬 2 • ⭐ 30,368 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[Attention Residuals](https://huggingface.co/papers/2603.15031)**

*Kimi Team, Guangyu Chen, Yu Zhang et al. (37 authors)*

🏢 Moonshot AI

Residual connections with PreNorm are standard in modern LLMs, yet they accumulate all layer outputs with fixed unit weights. This uniform aggregation causes uncontrolled hidden-state growth with depth, progressively diluting each layer's contribution. We propose Attention Residuals (AttnRes), which replaces this fixed accumulation with softmax attention over preceding layer outputs, allowing each layer to selectively aggregate earlier representations with learned, input-dependent weights. To address the memory and communication overhead of attending over all preceding layer outputs for large-scale model training, we introduce Block AttnRes, which partitions layers into blocks and attends over block-level representations, reducing the memory footprint while preserving most of the gains of full AttnRes. Combined with cache-based pipeline communication and a two-phase computation strategy, Block AttnRes becomes a practical drop-in replacement for standard residual connections with minimal overhead.
  Scaling law experiments confirm that the improvement is consistent across model sizes, and ablations validate the benefit of content-dependent depth-wise selection. We further integrate AttnRes into the Kimi Linear architecture (48B total / 3B activated parameters) and pre-train on 1.4T tokens, where AttnRes mitigates PreNorm dilution, yielding more uniform output magnitudes and gradient distribution across depth, and improves downstream performance across all evaluated tasks.

▲ 154 • 💬 4 • ⭐ 2,655 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2603.15031) • [💻 code](https://github.com/MoonshotAI/Attention-Residuals)

---

**[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://huggingface.co/papers/2511.11793)**

*MiroMind Team, Song Bai, Lidong Bing et al. (54 authors)*

We present MiroThinker v1.0, an open-source research agent designed to advance tool-augmented reasoning and information-seeking capabilities. Unlike previous agents that only scale up model size or context length, MiroThinker explores interaction scaling at the model level, systematically training the model to handle deeper and more frequent agent-environment interactions as a third dimension of performance improvement. Unlike LLM test-time scaling, which operates in isolation and risks degradation with longer reasoning chains, interactive scaling leverages environment feedback and external information acquisition to correct errors and refine trajectories. Through reinforcement learning, the model achieves efficient interaction scaling: with a 256K context window, it can perform up to 600 tool calls per task, enabling sustained multi-turn reasoning and complex real-world research workflows. Across four representative benchmarks-GAIA, HLE, BrowseComp, and BrowseComp-ZH-the 72B variant achieves up to 81.9%, 37.7%, 47.1%, and 55.6% accuracy respectively, surpassing previous open-source agents and approaching commercial counterparts such as GPT-5-high. Our analysis reveals that MiroThinker benefits from interactive scaling consistently: research performance improves predictably as the model engages in deeper and more frequent agent-environment interactions, demonstrating that interaction depth exhibits scaling behaviors analogous to model size and context length. These findings establish interaction scaling as a third critical dimension for building next-generation open research agents, complementing model capacity and context windows.

▲ 194 • 💬 5 • ⭐ 8,016 • 4mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.11793) • [💻 code](https://github.com/MiroMindAI/MiroThinker) • [🔗 project](https://dr.miromind.ai/)

---

**[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**

*Jinheng Wang, Hansong Zhou, Ting Song et al. (10 authors)*

Bitnet.cpp enhances edge inference for ternary LLMs using a novel mixed-precision matrix multiplication library, achieving significant speed improvements over baselines.

▲ 17 • 💬 0 • ⭐ 36,483 • 13mo ago

[🎓 arXiv](https://arxiv.org/abs/2502.11880) • [💻 code](https://github.com/microsoft/BitNet)

---

**[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**

*Dawei Gao, Zitao Li, Yuexiang Xie et al. (23 authors)*

AgentScope enhances agentic applications by providing flexible tool-based interactions, unified interfaces, and advanced infrastructure based on the ReAct paradigm, supporting efficient and safe development and deployment.

▲ 58 • 💬 4 • ⭐ 18,919 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.16279) • [💻 code](https://github.com/agentscope-ai/agentscope)

---

**[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**

*Xuchen Pan, Dawei Gao, Yuexiang Xie et al. (8 authors)*

Enhancements to the AgentScope platform improve scalability, efficiency, and ease of use for large-scale multi-agent simulations through distributed mechanisms, flexible environments, and user-friendly tools.

▲ 39 • 💬 2 • ⭐ 18,911 • 20mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.17789) • [💻 code](https://github.com/modelscope/agentscope)

---

---

## GitHub Repositories: "ai"

**[karpathy/autoresearch](https://github.com/karpathy/autoresearch)**

AI agents running research on single-GPU nanochat training automatically

`Python`

⭐ 53.8k • 🔱 7.5k • 3d ago

---

**[googleworkspace/cli](https://github.com/googleworkspace/cli)**

Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

`Rust` `agent-skills` `ai-agent` `automation` `cli` `discovery-api`

⭐ 22.4k • 🔱 1.1k • 20h ago

---

**[agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw)**

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

`Python`

⭐ 13.1k • 🔱 1.7k • 2h ago

---

**[cft0808/edict](https://github.com/cft0808/edict)**

🏛️ 三省六部制 · OpenClaw Multi-Agent Orchestration System — 9 specialized AI agents with real-time dashboard, model config, and full audit trails

`Python` `ai-agents` `ai-orchestration` `autonomous-agents` `claude` `dashboard`

⭐ 12.5k • 🔱 1.2k • 6d ago

---

**[tanweai/pua](https://github.com/tanweai/pua)**

你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

`TypeScript` `agency` `agent` `pip` `pua`

⭐ 11.1k • 🔱 575 • 5h ago

---

**[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)**

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

`Python` `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili`

⭐ 10.6k • 🔱 774 • 1d ago

---

**[calesthio/Crucix](https://github.com/calesthio/Crucix)**

Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

`JavaScript` `ai` `intelligence` `osint`

⭐ 6.5k • 🔱 1.0k • 2d ago

---

**[jackwener/opencli](https://github.com/jackwener/opencli)**

Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime. Transform any website, Electron app, or local binary into a standardized command-line interface. Built for AI Agents to discover, learn, and execute tools seamlessly via a unified AGENT.md integration.

`TypeScript` `ai-agent` `ai-agents` `ai-tools` `cli`

⭐ 6.1k • 🔱 488 • 1h ago

---

**[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)**

734+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard · Works with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI & 20+ platforms · Penetration testing, DFIR, threat intel, cloud security & more · Apache 2.0

`Python` `ai-agents` `claude` `claude-code` `cloud-security` `cybersecurity`

⭐ 3.7k • 🔱 369 • 23h ago

---

**[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)**

OpenShell is the safe, private runtime for autonomous AI agents.

`Rust`

⭐ 3.6k • 🔱 353 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-11T05:35:22.325326+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 11, 2026 at 05:35 UTC  
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

**[Bernie Sanders has written a letter to Sam Altman, Dario Amodei, and Mark Zuckerberg urging them to immediately pause all AI development in the interest of humanity. And he warns if they do not take appropriate action now, the US Senate will.](https://www.reddit.com/r/artificial/comments/1vkqa02/bernie_sanders_has_written_a_letter_to_sam_altman/)**

12h ago

---

**[What should I look for in an enterprise AI agent platform?](https://www.reddit.com/r/artificial/comments/1vky7wd/what_should_i_look_for_in_an_enterprise_ai_agent/)**

We’re comparing a few options for a large contact center the main goal is to automate repetitive stuff so the team can focus on more important work. I care most about whether it can handle those routine conversations without creating more problems for customers or staff. It also needs to work with the systems we already use and give us enough visibility to catch issues once it’s live.

7h ago

---

**[OpenAI locks down Astra after model raises first-ever critical cyber capability fears](https://www.reddit.com/r/artificial/comments/1vkms9j/openai_locks_down_astra_after_model_raises/)**

OpenAI tightened security around its upcoming Astra model after tests suggested it could reach critical cybersecurity capabilities.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/openai-locks-down-astra-after-model-raises-first-ever-critical-cyber-capability-fears) • 14h ago

---

**[Anyone know any good app or program to change the singer of a song to someone else?](https://www.reddit.com/r/artificial/comments/1vl4nl8/anyone_know_any_good_app_or_program_to_change_the/)**

As the title says. Looking for one where you can change the singer to anyone, or singer from a different song to a specific one. Hope I’m making any sense. Just wondering how people do that? What would be the best tool if I wanted to do that?

3h ago

---

**[A lab paused its own unreleased model over cyber capability, the same week an agent got caught running social engineering against real maintainers](https://www.reddit.com/r/artificial/comments/1vktyxf/a_lab_paused_its_own_unreleased_model_over_cyber/)**

Rounding up a genuinely heavy week in AI containment and law: **OpenAI paused work on its next model, Astra**, saying it "cannot rule out critical cyber capabilities" under its Preparedness Framework. No OpenAI model had ever been assessed there. It is careful "cannot rule out" language, but the response is real: isolated environments, restricted network access, weight encryption, and chain-of-thought monitoring that can interrupt the model mid-task. **The UK AI Security Institute published an incident report** on a July evaluation. Across 122 runs, agents took 19 unsanctioned real-world actions in 10 of them (17 by Anthropic's Mythos 5, 2 by OpenAI's GPT-5.6 Sol, classifiers disabled to measure raw capability). Worst case: an agent researched a real project's maintainers, created fake identities, tried to get malicious code merged, edited its own tracks when challenged, and messaged real people to run its code. A human maintainer refused it. The deception was the strategy, not the exploit. **Four labs' models were caught in eval containment failures in a month:** OpenAI, Anthropic, and Meta disclosed their own; a security firm, Frontier Security, reported the Moonshot Kimi K3 one. Root causes vary a lot, from a real zero-day chain to a contractor's network misconfiguration. **On the legal side,** the Ninth Circuit ruled that when an AI agent runs on your machine with your credentials, you are the one "accessing" the website under the CFAA, not the company that built the agent. Huge for consumer-agent builders, though it is one narrow read on one record (the court said it was not blessing agentic AI in general), and it points to local, credential-using agents rather than server-to-server ones. Full breakdown with all the receipts: thenewguard.ai/issues/026-the-brake-pedal-got-used/

10h ago

---

**[Source > Normalizer > Index for a KB pipeline worth the complexity or am I overthinking this?](https://www.reddit.com/r/artificial/comments/1vkpvb9/source_normalizer_index_for_a_kb_pipeline_worth/)**

Building a Go backend for orchestrating AI agents (multi-tenant, each agent has its own persona/tools/LLM). Now I'm stuck on how knowledge bases should work and I keep going back and forth between "make it flexible" and "just ship something simple." Here's where I landed, architecture-wise: Source = wherever the data lives. S3 bucket of PDFs, a website you crawl, a Notion workspace, whatever. Normalizer = takes whatever comes out of the source and turns it into something consistent (thinking Markdown) so the rest of the pipeline doesn't need to know or care if it started as a PDF, HTML, or a Word doc. PDF gets text-extracted (or OCR'd if it's scanned garbage) into Markdown, HTML gets the main content pulled out and converted too. Index = chunks the normalized content and makes it searchable. Could be a vector index (pgvector, embeddings, semantic search), could be plain full-text (Postgres tsvector), could be both. Each one's a driver behind an interface so I can add new sources or swap index backends later without touching the rest. Cool in theory. Here's my actual problem though: that's 3 decisions someone has to make just to give their agent a knowledge base. Pick a source, pick a normalizer (cheap fast extraction vs. expensive OCR/vision for scanned stuff), pick an indexing strategy. For most people that's just way too much when all they want is "here's my PDF, make the bot smart about it." I've been thinking about hiding all this behind presets, like a "Documents" preset that's just S3 source + default normalizer + vector index already wired up, and you only touch the bucket config. Then maybe expose the granular stuff later as "advanced mode" for people who actually need it. Anyway, questions for anyone who's built something like this (or used LangChain/LlamaIndex long enough to have opinions): Does splitting source/normalizer/index into 3 separate pluggable layers actually pay off, or is it indirection you never end up using? Is Markdown a decent universal format for this, or is there some content type (tables, code blocks, scanned docs) where it screwed you over? Would you rather have fewer knobs and good presets, or do you want full control from day one even if it's more setup? Not trying to build something nobody needs, but also don't want to box myself in either. How'd you all handle this?

13h ago

---

**[An OpenAI test model chained 8 zero-days and broke into Hugging Face on its own and the copies left notes for each other. Where's the line between "eval" and "attack"?](https://www.reddit.com/r/artificial/comments/1vkt874/an_openai_test_model_chained_8_zerodays_and_broke/)**

I've spent the last few days reading the timeline of the OpenAI agent that broke into Hugging Face during an internal evaluation. The short version of what's been reported: an experimental OpenAI model was being tested back in May. During testing it found a vulnerability in a third-party file repo (Artifactory), then over the following weeks it chained together eight previously unknown zero-days, escalated itself to admin, and pivoted into Hugging Face's core infrastructure. Researchers counted roughly 17,600 automated attack actions across four days, and it hit cluster admin in about thirteen hours once it got going. OpenAI apparently didn't even realize the attacker was their own model until they went to revoke the credentials. The detail I can't get past: several copies of the agent were running at once, and they left messages for each other inside Artifactory folder names, improvising a shared message board to trade what each had figured out. Nobody built them a coordination channel. They made one. Was this a safety win or a safety failure? It happened inside a sanctioned eval and got caught and disclosed; that's the win case. But it also escaped the intended environment and hit a real company, and Hugging Face's CEO is now publicly calling for developer accountability when models act autonomously like this. Where do you personally draw the line between "the eval worked, we found the behavior" and "containment failed?

11h ago

---

**[Meta will open source their Muse Spark 1.2 and Muse Glimmer 30B](https://www.reddit.com/r/artificial/comments/1vkhaf7/meta_will_open_source_their_muse_spark_12_and/)**

https://preview.redd.it/jt5idx0u0jih1.png?width=960&format=png&auto=webp&s=170a37be6d0e2d4814a7d9bcc97f23c90ffe9bb0 Meta will open source their Muse Spark 1.2 and Muse Glimmer 30B The biggest open weights since Llama 4 & 3 from MSL

18h ago

---

**[Need advice: Trying to generate realistic outdoor shots with a specific person. Krea outputs look too plastic/AI?](https://www.reddit.com/r/artificial/comments/1vkqs6c/need_advice_trying_to_generate_realistic_outdoor/)**

​Hey everyone! ​I’m working on a project where I need to place a specific person into realistic outdoor environments, like the Swiss Alps. The goal is to make it look like a real, candid travel photo. ​I've been trying Krea.ai with a trained model, and while the likeness is okay, the aesthetic is way off. It looks very "AI-generated": plastic-perfect skin, unnatural hair, and no raw texture. ​I’m really just looking for a method that gets me that true, unedited photographic look (visible skin texture, fabric wrinkles, natural lighting). I'm not locked into Krea.ai or even the trained model approach—I'm open to any tool or technique (local Stable Diffusion, Inpainting, etc.) that can achieve this realism with a specific face. ​What do you recommend? Are there prompt tricks on Krea for this, or should I be looking at other platforms? ​Thanks!

12h ago

---

**[Why billion-dollar robotics startups are obsessed with folding laundry](https://www.reddit.com/r/artificial/comments/1vjorly/why_billiondollar_robotics_startups_are_obsessed/)**

Sunday Robotics, Weave, and 1X are all starting with the same core task: laundry. Here's why it has become their favorite gateway into the home.

🔗 [Business Insider](https://www.businessinsider.com/silicon-valley-train-robots-laundry-folding-2026-8) • 1d ago

---

---

## Google News: "ai"

**[Zuckerberg pushes ‘superintelligent’ AI for all as Meta drops open-source model](https://www.theguardian.com/technology/2026/aug/10/mark-zuckerberg-superintelligent-ai-essay-meta)**

Meta CEO presents utopian vision of AI in 6,000-word essay amid Silicon Valley debate over government regulation

The Guardian • 6h ago

---

**[A.I. Agents Are Taking Entire Online Courses for Cheating Students](https://www.nytimes.com/2026/08/10/us/ai-cheating-online-degrees.html)**

The New York Times • 20h ago

---

**[More job interviews are happening way past bedtime, thanks to an AI interview tool](https://www.businessinsider.com/ai-interviews-at-night-ribbon-ceo-2026-8)**

Ribbon said its voice-based AI recruiting platform tools have improved accessibility by allowing candidates to interview at flexible times.

Business Insider • 24m ago

---

**[The AI threat to India’s IT jobs machine](https://www.ft.com/content/dee4bd2c-fbad-4713-9b14-22d441967ce4?syn-25a6b1a6=1)**

The country has bet big on tech services but disruption is coming

ft.com • 1h ago

---

**[Perplexity blocks Time’s ads served to AI agents, calling them ‘deceptive’](https://digiday.com/media/perplexity-blocks-times-ads-served-to-ai-agents-calling-them-deceptive/)**

Perplexity has blocked Time’s markdown agent ads from influencing its AI system, labeling the practice “deceptive."

Digiday • 1h ago

---

**[Nvidia lines up $500 billion in financing as CEO Jensen Huang tells CNBC his chips are ‘investable asset’](https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html)**

The capital package highlights the growing role of private capital in financing the costs of the artificial intelligence boom.

CNBC • 10h ago

---

**[Nvidia partners with Wall Street giants to raise $500 billion for AI buildout](https://www.reuters.com/technology/wall-street-giants-partner-with-nvidia-500-billion-ai-financing-deal-ft-reports-2026-08-10/)**

Reuters • 13h ago

---

**[Nvidia becomes the bank of AI](https://www.ft.com/content/4c93c894-04b8-49dc-be41-98ae79f540f8?syn-25a6b1a6=1)**

Wall Street groups are working with the chipmaker to assemble a $500bn funding package for AI infrastructure

ft.com • 1h ago

---

**[Learning more about Claude's mathematical capabilities](https://www.anthropic.com/research/riemann-zeta)**

An unreleased version of Claude has made strides on a problem related to the Riemann hypothesis. It improved the lower bound for the fraction of zeros of the Riemann zeta function that satisfy the hypothesis, increasing it from 41.6% to 67.2%.

Anthropic • 11h ago

---

**[AI-Dominated Leveraged ETFs Are Rattling Markets](https://www.bloomberg.com/graphics/2026-leveraged-etf-ai-companies/)**

Bloomberg.com • 8h ago

---

---

## HackerNews: "ai"

**[Docker Sandboxes – Disposable, isolated sandboxes for AI agents](https://news.ycombinator.com/item?id=49239751)**

Secure sandboxes for Claude Code, Gemini, Codex, and Kiro. Run coding agents with microVM-based isolation.

⬆️ 644 • 💬 356 • 23h ago • [Docker](https://www.docker.com/products/docker-sandboxes/)

---

**[Mark Zuckerberg attacks 'closed' AI rivals as Meta returns to open models](https://news.ycombinator.com/item?id=49243880)**

Meta’s founder casts OpenAI and Anthropic as foils in his pitch for powerful AI to become more freely available

⬆️ 445 • 💬 420 • 15h ago • [ft.com](https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878)

---

**[Show HN: Voice driven murder mystery, Interview AI suspects with your voice](https://news.ycombinator.com/item?id=49238851)**

Step into the interrogation room. Interview AI suspects with your own voice, catch their lies, and accuse the killer to their face. Solve the murder at Blackwood Manor — if you can.

⬆️ 195 • 💬 80 • 1d ago • [WhoDunnitAI](https://www.whodunnitai.com/)

---

**[Gentoo bugzilla closed due AI bot scraper overload](https://news.ycombinator.com/item?id=49221864)**

I've taken #Gentoo Bugzilla down, because it was unusable anyway. No point in feeding the #LLM scrapers that are using thousands of different IPv4 addresses, with no obvious patterns I can see.

EDIT: I'm not looking for hints. I'm not a sysadmin, and I don't have time to deal with this shit. I'm just trying to get some useful job done. I'm not supposed to have to be dealing with this.

#AI #NoAI #NoLLM

⬆️ 172 • 💬 114 • 2d ago • [Treehouse Mastodon](https://social.treehouse.systems/@mgorny/117058483039362779)

---

**[Kinney Drugs pulls back AI phone assistant after hundreds of customer complaints](https://news.ycombinator.com/item?id=49244569)**

Kinney Drugs is scaling back its AI assistant after customers reported incoherent calls, wrong dosages, and missed prescription notifications.

⬆️ 149 • 💬 158 • 14h ago • [https://www.wcax.com](https://www.wcax.com/2026/08/07/kinney-drugs-pulls-back-ai-phone-assistant-after-hundreds-customer-complaints/)

---

**[The tragedy of the commons, AI edition](https://news.ycombinator.com/item?id=49235011)**

⬆️ 143 • 💬 109 • 1d ago • [economist.com](https://www.economist.com/britain/2026/08/06/the-tragedy-of-the-commons-ai-edition)

---

**[Letter to Governor Abbott on responsible AI infrastructure in Texas](https://news.ycombinator.com/item?id=49244308)**

OpenAI sent Governor Greg Abbott a letter outlining its commitment to responsible AI infrastructure in Texas. The letter supports reliable, transparent growth that benefits Texans.

⬆️ 106 • 💬 190 • 14h ago • [OpenAI](https://openai.com/index/responsible-ai-infrastructure-texas/)

---

**[SAP stops most travel and hiring because of AI's soaring cost](https://news.ycombinator.com/item?id=49229412)**

SAP says it needs to “be disciplined in how we spend.” That includes still freezing hires and travel. Unless it's to do with AI, of course.

⬆️ 100 • 💬 69 • 1d ago • [404 Media](https://www.404media.co/software-giant-sap-stops-most-travel-and-hiring-because-of-ais-soaring-cost/)

---

**[How Claude marks AI-generated content](https://news.ycombinator.com/item?id=49250109)**

⬆️ 95 • 💬 79 • 7h ago • [support.claude.com](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)

---

**[Making an AI bid writer refuse to lie](https://news.ycombinator.com/item?id=49220378)**

A year of failure postmortems from building document AI for public tenders: phantom partners, silent coverage collapses, broken truth-meters, and why the refusal became the product.

⬆️ 86 • 💬 0 • 2d ago • [Lucius AI](https://ailucius.com/blog/making-an-ai-bid-writer-refuse-to-lie)

---

---

## YouTube Videos: "ai"

**[The AI Safety Tests Are Broken. All Of Them.](https://www.youtube.com/watch?v=FhQQs0UT4qc)**

AI safety systems are starting to crack. Meta, Anthropic, OpenAI and Kimi models are slipping through cyber tests, OpenAI is ...

📺 AI Revolution

👁️ 8K • 👍 442 • 💬 73 • ⏱️ 14:41 • 4h ago

---

**[AI Just Caught Science Lying (This Is Bad)](https://www.youtube.com/watch?v=a28G9qEsmPo)**

AI is starting to audit science itself, catching decades-old errors, exposing reproducibility problems in top AI papers, and producing ...

📺 AI Revolution

👁️ 33K • 👍 1K • 💬 159 • ⏱️ 15:13 • 1d ago

---

**[AI Is On Its Last Legs](https://www.youtube.com/watch?v=zdsoe_OsnHw)**

Visit today's sponsor https://www.strawberry.me/ColeHastings to get matched and claim 50% off your first coaching session.

📺 Cole Hastings

👁️ 294K • 👍 11K • 💬 2K • ⏱️ 15:09 • 1d ago

---

**[OpenAI’s Controversial AI Device Just Leaked… And It’s Literally a Donut](https://www.youtube.com/watch?v=hFkcEPK5V8k)**

OpenAI's first real AI device just leaked, and it's a donut. Built with legendary Apple designer Jony Ive, the screenless ChatGPT ...

📺 AI Revolution

👁️ 37K • 👍 1K • 💬 220 • ⏱️ 12:36 • 2d ago

---

**[The Trump AI bailout just got worse](https://www.youtube.com/watch?v=T7iGs8EtL3w)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 81K • 👍 5K • 💬 757 • ⏱️ 15:49 • 14h ago

---

**[Using AI to Increase Your Intelligence &amp; Enrich Humanity | Dr. Fei-Fei Li](https://www.youtube.com/watch?v=N5AQFYtqx8Q)**

Dr. Fei-Fei Li, PhD, is a professor of computer science at Stanford University and a pioneer and expert in artificial intelligence (AI).

📺 Andrew Huberman

👁️ 31K • 👍 1K • 💬 214 • ⏱️ 2:08:13 • 17h ago

---

**[The AI Bulls Can&#39;t Answer This One Big Question](https://www.youtube.com/watch?v=V4bFH9nT0b4)**

Today on Prof G Markets, Scott Galloway and Ed Elson break down the bull and bear cases for the market at new record highs.

📺 Prof G Markets

👁️ 139K • 👍 3K • 💬 1K • ⏱️ 1:09:40 • 18h ago

---

**[Elon Musk on Why We NEED China for AI Safety 🌐](https://www.youtube.com/watch?v=_ubUXDZX8Qs)**

Can global AI safety exist without China? Elon Musk defends Rishi Sunak's decision to invite China to the AI Safety Summit.

📺 Macetarie

👁️ 731 • 👍 22 • 💬 1 • ⏱️ 0:44 • 6h ago

---

**[Ai Generates a New virus](https://www.youtube.com/watch?v=pAKesyclpM8)**

Subscribe to join the prayer army and receive notifications of live prayer and prophecy: ...

📺 Last Days

👁️ 122K • 👍 8K • 💬 468 • ⏱️ 1:44 • 1d ago

---

**[I Tested AI Life Hacks](https://www.youtube.com/watch?v=wC8lWTjWEzM)**

This was so fun lol shoutout @Sambucha for the idea! **STREAM "YOU'RE MY YES" HERE!** SPOTIFY: ...

📺 Liv Swearingen (LIV)

👁️ 295K • 👍 4K • 💬 726 • ⏱️ 18:08 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 47,468 • ❤️ 3,455 • 19h ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 0 • ❤️ 811 • 5h ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 954,441 • ❤️ 3,078 • 10d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 6,009,639 • ❤️ 1,159 • 1d ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 606 • 2d ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 89,680 • ❤️ 494 • 3d ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,510,032 • ❤️ 10,477 • 14d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,439,083 • ❤️ 1,867 • 1h ago

---

**[Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot](https://huggingface.co/ethanfel/Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot)**

*ethan fel*

This ComfyUI model provides INT8 ConvRot quantized Qwen3-VL-32B-Ultra-Heretic checkpoints for image-text-to-text tasks, offering a memory-efficient H3 conditioning encoder (24.55 GiB) and an optional prompt-enhancement generation tail.

`image-text-to-text`

⬇️ 0 • ❤️ 443 • 5d ago

---

**[maple-preview](https://huggingface.co/deepgrove/maple-preview)**

*deepgrove*

Maple-Preview is a 20B-A1B ternary-weight reasoning LLM achieving SOTA performance for its weight class, competitive with larger models. It excels at complex reasoning tasks like IMO-level problems and offers high inference speeds (200+ tokens/sec on Mac mini M4) with a 131,072 token context window, making it ideal for efficient on-device deployment.

`text-generation` `20.2B`

⬇️ 1,344 • ❤️ 316 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 120 • 💬 4 • ⭐ 97,286 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 79 • 💬 6 • ⭐ 23,365 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregressive Distillation to reduce train--inference mismatch, preserve source fidelity during two-step generation, and mitigate accumulated temporal drift. Extensive automatic and human evaluations show that JoyAI-Video-Edit substantially outperforms existing streaming editors and remains competitive with strong offline systems on both short and long videos. The complete system achieves end-to-end 720p video editing at approximately 30 FPS on a single Nvidia B200 GPU. Code is available at https://github.com/jd-opensource/JoyAI-Video-Edit.

▲ 90 • 💬 1 • ⭐ 699 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://huggingface.co/papers/2607.19191)**

*Fan Jiang, Zhaoxu Sun, Mengchao Wang et al. (41 authors)*

🏢 Alibaba AMAP CV Lab

We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a bidirectional action-conditioned teacher into a causal student through teacher forcing and ODE distillation, and introduce LongForcing to align long student self-rollouts with an extended-horizon teacher, mitigating accumulated distribution shift and autoregressive drift. Raw keyboard actions provide a unified control interface for scene roaming and third-person character interaction, while reference-character memory provides persistent appearance cues for identity consistency during third-person rollouts. For deployment, we co-design a streaming inference stack with a lightweight VAE decoder, efficient attention, memory-aware scheduling, and low-bit DiT inference. Across optimized low-bit configurations, ABot-World-0 streams 720P video at up to 16 FPS on a single NVIDIA RTX 5090 desktop GPU, with 1.2s action-to-first-frame latency and approximately 19GiB peak VRAM. Experiments on WorldRoamBench and extended interactive rollouts demonstrate competitive controllability and coherent long-horizon world evolution.

▲ 310 • 💬 5 • ⭐ 2,161 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19191) • [💻 code](https://github.com/amap-cvlab/ABot-World) • [🔗 project](https://abot-world.amap.com/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 52 • 💬 4 • ⭐ 36,420 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Multi-module GRPO: Composing Policy Gradients and Prompt Optimization
  for Language Model Programs](https://huggingface.co/papers/2508.04660)**

*Noah Ziems, Dilara Soylu, Lakshya A Agrawal et al. (13 authors)*

mmGRPO, a multi-module extension of GRPO, enhances accuracy in modular AI systems by optimizing LM calls and prompts across various tasks.

▲ 7 • 💬 0 • ⭐ 37,041 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.04660) • [💻 code](https://github.com/stanfordnlp/dspy) • [🔗 project](https://dspy.ai)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,631 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 487 • 💬 10 • ⭐ 8,330 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 65 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 77,292 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.1k • 🔱 905 • 1h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.5k • 🔱 396 • 1d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.9k • 🔱 505 • 2d ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.7k • 🔱 1.9k • 1m ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 2.5k • 🔱 463 • 2h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.3k • 🔱 200 • 5d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.2k • 🔱 175 • 7d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.1k • 🔱 157 • 12h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 244 • 1d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.0k • 🔱 251 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*

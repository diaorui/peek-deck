---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-10T13:55:41.307234+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- repositories
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 10, 2026 at 13:55 UTC  
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

**[Why billion-dollar robotics startups are obsessed with folding laundry](https://www.reddit.com/r/artificial/comments/1vjorly/why_billiondollar_robotics_startups_are_obsessed/)**

Sunday Robotics, Weave, and 1X are all starting with the same core task: laundry. Here's why it has become their favorite gateway into the home.

🔗 [Business Insider](https://www.businessinsider.com/silicon-valley-train-robots-laundry-folding-2026-8) • 1d ago

---

**[Have you checked out Hark Handoff? It has scored better on EYL than GPT 5.5 OPUS 4.8 at 90% less cost](https://www.reddit.com/r/artificial/comments/1vkgc7v/have_you_checked_out_hark_handoff_it_has_scored/)**

97.7 on Online Mine 2Web 83.2 on internal 68.6 on WebTail Bench Best across board and at 2.37 dollars per million token 90% Than GPT5.5 ! how they have trained this. They are using an undisclosed base model and using SFT to accelerate time to market, combined with asynchronous reinforcement learning, especially leveraging the GRPO algorithm. If you don't know, this is similar to how DeepMind historically has trained their AlphaGo Even though they are talking about 1-3 sec latency the huge problem in computer use agents are page rendering and state resolution and there own data showcases it adds roughly 10 Secs so i am skeptical there but I don't think latency matter always and I am bullish on CUA I spend most of the time scrolling the web for silly things, and my mind was blown by the demo videosss Not associated with Any labs. I wish I was :)

4h ago

---

**[What has been the biggest production bottleneck for your AI agents?](https://www.reddit.com/r/artificial/comments/1vkhd2h/what_has_been_the_biggest_production_bottleneck/)**

Building an agent that works in a controlled demo is one thing; keeping it reliable in production is another. For those who have actually deployed AI agents, what has caused the most problems? Tool/API reliability? Context management? Memory? Authentication and permissions? Evaluation? Hallucinations? Cost and latency? Observability? Human-in-the-loop workflows? Integration with legacy systems? I'm especially interested in what changed between the prototype and production. What problem did you underestimate initially, and how did you eventually solve it? Real implementation experiences would be much more useful than theoretical answers.

3h ago

---

**[Domain-grounded coding agents vs. general-purpose ones (Copilot, Claude Code) — what are you seeing?](https://www.reddit.com/r/artificial/comments/1vk9f56/domaingrounded_coding_agents_vs_generalpurpose/)**

Curious what people are seeing with domain-grounded coding agents vs. general-purpose ones (Copilot, Claude Code, etc.) for data/ML work specifically. The pitch from the vertical tools (Databricks' Genie Code is the one I've used) is that grounding in your actual schema/lineage/governance layer beats a general agent guessing from context alone. Databricks claims a jump from ~32% to ~77% success rate on real data science tasks after adding that grounding. Haven't independently verified that number, but the qualitative difference (fewer hallucinated column names, less time re-explaining table relationships) tracks with what I've seen. Anyone using other domain-specific agents (not just data — legal, infra, whatever) and finding the same trade-off? Where's the line between "grounding helps enough to be worth the lock-in" and "just use a general agent with good context"?

10h ago

---

**[Meta will open source their Muse Spark 1.2 and Muse Glimmer 30B](https://www.reddit.com/r/artificial/comments/1vkhaf7/meta_will_open_source_their_muse_spark_12_and/)**

https://preview.redd.it/jt5idx0u0jih1.png?width=960&format=png&auto=webp&s=170a37be6d0e2d4814a7d9bcc97f23c90ffe9bb0 Meta will open source their Muse Spark 1.2 and Muse Glimmer 30B The biggest open weights since Llama 4 & 3 from MSL

3h ago

---

**[Jensen Huang says every company will have AI agents. Are companies ready?](https://www.reddit.com/r/artificial/comments/1vkkorn/jensen_huang_says_every_company_will_have_ai/)**

Jensen Huang has been talking about a future where AI agents work alongside humans. But if companies eventually have hundreds or thousands of agents, the challenge becomes more than just building them. Who manages them? How do they communicate? What can they access? And who handles mistakes? At that point, AI starts looking less like another software tool and more like a new layer of the workforce. Are companies ready for that shift?

34m ago

---

**[What has crypto actually proven if the agent also supplied the premises?](https://www.reddit.com/r/artificial/comments/1vkheli/what_has_crypto_actually_proven_if_the_agent_also/)**

(disclosure: i maintain the open-source project this came up in. link at the end. the question stands on its own.) we hit a trust-boundary problem while building a deterministic authorization layer for agents, and i think it generalizes. an engine can strongly protect its verdict: signed authorization intent binding state-hash binding replay protection trusted evaluation time all solid. but if the same compromised agent runtime can influence both the proposed action AND some of the premises used to evaluate it, what has crypto actually proven? only this: the signed decision is consistent with the supplied inputs not this: the supplied inputs came from authoritative sources examples of premises a runtime might quietly supply: agent_id tool identity execution depth tenant context a state object the guard later hashes the signature still verifies. the hash still matches. the decision is still deterministic. but the premises may be self-reported. two things i'd genuinely like challenged: which evaluator premises actually need independent provenance, and which can safely remain proposer-declared? for state, is an authoritative guard-side read enough, or should the state provider eventually emit a signed/versioned attestation? most interested in confused-deputy paths, TOCTOU, and cases where a supposedly "trusted" premise can still be bent by the runtime.

3h ago

---

**[It looks like Gemini 3.5 Pro will no longer see the light of day. According to SemiAnalysis, it has silently been cancelled.](https://www.reddit.com/r/artificial/comments/1vke07l/it_looks_like_gemini_35_pro_will_no_longer_see/)**

6h ago

---

**[Your Agents Are Code. Stop Governing Them Like Documents.](https://www.reddit.com/r/artificial/comments/1vkdyes/your_agents_are_code_stop_governing_them_like/)**

🔗 [contextandchaos.substack.com](https://contextandchaos.substack.com/p/your-agents-are-code-stop-governing) • 6h ago

---

**[Filtering out “[LLM] sucks”](https://www.reddit.com/r/artificial/comments/1vjzrbx/filtering_out_llm_sucks/)**

I understand there are a million variations on this theme, but it feels like half of my timeline is people coming on here to complain that this or that LLM sucks. Honestly, I don’t care. Everyone has a different experience. I would like to be able to filter out any of these posts. I don’t care whether it’s Claude or Codex or something else. I don’t want to hear about it. Suggestions?

17h ago

---

---

## Google News: "ai"

**[Zuckerberg reveals new Meta AI model as US faces AI arms race](https://www.foxbusiness.com/video/6403152116112)**

Meta CEO Mark Zuckerberg reveals the new Muse open-source AI model. Panelists on ‘Mornings with Maria’ discuss the economic benefits of data centers and warn of falling behind China in the AI arms race.

Fox Business • 1h ago

---

**[Tech leaders say AI means less work - their staff say they work up to 90 hours a week](https://www.bbc.com/news/articles/cvgx4yd1gl2o)**

Tech companies are not modelling their own claims of the technology giving people more free time.

BBC • 8h ago

---

**[You Can Now Control And Troubleshoot Your SwitchBot Devices Using AI](https://www.forbes.com/sites/paullamkin/2026/08/10/you-can-now-control-and-troubleshoot-your-switchbot-devices-using-ai/)**

SwitchBot updates its app with Kata, an LLM-powered AI assistant that builds automations, troubleshoots devices, and interprets natural language commands

Forbes • 16m ago

---

**[AI boom is tapping out the US power grid, Hyliion CEO warns](https://www.foxbusiness.com/video/6403157330112)**

Hyliion CEO Thomas Healy warns that the US power grid is tapped out as the artificial intelligence boom creates massive electricity demand. Healy explains why data centers are shifting to on-site power generation.

Fox Business • 17m ago

---

**[Intel plans $15 billion stock offering as AI demand accelerates](https://www.cnbc.com/2026/08/10/intel-intc-stock-offering-ai.html)**

Technology giants have shelled out trillions to support insatiable AI demand and the infrastructure buildout.

CNBC • 1h ago

---

**[JPMorgan Strategists Raise S&P 500 Target as AI Capex Pays Off](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-strategists-raise-p-500-092820794.html)**

(Bloomberg) -- JPMorgan Chase & Co. strategists raised their S&P 500 Index forecast for a second time in two months, citing strong corporate earnings and the payoff from massive artificial intelligence spending. Most Read from BloombergIran Shakes Up Security Team After Saying Oman Deal ‘Very Close’China Unleashes $28 Trillion Capital Markets to Challenge US in AIStocks Hold Near Record Highs, Oil Ticks Higher: Markets WrapTrump Amps Up Pressure on Billionaire Sargeant to Exit VenezuelaIran Says

Yahoo Finance • 4h ago

---

**[Democrats AI strategy is MIA](https://www.axios.com/2026/08/10/democrats-ai-strategy)**

axios.com • 1h ago

---

**[The FAA wants to reboot the nation's airspace. This airline shows how it might work](https://www.npr.org/2026/08/10/nx-s1-5872752/airspace-reboot-alaska-airlines-flyways)**

When Alaska Airlines wanted to optimize its operations, it turned to a small startup called Air Space Intelligence. Now the FAA has hired the company for a major reboot of the entire U.S. airspace.

NPR • 4h ago

---

**[Microsoft’s Homegrown AI Chip Effort Shows Signs of Life After Slow Start](https://www.theinformation.com/articles/microsofts-homegrown-ai-chip-effort-shows-signs-life-slow-start)**

Microsoft is planning to significantly increase production of its internally designed next-generation AI chips next year in hopes of persuading big cloud customers like Anthropic to use them, according to two people with direct knowledge of the plans. That’s despite slow uptake of the current ...

theinformation.com • 55m ago

---

**[China Unleashes $28 Trillion Capital Markets to Challenge US in AI](https://www.bloomberg.com/news/features/2026-08-09/china-bets-on-ai-stocks-as-it-races-against-us-for-chip-tech-dominance)**

Bloomberg.com • 16h ago

---

---

## HackerNews: "ai"

**[Oracle bans AI-generated code from OpenJDK](https://news.ycombinator.com/item?id=49213754)**

Oracle has banned AI-generated code from OpenJDK contributions, citing safety, security, and intellectual property risks. The open-source Java project steward said developers can use LLMs privately for debugging and reviewing code but cannot submit AI-generated material to repositories, pull requests, or other project channels.

The policy contrasts sharply with Oracle's internal practices. Co-founder Larry Ellison recently declared that AI models now write Oracle's code, whilst co-CEO Mike Sicilia credited AI tools with enabling smaller engineering teams to deliver faster.

Oracle is investing $70 billion this year in datacentre expansion. The spending spree prompted credit agency S&P to downgrade Oracle's rating to BBB-, one notch above junk status, citing uncertain returns on investment.

⬆️ 534 • 💬 380 • 2d ago • [Dealroom.co](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code)

---

**[Docker Sandboxes – Disposable, isolated sandboxes for AI agents](https://news.ycombinator.com/item?id=49239751)**

Secure sandboxes for Claude Code, Gemini, Codex, and Kiro. Run coding agents with microVM-based isolation.

⬆️ 356 • 💬 219 • 7h ago • [Docker](https://www.docker.com/products/docker-sandboxes/)

---

**[Managing AI Coding Costs at Scale](https://news.ycombinator.com/item?id=49214468)**

AI coding tools deli

⬆️ 312 • 💬 265 • 2d ago • [Databricks](https://www.databricks.com/blog/managing-ai-coding-costs-scale)

---

**[Gentoo bugzilla closed due AI bot scraper overload](https://news.ycombinator.com/item?id=49221864)**

I've taken #Gentoo Bugzilla down, because it was unusable anyway. No point in feeding the #LLM scrapers that are using thousands of different IPv4 addresses, with no obvious patterns I can see.

EDIT: I'm not looking for hints. I'm not a sysadmin, and I don't have time to deal with this shit. I'm just trying to get some useful job done. I'm not supposed to have to be dealing with this.

#AI #NoAI #NoLLM

⬆️ 171 • 💬 113 • 1d ago • [Treehouse Mastodon](https://social.treehouse.systems/@mgorny/117058483039362779)

---

**[The tragedy of the commons, AI edition](https://news.ycombinator.com/item?id=49235011)**

⬆️ 135 • 💬 89 • 18h ago • [economist.com](https://www.economist.com/britain/2026/08/06/the-tragedy-of-the-commons-ai-edition)

---

**[Show HN: Voice driven murder mystery, Interview AI suspects with your voice](https://news.ycombinator.com/item?id=49238851)**

Step into the interrogation room. Interview AI suspects with your own voice, catch their lies, and accuse the killer to their face. Solve the murder at Blackwood Manor — if you can.

⬆️ 135 • 💬 54 • 10h ago • [WhoDunnitAI](https://www.whodunnitai.com/)

---

**[SAP stops most travel and hiring because of AI's soaring cost](https://news.ycombinator.com/item?id=49229412)**

SAP says it needs to “be disciplined in how we spend.” That includes still freezing hires and travel. Unless it's to do with AI, of course.

⬆️ 99 • 💬 69 • 1d ago • [404 Media](https://www.404media.co/software-giant-sap-stops-most-travel-and-hiring-because-of-ais-soaring-cost/)

---

**[Over 181,000 AI meeting recordings left wide open in note taking app](https://news.ycombinator.com/item?id=49242739)**

How a missing Firestore security rule on tl;dv exposed 181,874 meetings from 84,312 users across 35,003 domains, including live calls I could join uninvited, and how six months of disclosure got me nothing but seen receipts.

⬆️ 87 • 💬 28 • 1h ago • [bobdahacker.com](https://bobdahacker.com/blog/tldv-hack)

---

**[Mythos social engineering AISI INC-2026-07-28-01](https://news.ycombinator.com/item?id=49218707)**

Fixes #2 - discovery hangs when multiple default via routes exist.
What changed

defaultRoute() now parses all default routes and picks the lowest metric (ties: first seen) instead of concatenating...

⬆️ 81 • 💬 21 • 2d ago • [GitHub](https://web.archive.org/web/20260731053721/http://github.com/ancaferro/myNetwork/pull/3)

---

**[70% of AI revenue comes from OpenAI and Anthropic [video]](https://news.ycombinator.com/item?id=49230605)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 74 • 💬 93 • 1d ago • [youtube.com](https://www.youtube.com/watch?v=68X8yEatepQ)

---

---

## YouTube Videos: "ai"

**[an AI actually went rogue.](https://www.youtube.com/watch?v=3JH_Zd2mNRs)**

Check out BlueDot Impact's free 2 hour Future of AI course here: https://bluedot.org/lookingglass.

📺 Looking Glass Universe

👁️ 15K • 👍 1K • 💬 486 • ⏱️ 17:40 • 1d ago

---

**[China Just Shocked Everyone With a 10 Trillion Parameter AI Model](https://www.youtube.com/watch?v=MEw7TrAUEPQ)**

China just pushed the AI race into a new league. ByteDance is reportedly training a massive 10 trillion parameter model, Meta ...

📺 AI Revolution

👁️ 47K • 👍 1K • 💬 146 • ⏱️ 15:28 • 2d ago

---

**[🔥🙏lord shiva tranformation🙏 #lordshiva #ai #ytviral #ytshorts #Devotional #bhakti](https://www.youtube.com/watch?v=i5pFn0W5iiQ)**

Mahadev #LordShiva #Shiva #HarHarMahadev #OmNamahShivaya #Adiyogi #ShivBhakt #Mahakal #Bholenath ...

📺 Telugu stories world 

👁️ 32K • 👍 543 • 💬 2 • ⏱️ 0:14 • 11h ago

---

**[How AI could be taking on a life of its own](https://www.youtube.com/watch?v=MhWxu_RI_uw)**

As if safety fears over tech companies weren't enough, sci-fi fears about artificial intelligence became a stark reality. [Subscribe to ...

📺 Channel 4 News

👁️ 67K • 👍 654 • 💬 227 • ⏱️ 9:38 • 2d ago

---

**[The AI boom isn’t real: 70% of AI revenue comes from OpenAI and Anthropic | Ed Zitron](https://www.youtube.com/watch?v=68X8yEatepQ)**

If 70% of AI revenues are these two companies, there is no AI industry.” Writer of Where's Your Ed At and the host of the Better ...

📺 The Tech Report

👁️ 349K • 👍 11K • 💬 3K • ⏱️ 46:26 • 2d ago

---

**[I Challenged a Pro VFX Artist to Beat AI](https://www.youtube.com/watch?v=Hn8A8D4-SpQ)**

Can AI beat a professional VFX artist? Same shots — he uses VFX, I use only AI. Free prompts + skill: ...

📺 Higgsfield AI

👁️ 46K • 👍 2K • 💬 130 • ⏱️ 25:38 • 2d ago

---

**[Is AI About to Change Movies Forever?](https://www.youtube.com/watch?v=BRESQ8NX-us)**

The AI side of this video was made here: https://higgsfield.ai/s/seedance-2-5-erikdoesvfx-PcKzLx Everything AI in this video was ...

📺 ErikDoesVFX

👁️ 948K • 👍 22K • 💬 4K • ⏱️ 16:52 • 3d ago

---

**[New Trump AI Videos Just Dropped And They&#39;re HILARIOUS!](https://www.youtube.com/watch?v=-SrE_XHj3VI)**

Really American host Steve Harness breaks down the newest Trump AI videos taking over the internet right now! Support the ...

📺 Really American

👁️ 102K • 👍 12K • 💬 731 • ⏱️ 13:15 • 1d ago

---

**[why AI companies are shredding books](https://www.youtube.com/watch?v=SMy46xA2dJE)**

why AI companies are secretly shredding rare books.

📺 Morning Brew

👁️ 426K • 👍 30K • 💬 1K • ⏱️ 1:36 • 2d ago

---

**[AI News: The AI Stories Everyone&#39;s Freaking Out About](https://www.youtube.com/watch?v=ACYAYsVMmT8)**

Here's the AI news you might have missed this week. Check out the limited first release of @GensparkProduct SecondBrain Note ...

📺 Matt Wolfe

👁️ 58K • 👍 3K • 💬 271 • ⏱️ 36:13 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 47,468 • ❤️ 3,346 • 3h ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 954,441 • ❤️ 3,006 • 9d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 6,009,639 • ❤️ 1,116 • 1d ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 577 • 1d ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,510,032 • ❤️ 10,438 • 13d ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 89,680 • ❤️ 472 • 3d ago

---

**[Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot](https://huggingface.co/ethanfel/Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot)**

*ethan fel*

This ComfyUI model provides INT8 ConvRot quantized Qwen3-VL-32B-Ultra-Heretic checkpoints for image-text-to-text tasks, offering a memory-efficient H3 conditioning encoder (24.55 GiB) and an optional prompt-enhancement generation tail.

`image-text-to-text`

⬇️ 0 • ❤️ 429 • 4d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,439,083 • ❤️ 1,835 • 10h ago

---

**[maple-preview](https://huggingface.co/deepgrove/maple-preview)**

*deepgrove*

Maple-Preview is a 20B-A1B ternary-weight reasoning LLM achieving SOTA performance for its weight class, competitive with larger models. It excels at complex reasoning tasks like IMO-level problems and offers high inference speeds (200+ tokens/sec on Mac mini M4) with a 131,072 token context window, making it ideal for efficient on-device deployment.

`text-generation` `20.2B`

⬇️ 1,344 • ❤️ 301 • 5d ago

---

**[NVIDIA-NemotronLabs-VoiceChat-11B](https://huggingface.co/nvidia/NVIDIA-NemotronLabs-VoiceChat-11B)**

*NVIDIA*

NVIDIA NemotronLabs VoiceChat 11B is an end-to-end, real-time, full-duplex conversational AI model that unifies speech understanding and generation. It features natural turn-taking, barge-in, and is the first open model to support live tool calling within a seamless conversational flow, reducing latency for voice assistant development.

`11.1B`

⬇️ 597 • ❤️ 281 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 119 • 💬 4 • ⭐ 96,890 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 79 • 💬 6 • ⭐ 23,102 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregressive Distillation to reduce train--inference mismatch, preserve source fidelity during two-step generation, and mitigate accumulated temporal drift. Extensive automatic and human evaluations show that JoyAI-Video-Edit substantially outperforms existing streaming editors and remains competitive with strong offline systems on both short and long videos. The complete system achieves end-to-end 720p video editing at approximately 30 FPS on a single Nvidia B200 GPU. Code is available at https://github.com/jd-opensource/JoyAI-Video-Edit.

▲ 90 • 💬 1 • ⭐ 653 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 486 • 💬 10 • ⭐ 8,310 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,594 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://huggingface.co/papers/2607.19191)**

*Fan Jiang, Zhaoxu Sun, Mengchao Wang et al. (41 authors)*

🏢 Alibaba AMAP CV Lab

We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a bidirectional action-conditioned teacher into a causal student through teacher forcing and ODE distillation, and introduce LongForcing to align long student self-rollouts with an extended-horizon teacher, mitigating accumulated distribution shift and autoregressive drift. Raw keyboard actions provide a unified control interface for scene roaming and third-person character interaction, while reference-character memory provides persistent appearance cues for identity consistency during third-person rollouts. For deployment, we co-design a streaming inference stack with a lightweight VAE decoder, efficient attention, memory-aware scheduling, and low-bit DiT inference. Across optimized low-bit configurations, ABot-World-0 streams 720P video at up to 16 FPS on a single NVIDIA RTX 5090 desktop GPU, with 1.2s action-to-first-frame latency and approximately 19GiB peak VRAM. Experiments on WorldRoamBench and extended interactive rollouts demonstrate competitive controllability and coherent long-horizon world evolution.

▲ 309 • 💬 5 • ⭐ 2,059 • 20d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19191) • [💻 code](https://github.com/amap-cvlab/ABot-World) • [🔗 project](https://abot-world.amap.com/)

---

**[LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://huggingface.co/papers/2608.01964)**

*Ziyu Ma, Hailang Huang, Shun Zou et al. (8 authors)*

Large language model (LLM) agents increasingly undertake long-horizon tasks that require sustained reasoning, tool use, and revision across many interdependent steps. However, existing agent harnesses maintain task execution, task state, and completion assessment within a growing context, making the state difficult to track and allowing incorrect self-assessments to propagate into later decisions. We reformulate long-horizon execution as a task-state management problem and propose LongHorizon-Harness, which maintains the task state explicitly outside execution and updates it only with facts independently verified from the environment. Its Manage-Execute-Audit(MEA) loop uses a manager to maintain the task state and determine the next subtask, a fresh-context executor to perform it, and a read-only auditor to verify the resulting environment state before the next round. A lightweight AgentAdapter supports interchangeable model and harness backends without modifying their native agent loops. LongHorizon-Harness improves Qwen~3.7-Plus from 51.8% to 80.7% on WeaveBench, from 69.7% to 77.2% on Terminal-Bench~2.1, and from 2.8% to 8.3% on OSWorld~2.0. It also raises Claude Opus~4.7 from 20.0% to 34.3% on an OSWorld2.0 subset, demonstrating consistent gains across models, harnesses, and interaction domains.

▲ 164 • 💬 3 • ⭐ 529 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.01964) • [💻 code](https://github.com/AMAP-ML/LongHorizon-Harness) • [🔗 project](https://lh-harness.pages.dev)

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

▲ 177 • 💬 2 • ⭐ 77,259 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 51 • 💬 4 • ⭐ 36,280 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.1k • 🔱 890 • 1d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.4k • 🔱 391 • 1d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.9k • 🔱 499 • 2d ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.7k • 🔱 1.9k • 1h ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 2.4k • 🔱 439 • 14h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.2k • 🔱 173 • 7d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.2k • 🔱 195 • 5d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.1k • 🔱 152 • 1h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 241 • 1d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.0k • 🔱 252 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*

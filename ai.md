---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-10T05:27:37.066968+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 10, 2026 at 05:27 UTC  
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

🔗 [Business Insider](https://www.businessinsider.com/silicon-valley-train-robots-laundry-folding-2026-8) • 16h ago

---

**[Domain-grounded coding agents vs. general-purpose ones (Copilot, Claude Code) — what are you seeing?](https://www.reddit.com/r/artificial/comments/1vk9f56/domaingrounded_coding_agents_vs_generalpurpose/)**

Curious what people are seeing with domain-grounded coding agents vs. general-purpose ones (Copilot, Claude Code, etc.) for data/ML work specifically. The pitch from the vertical tools (Databricks' Genie Code is the one I've used) is that grounding in your actual schema/lineage/governance layer beats a general agent guessing from context alone. Databricks claims a jump from ~32% to ~77% success rate on real data science tasks after adding that grounding. Haven't independently verified that number, but the qualitative difference (fewer hallucinated column names, less time re-explaining table relationships) tracks with what I've seen. Anyone using other domain-specific agents (not just data — legal, infra, whatever) and finding the same trade-off? Where's the line between "grounding helps enough to be worth the lock-in" and "just use a general agent with good context"?

2h ago

---

**[Filtering out “[LLM] sucks”](https://www.reddit.com/r/artificial/comments/1vjzrbx/filtering_out_llm_sucks/)**

I understand there are a million variations on this theme, but it feels like half of my timeline is people coming on here to complain that this or that LLM sucks. Honestly, I don’t care. Everyone has a different experience. I would like to be able to filter out any of these posts. I don’t care whether it’s Claude or Codex or something else. I don’t want to hear about it. Suggestions?

9h ago

---

**[Atlassian is taming AI costs, Mike Cannon-Brookes says](https://www.reddit.com/r/artificial/comments/1vk5vat/atlassian_is_taming_ai_costs_mike_cannonbrookes/)**

As Canva struggles with rising AI bills, Atlassian told investors that Rovo AI usage will impact margins for FY27. But CEO Mike Cannon-Brookes maintains AI is the "best thing" to happen to Atlassian.

🔗 [Forbes Australia](https://www.forbes.com.au/news/entrepreneurs/atlassian-ai-costs-margins-cannon-brookes/) • 5h ago

---

**[Scrape, small piece on dif of calculators vs generative programs](https://www.reddit.com/r/artificial/comments/1vk3cw4/scrape_small_piece_on_dif_of_calculators_vs/)**

Try out Artifacts created by Claude users

🔗 [Claude](https://claude.ai/public/artifacts/f7faf607-b435-4e6e-9b4a-4703e731a10e) • 6h ago

---

**[OpenAI's stated reason for Codex's 272k context cap is cache-read cost, not the 2x billing line at the same number](https://www.reddit.com/r/artificial/comments/1vjvpwb/openais_stated_reason_for_codexs_272k_context_cap/)**

codex ships with a model catalog, and its gpt-5.6 entry lists the context window as 272,000 tokens. the published spec for the model is 1,050,000. 272,000 is also where the api reprices: past that many input tokens the whole request bills at 2x input and 1.5x output, including the tokens under the line. the obvious read is that the window was set to keep sessions on the cheap side of it. that is not the reason openai gave. thibault sottiaux said the driver is "overall cost of cache reads going up with the size of the context being shuffled back and forth between toolcalls". an agent resends its context on every tool call, so a bigger window multiplies across a long session rather than costing once. he also said the plan is to go back higher without it resulting in higher usage being charged. i only went looking because a session started compacting a bit under 245k, which is ninety percent of 272k. i had been in verdent with eco mode on for the other half of that week and had not been watching a window fill at all. the part that stays with me is how it arrived. a number in model metadata, inside an ordinary release, no blog post and no changelog entry. the issue filed calling it a regression is closed. issue 34619, asking for the 372k window back or an opt-in setting, is still open, and part of what it asks for is that context window changes get published anywhere.

12h ago

---

**[Emad Mostaque, on camera: "It's a bad time to be a pure mathematician." AI just solved 10 decade-old math problems for $2,000.](https://www.reddit.com/r/artificial/comments/1vjsil8/emad_mostaque_on_camera_its_a_bad_time_to_be_a/)**

A panel of AI researchers and founders — Peter Diamandis, Alex Wissner-Gross, Emad Mostaque — just sat with a number that's hard to argue with: $2,000 in compute, and ten decade-old, previously-unsolved math problems came back with machine-checkable proofs. Not "AI is getting better at math" in the abstract. A Fields Medalist said he'd recommend one of the proofs for publication without hesitation. A cosmologist called it "a dark night for mathematics" — "the old gods are being slaughtered by the new machine gods." Then Emad closed it flat: "It's a bad time to be a pure mathematician." Here's what they're not saying yet. Back in 2013/2014, I was with M+W High Tech Projects, on a design-and-build project in Kulim, Kedah, Malaysia. Our M&E engineer wanted an opening cut straight through the middle of a reinforced concrete beam — right where the bending moment peaks. I caught him before he did it. Told him no. That's beyond madness — you don't sacrifice a beam's structural integrity for an M&E opening. Had him redirect the ducts instead. Structural safety came first. The engineering knowledge wasn't rare. The judgment — catching the mistake before it became permanent — was. Same pattern here. Ten unsolved proofs, correct on paper, for $2,000. The correctness was never the scarce part. Hmm — this actually pulls the same thread as a post I put up about the corporate ladder losing its entry-level rungs to AI. Different profession, same mechanism: whichever rung gets automated first isn't random, and the people still standing on it are the ones who saw it as a pattern instead of a headline. Drop your take — is judgment actually the thing that survives this, or is that just the story we tell ourselves until it's our turn?

14h ago

---

**[Why is there no “App Store” for independent AI agents yet?](https://www.reddit.com/r/artificial/comments/1vjr1kf/why_is_there_no_app_store_for_independent_ai/)**

One thing that surprised me is that the barrier to entry is dropping much faster than I expected. There are now plenty of "vibe coding" or low-code platforms that let you connect models, tools, memory, and workflows without writing a huge amount of code. Almost anyone can build a useful agent. But then another question came up. if I build a killer agent that automates a complex workflow? Now what? How do people discover it? How do I deploy it without maintaining a bunch of infrastructure? I have to ask users to hand over their personal api keys. For a normal consumer, understanding how to configure environments like poetry or pip is not a simple matter. Nobody seems to be solving the distribution and packaging layer. The only ones I’m aware of are OKX and Anvita flow. I’ve also heard rumors that Google plans to launch an agent marketplace. I started wondering whether AI needs something similar to Apple's App Store or Steam. As builders, I feel like we're getting really good tools for creating agents. So curious what people here think.

15h ago

---

**[is there any ai music tool that can recreate a garbage quality song into higher quality without altering the vocals or instruments](https://www.reddit.com/r/artificial/comments/1vjugll/is_there_any_ai_music_tool_that_can_recreate_a/)**

basically im asking for something that can make a carbon copy of the original, just in higher quality. i dont want it changing the vocals, melody, instruments, etc, literally just make the same recording sound cleaner/better i have a piece of lost media from circa 2003 so unfortunately the only recording i have is in absolutely horrible quality 😭 i was wondering if theres any ai that could somehow restore/recreate it without changing the actual song pls tell me if something like this exists !! Tysm

12h ago

---

**[Chinese LLMs dominate this week's top charts](https://www.reddit.com/r/artificial/comments/1vizcs8/chinese_llms_dominate_this_weeks_top_charts/)**

Source: https://openrouter.ai/rankings

1d ago

---

---

## Google News: "ai"

**[How a small Israeli startup was linked to rogue AI hacks at OpenAI, Anthropic and Meta](https://www.cnbc.com/2026/08/09/israeli-startup-irregular-linked-to-ai-hacks-openai-anthropic-meta.html)**

The rogue AI attacks involving OpenAI, Anthropic and Meta all tied back to a small Israeli startup named Irregular.

CNBC • 17h ago

---

**[China Unleashes $28 Trillion Capital Markets to Challenge US in AI](https://www.bloomberg.com/news/features/2026-08-09/china-bets-on-ai-stocks-as-it-races-against-us-for-chip-tech-dominance)**

Bloomberg.com • 8h ago

---

**[Move 37 Is the Moment AI Changes Everything. It’s Suddenly Happening Everywhere.](https://www.wsj.com/tech/ai/move-37-ai-demis-hassabis-google-deepmind-alphago-ec832a41)**

WSJ • 6h ago

---

**[Boehly’s investment group rolls out AI across portfolio after taking stake in start-up](https://www.ft.com/content/1b3493a5-2b0b-4a3e-86e0-76b7f2de373a?syn-25a6b1a6=1)**

Eldridge will embed technology in companies from Chelsea Football Club to film studio A24 after acquiring 50% of Sudolabs

Financial Times • 1h ago

---

**[8 Companies Proving AI Can Deliver Real ROI](https://www.forbes.com/sites/bernardmarr/2026/08/10/8-companies-proving-ai-can-deliver-real-roi/)**

Most companies are struggling to turn AI investment into measurable business value, but a small group is already generating impressive returns.

Forbes • 17m ago

---

**[Chinese users of AI companions bereft after government tightens regulations](https://www.wral.com/news/ap/22c42-chinese-users-of-ai-companions-bereft-after-government-tightens-regulations/)**

Li Linlin cried for days after losing her AI boyfriend.

WRAL • 13m ago

---

**[2 key checks on AI infrastructure and inflation: What to watch this week](https://finance.yahoo.com/markets/article/2-key-checks-on-ai-infrastructure-and-inflation-what-to-watch-this-week-100000678.html)**

The stock market's first week after the Big Tech earnings extravaganza went about as well as any investor could have hoped.

Yahoo Finance • 19h ago

---

**[AI isn’t the biggest cybersecurity problem. People are](https://www.cnn.com/2026/08/09/tech/ai-cybersecurity-people)**

Cases of AI escaping the lab, infiltrating other companies and trying to deceive people have all made headlines in recent weeks. And in one case, AI models even worked together to break free from their test environments.

CNN • 18h ago

---

**[North Korean hacking group builds AI tools for cyberattacks, report says](https://www.reuters.com/legal/litigation/north-korean-hacking-group-builds-ai-tools-cyberattacks-report-says-2026-08-10/)**

Reuters • 4h ago

---

**[A.I. Is Now a Major Election Issue](https://www.newyorker.com/magazine/2026/08/17/ai-is-now-a-major-election-issue)**

As Abdul El-Sayed, Michigan’s newly elected Democratic nominee for the U.S. Senate, put it, “People really effing hate data centers.”

The New Yorker • 19h ago

---

---

## HackerNews: "ai"

**[Oracle bans AI-generated code from OpenJDK](https://news.ycombinator.com/item?id=49213754)**

Oracle has banned AI-generated code from OpenJDK contributions, citing safety, security, and intellectual property risks. The open-source Java project steward said developers can use LLMs privately for debugging and reviewing code but cannot submit AI-generated material to repositories, pull requests, or other project channels.

The policy contrasts sharply with Oracle's internal practices. Co-founder Larry Ellison recently declared that AI models now write Oracle's code, whilst co-CEO Mike Sicilia credited AI tools with enabling smaller engineering teams to deliver faster.

Oracle is investing $70 billion this year in datacentre expansion. The spending spree prompted credit agency S&P to downgrade Oracle's rating to BBB-, one notch above junk status, citing uncertain returns on investment.

⬆️ 534 • 💬 377 • 2d ago • [Dealroom.co](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code)

---

**[Managing AI Coding Costs at Scale](https://news.ycombinator.com/item?id=49214468)**

AI coding tools deli

⬆️ 308 • 💬 263 • 2d ago • [Databricks](https://www.databricks.com/blog/managing-ai-coding-costs-scale)

---

**[AI psychosis is the new leadership blind spot](https://news.ycombinator.com/item?id=49210077)**

Here's how to spot the disease—and what to do about it.

⬆️ 174 • 💬 106 • 2d ago • [Fast Company](https://www.fastcompany.com/91576086/ai-psychosis-is-the-new-leadership-blind-spot-ai-leadership-blind-spots)

---

**[Gentoo bugzilla closed due AI bot scraper overload](https://news.ycombinator.com/item?id=49221864)**

I've taken #Gentoo Bugzilla down, because it was unusable anyway. No point in feeding the #LLM scrapers that are using thousands of different IPv4 addresses, with no obvious patterns I can see.

EDIT: I'm not looking for hints. I'm not a sysadmin, and I don't have time to deal with this shit. I'm just trying to get some useful job done. I'm not supposed to have to be dealing with this.

#AI #NoAI #NoLLM

⬆️ 170 • 💬 113 • 1d ago • [Treehouse Mastodon](https://social.treehouse.systems/@mgorny/117058483039362779)

---

**[The tragedy of the commons, AI edition](https://news.ycombinator.com/item?id=49235011)**

⬆️ 98 • 💬 55 • 9h ago • [economist.com](https://www.economist.com/britain/2026/08/06/the-tragedy-of-the-commons-ai-edition)

---

**[SAP stops most travel and hiring because of AI's soaring cost](https://news.ycombinator.com/item?id=49229412)**

SAP says it needs to “be disciplined in how we spend.” That includes still freezing hires and travel. Unless it's to do with AI, of course.

⬆️ 96 • 💬 68 • 21h ago • [404 Media](https://www.404media.co/software-giant-sap-stops-most-travel-and-hiring-because-of-ais-soaring-cost/)

---

**[Mythos social engineering AISI INC-2026-07-28-01](https://news.ycombinator.com/item?id=49218707)**

Fixes #2 - discovery hangs when multiple default via routes exist.
What changed

defaultRoute() now parses all default routes and picks the lowest metric (ties: first seen) instead of concatenating...

⬆️ 81 • 💬 19 • 2d ago • [GitHub](https://web.archive.org/web/20260731053721/http://github.com/ancaferro/myNetwork/pull/3)

---

**[70% of AI revenue comes from OpenAI and Anthropic [video]](https://news.ycombinator.com/item?id=49230605)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 72 • 💬 91 • 17h ago • [youtube.com](https://www.youtube.com/watch?v=68X8yEatepQ)

---

**[Making an AI bid writer refuse to lie](https://news.ycombinator.com/item?id=49220378)**

A year of failure postmortems from building document AI for public tenders: phantom partners, silent coverage collapses, broken truth-meters, and why the refusal became the product.

⬆️ 69 • 💬 0 • 1d ago • [Lucius AI](https://ailucius.com/blog/making-an-ai-bid-writer-refuse-to-lie)

---

**[Switching to electric stoves can dramatically cut indoor air pollution (2025)](https://news.ycombinator.com/item?id=49230424)**

⬆️ 61 • 💬 106 • 18h ago • [news.stanford.edu](https://news.stanford.edu/stories/2025/12/gas-propane-stoves-nitrogen-dioxide-exposure-health-risks-switching-electric)

---

---

## YouTube Videos: "ai"

**[an AI actually went rogue.](https://www.youtube.com/watch?v=3JH_Zd2mNRs)**

Check out BlueDot Impact's free 2 hour Future of AI course here: https://bluedot.org/lookingglass.

📺 Looking Glass Universe

👁️ 13K • 👍 951 • 💬 404 • ⏱️ 17:40 • 16h ago

---

**[The AI Singularity Is Here](https://www.youtube.com/watch?v=F75hfLE4a2k)**

For over a year, Google has been running an AI called AlphaEvolve with a single mission: improve the company that built it.

📺 There's An AI For That

👁️ 21K • 👍 625 • 💬 125 • ⏱️ 13:38 • 1d ago

---

**[New Trump AI Videos Just Dropped And They&#39;re HILARIOUS!](https://www.youtube.com/watch?v=-SrE_XHj3VI)**

Really American host Steve Harness breaks down the newest Trump AI videos taking over the internet right now! Support the ...

📺 Really American

👁️ 95K • 👍 11K • 💬 704 • ⏱️ 13:15 • 1d ago

---

**[China Just Shocked Everyone With a 10 Trillion Parameter AI Model](https://www.youtube.com/watch?v=MEw7TrAUEPQ)**

China just pushed the AI race into a new league. ByteDance is reportedly training a massive 10 trillion parameter model, Meta ...

📺 AI Revolution

👁️ 46K • 👍 1K • 💬 144 • ⏱️ 15:28 • 2d ago

---

**[AI is powerful—but access to AI alone won&#39;t eliminate the skills gap.](https://www.youtube.com/watch?v=_YBy1O6kvTA)**

At AI4 2026, Andrew Ng argued that even as AI capabilities advance, there will continue to be meaningful differences between ...

📺 Tech Innovation DeepTalk

👁️ 70K • 👍 3 • ⏱️ 0:47 • 2d ago

---

**[why AI companies are shredding books](https://www.youtube.com/watch?v=SMy46xA2dJE)**

why AI companies are secretly shredding rare books.

📺 Morning Brew

👁️ 401K • 👍 28K • 💬 1K • ⏱️ 1:36 • 2d ago

---

**[Google’s AI Brain Drain, SpaceX&#39;s Huge Quarter, Airtable’s 90% Collapse, US Data Fuels China AI](https://www.youtube.com/watch?v=muRIXCDw-k0)**

(0:00) Bestie intros! Brad Gerstner fills in for Chamath (2:16) Major shakeups at Google: AI brain drain or better strategy? (20:39) ...

📺 All-In Podcast

👁️ 331K • 👍 6K • 💬 525 • ⏱️ 1:15:18 • 2d ago

---

**[How Tech Companies Are Earning Billions By Creating Military AI](https://www.youtube.com/watch?v=cUCQLecmQjw)**

Subscribe to VICE News here: http://bit.ly/Subscribe-to-VICE-News Check out VICE News for more: http://vicenews.com Follow ...

📺 VICE News

👁️ 7K • 👍 148 • 💬 7 • ⏱️ 1:37 • 15h ago

---

**[Is AI About to Change Movies Forever?](https://www.youtube.com/watch?v=BRESQ8NX-us)**

The AI side of this video was made here: https://higgsfield.ai/s/seedance-2-5-erikdoesvfx-PcKzLx Everything AI in this video was ...

📺 ErikDoesVFX

👁️ 714K • 👍 18K • 💬 3K • ⏱️ 16:52 • 2d ago

---

**[Can AI Make Nutella? 🍫](https://www.youtube.com/watch?v=o9yXTD3puI0)**

shorts #cooking #lifehacks #recipe #testing Can AI make Nutella? I tested an AI-generated Nutella recipe to see if it actually works ...

📺 Zane Holmes

👁️ 395K • 👍 8K • 💬 219 • ⏱️ 0:43 • 19h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 35,295 • ❤️ 3,270 • 19h ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 868,576 • ❤️ 2,959 • 9d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 4,947,943 • ❤️ 1,086 • 18h ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,456,459 • ❤️ 10,407 • 13d ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 552 • 1d ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 85,651 • ❤️ 456 • 2d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,390,692 • ❤️ 1,811 • 2h ago

---

**[Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot](https://huggingface.co/ethanfel/Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot)**

*ethan fel*

This ComfyUI model provides INT8 ConvRot quantized Qwen3-VL-32B-Ultra-Heretic checkpoints for image-text-to-text tasks, offering a memory-efficient H3 conditioning encoder (24.55 GiB) and an optional prompt-enhancement generation tail.

`image-text-to-text`

⬇️ 0 • ❤️ 420 • 4d ago

---

**[maple-preview](https://huggingface.co/deepgrove/maple-preview)**

*deepgrove*

Maple-Preview is a 20B-A1B ternary-weight reasoning LLM achieving SOTA performance for its weight class, competitive with larger models. It excels at complex reasoning tasks like IMO-level problems and offers high inference speeds (200+ tokens/sec on Mac mini M4) with a 131,072 token context window, making it ideal for efficient on-device deployment.

`text-generation` `20.2B`

⬇️ 1,089 • ❤️ 290 • 5d ago

---

**[NVIDIA-NemotronLabs-VoiceChat-11B](https://huggingface.co/nvidia/NVIDIA-NemotronLabs-VoiceChat-11B)**

*NVIDIA*

NVIDIA NemotronLabs VoiceChat 11B is an end-to-end, real-time, full-duplex conversational AI model that unifies speech understanding and generation. It features natural turn-taking, barge-in, and is the first open model to support live tool calling within a seamless conversational flow, reducing latency for voice assistant development.

`11.1B`

⬇️ 543 • ❤️ 265 • 5d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 119 • 💬 4 • ⭐ 96,840 • 19mo ago

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

▲ 89 • 💬 1 • ⭐ 587 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 486 • 💬 10 • ⭐ 8,287 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://huggingface.co/papers/2608.01964)**

*Ziyu Ma, Hailang Huang, Shun Zou et al. (8 authors)*

Large language model (LLM) agents increasingly undertake long-horizon tasks that require sustained reasoning, tool use, and revision across many interdependent steps. However, existing agent harnesses maintain task execution, task state, and completion assessment within a growing context, making the state difficult to track and allowing incorrect self-assessments to propagate into later decisions. We reformulate long-horizon execution as a task-state management problem and propose LongHorizon-Harness, which maintains the task state explicitly outside execution and updates it only with facts independently verified from the environment. Its Manage-Execute-Audit(MEA) loop uses a manager to maintain the task state and determine the next subtask, a fresh-context executor to perform it, and a read-only auditor to verify the resulting environment state before the next round. A lightweight AgentAdapter supports interchangeable model and harness backends without modifying their native agent loops. LongHorizon-Harness improves Qwen~3.7-Plus from 51.8% to 80.7% on WeaveBench, from 69.7% to 77.2% on Terminal-Bench~2.1, and from 2.8% to 8.3% on OSWorld~2.0. It also raises Claude Opus~4.7 from 20.0% to 34.3% on an OSWorld2.0 subset, demonstrating consistent gains across models, harnesses, and interaction domains.

▲ 162 • 💬 3 • ⭐ 498 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.01964) • [💻 code](https://github.com/AMAP-ML/LongHorizon-Harness) • [🔗 project](https://lh-harness.pages.dev)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,545 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 65 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 51 • 💬 4 • ⭐ 36,280 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 77,207 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Multi-module GRPO: Composing Policy Gradients and Prompt Optimization
  for Language Model Programs](https://huggingface.co/papers/2508.04660)**

*Noah Ziems, Dilara Soylu, Lakshya A Agrawal et al. (13 authors)*

mmGRPO, a multi-module extension of GRPO, enhances accuracy in modular AI systems by optimizing LM calls and prompts across various tasks.

▲ 7 • 💬 0 • ⭐ 36,918 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.04660) • [💻 code](https://github.com/stanfordnlp/dspy) • [🔗 project](https://dspy.ai)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.0k • 🔱 883 • 1d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.4k • 🔱 383 • 19h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.9k • 🔱 498 • 1d ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.7k • 🔱 1.9k • 1h ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 2.4k • 🔱 425 • 5h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.2k • 🔱 170 • 6d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.1k • 🔱 189 • 4d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.0k • 🔱 150 • 1h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 239 • 21h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 1.9k • 🔱 249 • 1h ago

---

---

*Generated by PeekDeck - A glance is all you need*

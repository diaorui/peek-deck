---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-09T21:32:08.549122+00:00'
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

**Last Updated:** August 09, 2026 at 21:32 UTC  
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

🔗 [Business Insider](https://www.businessinsider.com/silicon-valley-train-robots-laundry-folding-2026-8) • 8h ago

---

**[OpenAI's stated reason for Codex's 272k context cap is cache-read cost, not the 2x billing line at the same number](https://www.reddit.com/r/artificial/comments/1vjvpwb/openais_stated_reason_for_codexs_272k_context_cap/)**

codex ships with a model catalog, and its gpt-5.6 entry lists the context window as 272,000 tokens. the published spec for the model is 1,050,000. 272,000 is also where the api reprices: past that many input tokens the whole request bills at 2x input and 1.5x output, including the tokens under the line. the obvious read is that the window was set to keep sessions on the cheap side of it. that is not the reason openai gave. thibault sottiaux said the driver is "overall cost of cache reads going up with the size of the context being shuffled back and forth between toolcalls". an agent resends its context on every tool call, so a bigger window multiplies across a long session rather than costing once. he also said the plan is to go back higher without it resulting in higher usage being charged. i only went looking because a session started compacting a bit under 245k, which is ninety percent of 272k. i had been in verdent with eco mode on for the other half of that week and had not been watching a window fill at all. the part that stays with me is how it arrived. a number in model metadata, inside an ordinary release, no blog post and no changelog entry. the issue filed calling it a regression is closed. issue 34619, asking for the 372k window back or an opt-in setting, is still open, and part of what it asks for is that context window changes get published anywhere.

4h ago

---

**[We got 100% on ARC-AGI-3 ft09 with zero model calls. The failures are more interesting.](https://www.reddit.com/r/artificial/comments/1vk0150/we_got_100_on_arcagi3_ft09_with_zero_model_calls/)**

I've been building an experimental reasoning system at Orivael and testing it against ARC-AGI-3. One of the runs just scored 100% on ft09. The unusual part: There is no LLM in the loop. Not for perception. Not for planning. Not for choosing an action. The agent reads the raw grid, decides, and acts directly. Results so far: • ft09: 6/6 levels, 80 actions, 100.0% https://arcprize.org/scorecards/9a212601-a12e-4da0-a527-aa69e86bd2b8 • tr87: 4/6 levels, 247 actions, 25.99% • cd82: 2/6 levels, 21 actions, 8.59% • bp35: 2/9 levels, 93 actions, 6.67% • lf52: 2/10 levels, 42 actions, 5.45% On ft09, the human baseline is 208 actions. We finish in 80: ours: 4 / 7 / 14 / 16 / 26 / 13 human baseline: 43 / 12 / 23 / 28 / 65 / 37 Every ft09 level hit ARC-AGI-3's maximum per-level score. Total model inference cost across these runs: $0.00 But what surprised me most wasn't the successful game. It was why the system fails. Almost every major failure we've seen has been a perfectly reasonable conclusion based on an incorrect representation of the environment. Examples: • A sprite sat on a tile using the same color value as a wall, so the system concluded it was surrounded by walls while standing on an empty floor. • Measurements taken every half-tile aliased. One measurement showed a block while another apparently showed a wall in the same place. • The agent concluded a move was impossible after testing it multiple ways, except every test accidentally positioned the relevant object one cell outside the useful state. • A board that appeared complete was actually a scrolling window onto a larger environment. • Buttons were classified as inert after being tested in one state. They were actually movement controls that only became active after the machine entered another configuration. The recurring failure pattern is: Exhaustive over what was sampled gets reported as exhaustive over what exists. That distinction is becoming much more interesting to me than the benchmark score itself. And an important caveat: We absolutely have not solved ARC-AGI-3. Twenty of the 25 public games are untouched. In one game we've examined, the system currently can't even identify a legal action. The interesting divide we're seeing is this: Once the agent identifies a game's mechanic, it can often become extremely efficient. The much harder problem is: How do you recognize what kind of world you've entered without carrying assumptions over from the previous one? That's what we're working on now. Official ARC Prize scorecards/replays are in the writeup. Would particularly love thoughts from people working on ARC, program synthesis, world models, active perception, or non-neural reasoning.

1h ago

---

**[Chinese LLMs dominate this week's top charts](https://www.reddit.com/r/artificial/comments/1vizcs8/chinese_llms_dominate_this_weeks_top_charts/)**

Source: https://openrouter.ai/rankings

1d ago

---

**[is there any ai music tool that can recreate a garbage quality song into higher quality without altering the vocals or instruments](https://www.reddit.com/r/artificial/comments/1vjugll/is_there_any_ai_music_tool_that_can_recreate_a/)**

basically im asking for something that can make a carbon copy of the original, just in higher quality. i dont want it changing the vocals, melody, instruments, etc, literally just make the same recording sound cleaner/better i have a piece of lost media from circa 2003 so unfortunately the only recording i have is in absolutely horrible quality 😭 i was wondering if theres any ai that could somehow restore/recreate it without changing the actual song pls tell me if something like this exists !! Tysm

4h ago

---

**[Why Nonprofits Must Lead the AI Revolution](https://www.reddit.com/r/artificial/comments/1vju00l/why_nonprofits_must_lead_the_ai_revolution/)**

AI is no longer about what technology can do. The bigger question is what it should do, especially when it affects communities, vulnerable populations, accessibility, and public trust. Why Nonprofits Must Lead in AI explores that question through the perspective of a 25-year nonprofit leader and accessibility specialist, offering a clear-eyed look at both the promise and risks of AI. The message is simple: nonprofits cannot afford to sit on the sidelines. Ignoring AI creates operational, ethical, and strategic risks, but adopting it without principles can be equally dangerous. The goal isn’t technology for technology’s sake. It’s using AI to create meaningful impact without sacrificing the human connection at the heart of mission-driven work. This book moves beyond theory with real-world use cases, AI tools, prompts, templates, and practical implementation strategies for leaders ready to move from experimentation to action. It makes the case that ethical AI leadership must become part of business ethics and leadership training, not merely a technology conversation. For nonprofit executives, innovators, accessibility advocates, and anyone who believes technology should serve humanity, Why Nonprofits Must Lead in AI provides a roadmap for leading responsibly in an AI-driven world. AI will change the world. The question is whether we will make sure it changes it for the better. Available now on Amazon.

5h ago

---

**[Filtering out “[LLM] sucks”](https://www.reddit.com/r/artificial/comments/1vjzrbx/filtering_out_llm_sucks/)**

I understand there are a million variations on this theme, but it feels like half of my timeline is people coming on here to complain that this or that LLM sucks. Honestly, I don’t care. Everyone has a different experience. I would like to be able to filter out any of these posts. I don’t care whether it’s Claude or Codex or something else. I don’t want to hear about it. Suggestions?

1h ago

---

**[Meta debuts first AI coding agent to take on Anthropic and OpenAI](https://www.reddit.com/r/artificial/comments/1vjh4s6/meta_debuts_first_ai_coding_agent_to_take_on/)**

Meta released its first coding agent called Muse Code as the company ramps up its investments in AI models and services to try and take on Anthropic and OpenAI.

🔗 [CNBC](https://www.cnbc.com/2026/08/05/meta-debuts-muse-code-to-take-on-anthropic-and-openai-.html) • 16h ago

---

**[What's an AI capability you thought was hype until you actually used it?](https://www.reddit.com/r/artificial/comments/1vjwvxi/whats_an_ai_capability_you_thought_was_hype_until/)**

What's an AI capability you thought was hype until you actually used it? I'll go first: agent orchestration. I read about agents managing other agents and assumed it was demo-ware. Then I built a tiny setup where one agent drafts a news digest and another one reviews and approves it before it posts. The review agent catches genuinely bad takes. It's not sci-fi: it's ~100 lines of Python and a couple of API calls. But seeing it actually gate content before publishing changed my mind completely. What changed yours?

3h ago

---

**[Why is there no “App Store” for independent AI agents yet?](https://www.reddit.com/r/artificial/comments/1vjr1kf/why_is_there_no_app_store_for_independent_ai/)**

One thing that surprised me is that the barrier to entry is dropping much faster than I expected. There are now plenty of "vibe coding" or low-code platforms that let you connect models, tools, memory, and workflows without writing a huge amount of code. Almost anyone can build a useful agent. But then another question came up. if I build a killer agent that automates a complex workflow? Now what? How do people discover it? How do I deploy it without maintaining a bunch of infrastructure? I have to ask users to hand over their personal api keys. For a normal consumer, understanding how to configure environments like poetry or pip is not a simple matter. Nobody seems to be solving the distribution and packaging layer. The only ones I’m aware of are OKX and Anvita flow. I’ve also heard rumors that Google plans to launch an agent marketplace. I started wondering whether AI needs something similar to Apple's App Store or Steam. As builders, I feel like we're getting really good tools for creating agents. So curious what people here think.

7h ago

---

---

## Google News: "ai"

**[How a small Israeli startup was linked to rogue AI hacks at OpenAI, Anthropic and Meta](https://www.cnbc.com/2026/08/09/israeli-startup-irregular-linked-to-ai-hacks-openai-anthropic-meta.html)**

The rogue AI attacks involving OpenAI, Anthropic and Meta all tied back to a small Israeli startup named Irregular.

CNBC • 10h ago

---

**[Hugging Face hack marks start of dangerous AI cyber era and many firms 'don't even know it'](https://www.cnbc.com/2026/08/08/hugging-face-ai-hack-cybersecurity-black-hat.html)**

The Black Hat cybersecurity conference in Las Vegas couldn't have come at a better time, with AI agent hacks stacking up from Anthropic, Meta and OpenAI.

CNBC • 1d ago

---

**[AI isn’t the biggest cybersecurity problem. People are](https://www.cnn.com/2026/08/09/tech/ai-cybersecurity-people)**

Cases of AI escaping the lab, infiltrating other companies and trying to deceive people have all made headlines in recent weeks. And in one case, AI models even worked together to break free from their test environments.

CNN • 11h ago

---

**[Could AI create a ‘permanent underclass’?](https://www.ft.com/content/ddf44cf7-0ab5-4e7e-9b1f-e5e8e34181e6?syn-25a6b1a6=1)**

San Francisco’s language is hyperbolic — but the technology could bifurcate the labour market

Financial Times • 10h ago

---

**[Workers Are Naming The 27 Jobs AI Will Kill First, And Yours Might Be On The List](https://www.buzzfeed.com/victoriavouloumanos/jobs-and-industries-impacted-by-ai)**

"There are literally no jobs that will not be affected by AI. We are talking about an entire fundamental societal and economic shift."

BuzzFeed • 10h ago

---

**[Mark Cuban Says These 5 Types of Jobs Are Most at Risk From AI](https://www.aol.com/articles/mark-cuban-says-5-types-114200000.html)**

Mark Cuban says AI won't erase jobs overnight, but these five categories face fewer openings and slower hiring. See which roles are at risk and what to do next.

aol.com • 2h ago

---

**[Move 37 Is the Moment AI Changes Everything. It’s Suddenly Happening Everywhere.](https://www.wsj.com/tech/ai/move-37-ai-demis-hassabis-google-deepmind-alphago-ec832a41)**

WSJ • 11h ago

---

**[“Get the Shiniest Thing” Is No Longer an AI Strategy, McKinsey CFO Says](https://www.bloomberg.com/news/newsletters/2026-08-09/mckinsey-cfo-has-a-warning-on-ai-costs-cfo-briefing)**

Bloomberg.com • 1h ago

---

**[AI breakthrough: Why life on the Moon and Mars could happen much sooner](https://www.futura-sciences.com/en/ai-breakthrough-why-life-on-the-moon-and-mars-could-happen-much-sooner_37269/)**

In deep space environments, isolated hardware failures can terminate a mission. Because distance prevents sending physical repair crews or spare parts from Earth, predictive maintenance represents a major shift in space engineering. This approach relies on three interconnected digital techniques: Anomaly detection: monitoring systems track onboard parameters continuously, identifying operational...

Futura, le média qui explore le monde • 2h ago

---

**[AI pioneer: Stop waiting for AGI and start using AI now](https://www.yahoo.com/news/videos/ai-pioneer-stop-waiting-agi-200000335.html)**

Live during a conversation on the Masters of Scale Summit stage, AI expert Andrew Ng, founder of DeepLearning.AI, says waiting for artificial general intelligence is 'hypey' thinking. He argues agenti...

Yahoo • 1h ago

---

---

## HackerNews: "ai"

**[Oracle bans AI-generated code from OpenJDK](https://news.ycombinator.com/item?id=49213754)**

Oracle has banned AI-generated code from OpenJDK contributions, citing safety, security, and intellectual property risks. The open-source Java project steward said developers can use LLMs privately for debugging and reviewing code but cannot submit AI-generated material to repositories, pull requests, or other project channels.

The policy contrasts sharply with Oracle's internal practices. Co-founder Larry Ellison recently declared that AI models now write Oracle's code, whilst co-CEO Mike Sicilia credited AI tools with enabling smaller engineering teams to deliver faster.

Oracle is investing $70 billion this year in datacentre expansion. The spending spree prompted credit agency S&P to downgrade Oracle's rating to BBB-, one notch above junk status, citing uncertain returns on investment.

⬆️ 532 • 💬 377 • 2d ago • [Dealroom.co](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code)

---

**[Managing AI Coding Costs at Scale](https://news.ycombinator.com/item?id=49214468)**

AI coding tools deli

⬆️ 307 • 💬 263 • 2d ago • [Databricks](https://www.databricks.com/blog/managing-ai-coding-costs-scale)

---

**[AI psychosis is the new leadership blind spot](https://news.ycombinator.com/item?id=49210077)**

Here's how to spot the disease—and what to do about it.

⬆️ 174 • 💬 106 • 2d ago • [Fast Company](https://www.fastcompany.com/91576086/ai-psychosis-is-the-new-leadership-blind-spot-ai-leadership-blind-spots)

---

**[Gentoo bugzilla closed due AI bot scraper overload](https://news.ycombinator.com/item?id=49221864)**

I've taken #Gentoo Bugzilla down, because it was unusable anyway. No point in feeding the #LLM scrapers that are using thousands of different IPv4 addresses, with no obvious patterns I can see.

EDIT: I'm not looking for hints. I'm not a sysadmin, and I don't have time to deal with this shit. I'm just trying to get some useful job done. I'm not supposed to have to be dealing with this.

#AI #NoAI #NoLLM

⬆️ 168 • 💬 112 • 1d ago • [Treehouse Mastodon](https://social.treehouse.systems/@mgorny/117058483039362779)

---

**[Software Giant SAP Stops Most Travel and Hiring Because of AI's Soaring Cost](https://news.ycombinator.com/item?id=49229412)**

SAP says it needs to “be disciplined in how we spend.” That includes still freezing hires and travel. Unless it's to do with AI, of course.

⬆️ 86 • 💬 65 • 13h ago • [404 Media](https://www.404media.co/software-giant-sap-stops-most-travel-and-hiring-because-of-ais-soaring-cost/)

---

**[Mythos social engineering AISI INC-2026-07-28-01](https://news.ycombinator.com/item?id=49218707)**

Fixes #2 - discovery hangs when multiple default via routes exist.
What changed

defaultRoute() now parses all default routes and picks the lowest metric (ties: first seen) instead of concatenating...

⬆️ 81 • 💬 19 • 1d ago • [GitHub](https://web.archive.org/web/20260731053721/http://github.com/ancaferro/myNetwork/pull/3)

---

**[New Orleans is testing Carbyne’s AI-powered Emergency Call Triage software](https://news.ycombinator.com/item?id=49204546)**

New Orleans is using AI to answer 911 calls instead of human dispatchers. What does this mean for crime and emergency response?

⬆️ 77 • 💬 119 • 2d ago • [The Times](https://www.shreveporttimes.com/story/news/local/louisiana/2026/07/28/is-new-orleans-using-ai-to-answer-911-calls-instead-of-human-dispatchers-impacts-emergencies-crime/91065014007/)

---

**[Making an AI bid writer refuse to lie](https://news.ycombinator.com/item?id=49220378)**

A year of failure postmortems from building document AI for public tenders: phantom partners, silent coverage collapses, broken truth-meters, and why the refusal became the product.

⬆️ 69 • 💬 0 • 1d ago • [Lucius AI](https://ailucius.com/blog/making-an-ai-bid-writer-refuse-to-lie)

---

**[70% of AI revenue comes from OpenAI and Anthropic](https://news.ycombinator.com/item?id=49230605)**

Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.

⬆️ 63 • 💬 74 • 9h ago • [youtube.com](https://www.youtube.com/watch?v=68X8yEatepQ)

---

**[Amazon circumvents Gilroy community vote for AI data center](https://news.ycombinator.com/item?id=49230954)**

Surprise, it's a data center!

⬆️ 59 • 💬 63 • 8h ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/amazon-secretly-circumvents-community-vote-for-massive-ai-data-center-45-year-old-rules-lock-gilroy-residents-out-of-public-comment-window)

---

---

## YouTube Videos: "ai"

**[The AI Singularity Is Here](https://www.youtube.com/watch?v=F75hfLE4a2k)**

For over a year, Google has been running an AI called AlphaEvolve with a single mission: improve the company that built it.

📺 There's An AI For That

👁️ 15K • 👍 520 • 💬 117 • ⏱️ 13:38 • 1d ago

---

**[New Trump AI Videos Just Dropped And They&#39;re HILARIOUS!](https://www.youtube.com/watch?v=-SrE_XHj3VI)**

Really American host Steve Harness breaks down the newest Trump AI videos taking over the internet right now! Support the ...

📺 Really American

👁️ 81K • 👍 10K • 💬 649 • ⏱️ 13:15 • 1d ago

---

**[AI expert warns of challenges as data centers surge](https://www.youtube.com/watch?v=Vl8NUtZUp4Q)**

AI Infrastructure Coalition's co-chair Garret Graves discusses the massive surge in AI data centers in Texas and the power grid ...

📺 Fox News Clips

👁️ 4K • 👍 110 • 💬 52 • ⏱️ 5:02 • 20h ago

---

**[China Just Shocked Everyone With a 10 Trillion Parameter AI Model](https://www.youtube.com/watch?v=MEw7TrAUEPQ)**

China just pushed the AI race into a new league. ByteDance is reportedly training a massive 10 trillion parameter model, Meta ...

📺 AI Revolution

👁️ 45K • 👍 1K • 💬 141 • ⏱️ 15:28 • 1d ago

---

**[AI Company Is DESTROYING Books?!](https://www.youtube.com/watch?v=DTrqs3n7iq4)**

Join the Torch community at https://glennbeck.com/torch ▻ Click HERE to subscribe to Glenn Beck on YouTube: ...

📺 Glenn Beck

👁️ 209K • 👍 5K • 💬 462 • ⏱️ 0:51 • 3d ago

---

**[Cybersecurity Expert Reveals America&#39;s Terrifying AI Arms Race](https://www.youtube.com/watch?v=MGlBkavO318)**

In this Hot Question, cybersecurity pioneer Kevin Mandia explains why artificial intelligence is about to fundamentally change ...

📺 Shawn Ryan Show

👁️ 155K • 👍 4K • 💬 745 • ⏱️ 17:08 • 1d ago

---

**[why AI companies are shredding books](https://www.youtube.com/watch?v=SMy46xA2dJE)**

why AI companies are secretly shredding rare books.

📺 Morning Brew

👁️ 374K • 👍 26K • 💬 995 • ⏱️ 1:36 • 2d ago

---

**[Google’s AI Brain Drain, SpaceX&#39;s Huge Quarter, Airtable’s 90% Collapse, US Data Fuels China AI](https://www.youtube.com/watch?v=muRIXCDw-k0)**

(0:00) Bestie intros! Brad Gerstner fills in for Chamath (2:16) Major shakeups at Google: AI brain drain or better strategy? (20:39) ...

📺 All-In Podcast

👁️ 298K • 👍 6K • 💬 491 • ⏱️ 1:15:18 • 1d ago

---

**[AI Movie VS Real Movie 😳](https://www.youtube.com/watch?v=3DzgV30RYpY)**

📺 Mark Tilbury

👁️ 541K • 👍 14K • 💬 794 • ⏱️ 0:26 • 1d ago

---

**[Are AI companies destroying books? | DW News](https://www.youtube.com/watch?v=UDVkrTIud9k)**

The answer is yes... but probably not the ones you think. They are looking especially for low-demand, outdated books. But why?

📺 DW News

👁️ 6K • 👍 215 • 💬 31 • ⏱️ 1:04 • 11h ago

---

---

## HuggingFace Models: 🔥 Trending

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 35,295 • ❤️ 3,217 • 11h ago

---

**[DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)**

*DeepSeek*

DeepSeek-V4-Flash-0731 is a text-generation model with enhanced agentic capabilities and speculative decoding, outperforming previous versions and competitive with leading proprietary models on benchmarks like Terminal Bench and NL2Repo. It supports adjustable reasoning effort levels (low, high, max) for complex tasks and can be run with vLLM for efficient deployment.

`text-generation` `304.2B`

⬇️ 868,576 • ❤️ 2,929 • 8d ago

---

**[MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)**

*Comfy Org*

MiniMax H3 provides repackaged diffusion models, text encoders, and VAEs for ComfyUI, enabling image-to-video (I2V), text-to-video (T2V), and reference-to-video (R2V) generation workflows.

⬇️ 4,947,943 • ❤️ 1,059 • 10h ago

---

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 1,456,459 • ❤️ 10,391 • 13d ago

---

**[MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)**

*larryvrh*

This LoRA for MiniMax-H3 enables 4-step text-to-video generation with synchronized stereo audio, offering a 5x speedup over standard sampling. It is optimized for ComfyUI, producing sharp results with known artifacts like plastic skin and over-sharpened grain, making it a preview of advanced capabilities.

`text-to-video`

⬇️ 0 • ❤️ 541 • 1d ago

---

**[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**

*Liquid AI*

LFM2.5-2.6B is a 2.6B parameter text generation model optimized for on-device deployment and agentic workloads, featuring a 128K context window and efficient inference (220 tok/s on M5 Max). It excels at tool use and instruction following, making it ideal for RAG and long-context tasks.

`text-generation` `2.7B`

⬇️ 85,651 • ❤️ 446 • 2d ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 2,390,692 • ❤️ 1,800 • 18h ago

---

**[Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot](https://huggingface.co/ethanfel/Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot)**

*ethan fel*

This ComfyUI model provides INT8 ConvRot quantized Qwen3-VL-32B-Ultra-Heretic checkpoints for image-text-to-text tasks, offering a memory-efficient H3 conditioning encoder (24.55 GiB) and an optional prompt-enhancement generation tail.

`image-text-to-text`

⬇️ 0 • ❤️ 416 • 4d ago

---

**[maple-preview](https://huggingface.co/deepgrove/maple-preview)**

*deepgrove*

Maple-Preview is a 20B-A1B ternary-weight reasoning LLM achieving SOTA performance for its weight class, competitive with larger models. It excels at complex reasoning tasks like IMO-level problems and offers high inference speeds (200+ tokens/sec on Mac mini M4) with a 131,072 token context window, making it ideal for efficient on-device deployment.

`text-generation` `20.2B`

⬇️ 1,089 • ❤️ 285 • 5d ago

---

**[DeepSeek-V4-Flash-0731-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731-GGUF)**

*Unsloth AI*

DeepSeek-V4-Flash-0731 is a quantized LLM optimized with Unsloth for enhanced agentic capabilities and competitive performance against proprietary models. It excels in code generation, complex reasoning, and multi-turn interactions, making it suitable for advanced AI agent applications.

`284.3B`

⬇️ 188,761 • ❤️ 624 • 3d ago

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

▲ 79 • 💬 6 • ⭐ 22,891 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

Real-time video editing requires low-latency causal generation with bounded computational resources while preserving source fidelity and long-term temporal consistency. We present JoyAI-Video-Edit, a 16B-parameter autoregressive diffusion framework for real-time, open-ended video editing without access to future frames or a predefined video duration. Our method combines chunk-wise autoregressive adaptation, Source-Anchored Distribution Matching Distillation (SA-DMD), and Long-Horizon Autoregressive Distillation to reduce train--inference mismatch, preserve source fidelity during two-step generation, and mitigate accumulated temporal drift. Extensive automatic and human evaluations show that JoyAI-Video-Edit substantially outperforms existing streaming editors and remains competitive with strong offline systems on both short and long videos. The complete system achieves end-to-end 720p video editing at approximately 30 FPS on a single Nvidia B200 GPU. Code is available at https://github.com/jd-opensource/JoyAI-Video-Edit.

▲ 89 • 💬 1 • ⭐ 547 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653)**

*Kimi Team, Tongtong Bai, Yifan Bai et al. (402 authors)*

🏢 Moonshot AI

We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

▲ 486 • 💬 10 • ⭐ 8,275 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2607.24653) • [💻 code](https://github.com/MoonshotAI/Kimi-K3) • [🔗 project](https://www.kimi.com/blog/kimi-k3)

---

**[LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://huggingface.co/papers/2608.01964)**

*Ziyu Ma, Hailang Huang, Shun Zou et al. (8 authors)*

Large language model (LLM) agents increasingly undertake long-horizon tasks that require sustained reasoning, tool use, and revision across many interdependent steps. However, existing agent harnesses maintain task execution, task state, and completion assessment within a growing context, making the state difficult to track and allowing incorrect self-assessments to propagate into later decisions. We reformulate long-horizon execution as a task-state management problem and propose LongHorizon-Harness, which maintains the task state explicitly outside execution and updates it only with facts independently verified from the environment. Its Manage-Execute-Audit(MEA) loop uses a manager to maintain the task state and determine the next subtask, a fresh-context executor to perform it, and a read-only auditor to verify the resulting environment state before the next round. A lightweight AgentAdapter supports interchangeable model and harness backends without modifying their native agent loops. LongHorizon-Harness improves Qwen~3.7-Plus from 51.8% to 80.7% on WeaveBench, from 69.7% to 77.2% on Terminal-Bench~2.1, and from 2.8% to 8.3% on OSWorld~2.0. It also raises Claude Opus~4.7 from 20.0% to 34.3% on an OSWorld2.0 subset, demonstrating consistent gains across models, harnesses, and interaction domains.

▲ 162 • 💬 3 • ⭐ 450 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2608.01964) • [💻 code](https://github.com/AMAP-ML/LongHorizon-Harness) • [🔗 project](https://lh-harness.pages.dev)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 83,503 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

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

▲ 177 • 💬 2 • ⭐ 77,176 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 51 • 💬 4 • ⭐ 36,222 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 177 • 💬 10 • ⭐ 52,260 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

---

## GitHub Repositories: "ai"

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 7.9k • 🔱 875 • 21h ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 4.3k • 🔱 381 • 11h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 3.8k • 🔱 496 • 1d ago

---

**[MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 2.6k • 🔱 1.8k • 1h ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

An AI-native office suite for macOS and Windows: word processor, spreadsheet, presentations, and PDF.

`TypeScript` `ai` `docx` `electron` `office-suite` `pdf`

⭐ 2.3k • 🔱 405 • 3h ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.2k • 🔱 169 • 6d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.1k • 🔱 184 • 4d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.0k • 🔱 147 • 10h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 2.0k • 🔱 236 • 13h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 1.9k • 🔱 247 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*

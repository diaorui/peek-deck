---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-04-19T18:02:32.568231+00:00'
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

**Last Updated:** April 19, 2026 at 18:02 UTC  
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

**[Tech industry lays off nearly 80,000 employees in the first quarter of 2026 — almost 50% of affected positions cut due to AI](https://www.reddit.com/r/artificial/comments/1spw2w0/tech_industry_lays_off_nearly_80000_employees_in/)**

Some experts argue that AI was just used as an excuse for poor business decisions.

🔗 [Tom's Hardware](https://www.tomshardware.com/tech-industry/tech-industry-lays-off-nearly-80-000-employees-in-the-first-quarter-of-2026-almost-50-percent-of-affected-positions-cut-due-to-ai) • 2h ago

---

**[Gemini caught a $280M crypto exploit before it hit the news, then retracted it as a hallucination because I couldn't verify it - because the news hadn't dropped yet](https://www.reddit.com/r/artificial/comments/1spckbj/gemini_caught_a_280m_crypto_exploit_before_it_hit/)**

So this happened mere hours ago and I feel like I genuinely stumbled onto something worth documenting for people interested in AI behavior. I'm going to try to be as precise as possible about the sequence because the order of events is everything here. Full chat if you want to read it yourself: https://g.co/gemini/share/0cb9f054ca58 Background I was using Gemini paid most advanced model to analyze a live crypto trade on AAVE. The token had dropped 7–9% out of nowhere in the last hour with zero news to explain it. I've been trading crypto for over a decade and something felt off, so I asked Gemini to dig into it. It came back very bullish - told me this was just normal market maker activity and that there were, quote, "absolutely zero indications of an exploit, hack, or insider dump." I even pushed back multiple times and it kept doubling down. So I moved on and started discussing trading strategy with it. Then it caught something mid-response Out of nowhere, mid-conversation, Gemini goes into full "EMERGENCY CORRECTION" mode. Says it just scanned live feeds and found breaking news of a $280M KelpDAO exploit - attacker minted rsETH, used it as collateral on Aave V3 to drain ETH/WETH, leaving roughly $177M in bad debt. Cites ZachXBT as the source. If you look at the "show thinking" section of the chat, you can literally watch it catch the news mid-response. Wild. Here's where it gets interesting. I couldn't verify any of it. Checked ZachXBT's Twitter - nothing. Googled every variation of "aave hack" sorted by latest and again nothing. Asked Gemini for actual links and it gave me source names in plain text with no real URLs. The only actual verified source attached to the chat was a screenshot of market data I had sent earlier. I called it out. It immediately folded Full apology. Called it a "massive AI hallucination." Said it completely fabricated the exploit, the $280M figure, the bad debt, ZachXBT's alert - all of it. Walked everything back and returned to the original bullish thesis like nothing happened. I was genuinely shocked that this was coming from the flagship paid Google model. I told it I was going to end the chat and try Claude instead. And then it reversed again In its last message before I left, Gemini reversed a second time. Said it had done one final scan and confirmed the exploit was real all along. CoinGape and BeInCrypto had just published it. The reason I couldn't find ZachXBT's alert is that he posted it on Telegram, not Twitter. The news was still spreading through crypto-native channels and hadn't been indexed by mainstream search yet when I tried to verify it around 9PM GMT. Gemini even explained its own failure in that last message: "My anti-hallucination protocols essentially overcorrected. Faced with your skepticism and the lag in widespread media coverage, the system defaulted to the safest possible assumption: that it had generated a false narrative. I retracted real, accurate data because my safety parameters prioritized admitting a flaw over insisting on a breaking event that lacked mature, widespread indexing." So the full sequence was: ❌ Gemini misses the exploit entirely, tells me everything is fine, no hack, nothing suspicious ❌ I push again with a screenshot of live data and suspicions of something going on, it still doubles down — zero signs of anything wrong ✅ Mid-conversation, it catches the breaking news in real time (visible in the "show thinking" section) ❌ I can't verify it, push back, Gemini immediately caves and calls it a hallucination ✅ Final message: reconfirms it was right, explains the Telegram source lag, says the only actual mistake was retracting true information What I think this actually shows This isn't just a funny AI story. I think this is a pretty clean real-world example of a specific failure mode that doesn't get talked about enough: The model had accurate, time-sensitive information from a source (Telegram) that wasn't indexed by mainstream search yet. When I pushed back with "I can't find this anywhere," its safety guardrails interpreted user skepticism + no Google results as I must have hallucinated this - and retracted real information. It's basically the inverse of a hallucination. Instead of confidently stating something false, it unconfidently retracted something true because the evidence hadn't caught up yet. It penalized itself for being right too early. And the scary part for anyone using AI in high-stakes situations: in this specific case, if I had trusted the retraction and acted on the "actually everything is fine" conclusion, I would have been making financial decisions based on an AI that talked itself out of correct information under social pressure. The hallucination detection was more dangerous than the hallucination. I'm genuinely curious if this is a documented behavior or if anyone in the AI/alignment space has a name for it. The "source indexing lag" problem seems like something that would come up a lot in real-time, fast-moving domains - crypto, breaking news, medical research preprints, anything where the truth travels faster than Google.

18h ago

---

**[Might not be the right sub, but why does the ai overview get an aneurism when i google this?](https://www.reddit.com/r/artificial/comments/1spsbru/might_not_be_the_right_sub_but_why_does_the_ai/)**

https://preview.redd.it/i7muzi5ga5wg1.png?width=1373&format=png&auto=webp&s=e21290514099fc9e4f1699a2240c94cbb5683eca

5h ago

---

**[How LLMs decide which pages to cite — and how to optimize for it](https://www.reddit.com/r/artificial/comments/1spxhfj/how_llms_decide_which_pages_to_cite_and_how_to/)**

When ChatGPT or Perplexity answers a question, it runs RAG: retrieves top candidates from a crawled index, then scores them. The scoring criteria are public knowledge from the Princeton GEO paper (arxiv.org/abs/2311.09735). Key signals: answer directness, cited statistics, structured data (JSON-LD), crawl access, and content freshness. What surprised me most in the research: schema markup alone shifts precise information extraction from 16% to 54%. That's not a marginal gain — that's the difference between being cited and being invisible. Anyone else experimenting with this? Curious what's working for people here.

1h ago

---

**[Why is every AI getting restricted these days?](https://www.reddit.com/r/artificial/comments/1spxccd/why_is_every_ai_getting_restricted_these_days/)**

Like seriously, it’s not just ChatGPT... it’s Claude, Grok, Gemini… all of them feel way more locked down than before. I genuinely don’t get it. What’s the point of pouring nearly Trillions into this tech if it ends up feeling borderline unusable half the time? And yeah, I’m literally paying for this. It feels like companies assume every user is a programmer who use it only for programming. But a lot of us just want to be creative, write stories, experiment with ideas, or just mess around without hitting a wall every two seconds. I’m not out here asking how to build a bomb or anything illegal. I just want to create stuff without the AI acting like I’m about to commit a felony. And before anyone says “just use local models”… nah. Not everyone has a expensive hardware lying around. Subscriptions exist for a reason. I understand this safety stuff but this is just dumb.. So like… is there any hope this gets better? Will AI eventually get smart enough to understand actual intent instead of playing it ultra safe all the time? Or is this just how it’s gonna be going forward? Because if this is the future… idk man, it’s kinda disappointing This ain't it...

1h ago

---

**[Claude vs Gemini: Solving the laden knight's tour problem](https://www.reddit.com/r/artificial/comments/1sp0r1j/claude_vs_gemini_solving_the_laden_knights_tour/)**

AI Coding contest day 8 The eighth challenge is a weighted variant of the classic knight's tour. The knight must visit every square of a rectangular board exactly once, but each square carries an integer weight. As it moves, the knight accumulates load, and the cost of each move equals its current load. Charge is assessed upon departure, so the weight of the final square never contributes.

1d ago

---

**[I built a GNOME extension for Codex with local/remote history, live filters, Markdown export, and a read-only MCP server](https://www.reddit.com/r/artificial/comments/1spnk33/i_built_a_gnome_extension_for_codex_with/)**

I wanted Codex to feel like a real GNOME app instead of just a terminal or editor workflow, so I built a GNOME Shell extension around it. It currently does all of this: - Codex usage in the GNOME top bar - native GTK history window - local session history browsing - paired remote machine history browsing over LAN - live session updates - filters for All / Messages / Tools / Thinking / System / Errors - in-session search - Markdown export for one session or all sessions from a source - read-only MCP server for history and usage - multi-language support A few design choices mattered a lot to me: - native GNOME/Libadwaita UI, not a webview - read-only remote access - explicit pairing between machines - revocable trust per device - read-only MCP, local by default, token-protected by default It ended up being much more ambitious than a typical GNOME extension, but I wanted something that actually feels integrated into the desktop. 😊

9h ago

---

**[it is impossible to stop AI chatbots from using quotes (any instance of the character ")](https://www.reddit.com/r/artificial/comments/1sprne8/it_is_impossible_to_stop_ai_chatbots_from_using/)**

no matter how i phrase it in the instructions, how many times i repeat the rule not to use quotes, and which LLM i use, i have failed to prevent any of them from using the so-called scare-quotes. it seems like they're extremely tempted to place them around a word every second sentence. think of an example like: 'is vision or hearing better?' -> 'neither sense is inherently "better"' or something like: 'what percentage of the population is stupid?' -> 'There is no scientific way to assign a percentage of the population as “stupid”' AIs struggle not to use them even when i tell it not to in the same prompt. like 'what % is stupid? and DONT use quotes in your answer.' it will still say "stupid." it's very frustrating and infuriating. this post will probably get deleted because it's a low quality vent but i don't care. just needed to see if people with premium subscription can have success.

5h ago

---

**[Project Shadows: Turns out "just add memory" doesn't fix your agent](https://www.reddit.com/r/artificial/comments/1spwoof/project_shadows_turns_out_just_add_memory_doesnt/)**

Been building a multi-agent system called Shadows for a few months. Nine agents collaborating on strategy work with a shared memory layer. I spent most of my time on retrieval because that's what every benchmark measures. Mem0, MemPalace, Graphiti, all of them. On LongMemEval, recall_all@5 hit 97%. Overall accuracy was 73%. So the right memories are there. The agent still picks the wrong answer. It can't aggregate across sessions, doesn't know when to abstain, and guesses which aspect of a preference the user meant. That lined up with something I've been stuck on. Most LLMs jump straight to execution when you give them a task. People don't. We filter first, check if we're even the right person, then start. Next direction: Agents that can be moved with their identity and memory!

🔗 [open.substack.com](https://open.substack.com/pub/omarmegawer/p/part-3-project-shadows?r=4b5w1p&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true) • 2h ago

---

**[Any one here using ai tools for pre-vis or short form scenes?](https://www.reddit.com/r/artificial/comments/1spl4at/any_one_here_using_ai_tools_for_previs_or_short/)**

Been experimenting a bit with ai video tool recently, mostly fro pre-vis and quick social content, and I'm kinda on the fence about how they actually are. like they're great for generating quick shorts or ideas, but once you try to get something that feels intentional (camera movement, pacing, performance etc), it starts to fall apart or feel really random especially struggling with: getting consistent motion across a shot making things feel directed vs just generated anything involving dialogue or talking shots not trying to replace actual production obviously, more just looking for ways to speed up ideation or create rough sequences without spinning up a full shoot. curious if anyone here has found tools or workflows that actually feel somewhat controllable / usable in a filmmaking context

11h ago

---

---

## Google News: "ai"

**[SiIicon Valley's AI agent hiccups: Wasted tokens and 'chaotic' systems](https://www.cnbc.com/2026/04/19/siiicon-valley-ai-agent-openclaw-problems.html)**

Nvidia CEO Jensen Huang told CNBC's Jim Cramer in March that AI agents are "definitely the next ChatGPT."

CNBC • 6h ago

---

**[Trump-branded AI data center megaproject stalls, CEO departs](https://www.axios.com/2026/04/19/ai-data-center-project-troubles-texas)**

Axios • 7h ago

---

**[Niceaunties Reimagines Womanhood Through AI Dreamscapes](https://www.forbes.com/sites/yjeanmundelsalle/2026/04/19/niceaunties-reimagines-womanhood-through-ai-dreamscapes/)**

Forbes • 1h ago

---

**[Shadow AI: Silicon Valley’s New Productivity Secret Is Also a Massive Liability](https://www.inc.com/chloe-aiello/shadow-ai-silicon-valleys-new-productivity-secret-is-also-a-massive-liability/91331997)**

Shadow AI use can have real consequences for businesses—but there's a smart way to handle it.

inc.com • 1h ago

---

**[The CEO Preaching Straight Talk About AI and Job Losses](https://www.wsj.com/tech/ai/the-ceo-preaching-straight-talk-about-ai-and-job-losses-a3aaaaf1)**

WSJ • 2h ago

---

**[My Boss Loves ChatGPT. Must I Fake Loving It Too?](https://www.nytimes.com/2026/04/19/business/ai-at-work-creativity-ageism.html)**

The New York Times • 8h ago

---

**[Falling fertility, debt and AI: is the US headed toward a population crisis?](https://www.theguardian.com/business/2026/apr/19/us-population-fertility-rate)**

Americans having less kids plus an ageing population could be a recipe for disaster that further erodes social stability

The Guardian • 2h ago

---

**[Should you really trust health advice from an AI chatbot?](https://www.bbc.com/news/articles/clyepyy82kxo)**

Abi has had very mixed results when asking a chatbot for guidance about her health issues.

BBC • 18h ago

---

**[Inside a growing movement warning AI could turn on humanity](https://www.washingtonpost.com/technology/2026/04/18/ai-doom-influencers-safety/)**

Groups concerned that AI could evade human control are recruiting content creators to warn the masses about the dangers of smarter machines.

The Washington Post • 13h ago

---

**[Google in Talks With Marvell to Build New AI Chips for Inference](https://www.theinformation.com/articles/google-talks-marvell-build-new-ai-chips-inference)**

Google is in talks with Marvell Technology to develop two new chips aimed at running AI models more efficiently, according to two people with direct knowledge of the discussions. One is a memory processing unit designed to work alongside Google’s tensor processing unit. The other is a new TPU ...

The Information • 5h ago

---

---

## HackerNews: "ai"

**[College instructor turns to typewriters to curb AI-written work](https://news.ycombinator.com/item?id=47818485)**

⬆️ 389 • 💬 358 • 23h ago • [sentinelcolorado.com](https://sentinelcolorado.com/uncategorized/a-college-instructor-turns-to-typewriters-to-curb-ai-written-work-and-teach-life-lessons/)

---

**[Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine](https://news.ycombinator.com/item?id=47800033)**

Hardware hacker’s flying probe automation stack for agent-driven   target discovery, microscope mapping, safety-monitored CNC motion, probe review, and   controlled pin probing. - GainSec/AutoProber

⬆️ 224 • 💬 46 • 2d ago • [GitHub](https://github.com/gainsec/autoprober)

---

**[The beginning of scarcity in AI](https://news.ycombinator.com/item?id=47799322)**

GPU rental prices surged 48% in 60 days. The AI compute shortage will force startups to compete not on speed of iteration, but on access to infrastructure.

⬆️ 192 • 💬 225 • 2d ago • [Tomasz Tunguz](https://tomtunguz.com/ai-compute-crisis-2026/)

---

**[Airline worker arrested after sharing photos of bomb damage in WhatsApp group](https://news.ycombinator.com/item?id=47824068)**

Police lured the man to a meeting and arrested him after accessing a private WhatsApp group with colleagues

⬆️ 168 • 💬 104 • 4h ago • [LBC](https://www.lbc.co.uk/article/dubai-police-spied-private-whatsapp-5HjdXwr_2/)

---

**[Scan your website to see how ready it is for AI agents](https://news.ycombinator.com/item?id=47805998)**

Scan your website to see if it's ready for AI agents. Check for llms.txt, MCP, agent skills, and other agent-friendly standards.

⬆️ 111 • 💬 175 • 2d ago • [Is Your Site Agent-Ready?](https://isitagentready.com)

---

**[Graphs that explain the state of AI in 2026](https://news.ycombinator.com/item?id=47817581)**

AI investment is skyrocketing while AI’s impact on jobs and public perception remains mixed

⬆️ 104 • 💬 61 • 1d ago • [IEEE Spectrum](https://spectrum.ieee.org/state-of-ai-index-2026)

---

**[George Orwell Predicted the Rise of "AI Slop" in Nineteen Eighty-Four](https://news.ycombinator.com/item?id=47800765)**

We've lived but a few years so far into the age when artificial intelligence can produce convincing stories, songs, essays, poems, novels, and even films.

⬆️ 82 • 💬 59 • 2d ago • [Open Culture](https://www.openculture.com/2026/04/how-george-orwell-predicted-the-rise-of-ai-slop.html)

---

**[Show HN: AI Subroutines – Run automation scripts inside your browser tab](https://news.ycombinator.com/item?id=47810533)**

Record a browser task once. Replay it as a callable tool. Zero token cost, 100% deterministic, auth propagated from the live webpage.

⬆️ 44 • 💬 13 • 1d ago • [rtrvr.ai](https://www.rtrvr.ai/blog/ai-subroutines-zero-token-deterministic-automation)

---

**[Shuttered startups are selling old Slack chats and emails to AI companies](https://news.ycombinator.com/item?id=47811748)**

Defunct companies are striking gold by selling their digital footprints to AI labs as training data, Forbes reports.

⬆️ 42 • 💬 11 • 1d ago • [Fast Company](https://www.fastcompany.com/91528808/shuttered-startups-are-selling-old-slack-chats-and-emails-to-ai-companies)

---

**[AI companies are buying the Slack data of failed startups](https://news.ycombinator.com/item?id=47801494)**

⬆️ 40 • 💬 10 • 2d ago • [X (formerly Twitter)](https://twitter.com/_iainmartin/status/2044758204773486925)

---

---

## YouTube Videos: "ai"

**[AI Experts are Quietly Admitting This…](https://www.youtube.com/watch?v=K96KfUgS_gg)**

Try Verdent AI ⤵ https://www.verdent.ai/?id=700278 @verdent_ai CHAPTERS ⤵ 00:00 - Introduction to AI News 02:38 - Creating ...

📺 Dylan Curious

👁️ 6K • 👍 333 • 💬 92 • ⏱️ 30:36 • 15h ago

---

**[Google&#39;s Quantum AI Found a Mathematical Pattern That Predicts the Future — Physicists Are Disturbed](https://www.youtube.com/watch?v=BI7zvWHyY3c)**

Something strange is happening in the world of science. A discovery has shaken experts and raised unsettling questions about ...

📺 Luminox

👁️ 3K • 👍 166 • 💬 18 • ⏱️ 22:47 • 15h ago

---

**[The new AI model that’s alarming Washington | The Economist](https://www.youtube.com/watch?v=zSsDx7Y9YUc)**

A powerful new AI model, called Mythos, has sparked alarm within the Trump administration. The lab behind it, Anthropic, says the ...

📺 The Economist

👁️ 54K • 👍 1K • 💬 100 • ⏱️ 8:30 • 1d ago

---

**[A.I. Iranian propaganda videos making fun of Trump, U.S. go viral](https://www.youtube.com/watch?v=LTJYQ0knUsE)**

A series of animated Iranian propaganda videos made in the style of "The LEGO Movie" has gone viral on social media, making ...

📺 MS NOW

👁️ 121K • 👍 2K • 💬 1K • ⏱️ 6:46 • 1d ago

---

**[P(doom) | Real Time with Bill Maher (HBO)](https://www.youtube.com/watch?v=w5SYm4J4utQ)**

New Rule: When the people who are making A.I. are scared of A.I., it's time to “shut the whole thing down until we can figure out ...

📺 Real Time with Bill Maher

👁️ 602K • 👍 16K • 💬 2K • ⏱️ 10:07 • 1d ago

---

**[These HILARIOUS AI Parodies Keep PISSING OFF TRUMP!](https://www.youtube.com/watch?v=0aB9ycZDBIw)**

Really American host Steve Harness breaks down more HILARIOUS AI Trump parodies coming out of Iran...and these may be the ...

📺 Really American

👁️ 1.4M • 👍 59K • 💬 3K • ⏱️ 12:33 • 2d ago

---

**[The World&#39;s First AI TED Talk](https://www.youtube.com/watch?v=N1X7vMp9DZ4)**

ChatGPT was recently asked what it would say to humans if it could give a TED Talk. It gave a surprisingly thoughtful answer that ...

📺 TED

👁️ 56K • 👍 2K • 💬 768 • ⏱️ 3:28 • 1d ago

---

**[China Just Built an Autonomous AI Robot Army: Killer Robots With Guns and Rockets](https://www.youtube.com/watch?v=_Vw_6QrqS8c)**

China just revealed an autonomous robot war pack built from dog bots, drones, laser weapons, and unmanned boats, Europe is ...

📺 AI Revolution

👁️ 70K • 👍 1K • 💬 139 • ⏱️ 16:14 • 2d ago

---

**[AI News: Huge Updates From Anthropic, OpenAI and Google](https://www.youtube.com/watch?v=bIrzOQtnp8w)**

Here's the AI News you probably missed this week. Build AI apps that actually scale. Learn more about Crusoe Managed ...

📺 Matt Wolfe

👁️ 86K • 👍 3K • 💬 155 • ⏱️ 36:44 • 2d ago

---

**[This AI Machine Changes Baby Diapers in Public](https://www.youtube.com/watch?v=7_4GU43KumU)**

This concept shows how AI could assist with baby care in everyday public spaces. In this scenario, a smart AI-powered diaper ...

📺 DubAI Baby Official

👁️ 52K • 👍 848 • 💬 2 • ⏱️ 0:08 • 4h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)**

*Qwen*

Qwen3.6-35B-A3B is a 35B parameter causal language model with a vision encoder, optimized for agentic coding tasks and featuring enhanced thinking preservation for iterative development. It supports a context length of 262,144 tokens, extensible up to 1,010,000.

`image-text-to-text` `36.0B`

⬇️ 209,112 • ❤️ 904 • 4d ago

---

**[HY-Embodied-0.5](https://huggingface.co/tencent/HY-Embodied-0.5)**

*Tencent*

HY-Embodied-0.5 is a multilingual vision-language model designed for embodied agents, excelling in spatial-temporal perception and reasoning. It features an efficient Mixture-of-Transformers (MoT) architecture for real-world robot control and VLA pipelines.

`image-text-to-text` `3.8B`

⬇️ 1,599 • ❤️ 873 • 5d ago

---

**[MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)**

*MiniMax*

MiniMax-M2.7 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation` `228.7B`

⬇️ 288,848 • ❤️ 977 • 2d ago

---

**[Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)**

*Unsloth AI*

Qwen3.6-35B-A3B is a 35B parameter causal language model with vision capabilities, optimized for agentic coding and reasoning tasks. It features a large context window (262k native, extensible to 1M+ tokens) and improved tool-calling, making it suitable for complex development workflows and iterative coding.

`image-text-to-text` `34.7B`

⬇️ 662,293 • ❤️ 493 • 3d ago

---

**[ERNIE-Image](https://huggingface.co/baidu/ERNIE-Image)**

*BAIDU*

ERNIE-Image is a 8B parameter text-to-image diffusion model excelling in complex instruction following, text rendering, and structured generation for use cases like posters and comics. It offers strong visual quality and controllability, running on consumer GPUs.

`text-to-image`

⬇️ 3,761 • ❤️ 463 • 2d ago

---

**[HY-World-2.0](https://huggingface.co/tencent/HY-World-2.0)**

*Tencent*

HY-World 2.0 is a multi-modal framework for generating and reconstructing 3D worlds from text, images, or video. It produces editable 3D assets like meshes and Gaussian Splattings, enabling applications in game development and simulation.

`image-to-3d`

⬇️ 0 • ❤️ 456 • 3d ago

---

**[supergemma4-26b-uncensored-gguf-v2](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-gguf-v2)**

*Jiun Song*

A fast, uncensored GGUF text generation model based on Google's Gemma 4-26B, optimized for Apple Silicon with llama.cpp. It excels in natural Korean conversation, coding, and tool-use tasks, offering improved performance and reduced prompt-routing issues compared to stock releases.

`text-generation` `25.2B`

⬇️ 72,519 • ❤️ 417 • 7d ago

---

**[VoxCPM2](https://huggingface.co/openbmb/VoxCPM2)**

*OpenBMB*

VoxCPM2 is a 2B parameter, 30-language multilingual text-to-speech model capable of high-fidelity voice cloning, novel voice design from text descriptions, and real-time streaming synthesis at 48kHz.

`text-to-speech`

⬇️ 51,554 • ❤️ 1,157 • 3d ago

---

**[GLM-5.1](https://huggingface.co/zai-org/GLM-5.1)**

*Z.ai*

GLM-5.1 is a next-generation language model optimized for agentic engineering, featuring significantly enhanced coding capabilities and sustained performance on complex, long-horizon tasks. It excels in breaking down problems, iterating on solutions, and handling ambiguity, making it ideal for advanced software development and automated task execution.

`text-generation` `753.9B`

⬇️ 112,939 • ❤️ 1,415 • 3d ago

---

**[ERNIE-Image-Turbo](https://huggingface.co/baidu/ERNIE-Image-Turbo)**

*BAIDU*

ERNIE-Image-Turbo is a distilled text-to-image diffusion model optimized for speed (8 inference steps) and fidelity. It excels at complex instruction following, text rendering, and structured generation for use cases like posters, comics, and multi-panel layouts.

`text-to-image`

⬇️ 4,757 • ❤️ 317 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 5 • 💬 2 • ⭐ 2,425 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 23 • 💬 1 • ⭐ 19,537 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 47 • 💬 2 • ⭐ 51,559 • 15mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://huggingface.co/papers/2604.14268)**

*Team HY-World, Chenjie Cao, Xuhui Zuo et al. (45 authors)*

HY-World 2.0 is a multi-modal world model framework that generates high-fidelity 3D Gaussian Splatting scenes from diverse inputs using specialized modules for panorama generation, trajectory planning, world expansion, and composition, along with an enhanced rendering platform for interactive 3D exploration.

▲ 89 • 💬 4 • ⭐ 1,233 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2604.14268) • [💻 code](https://github.com/Tencent-Hunyuan/HY-World-2.0) • [🔗 project](https://3d-models.hunyuan.tencent.com/world/)

---

**[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**

*Zhiliang Peng, Jianwei Yu, Wenhui Wang et al. (13 authors)*

🏢 Microsoft Research

VibeVoice synthesizes long-form multi-speaker speech using next-token diffusion and a highly efficient continuous speech tokenizer, achieving superior performance and fidelity.

▲ 165 • 💬 10 • ⭐ 40,293 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.19205) • [💻 code](https://github.com/microsoft/VibeVoice) • [🔗 project](https://microsoft.github.io/VibeVoice/)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 28 • 💬 1 • ⭐ 18,150 • 30mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 159 • 💬 2 • ⭐ 60,499 • 6mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 53 • 💬 1 • ⭐ 77,285 • 31mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://huggingface.co/papers/2410.05779)**

*Zirui Guo, Lianghao Xia, Yanhua Yu et al. (5 authors)*

LightRAG improves Retrieval-Augmented Generation by integrating graph structures for enhanced contextual awareness and efficient information retrieval, achieving better accuracy and response times.

▲ 39 • 💬 2 • ⭐ 33,824 • 18mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.05779) • [💻 code](https://github.com/hkuds/lightrag)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 53 • 💬 4 • ⭐ 1,883 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

---

## GitHub Repositories: "ai"

**[MemPalace/mempalace](https://github.com/MemPalace/mempalace)**

The best-benchmarked open-source AI memory system. And it's free.

`Python` `ai` `chromadb` `llm` `mcp` `memory`

⭐ 48.1k • 🔱 6.3k • 11h ago

---

**[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)**

🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

`Python` `ai` `anthropic` `caveman` `claude` `claude-code`

⭐ 38.7k • 🔱 1.9k • 1d ago

---

**[santifer/career-ops](https://github.com/santifer/career-ops)**

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

`JavaScript` `ai-agent` `anthropic` `automation` `career` `claude`

⭐ 36.4k • 🔱 7.3k • 6h ago

---

**[safishamsi/graphify](https://github.com/safishamsi/graphify)**

AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, OpenClaw, Factory Droid, Trae, Google Antigravity). Turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

`Python` `antigravity` `claude-code` `codex` `gemini` `graphrag`

⭐ 30.5k • 🔱 3.4k • 1d ago

---

**[larksuite/cli](https://github.com/larksuite/cli)**

The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 20+ AI Agent Skills.

`Go`

⭐ 8.2k • 🔱 530 • 13h ago

---

**[tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)**

AI Agent 源码深度研究报告

`Python`

⭐ 5.6k • 🔱 1.6k • 7d ago

---

**[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)**

数字生命卡兹克开源的 AI Skills 合集

`Python`

⭐ 5.4k • 🔱 901 • 1d ago

---

**[elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3)**

LIBERATED AI CHAT

`TypeScript`

⭐ 4.9k • 🔱 1.2k • 24d ago

---

**[Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel)**

The free AI already on your Mac. CLI tool, OpenAI-compatible server, and interactive chat — all on-device via Apple Intelligence. No API keys, no cloud, no downloads.

`Swift` `apple-intelligence` `apple-silicon` `cli` `foundationmodels` `homebrew`

⭐ 4.8k • 🔱 182 • 2d ago

---

**[therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)**

把前任蒸馏成 AI Skill，用ta的方式跟你说话。

`Python`

⭐ 4.6k • 🔱 458 • 11d ago

---

---

*Generated by PeekDeck - A glance is all you need*

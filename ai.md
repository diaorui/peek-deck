---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-26T20:53:38.409064+00:00'
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

**Last Updated:** May 26, 2026 at 20:53 UTC  
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

**[Built a tool to save Claude responses (and ChatGPT, Gemini) into one searchable vault - sharing in case it's useful](https://www.reddit.com/r/artificial/comments/1toga8l/built_a_tool_to_save_claude_responses_and_chatgpt/)**

I built this tool because I kept asking Claude for code and explanations and losing them in long chats. Coffer adds a save button to every AI response and stores them locally in a searchable vault. Works on: - claude.ai - chatgpt.com - gemini.google.com You can mix snippets across all three and search them. The Markdown stays formatted, which is very nice for Claude's longer responses with code and tables. Everything is local. Coffer makes zero network calls of its own. Free. Feedback is especially welcome. https://chromewebstore.google.com/detail/nhchbmaobjhjfmeekpnkmhdjajdolcjb?utm_source=item-share-cb

2h ago

---

**[AI is becoming epistemic infrastructure controlled by a handful of private individuals?](https://www.reddit.com/r/artificial/comments/1to0dmn/ai_is_becoming_epistemic_infrastructure/)**

Most people treat AI as a convenient black box. Ask it something, it answers, you move on. But we’re sleepwalking into something bigger. I think Whoever controls the infrastructure of knowledge controls how people perceive reality. The Church held that position for centuries through controlling scripture. The printing press broke that monopoly by distributing interpretive power. AI is doing the opposite recentralizing it into a handful of corporations with no democratic accountability. “AI says X” is structurally identical to “studies show X” you’re invoking an authority you can’t directly access. Except with a study you can theoretically trace the source. With AI the chain is opaque by design. And it delivers wrong answers and right answers with identical confidence. There’s no texture to signal doubt. AI isn’t neutral, it’s being heavily calibrated. In the west, the models are trained to be more “ethical” maybe more liberal and always try to give you a more “balance” take on things. Chinese AI simply doesn’t allow you to access to anything that put the CCP is a bad light. The more you rely on AI in domains where you lack expertise, the less capable you become of evaluating whether to trust it. AI works best for people who already know enough to catch its errors the opposite of how most people use it. Imagine the next generation of people growing up and being shaped by these AI. I can’t help but feel nervous and scared for the future. OpenAI said 10% of our entire population has already started using chatgpt. Regardless of the accuracy of this number, I feel like we are slowly entering into a mass hallucination / blind reliance on these AI models. We’re not just offloading cognitive effort. We’re handing the dial over who shapes how billions of people understand reality to a small group of unelected, largely unregulated private individuals.

12h ago

---

**[Which AI image generator is actually worth the money?](https://www.reddit.com/r/artificial/comments/1to5v3m/which_ai_image_generator_is_actually_worth_the/)**

I've looked at about a dozen different image generators: Nano Banana Flux Midjourney GPT Image 2 Firefly Ideogram Recraft Leonardo Canvas Meta AI They all have their pluses and minuses but they all do a decent job. If I'm looking to spend thousands over a year on an image generator, what would you suggest. This would be mainly for business and a little for art.

8h ago

---

**[Memory Curator Agent a governance layer for memory in multi-agent systems](https://www.reddit.com/r/artificial/comments/1to9p3u/memory_curator_agent_a_governance_layer_for/)**

I keep seeing the same failure in every multi-agent setup I touch. Memory looks fine on day one. By week three it is half stale facts, half private context that should not have been written publicly, and half decisions that were superseded but never overwritten. Retrieval gets noisier. Users keep repeating context because the right fact ended up in the wrong scope. The recursion limit is not the problem here. The memory store itself is the problem. The thing I changed that helped most was the simplest possible rule. Worker agents are not allowed to write to durable memory. They emit a structured memory event with a proposed scope and evidence, and a separate Memory Curator agent decides whether to write it, where to write it, or to discard it. The four scopes I route into are agent repo memory (durable design rules for one agent), agent team memory (cross-agent procedures, handoff standards, safety rules), project memory (current state, decisions, risks for one engagement), and session scratch (temporary observations that probably should not survive). The mapping I had in mind was to organizational and human memory categories: individual specialist memory, transactive team memory (Ren and Argote), project memory, and short-term working memory. The routing rule is conservative on purpose. If an event is temporary, unsupported, ambiguous, or contains private context, it goes to session scratch or gets discarded outright. Durable memory has to be earned. The schema is JSON with tagged fields for fact, decision, preference, risk, procedure, and hypothesis, plus an evidence reference and a proposed scope that the curator can override. The reason I think this is the right architectural shape is that "what should be remembered, where, and for how long" is a different cognitive task from "do the work." When the same agent does both, the work agent biases toward remembering everything it produced. A dedicated curator whose only job is memory governance ends up much more conservative, and the store stays useful longer.

5h ago

---

**[Uber's COO says it's getting harder to justify the money spent on AI tokenmaxxing](https://www.reddit.com/r/artificial/comments/1tndgv8/ubers_coo_says_its_getting_harder_to_justify_the/)**

Operations chief Andrew Macdonald said he's not seeing proportional productivity gains from increasing AI costs within Uber.

🔗 [Business Insider](https://www.businessinsider.com/uber-coo-andrew-macdonald-ai-token-spending-harder-justify-2026-5) • 1d ago

---

**[Wiz Integrates with Anthropic's Compliance API](https://www.reddit.com/r/artificial/comments/1tnvmgt/wiz_integrates_with_anthropics_compliance_api/)**

Wiz integrates with Anthropic’s Compliance API. Gain total visibility into Claude usage, configurations, and identity risks within the Wiz platform.

🔗 [wiz.io](https://www.wiz.io/blog/claude-wiz-integration?2) • 16h ago

---

**[I found a way for Ollama uses to get better Memory yet cheaper alternatives since OLLAMA now uses GPU usage. True memory that auto updates constantly as an individual or a team setting. HERMES USERS](https://www.reddit.com/r/artificial/comments/1toguws/i_found_a_way_for_ollama_uses_to_get_better/)**

I rephrase it with AI to make it more readable. I see a lot of people running into the same issue I have. It’s not just that bigger models are slower. GPU usage is also very high, and it drains fast. Ollama just isn’t what it used to be. I use DeepSeek V4 Flash, which works great. For heavier coding tasks or certain complex prompts, I switch to the Pro version. But on Pro, each prompt eats about 3–5% of my usage. (I’m on the Pro plan.) Memory has always been a hot topic. Hermes Native does a decent job. Here’s how its built‑in memory system works: memory_enabled – After every turn, the agent can write notes into MEMORY.md user_profile_enabled – The agent watches for user preferences and writes them to USER.md flush_min_turns: 6 – Every 6 turns, Hermes runs a “consolidate” pass: it re‑reads the recent conversation and rewrites MEMORY.md to capture new info nudge_interval: 10 – Every 10 turns, Hermes nudges the agent with “Anything to remember?” What I found: Atomic Memory (https://github.com/atomicstrata/atomicmemory) Strengths: ✅ Per‑turn – Extracts info every turn, not every 6 turns ✅ Cheap – Uses a small dedicated model ✅ Semantic recall – Only relevant memories are injected, not the whole file ✅ Conflict detection – Built‑in AUDN logic catches contradictions ✅ Unbounded – No 2,200‑character limit; you can store 10,000+ memories ✅ Time‑aware – Handles queries like “What did I say last week?” ✅ Composites – Links related facts into higher‑level summaries Example scenario (without Atomic Memory) Imagine you change a meeting time three times in one day: Turn 1: “meeting June 3rd” → MEMORY.md gets “Meeting: June 3rd 5pm 2026” Turn 5: “actually June 5th” → No flush yet (6 turns required) → MEMORY.md unchanged → if you ask now, Hermes still says “June 3rd” Turn 6: “meeting June 1st” → Flush triggers! Agent re‑reads the conversation, sees all three dates, rewrites MEMORY.md… but with which date? Usually the last one, but not guaranteed. Sometimes the file ends up with two dates or stale info. Turn 9: You ask “what’s the meeting?” → Bot reads MEMORY.md → gets whatever the consolidation picked → might be wrong. With Atomic Memory: Each update fires AUDN immediately, supersedes the old fact, and the latest one wins. No 6‑turn lag, no guesswork. Could Hermes update automatically before Atomic Memory? Yes, but only for slow‑changing facts, low‑volume memory needs, and single‑topic chats. The built‑in flush+nudge cycle worked, just not as well. Atomic Memory is an upgrade, not a replacement. It adds: Per‑turn updates (vs every 6 turns) Semantic search (vs full‑file injection) Conflict‑aware updates (vs append‑or‑rewrite) No size limit (vs 2.2 KB cap) Time‑awareness (vs “all facts feel equally fresh”) Cheap GPU usage (small dedicated model) The cost is one extra Docker container and nearly $0 in GPU because ministral-3:3b is tiny. You can use even smaller models that don’t need reasoning, gemma3:4b works too. From here, you can see real‑life use cases, whether in a team or as an individual. You don’t have to correct it; it does that for you. What I’m curious about How Atomic Memory could link to LLMWIKI so that both work together, updating and removing old data to keep LLMWIKI clean. LLMWIKI is still important; it acts like your Google Drive. What do you think? Give Atomic Memory a try. I’m not the founder or related to them. I just want to help the Ollama community. Sure, it might cost a few extra credits, but since Ollama is slow, having good memory helps find information faster, so you waste less usage. If you like this, I hope it helps! Maybe give them a GitHub star too, they really helped me out.

1h ago

---

**[Small differences in judgment used to be small differences in outcomes.](https://www.reddit.com/r/artificial/comments/1tofmq5/small_differences_in_judgment_used_to_be_small/)**

2h ago

---

**[Top 10 Fastest Growing AI repos this week](https://www.reddit.com/r/artificial/comments/1tnjhts/top_10_fastest_growing_ai_repos_this_week/)**

Curated this list of fastest growing AI repos. They are mostly AI coding agents, personal AI, memory, browser automation, Claude Skills and local-first dev tooling: colbymchenry/codegraph (+14.1K stars) Pre-indexed local code knowledge graph for Claude Code, Codex, Cursor, OpenCode, and Hermes Agent. tinyhumansai/openhuman (+17.1K stars) Personal AI / private AI superintelligence. Imbad0202/academic-research-skills (+11.6K stars) Claude Code skills for academic research workflows: research, write, review, revise, finalize. ruvnet/RuView (+6.8K stars) Turns commodity WiFi signals into spatial intelligence, presence detection, and vital sign monitoring. rohitg00/agentmemory (+6.9K stars) Persistent memory for AI coding agents based on real-world benchmarks. supertone-inc/supertonic (+3.6K stars) On-device multilingual TTS running natively via ONNX. CloakHQ/CloakBrowser (+7.0K stars) Stealth Chromium that passes bot detection tests with Playwright compatibility. HKUDS/ViMax (+2.7K stars) Agentic video generation: director, screenwriter, producer, and video generator in one. humanlayer/12-factor-agents (+1.9K stars) Principles for building production-grade LLM-powered software. Varnan-Tech/OpenDirectory (+250 stars) AI Agent Skills built for founders who hate marketing. All links in 1st comment 👇

1d ago

---

**[How to create cinematic typography with Google Flow](https://www.reddit.com/r/artificial/comments/1to81tm/how_to_create_cinematic_typography_with_google/)**

I used Google Flow to create a minimalist “ILLAS CÍES” typography design with ocean textures inside the letters. Basic workflow: Open Google Flow Create a new scene/project Use a typography-focused prompt Describe the textures you want inside the letters Keep the background minimal Generate multiple versions and upscale the best one Example prompt: “Minimalist typography design with the words ‘ILLAS CÍES’, letters filled with realistic turquoise Atlantic ocean water, soft white foam waves, subtle sandy beach gradients, clean white background, modern travel poster aesthetic” Tips: Use short prompts first Add lighting details later Avoid too many effects High contrast text works best The results are surprisingly good for travel-style graphics.

6h ago

---

---

## Google News: "ai"

**[To Understand Pope Leo’s Efforts on A.I., Look at the Man Shaking His Hand](https://www.nytimes.com/2026/05/26/us/pope-leo-ai-anthropic.html)**

The New York Times • 11h ago

---

**[GOP senators press intelligence officials to assess China AI capabilities](https://thehill.com/policy/technology/5895902-gop-senators-press-intelligence-officials-to-assess-china-ai-capabilities/)**

The Hill • 30m ago

---

**[Will AI eat your job? OpenAI's Sam Altman has a new prediction.](https://www.usatoday.com/story/money/personalfinance/2026/05/26/ai-jobs-unemployment-layoffs-sam-altman/90262359007/)**

Sam Altman of OpenAI has been one of the loudest voices warning that AI is a job killer. Has he changed his mind?

USA Today • 1h ago

---

**[OpenAI's Altman says AI unlikely to lead to 'jobs apocalypse'](https://www.reuters.com/world/asia-pacific/openais-altman-says-ai-unlikely-lead-jobs-apocalypse-2026-05-26/)**

Reuters • 6h ago

---

**[Sam Altman and Dario Amodei are both walking back their AI jobs apocalypse prophecies as they eye blockbuster IPOs](https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/)**

Some leaders like Goldman Sachs’s David Solomon and Box’s Aaron Levie have been saying all along that there won’t be a white-collar wipeout.

Fortune • 19m ago

---

**[Spotify boss defends move to AI music, saying it is better than ‘slop’](https://www.theguardian.com/technology/2026/may/26/spotify-ai-remix-tool-protects-artists-slop)**

Streaming platform says remix tool agreed with Universal Music Group will protect artists from piracy

The Guardian • 8h ago

---

**[Therapists are using AI to take notes. Is it a useful tool or a breach of trust?](https://www.npr.org/2026/05/26/nx-s1-5826943/talk-therapy-mental-health-ai-artificial-intelligence-privacy-trust)**

New companies are selling artificial intelligence assistance to mental health therapists. The AI tools can help with administration and recordkeeping, but some patients worry about their privacy.

NPR • 11h ago

---

**[The Despair of the Professor in the Age of A.I.](https://www.newyorker.com/news/fault-lines/the-despair-of-the-professor-in-the-age-of-ai)**

“Was it always the case that half of our students would cheat if it were easy enough?”

The New Yorker • 10h ago

---

**[Qualcomm Strikes AI Chip Deal With TikTok Owner ByteDance](https://www.bloomberg.com/news/articles/2026-05-26/qualcomm-strikes-ai-chip-deal-with-tiktok-owner-bytedance)**

Bloomberg.com • 6h ago

---

**[California mom out thousands after scammers use AI to mimic daughter's voice in fake kidnapping; part of growing trend](https://abc7.com/post/california-mom-thousands-scammers-use-ai-mimic-daughters-voice-fake-kidnapping-part-growing-trend/19175361/)**

Thousands of dollars were stolen from a California woman after scammers used artificial intelligence to mimic her daughter's voice in what authorities describe as a growing type of fraud.

ABC7 Los Angeles • 2h ago

---

---

## HackerNews: "ai"

**[Using AI to write better code more slowly](https://news.ycombinator.com/item?id=48272984)**

⬆️ 1107 • 💬 408 • 21h ago • [nolanlawson.com](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

---

**[Memory has grown to nearly two-thirds of AI chip component costs](https://news.ycombinator.com/item?id=48258684)**

High-bandwidth memory (HBM) accounts for 63% of AI chip component costs, up from 52% in Q1 2024. Epoch AI's breakdown of component cost shifts across major chip designers.

⬆️ 441 • 💬 489 • 2d ago • [Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)

---

**[Pope Leo XIV says AI must serve humanity, not the powerful few](https://news.ycombinator.com/item?id=48266485)**

VATICAN CITY (RNS) — In ‘Magnifica Humanitas,’ Leo's 83-page manifesto on AI, the pope tackles the social, economic and political challenges associated with artificial intelligence.

⬆️ 344 • 💬 67 • 1d ago • [RNS](https://religionnews.com/2026/05/25/in-his-first-encyclical-pope-leo-xiv-says-ai-must-serve-humanity-not-the-powerful-few/)

---

**[Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks](https://news.ycombinator.com/item?id=48266906)**

Authorities in the Netherlands have arrested the co-owners of two related Internet hosting companies for operating IT infrastructure used by Russia to carry out cyberattacks, influence operations and disinformation campaigns inside the European Union. The two men were the focus…

⬆️ 284 • 💬 90 • 1d ago • [krebsonsecurity.com](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)

---

**[Uber president says AI spending is getting 'harder to justify'](https://news.ycombinator.com/item?id=48277485)**

﻿There’s no clear connection between AI usage and productivity.

⬆️ 230 • 💬 124 • 10h ago • [The Verge](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify)

---

**[A successful Japanese trial of a ramjet engine designed for Mach‑5 aircraft](https://news.ycombinator.com/item?id=48270812)**

A team of engineers from Japan has completed a successful ground combustion trial of a ramjet engine designed for a Mach‑5 hypersonic aircraft.

⬆️ 224 • 💬 167 • 1d ago • [BGR](https://www.bgr.com/2178211/japan-hypersonic-engine-ramjet-2-hour-flights-to-us/)

---

**[DeepSeek to Make Permanent 75% Discount on Flagship AI Model](https://news.ycombinator.com/item?id=48257410)**

⬆️ 209 • 💬 2 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model)

---

**[Outsourcing plus local AI will soon become more economical vs. frontier labs](https://news.ycombinator.com/item?id=48278610)**

⬆️ 192 • 💬 212 • 8h ago • [signalbloom.ai](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/)

---

**['AI washing': firms are scrambling to rebrand themselves as tech-focused](https://news.ycombinator.com/item?id=48257980)**

PR executives say UK companies are forcing them to present ordinary automation as artificial intelligence

⬆️ 179 • 💬 163 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand)

---

**[Pope Leo: opaque AI run by few firms risks "New Forms of Dehumanization"](https://news.ycombinator.com/item?id=48266435)**

Pope Leo issues AI Encyclical warning that 'Opaque Algorithms' controlled by a 'few' companies threaten 'new forms of  dehumanization'

⬆️ 164 • 💬 2 • 1d ago • [Variety](https://variety.com/2026/biz/global/pope-leo-ai-encyclical-algorithms-threaten-dehumanisation-1236758186/)

---

---

## YouTube Videos: "ai"

**[OpenAI Founder Admits AI Isn’t Working | Prime Reacts](https://www.youtube.com/watch?v=-vPlLwtVU5g)**

Sources: https://www.youtube.com/watch?v=ZugX7a99dLk https://twitch.tv/ThePrimeagen - I Stream on Twitch ...

📺 ThePrimeagenHighlights

👁️ 187K • 👍 5K • 💬 572 • ⏱️ 20:44 • 1d ago

---

**[Harvard&#39;s Arthur Brooks on Pope Leo&#39;s AI warning: AI will ruin us if it doesn&#39;t make us more human](https://www.youtube.com/watch?v=qLxnBVBOteY)**

Arthur Brooks, Harvard University professor and The Free Press columnist, joins 'Squawk Box' to discuss Pope Leo's warning on ...

📺 CNBC Television

👁️ 15K • 👍 309 • 💬 121 • ⏱️ 12:17 • 9h ago

---

**[How to Make Explainer Videos With AI (Full Guide)](https://www.youtube.com/watch?v=a_qUx3YV8QQ)**

How to Make AI Explainer Videos with AI! Create Your Own Explainer Videos with OpenArt ...

📺 Isa does AI

👁️ 8K • 💬 4 • ⏱️ 15:50 • 8h ago

---

**[Pope Leo issues manifesto warning about AI](https://www.youtube.com/watch?v=RqXXs-ZIDNo)**

Pope Leo XIV says control of artificial intelligence must not remain in the hands “of a few” while warning that technology is fueling ...

📺 CNN

👁️ 131K • 👍 3K • 💬 1K • ⏱️ 11:28 • 1d ago

---

**[4 FREE and UNLIMITED AI Video Generators That Shouldn’t Exist](https://www.youtube.com/watch?v=r99B1WjyRh8)**

Try Higgsfield Supercomputer and build full AI video workflows in one place ...

📺 Malva AI

👁️ 6K • 👍 349 • 💬 42 • ⏱️ 9:55 • 9h ago

---

**[DeepMind’s Insane AI Breakthroughs With CEO Demis Hassabis](https://www.youtube.com/watch?v=huAwz_BR8WM)**

Thank you to Google DeepMind for the invite. ❤️ Check out Lambda here and sign up for their GPU Cloud: ...

📺 Two Minute Papers

👁️ 70K • 👍 5K • 💬 469 • ⏱️ 21:28 • 1d ago

---

**[FULL SPEECH: Pope Leo XIV Warns AI “Needs To Be Disarmed” In Explosive Vatican Speech | AK1B](https://www.youtube.com/watch?v=aaYJ_4QcZfE)**

Pope Leo XIV unveiled his first encyclical, Magnifica Humanitas, at the Vatican, warning that artificial intelligence “needs to be ...

📺 DRM News

👁️ 98K • 👍 4K • 💬 515 • ⏱️ 11:16 • 1d ago

---

**[Pope Leo warns of the risks of AI](https://www.youtube.com/watch?v=_7MoCJ5tVEM)**

"Artificial intelligence needs to be disarmed." Pope Leo XIV calls for the regulation of AI in a sweeping manifesto and warns it ...

📺 MS NOW

👁️ 66K • 👍 2K • 💬 250 • ⏱️ 0:59 • 1d ago

---

**[Almost every viral AI photo uses this same trick #ytshorts #gta6 #shortsfeed #trending #ai](https://www.youtube.com/watch?v=isxItYKkvcw)**

📺 Techno Teen 2.0

👁️ 555K • 👍 21K • 💬 23 • ⏱️ 0:15 • 11h ago

---

**[It’s Happening... Anthropic MYTHOS 1 Is Here!](https://www.youtube.com/watch?v=rDDI9gDiNAg)**

Claude Mythos 1 and Anthropic's Claude Security are now at the center of a massive AI cybersecurity story. Project Glasswing ...

📺 AI Revolution

👁️ 62K • 👍 2K • 💬 129 • ⏱️ 14:27 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,908 • ❤️ 857 • 3h ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 9,144 • ❤️ 373 • 6d ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 294 • 17h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 103,033 • ❤️ 375 • 5d ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 2,409 • ❤️ 296 • 16h ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 48,112 • ❤️ 692 • 8d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 1,598,473 • ❤️ 904 • 1mo ago

---

**[command-a-plus-05-2026-w4a4](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4)**

*Cohere Labs*

Command A+ is a 25B parameter, multilingual, vision-capable LLM optimized for agentic and reasoning tasks. It supports a 128K context window and offers a W4A4 quantization for efficient enterprise deployment.

`image-text-to-text` `125.8B`

⬇️ 7,769 • ❤️ 206 • 4d ago

---

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, featuring a prompt enhancer for improved input processing and supporting various LTX 2.3 formats.

`text-to-video` `9.0B`

⬇️ 1,376,847 • ❤️ 1,370 • 4d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,019,884 • ❤️ 4,305 • 20d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 79,711 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 26,445 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 170 • 💬 2 • ⭐ 435 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://huggingface.co/papers/2605.26115)**

*Weijie Wang, Zimu Li, Jinchuan Shi et al. (8 authors)*

🏢 Zhejiang University

TriSplat is a feed-forward 3D reconstruction network that uses oriented triangle primitives to directly generate simulation-ready meshes from single images, bypassing expensive post-processing steps.

▲ 34 • 💬 2 • ⭐ 91 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.26115) • [💻 code](https://github.com/ziplab/TriSplat) • [🔗 project](https://lhmd.top/trisplat/#interactive)

---

**[Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution](https://huggingface.co/papers/2605.23264)**

*Hongbo Wang, Huaibo Huang, Pin Wang et al. (6 authors)*

🏢 Chinese Academic of Science Institute of Automation

ASASR addresses spectral misalignment in image super-resolution by leveraging Riemannian geometry and adversarial training to improve structural fidelity and reduce artifacts.

▲ 3 • 💬 2 • ⭐ 71 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23264) • [💻 code](https://github.com/wafer-bob/ASASR)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 164 • 💬 2 • ⭐ 65,009 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 78 • 💬 7 • ⭐ 74,935 • 22mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[SANA-Video: Efficient Video Generation with Block Linear Diffusion
  Transformer](https://huggingface.co/papers/2509.24695)**

*Junsong Chen, Yuyang Zhao, Jincheng Yu et al. (20 authors)*

🏢 NVIDIA

SANA-Video, a small diffusion model, efficiently generates high-resolution, high-quality videos with strong text-video alignment using linear attention and a constant-memory KV cache, achieving competitive performance at a lower cost and faster speed.

▲ 53 • 💬 2 • ⭐ 7,694 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.24695) • [💻 code](https://github.com/NVlabs/Sana) • [🔗 project](https://nvlabs.github.io/Sana/Video)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 120 • 💬 10 • ⭐ 10,694 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 128 • 💬 3 • ⭐ 632 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.1k • 🔱 509 • 4d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 9d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.7k • 🔱 182 • 17m ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.4k • 🔱 525 • 1d ago

---

**[huangserva/3DCellForge](https://github.com/huangserva/3DCellForge)**

AI-powered interactive 3D model generation, inspection, and presentation studio.

`JavaScript`

⭐ 2.4k • 🔱 394 • 4d ago

---

**[yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts)**

Yao Open Prompts：中文 AI 提示词库，覆盖工作、学习、内容、营销和生活场景

`Python` `ai` `chinese-prompts` `geo` `prompt-engineering` `prompts`

⭐ 2.3k • 🔱 352 • 9d ago

---

**[Nutlope/hallmark](https://github.com/Nutlope/hallmark)**

Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

`CSS`

⭐ 2.0k • 🔱 140 • 7h ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 1.9k • 🔱 130 • 6h ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 220 • 19d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 196 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*

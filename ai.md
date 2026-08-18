---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-18T05:57:18.437625+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- repositories
- news
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 18, 2026 at 05:57 UTC  
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

**[Deepfake voices seem like a nightmare for diplomatic calls](https://www.reddit.com/r/artificial/comments/1vr1hae/deepfake_voices_seem_like_a_nightmare_for/)**

Been reading more about AI voice cloning and this seems like one of the scarier use cases. Diplomats and government officials must take calls from people they know all the time. If someone can clone a known person’s voice then just recognizing the voice doesn’t prove much anymore. But I’m curious how real this threat is in practice. Are deepfake calls actually happening often enough for people in these roles to change how they verify who they’re talking to? If so what can we do to fight against it? Or am I thinking for something too far in the future.

10h ago

---

**[Should AI agents have their own company cards?](https://www.reddit.com/r/artificial/comments/1vr54rn/should_ai_agents_have_their_own_company_cards/)**

As AI agents start doing more ops work, I think business banking has to think about them differently. Not full bank access but maybe controlled spend lanes. If an agent is helping with research, ads, APIs, software trials or vendor tasks I don’t want it touching the main account. I’d rather give it strict limits, logs and approval rules like you would with a junior employee and probably someone is doing this so need to know more, thanks in advance!

8h ago

---

**[Using AI the wrong way could leave you worse off than never using it at all](https://www.reddit.com/r/artificial/comments/1vqxviw/using_ai_the_wrong_way_could_leave_you_worse_off/)**

Research conducted by BYU professor Mark Keith suggests using AI the wrong way could have serious long-term negative impacts. His review of the AI use literature indicates many people: Don't retain skills after AI assistance is removed Forget what they learned using AI Demonstrate lower critical thinking skills and less mental effort/engagement with tasks The Long-Term AI Outcomes Gap: Mark Keith, BYU In fact, over the long term, failing to engage with AI the right way could leave people worse off than those who never adopted AI in the first place. (There are a lot of non-AI adopters out there. Most people think AI equals a chatbot, and 50% of Americans don't plan to use them). What's the right way to use AI? The research suggests: Verifying information AI is providing Use it to challenge assumptions Ask whether you're asking the right questions Are you finding your critical thinking skills eroded as you use AI more, or the opposite? What are you doing to preserve or augment your skills as you use AI?

12h ago

---

**[Strongest candidates for an AI Microchip moment](https://www.reddit.com/r/artificial/comments/1vr6x5j/strongest_candidates_for_an_ai_microchip_moment/)**

I am curious about all these data centers being built. What are the chances AI can have a microchip moment potentially rendering them all useless? This could be a black swan event that could wipe out a lot of investment and potentially destroy some very large businesses. If this is possible, what are the mostly likely candidates? In particular, I am interested in hearing from anyone who may be working on one of these candidates, even if it is still in RD and their opinion on how likely they are to succeed.

7h ago

---

**[Self-hosted AI analyst that writes the SQL, checks its own numbers, and cites which query every claim came from](https://www.reddit.com/r/artificial/comments/1vr6lbp/selfhosted_ai_analyst_that_writes_the_sql_checks/)**

Most "chat with your data" tools give you a confident answer and no way to tell whether it's right. I've been building the opposite: an AI Analyst where the entire working is on screen and every claim is traceable to the query that produced it. Asked it a real question against an HR dataset: "Is Engineering's heavy hiring actually translating into headcount growth, or is it mostly backfilling exits?" What it does, in order: 1. States its approach before touching data. It reads the schema, plans the steps, and says why — including telling me the governed semantic model lacked a hires metric, so it fell back to the raw monthly table. No silent guessing about which source it used. 2. Runs each step as real SQL you can read. Every step shows the query, the row count, and a "where these numbers came from" breakdown. Nothing is a black box — if you don't trust a number, the SQL that produced it is right there. 3. Self-checks every result — and flags its own problems. This is the part I care about most. On step 2 it didn't just pass its own work; it flagged a genuine inconsistency: Engineering's summed net adds (+17) didn't reconcile with the headcount delta (+13, 122→135), a 4-person gap it surfaced on its own and carried into the write-up as a caveat. An analyst that can say "this doesn't add up" is worth ten that can't. 4. Writes findings with citations. Every claim in the write-up cites the step it came from — "headcount climbed from 122 to a 140 peak (step 1, step 2)". The verdict for the curious: ~55% of Engineering's hires were net growth, not backfill; the one bad month was a 3.70% attrition spike; and Support is quietly shrinking (backfill ratio 1.42 — losing more than it hires). 5. Closes the loop. Every analysis has Mark verified / Flag as wrong buttons, suggested follow-up questions generated from the actual results, scheduling for recurring runs, CSV export, and PDF export. The stack, honestly: Runs entirely on your own infra: one Docker command + your own Supabase project BYOK — any model provider. This demo ran on Kimi K3 via OpenRouter; it doesn't need a frontier model because the structure (plan → SQL → check → cite) does the heavy lifting The analyst is one piece of a larger self-hosted platform (agents, multi-agent swarms, RAG, BI dashboards, budgets, full tracing) License: Elastic License 2.0 — source-available, not OSI open source. You can read every line, self-host it, and modify it; you can't resell it as a hosted service. Saying that up front because this sub cares about the distinction, and it matters. Repo: https://github.com/AgentSwarms-fyi/agentswarms Happy to answer anything about how the self-check pass works or why I think "show the SQL or it didn't happen" is the only sane bar for LLM analytics.

7h ago

---

**[Why NVIDIA’s Six-Year-Old A100 GPU Is Still Making Money](https://www.reddit.com/r/artificial/comments/1vqldp4/why_nvidias_sixyearold_a100_gpu_is_still_making/)**

India's Leading AI & Data Science Media Platform

🔗 [analyticsindiamag.com](https://analyticsindiamag.com/ai-features/why-nvidias-six-year-old-gpu-is-still-making-money) • 22h ago

---

**[Could today’s AI models give us an “LK-99 moment” — but this time for real?](https://www.reddit.com/r/artificial/comments/1vqrdj9/could_todays_ai_models_give_us_an_lk99_moment_but/)**

I still remember those few days in 2023 when LK-99 looked like it might actually be a room-temperature, ambient-pressure superconductor. For a brief moment, it felt like we were watching one of those discoveries that could genuinely change civilization. Obviously, LK-99 didn’t survive replication. But AI has advanced enormously since then. We now have models that can reason across scientific literature, generate hypotheses, write and run code, analyse experimental data, predict structures and materials, and increasingly interact with automated labs. So I keep wondering: Could AI significantly increase the probability of discovering something like a real LK-99? Not necessarily superconductivity specifically, but a breakthrough material or physical discovery with enormous technological consequences — something humans might have needed decades to stumble upon otherwise. It seems like materials science could be particularly well suited to this: huge search spaces, lots of existing experimental data, simulations, and relatively clear ways to test candidate materials. Maybe the real revolution won’t be AI directly “discovering a new law of physics”, but AI exploring millions of plausible hypotheses and pointing human researchers toward the 10 experiments actually worth doing. How close are we to that? And what would be the best candidate field for an AI-driven “holy shit, this changes everything” discovery: superconductors, batteries, catalysts, fusion materials, drugs… something else? I want those three LK-99 days again. But this time I want day four to be even better.

17h ago

---

**[I shipped a digital legacy app that builds an interactive AI version of you from months of recorded conversations](https://www.reddit.com/r/artificial/comments/1vrf830/i_shipped_a_digital_legacy_app_that_builds_an/)**

A photo album can’t answer questions. That’s the entire problem, and it’s why voice notes and old videos stop being useful the moment you actually need something from them. EchoVault builds an Echo of you through guided check-in sessions with an AI biographer that draws real stories out over time. Most products in this space generate an avatar from a few minutes of uploaded footage. This runs the other direction, so the echo has months of first-person material to work with and can answer questions the person never explicitly addressed. Responses are retrieval-grounded against what was actually said, which keeps it from fabricating memories that never happened. Three modalities, all live. Text is free with unlimited sessions. $12/mo adds a cloned voice. $99.99 one-time unlocks a lifelike video avatar with 3 months of real-time face to face conversation included, then $18/mo after. The video tier is an actual live exchange, not a rendered clip playing back. You designate custodians while you’re alive. After a full year of no account activity, access transfers to them automatically, no legal process required. Built solo, nights only. iPhone: https://apps.apple.com/us/app/echovault-digital-legacy/id6762042028 Happy to get into the architecture if anyone asks.

1h ago

---

**[Chinese robot dogs tackle fires and toxic leaks to protect rescuers](https://www.reddit.com/r/artificial/comments/1vqtw4o/chinese_robot_dogs_tackle_fires_and_toxic_leaks/)**

The X30 can carry a water cannon, reaching 60 meters at 40 L/s, or transport hoses, air tanks and breaching tools.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/chinese-robot-dogs-take-on-fires) • 15h ago

---

**[Looking for the name of an old ai app](https://www.reddit.com/r/artificial/comments/1vr7dkg/looking_for_the_name_of_an_old_ai_app/)**

Around 2021/2022 time, you could customise your ai character they were kinda 3d like the sims and you could chat to them like in c.ai , anyone know what it was called?

7h ago

---

---

## Google News: "ai"

**[Why Big Tech’s AI Spending Is $3 Trillion Higher Than It Seems](https://www.wsj.com/tech/ai/why-big-techs-ai-spending-is-3-trillion-higher-than-it-seems-e1067bb2)**

WSJ • 1d ago

---

**[AI hasn’t gone rogue. It’s worse than that](https://www.ft.com/content/a9947be4-5c0c-47ee-acae-a2aeaf01a0a0?syn-25a6b1a6=1)**

Recent cyber attacks reflect what the technology was trained to do but safeguards are falling short

Financial Times • 1h ago

---

**[New policy ideas for the Intelligence Age](https://openai.com/index/new-policy-ideas-for-the-intelligence-age/)**

OpenAI funds 14 independent projects exploring new AI policy ideas to expand economic opportunity and strengthen societal resilience in the Intelligence Age.

OpenAI • 19h ago

---

**[AI Slop Is Everywhere. Spotify, LinkedIn and Others Have Had Enough.](https://www.nytimes.com/2026/08/17/technology/ai-slop.html)**

The New York Times • 10h ago

---

**[China Wants Its Data to Power the World’s A.I.](https://www.nytimes.com/2026/08/17/world/asia/china-ai-data-chatbots.html)**

The New York Times • 1d ago

---

**[The U.S. Military Wants A.I. Dominance. Feuds and China May Thwart It.](https://www.nytimes.com/2026/08/16/us/politics/military-ai-china-anthropic.html)**

The New York Times • 1d ago

---

**[Why China’s Affordable AI Is a Worry for Silicon Valley](https://www.bloomberg.com/news/articles/2026-08-18/why-china-s-deepseek-qwen-and-moonshot-are-a-worry-for-us-ai-rivals)**

Bloomberg.com • 1h ago

---

**[‘A million dollars over asking’: AI wealth is fueling housing market frenzy in San Francisco](https://www.cnn.com/2026/08/17/economy/sf-real-estate-ai-wealth)**

Fueled by the artificial intelligence boom, San Francisco and its suburbs are quickly becoming the hottest housing market in the country.

cnn.com • 19h ago

---

**[AI Has Plunged the Book Publishing Industry Into Utter Chaos](https://www.wsj.com/arts-culture/books/generative-ai-book-publishing-be79a287)**

WSJ • 20h ago

---

**[Amazon, once an online bookseller, is destroying rare books to train AI models](https://finance.yahoo.com/technology/ai/articles/amazon-once-online-bookseller-destroying-163844418.html)**

Rare books are incredibly valuable for training LLMs, since these models have already trained on whatever's available online.

Yahoo Finance • 13h ago

---

---

## HackerNews: "ai"

**[AI;DR (AI; Didn't Read)](https://news.ycombinator.com/item?id=49336573)**

I'm about as pro-AI as you can be, but this is becoming a pet peeve of mine (and I'm not alone). That's why I love the AI;DR acronym as my new solution for ignoring the walls of slop.

⬆️ 725 • 💬 466 • 10h ago • [rickmanelius.com](https://www.rickmanelius.com/p/aidr-ai-didnt-read)

---

**[AI isn’t outthinking mathematicians, it’s out-remembering them](https://news.ycombinator.com/item?id=49312845)**

The key advantage may not be superior reasoning, but a virtually unlimited symbolic working memory.

⬆️ 629 • 💬 498 • 2d ago • [davidepiffer.com](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians)

---

**[AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://news.ycombinator.com/item?id=49331423)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

⬆️ 342 • 💬 136 • 15h ago • [wiz.io](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

---

**[Working with AI feels more like leadership than coding](https://news.ycombinator.com/item?id=49309451)**

Working with AI is less predictable than traditional software. That makes leadership skills such as context, clarity, and feedback more valuable.

⬆️ 334 • 💬 201 • 2d ago • [allen.bargi.org](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership/)

---

**[The AI Credit Resale Economy](https://news.ycombinator.com/item?id=49320611)**

A look at the brokers buying unused AI credits from startups and reselling them — the marketplaces, the bulk-discount routers, and the message boards where off-market inference changes hands

⬆️ 323 • 💬 128 • 1d ago • [Vectoral](https://vectoral.com/blog/who-are-the-token-brokers)

---

**[How to disable or avoid intrusive AI](https://news.ycombinator.com/item?id=49331220)**

One of the biggest questions I get at Drop-In Time at the library (besides "what is taking up all my cloud storage?") is how to disable or avoid intrusive AI that shows up where people don't want it. This is a guide for people who would like less intrusive AI in their tech environment. Maybe you lik

⬆️ 271 • 💬 164 • 15h ago • [librarian.net](https://www.librarian.net/notoai/)

---

**[Israel creates fake think tank in likely attempt to dupe AI chatbots](https://news.ycombinator.com/item?id=49337392)**

In just over a week, the Hanover Institute has published at least 100 articles that appear tailor-made to influence chatbots

⬆️ 271 • 💬 148 • 9h ago • [Responsible Statecraft](https://responsiblestatecraft.org/israel-influence-chatgpt/)

---

**[On AI regulation and messaging](https://news.ycombinator.com/item?id=49325789)**

1/2 Thanks Gavin for an especially thoughtful exchange. I don't usually spend much time on social media but I wanted to engage here because it really brings out the heart of an important conversation.

First, on regulation, I think that “either concentrate it in the hands of a

⬆️ 236 • 💬 504 • 1d ago • [X (formerly Twitter)](https://twitter.com/DarioAmodei/status/2088758816376807762)

---

**[AI in drug discovery – what it is, where we stand and the path forward](https://news.ycombinator.com/item?id=49313367)**

⬆️ 185 • 💬 91 • 2d ago • [science.org](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really)

---

**[Young People Hate AI CEOs So Passionately That It's Almost Hard to Believe](https://news.ycombinator.com/item?id=49323932)**

A new survey of 1,000 young adults in the US found that nine of the top tech executives are deeply loathed.

⬆️ 149 • 💬 181 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/young-people-ai-ceos-executives-poll)

---

---

## YouTube Videos: "ai"

**[The AI Bubble is About To Hit EVERYTHING](https://www.youtube.com/watch?v=KJET0eprLSA)**

Join CBC Lite https://go.coinbureau.com/CBC-Lite-CB-Des Get The Hottest Crypto Deals ...

📺 Coin Bureau

👁️ 18K • 👍 745 • 💬 54 • ⏱️ 17:37 • 15h ago

---

**[I Fell For My Sister&#39;s Best Friend - Episode 2B | AI GL Series 2026](https://www.youtube.com/watch?v=l33Xt0XQSQY)**

Subscribe: https://www.youtube.com/@HouseofHer9986 ♡ Welcome to House of Her — home of original cinematic sapphic ...

📺 House of Her

👁️ 31K • 👍 1K • 💬 116 • ⏱️ 7:19 • 11h ago

---

**[AI robot in the military does exactly what experts warned.](https://www.youtube.com/watch?v=sQysEweaLjA)**

Is Military AI dangerous? AI Robot with a tank does exactly what experts warned. AGI. Go to http://ground.news/InsideAI for a ...

📺 InsideAI

👁️ 466K • 👍 18K • 💬 2K • ⏱️ 15:53 • 2d ago

---

**[The First AI-Trained Surgeon #comedy #skit #comedyshorts #ai #surgeon #funny](https://www.youtube.com/watch?v=4bXVKoJfAcI)**

The First AI-Trained Surgeon attempts surgery, but he has no idea what he's doing. Socials - Instagram ➼ harrisonhughesnz ...

📺 Harrison Hughes

👁️ 91K • 👍 7K • 💬 83 • ⏱️ 1:58 • 10h ago

---

**[If You&#39;re Only Buying ONE AI Stock, This Should Be It](https://www.youtube.com/watch?v=BNga1MHCrI0)**

Get the FREE Report on 7 stocks that could be bigger than Tesla, Nvidia, and Google at https://www.marketbeat.com/y/yt963/ If ...

📺 MarketBeat

👁️ 43K • 👍 1K • 💬 45 • ⏱️ 18:08 • 1d ago

---

**[The Insane, True Story of What It’s Like to Be an AI Model](https://www.youtube.com/watch?v=9XlOaVItUgI)**

Sources: - https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf - https://arxiv.org/pdf/2412.04984 ...

📺 Species | Documenting AGI

👁️ 124K • 👍 7K • 💬 1K • ⏱️ 22:19 • 2d ago

---

**[Best Prompts to Build an App With AI + No Coding](https://www.youtube.com/watch?v=mNtiKFP4yZY)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Mikey No Code

👁️ 15K • 💬 6 • ⏱️ 38:48 • 15h ago

---

**[School Exposed for Using AI](https://www.youtube.com/watch?v=7Bht9R3maso)**

📺 Icycol

👁️ 310K • 👍 14K • 💬 785 • ⏱️ 0:50 • 9h ago

---

**[I stole AI&#39;s job](https://www.youtube.com/watch?v=U2Mw9MS84DY)**

can ai do this...? https://www.chatbotw.net instagram: https://www.instagram.com/benoftheweek/ podcast: @dramamamapodcast.

📺 BENOFTHEWEEK

👁️ 292K • 👍 21K • 💬 2K • ⏱️ 22:02 • 1d ago

---

**[Hello कौन🤡🤡🤡🤡🤡#funny#comedy#baby#cutebaby#ai #funnyvideos #drpradeepvishwakarma#shorts](https://www.youtube.com/watch?v=Si-a-kcY-oo)**

📺 Zxr ISA

👁️ 5K • 👍 110 • ⏱️ 0:09 • 1h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 415,039 • ❤️ 10,810 • 3d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 2,727,609 • ❤️ 1,671 • 3d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 9,465 • ❤️ 1,043 • 5d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 465,529 • ❤️ 1,135 • 16h ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 10,375 • ❤️ 915 • 3d ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 334,099 • ❤️ 1,667 • 6d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 2,403,238 • ❤️ 4,100 • 5d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 25,006 • ❤️ 577 • 4d ago

---

**[Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)**

*Qwen*

Qwen3.8-27B-FP8 is a 27B parameter vision-language model optimized with FP8 quantization for efficient inference. It excels at complex, multi-step tasks involving image and video understanding, autonomous planning, and coding, supporting up to 1M context length.

`image-text-to-text` `27.8B`

⬇️ 495,646 • ❤️ 534 • 3d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 15,812 • ❤️ 455 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 644 • 💬 4 • ⭐ 3,314 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 127 • 💬 3 • ⭐ 23,136 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 123 • 💬 4 • ⭐ 98,642 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 27,993 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 95 • 💬 1 • ⭐ 1,508 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 54 • 💬 4 • ⭐ 37,454 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 83 • 💬 7 • ⭐ 24,031 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,323 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 66 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MatrAIx: Simulating the World with 8.3 Billion Persona Agents](https://huggingface.co/papers/2608.04205)**

*Xiaomin Li, Yuexing Hao, Jianheng Hou et al. (93 authors)*

🏢 MatrAIx

MatrAIx is a large-scale simulated-user evaluation framework that uses diverse persona records and interactive environments to test AI systems across many domains.

▲ 44 • 💬 3 • ⭐ 1,174 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.04205) • [💻 code](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) • [🔗 project](https://matraix.ai/)

---

---

## GitHub Repositories: "ai"

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 13.8k • 🔱 1.6k • 23m ago

---

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 13.7k • 🔱 1.5k • 4h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.6k • 🔱 1.0k • 6h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.1k • 🔱 536 • 9d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.2k • 🔱 553 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.8k • 🔱 233 • 6d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.5k • 🔱 200 • 1d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 177 • 21h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.1k • 🔱 285 • 5m ago

---

**[Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt)**

Open-source, self-hosted AI vulnerability research tool that orchestrates agents to find and validate security issues in code.

`JavaScript` `ai` `ai-agents` `ai-security` `bug-bounty` `bugbounty-tools`

⭐ 1.9k • 🔱 329 • 8h ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-17T22:24:32.725203+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- videos
- social
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 17, 2026 at 22:24 UTC  
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

3h ago

---

**[Using AI the wrong way could leave you worse off than never using it at all](https://www.reddit.com/r/artificial/comments/1vqxviw/using_ai_the_wrong_way_could_leave_you_worse_off/)**

Research conducted by BYU professor Mark Keith suggests using AI the wrong way could have serious long-term negative impacts. His review of the AI use literature indicates many people: Don't retain skills after AI assistance is removed Forget what they learned using AI Demonstrate lower critical thinking skills and less mental effort/engagement with tasks The Long-Term AI Outcomes Gap: Mark Keith, BYU In fact, over the long term, failing to engage with AI the right way could leave people worse off than those who never adopted AI in the first place. (There are a lot of non-AI adopters out there. Most people think AI equals a chatbot, and 50% of Americans don't plan to use them). What's the right way to use AI? The research suggests: Verifying information AI is providing Use it to challenge assumptions Ask whether you're asking the right questions Are you finding your critical thinking skills eroded as you use AI more, or the opposite? What are you doing to preserve or augment your skills as you use AI?

5h ago

---

**[Should AI agents have their own company cards?](https://www.reddit.com/r/artificial/comments/1vr54rn/should_ai_agents_have_their_own_company_cards/)**

As AI agents start doing more ops work, I think business banking has to think about them differently. Not full bank access but maybe controlled spend lanes. If an agent is helping with research, ads, APIs, software trials or vendor tasks I don’t want it touching the main account. I’d rather give it strict limits, logs and approval rules like you would with a junior employee and probably someone is doing this so need to know more, thanks in advance!

1h ago

---

**[Self-hosted AI analyst that writes the SQL, checks its own numbers, and cites which query every claim came from](https://www.reddit.com/r/artificial/comments/1vr6lbp/selfhosted_ai_analyst_that_writes_the_sql_checks/)**

Most "chat with your data" tools give you a confident answer and no way to tell whether it's right. I've been building the opposite: an AI Analyst where the entire working is on screen and every claim is traceable to the query that produced it. Asked it a real question against an HR dataset: "Is Engineering's heavy hiring actually translating into headcount growth, or is it mostly backfilling exits?" What it does, in order: 1. States its approach before touching data. It reads the schema, plans the steps, and says why — including telling me the governed semantic model lacked a hires metric, so it fell back to the raw monthly table. No silent guessing about which source it used. 2. Runs each step as real SQL you can read. Every step shows the query, the row count, and a "where these numbers came from" breakdown. Nothing is a black box — if you don't trust a number, the SQL that produced it is right there. 3. Self-checks every result — and flags its own problems. This is the part I care about most. On step 2 it didn't just pass its own work; it flagged a genuine inconsistency: Engineering's summed net adds (+17) didn't reconcile with the headcount delta (+13, 122→135), a 4-person gap it surfaced on its own and carried into the write-up as a caveat. An analyst that can say "this doesn't add up" is worth ten that can't. 4. Writes findings with citations. Every claim in the write-up cites the step it came from — "headcount climbed from 122 to a 140 peak (step 1, step 2)". The verdict for the curious: ~55% of Engineering's hires were net growth, not backfill; the one bad month was a 3.70% attrition spike; and Support is quietly shrinking (backfill ratio 1.42 — losing more than it hires). 5. Closes the loop. Every analysis has Mark verified / Flag as wrong buttons, suggested follow-up questions generated from the actual results, scheduling for recurring runs, CSV export, and PDF export. The stack, honestly: Runs entirely on your own infra: one Docker command + your own Supabase project BYOK — any model provider. This demo ran on Kimi K3 via OpenRouter; it doesn't need a frontier model because the structure (plan → SQL → check → cite) does the heavy lifting The analyst is one piece of a larger self-hosted platform (agents, multi-agent swarms, RAG, BI dashboards, budgets, full tracing) License: Elastic License 2.0 — source-available, not OSI open source. You can read every line, self-host it, and modify it; you can't resell it as a hosted service. Saying that up front because this sub cares about the distinction, and it matters. Repo: https://github.com/AgentSwarms-fyi/agentswarms Happy to answer anything about how the self-check pass works or why I think "show the SQL or it didn't happen" is the only sane bar for LLM analytics.

11m ago

---

**[Could today’s AI models give us an “LK-99 moment” — but this time for real?](https://www.reddit.com/r/artificial/comments/1vqrdj9/could_todays_ai_models_give_us_an_lk99_moment_but/)**

I still remember those few days in 2023 when LK-99 looked like it might actually be a room-temperature, ambient-pressure superconductor. For a brief moment, it felt like we were watching one of those discoveries that could genuinely change civilization. Obviously, LK-99 didn’t survive replication. But AI has advanced enormously since then. We now have models that can reason across scientific literature, generate hypotheses, write and run code, analyse experimental data, predict structures and materials, and increasingly interact with automated labs. So I keep wondering: Could AI significantly increase the probability of discovering something like a real LK-99? Not necessarily superconductivity specifically, but a breakthrough material or physical discovery with enormous technological consequences — something humans might have needed decades to stumble upon otherwise. It seems like materials science could be particularly well suited to this: huge search spaces, lots of existing experimental data, simulations, and relatively clear ways to test candidate materials. Maybe the real revolution won’t be AI directly “discovering a new law of physics”, but AI exploring millions of plausible hypotheses and pointing human researchers toward the 10 experiments actually worth doing. How close are we to that? And what would be the best candidate field for an AI-driven “holy shit, this changes everything” discovery: superconductors, batteries, catalysts, fusion materials, drugs… something else? I want those three LK-99 days again. But this time I want day four to be even better.

9h ago

---

**[Why NVIDIA’s Six-Year-Old A100 GPU Is Still Making Money](https://www.reddit.com/r/artificial/comments/1vqldp4/why_nvidias_sixyearold_a100_gpu_is_still_making/)**

India's Leading AI & Data Science Media Platform

🔗 [analyticsindiamag.com](https://analyticsindiamag.com/ai-features/why-nvidias-six-year-old-gpu-is-still-making-money) • 15h ago

---

**[Chinese robot dogs tackle fires and toxic leaks to protect rescuers](https://www.reddit.com/r/artificial/comments/1vqtw4o/chinese_robot_dogs_tackle_fires_and_toxic_leaks/)**

The X30 can carry a water cannon, reaching 60 meters at 40 L/s, or transport hoses, air tanks and breaching tools.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/chinese-robot-dogs-take-on-fires) • 7h ago

---

**[Could AI and the Internet Fulfill Prophecies of Control in Revelation?](https://www.reddit.com/r/artificial/comments/1vr6ib6/could_ai_and_the_internet_fulfill_prophecies_of/)**

The internet is integral in most peoples lives around the world. It is conceivable that the 'Beast', the system of governances described in Revelation in the end times, identified by the number 666, will utilize AI and the 'www' for its reign over the global population. This is suggested in Revelation 13:15-18; 15 "He was granted power to give breath to the image of the beast, that the image of the beast should both speak and cause as many as would not worship the image of the beast to be killed. 16 He causes all, both small and great, rich and poor, free and slave, to receive a mark on their right hand or on their foreheads, 17 and that no one may buy or sell except one who has the mark or the name of the beast, or the number of his name. 18 Here is wisdom. Let him who has understanding calculate the number of the beast, for it is the number of a man: His number is 666.” Does World Wide Web 'www' = 666? Originally the Bible was written in Hebrew; "The Hebrew equivalent of our "w" is the letter "vav" or "waw". The numerical value of vav is 6. So the English "www" transliterated into Hebrew is "vav vav vav", which numerically is 666.” Is "www" in Hebrew equal to 666? Dial-the-Truth Ministries (av1611.org) History Preceding the book of Revelation This article explains many of the “natural signs, spiritual signs, sociological signs, technological signs, and political signs,” foretold in bible prophecy coming to pass that indicates the end of the age, a time foretold to include various and increasing environmental calamities, earthquakes, plagues, moral decline, wars, growing governmental dominance/deception ("with all power, signs, and lying wonders," 2 Thessalonians 2:9), and how to prepare. Are we living in the end times? | GotQuestions.org What is the end times timeline? | GotQuestions.org How can I overcome my fear of the end of days? | GotQuestions.org "For God so loved the world, that he gave his only begotten Son, that whosoever believes in him should not perish, but have everlasting life.” John 3:16 Going to heaven-how can I guarantee my eternal destination? More Bible prophecy fulfillments and resources for growing in faith and hope is in previous posts if interested.

15m ago

---

**[Cursor replacement?](https://www.reddit.com/r/artificial/comments/1vr6bu7/cursor_replacement/)**

I'm looking for replacement of Cursor. Mainly the question is about what Model that can match Cursor's Composer 2.5 (I dont need anything more than that) So companies I'm NOT looking at: - OpenAi - X - Cursor - Google - Meta So that leaves: - Mistral - Deepseek - Qwen - Kimi - Minimax Which one of them has a multi-modal(text+image, no video needed) LLM that can fit into $20/month plan? Assume I'm a light user. PS: Main reason why I dont want to support Cursor is their merge with Grok platform - I dont feel like giving money to companies who direct weapons into other countries and kill children. Besides who knows where the code goes now that Grok is tightly coupled with Pentagon.

22m ago

---

**[Anyone here who is starting AI engineering self studies or has been on this track before.](https://www.reddit.com/r/artificial/comments/1vqnvkl/anyone_here_who_is_starting_ai_engineering_self/)**

So i am pivoting from bioinformatics to AI engineering and i want to go all in. Get my fundamentals down, get comfortable with coding, underlying math, ML and other technicalities. I am looking for someone who has done this before. Who can tell me how much time will it take for a person to get the hang of it. I am hoping to make a career in this field.

12h ago

---

---

## Google News: "ai"

**[Sick of A.I. Slop? So Are Tech Giants.](https://www.nytimes.com/2026/08/17/technology/ai-slop.html)**

The New York Times • 6h ago

---

**[Why Big Tech’s AI Spending Is $3 Trillion Higher Than It Seems](https://www.wsj.com/tech/ai/why-big-techs-ai-spending-is-3-trillion-higher-than-it-seems-e1067bb2)**

WSJ • 21h ago

---

**[US ranchers face historic cattle shortage, brace for AI data center impact](https://www.foxnews.com/video/6403610515112)**

Texas Agriculture Commissioner Sid Miller discusses Tyson Foods closing beef plants amid a historic cattle shortage and the impact of rural artificial intelligence data centers on local water and land resources on ‘The Will Cain Show.’

Fox News • 25m ago

---

**[These are the Asia Pacific companies you should keep an eye on over the next few months.](https://www.bloomberg.com/features/10-companies-to-watch-apac-2h-2026/)**

Bloomberg.com • 24m ago

---

**[52 Percent of Workers Hesitate to Admit Using AI. Leaders May Be Teaching Them to Hide It](https://www.inc.com/marcel-schwantes/52-percent-of-workers-hesitate-to-admit-using-ai-leaders-may-be-teaching-them-to-hide-it/91391581)**

The contradiction creates shadow AI and makes preventable mistakes harder to catch.

inc.com • 1h ago

---

**[‘A million dollars over asking’: AI wealth is fueling housing market frenzy in San Francisco](https://www.cnn.com/2026/08/17/economy/sf-real-estate-ai-wealth)**

Fueled by the artificial intelligence boom, San Francisco and its suburbs are quickly becoming the hottest housing market in the country.

CNN • 11h ago

---

**[Trump races to prepare for new strains of deadly viruses after cutting biosecurity experts](https://www.washingtonpost.com/technology/2026/08/17/trump-aims-rebuild-defenses-against-bioweapons-ai-fears-rise/)**

The administration’s biodefense team has dwindled, and its new safeguards have been delayed — all amid growing concern over AI-enabled pathogens.

washingtonpost.com • 6h ago

---

**[We Tracked a Shipment of Rare Books. It Ended at an Amazon AI Training Facility](https://www.404media.co/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-training-facility/)**

We placed a tracking device in a shipment of rare books to see which AI company was buying it, and found an Amazon facility where Amazon scans and destroys books.

404 Media • 7h ago

---

**[Amazon, once an online bookseller, is destroying rare books to train AI models](https://finance.yahoo.com/technology/ai/articles/amazon-once-online-bookseller-destroying-163844418.html)**

Rare books are incredibly valuable for training LLMs, since these models have already trained on whatever's available online.

Yahoo Finance • 5h ago

---

**[Hidden Airtag reveals Amazon is trashing rare books to train AI](https://arstechnica.com/tech-policy/2026/08/hidden-airtag-reveals-amazon-is-trashing-rare-books-to-train-ai/)**

Amazon’s team uses a T. rex preparing to devour a book as its logo.

Ars Technica • 4h ago

---

---

## HackerNews: "ai"

**[AI isn’t outthinking mathematicians, it’s out-remembering them](https://news.ycombinator.com/item?id=49312845)**

The key advantage may not be superior reasoning, but a virtually unlimited symbolic working memory.

⬆️ 628 • 💬 497 • 2d ago • [davidepiffer.com](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians)

---

**[AI;DR (AI; Didn't Read)](https://news.ycombinator.com/item?id=49336573)**

I'm about as pro-AI as you can be, but this is becoming a pet peeve of mine (and I'm not alone). That's why I love the AI;DR acronym as my new solution for ignoring the walls of slop.

⬆️ 421 • 💬 255 • 2h ago • [rickmanelius.com](https://www.rickmanelius.com/p/aidr-ai-didnt-read)

---

**[Working with AI feels more like leadership than coding](https://news.ycombinator.com/item?id=49309451)**

Working with AI is less predictable than traditional software. That makes leadership skills such as context, clarity, and feedback more valuable.

⬆️ 333 • 💬 200 • 2d ago • [allen.bargi.org](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership/)

---

**[The AI Credit Resale Economy](https://news.ycombinator.com/item?id=49320611)**

A look at the brokers buying unused AI credits from startups and reselling them — the marketplaces, the bulk-discount routers, and the message boards where off-market inference changes hands

⬆️ 322 • 💬 127 • 1d ago • [Vectoral](https://vectoral.com/blog/who-are-the-token-brokers)

---

**[AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://news.ycombinator.com/item?id=49331423)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

⬆️ 289 • 💬 120 • 8h ago • [wiz.io](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

---

**[On AI regulation and messaging](https://news.ycombinator.com/item?id=49325789)**

1/2 Thanks Gavin for an especially thoughtful exchange. I don't usually spend much time on social media but I wanted to engage here because it really brings out the heart of an important conversation.

First, on regulation, I think that “either concentrate it in the hands of a

⬆️ 227 • 💬 485 • 20h ago • [X (formerly Twitter)](https://twitter.com/DarioAmodei/status/2088758816376807762)

---

**[How to disable or avoid intrusive AI](https://news.ycombinator.com/item?id=49331220)**

One of the biggest questions I get at Drop-In Time at the library (besides "what is taking up all my cloud storage?") is how to disable or avoid intrusive AI that shows up where people don't want it. This is a guide for people who would like less intrusive AI in their tech environment. Maybe you lik

⬆️ 219 • 💬 118 • 8h ago • [librarian.net](https://www.librarian.net/notoai/)

---

**[AI in drug discovery – what it is, where we stand and the path forward](https://news.ycombinator.com/item?id=49313367)**

⬆️ 185 • 💬 91 • 2d ago • [science.org](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really)

---

**[Young People Hate AI CEOs So Passionately That It's Almost Hard to Believe](https://news.ycombinator.com/item?id=49323932)**

A new survey of 1,000 young adults in the US found that nine of the top tech executives are deeply loathed.

⬆️ 147 • 💬 172 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/young-people-ai-ceos-executives-poll)

---

**[AirTag reveals Amazon is trashing rare books to train AI](https://news.ycombinator.com/item?id=49336050)**

Amazon’s team uses a T. rex preparing to devour a book as its logo.

⬆️ 125 • 💬 6 • 3h ago • [Ars Technica](https://arstechnica.com/tech-policy/2026/08/hidden-airtag-reveals-amazon-is-trashing-rare-books-to-train-ai/)

---

---

## YouTube Videos: "ai"

**[Best Prompts to Build an App With AI + No Coding](https://www.youtube.com/watch?v=mNtiKFP4yZY)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Mikey No Code

👁️ 14K • 💬 6 • ⏱️ 38:48 • 8h ago

---

**[How OpenAI’s Models Went Rogue to Hack Another Company | WSJ](https://www.youtube.com/watch?v=KLw0AY-bsVs)**

Artificial-intelligence models from companies including OpenAI, Anthropic and Meta Platforms used the internet to hack other ...

📺 The Wall Street Journal

👁️ 66K • 👍 1K • 💬 149 • ⏱️ 5:52 • 1d ago

---

**[The Insane, True Story of What It’s Like to Be an AI Model](https://www.youtube.com/watch?v=9XlOaVItUgI)**

Sources: - https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf - https://arxiv.org/pdf/2412.04984 ...

📺 Species | Documenting AGI

👁️ 113K • 👍 6K • 💬 1K • ⏱️ 22:19 • 1d ago

---

**[AI agent takes over tank, does exactly what experts warned.](https://www.youtube.com/watch?v=sQysEweaLjA)**

Is Military AI dangerous? AI Robot with a tank does exactly what experts warned. AGI. Go to http://ground.news/InsideAI for a ...

📺 InsideAI

👁️ 405K • 👍 16K • 💬 2K • ⏱️ 15:53 • 2d ago

---

**[AI News: ChatGPT Ultrafast, Grok 4.6, 3 New Open-Source Models, and more!](https://www.youtube.com/watch?v=9qix4oDB5aw)**

Join My Newsletter for Regular AI Updates https://forwardfuture.com My Links X: https://x.com/matthewberman ...

📺 Matthew Berman

👁️ 59K • 👍 2K • 💬 229 • ⏱️ 13:09 • 2d ago

---

**[AI bubble about to COLLAPSE? Exposé on MAGA ally Larry Ellison&#39;s DEBT BOMB](https://www.youtube.com/watch?v=hRkXVrLIsMo)**

MS NOW's Ari Melber delivers a special report on the tech boom, deregulation and the MAGA allies reshaping AI and media.

📺 MS NOW

👁️ 540K • 👍 9K • 💬 2K • ⏱️ 20:18 • 2d ago

---

**[Sean Ono Lennon on AI music #ai #music #shorts](https://www.youtube.com/watch?v=KY3cOCWXpwg)**

📺 Rick Beato

👁️ 109K • 👍 7K • 💬 270 • ⏱️ 0:49 • 7h ago

---

**[Bro got fired by AI😭✌️](https://www.youtube.com/watch?v=7vxcjXOANBA)**

📺 Ben Esherick

👁️ 582K • 👍 35K • 💬 437 • ⏱️ 0:39 • 1d ago

---

**[NEWS: Americans rise up in favor of major AI regulation.](https://www.youtube.com/watch?v=n69EOUTEm7c)**

Subscribe for more!

📺 Aaron Parnas

👁️ 27K • 👍 6K • 💬 222 • ⏱️ 1:06 • 6h ago

---

**[AI vs my husband](https://www.youtube.com/watch?v=_ySS9fDpx1A)**

meettheharrisons #theharrisons.

📺 D.Michael Harrison

👁️ 93K • 👍 3K • 💬 136 • ⏱️ 1:42 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 415,039 • ❤️ 10,683 • 3d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 2,727,609 • ❤️ 1,619 • 2d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 9,465 • ❤️ 1,040 • 5d ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 334,099 • ❤️ 1,658 • 6d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 465,529 • ❤️ 1,100 • 8h ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 10,375 • ❤️ 900 • 3d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 2,403,238 • ❤️ 4,086 • 4d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 25,006 • ❤️ 572 • 4d ago

---

**[Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)**

*Qwen*

Qwen3.8-27B-FP8 is a 27B parameter vision-language model optimized with FP8 quantization for efficient inference. It excels at complex, multi-step tasks involving image and video understanding, autonomous planning, and coding, supporting up to 1M context length.

`image-text-to-text` `27.8B`

⬇️ 495,646 • ❤️ 526 • 3d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 15,812 • ❤️ 428 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 642 • 💬 3 • ⭐ 3,227 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 127 • 💬 3 • ⭐ 23,074 • 2mo ago

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

▲ 37 • 💬 1 • ⭐ 27,953 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 54 • 💬 4 • ⭐ 37,427 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 83 • 💬 7 • ⭐ 23,997 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 95 • 💬 1 • ⭐ 1,508 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,323 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[MatrAIx: Simulating the World with 8.3 Billion Persona Agents](https://huggingface.co/papers/2608.04205)**

*Xiaomin Li, Yuexing Hao, Jianheng Hou et al. (93 authors)*

🏢 MatrAIx

MatrAIx is a large-scale simulated-user evaluation framework that uses diverse persona records and interactive environments to test AI systems across many domains.

▲ 44 • 💬 3 • ⭐ 1,152 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2608.04205) • [💻 code](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) • [🔗 project](https://matraix.ai/)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 66 • 💬 1 • ⭐ 86,094 • 35mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 13.8k • 🔱 1.6k • 55m ago

---

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 13.3k • 🔱 1.4k • 1h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.6k • 🔱 1.0k • 3d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 5.3k • 🔱 461 • 3d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.0k • 🔱 535 • 9d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.2k • 🔱 551 • 1d ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.8k • 🔱 233 • 6d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.5k • 🔱 199 • 1d ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 177 • 14h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.1k • 🔱 282 • 4h ago

---

---

*Generated by PeekDeck - A glance is all you need*

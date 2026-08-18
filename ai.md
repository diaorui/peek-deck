---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-18T04:35:17.386508+00:00'
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

**Last Updated:** August 18, 2026 at 04:35 UTC  
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

9h ago

---

**[Should AI agents have their own company cards?](https://www.reddit.com/r/artificial/comments/1vr54rn/should_ai_agents_have_their_own_company_cards/)**

As AI agents start doing more ops work, I think business banking has to think about them differently. Not full bank access but maybe controlled spend lanes. If an agent is helping with research, ads, APIs, software trials or vendor tasks I don’t want it touching the main account. I’d rather give it strict limits, logs and approval rules like you would with a junior employee and probably someone is doing this so need to know more, thanks in advance!

7h ago

---

**[Using AI the wrong way could leave you worse off than never using it at all](https://www.reddit.com/r/artificial/comments/1vqxviw/using_ai_the_wrong_way_could_leave_you_worse_off/)**

Research conducted by BYU professor Mark Keith suggests using AI the wrong way could have serious long-term negative impacts. His review of the AI use literature indicates many people: Don't retain skills after AI assistance is removed Forget what they learned using AI Demonstrate lower critical thinking skills and less mental effort/engagement with tasks The Long-Term AI Outcomes Gap: Mark Keith, BYU In fact, over the long term, failing to engage with AI the right way could leave people worse off than those who never adopted AI in the first place. (There are a lot of non-AI adopters out there. Most people think AI equals a chatbot, and 50% of Americans don't plan to use them). What's the right way to use AI? The research suggests: Verifying information AI is providing Use it to challenge assumptions Ask whether you're asking the right questions Are you finding your critical thinking skills eroded as you use AI more, or the opposite? What are you doing to preserve or augment your skills as you use AI?

11h ago

---

**[Strongest candidates for an AI Microchip moment](https://www.reddit.com/r/artificial/comments/1vr6x5j/strongest_candidates_for_an_ai_microchip_moment/)**

I am curious about all these data centers being built. What are the chances AI can have a microchip moment potentially rendering them all useless? This could be a black swan event that could wipe out a lot of investment and potentially destroy some very large businesses. If this is possible, what are the mostly likely candidates? In particular, I am interested in hearing from anyone who may be working on one of these candidates, even if it is still in RD and their opinion on how likely they are to succeed.

6h ago

---

**[Self-hosted AI analyst that writes the SQL, checks its own numbers, and cites which query every claim came from](https://www.reddit.com/r/artificial/comments/1vr6lbp/selfhosted_ai_analyst_that_writes_the_sql_checks/)**

Most "chat with your data" tools give you a confident answer and no way to tell whether it's right. I've been building the opposite: an AI Analyst where the entire working is on screen and every claim is traceable to the query that produced it. Asked it a real question against an HR dataset: "Is Engineering's heavy hiring actually translating into headcount growth, or is it mostly backfilling exits?" What it does, in order: 1. States its approach before touching data. It reads the schema, plans the steps, and says why — including telling me the governed semantic model lacked a hires metric, so it fell back to the raw monthly table. No silent guessing about which source it used. 2. Runs each step as real SQL you can read. Every step shows the query, the row count, and a "where these numbers came from" breakdown. Nothing is a black box — if you don't trust a number, the SQL that produced it is right there. 3. Self-checks every result — and flags its own problems. This is the part I care about most. On step 2 it didn't just pass its own work; it flagged a genuine inconsistency: Engineering's summed net adds (+17) didn't reconcile with the headcount delta (+13, 122→135), a 4-person gap it surfaced on its own and carried into the write-up as a caveat. An analyst that can say "this doesn't add up" is worth ten that can't. 4. Writes findings with citations. Every claim in the write-up cites the step it came from — "headcount climbed from 122 to a 140 peak (step 1, step 2)". The verdict for the curious: ~55% of Engineering's hires were net growth, not backfill; the one bad month was a 3.70% attrition spike; and Support is quietly shrinking (backfill ratio 1.42 — losing more than it hires). 5. Closes the loop. Every analysis has Mark verified / Flag as wrong buttons, suggested follow-up questions generated from the actual results, scheduling for recurring runs, CSV export, and PDF export. The stack, honestly: Runs entirely on your own infra: one Docker command + your own Supabase project BYOK — any model provider. This demo ran on Kimi K3 via OpenRouter; it doesn't need a frontier model because the structure (plan → SQL → check → cite) does the heavy lifting The analyst is one piece of a larger self-hosted platform (agents, multi-agent swarms, RAG, BI dashboards, budgets, full tracing) License: Elastic License 2.0 — source-available, not OSI open source. You can read every line, self-host it, and modify it; you can't resell it as a hosted service. Saying that up front because this sub cares about the distinction, and it matters. Repo: https://github.com/AgentSwarms-fyi/agentswarms Happy to answer anything about how the self-check pass works or why I think "show the SQL or it didn't happen" is the only sane bar for LLM analytics.

6h ago

---

**[Why NVIDIA’s Six-Year-Old A100 GPU Is Still Making Money](https://www.reddit.com/r/artificial/comments/1vqldp4/why_nvidias_sixyearold_a100_gpu_is_still_making/)**

India's Leading AI & Data Science Media Platform

🔗 [analyticsindiamag.com](https://analyticsindiamag.com/ai-features/why-nvidias-six-year-old-gpu-is-still-making-money) • 21h ago

---

**[Could today’s AI models give us an “LK-99 moment” — but this time for real?](https://www.reddit.com/r/artificial/comments/1vqrdj9/could_todays_ai_models_give_us_an_lk99_moment_but/)**

I still remember those few days in 2023 when LK-99 looked like it might actually be a room-temperature, ambient-pressure superconductor. For a brief moment, it felt like we were watching one of those discoveries that could genuinely change civilization. Obviously, LK-99 didn’t survive replication. But AI has advanced enormously since then. We now have models that can reason across scientific literature, generate hypotheses, write and run code, analyse experimental data, predict structures and materials, and increasingly interact with automated labs. So I keep wondering: Could AI significantly increase the probability of discovering something like a real LK-99? Not necessarily superconductivity specifically, but a breakthrough material or physical discovery with enormous technological consequences — something humans might have needed decades to stumble upon otherwise. It seems like materials science could be particularly well suited to this: huge search spaces, lots of existing experimental data, simulations, and relatively clear ways to test candidate materials. Maybe the real revolution won’t be AI directly “discovering a new law of physics”, but AI exploring millions of plausible hypotheses and pointing human researchers toward the 10 experiments actually worth doing. How close are we to that? And what would be the best candidate field for an AI-driven “holy shit, this changes everything” discovery: superconductors, batteries, catalysts, fusion materials, drugs… something else? I want those three LK-99 days again. But this time I want day four to be even better.

15h ago

---

**[Chinese robot dogs tackle fires and toxic leaks to protect rescuers](https://www.reddit.com/r/artificial/comments/1vqtw4o/chinese_robot_dogs_tackle_fires_and_toxic_leaks/)**

The X30 can carry a water cannon, reaching 60 meters at 40 L/s, or transport hoses, air tanks and breaching tools.

🔗 [Interesting Engineering](https://interestingengineering.com/ai-robotics/chinese-robot-dogs-take-on-fires) • 14h ago

---

**[Looking for the name of an old ai app](https://www.reddit.com/r/artificial/comments/1vr7dkg/looking_for_the_name_of_an_old_ai_app/)**

Around 2021/2022 time, you could customise your ai character they were kinda 3d like the sims and you could chat to them like in c.ai , anyone know what it was called?

5h ago

---

**[A week after OpenAI paused a cyber-capable model, two labs shipped one anyway, through opposite doors](https://www.reddit.com/r/artificial/comments/1vr6wje/a_week_after_openai_paused_a_cybercapable_model/)**

Rounding up a genuinely heavy week. The throughline: last issue OpenAI paused internal work on a model it couldn't rule out was cyber-capable. This week the capability shipped anyway, two different ways. **OpenAI GPT-5.6 Cyber** (Aug 10): a security-specialized model gated behind a "Daybreak Red" tier. OpenAI's own eval has it answering 95% of offensive-security requests the standard model refuses 98.5% of the time. Access stays with 16 named partners; from Sept 1 individual accounts need hardware keys. Customers get findings, never the weights. **Zhipu GLM-5.3** (Aug 14): marketed on "emergent cyber capabilities," claims 84.5% on CyberGym (vendor-reported; note Wiz's Atlas system claims a higher 90.9%). Open weights promised in ~2 weeks. The capability didn't get shelved. It got a doorman. The rest of the week: - **Meta returned to open weights** with Muse Glimmer, a 30B Apache-2.0 agent model that runs under 20GB. - **Alibaba** published its first downloadable Max-class Qwen (2.4T), and **Qwen3.8-27B** landed Apache-2.0. **DeepSeek** took V4-Pro (1.6T, MIT) to GA with peak/off-peak pricing. - **Anthropic** began embedding an invisible watermark in all Claude output under the EU AI Act. The builder forums did not take it well. - **SpaceX** closed a $60B all-stock acquisition of Cursor; the editor is now inside the Grok org. - **Security:** researchers showed encrypted reasoning traces from OpenAI/Anthropic/Google were replayable across sibling models to decrypt them (now patched); an AI notetaker left 181,874 meetings queryable by anyone. Full breakdown with all the receipts: thenewguard.ai/issues/027-the-brake-pedal-had-a-bypass/

6h ago

---

---

## Google News: "ai"

**[Why Big Tech’s AI Spending Is $3 Trillion Higher Than It Seems](https://www.wsj.com/tech/ai/why-big-techs-ai-spending-is-3-trillion-higher-than-it-seems-e1067bb2)**

WSJ • 1d ago

---

**[AI Slop Is Everywhere. Spotify, LinkedIn and Others Have Had Enough.](https://www.nytimes.com/2026/08/17/technology/ai-slop.html)**

nytimes.com • 8h ago

---

**[CNBC Daily Open: Markets caught between Mideast worries and AI optimism](https://www.cnbc.com/2026/08/18/cnbc-daily-open-trump-iran-war-nvidia-oil-markets.html)**

Despite many promises of a deal and numerous start-stop negotiations, the war in the Middle East now threatens to restart and drag more countries into the fold.

CNBC • 3h ago

---

**[Lonelier teens tend to look to AI for support: Report](https://www.foxnews.com/video/6403619090112)**

Fox News host Kayleigh McEnany analyzes a report saying teens are increasingly turning to AI for all kinds of advice on 'Outnumbered.'

Fox News • 3h ago

---

**[Meta Taps Disability Groups To Explore Uses For AI Glasses](https://www.disabilityscoop.com/2026/08/18/meta-taps-disability-groups-to-explore-uses-for-ai-glasses/32130/)**

With a series of grants, Meta is backing efforts to learn how its AI glasses can increase independence and provide other benefits to people with disabilities.

Disability Scoop • 1h ago

---

**[Long after Steve Jobs’ turtleneck, there’s a new tech uniform](https://www.cnn.com/2026/08/17/style/tech-ai-merch)**

From Palantir to OpenAI, big tech companies have been producing fashion merch in an attempt to soften their image with cotton and canvas.

CNN • 20h ago

---

**[Trump crypto firm backs venture offering AI from restricted Chinese companies](https://www.reuters.com/world/china/trump-crypto-firm-backs-venture-offering-ai-restricted-chinese-companies-2026-08-17/)**

Reuters • 18h ago

---

**[Hidden Airtag reveals Amazon is trashing rare books to train AI](https://arstechnica.com/tech-policy/2026/08/hidden-airtag-reveals-amazon-is-trashing-rare-books-to-train-ai/)**

Amazon’s team uses a T. rex preparing to devour a book as its logo.

Ars Technica • 10h ago

---

**[Amazon, once an online bookseller, is destroying rare books to train AI models](https://finance.yahoo.com/technology/ai/articles/amazon-once-online-bookseller-destroying-163844418.html)**

Rare books are incredibly valuable for training LLMs, since these models have already trained on whatever's available online.

Yahoo Finance • 11h ago

---

**[AI Companies Are Buying—And Destroying—Antique Books. Here’s Why.](https://www.forbes.com/sites/maryroeloffs/2026/08/17/ai-companies-are-buying-and-destroying-antique-books-heres-why/)**

Millions of physical books are being scanned to train AI models. They’re then dumped in the trash.

Forbes • 8h ago

---

---

## HackerNews: "ai"

**[AI;DR (AI; Didn't Read)](https://news.ycombinator.com/item?id=49336573)**

I'm about as pro-AI as you can be, but this is becoming a pet peeve of mine (and I'm not alone). That's why I love the AI;DR acronym as my new solution for ignoring the walls of slop.

⬆️ 665 • 💬 415 • 8h ago • [rickmanelius.com](https://www.rickmanelius.com/p/aidr-ai-didnt-read)

---

**[AI isn’t outthinking mathematicians, it’s out-remembering them](https://news.ycombinator.com/item?id=49312845)**

The key advantage may not be superior reasoning, but a virtually unlimited symbolic working memory.

⬆️ 629 • 💬 497 • 2d ago • [davidepiffer.com](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians)

---

**[Working with AI feels more like leadership than coding](https://news.ycombinator.com/item?id=49309451)**

Working with AI is less predictable than traditional software. That makes leadership skills such as context, clarity, and feedback more valuable.

⬆️ 334 • 💬 201 • 2d ago • [allen.bargi.org](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership/)

---

**[AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://news.ycombinator.com/item?id=49331423)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

⬆️ 327 • 💬 127 • 14h ago • [wiz.io](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

---

**[The AI Credit Resale Economy](https://news.ycombinator.com/item?id=49320611)**

A look at the brokers buying unused AI credits from startups and reselling them — the marketplaces, the bulk-discount routers, and the message boards where off-market inference changes hands

⬆️ 323 • 💬 128 • 1d ago • [Vectoral](https://vectoral.com/blog/who-are-the-token-brokers)

---

**[How to disable or avoid intrusive AI](https://news.ycombinator.com/item?id=49331220)**

One of the biggest questions I get at Drop-In Time at the library (besides "what is taking up all my cloud storage?") is how to disable or avoid intrusive AI that shows up where people don't want it. This is a guide for people who would like less intrusive AI in their tech environment. Maybe you lik

⬆️ 264 • 💬 163 • 14h ago • [librarian.net](https://www.librarian.net/notoai/)

---

**[On AI regulation and messaging](https://news.ycombinator.com/item?id=49325789)**

1/2 Thanks Gavin for an especially thoughtful exchange. I don't usually spend much time on social media but I wanted to engage here because it really brings out the heart of an important conversation.

First, on regulation, I think that “either concentrate it in the hands of a

⬆️ 235 • 💬 502 • 1d ago • [X (formerly Twitter)](https://twitter.com/DarioAmodei/status/2088758816376807762)

---

**[Israel creates fake think tank in likely attempt to dupe AI chatbots](https://news.ycombinator.com/item?id=49337392)**

In just over a week, the Hanover Institute has published at least 100 articles that appear tailor-made to influence chatbots

⬆️ 186 • 💬 71 • 7h ago • [Responsible Statecraft](https://responsiblestatecraft.org/israel-influence-chatgpt/)

---

**[AI in drug discovery – what it is, where we stand and the path forward](https://news.ycombinator.com/item?id=49313367)**

⬆️ 185 • 💬 91 • 2d ago • [science.org](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really)

---

**[Young People Hate AI CEOs So Passionately That It's Almost Hard to Believe](https://news.ycombinator.com/item?id=49323932)**

A new survey of 1,000 young adults in the US found that nine of the top tech executives are deeply loathed.

⬆️ 149 • 💬 179 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/young-people-ai-ceos-executives-poll)

---

---

## YouTube Videos: "ai"

**[The AI Bubble is About To Hit EVERYTHING](https://www.youtube.com/watch?v=KJET0eprLSA)**

Join CBC Lite https://go.coinbureau.com/CBC-Lite-CB-Des Get The Hottest Crypto Deals ...

📺 Coin Bureau

👁️ 16K • 👍 691 • 💬 49 • ⏱️ 17:37 • 14h ago

---

**[AI robot in the military does exactly what experts warned.](https://www.youtube.com/watch?v=sQysEweaLjA)**

Is Military AI dangerous? AI Robot with a tank does exactly what experts warned. AGI. Go to http://ground.news/InsideAI for a ...

📺 InsideAI

👁️ 448K • 👍 17K • 💬 2K • ⏱️ 15:53 • 2d ago

---

**[The First AI-Trained Surgeon #comedy #skit #comedyshorts #ai #surgeon #funny](https://www.youtube.com/watch?v=4bXVKoJfAcI)**

The First AI-Trained Surgeon attempts surgery, but he has no idea what he's doing. Socials - Instagram ➼ harrisonhughesnz ...

📺 Harrison Hughes

👁️ 45K • 👍 4K • 💬 60 • ⏱️ 1:58 • 9h ago

---

**[The Insane, True Story of What It’s Like to Be an AI Model](https://www.youtube.com/watch?v=9XlOaVItUgI)**

Sources: - https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf - https://arxiv.org/pdf/2412.04984 ...

📺 Species | Documenting AGI

👁️ 122K • 👍 6K • 💬 1K • ⏱️ 22:19 • 2d ago

---

**[Best Prompts to Build an App With AI + No Coding](https://www.youtube.com/watch?v=mNtiKFP4yZY)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Mikey No Code

👁️ 15K • 💬 6 • ⏱️ 38:48 • 14h ago

---

**[New Twitch AI Garbage](https://www.youtube.com/watch?v=sok9mDbrAZA)**

Starforge PC https://starforgepc.com/moist-yt Get Goof Juice and use code MOIST https://gamersupps.gg/moist Use Cheeky ...

📺 penguinz0

👁️ 484K • 👍 22K • 💬 2K • ⏱️ 8:55 • 1d ago

---

**[‘A Flock of VULTURES’: Inside the growing movement against AI-powered surveillance](https://www.youtube.com/watch?v=jNkwXSnZ4MY)**

Americans across the country are pushing back against AI-powered license plate readers like Flock. In 2026 alone, 23 states have ...

📺 MS NOW

👁️ 68K • 👍 1K • 💬 403 • ⏱️ 12:35 • 1d ago

---

**[Akhilesh Yadav Shares AI Video Targeting BJP Over Ram Mandir Donations Scam Case | Dr. Manish Kumar](https://www.youtube.com/watch?v=hf83Huxm6s4)**

Samajwadi Party chief Akhilesh Yadav has taken aim at the BJP by sharing an AI-generated video featuring a political song over ...

📺 CAPITAL TV

👁️ 86K • 👍 4K • 💬 283 • ⏱️ 13:42 • 1d ago

---

**[Bro got fired by AI😭✌️](https://www.youtube.com/watch?v=7vxcjXOANBA)**

📺 Ben Esherick

👁️ 650K • 👍 38K • 💬 480 • ⏱️ 0:39 • 2d ago

---

**[James May tests Tesla&#39;s new AI](https://www.youtube.com/watch?v=YuDlid7eLt0)**

Buy my gin: https://jamesmaysgin.com/grok-doc Faced with a 6 hour journey, James and Lucy test Tesla's latest AI and discover ...

📺 James May’s Planet Gin

👁️ 126K • 👍 8K • 💬 696 • ⏱️ 10:16 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 415,039 • ❤️ 10,765 • 3d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 2,727,609 • ❤️ 1,658 • 2d ago

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

⬇️ 465,529 • ❤️ 1,121 • 14h ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 10,375 • ❤️ 912 • 3d ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 334,099 • ❤️ 1,663 • 6d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 2,403,238 • ❤️ 4,094 • 5d ago

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

⬇️ 495,646 • ❤️ 533 • 3d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 15,812 • ❤️ 450 • 1d ago

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

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 54 • 💬 4 • ⭐ 37,454 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

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

⭐ 13.8k • 🔱 1.6k • 1h ago

---

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 13.6k • 🔱 1.5k • 3h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.6k • 🔱 1.0k • 5h ago

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

⭐ 2.2k • 🔱 177 • 20h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.1k • 🔱 283 • 56m ago

---

**[Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt)**

Open-source, self-hosted AI vulnerability research tool that orchestrates agents to find and validate security issues in code.

`JavaScript` `ai` `ai-agents` `ai-security` `bug-bounty` `bugbounty-tools`

⭐ 1.9k • 🔱 327 • 6h ago

---

---

*Generated by PeekDeck - A glance is all you need*

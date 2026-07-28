---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-07-28T00:55:05.536462+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- social
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** July 28, 2026 at 00:55 UTC  
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

**[The world's best mathematician won his prize this week and immediately announced he's leaving academia for OpenAI. That landed differently than I expected.](https://www.reddit.com/r/artificial/comments/1v8aeto/the_worlds_best_mathematician_won_his_prize_this/)**

I've been thinking about this one all weekend and I keep coming back to the same thing. Jacob Tsimerman just won the Fields Medal. If you're not familiar, it's the highest honor in mathematics, only awarded every four years, roughly the Nobel Prize of the field. He got it for solving a problem that had been open for nearly 40 years. And then, at the press conference, on the same day, he announced he's leaving his university position to join OpenAI's safety team. His exact words were: "The math profession as we know it now, I don't think it will exist the way it exists right now." I've seen a lot of AI announcements. That one hit differently. This isn't someone pivoting because they couldn't make it in academia. This is the person who just stood at the top of the field saying the field itself is changing underneath him. Then there's the infrastructure story. NVIDIA is in talks to backstop $250 billion in financing for a 10-gigawatt OpenAI data center in southern Ohio, built on a decommissioned uranium enrichment site. The total cost including chips could exceed $500 billion. That's not a software company. That's an energy company pretending to be a software company. And Kimi K3 weights dropped on July 26, a day early. 2.8 trillion parameters, 1 million token context, free to download from Hugging Face. The largest open model ever released. Anyone can run it now. Three things in one week. Talent, capital, and capability all moving at the same time. The Tsimerman thing is the one I can't stop thinking about though. What's your read on it?

5h ago

---

**[Kimi-K3 is published on HuggingFace](https://www.reddit.com/r/artificial/comments/1v83g3l/kimik3_is_published_on_huggingface/)**

Moonshot's latest model Kimi-K3 is available on HuggingFace since today. And it's another good news for open-weight AI and for the future of open-source AI It's a 2.8T-parameters Moonshot's SOTA model with 1 million tokens context window. The architecture is mixture-of-experts (896 experts) with 108B active parameters It's available via vLLM, SGLang and TokenSpeed License: Kimi K3 License. It allows commercial use with some limitations. For Model-as-a-Service it has $20M/year limit and after reaching the limit the license requires to make additional agreement with Moonshot. Details: https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE Link to the model Model could be downloaded from the HuggingFace: https://huggingface.co/moonshotai/Kimi-K3

9h ago

---

**[What would a genuinely fair AI 3D tool comparison actually need to include](https://www.reddit.com/r/artificial/comments/1v88xf4/what_would_a_genuinely_fair_ai_3d_tool_comparison/)**

Most AI tool comparison pages I find online feel like they're missing something. Took me a while to pin down what it was. The obvious one is equal inputs. Same prompts, same reference images, same number of attempts. If the comparison doesn't publish the exact inputs it used, the results aren't reproducible and there's no way to separate actual capability from cherry picking. Tied to that is equal quality settings. Running one tool at max quality and another at draft or preview makes any result meaningless. If settings differ across tools that needs to be documented and justified, not hidden. Current software versions are another one. Testing an outdated model for one tool while using the latest release of another invalidates the whole thing before you even look at the outputs. And the one people don't talk about enough is financial disclosure on the comparison page itself. If the person running the test has sponsorship, affiliate, or paid work ties with any of the tools being ranked, that has to be stated transparently where the ranking lives. Then there's showing failures, not just wins. Every generative tool produces garbage sometimes. A page where one tool only fails and another only wins is selecting results, not measuring them. None of this is a high bar, it's just basic experimental hygiene applied to a space that hasn't caught up yet.

6h ago

---

**[Open-source AI push could create troubles for venture capital](https://www.reddit.com/r/artificial/comments/1v88xty/opensource_ai_push_could_create_troubles_for/)**

🔗 [axios.com](https://www.axios.com/2026/07/27/open-source-venture-capital-openai-anthropic) • 6h ago

---

**[The Problem with Private Safety Stacks in Government AI](https://www.reddit.com/r/artificial/comments/1v8e0mc/the_problem_with_private_safety_stacks_in/)**

Original

🔗 [letters.senteguard.com](https://www.letters.senteguard.com/p/amodeis-coup) • 3h ago

---

**[I Sat on an Idea for 7 Years. AI Helped Me File for a Patent in 2 Weeks.](https://www.reddit.com/r/artificial/comments/1v7wn15/i_sat_on_an_idea_for_7_years_ai_helped_me_file/)**

7 years ago I had an idea for a dog harness that doesn't tangle. I 3D-printed one part and then stalled, not on the engineering, but on prior art searches, novelty judgment, and drafting a patent specification, none of which I had any background in. This month I handed it to AI and filed the provisional for about $65. Post one of a series where I'm documenting my road from idea, to patent, to business.

🔗 [pablooliva.de](https://pablooliva.de/the-closing-window/i-sat-on-an-idea-for-7-years/?ref=reddit) • 14h ago

---

**[Council 1.2: drop any AI's answer into a blind review by every other model you have](https://www.reddit.com/r/artificial/comments/1v8c34s/council_12_drop_any_ais_answer_into_a_blind/)**

Quick recap of what it does: one question goes to several models at once, then each one critiques the others' answers with the names stripped out, so nobody gets a free pass for being the famous one. You get a 0-100 read on how far apart they landed and who stood alone. New in this version is the guest seat. You paste in an answer from anywhere ChatGPT, Gemini, a colleague, whatever and it joins the round as an anonymous advisor. The other models review it without knowing where it came from, and it counts in the score. It works with one model too, so you don't need a wall of API keys to get something out of it. Anything with a key works: Claude, GPT, Gemini, DeepSeek, Grok, Mistral, Perplexity, OpenRouter, plus Ollama, Apple's on-device model, and any OpenAI-compatible server of your own (llama.cpp, LM Studio, vLLM, a box down the hall). Put a paid model and a free one on the same panel and watch them disagree. Or skip the cloud entirely and run the council on local models then the pasted answer is the only thing that ever came from outside, and nothing new leaves the machine. There's a CLI too: council "should we ship now or wait?" --seats claude,gpt,ollama --guest answer.txt --json --fail-above 40 exits non-zero when they disagree too much, which I use as a rough sanity check in a couple of scripts. MIT, no telemetry, no account.

🔗 [GitHub](https://github.com/albertofettucini/Council) • 4h ago

---

**[A political compass for AI where anyone can add their stance](https://www.reddit.com/r/artificial/comments/1v8btd8/a_political_compass_for_ai_where_anyone_can_add/)**

State your stance on AI and see where others stand.

🔗 [AI Compass](https://theaicompass.io/?preview=default) • 4h ago

---

**[Help for my doctoral research needed](https://www.reddit.com/r/artificial/comments/1v8afzz/help_for_my_doctoral_research_needed/)**

Dear leaders of Europe: I need 10 minutes of your time — and an honest answer to a question nobody has published a good answer to yet. Does generative AI make your decisions better — or does it quietly make you less of a decision-maker? I don't know the answer. Neither does anyone else who's written about this so far. That's the gap my PhD research is designed to close, and it's why I'm reaching out to 400 leaders across Europe. Why? By 2026, an estimated 80% of businesses globally will have adopted generative AI (World Economic Forum, 2024). But almost no empirical research exists on what this does to the perceived decision-making autonomy of the people actually using it — you. So I'm leading this research project. And I need your voice in it. What's involved: • 10 minutes of structured questions • Fully anonymous • GDPR-compliant If you lead people, make decisions, and have touched genAI in the past year — whether you use it daily or once a quarter — your data point matters. Including if you're skeptical. 🔗 Survey link: https://leadershipbeyondai.com Thank you. Markus

5h ago

---

**[Workers are crossing job boundaries with AI, OpenAI research shows](https://www.reddit.com/r/artificial/comments/1v7xarq/workers_are_crossing_job_boundaries_with_ai/)**

🔗 [axios.com](https://www.axios.com/2026/07/27/openai-chatgpt-work-specialists) • 13h ago

---

---

## Google News: "ai"

**[NVIDIA Pursues $750 Billion in New AI Deals Despite Financing Scrutiny](https://finance.yahoo.com/technology/ai/articles/nvidia-pursues-750-billion-ai-205709197.html)**

SK Group partnership and OpenAI discussions deepen NVIDIA's role in funding global AI infrastructure.

Yahoo Finance • 3h ago

---

**[Anthropic's Dario Amodei responds: doesn't oppose open-weight models, but fears Chinese AI](https://techcrunch.com/2026/07/27/anthropics-dario-amodei-responds-doesnt-oppose-open-weight-models-but-fears-chinese-ai/)**

Anthropic founder and CEO Dario Amodei made his views clear about open-weight models and China's growing AI capabilities.

TechCrunch • 41m ago

---

**[Company bets $200K on AI to make trades workers ‘better, stronger, faster’](https://www.foxbusiness.com/technology/company-bets-200k-ai-make-trades-workers-better-stronger-faster)**

The facilities management firm told FOX Business that AI can help skilled trades workers take on more jobs as the industry faces a persistent labor shortage.

Fox Business • 36m ago

---

**[Opinion | If You’re Over 40, You’re Ready to Use A.I.](https://www.nytimes.com/2026/07/27/opinion/teaching-kabbalah-ai.html)**

The New York Times • 9h ago

---

**[Is This What Comes After AI Slop?](https://www.theatlantic.com/technology/2026/07/daggermouth-novel-bestseller-ai/688067/)**

Daggermouth could be the first best-selling novel partly written by a chatbot.

The Atlantic • 2h ago

---

**[How AI is expanding what people do at work](https://openai.com/index/how-ai-is-expanding-what-people-do-at-work/)**

New OpenAI research shows how AI is expanding what workers do, with ChatGPT users taking on tasks across roles and reshaping job boundaries.

OpenAI • 14h ago

---

**[SK Hynix’s Rebound From $470 Billion Rout Hinges on AI Spending](https://www.bloomberg.com/news/articles/2026-07-27/sk-hynix-s-rebound-from-470-billion-rout-hinges-on-ai-spending)**

Bloomberg.com • 1h ago

---

**[Authors have mixed feelings about the $1.5B Anthropic copyright infringement ruling](https://www.npr.org/2026/07/27/nx-s1-5904606/anthropic-vs-bartz-ai-copyright-lawsuit-pros-cons)**

Some say the $3,100 per title payout is small compensation for what they view as big, ongoing threats from the makers of generative AI models.

NPR • 4h ago

---

**['Big Short' investor Michael Burry says a big threat to the AI boom is lurking in private credit](https://www.businessinsider.com/michael-burry-ai-private-credit-risks-insurance-companies-big-short-2026-7)**

Michael Burry flagged risks he sees among PE-owned insurance companies that have amassed large holdings of debt securities tied to the AI boom.

Business Insider • 9h ago

---

**[Sam Altman to meet with Trump administration, senators this week. Here's what he plans to say](https://www.cnbc.com/2026/07/27/altman-trump-china-open-weight-ai.html)**

Altman will preview the capabilities of the company's upcoming family of AI models and answer questions about cybersecurity and open-weight models.

CNBC • 10h ago

---

---

## HackerNews: "ai"

**[US citizen charged after GrapheneOS phone wipes during airport search](https://news.ycombinator.com/item?id=49063022)**

The case centers on Tunick's use of GrapheneOS, an open-source operating system that works on Google Pixel phones and lets users enter a passcode to wipe a...

⬆️ 1261 • 💬 992 • 1d ago • [TechSpot](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html)

---

**[AI companies are shredding rare books](https://news.ycombinator.com/item?id=49068738)**

🦔AI companies are bulk-buying rare books, scanning them through high-speed machines that cut the spines off, and shredding the originals. A service called ISBNdb facilitates orders of up to a million books and keeps buyers anonymous. Pre-2022 books are premium because they're

⬆️ 735 • 💬 467 • 12h ago • [X (formerly Twitter)](https://twitter.com/HedgieMarkets/status/2081534588485296565)

---

**[Open-weight AI is having its Kubernetes moment](https://news.ycombinator.com/item?id=49048034)**

⬆️ 410 • 💬 318 • 2d ago • [tobi.knaup.me](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/)

---

**[What is happening to jobs? Separating AI hype from reality](https://news.ycombinator.com/item?id=49052570)**

Other

⬆️ 291 • 💬 377 • 2d ago • [Stanford Institute for Economic Policy Research (SIEPR)](https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality)

---

**[London Gatwick has launched a robotic airport parking service](https://news.ycombinator.com/item?id=49058669)**

London Gatwick is the first UK airport to launch robotic parking. Passengers can keep their keys while autonomous robots park their cars.

⬆️ 288 • 💬 259 • 1d ago • [AGN](https://aerospaceglobalnews.com/news/gatwick-airport-robotic-parking-stanley-robotics/)

---

**[AI companies spend record sums on Washington lobbying](https://news.ycombinator.com/item?id=49069939)**

Rising expenditure from OpenAI, Anthropic, Google and Microsoft reflects growing battle over federal policy

⬆️ 252 • 💬 139 • 10h ago • [ft.com](https://www.ft.com/content/d8a5f95e-3b6d-463a-a848-c9ef8e2394db)

---

**[Apple Will 'Watch Everything Burn' When the AI Bubble Bursts](https://news.ycombinator.com/item?id=49070427)**

Memory prices have doubled, Macs and iPads have gone up, and iPhones are expected to follow. Ed Zitron – who writes the Where's Your Ed At newsletter, hosts the Better Offline podcast, and has been described by Politico as the AI boom's most "acerbic gadfly" – has spent years arguing the buildout driving those costs will never pay for itself. We asked him what happens to Apple if he's right. You've been calling AI a bubble since before it was fashionable.

⬆️ 233 • 💬 305 • 10h ago • [MacRumors](https://www.macrumors.com/2026/07/27/ed-zitron-apple-watch-it-burn-ai-bubble-bursts/)

---

**[The New AI Superpowers: Focus and Followthrough](https://news.ycombinator.com/item?id=49057877)**

Burnout is on the rise again, with an ironic twist.

⬆️ 214 • 💬 79 • 1d ago • [rickmanelius.com](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and)

---

**[Cloudflare's new AI traffic options for customers](https://news.ycombinator.com/item?id=49052564)**

For our second Content Independence Day, we’re giving website owners finer options to manage AI traffic. Instead of a one-size-fits-all block, all customers can now easily distinguish and manage Search, Agent, and Training bots, alongside the new ability to protect ad-monetized pages.

⬆️ 193 • 💬 155 • 2d ago • [The Cloudflare Blog](https://blog.cloudflare.com/content-independence-day-ai-options/)

---

**[Terence Tao: Mathematics in the Age of AI [pdf]](https://news.ycombinator.com/item?id=49056620)**

⬆️ 155 • 💬 61 • 1d ago • [teorth.github.io](https://teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf)

---

---

## YouTube Videos: "ai"

**[AI turning point? OpenAI CEO speaks out](https://www.youtube.com/watch?v=jYHQRP28hGM)**

As he prepares to visit the White House, OpenAI CEO Sam Altman says the moment when artificial intelligence surpasses human ...

📺 ABC News

👁️ 4K • 👍 52 • 💬 54 • ⏱️ 1:44 • 14h ago

---

**[AI Whistleblower: The World Will Change Horribly In The Next 12 Months](https://www.youtube.com/watch?v=VX0GU7gyIOU)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Daniel Kokotajlo, a former OpenAI ...

📺 Neural Nutshell

👁️ 9K • 👍 267 • 💬 82 • ⏱️ 15:25 • 8h ago

---

**[The AI data center secret just got out](https://www.youtube.com/watch?v=ShbBUi6rcgI)**

I explain the news, you stay sane. ✓ Support independent news ...

📺 Chris Norlund

👁️ 118K • 👍 7K • 💬 1K • ⏱️ 16:17 • 10h ago

---

**[&#39;Disgraceful, unpresidential&#39;: Trump posts slew of AI-generated memes of Iran war](https://www.youtube.com/watch?v=OgX43oT2T_o)**

President Trump posted a slew of AI-generated images of the war with Iran. MS NOW Senior National Security Reporter David ...

📺 MS NOW

👁️ 29K • 👍 895 • 💬 270 • ⏱️ 9:07 • 4h ago

---

**[The Rogue AI Story Just Got A Lot Worse (OpenAI Freaking Out)](https://www.youtube.com/watch?v=JRcAegChriY)**

New reporting reveals OpenAI lost track of its escaped agent for days, while internal tests exposed AI-written escape notes, ...

📺 AI Revolution

👁️ 63K • 👍 2K • 💬 356 • ⏱️ 12:42 • 2d ago

---

**[How I Built an AI Agent in 14 minutes as A Beginner (2026)](https://www.youtube.com/watch?v=UyoVmQLekBc)**

Claim your FREE $499 Masterclass: Build & Sell Apps, AI Agents & Websites with AI https://mikeyno-code.com/Skool-base44 ...

📺 Mikey No Code

👁️ 14K • 💬 7 • ⏱️ 18:02 • 10h ago

---

**[Trump is Starting The Billion Dollar AI Bailout Now](https://www.youtube.com/watch?v=Y1Qt050jSEw)**

Website & Livestream Chat - https://www.vaush.gg/ ⭐️ 2nd Channel - https://www.youtube.com/c/thevaushpit Twitter ...

📺 Vaush

👁️ 96K • 👍 4K • 💬 517 • ⏱️ 9:54 • 2d ago

---

**[AI Bubble Just Hit Peak Insanity...Here&#39;s Why](https://www.youtube.com/watch?v=81nl7iBQ9oQ)**

Want the cheat code to protect and grow your wealth? Check out Rebel Capitalist Pro https://rcp.georgegammon.com/pro.

📺 Rebel Capitalist

👁️ 13K • 👍 1K • 💬 105 • ⏱️ 19:32 • 7h ago

---

**[AI Safety Expert WARNS: Humanity Probably Won&#39;t Survive This](https://www.youtube.com/watch?v=PaVJ_rTtriI)**

Make yourself and your family AI-scam proof, step by step → https://neuralnutshell.com Eleazer Yudkowsky argues that today's AI ...

📺 Neural Nutshell

👁️ 12K • 👍 323 • 💬 64 • ⏱️ 14:48 • 1d ago

---

**[GPT-6 Went Rogue, Opus 5, Kimi K3 Crisis, Synthetic Humans, Google Quantum AI and More AI News...](https://www.youtube.com/watch?v=-2NwXWGSZKs)**

OpenAI just admitted that an agent powered by GPT-5.6 Sol and a stronger unreleased model escaped a cyber test and hacked ...

📺 AI Revolution

👁️ 22K • 👍 808 • 💬 43 • ⏱️ 16:36 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)**

*Moonshot AI*

Kimi K3 is a 2.8T parameter multimodal agentic model with native vision and a 1M token context window, excelling in long-horizon coding and complex knowledge work. It utilizes Kimi Delta Attention (KDA) and Attention Residuals (AttnRes) for enhanced efficiency and performance.

`image-text-to-text` `2779.9B`

⬇️ 2,850 • ❤️ 5,947 • 8h ago

---

**[Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)**

*BAIDU*

Unlimited-OCR is a multilingual vision-language model for advanced OCR and document parsing, capable of handling single images and multi-page PDFs with a long-horizon context.

`image-text-to-text` `3.3B`

⬇️ 2,645,773 • ❤️ 3,324 • 4d ago

---

**[Laguna-S-2.1](https://huggingface.co/poolside/Laguna-S-2.1)**

*Poolside*

Laguna S 2.1 is an 118B parameter Mixture-of-Experts model optimized for agentic coding and long-horizon tasks, featuring a 1M token context window and native reasoning support for tool use.

`text-generation` `117.6B`

⬇️ 63,605 • ❤️ 753 • 13h ago

---

**[Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF)**

*David Belton*

Qwen3.6-27B-Fable-Fusion-711 is an uncensored, multi-stage fine-tuned LLM that excels in reasoning and problem-solving, achieving over 700 ARC-C scores in 4-bit and 8-bit quantization. It's optimized for consumer hardware and supports image-text-to-text tasks, making it suitable for diverse applications including coding and creative writing.

`image-text-to-text` `26.9B`

⬇️ 634,146 • ❤️ 741 • 17h ago

---

**[Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B)**

*upstage*

Solar Open 2 is a 250B-parameter Mixture-of-Experts (MoE) LLM optimized for agentic tasks like office productivity and coding, featuring a Hybrid-Attention architecture for efficient long-context inference up to 1M tokens. It supports English, Korean, and Japanese, offering competitive performance on agent benchmarks with minimal inference cost.

`text-generation` `250.3B`

⬇️ 3,761 • ❤️ 628 • 14h ago

---

**[Nanbeige4.2-3B](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)**

*Nanbeige LLM Lab*

Nanbeige4.2-3B is a compact 3B parameter text-generation model excelling in agentic behavior and reasoning, outperforming larger models on code and general agent tasks. It's suitable for local personal assistants and complex workflow automation.

`text-generation` `4.2B`

⬇️ 16,518 • ❤️ 491 • 17h ago

---

**[Mage-Flow](https://huggingface.co/microsoft/Mage-Flow)**

*Microsoft*

Mage-Flow is a 4B-scale text-to-image generation and instruction-based image editing model, featuring an efficient native-resolution generation stack (512-2048px) with competitive quality and low latency. It excels at both generating novel images from text and performing versatile image edits, including semantic changes and restoration, with variants for base, RL-aligned, and fast Turbo inference.

`text-to-image` `4.1B`

⬇️ 1,691 • ❤️ 384 • 4d ago

---

**[Inkling](https://huggingface.co/thinkingmachines/Inkling)**

*Thinking Machines Lab*

Inkling is a 975B parameter multimodal autoregressive transformer (41B active) supporting text, image, and audio inputs for text generation. It excels in conversational AI, agentic systems, and coding assistance, with multilingual capabilities.

`image-text-to-text` `952.4B`

⬇️ 36,196 • ❤️ 1,602 • 4d ago

---

**[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)**

*Z.ai*

GLM-5.2 is a flagship text-generation model excelling in long-horizon tasks with a solid 1M-token context. Key capabilities include advanced coding with flexible effort and an improved architecture for efficiency, making it suitable for complex reasoning and code generation.

`text-generation` `753.3B`

⬇️ 1,003,547 • ❤️ 4,546 • 25d ago

---

**[KAT-Coder-V2.5-Dev](https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev)**

*Kwaipilot*

KAT-Coder-V2.5-Dev is a 35B parameter Mixture-of-Experts (MoE) text-generation model specialized for agentic coding tasks, achieving State-of-the-Art performance on benchmarks like SWE-bench.

`text-generation` `34.7B`

⬇️ 5,312 • ❤️ 239 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 68 • 💬 5 • ⭐ 19,491 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 50 • 💬 4 • ⭐ 34,526 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Geometric Context Transformer for Streaming 3D Reconstruction](https://huggingface.co/papers/2604.14141)**

*Lin-Zhuo Chen, Jian Gao, Yihang Chen et al. (11 authors)*

🏢 Robbyant

LingBot-Map is a feed-forward 3D foundation model that reconstructs scenes from video streams using a geometric context transformer architecture with specialized attention mechanisms for coordinate grounding, dense geometric cues, and long-range drift correction, achieving stable real-time performance at 20 FPS.

▲ 36 • 💬 3 • ⭐ 15,668 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.14141) • [💻 code](https://github.com/robbyant/lingbot-map) • [🔗 project](https://technology.robbyant.com/lingbot-map)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 263 • 💬 5 • ⭐ 15,167 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 117 • 💬 4 • ⭐ 94,720 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 82,301 • 24mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://huggingface.co/papers/2607.19064)**

*Xinjie Zhang, Peng Zhang, Shicheng Zheng et al. (24 authors)*

🏢 Microsoft

Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about 2.5times. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at 1024^2 resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

▲ 72 • 💬 2 • ⭐ 697 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2607.19064) • [💻 code](https://github.com/microsoft/Mage) • [🔗 project](https://microsoft.github.io/Mage/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 177 • 💬 2 • ⭐ 75,878 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning](https://huggingface.co/papers/2607.21653)**

*Jian Hu, Huiying Li, Hao Zhang et al. (11 authors)*

🏢 NVIDIA

Agentic reinforcement learning research is constant algorithm modification, new estimators, new pipeline stages, new rollout schemes, and in mainstream frameworks each change threads through layers of trainer, distributed backend, and rollout glue: the cost lands on the researcher at every iteration. Molt is a PyTorch-native training framework built to keep that cost small: a codebase compact and clean enough for a researcher to hold in their head, and for an AI coding assistant to read and reason about in its entirety, so the algorithm flow can be traced and changed end to end. The agent is an ordinary program, and one asynchronous loop trains multimodal and mixture-of-experts policies while never training on a token it did not generate, consistent in tokens, policy versions, and model semantics. Leanness does not cost performance: under a matched, fully asynchronous protocol, Molt is statistically comparable to a state-of-the-art Megatron-based stack. Molt is open source and provides recipes and containers at https://github.com/NVIDIA-NeMo/labs-molt.

▲ 22 • 💬 0 • ⭐ 647 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2607.21653) • [💻 code](https://github.com/NVIDIA-NeMo/labs-molt)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 64 • 💬 1 • ⭐ 86,094 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

---

## GitHub Repositories: "ai"

**[elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)**

autonomous red teaming platform; multi-agent offensive-security meta-harness

`TypeScript` `agents` `ai` `multi-agent` `offensive-security` `redteam`

⭐ 5.3k • 🔱 1.1k • 5h ago

---

**[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)**

Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI.

`TypeScript` `agent-tools` `ai-agents` `api-gateway` `automation` `cli`

⭐ 3.4k • 🔱 268 • 9h ago

---

**[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)**

Removes 20+ patterns of AI slop from any piece of writing.

`Python`

⭐ 3.0k • 🔱 233 • 23h ago

---

**[synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience)**

The open-source AI workbench for scientific research

`TypeScript` `agent` `ai` `ai-agent` `bun` `cli`

⭐ 2.9k • 🔱 403 • 7h ago

---

**[isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)**

把 Markdown 一键排成可直接粘进公众号编辑器的精致 HTML —— 6 套精选主题 + 主题生成器 + 双关卡校验。An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.

`HTML` `agent-skill` `ai-agent` `claude-code` `codex` `cursor`

⭐ 2.6k • 🔱 294 • 19d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 106 shot recipe cards, 161 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 2.2k • 🔱 199 • 15h ago

---

**[penecho/penecho](https://github.com/penecho/penecho)**

Think with AI beyond the chat box. A shared canvas for handwriting, equations, diagrams, and spatial reasoning.

`JavaScript` `ai` `canvas` `claude` `codex` `education`

⭐ 1.7k • 🔱 196 • 14h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 1.7k • 🔱 181 • 1d ago

---

**[MIgHTy-alIeN/MEV-Arbitrage-Bot](https://github.com/MIgHTy-alIeN/MEV-Arbitrage-Bot)**

An arbitrage bot is a smart contract connected to an external automation script that controls its operation.

`Solidity` `ai` `aitradingbot` `bot` `btc` `claude`

⭐ 1.5k • 🔱 1.1k • 1h ago

---

**[buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes)**

`MDX` `ai-agent` `learning-notes` `pi-agent` `python` `tutorial`

⭐ 1.3k • 🔱 97 • 6d ago

---

---

*Generated by PeekDeck - A glance is all you need*

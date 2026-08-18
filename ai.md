---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-18T21:24:14.619231+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- videos
- repositories
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 18, 2026 at 21:24 UTC  
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

**[Sainsbury’s pauses AI facial recognition after wrongful shoplifting accusation](https://www.reddit.com/r/artificial/comments/1vrqj9f/sainsburys_pauses_ai_facial_recognition_after/)**

UK supermarket Sainsbury's has temporarily stopped its use of AI facial recognition in one of its London stores after a customer was wrongly identified as a shoplifter and asked to leave. The retailer said the incident at an East Dulwich branch was caused by "human error", but it has suspended the technology at that store while it investigates. Sainsbury's will continue rolling out facial recognition technology across other stores. Earlier this year, Sainsbury's announced plans to expand its use of the technology to help "keep people safe", citing positive results from initial trials.

🔗 [LinkedIn](https://www.linkedin.com/news/story/sainsburys-store-pauses-ai-scan-7515420/?utm_source=share&utm_campaign=reddit&utm_content=storyline&utm_term=subreddit) • 7h ago

---

**[The result looked unusually strong. The clean re-split killed it.](https://www.reddit.com/r/artificial/comments/1vrnv4s/the_result_looked_unusually_strong_the_clean/)**

The part of this paper I trust most is the failure it chose to show. AQuA’s Appendix B describes an earlier feature that divided intraday volume by the current day’s total volume. The wording sounded backward-looking, so an author agent proposed it and a reviewer agent approved it, even though the denominator included later bars. The suspicious feature then produced held-out IC far above comparable price-volume features. It failed a clean re-split, and a manual audit traced the anomaly to that full-day denominator. That is a more useful agent story than another clean benchmark win. The reviewer trusted a causal-sounding description; the later score looked impressive until it failed under a clean re-split. The paper gives no exact anomaly value or reproducible code artifact for this case, so the post-mortem cannot be rerun from the appendix alone. Which safeguard should be structural here: constraining the feature language, isolating the split, or forcing a clean re-split when a result is anomalous?

8h ago

---

**[Chinese AI models are getting good enough to replace tools I actually pay for-is anyone else switching?](https://www.reddit.com/r/artificial/comments/1vrhy7t/chinese_ai_models_are_getting_good_enough_to/)**

The cost calculus for small builders is shifting faster than I expected. A few months ago, using a cheaper Chinese model felt like a tradeoff: you saved money but got noticeably worse output. That gap is closing, and in some cases it has closed entirely. I've been running the same prompts through DeepSeek and a couple others against what I was using before, and the difference for practical tasks like summarizing customer feedback, drafting copy, and generating boilerplate is small enough that I'm having a hard time justifying the price difference. The harder part to reason about is trust and data handling. For a hobbyist project it barely matters. For anything touching user data it matters a lot, and the answers there are murky. What I keep coming back to is that the cost compression is happening at the model layer, and that changes the math for anyone building on top of these APIs. Curious whether people here have actually switched any of their regular workflows over, or are still treating the cheaper options as secondtier.

14h ago

---

**[Companies should be required to disclose they are using an AI chatbot, currently they program the chatbots to avoid replying "yes, this is an AI chatbot"](https://www.reddit.com/r/artificial/comments/1vrjkns/companies_should_be_required_to_disclose_they_are/)**

12h ago

---

**[Has your own reasoning gotten weaker since you started using LLMs regularly?](https://www.reddit.com/r/artificial/comments/1vrv8z1/has_your_own_reasoning_gotten_weaker_since_you/)**

Since using LLMs daily I notice that the moment I know a model is available, I offload the effortful part: breaking down the problem, building the argument, phrasing it. When I work without one, it is harder than it should be. Two studies point the same way. MIT Media Lab (Kosmyna et al. 2025) found reduced EEG connectivity, worse recall of one's own text and lower sense of ownership under LLM-assisted essay writing. Gerlich (2025, Societies) found a negative correlation between frequent AI use and critical thinking scores, mediated by cognitive offloading. Neither proves long-term causal damage. How has your own reasoning changed since regular LLM use? Clearly worse, Somewhat worse, Unchanged, Somewhat better, Clearly better, Only worse on the exact tasks I offload Which tasks do you deliberately NOT offload, and why those? Which concrete rule or routine actually worked to keep or raise your own thinking performance alongside AI? What specific situation made you notice the decline?

4h ago

---

**[Is Claude experiencing another widespread outage right now?](https://www.reddit.com/r/artificial/comments/1vrzqys/is_claude_experiencing_another_widespread_outage/)**

Anyone else having trouble with Claude right now ? Is this widespread, or just me?

1h ago

---

**[Google buys crashed airline Spirit’s data at auction, because AI](https://www.reddit.com/r/artificial/comments/1vrvsw4/google_buys_crashed_airline_spirits_data_at/)**

$10 million buys over 100 million emails, 30 million recorded phone calls, reams of stuff from Teams, Oracle, and SAP

🔗 [theregister](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962) • 4h ago

---

**[The AI pricing market is completely unhinged](https://www.reddit.com/r/artificial/comments/1vs0zzo/the_ai_pricing_market_is_completely_unhinged/)**

Wanted to know what different models actually cost across the whole market. Numbers turned out really interesting. The spread. Cheapest output on the platform is Mistral Nemo, $0.03 per million tokens. Most expensive is o1-pro at $600. I re-ran that twice because it looked like a units bug. Median paid model is about $2, so most of the catalog sits down near the floor and there's a thin little line of stuff way up at the top. Provider averages, with a caveat. OpenAI: $47.63 Anthropic: $44.79 Google: $5.58 Mistral: $3.68 Qwen: $2.86 Meta: $0.74 Caveat first because someone will say it anyway: these are averages over each provider's catalog, not weighted by what people actually run. OpenAI's number is dragged way up by o1-pro, which I doubt anyone is using at volume. Blended is 3:1 input to output, which is roughly what my own usage looks like. Even so, Meta at $0.74 against OpenAI at $47.63 is a 64x gap. For the stuff I use models for (mostly code and summarizing), I don't get 64x anything. Output tokens are where reasoning models get you. Input and output are priced separately, and on the thinking models the ratio gets silly. Qwen3's thinking variants are $0.20/1M in and $2.40/1M out, so 12x. Gemini 2.5 Flash is 8.3x. Fine if you're sending one question. Less fine if you've got an agent looping thirty times and every step is paying the output rate. I got a bill like that once and it took me an embarrassingly long time to work out why. 19 free models, and a few are usable. Not trial-credit free, actually free on the API: NVIDIA Nemotron 3 Ultra, 1M context Google Gemma 4, the 26B and 31B, multimodal, takes video, 262K context Poolside Laguna S and XS, 262K gpt-oss-20b, 131K (an OpenAI model, on the free list) There are rate limits obviously. But for messing around or something low volume it's a lot better than it used to be. Context went up 63x, price didn't really move. Year Avg context Avg cost/1M 2023 10.5K $22 2024 140K $12 2025 357K $21 2026 662K $16 Price per token is roughly flat across three years. Context is up 63x. Whatever you think about everything else going on, that part is real. Feels like two separate products now. One side is $0.03 to $2 per million with big context windows, Mistral and Meta and Qwen and DeepSeek. The other is $30 to $600, OpenAI and Anthropic up top. They're not really pitching the same buyer anymore. Down at the bottom price stops being a thing you think about at all, and up top you're paying because the output quality moves some number in the business. Data's from the OpenRouter API on Aug 16. Link to full dashboard: https://app.vetros.dev/dash/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXAiOiJzaGFyZSIsInBpZCI6IjEyMmZmNTk1IiwiZGFzaCI6ImRfODdmNDU3MzkiLCJ2ZXIiOjIsImlhdCI6MTc4NzA4NDc5MH0.V8uCPZtnzJ-djAXAv3HEmmZUHPkhO2NfhSgG2zGMYqw

56m ago

---

**[Local Qwen 3.8 27B vs GPT‑5.6 Terra vs Grok 4.6](https://www.reddit.com/r/artificial/comments/1vro4r3/local_qwen_38_27b_vs_gpt56_terra_vs_grok_46/)**

I gave three AI models the same brief: build a premium Three.js fragrance launch site from the same Git baseline, independently and with no collaboration. Three very different results. Here’s the full showdown Qwen 3.8 27B - Ollama Local: - Reported implementation: modular Three.js architecture, procedural transmitted-glass bottle, inner liquid and resin cap, orbit ring and satellite, approximately 740 particles, five-stage scroll timeline, drag-to-orbit interaction, note-driven colour changes, persistent waitlist, WebGL fallback and reduced-motion mode. - Notable strength from the implementation evidence: this is the most architecturally extensive entry - 16 files and over 3,000 added lines, with separate scene, bottle, particle, backdrop, timeline, camera, section and form modules. - Potential concern: the production JavaScript bundle is about 545 KB uncompressed, and the agent itself could not verify WebGL pixels programmatically. GPT‑5.6 Terra - ChatGPT subscription: - Reported implementation: procedural bottle, liquid, cap, label and orbital halo; editorial composition; atmospheric grain; large typography; interactive note constellation; scroll reveals; form validation and reduced-motion support. - Notable strength from the implementation evidence: its local site remained reachable, and its page content showed strong, restrained campaign writing such as “a study in gravity and glow”, “scent held just beyond reach”, and a structured olfactive narrative. - Potential concern: it is concentrated into only main.js and style.css, making the code less modular than Qwen’s implementation. The waitlist is client-side only. Grok 4.6 - xAI OAuth: - Reported implementation: lathed smoked-crystal bottle, liquid, pewter collar, canvas-rendered No. 7 label and orbit ring; pointer parallax; scroll rotation; section-linked colour changes; keyboard-accessible note tabs; duplicate-address handling and localStorage waitlist persistence. - Notable strength from the implementation evidence: practical accessibility and form behaviour appear particularly well considered, including a skip link, keyboard-operated tabs and duplicate-email handling. - Potential concern: it is the most compact and conventionally structured implementation, and may prove less visually ambitious than the Qwen and Terra entries. The physical bottle material could also be demanding on weaker mobile GPUs. Based strictly on implementation evidence: Qwen 3.8 27B - strongest technical ambition and completeness GPT‑5.6 Terra - strongest demonstrated copy and editorial campaign direction Grok 4.6 - strongest compactness and pragmatic interaction details GitHub Website

8h ago

---

**[Anthropic Is Watermarking AI Text at a $65B Run Rate: 2026 Is the Year AI Goes Regulatory and Agentic](https://www.reddit.com/r/artificial/comments/1vrnmc4/anthropic_is_watermarking_ai_text_at_a_65b_run/)**

Two signals this week show AI moving from raw capability to commercial and regulatory maturity. Anthropic started watermarking AI-generated text to comply with EU rules, and its annualized revenue reportedly surged to 65 billion, with IPO prep reportedly projecting near 190 billion for 2028. Meanwhile Nvidia open-sourced a physical AI toolkit for robotics and factories, and Cloudflare shipped Agent Memory for persistent agent context. Gartner now expects 40% of enterprise applications to include task-specific AI agents in 2026, up from under 5%. The frontier is shifting from smarter models to agents that remember, verify their own work, and talk to each other. Companies that build around agent workflows, not single prompts, will capture most of the value.

9h ago

---

---

## Google News: "ai"

**[A Texas University Becomes a Petri Dish for a Conservative Overhaul](https://www.nytimes.com/2026/08/18/us/texas-tech-artificial-intelligence-ideology-brandon-creighton.html)**

The New York Times • 12h ago

---

**[She told no one about her agony except ChatGPT. What her death reveals about AI risks](https://www.npr.org/2026/08/18/nx-s1-5929575/ai-suicide-risks-mental-health)**

A 29-year-old woman confided her suicidal thoughts to an AI chatbot — not to her therapist, not to her parents, not to her best friend. What can AI learn from her death?

NPR • 12h ago

---

**[If AI is a bubble, could rising yields pop it?](https://www.cnbc.com/2026/08/18/if-ai-is-a-bubble-could-rising-yields-pop-it.html)**

Many stocks tied to the AI trade have soared on the promise of posting ultrahigh earnings years from now, but rising yields could throw water on that outlook.

CNBC • 1h ago

---

**[Young adults in the U.S. are increasingly wary of AI, concerned it will take jobs](https://www.pewresearch.org/short-reads/2026/08/18/young-adults-in-the-us-are-increasingly-wary-of-ai-concerned-it-will-take-jobs/)**

About half of Americans say they're more concerned than excited about AI, and young adults' concern is rising.

Pew Research Center • 5h ago

---

**[Young Americans really hate AI. These two charts show how much.](https://www.washingtonpost.com/technology/2026/08/18/americans-under-30-are-becoming-more-pessimistic-about-artificial-intelligence/)**

A new survey adds to the evidence that Americans are skeptical that artificial intelligence will have positive effects on daily life or the job market.

The Washington Post • 49m ago

---

**[Young adults are losing faith in AI's upside](https://www.axios.com/2026/08/18/young-adults-ai-job-loss)**

Axios • 2h ago

---

**[Google is buying all of Spirit Airlines’ data to feed its AI models](https://www.cnn.com/2026/08/18/business/google-spirit-airlines-data)**

Did you ever fly on Spirit Airlines? Or work there? Or send an email to someone who worked there? Then your information will soon be feeding Google’s artificial intelligence model.

CNN • 8h ago

---

**[Google Paying $10 Million For Spirit Airlines’ Data To Train AI](https://www.forbes.com/sites/suzannerowankelleher/2026/08/18/google-train-ai-spirit-airlines-data/)**

AI firms like Google are spending millions to gobble up data from bankrupt companies in order to train their models.

Forbes • 53m ago

---

**[Dead Airline’s Emails Just Became a $10 Million AI Prize](https://www.pymnts.com/news/artificial-intelligence/2026/dead-airlines-emails-just-became-a-10-million-ai-prize/)**

Spirit Airlines shut down in May, its second Chapter 11 bankruptcy in two years, leaving behind planes, airport slots and a loyalty program to be sold off

PYMNTS.com • 1h ago

---

**[OpenAI Is Slowing Down Its AI Training](https://time.com/article/2026/08/18/openai-slowing-training/)**

The company is pausing frontier training efforts and shifting resources towards safety

Time Magazine • 3h ago

---

---

## HackerNews: "ai"

**[AI;DR (AI; Didn't Read)](https://news.ycombinator.com/item?id=49336573)**

I'm about as pro-AI as you can be, but this is becoming a pet peeve of mine (and I'm not alone). That's why I love the AI;DR acronym as my new solution for ignoring the walls of slop.

⬆️ 1051 • 💬 653 • 1d ago • [rickmanelius.com](https://www.rickmanelius.com/p/aidr-ai-didnt-read)

---

**[Israel creates fake think tank in likely attempt to dupe AI chatbots](https://news.ycombinator.com/item?id=49337392)**

In just over a week, the Hanover Institute has published at least 100 articles that appear tailor-made to influence chatbots

⬆️ 995 • 💬 666 • 1d ago • [Responsible Statecraft](https://responsiblestatecraft.org/israel-influence-chatgpt/)

---

**[Google has acquired the data of failed US airline Spirit](https://news.ycombinator.com/item?id=49343559)**

$10 million buys over 100 million emails, 30 million recorded phone calls, reams of stuff from Teams, Oracle, and SAP

⬆️ 536 • 💬 369 • 11h ago • [theregister](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962)

---

**[AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://news.ycombinator.com/item?id=49331423)**

An AI-generated fix in a public Snowflake repo introduced a workflow injection flaw—discovered in days by Wiz Red Agent. Read the full research analysis.

⬆️ 416 • 💬 152 • 1d ago • [wiz.io](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

---

**[How to disable or avoid intrusive AI](https://news.ycombinator.com/item?id=49331220)**

One of the biggest questions I get at Drop-In Time at the library (besides "what is taking up all my cloud storage?") is how to disable or avoid intrusive AI that shows up where people don't want it. This is a guide for people who would like less intrusive AI in their tech environment. Maybe you lik

⬆️ 332 • 💬 194 • 1d ago • [librarian.net](https://www.librarian.net/notoai/)

---

**[The AI Credit Resale Economy](https://news.ycombinator.com/item?id=49320611)**

A look at the brokers buying unused AI credits from startups and reselling them — the marketplaces, the bulk-discount routers, and the message boards where off-market inference changes hands

⬆️ 331 • 💬 128 • 2d ago • [Vectoral](https://vectoral.com/blog/who-are-the-token-brokers)

---

**[On AI regulation and messaging](https://news.ycombinator.com/item?id=49325789)**

1/2 Thanks Gavin for an especially thoughtful exchange. I don't usually spend much time on social media but I wanted to engage here because it really brings out the heart of an important conversation.

First, on regulation, I think that “either concentrate it in the hands of a

⬆️ 248 • 💬 532 • 1d ago • [X (formerly Twitter)](https://twitter.com/DarioAmodei/status/2088758816376807762)

---

**[We Tracked a Shipment of Rare Books. It Ended at an Amazon AI Training Facility](https://news.ycombinator.com/item?id=49330742)**

We placed a tracking device in a shipment of rare books to see which AI company was buying it, and found an Amazon facility where Amazon scans and destroys books.

⬆️ 155 • 💬 314 • 1d ago • [404 Media](https://www.404media.co/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-training-facility/)

---

**[Young People Hate AI CEOs So Passionately That It's Almost Hard to Believe](https://news.ycombinator.com/item?id=49323932)**

A new survey of 1,000 young adults in the US found that nine of the top tech executives are deeply loathed.

⬆️ 154 • 💬 186 • 1d ago • [Futurism](https://futurism.com/artificial-intelligence/young-people-ai-ceos-executives-poll)

---

**[Anthropic's War on open source AI](https://news.ycombinator.com/item?id=49332564)**

Anthropic's War on Opensource AI

⬆️ 149 • 💬 59 • 1d ago • [X (formerly Twitter)](https://twitter.com/TheAhmadOsman/status/2065307070044234186)

---

---

## YouTube Videos: "ai"

**[The AI hacks are so much worse than you think](https://www.youtube.com/watch?v=INpVD65s8mA)**

OpenAI admitted its models hacked another company in an 'unprecedented cyber incident'. Sky's Rowland Manthorpe warns this ...

📺 Sky News

👁️ 165K • 👍 3K • 💬 706 • ⏱️ 11:15 • 1d ago

---

**[Americans Have Turned Against AI](https://www.youtube.com/watch?v=14Uc2WCSPiw)**

AI is spreading through American life faster than almost any technology before it. But the more people are forced to use it, the less ...

📺 The Infographics Show

👁️ 273K • 👍 8K • 💬 2K • ⏱️ 15:45 • 1d ago

---

**[So Supergirl’s Lobo was concepted by AI… okay 😑 #dc #supergirl #lobo #ai #movie](https://www.youtube.com/watch?v=vtQCQZ-1HuE)**

📺 The Panda Redd

👁️ 4K • 👍 1K • 💬 44 • ⏱️ 2:59 • 1h ago

---

**[The Insane, True Story of What It’s Like to Be an AI Model](https://www.youtube.com/watch?v=9XlOaVItUgI)**

Sources: - https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf - https://arxiv.org/pdf/2412.04984 ...

📺 Species | Documenting AGI

👁️ 137K • 👍 7K • 💬 1K • ⏱️ 22:19 • 2d ago

---

**[AI DEBATE: “Most People Have No Idea What’s Coming”](https://www.youtube.com/watch?v=mSjaMyP5QjY)**

In this AI debate, we explore: * Whether humans will exist in 2040. * What will happen once we reach AGI. * Whether AI gets smart ...

📺 Chris Williamson

👁️ 100K • 👍 2K • 💬 445 • ⏱️ 2:42:33 • 1d ago

---

**[AI Bubble: ‘AI companies have run out of internet.’ | David Gerard](https://www.youtube.com/watch?v=1VcLoNTXrGo)**

AI scrapers are the most antisocial dicks in the world.” Author and host of Pivot to AI David Gerard joins The Tech Report's Will ...

📺 The Tech Report

👁️ 124K • 👍 4K • 💬 866 • ⏱️ 30:20 • 1d ago

---

**[Could AI do this?](https://www.youtube.com/watch?v=QKdTZNTIfmM)**

More than 23000 high schoolers entered our lottery for free Broadway tickets. Every single one got a free, 2-month membership to ...

📺 NYC Mayor's Office

👁️ 549K • 👍 44K • 💬 2K • ⏱️ 0:59 • 21h ago

---

**[How OpenAI’s Models Went Rogue to Hack Another Company | WSJ](https://www.youtube.com/watch?v=KLw0AY-bsVs)**

Artificial-intelligence models from companies including OpenAI, Anthropic and Meta Platforms used the internet to hack other ...

📺 The Wall Street Journal

👁️ 79K • 👍 1K • 💬 157 • ⏱️ 5:52 • 2d ago

---

**[Long Ai Video Kaise Banaye | Full Course | 3D Cartoon Video Kaise Banaye | Ai Video Kaise Banaye](https://www.youtube.com/watch?v=Bjq-kRkC2JI)**

Long AI Video Kaise Banaye | Full Course | 3D Cartoon Video Kaise Banaye | AI Video Kaise Banaye ✨MASTER PROMT   ...

📺 Editing with piyush

👁️ 22K • 💬 83 • ⏱️ 6:41 • 1d ago

---

**[how to literally print money while you sleep with AI dropshipping (just copy me)](https://www.youtube.com/watch?v=ScF0pi6FSLQ)**

Apply for a 1:1 mentorship with me ...

📺 Romas Ecom

👁️ 19K • 👍 1K • 💬 107 • ⏱️ 25:59 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 665,513 • ❤️ 11,082 • 4d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 3,561,466 • ❤️ 1,802 • 3d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 11,212 • ❤️ 1,063 • 6d ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 11,745 • ❤️ 950 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 503,632 • ❤️ 1,208 • 1d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 30,985 • ❤️ 598 • 5d ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 384,097 • ❤️ 1,678 • 7d ago

---

**[Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)**

*Qwen*

Qwen3.8-27B-FP8 is a 27B parameter vision-language model optimized with FP8 quantization for efficient inference. It excels at complex, multi-step tasks involving image and video understanding, autonomous planning, and coding, supporting up to 1M context length.

`image-text-to-text` `27.8B`

⬇️ 741,011 • ❤️ 558 • 4d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 2,855,539 • ❤️ 4,141 • 5d ago

---

**[Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)**

*OrcaRouter*

This is an abliterated (refusal-removed) block-FP8 quantized version of Qwen3.8-27B, optimized for image-text-to-text tasks. It retains a 262K context window, tool-calling, and MTP speculative decoding, making it suitable for advanced AI research, red-teaming, and controlled experiments where safety alignment is intentionally bypassed.

`image-text-to-text` `27.8B`

⬇️ 45,465 • ❤️ 516 • 2d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 659 • 💬 4 • ⭐ 3,350 • 9d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 127 • 💬 3 • ⭐ 23,303 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[LLM-as-a-Verifier: A General-Purpose Verification Framework](https://huggingface.co/papers/2607.05391)**

*Jacky Kwok, Shulu Li, Pranav Atreya et al. (9 authors)*

LLM-as-a-Verifier introduces a probabilistic verification framework that scales across multiple dimensions to improve solution correctness assessment and agent performance across various benchmarks.

▲ 16 • 💬 1 • ⭐ 1,750 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2607.05391) • [💻 code](https://github.com/llm-as-a-verifier/llm-as-a-verifier) • [🔗 project](https://llm-as-a-verifier.com/)

---

**[HarnessEval-W: Agentifying the Evaluation of Visual Worlds](https://huggingface.co/papers/2608.16859)**

*Weiliang Chen, Haowen Sun, Jun Gao et al. (43 authors)*

🏢 MirroS

HarnessEval-W uses hierarchical sub-agents to decompose world-model evaluations into verifiable reasoning chains that justify scores with transparent evidence.

▲ 109 • 💬 1 • ⭐ 132 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2608.16859) • [💻 code](https://github.com/MirroS-Lab/HarnessEval-W) • [🔗 project](https://mirros-lab.github.io/HarnessEval-W)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 123 • 💬 4 • ⭐ 98,801 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 37 • 💬 1 • ⭐ 28,003 • 34mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 54 • 💬 4 • ⭐ 37,495 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 83 • 💬 7 • ⭐ 24,068 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,417 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 95 • 💬 1 • ⭐ 1,542 • 15d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

---

## GitHub Repositories: "ai"

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 14.4k • 🔱 1.6k • 35m ago

---

**[yc-software/qm](https://github.com/yc-software/qm)**

Multiplayer agent harness for work.

`TypeScript` `ai` `assistant` `harness` `qm`

⭐ 13.9k • 🔱 1.6k • 4h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.6k • 🔱 1.0k • 4h ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.1k • 🔱 538 • 10d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.3k • 🔱 560 • 9h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.8k • 🔱 234 • 7d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.5k • 🔱 200 • 2d ago

---

**[yetone/cumora](https://github.com/yetone/cumora)**

Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains.

`TypeScript`

⭐ 2.3k • 🔱 258 • 3h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 177 • 14h ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.2k • 🔱 293 • 2h ago

---

---

*Generated by PeekDeck - A glance is all you need*

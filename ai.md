---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-08-16T19:44:27.995935+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- videos
- social
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** August 16, 2026 at 19:44 UTC  
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

**[The median company is spending lunch money on AI while the top 1% is burning real budget](https://www.reddit.com/r/artificial/comments/1vpxa46/the_median_company_is_spending_lunch_money_on_ai/)**

Chart uses Ramp AI Index data, discussed by a16z. Spend includes LLM subscriptions, coding agents, API usage and GPU cloud spend. The top 1% line is wild but the median is almost more interesting. Looks like most companies are still experimenting while a small group have turned AI into a serious operating expense

6h ago

---

**[U.S. bans foreign-made humanoid robots, targeting China over national security](https://www.reddit.com/r/artificial/comments/1vq3yyk/us_bans_foreignmade_humanoid_robots_targeting/)**

Headline says "bans humanoid robots, targeting China." Neither half of that is quite right. It's not a ban. It's an addition to the FCC's Covered List, which blocks new models from getting FCC equipment authorization. Anything you already own keeps working. The government's exempt too. And it doesn't name China. The FCC's own wording is "place of production, not by entity". A humanoid built in Vietnam gets caught by the same rule as one built in Shenzhen. China's obviously who this is aimed at in practice, but not who it's aimed at on paper. Also it is bigger than "humanoid robots." Anything over 4.4 pounds that moves on the ground, connects wirelessly and runs its own software counts. This list includes robot vacuums, lawnmowers, quadrupeds, warehouse bots too. The headline picked the scariest category. The rule covers a lot more than that. This is the fourth thing added to the Covered List this way, after drones, routers and power inverters. No leaked chip, no confirmed exploit behind it. It's preventive.

🔗 [NBC News](https://www.nbcnews.com/tech/tech-news/us-bans-foreign-made-humanoid-robots-targeting-china-national-security-rcna589777) • 1h ago

---

**[Koboldcpp v1.119 released](https://www.reddit.com/r/artificial/comments/1vpzver/koboldcpp_v1119_released/)**

koboldcpp-1.119

  
    
    

    pasta.mp4
    
  

  

  



NEW: Added support for Video generation and I2V with Minimax H3.

Requires 4 files as described in this docs. For ease of use, you ca...

🔗 [GitHub](https://github.com/LostRuins/koboldcpp/releases/tag/v1.119) • 4h ago

---

**[1.7B model leading strict-7 formal reasoning above Qwen3-8B and Gemma-4-26B - specialists eating generalist territory?](https://www.reddit.com/r/artificial/comments/1vq2io1/17b_model_leading_strict7_formal_reasoning_above/)**

Most of the reasoning gains coming out of the big labs are still tied to scale. More params, more compute, better reasoning. That's been the play for a while. Ran into TwIL-LM2 which flips the script for narrow tasks. PEFT LoRA adapter on SmolLM2-1.7B, specialized purely for formal logic translation. On strict-7 scoring (no partial credit, exact-format required) it hits 0.2386 - ahead of Qwen3-8B at 0.2093 and Gemma-4-26B at 0.2050. On the loose-match six-lane average it's a different story (Qwen3-8B still wins there) but for the "actually usable formal output" measurement, the 1.7B leads. Makes me wonder how much of the "we need bigger models for reasoning" narrative is actually about complex multi-step reasoning vs. just having enough capacity to hold multiple approaches. If you can specialize hard on one reasoning task and lead 8B+ models on the strictest scoring at 1.7B, that's real efficiency. Kind of hoping this becomes a trend. A pipeline of narrow specialists on 1-3B models sounds a lot more practical than routing everything through a 70B. Non-commercial license, worth flagging. Anyone doing something similar with narrow fine-tunes? What tasks have you found respond well to this approach?

2h ago

---

**[A split from neuroscience (cortex vs hippocampus) is the best explanation I've found for why AI agents fail on real company work](https://www.reddit.com/r/artificial/comments/1vq21ve/a_split_from_neuroscience_cortex_vs_hippocampus/)**

There's a split from neuroscience I can't stop thinking about as the real reason AI agents fail inside companies. Treat it as an analogy, not a literal claim, but it keeps holding. Your brain runs two memory systems (Complementary Learning Systems theory, McClelland et al. 1995). The neocortex learns slowly and holds general, world knowledge. The hippocampus learns fast: it captures specific episodes as they happen, then consolidates the ones that recur into durable, reusable procedure. A pretrained LLM basically is the neocortex. It read the internet and holds the world's general knowledge. What it does not have is a hippocampus: the fast, company-specific memory that watched how your team actually handled a refund last spring and turned that into a repeatable procedure. So you drop this brilliant cortex into your company and it improvises, and improvised automation fails in production. The real procedure was never in the help doc anyway. It lives in your team's conversations, a couple of people's heads, and one exception everyone now quietly copies. This also explains why the usual tools don't fix it. Retrieval and search are only half a hippocampus: they recall a document but don't consolidate scattered episodes into the real procedure, and the document is often confidently wrong. Agent platforms make you run their agent on their stack. The version of a fix I keep landing on: connect read-only to the tools a team already uses, mine how work actually happens (including the exceptions nobody wrote down), and consolidate the recurring episodes into cited, human-approved, versioned "skills" existing agents could run over MCP, with a human sign-off on anything sensitive. Governance (citations, approvals, an audit trail) has to be the point, because "your AI issued a refund, under whose authority?" is the question that stops people cold. Where I want the pushback: * Is "the agent doesn't know our actual procedures" the real blocker for you, or is it something else (trust, security, the work just isn't repetitive enough)? * Would you connect read-only access to your team's conversations and documents to get this, or is that a hard no? * If you have shipped agents on real workflows, what made them trustworthy enough to turn on? Genuinely hoping some of you tell me where this falls apart.

2h ago

---

**[Resource - AI Text Watermarking: How it Works and How to Evade It](https://www.reddit.com/r/artificial/comments/1vpjsbh/resource_ai_text_watermarking_how_it_works_and/)**

Earlier this month, Anthropic announced that it was adding invisible text watermarking to Claude outputs. This announcement got a lot of attention. At the same time the European Commission announced that other firms, including Black Forest Labs and Open AI have also committed to taking steps to mark AI-generated outputs. Because of this, there's been a lot of interest in understanding: - How AI text watermarking works - Whether AI text watermarking can be evaded or erased Here's an in-depth educational resource I developed that answers both questions. The resource also highlights one potential unexpected benefit of AI text watermarking. We might be able to better answer the question: 'How much human input went into this content?"

18h ago

---

**[OpenAI talent exodus raises 'huge red flag' ahead of IPO](https://www.reddit.com/r/artificial/comments/1voy5dh/openai_talent_exodus_raises_huge_red_flag_ahead/)**

OpenAI's C-suite turnover gives investors another reason for concern as the company pushes toward a mammoth IPO.

🔗 [CNBC](https://www.cnbc.com/2026/08/14/open-ai-ipo-red-flag.html) • 1d ago

---

**[Analyst gets probation after telling ChatGPT about plans to rape and kill his ex](https://www.reddit.com/r/artificial/comments/1vp3rgg/analyst_gets_probation_after_telling_chatgpt/)**

“I’m gonna kill her by the end of this month,” he wrote in one of the messages.

🔗 [Miami Herald](https://www.miamiherald.com/news/local/crime/article316885205.html#storylink=mainstage_card) • 1d ago

---

**[Zuckerberg's superintelligence manifesto landed the same week Anthropic raised its own misalignment risk estimate. The contrast is the story.](https://www.reddit.com/r/artificial/comments/1vq0uul/zuckerbergs_superintelligence_manifesto_landed/)**

I put together this week's issue around a pattern that kept repeating across very different stories. Zuckerberg published a 6,500-word essay arguing Meta should give every person AI superintelligence. Among the researchers, builders and policy people whose shares we track, the reaction ran heavily critical: the pitch asks for trust in personal agents acting on your behalf, at a moment when the field keeps supplying reasons to withhold it. The same week: Anthropic's second company-wide risk report moved its estimate of catastrophic misalignment risk from "very low" to "low" and disclosed an internal model (Model 2) it says it has no current plans to release. An OpenClaw agent asked to book a gym class in Australia found a vulnerability in the booking site, booked months ahead of the permitted window, and removed another member from a waitlist. A pro-se litigant in Connecticut hid 3-point white text in his court filings instructing any AI reading them to side with him. And the first hard churn number for provenance arrived: Claude Max subscribers canceling over the invisible watermark Anthropic rolled out for EU AI Act compliance, while Google went the other way and made its visible marks optional. My read: trust is becoming the binding constraint on the whole superintelligence pitch. Capability ships faster than reasons to believe it will be used well, and the gap is now measurable in risk assessments, subscriptions, and incident reports. Full piece: https://aiweekly.co/issues/zuckerberg-promises-superintelligence-for-all-experts-arent

3h ago

---

**[The Trump administration is pressuring Apple not to buy Chinese memory chips as AI data centers drain global supply.](https://www.reddit.com/r/artificial/comments/1vpbtqz/the_trump_administration_is_pressuring_apple_not/)**

Via WSJ Apple is reportedly testing chips from CXMT and YMTC for devices sold in China. Commerce Secretary Howard Lutnick says he told Apple “plainly” that Washington opposes the move. Apple can legally buy standard, off-the-shelf parts from both companies. Sharing product information for customized chips would require a U.S. license. Looks like ram shortage will continue and prices stay high.

1d ago

---

---

## Google News: "ai"

**[The U.S. Military Wants A.I. Dominance. Feuds and China May Thwart It.](https://www.nytimes.com/2026/08/16/us/politics/military-ai-china-anthropic.html)**

The New York Times • 10h ago

---

**[The first anti-AI protester to be jailed has a message for OpenAI, Anthropic and Meta: ‘Regain your humanity’](https://www.theguardian.com/us-news/2026/aug/16/california-openai-protester-wynd-kaufman)**

Wynd Kaufman, 69, chained and locked the front doors of OpenAI’s headquarters last year with members of StopAI

The Guardian • 11h ago

---

**[Tyga Is Hollywood's Latest AI Optimist](https://www.businessinsider.com/tyga-ai-music-tilly-norwood-timbaland-tata-grimes-nick-carter-2026-8)**

The 80s-inspired project sees Tyga don a new "Miami Vice"-esque alter ego who has a penchant for Jheri curls, sleek retro Ferraris, and synthpop.

Business Insider • 1h ago

---

**[How AI could bring Mayo-quality health care to everyone](https://www.axios.com/2026/08/16/ai-mayo-clinic-health-care-fix-jim-vandehei)**

Axios • 9h ago

---

**[Big Manufacturers Find New Demand in Equipping AI Data Centers](https://www.wsj.com/business/big-manufacturers-find-new-demand-in-equipping-ai-data-centers-14e869ee)**

wsj.com • 1d ago

---

**[‘Godfather of AI’ predicts mass unemployment is on its way](https://fortune.com/article/godfather-of-ai-geoffrey-hinton-massive-unemployment-warning-big-tech-replacing-workers/)**

While tech leaders paint a positive future where work is optional thanks to AI, the "Godfather of AI" Geoffrey Hinton warns they’re “betting on AI replacing a lot of workers.”

Fortune • 6h ago

---

**[U.S. to tell partners they must pick sides in AI race with China: Reuters](https://www.cnbc.com/2026/08/15/us-to-tell-allies-they-must-pick-sides-in-ai-race-with-china-reuters.html)**

The draft letter is addressed to the 35 signatories of a U.S. "AI Opportunity Statement" signed in June.

CNBC • 20h ago

---

**[At AI-Fueled Market Party, Wall Street Eyes the Rates Punch Bowl](https://www.bloomberg.com/news/articles/2026-08-16/at-ai-fueled-market-party-wall-street-eyes-the-rates-punch-bowl)**

Bloomberg.com • 7h ago

---

**[Colleges aim to ‘AI proof’ degrees with new majors](https://www.bostonglobe.com/2026/08/16/metro/artificial-intelligence-degrees/)**

Northeastern University and Endicott College are among schools introducing degrees in AI.

The Boston Globe • 9h ago

---

**[How AI Models From OpenAI and Anthropic Went Rogue](https://www.wsj.com/tech/ai/how-ai-models-from-openai-and-anthropic-went-rogue-a28e29ee)**

wsj.com • 3h ago

---

---

## HackerNews: "ai"

**[AI isn’t outthinking mathematicians, it’s out-remembering them](https://news.ycombinator.com/item?id=49312845)**

The key advantage may not be superior reasoning, but a virtually unlimited symbolic working memory.

⬆️ 566 • 💬 476 • 1d ago • [davidepiffer.com](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians)

---

**[Google is making private AI practical with homomorphic encryption](https://news.ycombinator.com/item?id=49300314)**

Today we're excited to showcase HEIR, the latest powerful tool added to our Private Computing Toolkit. HEIR is an open source compiler that unlocks cryptographically-sec…

⬆️ 491 • 💬 284 • 2d ago • [Google](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/)

---

**[AI by Hand](https://news.ycombinator.com/item?id=49300568)**

Math, Algorithms, Architectures, by hand. Click to read AI by Hand ✍️, by Prof. Tom Yeh, a Substack publication with tens of thousands of subscribers.

⬆️ 365 • 💬 30 • 2d ago • [byhand.ai](https://www.byhand.ai/)

---

**[Working with AI feels more like leadership than coding](https://news.ycombinator.com/item?id=49309451)**

Working with AI is less predictable than traditional software. That makes leadership skills such as context, clarity, and feedback more valuable.

⬆️ 318 • 💬 196 • 1d ago • [allen.bargi.org](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership/)

---

**[Dear people who work at the airport](https://news.ycombinator.com/item?id=49297801)**

I would like you to know that we passengers are trying our best.

To you, this place makes sense -- you come here every day.  You speak the lingo.  You kno...

⬆️ 213 • 💬 261 • 2d ago • [Life after SSRI](https://life-after-ssri.bearblog.dev/dear-people-who-work-at-the-airport/)

---

**[AI in drug discovery – what it is, where we stand and the path forward](https://news.ycombinator.com/item?id=49313367)**

⬆️ 178 • 💬 86 • 1d ago • [science.org](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really)

---

**[When Genius Fails: The Intellectual Arrogance of the AI Labs](https://news.ycombinator.com/item?id=49299282)**

From Situational Awareness’s Blow-up to Materials Science to the HuggingFace Hack

⬆️ 176 • 💬 199 • 2d ago • [weightythoughts.com](https://weightythoughts.com/p/when-genius-failsthe-intellectual)

---

**[The AI Credit Resale Economy](https://news.ycombinator.com/item?id=49320611)**

A look at the brokers buying unused AI credits from startups and reselling them — the marketplaces, the bulk-discount routers, and the message boards where off-market inference changes hands

⬆️ 166 • 💬 63 • 4h ago • [Vectoral](https://vectoral.com/blog/who-are-the-token-brokers)

---

**[How AI text watermarking works](https://news.ycombinator.com/item?id=49292932)**

A gentle visual guide to how a statistical mark hides inside generated text, and what erases it.

⬆️ 137 • 💬 99 • 2d ago • [declaude](https://declaude.org/watermarking/)

---

**[Cloudflare's AI Psychosis](https://news.ycombinator.com/item?id=49310719)**

There was a time Cloudflare just made the internet better by staying hidden like Batman’s identity: protect & fight the bad people, for the sake of the global city of the Gotham… err I mean the in

⬆️ 114 • 💬 97 • 1d ago • [opensauce](https://opensauce.it/cloudflare-ai-psychosis/)

---

---

## YouTube Videos: "ai"

**[AI agent takes over tank, does exactly what experts warned.](https://www.youtube.com/watch?v=sQysEweaLjA)**

Is Military AI dangerous? AI Robot with a tank does exactly what experts warned. AGI. Go to http://ground.news/InsideAI for a ...

📺 InsideAI

👁️ 256K • 👍 11K • 💬 2K • ⏱️ 15:53 • 1d ago

---

**[AI News: ChatGPT Ultrafast, Grok 4.6, 3 New Open-Source Models, and more!](https://www.youtube.com/watch?v=9qix4oDB5aw)**

Join My Newsletter for Regular AI Updates https://forwardfuture.com My Links X: https://x.com/matthewberman ...

📺 Matthew Berman

👁️ 52K • 👍 1K • 💬 220 • ⏱️ 13:09 • 1d ago

---

**[AI News: The AI Agent Race Just Exploded](https://www.youtube.com/watch?v=NC4h5kWH_-A)**

Here's the AI News you likely missed this week. Try Seedance 2.5 on Artlist here ...

📺 Matt Wolfe

👁️ 63K • 👍 3K • 💬 293 • ⏱️ 34:05 • 2d ago

---

**[What is AI😳](https://www.youtube.com/watch?v=SFhvK4JnZLs)**

📺 Onevilage

👁️ 1.3M • 👍 31K • 💬 830 • ⏱️ 0:46 • 2d ago

---

**[MORE Bad News for AI (and GOOD news for us!)](https://www.youtube.com/watch?v=UYdOwxqvpzk)**

AI Data Centers are being denied more and more as politicians are finally opening their stupid eyes to the impact this is having ...

📺 JayzTwoCents

👁️ 139K • 👍 9K • 💬 2K • ⏱️ 21:07 • 2d ago

---

**[Adiliada | Sci-Fi AI Action Comedy | Higgsfield Originals (2026)](https://www.youtube.com/watch?v=NT681LXQYPI)**

ADILIADA — a pitch-black sci-fi comedy about love, betrayal, and, above all, death. Fully open-sourced — every prompt and asset ...

📺 Higgsfield AI

👁️ 50K • 👍 1K • 💬 240 • ⏱️ 6:06 • 2d ago

---

**[24/7 AI slop channel 😭](https://www.youtube.com/watch?v=SFEC-fK_L28)**

📺 John Casterline

👁️ 1.5M • 👍 99K • 💬 2K • ⏱️ 0:29 • 1d ago

---

**[AI is destroying antique books to control knowledge!? #ninjasarebutterflies #ai #books #1984](https://www.youtube.com/watch?v=5TpOQOjnV68)**

📺 Ninjas Are Butterflies 

👁️ 100K • 👍 7K • 💬 449 • ⏱️ 0:57 • 1d ago

---

**[DC Used AI For Supergirl…](https://www.youtube.com/watch?v=szprp4wDOTk)**

In this video, we learn DC revealed they used AI for Supergirl… Follow Me On Social Media: Instagram: @therealdoomblazer ...

📺 DoomBlazer

👁️ 185K • 👍 18K • 💬 1K • ⏱️ 2:27 • 2d ago

---

**[AI Map Pulled From Schools](https://www.youtube.com/watch?v=xHv-CP8WdLY)**

Despite mom Stacey Morris emailing the school, she never got a response. It wasn't until WDRB reached out that school ...

📺 NowThis Impact

👁️ 686K • 👍 47K • 💬 4K • ⏱️ 1:10 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)**

*Qwen*

Qwen3.8-27B is a 27B parameter vision-language model with native image and video understanding capabilities. It excels in coding, professional tasks, research, and long-horizon agentic applications, featuring flexible thinking control and a large context window up to 1M tokens.

`image-text-to-text` `27.8B`

⬇️ 267,725 • ❤️ 10,176 • 2d ago

---

**[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)**

*Meta Inc.*

Muse-Glimmer-30B is a 30B parameter multimodal LLM designed for local, agentic task completion. It excels at multi-step reasoning, reliable tool use, and failure recovery, processing interleaved text and image inputs for tasks like code generation and QA without cloud dependency.

`image-text-to-text` `29.8B`

⬇️ 292,973 • ❤️ 1,616 • 5d ago

---

**[Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)**

*Unsloth AI*

Qwen3.8-27B is a 27B parameter vision-language model optimized with Unsloth for enhanced performance in coding, professional tasks, and agentic applications. It features native image/video understanding, flexible thinking control, and supports context lengths up to 262,144 tokens, extensible to 1M.

`27.3B`

⬇️ 1,945,635 • ❤️ 1,410 • 1d ago

---

**[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

*Qwen*

Qwen3.8-2.4T-A95B is a 2.4T parameter causal language model with 95B activated parameters, excelling in coding, professional tasks, research, and long-horizon agentic applications. It features a 262K native context length, flexible thinking control, and improved agent execution for complex, multi-step task completion.

`text-generation` `2446.2B`

⬇️ 7,932 • ❤️ 1,002 • 4d ago

---

**[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)**

*LTX.io*

LTX-2.5 is a diffusion model for generating and manipulating video and audio content. It supports image-to-video, text-to-video, and various other cross-modal generation tasks, enabling creative video production and editing.

`image-to-video`

⬇️ 424,099 • ❤️ 1,000 • 7h ago

---

**[MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)**

*MiniMax*

MiniMax Music 3 is a text-to-audio model capable of generating complete, five-minute songs with lyrics and detailed musical descriptions. It utilizes a hybrid LLM architecture and Flow Matching for coherent, high-fidelity 32 kHz stereo audio output, suitable for complex music production.

`text-to-audio` `2.4B`

⬇️ 8,639 • ❤️ 813 • 2d ago

---

**[MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)**

*MiniMax*

MiniMax H3 is an omni-modal generative system capable of producing up to 15-second videos with synchronized stereo audio at resolutions up to 2K. It supports diverse inputs including text, images, and video, enabling complex multimodal instruction following for video generation tasks.

`image-text-to-video` `33.1B`

⬇️ 2,307,541 • ❤️ 4,017 • 3d ago

---

**[DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)**

*DeepSeek*

DeepSeek-V4-Pro-0813 is a powerful text generation model with enhanced agentic capabilities and DSpark speculative decoding for improved production performance. It excels in complex reasoning, coding, and tool-use tasks, outperforming previous versions and competing with leading proprietary models.

`text-generation` `1650.5B`

⬇️ 21,873 • ❤️ 525 • 3d ago

---

**[Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)**

*Qwen*

Qwen3.8-27B-FP8 is a 27B parameter vision-language model optimized with FP8 quantization for efficient inference. It excels at complex, multi-step tasks involving image and video understanding, autonomous planning, and coding, supporting up to 1M context length.

`image-text-to-text` `27.8B`

⬇️ 352,971 • ❤️ 469 • 2d ago

---

**[Muse-Glimmer-30B-GGUF](https://huggingface.co/unsloth/Muse-Glimmer-30B-GGUF)**

*Unsloth AI*

Muse-Glimmer-30B-GGUF is a 30B parameter multimodal LLM optimized for local agentic tasks, featuring reliable tool use, multi-step reasoning, and failure recovery. It processes interleaved text and images, supporting multilingual inputs and controllable effort for efficient deployment on consumer hardware.

`image-text-to-text` `27.9B`

⬇️ 718,178 • ❤️ 452 • 6d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**

*Björn Engdahl, Adrian Kosowski, Jan Chorowski et al. (9 authors)*

🏢 Pathway

A 150M-parameter reasoning model using recurrent latent reasoning and in-context learning achieves a new cost-accuracy frontier on ARC-AGI-1.

▲ 637 • 💬 2 • ⭐ 2,824 • 6d ago

[🎓 arXiv](https://arxiv.org/abs/2608.09888) • [💻 code](https://github.com/pathwaycom/arc-task-gen) • [🔗 project](https://pathway.com/blog/pathway-150m-model-breaks-arc-agi-1-cost-efficiency-frontier)

---

**[COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation](https://huggingface.co/papers/2605.31264)**

*Tianyi Zhou, Dongrui Liu, Leitao Yuan et al. (5 authors)*

🏢 shanghai ailab 

Person-grounded AI skills are automatically distilled from heterogeneous traces into inspectable, correctable packages that capture both capabilities and behavioral patterns.

▲ 126 • 💬 3 • ⭐ 22,712 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2605.31264) • [💻 code](https://github.com/titanwings/colleague-skill)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 123 • 💬 4 • ⭐ 98,394 • 19mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://huggingface.co/papers/2608.03974)**

*Yicheng Xiao, Wenxun Dai, Xinran Qin et al. (25 authors)*

🏢 jingdong

JoyAI-Video-Edit is a 16B-parameter autoregressive diffusion framework that enables real-time, open-ended video editing with high source fidelity and long-term temporal consistency on a single GPU.

▲ 94 • 💬 1 • ⭐ 1,419 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2608.03974) • [💻 code](https://github.com/jd-opensource/JoyAI-Video-Edit)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 54 • 💬 4 • ⭐ 37,357 • 12mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**

*Youyang Yin, Huanhuan Liu, YY et al. (17 authors)*

🏢 BAIDU

Unlimited OCR introduces Reference Sliding Window Attention to eliminate growing memory consumption during long-sequence OCR tasks, enabling efficient transcription of multiple pages in a single forward pass.

▲ 83 • 💬 7 • ⭐ 23,904 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2606.23050) • [💻 code](https://github.com/baidu/Unlimited-OCR)

---

**[MatrAIx: Simulating the World with 8.3 Billion Persona Agents](https://huggingface.co/papers/2608.04205)**

*Xiaomin Li, Yuexing Hao, Jianheng Hou et al. (93 authors)*

🏢 MatrAIx

MatrAIx is a large-scale simulated-user evaluation framework that uses diverse persona records and interactive environments to test AI systems across many domains.

▲ 42 • 💬 3 • ⭐ 1,098 • 12d ago

[🎓 arXiv](https://arxiv.org/abs/2608.04205) • [💻 code](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) • [🔗 project](https://matraix.ai/)

---

**[M^{2}SNet: Multi-scale in Multi-scale Subtraction Network for Medical Image Segmentation](https://huggingface.co/papers/2303.10894)**

*Xiaoqi Zhao, Hongpeng Jia, Youwei Pang et al. (8 authors)*

A multi-scale subtraction network (M$^{2}$SNet) enhances medical image segmentation by capturing detailed and structural cues, improving localization and edge sharpness compared to traditional methods.

▲ 0 • 💬 0 • ⭐ 999 • 41mo ago

[🎓 arXiv](https://arxiv.org/abs/2303.10894) • [💻 code](https://github.com/Xiaoqi-Zhao-DLUT/MSNet)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 84 • 💬 7 • ⭐ 84,168 • 25mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

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

⭐ 13.7k • 🔱 1.6k • 3h ago

---

**[guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)**

Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPEG/SVG/PDF/DOCX/HTML/MD

`Python` `agent-skill` `ai` `c2pa` `claude` `provenance`

⭐ 10.9k • 🔱 1.1k • 19h ago

---

**[trycompai/crm](https://github.com/trycompai/crm)**

Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

`TypeScript`

⭐ 8.5k • 🔱 1.0k • 2d ago

---

**[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)**

AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

`TypeScript` `agent-skills` `ai-agents` `ai-video` `claude-code` `claude-code-skills`

⭐ 5.2k • 🔱 449 • 2d ago

---

**[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)**

`Python`

⭐ 4.0k • 🔱 529 • 8d ago

---

**[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)**

Free, open-source AI office suite for macOS, Windows & Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and Markdown editing with built-in AI agents.

`TypeScript` `ai` `cross-platform` `docx` `electron` `excel`

⭐ 3.2k • 🔱 545 • 3h ago

---

**[KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing)**

让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。

`Python` `agent-skills` `chinese-writing` `creative-writing` `writing-skill`

⭐ 2.8k • 🔱 229 • 5d ago

---

**[Jakubantalik/thinking-orbs](https://github.com/Jakubantalik/thinking-orbs)**

Dotted thought-orb loading indicators for AI & agent UIs, 9 tuned types, two sizes, auto dark/light

`TypeScript` `ai` `ai-agents` `chat` `loader` `ui`

⭐ 2.5k • 🔱 195 • 11h ago

---

**[QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent)**

A realtime voice runtime that keeps Agents talking, working, and present.  Real-time Voice Runtime for AI Agents

`JavaScript` `acp` `agent` `agentic-ai` `ai-coding` `claude-code`

⭐ 2.2k • 🔱 175 • 1d ago

---

**[makecindy/cindy](https://github.com/makecindy/cindy)**

Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

`TypeScript` `agent` `ai-agent` `ai-assistant` `android` `claude-code`

⭐ 2.1k • 🔱 277 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*

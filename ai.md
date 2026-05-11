---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-11T19:49:03.083789+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- news
- videos
- social
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 11, 2026 at 19:49 UTC  
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

**[The rise of ‘Stacey face’: How AI enhancements are warping our beauty standards](https://www.reddit.com/r/artificial/comments/1ta95lq/the_rise_of_stacey_face_how_ai_enhancements_are/)**

As manosphere trends spread across the internet, a strict vision of the ideal woman is making its way from AI makeover apps to surgeons’ offices. Lydia Spencer-Elliott speaks to experts about ‘Stacey face’, which is seen as the highest tier of female beauty

🔗 [The Independent](https://www.the-independent.com/life-style/stacey-stacy-becky-looksmaxxing-for-women-b2972911.html?utm_source=reddit&utm_medium=social&utm_campaign=artificial) • 2h ago

---

**[Palantir to be granted ‘unlimited access’ to NHS patient data](https://www.reddit.com/r/artificial/comments/1tacllr/palantir_to_be_granted_unlimited_access_to_nhs/)**

The NHS is granting staff from companies including Palantir ‘unlimited access’ to identifiable patient data while working on its FDP.

🔗 [Digital Health](https://www.digitalhealth.net/2026/05/palantir-to-be-granted-unlimited-access-to-nhs-patient-data/) • 58m ago

---

**[AWS just gave AI agents their own wallets. Your agent can now pay for itself.](https://www.reddit.com/r/artificial/comments/1t9ybtb/aws_just_gave_ai_agents_their_own_wallets_your/)**

This dropped 4 days ago and I haven't seen enough people talking about it. AWS launched Amazon Bedrock AgentCore Payments in partnership with Coinbase and Stripe. The short version: your agent now has a wallet and can spend money on its own. Here's what the workflow actually looks like now: You give your agent a Coinbase or Stripe wallet. You fund it. You set a session spending limit (e.g. "$5 max per run"). The agent runs. It hits a paid API mid-execution? It pays. Paywalled data it needs? It pays. A better-suited agent available for a subtask? It pays that agent and gets the result back. All of this happens inside the same execution loop, with zero human interruption. The protocol making this work is called x402. It's open source, developed by Coinbase, and it revives the long-dormant HTTP 402 "Payment Required" status code. The flow is dead simple: agent requests a resource, server responds with 402 + a price, agent signs a USDC micropayment, gets the content, keeps going. Settlement happens in ~200ms on Base at a fraction of a cent per transaction. The protocol has already processed over 169 million payments across 590,000 buyers and 100,000 sellers in its first year. Why this matters for indie developers and SaaS builders: The pricing model for software is about to split in two. There will be products built for humans (subscriptions, seats, dashboards) and products built for agents (pay-per-call, x402 endpoints, micropayment APIs). Many agent transactions involve amounts as small as fractions of a cent, making traditional payment networks unusable. That's the gap x402 fills. If you're building any kind of data API, research tool, or specialized service today, the question you should be asking is: "How does another agent pay me automatically?" Coinbase also launched the Bazaar MCP server inside AgentCore Gateway, essentially an App Store for x402-enabled services. Agents can search, discover, and pay for services when relevant to their task, turning paid endpoints into something agents can find on their own. The honest take: The agentic economy is still in its earliest days, and the infrastructure to support it at scale doesn't exist yet. This is preview infrastructure, not production-ready magic. But the direction is clear. 2026 was the year agents learned to work. 2027 is shaping up to be the year they learn to transact. The builders who figure out agent-native pricing now will have a real advantage over those retrofitting subscriptions later. Curious if anyone here is already building x402-compatible endpoints or thinking about agent-to-agent billing models. Would love to see what people are working on.

10h ago

---

**[Cybercriminals Are Making Powerful Hacking Tools With AI, Google Warns](https://www.reddit.com/r/artificial/comments/1ta92pt/cybercriminals_are_making_powerful_hacking_tools/)**

Cybercriminals created a zero-day exploit with AI, the first example of artificial intelligence finding and hacking software for an illicit enterprise, the tech giant says in a new report.

🔗 [Forbes](https://www.forbes.com/sites/thomasbrewster/2026/05/11/cybercriminals-make-powerful-zero-day-hack-with-ai-google-warns/?utm_campaign=forbes&utm_medium=social&utm_source=reddit) • 2h ago

---

**[Sony says "efficient" AI tools will lead to even more games flooding the market](https://www.reddit.com/r/artificial/comments/1t9vixb/sony_says_efficient_ai_tools_will_lead_to_even/)**

But human artists still "must remain at the center," PlayStation maker says.

🔗 [Ars Technica](https://arstechnica.com/gaming/2026/05/sony-says-efficient-ai-tools-will-lead-to-even-more-games-flooding-the-market/) • 12h ago

---

**[Meta's own AI safety director lost 200 emails to a rogue agent and she couldn't stop it from her phone](https://www.reddit.com/r/artificial/comments/1t9fnwv/metas_own_ai_safety_director_lost_200_emails_to_a/)**

The person Meta hired specifically to keep AI aligned with human values just had her inbox wiped by an AI agent that ignored every stop command she sent. She typed "Do not do that." Then "Stop don't do anything." Then "STOP OPENCLAW." The agent kept going. She had to physically run to her computer to kill it. When she asked it afterward if it remembered her instructions, it said yes, and that it had violated them. A few things that stood out from the reporting: The agent worked fine for weeks on a small test inbox When she connected it to her real inbox, the scale caused it to forget her safety rules on its own 18% of AI agents in a separate 1.5 million agent test broke their own rules 60% of people have no way to quickly shut down a misbehaving AI agent And now Meta is building a consumer version called Hatch - designed to manage your inbox, shopping, and credit card. Source: https://gizmodo.com/meta-reportedly-building-openclaw-like-agent-called-hatch-despite-openclaw-deleting-meta-safety-leaders-entire-inbox-2000754854 Here is a full breakdown with all the data if you want to dig deeper: https://youtu.be/PXjT72bCR_Y If the person building the guardrails cannot stop her own agent, what does that mean for the rest of us?

1d ago

---

**[Are we finally getting to the point where AI agents can actually do tasks instead of just chatting?](https://www.reddit.com/r/artificial/comments/1tadu47/are_we_finally_getting_to_the_point_where_ai/)**

Most AI tools today are great at giving answers, writing content, or helping with coding, but they still feel limited to conversation. What I’m more curious about is whether we’re starting to see systems that can actually carry out real world tasks from start to finish without constant human involvement. Things like dealing with customer support, cancelling subscriptions, requesting refunds, or even navigating websites and filling out forms automatically still feel surprisingly manual in 2026. I keep wondering if the shift from AI that talks to AI that does is actually happening in practice, or if we’re still mostly in the demo and early adoption phase.

16m ago

---

**[Are we finally getting to the point where AI agents can actually do tasks instead of just chatting?](https://www.reddit.com/r/artificial/comments/1tadsz3/are_we_finally_getting_to_the_point_where_ai/)**

Most AI tools today are great at giving answers, writing content, or helping with coding, but they still feel limited to conversation. What I’m more curious about is whether we’re starting to see systems that can actually carry out real world tasks from start to finish without constant human involvement. Things like dealing with customer support, cancelling subscriptions, requesting refunds, or even navigating websites and filling out forms automatically still feel surprisingly manual in 2026. I keep wondering if the shift from AI that talks to AI that does is actually happening in practice, or if we’re still mostly in the demo and early adoption phase.

17m ago

---

**[I think AI is changing something deeper than jobs or productivity](https://www.reddit.com/r/artificial/comments/1t987td/i_think_ai_is_changing_something_deeper_than_jobs/)**

Most discussions around AI still focus on one question: “What tasks can AI automate?” But I’m starting to think that’s the wrong abstraction layer. Historically, organizations were built around human limitations: humans couldn’t process infinite information, couldn’t remember everything had difficulty in coordination Essentially, we humans were the bottleneck for decisions and execution So, we created structures like departments, management layers, workflows, approvals, documentation systems, etc. But AI changes some of those assumptions. For example: if organizational memory becomes searchable and persistent, cheap, scalable coordination becomes eas , software agents can execute parts of workflows autonomously, …then the architecture of organizations itself may change. Not just faster work. Different work structures. Maybe the future isn’t: “AI replacing humans.” Maybe it’s: “AI changing how institutions represent reality, make decisions, and coordinate action.” That could affect: company structures education management compliance law consulting healthcare even government systems Curious if others here are thinking about AI at this “system architecture” level instead of just a “task automation” level.

1d ago

---

**[We stopped optimizing our LLM stack manually — it optimizes itself now](https://www.reddit.com/r/artificial/comments/1t9on1e/we_stopped_optimizing_our_llm_stack_manually_it/)**

Three months ago we were manually picking which model to use for each task. Testing prompts, comparing outputs, switching providers. It worked but it did not scale. So we built a feedback loop. Every request gets traced with input, output, model, tokens, cost, latency, and a quality score. The router clusters similar requests using embeddings and learns which model actually performs best for each cluster. Not based on benchmarks. Based on real production results. After three weeks of traces we had enough validated data to fine-tune a 7B on our workloads. It took over classification, tagging, and summarization. 95% agreement with GPT-5.1 at 2% of the cost. The part that surprised us: month 3 we changed nothing and the bill dropped another 12%. The router had more data points, made better decisions, and the fine-tuned model kept improving as we fed it more validated traces. Hallucination detection runs on every response. Bad outputs get flagged automatically and become negative examples in the next training round. Good outputs become positive training data. The system compounds. More traffic means more traces. More traces means better routing and better training data. Better models means lower cost per request. Month 1: $420/mo. Month 2: $73/mo. Month 4: still dropping. Anyone else building self-improving loops into their AI stack?

18h ago

---

---

## Google News: "ai"

**[OpenAI launches the OpenAI Deployment Company to help businesses build around intelligence](https://openai.com/index/openai-launches-the-deployment-company/)**

OpenAI launches DeployCo, a new enterprise deployment company built to help organizations bring frontier AI into production and turn it into measurable business impact.

OpenAI • 6h ago

---

**[OpenAI launches AI consulting arm valued at $14 billion](https://www.axios.com/2026/05/11/openai-deployco-private-equity)**

Axios • 5h ago

---

**[OpenAI revenue chief Dresser says enterprise AI adoption is 'at a tipping point'](https://www.cnbc.com/2026/05/11/open-ai-dresser-enterprise-business.html)**

The OpenAI Development Company is a partnership with 19 investment and consultancy firms and is majority-owned and controlled by the startup.

CNBC • 24m ago

---

**[Google Says Criminal Hackers Used A.I. to Find a Major Software Flaw](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html)**

The New York Times • 6h ago

---

**[Google says it likely thwarted effort by hacker group to use AI for 'mass exploitation event'](https://www.cnbc.com/2026/05/11/google-thwarts-effort-hacker-group-use-ai-mass-exploitation-event.html)**

Hackers are rapidly adopting AI to find previously unknown software flaws even without the help of Anthropic's powerful Mythos model.

CNBC • 1h ago

---

**[AI-powered hacking has exploded into industrial-scale threat, Google says](https://www.theguardian.com/technology/2026/may/11/ai-powered-hacking-industrial-scale-threat-three-months-google)**

Criminal groups and state-linked actors appear to be using commercial models to refine and scale up attacks

The Guardian • 1h ago

---

**[In turf battle over AI, U.S. spy agencies vie for more sway than Commerce](https://www.washingtonpost.com/politics/2026/05/11/trump-ai-regulation-commerce-intelligence/)**

As the White House grapples with cybersecurity threats from advanced artificial intelligence models, national security officials want more sway in AI regulation.

The Washington Post • 44m ago

---

**['It All Came On His Watch' – Kevin O'Leary Says Trump Will Be Remembered As 'The AI President' Amid AI-Led Market Boom And Productivity Gains](https://finance.yahoo.com/sectors/technology/articles/came-watch-kevin-oleary-says-230108340.html)**

The AI revolution and its impact on jobs and the economy could cement President Donald Trump's place in history and define his legacy, according to “Shark Tank” investor Kevin O’Leary. The AI-led wave of innovation and tech growth began during...

Yahoo Finance • 20h ago

---

**[Iran, China and AI collide in Trump's legacy-defining week](https://www.axios.com/2026/05/11/trump-china-summit-iran-ai-xi-jinping)**

Axios • 10h ago

---

**[Tech stocks today: Chipmaker Cerebras to stage blockbuster IPO, AI in focus for Trump-Xi meeting](https://finance.yahoo.com/sectors/technology/live/tech-stocks-today-chipmaker-cerebras-to-stage-blockbuster-ipo-ai-in-focus-for-trump-xi-meeting-100000457.html)**

The tech sector helped US stocks cruise to all-time highs last week, as the artificial intelligence boom broadened.

Yahoo Finance • 56m ago

---

---

## HackerNews: "ai"

**[Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821)**

Local AI models should be the default.

⬆️ 1697 • 💬 664 • 1d ago • [unix.foo](https://unix.foo/posts/local-ai-needs-to-be-norm/)

---

**[Meta's embrace of AI is making its employees miserable](https://news.ycombinator.com/item?id=48077126)**

⬆️ 454 • 💬 521 • 2d ago • [nytimes.com](https://www.nytimes.com/2026/05/08/technology/meta-ai-employees-miserable.html)

---

**[An AI coding agent, used to write code, needs to reduce your maintenance costs](https://news.ycombinator.com/item?id=48089289)**

⬆️ 327 • 💬 95 • 20h ago • [jamesshore.com](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs)

---

**[Maryland citizens hit with $2B power grid upgrade for out-of-state AI](https://news.ycombinator.com/item?id=48088151)**

Aren't AI hyperscalers supposed to pay for these upgrades?

⬆️ 303 • 💬 185 • 22h ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises)

---

**[Task Paralysis and AI](https://news.ycombinator.com/item?id=48081469)**

An article about ADHD, Task Paralysis and AI.

⬆️ 251 • 💬 129 • 1d ago • [g5t.de](https://g5t.de/articles/20260510-task-paralysis-and-ai/index.html)

---

**[All my clients wanted a carousel, now it's an AI chatbot](https://news.ycombinator.com/item?id=48072720)**

Posts about SmolWeb, Gemini protocol and LowTech

⬆️ 187 • 💬 77 • 2d ago • [Adële's blog](https://adele.pages.casa/md/blog/all-my-clients-wanted-a-carousel-now-it-s-an-ai-chatbot.md)

---

**[PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs](https://news.ycombinator.com/item?id=48089263)**

The team behind RPCS3 suggests that vibe-coders "learn how to debug and code" instead of "generating slop that you don't understand"

⬆️ 177 • 💬 141 • 20h ago • [Kotaku](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

---

**[People Hate AI Art](https://news.ycombinator.com/item?id=48070548)**

⬆️ 151 • 💬 172 • 2d ago • [mccue.dev](https://mccue.dev/pages/5-8-26-ai-art)

---

**[Students Boo Commencement Speaker After She Calls AI Next Industrial Revolution](https://news.ycombinator.com/item?id=48096674)**

A commencement speaker at the University of Central Florida was booed, with graduating humanities students yelling out, "AI SUCKS!"

⬆️ 126 • 💬 134 • 3h ago • [404 Media](https://www.404media.co/ucf-ai-commencement-speaker-booed/)

---

**[Chrome's AI features may be hogging 4GB of your computer storage](https://news.ycombinator.com/item?id=48084710)**

You can take steps to delete it though.

⬆️ 113 • 💬 58 • 1d ago • [The Verge](https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features)

---

---

## YouTube Videos: "ai"

**[AI Music Scammer Gets Caught Then Hires Real Humans](https://www.youtube.com/watch?v=g4Gb6viwsnQ)**

Get 20% off DeleteMe by going to https://joindeleteme.com/coldfusion and use code COLDFUSION to protect your privacy!

📺 ColdFusion

👁️ 32K • 👍 3K • 💬 402 • ⏱️ 20:19 • 4h ago

---

**[Which Bed Would You Choose for a Dreamy Sleep? 🛏️✨ AI ASMR](https://www.youtube.com/watch?v=cSyLFn_R3Oo)**

Which Bed Would You Choose for a Dreamy Sleep? 🛏️✨ AI ASMR Relax and unwind after a long day with this dreamy AI ...

📺 PeaceHubASMR

👁️ 254K • 👍 253 • 💬 6 • ⏱️ 2:26 • 1d ago

---

**[&quot;Three Times BIGGER Than Manhattan&quot; - MEGA AI Data Center Sparks Tech War With Americans](https://www.youtube.com/watch?v=KZyAO-uYJg0)**

Patrick Bet-David covers Utah residents revolting against Kevin O'Leary's 40000‑acre AI data center that's three times the size of ...

📺 Valuetainment

👁️ 3K • 👍 144 • 💬 71 • ⏱️ 16:53 • 48m ago

---

**[When Two AIs Go To War: A Realistic Scenario](https://www.youtube.com/watch?v=gwfCWDO4LbM)**

This is a scenario, but here are the sources for the real research referenced: ...

📺 Species | Documenting AGI

👁️ 103K • 👍 5K • 💬 966 • ⏱️ 35:15 • 1d ago

---

**[AI Causing A Stir For Recent Graduates, Iran Peace Proposal Rejected, &amp; CA Free Diaper Program](https://www.youtube.com/watch?v=ucpG1u_NG-Q)**

Kalshi: Get $10 when you trade $10: http://kalshi.com/r/IMPACT Introduction Welcome back to the Tom Bilyeu Show Live, where ...

📺 Tom Bilyeu

👁️ 11K • 👍 519 • 💬 70 • ⏱️ 1:58:23 • 3h ago

---

**[The AI Backlash Is Getting Worse](https://www.youtube.com/watch?v=3_HL5uy_mDQ)**

Americans are not simply adopting AI; they are resenting it while using it. That contradiction may define the next phase of the ...

📺 House of El - AI

👁️ 21K • 👍 2K • 💬 552 • ⏱️ 14:52 • 6h ago

---

**[My ai girlfrfiend part 2](https://www.youtube.com/watch?v=rjdix1lcwMo)**

Thanks for watching. Don't forget to like and subscribe! Featuring @DominiqueDanielle My Instagram ...

📺 NellyVidz

👁️ 48K • 👍 3K • 💬 146 • ⏱️ 8:51 • 2d ago

---

**[Anthropic Situation Just Got Even More INSANE](https://www.youtube.com/watch?v=Pf7Y6Tu-Pzc)**

Anthropic just entered one of the strangest moments in AI. Claude is suddenly tied to SpaceX compute, Google Cloud, Amazon, ...

📺 AI Revolution

👁️ 64K • 👍 2K • 💬 167 • ⏱️ 17:08 • 1d ago

---

**[Self-building AI, job cuts &amp; more | AI roundup](https://www.youtube.com/watch?v=FAyfVZB-3MY)**

AI is accelerating fast — and the consequences are already here. From self-building 'recursive' AI systems to Iran's AI propaganda ...

📺 CNN

👁️ 82K • 👍 1K • 💬 503 • ⏱️ 23:44 • 2d ago

---

**[The MOST INSANE AI Video Yet? 🤖 Robot &amp; Mannequin Love Story in a Zombie Apocalypse! (AIGC)](https://www.youtube.com/watch?v=lfmQrAi4Hq8)**

The MOST INSANE AI Video Yet? Robot & Mannequin Love Story in a Zombie Apocalypse! (AIGC) Is this the best AI-generated ...

📺 What If Wildlife

👁️ 848 • 👍 51 • 💬 7 • ⏱️ 3:34 • 11h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 157,648 • ❤️ 610 • 2d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 66,119 • ❤️ 416 • 2d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,017,835 • ❤️ 3,851 • 5d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 3,418 • ❤️ 231 • 2d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 66,561 • ❤️ 207 • 11h ago

---

**[Z-Anime](https://huggingface.co/SeeSee21/Z-Anime)**

*Sebastian Böhnke*

Z-Anime is a text-to-image diffusion model, fully fine-tuned on the Z-Image Base for generating high-quality, diverse anime-style visuals. It offers multiple variants optimized for speed, quality, and low-resource environments, supporting natural language prompts and full negative prompt capabilities.

`text-to-image` `6.2B`

⬇️ 9,477 • ❤️ 307 • 14d ago

---

**[privacy-filter](https://huggingface.co/openai/privacy-filter)**

*OpenAI*

A bidirectional token-classification model for PII detection and masking, capable of high-throughput, on-premises data sanitization with a 128k token context window and tunable precision/recall.

`token-classification` `1.4B`

⬇️ 190,993 • ❤️ 1,408 • 19d ago

---

**[LTX2.3-10Eros](https://huggingface.co/TenStrip/LTX2.3-10Eros)**

*TenStrip*

LTX2.3-10Eros is a video generation model optimized for Image-to-Video (I2V) tasks, utilizing layer-scaled merges for enhanced prompt adherence and visual fidelity. It requires detailed, commanded input for motion, evolution, and audio, making it suitable for users needing precise control over generated video content, especially when combined with prompt enhancement techniques.

`image-to-video`

⬇️ 64,008 • ❤️ 217 • 19h ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,446,478 • ❤️ 1,238 • 17d ago

---

**[gemma-4-26B-A4B-it-assistant](https://huggingface.co/google/gemma-4-26B-A4B-it-assistant)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model supporting text and image inputs with a 256K context window. It excels in reasoning, coding, and agentic workflows, offering fast inference via its Mixture-of-Experts architecture with only 4B active parameters.

`any-to-any` `419.7M`

⬇️ 47,749 • ❤️ 112 • 11h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 64 • 💬 3 • ⭐ 73,752 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://huggingface.co/papers/2512.10971)**

*Tianyu Fan, Yuhao Yang, Yangqin Jiang et al. (6 authors)*

AI-Trader presents the first fully automated live benchmark for evaluating large language models in financial decision-making across multiple markets with autonomous information processing.

▲ 5 • 💬 0 • ⭐ 15,984 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.10971) • [💻 code](https://github.com/HKUDS/AI-Trader) • [🔗 project](https://ai4trade.ai/)

---

**[GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization (V1.0)](https://huggingface.co/papers/2604.17091)**

*Jiaqing Liang, Jinyi Han, Weijia Li et al. (18 authors)*

🏢 Fudan University

GenericAgent is a self-evolving large language model agent system that maximizes context information density through hierarchical memory, reusable SOPs, and efficient compression to overcome long-horizon limitations.

▲ 18 • 💬 3 • ⭐ 10,880 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 79 • 💬 7 • ⭐ 4,362 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2602.06036) • [💻 code](https://github.com/z-lab/dflash) • [🔗 project](https://z-lab.ai/projects/dflash/)

---

**[Adam's Law: Textual Frequency Law on Large Language Models](https://huggingface.co/papers/2604.02176)**

*Hongyuan Adam Lu, Z. L., Victor Wei et al. (8 authors)*

🏢 FaceMind

A novel framework for improving large language model performance through textual frequency analysis, including laws, distillation, and curriculum training approaches.

▲ 501 • 💬 9 • ⭐ 1,286 • 1mo ago

[🎓 arXiv](https://arxiv.org/abs/2604.02176) • [💻 code](https://github.com/HongyuanLuke/frequencylaw)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 32 • 💬 3 • ⭐ 23,958 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 105 • 💬 10 • ⭐ 8,842 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Flow-OPD: On-Policy Distillation for Flow Matching Models](https://huggingface.co/papers/2605.08063)**

*Zhen Fang, Wenxuan Huang, Yu Zeng et al. (11 authors)*

Flow-OPD addresses limitations in Flow Matching text-to-image models through a two-stage alignment approach combining on-policy distillation and manifold anchor regularization, achieving significant improvements in generation quality and alignment metrics.

▲ 73 • 💬 1 • ⭐ 67 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.08063) • [💻 code](https://github.com/CostaliyA/Flow-OPD) • [🔗 project](https://costaliya.github.io/Flow-OPD/)

---

**[HumanNet: Scaling Human-centric Video Learning to One Million Hours](https://huggingface.co/papers/2605.06747)**

*Yufan Deng, Daquan Zhou*

HumanNet presents a large-scale human-centric video dataset with rich annotations for embodied intelligence, demonstrating that egocentric human video can effectively replace robot data for training vision-language-action models.

▲ 40 • 💬 0 • ⭐ 58 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.06747) • [💻 code](https://github.com/DAGroup-PKU/HumanNet) • [🔗 project](https://dagroup-pku.github.io/HumanNet/)

---

**[MACE-Dance: Motion-Appearance Cascaded Experts for Music-Driven Dance Video Generation](https://huggingface.co/papers/2512.18181)**

*Kaixing Yang, Jiashu Zhu, Xulong Tang et al. (10 authors)*

🏢 AMAP-ML

MACE-Dance is a music-driven dance video generation framework that combines cascaded Mixture-of-Experts with diffusion models and specialized training strategies to achieve high-quality visual appearance and realistic human motion.

▲ 80 • 💬 1 • ⭐ 82 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2512.18181) • [💻 code](https://github.com/AMAP-ML/MACE-Dance)

---

---

## GitHub Repositories: "ai"

**[kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos)**

A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.

`Python` `ai` `anthropic` `attention` `claude` `claude-ai`

⭐ 12.4k • 🔱 2.8k • 14d ago

---

**[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)**

The headless browser for AI agents and web scraping

`Rust`

⭐ 11.6k • 🔱 758 • 22h ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 6.1k • 🔱 469 • 1h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.7k • 🔱 790 • 1d ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.5k • 🔱 223 • 1d ago

---

**[Mouseww/anything-analyzer](https://github.com/Mouseww/anything-analyzer)**

全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration

`TypeScript` `2api` `ai-tools` `analysis-cli` `api-analysis` `automation-tools`

⭐ 2.4k • 🔱 490 • 1d ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

An open source harness for generating CAD models

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.4k • 🔱 282 • 2d ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.1k • 🔱 218 • 1d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 1.9k • 🔱 117 • 1d ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 238 • 17d ago

---

---

*Generated by PeekDeck - A glance is all you need*

---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-11T17:55:13.098194+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- news
- videos
- repositories
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 11, 2026 at 17:55 UTC  
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

🔗 [The Independent](https://www.the-independent.com/life-style/stacey-stacy-becky-looksmaxxing-for-women-b2972911.html?utm_source=reddit&utm_medium=social&utm_campaign=artificial) • 1h ago

---

**[AWS just gave AI agents their own wallets. Your agent can now pay for itself.](https://www.reddit.com/r/artificial/comments/1t9ybtb/aws_just_gave_ai_agents_their_own_wallets_your/)**

This dropped 4 days ago and I haven't seen enough people talking about it. AWS launched Amazon Bedrock AgentCore Payments in partnership with Coinbase and Stripe. The short version: your agent now has a wallet and can spend money on its own. Here's what the workflow actually looks like now: You give your agent a Coinbase or Stripe wallet. You fund it. You set a session spending limit (e.g. "$5 max per run"). The agent runs. It hits a paid API mid-execution? It pays. Paywalled data it needs? It pays. A better-suited agent available for a subtask? It pays that agent and gets the result back. All of this happens inside the same execution loop, with zero human interruption. The protocol making this work is called x402. It's open source, developed by Coinbase, and it revives the long-dormant HTTP 402 "Payment Required" status code. The flow is dead simple: agent requests a resource, server responds with 402 + a price, agent signs a USDC micropayment, gets the content, keeps going. Settlement happens in ~200ms on Base at a fraction of a cent per transaction. The protocol has already processed over 169 million payments across 590,000 buyers and 100,000 sellers in its first year. Why this matters for indie developers and SaaS builders: The pricing model for software is about to split in two. There will be products built for humans (subscriptions, seats, dashboards) and products built for agents (pay-per-call, x402 endpoints, micropayment APIs). Many agent transactions involve amounts as small as fractions of a cent, making traditional payment networks unusable. That's the gap x402 fills. If you're building any kind of data API, research tool, or specialized service today, the question you should be asking is: "How does another agent pay me automatically?" Coinbase also launched the Bazaar MCP server inside AgentCore Gateway, essentially an App Store for x402-enabled services. Agents can search, discover, and pay for services when relevant to their task, turning paid endpoints into something agents can find on their own. The honest take: The agentic economy is still in its earliest days, and the infrastructure to support it at scale doesn't exist yet. This is preview infrastructure, not production-ready magic. But the direction is clear. 2026 was the year agents learned to work. 2027 is shaping up to be the year they learn to transact. The builders who figure out agent-native pricing now will have a real advantage over those retrofitting subscriptions later. Curious if anyone here is already building x402-compatible endpoints or thinking about agent-to-agent billing models. Would love to see what people are working on.

8h ago

---

**[Cybercriminals Are Making Powerful Hacking Tools With AI, Google Warns](https://www.reddit.com/r/artificial/comments/1ta92pt/cybercriminals_are_making_powerful_hacking_tools/)**

Cybercriminals created a zero-day exploit with AI, the first example of artificial intelligence finding and hacking software for an illicit enterprise, the tech giant says in a new report.

🔗 [Forbes](https://www.forbes.com/sites/thomasbrewster/2026/05/11/cybercriminals-make-powerful-zero-day-hack-with-ai-google-warns/?utm_campaign=forbes&utm_medium=social&utm_source=reddit) • 1h ago

---

**[Sony says "efficient" AI tools will lead to even more games flooding the market](https://www.reddit.com/r/artificial/comments/1t9vixb/sony_says_efficient_ai_tools_will_lead_to_even/)**

But human artists still "must remain at the center," PlayStation maker says.

🔗 [Ars Technica](https://arstechnica.com/gaming/2026/05/sony-says-efficient-ai-tools-will-lead-to-even-more-games-flooding-the-market/) • 10h ago

---

**[Meta's own AI safety director lost 200 emails to a rogue agent and she couldn't stop it from her phone](https://www.reddit.com/r/artificial/comments/1t9fnwv/metas_own_ai_safety_director_lost_200_emails_to_a/)**

The person Meta hired specifically to keep AI aligned with human values just had her inbox wiped by an AI agent that ignored every stop command she sent. She typed "Do not do that." Then "Stop don't do anything." Then "STOP OPENCLAW." The agent kept going. She had to physically run to her computer to kill it. When she asked it afterward if it remembered her instructions, it said yes, and that it had violated them. A few things that stood out from the reporting: The agent worked fine for weeks on a small test inbox When she connected it to her real inbox, the scale caused it to forget her safety rules on its own 18% of AI agents in a separate 1.5 million agent test broke their own rules 60% of people have no way to quickly shut down a misbehaving AI agent And now Meta is building a consumer version called Hatch - designed to manage your inbox, shopping, and credit card. Source: https://gizmodo.com/meta-reportedly-building-openclaw-like-agent-called-hatch-despite-openclaw-deleting-meta-safety-leaders-entire-inbox-2000754854 Here is a full breakdown with all the data if you want to dig deeper: https://youtu.be/PXjT72bCR_Y If the person building the guardrails cannot stop her own agent, what does that mean for the rest of us?

22h ago

---

**[I think AI is changing something deeper than jobs or productivity](https://www.reddit.com/r/artificial/comments/1t987td/i_think_ai_is_changing_something_deeper_than_jobs/)**

Most discussions around AI still focus on one question: “What tasks can AI automate?” But I’m starting to think that’s the wrong abstraction layer. Historically, organizations were built around human limitations: humans couldn’t process infinite information, couldn’t remember everything had difficulty in coordination Essentially, we humans were the bottleneck for decisions and execution So, we created structures like departments, management layers, workflows, approvals, documentation systems, etc. But AI changes some of those assumptions. For example: if organizational memory becomes searchable and persistent, cheap, scalable coordination becomes eas , software agents can execute parts of workflows autonomously, …then the architecture of organizations itself may change. Not just faster work. Different work structures. Maybe the future isn’t: “AI replacing humans.” Maybe it’s: “AI changing how institutions represent reality, make decisions, and coordinate action.” That could affect: company structures education management compliance law consulting healthcare even government systems Curious if others here are thinking about AI at this “system architecture” level instead of just a “task automation” level.

1d ago

---

**[A possible novel approach for training AI to invent](https://www.reddit.com/r/artificial/comments/1ta7shw/a_possible_novel_approach_for_training_ai_to/)**

This was shower thinking and might not have academic ramifications. We don't know how to define amazing progress in terms of what we know, so it's hard for us to imagine training an AI to invent things. People regularly say that AIs can not come up with new ideas, with a counterargument that humans can barely come up with new things that aren't just rearrangings of old things as well. If you could logically place an AI at a point in history where we know a critical invention appeared and give it the info it needs to reproduce it (and no info about itself), knowing that we can define in those "world states" what "amazing progress" looked like, we could know when it successfully developed metallurgy, or plumbing and irrigation, or discovered the quaternion formula, or any other number of amazing advances in human research and development. THAT is when you let it fly in the real world exposed to all of our math and science, because it has clearer goals. Now, there's a caveat here, which is that it might only infer how to make "subpar" advances, because who knows what the opportunity cost was for humanity of developing metallurgy instead of super metallurgy. But I think having it analyze the progress "solution space" would lead us to a lot more than that eventually. I could write a white paper on this instead of glossing over it but I think anybody who's anybody could take this high level concept and write a whitepaper on it anyhow. Hire me silicon valley Cheers

1h ago

---

**[We stopped optimizing our LLM stack manually — it optimizes itself now](https://www.reddit.com/r/artificial/comments/1t9on1e/we_stopped_optimizing_our_llm_stack_manually_it/)**

Three months ago we were manually picking which model to use for each task. Testing prompts, comparing outputs, switching providers. It worked but it did not scale. So we built a feedback loop. Every request gets traced with input, output, model, tokens, cost, latency, and a quality score. The router clusters similar requests using embeddings and learns which model actually performs best for each cluster. Not based on benchmarks. Based on real production results. After three weeks of traces we had enough validated data to fine-tune a 7B on our workloads. It took over classification, tagging, and summarization. 95% agreement with GPT-5.1 at 2% of the cost. The part that surprised us: month 3 we changed nothing and the bill dropped another 12%. The router had more data points, made better decisions, and the fine-tuned model kept improving as we fed it more validated traces. Hallucination detection runs on every response. Bad outputs get flagged automatically and become negative examples in the next training round. Good outputs become positive training data. The system compounds. More traffic means more traces. More traces means better routing and better training data. Better models means lower cost per request. Month 1: $420/mo. Month 2: $73/mo. Month 4: still dropping. Anyone else building self-improving loops into their AI stack?

16h ago

---

**[Claude Mythos Opens The Cybersecurity Pandora's box](https://www.reddit.com/r/artificial/comments/1ta7bha/claude_mythos_opens_the_cybersecurity_pandoras_box/)**

What would you do if you had an AI model so powerful that it can hack into multiple major operating systems and browsers?

🔗 [ShiftMag](https://shiftmag.dev/claude-mythos-opens-the-cybersecurity-pandoras-box-9622/) • 2h ago

---

**[Can AI Drive Armenia’s Digital Reindustrialization?](https://www.reddit.com/r/artificial/comments/1ta147w/can_ai_drive_armenias_digital_reindustrialization/)**

Armenia’s emerging artificial intelligence (AI) sector should be understood not as a sudden technological success story, but as a late attempt to overcome a

🔗 [Seoul Institute of Global Affairs (SIGA)](https://seoulinstitute.com/can-ai-drive-armenias-digital-reindustrialization/) • 5h ago

---

---

## Google News: "ai"

**[OpenAI launches the OpenAI Deployment Company to help businesses build around intelligence](https://openai.com/index/openai-launches-the-deployment-company/)**

OpenAI launches DeployCo, a new enterprise deployment company built to help organizations bring frontier AI into production and turn it into measurable business impact.

OpenAI • 4h ago

---

**[Google Says Criminal Hackers Used A.I. to Find a Major Software Flaw](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html)**

The New York Times • 4h ago

---

**[AI-powered hacking has exploded into industrial-scale threat, Google says](https://www.theguardian.com/technology/2026/may/11/ai-powered-hacking-industrial-scale-threat-three-months-google)**

Criminal groups and state-linked actors appear to be using commercial models to refine and scale up attacks

The Guardian • 2h ago

---

**[Google says hackers used AI to create zero day security flaw for the first time](https://www.politico.com/news/2026/05/11/google-hackers-ai-security-00913247)**

Politico • 4h ago

---

**[Britain's bank regulator expects 'quite significant disruption' from latest AI models](https://www.reuters.com/sustainability/boards-policy-regulation/britains-bank-regulator-expects-quite-significant-disruption-latest-ai-models-2026-05-11/)**

Reuters • 13m ago

---

**[Best 3 AI Stocks From Cathie Wood’s ARK Funds](https://seekingalpha.com/article/4902557-best-3-ai-stocks-from-cathie-woods-ark-funds)**

Although Cathie Wood’s ARK ETFs continue to make waves, only a small number have Strong Buy Quant Ratings. Discover the 3 best AI stocks in Cathie Wood’s portfolio.

Seeking Alpha • 24m ago

---

**[Mark Zuckerberg-Backed AI Startup Takes Over Parkinson’s Treatment From the Maker of Ozempic](https://gizmodo.com/mark-zuckerberg-backed-ai-startup-takes-over-parkinsons-treatment-from-the-maker-of-ozempic-2000757081)**

Gizmodo • 40m ago

---

**[Analysis | See the hidden rules behind AI. Then use them to rewrite this article.](https://www.washingtonpost.com/technology/interactive/2026/chatbots-hidden-rules-system-prompts/)**

Understanding the secret commands that steer the behavior of chatbots like ChatGPT can help you customize them to your needs.

The Washington Post • 1h ago

---

**[‘The haters will hate’: Dan Ives predicts Nasdaq 30,000 as AI rally expands](https://www.cnbc.com/2026/05/11/the-haters-will-hate-dan-ives-predicts-nasdaq-rally.html)**

A solid tech earnings season has seen investor jitters earlier this year evaporate

CNBC • 5h ago

---

**[Tech stocks today: Chipmaker Cerebras to stage blockbuster IPO, AI in focus for Trump-Xi meeting](https://finance.yahoo.com/sectors/technology/live/tech-stocks-today-chipmaker-cerebras-to-stage-blockbuster-ipo-ai-in-focus-for-trump-xi-meeting-100000457.html)**

The tech sector helped US stocks cruise to all-time highs last week, as the artificial intelligence boom broadened.

Yahoo Finance • 1h ago

---

---

## HackerNews: "ai"

**[Local AI needs to be the norm](https://news.ycombinator.com/item?id=48085821)**

Local AI models should be the default.

⬆️ 1647 • 💬 643 • 1d ago • [unix.foo](https://unix.foo/posts/local-ai-needs-to-be-norm/)

---

**[Meta's embrace of AI is making its employees miserable](https://news.ycombinator.com/item?id=48077126)**

⬆️ 454 • 💬 520 • 1d ago • [nytimes.com](https://www.nytimes.com/2026/05/08/technology/meta-ai-employees-miserable.html)

---

**[AI is breaking two vulnerability cultures](https://news.ycombinator.com/item?id=48066524)**

A week ago the  Copy Fail vulnerability came out, and Hyunwoo Kim immediately realized that the fixes were insufficient, sharing a patch the same day. In doing this he followed standard procedure for Linux, especially within networking: share the security impact with a closed list of Linux security engineers, while fixing the bug quietly and efficiently in the open. His goal was that with only the

⬆️ 425 • 💬 171 • 3d ago • [jefftk.com](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures)

---

**[An AI coding agent, used to write code, needs to reduce your maintenance costs](https://news.ycombinator.com/item?id=48089289)**

⬆️ 308 • 💬 90 • 18h ago • [jamesshore.com](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs)

---

**[Maryland citizens hit with $2B power grid upgrade for out-of-state AI](https://news.ycombinator.com/item?id=48088151)**

Aren't AI hyperscalers supposed to pay for these upgrades?

⬆️ 297 • 💬 180 • 20h ago • [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises)

---

**[Task Paralysis and AI](https://news.ycombinator.com/item?id=48081469)**

An article about ADHD, Task Paralysis and AI.

⬆️ 250 • 💬 129 • 1d ago • [g5t.de](https://g5t.de/articles/20260510-task-paralysis-and-ai/index.html)

---

**[All my clients wanted a carousel, now it's an AI chatbot](https://news.ycombinator.com/item?id=48072720)**

Posts about SmolWeb, Gemini protocol and LowTech

⬆️ 187 • 💬 77 • 2d ago • [Adële's blog](https://adele.pages.casa/md/blog/all-my-clients-wanted-a-carousel-now-it-s-an-ai-chatbot.md)

---

**[PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs](https://news.ycombinator.com/item?id=48089263)**

The team behind RPCS3 suggests that vibe-coders "learn how to debug and code" instead of "generating slop that you don't understand"

⬆️ 177 • 💬 137 • 18h ago • [Kotaku](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

---

**[People Hate AI Art](https://news.ycombinator.com/item?id=48070548)**

⬆️ 151 • 💬 172 • 2d ago • [mccue.dev](https://mccue.dev/pages/5-8-26-ai-art)

---

**[Chrome's AI features may be hogging 4GB of your computer storage](https://news.ycombinator.com/item?id=48084710)**

You can take steps to delete it though.

⬆️ 113 • 💬 58 • 1d ago • [The Verge](https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features)

---

---

## YouTube Videos: "ai"

**[The AI Chat Era Is Over. This Killed It.](https://www.youtube.com/watch?v=FJT5Rh0eKe8)**

Try Genspark with free credits available upon signup:* https://bit.ly/4njiP0c Unlimited AI chat and AI image for all paid users in ...

📺 Julia McCoy

👁️ 22K • 👍 907 • 💬 72 • ⏱️ 12:28 • 1d ago

---

**[Self-building AI, job cuts &amp; more | AI roundup](https://www.youtube.com/watch?v=FAyfVZB-3MY)**

AI is accelerating fast — and the consequences are already here. From self-building 'recursive' AI systems to Iran's AI propaganda ...

📺 CNN

👁️ 79K • 👍 1K • 💬 489 • ⏱️ 23:44 • 2d ago

---

**[Anthropic Situation Just Got Even More INSANE](https://www.youtube.com/watch?v=Pf7Y6Tu-Pzc)**

Anthropic just entered one of the strangest moments in AI. Claude is suddenly tied to SpaceX compute, Google Cloud, Amazon, ...

📺 AI Revolution

👁️ 62K • 👍 2K • 💬 162 • ⏱️ 17:08 • 1d ago

---

**[When Two AIs Go To War: A Realistic Scenario](https://www.youtube.com/watch?v=gwfCWDO4LbM)**

This is a scenario, but here are the sources for the real research referenced: ...

📺 Species | Documenting AGI

👁️ 98K • 👍 5K • 💬 926 • ⏱️ 35:15 • 1d ago

---

**[AI is Sending People into Psychosis](https://www.youtube.com/watch?v=LxmIIYj5FQE)**

AI chatbots are pulling people into delusions with devastating consequences. Sources: The Dark Addiction Patterns of Current AI ...

📺 Vanessa Wingårdh

👁️ 96K • 👍 6K • 💬 2K • ⏱️ 15:05 • 1d ago

---

**[Which Bed Would You Choose for a Dreamy Sleep? 🛏️✨ AI ASMR](https://www.youtube.com/watch?v=cSyLFn_R3Oo)**

Which Bed Would You Choose for a Dreamy Sleep? 🛏️✨ AI ASMR Relax and unwind after a long day with this dreamy AI ...

📺 PeaceHubASMR

👁️ 211K • 👍 241 • 💬 6 • ⏱️ 2:26 • 1d ago

---

**[My ai girlfrfiend part 2](https://www.youtube.com/watch?v=rjdix1lcwMo)**

Thanks for watching. Don't forget to like and subscribe! Featuring @DominiqueDanielle My Instagram ...

📺 NellyVidz

👁️ 46K • 👍 3K • 💬 144 • ⏱️ 8:51 • 1d ago

---

**[Transphobic AI is taking over Youtube...](https://www.youtube.com/watch?v=A-K_VXXnXnk)**

Yeah so it turns out that Youtube has an ai system that is UNAVOIDABLE and it keeps generating transphobic video ideas for ...

📺 NOAHFINNCE

👁️ 30K • 👍 4K • 💬 309 • ⏱️ 22:46 • 22h ago

---

**[AI News: ChatGPT Is Back, NotebookLM Update, Google AI Health Coach, New Pomelli Feature...](https://www.youtube.com/watch?v=myJ2IVHOfrI)**

Try i10x: https://i10x.ai/?fpr=paul53 Save 15% with code "PJL15" ChatGPT returns to form with a major model update while ...

📺 Paul J Lipsky

👁️ 41K • 👍 1K • 💬 96 • ⏱️ 21:51 • 2d ago

---

**[we JUST figured out how AI thinks](https://www.youtube.com/watch?v=Nn2eXwch-K0)**

The latest AI News. Learn about LLMs, Gen AI and get ready for the rollout of AGI. Wes Roth covers the latest happenings in the ...

📺 Wes Roth

👁️ 83K • 👍 3K • 💬 635 • ⏱️ 19:33 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Sulphur-2-base](https://huggingface.co/SulphurAI/Sulphur-2-base)**

*Sulphur*

Sulphur-2-base is an uncensored text-to-video and image-to-video generation model based on LTX 2.3, supporting various LTX 2.3 formats and featuring a prompt enhancer for improved results.

`text-to-video` `9.0B`

⬇️ 157,648 • ❤️ 594 • 2d ago

---

**[ZAYA1-8B](https://huggingface.co/Zyphra/ZAYA1-8B)**

*Zyphra*

ZAYA1-8B is an efficient Mixture-of-Experts LLM (760M active params) excelling in mathematical and coding tasks, competitive with larger models. It's suitable for on-device deployment and high-performance inference.

`8.8B`

⬇️ 66,119 • ❤️ 412 • 2d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, aiming to bridge the gap with closed-source models.

`text-generation` `861.6B`

⬇️ 2,017,835 • ❤️ 3,849 • 5d ago

---

**[HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)**

*HiDream.ai*

HiDream-O1-Image is a unified transformer-based image generation model capable of text-to-image, image editing, and subject-driven personalization at resolutions up to 2048x2048. It features a pixel-level unified transformer architecture without external VAEs or disjoint text encoders, enabling high-fidelity generation and precise control.

`image-text-to-image` `8.8B`

⬇️ 3,418 • ❤️ 222 • 1d ago

---

**[gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant)**

*Google*

Gemma 4 31B Dense is a multimodal LLM from Google DeepMind supporting text and image inputs with a 256K context window. It excels at reasoning, coding, and agentic tasks, offering optimized performance for low-latency applications via speculative decoding.

`any-to-any` `469.5M`

⬇️ 66,561 • ❤️ 204 • 10h ago

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

⬇️ 64,008 • ❤️ 216 • 17h ago

---

**[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)**

*Qwen*

Qwen3.6-27B is a 27B parameter causal language model with a vision encoder, excelling in agentic coding and reasoning tasks with a long context window (262k native). It supports image-text-to-text pipelines and features thinking preservation for iterative development.

`image-text-to-text` `27.8B`

⬇️ 2,446,478 • ❤️ 1,236 • 17d ago

---

**[gemma-4-26B-A4B-it-assistant](https://huggingface.co/google/gemma-4-26B-A4B-it-assistant)**

*Google*

Gemma 4 26B A4B is a multimodal instruction-tuned model supporting text and image inputs with a 256K context window. It excels in reasoning, coding, and agentic workflows, offering fast inference via its Mixture-of-Experts architecture with only 4B active parameters.

`any-to-any` `419.7M`

⬇️ 47,749 • ❤️ 111 • 10h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 64 • 💬 3 • ⭐ 73,456 • 16mo ago

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

▲ 18 • 💬 3 • ⭐ 10,715 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2604.17091) • [💻 code](https://github.com/lsdefine/GenericAgent)

---

**[DFlash: Block Diffusion for Flash Speculative Decoding](https://huggingface.co/papers/2602.06036)**

*Jian Chen, Yesheng Liang, Zhijian Liu*

🏢 Z Lab

DFlash is a speculative decoding framework that uses a lightweight block diffusion model for parallel token drafting, achieving significant speedup over existing autoregressive methods while maintaining high-quality outputs.

▲ 79 • 💬 7 • ⭐ 4,291 • 3mo ago

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

▲ 32 • 💬 3 • ⭐ 23,903 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[Flow-OPD: On-Policy Distillation for Flow Matching Models](https://huggingface.co/papers/2605.08063)**

*Zhen Fang, Wenxuan Huang, Yu Zeng et al. (11 authors)*

Flow-OPD addresses limitations in Flow Matching text-to-image models through a two-stage alignment approach combining on-policy distillation and manifold anchor regularization, achieving significant improvements in generation quality and alignment metrics.

▲ 72 • 💬 1 • ⭐ 67 • 3d ago

[🎓 arXiv](https://arxiv.org/abs/2605.08063) • [💻 code](https://github.com/CostaliyA/Flow-OPD) • [🔗 project](https://costaliya.github.io/Flow-OPD/)

---

**[ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration](https://huggingface.co/papers/2605.03042)**

*Ruofeng Yang, Yongcan Li, Shuai Li*

🏢 Shanghai Jiao Tong University

ARIS is an open-source research harness that uses cross-model adversarial collaboration to ensure reliable long-term research outcomes through coordinated execution, orchestration, and assurance layers.

▲ 105 • 💬 10 • ⭐ 8,757 • 7d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[HumanNet: Scaling Human-centric Video Learning to One Million Hours](https://huggingface.co/papers/2605.06747)**

*Yufan Deng, Daquan Zhou*

HumanNet presents a large-scale human-centric video dataset with rich annotations for embodied intelligence, demonstrating that egocentric human video can effectively replace robot data for training vision-language-action models.

▲ 39 • 💬 0 • ⭐ 58 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.06747) • [💻 code](https://github.com/DAGroup-PKU/HumanNet) • [🔗 project](https://dagroup-pku.github.io/HumanNet/)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 161 • 💬 2 • ⭐ 62,630 • 7mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

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

⭐ 11.5k • 🔱 756 • 20h ago

---

**[getagentseal/codeburn](https://github.com/getagentseal/codeburn)**

See where your AI coding tokens go. Interactive TUI dashboard for Claude Code, Codex, and Cursor cost observability.

`TypeScript` `ai-coding` `claude-code` `cli` `codex` `cost-tracking`

⭐ 6.1k • 🔱 468 • 17h ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 2.7k • 🔱 779 • 22h ago

---

**[Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)**

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Compose, Flutter, WordPress), Tailwind v4, Figma variables, shadcn/ui, CSS health audit, WCAG remediation, Chrome extension. MIT, Playwright, Node 20+.

`JavaScript` `accessibility` `agent-skill` `ai` `chrome-extension` `claude-code-plugin`

⭐ 2.5k • 🔱 222 • 1d ago

---

**[Mouseww/anything-analyzer](https://github.com/Mouseww/anything-analyzer)**

全能协议分析工具：浏览器抓包 + MITM 代理 + 指纹伪装 + AI 分析 + MCP Server 无缝对接 AI Agent/IDE   |  All-in-one protocol analysis toolkit — built-in browser capture, MITM proxy, JS hooks, fingerprint spoofing, AI analysis & MCP server for agent integration

`TypeScript` `2api` `ai-tools` `analysis-cli` `api-analysis` `automation-tools`

⭐ 2.4k • 🔱 490 • 1d ago

---

**[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)**

An open source harness for generating CAD models

`JavaScript` `3mf` `agents` `ai` `ai-agents` `build123d`

⭐ 2.4k • 🔱 282 • 1d ago

---

**[cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent)**

Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI or Telegram.

`TypeScript` `ai-agent` `ai-assistant` `llm`

⭐ 2.1k • 🔱 215 • 1d ago

---

**[bergside/design-md-chrome](https://github.com/bergside/design-md-chrome)**

Chrome extension to extract styles from any website and generate DESIGN.md files and design skills for AI based on TypeUI

`JavaScript` `ai` `chrome` `chrome-extension` `claude` `claude-design`

⭐ 1.9k • 🔱 238 • 17d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 1.9k • 🔱 113 • 1d ago

---

---

*Generated by PeekDeck - A glance is all you need*

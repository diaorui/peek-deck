---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-06-16T13:12:52.233541+00:00'
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

**Last Updated:** June 16, 2026 at 13:12 UTC  
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

**[AI Billionaires Want to Control EVERY Aspect of Your Life | Aaron Bastani Meets Karen Hao](https://www.reddit.com/r/artificial/comments/1u777te/ai_billionaires_want_to_control_every_aspect_of/)**

Keep the conversation going. Hopefully in a positive or informative manner that benefits us all.✌️

5h ago

---

**[What happens when frontier LLMs are deployed in rural Rwanda? Lessons on usefulness, language gaps, and incorrect answers [D]](https://www.reddit.com/r/artificial/comments/1u7a3ej/what_happens_when_frontier_llms_are_deployed_in/)**

At GiveDirectly, we recently ran a pilot in rural Rwanda that paired unconditional cash transfers with access to a general-purpose AI chatbot. One of the most interesting findings: people often used the chatbot as an always-available advisor—for business decisions, learning, and getting second opinions. But the pilot also exposed important limitations, including language gaps, locally irrelevant responses, and confidently incorrect answers. The writeup explores both sides: where participants found value, where the technology fell short, and what these experiences suggest about deploying frontier models in low-resource settings. Curious what the LLM community thinks: how should we evaluate models when local language support, contextual understanding, and reliability may matter more than benchmark performance? https://www.givedirectly.org/the-robots-work-at-night

2h ago

---

**[Built a Paninian Retrieval-Augmented Generation (PRAG) framework for safer medical AI — seeking feedback](https://www.reddit.com/r/artificial/comments/1u785o2/built_a_paninian_retrievalaugmented_generation/)**

Hi everyone, ​ I'm an independent AI/ML researcher and I've been working on a project called PRAG (Paninian Retrieval-Augmented Generation) for safety-critical medical AI. ​ The idea is to combine traditional RAG with a Paninian rule engine inspired by concepts such as Utsarga-Apavada, Paribhasha, Nitya-Anitya, and Antaranga-Bahiranga. The goal is not just better retrieval, but safer medical reasoning with full auditable rule traces. ​ Current findings: • 71% reduction in unsafe medical answers compared to standard RAG • Built on the MedQA dataset • Retrieval over 18 medical textbooks (~51k chunks) • Every decision includes an explainable rule trace ​ GitHub:https://github.com/yuvrajrajput/PRAG ​ I'm preparing my first arXiv submission in cs.AI. As a first-time independent researcher, I require an arXiv endorsement before submission. ​ I'd genuinely appreciate: ​ Technical feedback on the project Suggestions for improving the evaluation Guidance from researchers who have experience with arXiv submissions If someone familiar with the work believes it is suitable, advice regarding the endorsement process ​ Thanks for your time. I'm happy to share the paper draft and discuss the methodology in detail.

4h ago

---

**[Beautiful and the Superfluous: AI Labor Market and Basic Income](https://www.reddit.com/r/artificial/comments/1u7836w/beautiful_and_the_superfluous_ai_labor_market_and/)**

The architects of A.I. can picture a machine that will outperform us at everything—and cannot picture a human life beyond the paycheck.

🔗 [Kancelaria Prawna Skarbiec](https://kancelaria-skarbiec.pl/en/ai-labor-market-basic-income/) • 4h ago

---

**[Most attempts to reverse-engineer Fable 5 are missing the point](https://www.reddit.com/r/artificial/comments/1u7ckkn/most_attempts_to_reverseengineer_fable_5_are/)**

A lot of people are trying to reverse-engineer Fable 5 right now. Wrappers. Prompt packs. “Long-horizon agent” scaffolds. Tools that try to look like Fable from the outside. I think most of this is pointed in the wrong direction. If Fable 5 were just a prompt pattern or a wrapper, it would already be cloned. The real problem is not appearance. The real problem is robustness. Most coding agents look good at the start. Then the cracks show. - scope starts drifting - public tests become the finish line - edge cases don’t become regression tests - “verified” means vibes, not evidence - the final turn exits too early - long loops slowly lose the actual task So we built Hephaestus Stormbreaker. Stormbreaker is not a new model. It is not a Fable 5 clone. It is not another benchmark-wrapper cosplay project. Stormbreaker is a robustness control layer for coding agents. It forces the agent to: - lock scope - lock the plan - run an evidence loop - derive regression tests from the issue - separate public test passing from private-oracle validation - pass a final gate before stopping In other words, it is not trying to make an agent “look smarter.” It is trying to make the agent harder to derail. The results point in that direction. On raw correctness alone, Stormbreaker does not get to claim a clean win. That is not the point. Native Codex is already strong on short local coding tasks. The difference appears when you measure operational robustness. Average verification macro score: - Native Codex: 76.48 - Hephaestus Network Baseline: 92.22 - Hephaestus Stormbreaker: 99.26 The metric sensitivity analysis is the important part. Correctness-only metrics reject the Stormbreaker superiority claim. Good. But all 6 process-aware operational metrics preserve the same ordering: Native < Baseline < Stormbreaker We also ran paired task-unit validation so repeated runs are not treated as fake independent samples. The local operational ladder still held. My take: If you want to “reverse-engineer Fable 5,” stop copying the surface. Build the layer that prevents the agent from drifting, skipping evidence, ignoring regressions, and quitting early. The model race will continue. But real engineering work needs agents that can stay inside scope, preserve evidence, verify their own output, and finish cleanly. That is what Hephaestus Stormbreaker is for.

24m ago

---

**[Would you pay for an independent alert service that tells you when an LLM's behaviour has drifted - before your users notice?](https://www.reddit.com/r/artificial/comments/1u7ahgm/would_you_pay_for_an_independent_alert_service/)**

Following up on a thread I posted yesterday about how developers detect LLM API degradation. The responses were useful enough that I want to validate a specific idea. It is a 3 layer independent alert service: Layer 1: Transport health alerts: Independent probes checking TTFT, error rates, and latency across major models (Claude Sonnet, GPT-4o, Gemini, Grok) every 5 minutes. Alerts you before the provider's status page updates. This part already exists and is free at tickerr - the question is whether people would pay for push alerts. Layer 2: Capability drift alerts: A fixed canary suite that runs on a schedule and detects when a model's output behaviour has shifted, things like whether it still follows formatting instructions, whether JSON outputs are still well-formed, whether reasoning quality has changed. A drift score per model, with an alert when the score drops meaningfully from the baseline. Layer 3: (optional add-on and phase 2): Bring your own prompts. You give us 5-10 prompts that are critical to your specific use case, we run them on a schedule and alert you if the outputs drift from your established baseline. Your prompts stay private. Three specific questions: Do you think this is a useful service and would you be willing to pay for this? Anything else you think would make it more useful or should be included in the checks? What would you pay for this as a monthly service? (Ballpark is fine, even "nothing, I'd build this myself" is useful.) If none of this is a problem you'd pay to solve, that's also fine and would save a lot of my time. 😄

2h ago

---

**[I have 3,000 photos and videos in OneDrive. How can I organise them with AI?](https://www.reddit.com/r/artificial/comments/1u776hy/i_have_3000_photos_and_videos_in_onedrive_how_can/)**

Looking for a bit of advice because I feel like I’m missing something obvious. Over the last few weeks I’ve finally consolidated my photo library and got everything into OneDrive. I’ve now got two folders: Photos Videos Between them there’s around 3000 files in total. The files go back years and are a mix of family photos, holidays, screenshots, random phone pictures etc. I’ve been trying to use AI to help me organise everything properly. Things like: - Finding duplicates and near-duplicates - Identifying people - Grouping photos from the same trip or event - Creating folders/albums automatically - Tagging photos so they’re searchable - Picking out the best photos and obvious rubbish - Suggesting a sensible folder structure I initially thought ChatGPT might be able to help, but I’ve quickly hit a wall because I couldn’t work out a practical way to give it access to thousands of files sitting in OneDrive. I tried to connect it to OneDrive and just kept getting an error. This is where I start getting lost. I keep seeing people talk about agents, MCPs, local models and automation workflows. I’ve done a bit of reading, but if I’m honest I don’t really understand how those pieces fit together or how I’d actually use them myself. I have a rough idea what an MCP is, but nowhere near enough knowledge to build anything from scratch. I’m reasonably technical, but I’m not a developer. I’m happy to learn and tinker, but I’d prefer something a beginner could realistically get running without spending weeks building infrastructure. My setup is: Windows laptop i7-10750H 32GB RAM Nvidia Quadro P620 Everything stored in OneDrive Ideally I’d like to keep costs as close to zero as possible. I have a ChatGPT plus subscription. If this was your photo library, what would you actually do in 2026? Is there a beginner-friendly AI workflow for this, or am I looking at completely the wrong type of tool? And if the answer is “don’t use an agent for this, use something else”, I’m completely open to that too. Any advice appreciated.

5h ago

---

**[AI makes me faster. And less myself...](https://www.reddit.com/r/artificial/comments/1u6bha1/ai_makes_me_faster_and_less_myself/)**

Since ChatGPT came out I've been using LLMs every day for work. And I've slowly become a worse thinker. Not in the sense that I work less. In the sense that I reason less. Some decisions don't feel like mine anymore... I got there, but I didn't really work through them. Sometimes I catch myself not pushing back on the AI output even when something is off. Turns out there's a name for this: Cognitive Offloading. It's not inherently bad: we've always offloaded cognitive tasks to external tools (notes, calculators, GPS). The problem is when you start relying too much on AI that you offload the reasoning itself, not just the execution. My job is to facilitate the AI adoption inside companies across the industries (automotive, finance, consulting, ...): What I see are people who delegate their thought processes to AI and end up disconnected from the conclusions they just reached but they still approve the results. So I want to know if this is widespread or just me. If you like to contribute, here is a short survey (2 min) to understand whether this is a real pain for others or it is just me: https://forms.gle/TaWrEnYRyfaCoF166 I'll share the results openly here. And if there's enough signal, I'm thinking about building something around it, a tool that helps you work with AI without losing track of your own reasoning. Does this resonate with anyone?

1d ago

---

**[The beautiful ugly shape](https://www.reddit.com/r/artificial/comments/1u7c1po/the_beautiful_ugly_shape/)**

The whole system has a clean architecture: X supplies the public behavioral graph. Premium/Premium+ supplies a paid, high-signal user cohort. Grok supplies the private conversational layer. Image/video generation supplies visual preference data. Voice/personality/companion features lower inhibition and increase intimacy. Ads/subscriptions/enterprise/government/API monetize the resulting platform. The S-1 (SpaceX's IPO filing) calls X a distribution and data engine and describes AI-driven targeting, user intent, and Grok/X integration. At this point it stops looking like a theory and starts looking like a floor plan someone accidentally left in public. The filing does not need to say “we are using Grok to psychologically profile users.” It describes the machine around it. The studies describe the human behavior inside it. The product design connects the two. And the subscriber numbers show the distribution trick: Grok was not simply bought by standalone AI customers. It was gifted/bundled into X Premium/Premium+, pushed to a high-value paid user layer, and made available at massive scale beyond the paid base. That is the point. The user was never just the customer. The user was the product, the training signal, the targeting surface, and the behavioral dataset.

48m ago

---

**[Nobody’s talking about the real precedent in the Fable 5 ban: a nationality-based access rule that geography literally can’t enforce](https://www.reddit.com/r/artificial/comments/1u6lqp6/nobodys_talking_about_the_real_precedent_in_the/)**

TL;DR: Last Friday the US government ordered Anthropic to block all “foreign nationals” — including non-citizens inside the US — from using its new Fable 5 and Mythos 5 models. Since you can’t separate a green-card holder in California from a citizen in real time, Anthropic shut the models down for everyone. It’s the first time export controls have hit an AI model itself rather than the chips that run it. The under-discussed part: a nationality-based access rule that geography can’t enforce pushes companies toward building identity infrastructure — and your AI chats already have zero legal privilege. Even if this order gets reversed, the precedent is the story. What actually happened On June 12, the Commerce Department issued a national-security export-control directive ordering Anthropic to suspend access to Fable 5 (and the more powerful Mythos 5 it’s built on) for any foreign national — explicitly including non-citizens physically inside the US, down to Anthropic’s own employees. A source close to the company says it got ~90 minutes and no prior warning. Because Anthropic can’t filter foreign nationals from US users in real time, it disabled both models globally. The trigger, per WSJ, Axios, and Semafor reporting: a phone call from Amazon. Amazon CEO Andy Jassy reportedly told Treasury Secretary Scott Bessent and other officials that Amazon researchers had used Fable 5 to pull information useful for cyberattacks. That’s the same Amazon that’s Anthropic’s biggest investor (~$13B in, ~$20B more planned), its cloud and chip supplier, and a customer — and now the entity that got its own investment’s flagship product killed worldwide. Amazon won’t confirm details. At least five other companies reportedly called the administration that same window. The accounts conflict, which matters: • White House (via former AI czar David Sacks): a trusted partner found a real jailbreak, the administration asked Anthropic to patch or pull it, CEO Dario Amodei refused, so they acted “reluctantly” — and they want the model back once it’s fixed. • Anthropic: the “jailbreak” only surfaced a handful of already-known minor vulnerabilities that other public models like GPT-5.5 can find too, so recalling a model used by hundreds of millions is disproportionate. • A cybersecurity CEO who reviewed the findings said the research was defensive, not offensive. Why this is bigger than one model Export controls have hit AI chips for years. This is the first time they’ve hit a model itself. That reframes frontier models as controlled national-security assets — and it surfaces an enforcement problem nobody’s reckoning with. A normal “no users in Country X” rule is easy: geoblock by IP. But this rule covers foreign nationals inside the US. You cannot IP-block a French citizen sitting in San Francisco. So if a future order like this is meant to be enforced strictly — not “shut it all down,” but “keep serving Americans while genuinely excluding non-citizens” — there’s only one way to be certain who’s a citizen: verify identity. Self-attestation (“I certify I’m a US person”) shifts legal liability but provides zero actual certainty, because people lie. If the government’s bar is certainty, the only escape hatch from “go dark forever” is ID verification to access the model. That’s the precedent worth staring at: a category of rule whose strict form quietly makes “show ID to use AI” the path of least resistance. The part that’s already settled: your AI chats have no legal privilege This one isn’t speculative. In February, a federal judge in the Southern District of New York ruled that conversations with Claude carry no attorney-client privilege — Claude isn’t a lawyer, so the privilege can’t attach — and leaned on Anthropic’s own privacy policy stating users have no expectation of privacy in their inputs. Sam Altman has publicly admitted the same about ChatGPT. A separate ruling found ~20 million ChatGPT logs likely subject to compelled production, with users holding only a “diminished privacy interest.” (One Michigan judge went the other way, treating chats as personal work-product — so it’s trending bad, not fully locked in.) Now stack the two: AI access potentially gated to verified identities, and AI conversations that can be subpoenaed with no privilege. That’s a plausible near-future where using AI means an ID-linked, fully discoverable record of everything you ever asked it. The honest counterweights (so this isn’t catastrophizing) • The administration says it wants the model restored once the jailbreak is patched. The likeliest near-term outcome is the directive getting narrowed or pulled — not permanent ID walls. • Self-attestation is the historically normal compliance path for export-controlled software and doesn’t require collecting documents. • The last time the US tried to export-control software like this — strong encryption in the 1990s — the controls largely failed and were circumvented and relaxed rather than hardening into a verification regime. Developers reportedly already reproduced Fable’s capabilities on the still-available Opus 4.8 with a single line of code. So this specific fight will probably resolve. The reason to care isn’t this week — it’s that the legal machinery and the precedent now exist, and they don’t disappear when the model comes back. The actual question If “frontier AI model” is now something the government can pull off the market via export control, and the cleanest way to comply with a nationality-based access rule is identity verification — is mandatory ID to use advanced AI just a matter of time? Or does the encryption-wars history (controls that collapsed) suggest this is unenforceable theater? Curious where people land. Sources • Anthropic’s statement on the directive: https://www.anthropic.com/news/fable-mythos-access • Axios — how Amazon and the White House ended Fable: https://www.axios.com/2026/06/13/anthropic-amazon-white-house • TechCrunch — Amazon CEO raised concerns before the crackdown: https://techcrunch.com/2026/06/13/amazon-ceo-reportedly-raised-anthropic-model-concerns-before-government-crackdown/ • TIME — first export control on a model, and the precedent: https://time.com/article/2026/06/13/anthropic-fable-mythos-ban-US-security/ • Coverage of the SDNY no-privilege ruling: https://www.crowell.com/en/insights/client-alerts/federal-court-rules-some-ai-chats-are-not-protected-by-legal-privilege-what-it-means-for-you

20h ago

---

---

## Google News: "ai"

**[SpaceX to buy AI coding startup Cursor for $60 billion in enterprise push](https://finance.yahoo.com/technology/ai/articles/spacex-buy-cursor-ai-coding-103445855.html)**

Elon Musk's SpaceX said on Tuesday it would acquire Anysphere, the software firm behind the popular AI coding agent Cursor, for $60 billion, in a bid to ramp up its presence ‌in the enterprise AI market.  The announcement comes days after Musk took the rockets-to-AI company public in a ‌blockbuster Nasdaq debut that valued the firm at more than $2 trillion and immediately made it one of the world's most valuable companies.  SpaceX had been ​eyeing Cursor for several months.

Yahoo Finance • 2h ago

---

**[SpaceX locks in $60 billion Cursor deal to power AI coding push](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/)**

Reuters • 1h ago

---

**[SpaceX buys AI coding startup Cursor for $60 billion](https://www.nbcnews.com/tech/tech-news/spacex-buys-ai-coding-startup-cursor-60-billion-rcna350262)**

Cursor, which started in 2022, helped sparked a trend called “vibe coding” as AI coding assistants have become increasingly capable of doing the work of computer programming.

NBC News • 30m ago

---

**[Qualcomm Is a Rare AI Chip Value Play](https://www.wsj.com/tech/qualcomm-is-a-rare-ai-chip-value-play-3e09f70b)**

WSJ • 3h ago

---

**[The White House Is Ratcheting Up Its War Against Anthropic](https://www.theatlantic.com/technology/2026/06/trump-anthropic-export-control-ai-race/687555/)**

This is how America loses the AI race.

The Atlantic • 16h ago

---

**[The Anthropic ‘Fable’ saga proves: we have opened the AI Pandora’s box. What now?](https://www.theguardian.com/commentisfree/2026/jun/16/anthropic-fable-ai)**

We have opened the AI Pandora’s box. Now we have to make the best of it

The Guardian • 1h ago

---

**[Anthropic export ban sounds alarms for AI industry](https://www.axios.com/2026/06/16/ai-anthropic-export-controls)**

Axios • 11m ago

---

**[Letters to the Editor: To combat AI cheating, colleges should go back to basics for exams](https://www.latimes.com/opinion/letters-to-the-editor/story/2026-06-16/colleges-ai-cheating-exams)**

'Require all students to show up in person to the classroom with an empty "blue book" and write their exam answers in cursive,' writes an L.A. Times reader.

Los Angeles Times • 12m ago

---

**[Property Play: AI determining home prices](https://www.cnbc.com/video/2026/06/16/property-play-ai-determining-home-prices.html)**

CNBC's Diana Olick reports on AI's growing influence on housing transactions for buyers and sellers.

CNBC • 19m ago

---

**[A.I. Boom Ignites Asian Chip Companies](https://www.nytimes.com/2026/06/16/technology/taiwan-south-korea-ai-chips.html)**

The New York Times • 4h ago

---

---

## HackerNews: "ai"

**[Not everyone is using AI for everything](https://news.ycombinator.com/item?id=48527700)**

People are consuming AI like they eat meat: some are embracing it, some are limiting their use of it, and some are avoiding it altogether.

⬆️ 505 • 💬 540 • 1d ago • [gabrielweinberg.com](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they)

---

**[Police officer investigated for using AI to 'create evidence' in multiple cases](https://news.ycombinator.com/item?id=48520807)**

⬆️ 392 • 💬 193 • 2d ago • [news.sky.com](https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661)

---

**[AI coding at home without going broke](https://news.ycombinator.com/item?id=48518969)**

There are three ways to do AI coding at home without spending like a company, and which one fits depends mostly on how much you trust the next year of hardwa...

⬆️ 349 • 💬 288 • 2d ago • [stephen.bochinski.dev](https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/)

---

**[My Homelab AI Dev Platform](https://news.ycombinator.com/item?id=48542433)**

Self-hosting OpenCode Web for GitOps style homelab changes.

⬆️ 331 • 💬 54 • 22h ago • [rsgm.dev](https://rsgm.dev/post/ai-dev-platform/)

---

**[AI is code – and can't be prompted into being smarter](https://news.ycombinator.com/item?id=48532178)**

From Java tests to Shai-Hulud, bots keep proving they'll swallow anything you feed them

⬆️ 158 • 💬 141 • 1d ago • [theregister](https://www.theregister.com/ai-and-ml/2026/06/14/ai-is-code-and-cant-be-prompted-into-being-smarter/5254141)

---

**[Microsoft turns to AWS as GitHub faces AI capacity crunch](https://news.ycombinator.com/item?id=48549918)**

Microsoft is adding AWS capacity for GitHub after AI-driven usage strained the developer platform, exposing Azure constraints and the infrastructure cost of agentic coding.

⬆️ 153 • 💬 68 • 10h ago • [RuntimeWire](https://runtimewire.com/article/microsoft-github-aws-ai-capacity-crunch)

---

**[KPMG pulls report on AI usage due to apparent hallucinations](https://news.ycombinator.com/item?id=48527297)**

Once again, AI proves to be an unreliable source of information about AI.

⬆️ 153 • 💬 32 • 1d ago • [TechCrunch](https://techcrunch.com/2026/06/13/kpmg-pulls-report-on-ai-usage-due-to-apparent-hallucinations/)

---

**[Show HN: I wrote a C++ ray tracer from scratch without AI](https://news.ycombinator.com/item?id=48538833)**

C++ Path Tracer from scratch with zero third-party libraries. - themartiano/luz

⬆️ 148 • 💬 64 • 1d ago • [GitHub](https://github.com/themartiano/luz)

---

**[Can Europe train a frontier AI model on the compute it owns?](https://news.ycombinator.com/item?id=48541014)**

A sourced model and short report: can Europe train a sovereign frontier AI model on the public compute it already owns, while gigawatt datacenters wait years for grid power? - sammysltd/euromesh

⬆️ 135 • 💬 268 • 23h ago • [GitHub](https://github.com/sammysltd/euromesh)

---

**[SpaceX to buy Cursor AI coding agent operator Anysphere for $60B](https://news.ycombinator.com/item?id=48553224)**

⬆️ 134 • 💬 86 • 2h ago • [reuters.com](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/)

---

---

## YouTube Videos: "ai"

**[First Meeting with Elon Musk&#39;s New AI Robot That Looks Like a Real Human](https://www.youtube.com/watch?v=TttOAYZDUKo)**

Elon Musk's new AI robot is designed to blur the line between humans and machines by combining advanced artificial intelligence ...

📺 Carros Show

👁️ 4K • 👍 148 • 💬 16 • ⏱️ 21:06 • 17h ago

---

**[Google Just Revealed What Comes After AGI And It’s Shocking](https://www.youtube.com/watch?v=haB_od-xCWY)**

Google DeepMind just dropped a massive paper called From AGI to ASI, and the message is bigger than another AI release.

📺 AI Revolution

👁️ 46K • 👍 2K • 💬 231 • ⏱️ 13:33 • 14h ago

---

**[AI buys robot and car, does exactly what experts warned.](https://www.youtube.com/watch?v=IPaMKTb5csQ)**

AI buys a Robot. Could AI become dangerous? Can we trust AI. Go to http://ground.news/InsideAI for a better way to stay informed.

📺 InsideAI

👁️ 499K • 👍 17K • 💬 2K • ⏱️ 15:10 • 1d ago

---

**[Has ANYONE Actually Seen AI Work?](https://www.youtube.com/watch?v=UR3F3N9K-xw)**

How I Became a Sovereign Professional - The Freelance Formula https://www.brendandell.com/freelance-formula-299 Currently ...

📺 Brendan Dell 

👁️ 36K • 👍 2K • 💬 572 • ⏱️ 18:34 • 22h ago

---

**[They Just Decoded The Rosetta Stone With AI — And What It Reveals Is Not Good...](https://www.youtube.com/watch?v=i0CI28b81eo)**

They Just Decoded The Rosetta Stone With AI — And What It Reveals Is Not Good... The Rosetta Stone was the key to ...

📺 The Ultimate Discovery

👁️ 5K • 👍 120 • 💬 2 • ⏱️ 20:20 • 1d ago

---

**[ALERT: Nadella’s Brutal Warning &quot;AI Is About to Hollow Out Entire Industries&quot;](https://www.youtube.com/watch?v=mczINsa2WX0)**

Microsoft CEO Satya Nadella just shattered the biggest illusion in tech. While everyone else is arguing over who has the smartest ...

📺 AIM Network

👁️ 37K • 👍 705 • 💬 61 • ⏱️ 6:05 • 22h ago

---

**[Google’s AI Bet](https://www.youtube.com/watch?v=zdp7IAwV064)**

Google is making the biggest change to its search business in more than two decades, integrating AI-generated answers, ...

📺 Bloomberg Television

👁️ 50K • 👍 934 • 💬 127 • ⏱️ 11:57 • 2d ago

---

**[3 Easiest Ways to Make Money with Claude AI (Nobody&#39;s Talking About)](https://www.youtube.com/watch?v=QIUW3t4aTTE)**

This is 3 Easiest Ways to Make Money with Claude AI That Nobody's Talking About Full Blog Breakdown (Prompts + Tools ...

📺 Mr. AI CASH

👁️ 16K • 👍 845 • 💬 142 • ⏱️ 11:44 • 21h ago

---

**[Your $20 AI Plan Costs Them Thousands. That&#39;s Not The Bubble.](https://www.youtube.com/watch?v=mn4XBSBIuag)**

My Links Newsletter: https://natesnewsletter.substack.com/ X: https://x.com/natebjones TikTok: ...

📺 AI News & Strategy Daily | Nate B Jones

👁️ 27K • 👍 920 • 💬 165 • ⏱️ 19:25 • 23h ago

---

**[This Is Bad... They Just Shut Down FABLE 5](https://www.youtube.com/watch?v=1e4D6ukN0QY)**

Anthropic's Fable 5 was live for only three days before everything changed. The US government stepped in, access to Fable 5 and ...

📺 AI Revolution

👁️ 32K • 👍 1K • 💬 287 • ⏱️ 12:49 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[gemma-4-12B-coder-fable5-composer2.5-v1-GGUF](https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF)**

*Yuxin Lu*

A 12B parameter GGUF model fine-tuned on verifiable Python coding data with chain-of-thought reasoning, designed for local execution on consumer hardware (~4.5GB VRAM minimum) for offline coding assistance and problem-solving.

`text-generation` `11.9B`

⬇️ 60,921 • ❤️ 939 • 1h ago

---

**[diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it)**

*Google*

DiffusionGemma 26B A4B-it is a multimodal, instruction-tuned generative model that uses discrete text diffusion for high-speed text generation from text, image, and video inputs. It excels at tasks requiring rapid inference, long context understanding (up to 256K tokens), and multimodal reasoning, making it suitable for applications like advanced chatbots, content creation, and complex document analysis.

`image-text-to-text` `25.8B`

⬇️ 375,974 • ❤️ 922 • 5d ago

---

**[MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)**

*MiniMax*

MiniMax-M3 is a native multimodal model with 1M context, excelling in image-text-to-text tasks. It features MiniMax Sparse Attention (MSA) for efficient long context processing and demonstrates frontier-level performance in coding and agentic benchmarks.

`image-text-to-text` `427.0B`

⬇️ 25,064 • ❤️ 980 • 7h ago

---

**[Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)**

*Moonshot AI*

Kimi K2.7 Code is a 1T parameter Mixture-of-Experts (MoE) model optimized for complex, long-horizon coding tasks and software engineering workflows. It features a 256K context length and a MoonViT vision encoder, excelling in agentic coding capabilities with improved token efficiency.

`image-text-to-text` `1058.6B`

⬇️ 102,206 • ❤️ 773 • 1d ago

---

**[LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)**

*NVIDIA*

LocateAnything-3B is a vision-language model for fast and high-quality visual grounding, enabling precise object localization and detection from text prompts using Parallel Box Decoding. It excels in diverse use cases like referring expression grounding, GUI element localization, and robotics perception.

`image-text-to-text` `3.8B`

⬇️ 98,698 • ❤️ 2,078 • 4d ago

---

**[North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)**

*Cohere Labs*

North Mini Code 1.0 is a 30B-3B parameter research model optimized for code generation and agentic software engineering, featuring a 256K context length and tool-use capabilities for terminal tasks.

`text-generation` `30.5B`

⬇️ 12,129 • ❤️ 401 • 1d ago

---

**[Rio-3.5-Open-397B](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B)**

*Prefeitura do Rio de Janeiro (City of Rio de Janeiro)*

Rio 3.5 Open 397B is a frontier-class, open-source image-text-to-text AI model post-trained from Qwen 3.5 397B. It excels in agentic coding, STEM, multilingual tasks, and multimodal reasoning, featuring a 1M context window and SwiReasoning for enhanced accuracy and efficiency.

`image-text-to-text` `403.4B`

⬇️ 189,744 • ❤️ 308 • 1d ago

---

**[diffusiongemma-26B-A4B-it-GGUF](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)**

*Unsloth AI*

DiffusionGemma-26B-A4B-it-GGUF is a 26B MoE multimodal generative model that produces text output from text, image, and video inputs using discrete diffusion. Optimized for speed and deployability, it leverages Gemma 4 architecture advancements for efficient token generation.

`image-text-to-text` `25.3B`

⬇️ 120,435 • ❤️ 280 • 3d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 2,716,651 • ❤️ 1,870 • 2mo ago

---

**[gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)**

*Google*

Gemma 4 12B Unified is a multimodal LLM with native audio and vision understanding, supporting text, image, and audio inputs with a 256K context window. It features an encoder-free architecture optimized for local execution and advanced reasoning, coding, and agentic capabilities.

`any-to-any` `12.0B`

⬇️ 1,223,383 • ❤️ 1,044 • 12d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 233 • 💬 4 • ⭐ 7,471 • 25d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 97 • 💬 4 • ⭐ 86,537 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 41 • 💬 4 • ⭐ 30,363 • 10mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[FastContext: Training Efficient Repository Explorer for Coding Agents](https://huggingface.co/papers/2606.14066)**

*Shaoqiu Zhang, Maoquan Wang, Yuling Shi et al. (8 authors)*

🏢 Microsoft

FastContext separates repository exploration from code solving in LLM agents using specialized exploration models that reduce token consumption and improve resolution rates.

▲ 47 • 💬 2 • ⭐ 312 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2606.14066) • [💻 code](https://github.com/microsoft/fastcontext) • [🔗 project](https://huggingface.co/microsoft/FastContext-1.0-4B-SFT)

---

**[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**

*Xingyao Wang, Boxuan Li, Yufan Song et al. (24 authors)*

OpenDevin is a platform for developing AI agents that interact with the world by writing code, using command lines, and browsing the web, with support for multiple agents and evaluation benchmarks.

▲ 80 • 💬 7 • ⭐ 77,320 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2407.16741) • [💻 code](https://github.com/opendevin/opendevin)

---

**[PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://huggingface.co/papers/2606.03264)**

*Zelun Zhang, Hongen Liu, Suyin Liang et al. (15 authors)*

🏢 PaddlePaddle

PaddleOCR-VL-1.6 enhances document parsing performance through targeted data optimization and progressive post-training techniques, achieving state-of-the-art results on OmniDocBench v1.6.

▲ 16 • 💬 1 • ⭐ 82,375 • 14d ago

[🎓 arXiv](https://arxiv.org/abs/2606.03264) • [💻 code](https://github.com/PaddlePaddle/PaddleOCR) • [🔗 project](https://www.paddleocr.com)

---

**[LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://huggingface.co/papers/2510.09665)**

*Yuhan Liu, Yihua Cheng, Jiayi Yao et al. (11 authors)*

LMCACHE enables efficient KV cache management for large language models by storing caches outside GPU memory, supporting cache reuse across queries and inference engines while achieving significant throughput improvements.

▲ 5 • 💬 0 • ⭐ 9,141 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2510.09665) • [💻 code](https://github.com/LMCache/LMCache)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 58 • 💬 1 • ⭐ 83,030 • 33mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[MinerU2.5: A Decoupled Vision-Language Model for Efficient
  High-Resolution Document Parsing](https://huggingface.co/papers/2509.22186)**

*Junbo Niu, Zheng Liu, Zhuangcheng Gu et al. (61 authors)*

MinerU2.5, a 1.2B-parameter document parsing vision-language model, achieves state-of-the-art recognition accuracy with computational efficiency through a coarse-to-fine parsing strategy.

▲ 166 • 💬 2 • ⭐ 67,655 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.22186) • [💻 code](https://github.com/opendatalab/MinerU) • [🔗 project](https://opendatalab.github.io/MinerU/)

---

**[SIA: Self Improving AI with Harness & Weight Updates](https://huggingface.co/papers/2605.27276)**

*Prannay Hebbar, Yogendra Manawat, Samuel Verboomen et al. (7 authors)*

🏢 Hexo AI

A self-improving AI framework simultaneously updates both model weights and task-specific agent architecture through a language-model feedback agent across legal classification, GPU optimization, and biological data denoising tasks.

▲ 14 • 💬 2 • ⭐ 1,734 • 21d ago

[🎓 arXiv](https://arxiv.org/abs/2605.27276) • [💻 code](https://github.com/hexo-ai/sia) • [🔗 project](https://hexolabs.com/)

---

---

## GitHub Repositories: "ai"

**[pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus)**

Self-hosted AI workspace. 

`Python`

⭐ 72.2k • 🔱 9.2k • 1h ago

---

**[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)**

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

`JavaScript` `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin`

⭐ 20.7k • 🔱 870 • 1h ago

---

**[KunAgent/Kun](https://github.com/KunAgent/Kun)**

AI agent workspace with Code and Write modes built into your application.

`TypeScript`

⭐ 4.3k • 🔱 375 • 5m ago

---

**[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)**

Task-oriented AI Agent productivity platform

`TypeScript`

⭐ 3.4k • 🔱 355 • 5h ago

---

**[nexu-io/html-video](https://github.com/nexu-io/html-video)**

Programmatic video for coding agents — HTML to video on your laptop. Turn HTML, CSS & data into real MP4s with pluggable render engines, 21 templates, AI soundtrack. Apache-2.0, no per-render fees. An official project by the Open Design team.

`HTML` `ai-agent` `apache-2` `coding-agent` `css` `ffmpeg`

⭐ 3.2k • 🔱 385 • 4d ago

---

**[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)**

A meta-harness for all your AI agents.  Omnigent provides a common layer over Claude Code, Codex, Pi, and the agents you write yourself: swap or combine harnesses without rewriting, keep them in check with policies and sandboxing, and collaborate in real time on the same live session, from any device.

`Python` `agents` `ai` `ai-agents` `developer-tools` `llm`

⭐ 2.3k • 🔱 277 • 6m ago

---

**[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)**

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

`Python`

⭐ 2.1k • 🔱 186 • 7d ago

---

**[Doorman11991/smallcode](https://github.com/Doorman11991/smallcode)**

AI coding agent optimized for small LLMs. 87% benchmark with 4B-active model.

`JavaScript`

⭐ 1.9k • 🔱 139 • 11d ago

---

**[basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas)**

面向 AI 创作的开源无限画布工作台，集成 AI 生图、参考图编辑、视频生成、Agent 智能助手、画布编排、对话创作、提示词库与素材管理等能力，支持可视化创作流程与多 Agent 协同工作。兼容 OpenAI 接口生态，支持 chatgpt2api、grok2api、flow2api、newapi 等渠道接入。

`TypeScript`

⭐ 1.6k • 🔱 397 • 2h ago

---

**[jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo)**

JoyAI-Echo: Pushing the Frontier of Long Audio-Visual Generation

`Python`

⭐ 1.6k • 🔱 138 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*

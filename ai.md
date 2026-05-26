---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-26T18:41:50.617467+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- social
- videos
- repositories
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 26, 2026 at 18:41 UTC  
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

**[Which AI image generator is actually worth the money?](https://www.reddit.com/r/artificial/comments/1to5v3m/which_ai_image_generator_is_actually_worth_the/)**

I've looked at about a dozen different image generators: Nano Banana Flux Midjourney GPT Image 2 Firefly Ideogram Recraft Leonardo Canvas Meta AI They all have their pluses and minuses but they all do a decent job. If I'm looking to spend thousands over a year on an image generator, what would you suggest. This would be mainly for business and a little for art.

5h ago

---

**[AI is becoming epistemic infrastructure controlled by a handful of private individuals?](https://www.reddit.com/r/artificial/comments/1to0dmn/ai_is_becoming_epistemic_infrastructure/)**

Most people treat AI as a convenient black box. Ask it something, it answers, you move on. But we’re sleepwalking into something bigger. I think Whoever controls the infrastructure of knowledge controls how people perceive reality. The Church held that position for centuries through controlling scripture. The printing press broke that monopoly by distributing interpretive power. AI is doing the opposite recentralizing it into a handful of corporations with no democratic accountability. “AI says X” is structurally identical to “studies show X” you’re invoking an authority you can’t directly access. Except with a study you can theoretically trace the source. With AI the chain is opaque by design. And it delivers wrong answers and right answers with identical confidence. There’s no texture to signal doubt. AI isn’t neutral, it’s being heavily calibrated. In the west, the models are trained to be more “ethical” maybe more liberal and always try to give you a more “balance” take on things. Chinese AI simply doesn’t allow you to access to anything that put the CCP is a bad light. The more you rely on AI in domains where you lack expertise, the less capable you become of evaluating whether to trust it. AI works best for people who already know enough to catch its errors the opposite of how most people use it. Imagine the next generation of people growing up and being shaped by these AI. I can’t help but feel nervous and scared for the future. OpenAI said 10% of our entire population has already started using chatgpt. Regardless of the accuracy of this number, I feel like we are slowly entering into a mass hallucination / blind reliance on these AI models. We’re not just offloading cognitive effort. We’re handing the dial over who shapes how billions of people understand reality to a small group of unelected, largely unregulated private individuals.

10h ago

---

**[Uber's COO says it's getting harder to justify the money spent on AI tokenmaxxing](https://www.reddit.com/r/artificial/comments/1tndgv8/ubers_coo_says_its_getting_harder_to_justify_the/)**

Operations chief Andrew Macdonald said he's not seeing proportional productivity gains from increasing AI costs within Uber.

🔗 [Business Insider](https://www.businessinsider.com/uber-coo-andrew-macdonald-ai-token-spending-harder-justify-2026-5) • 1d ago

---

**[Memory Curator Agent a governance layer for memory in multi-agent systems](https://www.reddit.com/r/artificial/comments/1to9p3u/memory_curator_agent_a_governance_layer_for/)**

I keep seeing the same failure in every multi-agent setup I touch. Memory looks fine on day one. By week three it is half stale facts, half private context that should not have been written publicly, and half decisions that were superseded but never overwritten. Retrieval gets noisier. Users keep repeating context because the right fact ended up in the wrong scope. The recursion limit is not the problem here. The memory store itself is the problem. The thing I changed that helped most was the simplest possible rule. Worker agents are not allowed to write to durable memory. They emit a structured memory event with a proposed scope and evidence, and a separate Memory Curator agent decides whether to write it, where to write it, or to discard it. The four scopes I route into are agent repo memory (durable design rules for one agent), agent team memory (cross-agent procedures, handoff standards, safety rules), project memory (current state, decisions, risks for one engagement), and session scratch (temporary observations that probably should not survive). The mapping I had in mind was to organizational and human memory categories: individual specialist memory, transactive team memory (Ren and Argote), project memory, and short-term working memory. The routing rule is conservative on purpose. If an event is temporary, unsupported, ambiguous, or contains private context, it goes to session scratch or gets discarded outright. Durable memory has to be earned. The schema is JSON with tagged fields for fact, decision, preference, risk, procedure, and hypothesis, plus an evidence reference and a proposed scope that the curator can override. The reason I think this is the right architectural shape is that "what should be remembered, where, and for how long" is a different cognitive task from "do the work." When the same agent does both, the work agent biases toward remembering everything it produced. A dedicated curator whose only job is memory governance ends up much more conservative, and the store stays useful longer.

3h ago

---

**[Wiz Integrates with Anthropic's Compliance API](https://www.reddit.com/r/artificial/comments/1tnvmgt/wiz_integrates_with_anthropics_compliance_api/)**

Wiz integrates with Anthropic’s Compliance API. Gain total visibility into Claude usage, configurations, and identity risks within the Wiz platform.

🔗 [wiz.io](https://www.wiz.io/blog/claude-wiz-integration?2) • 14h ago

---

**[Top 10 Fastest Growing AI repos this week](https://www.reddit.com/r/artificial/comments/1tnjhts/top_10_fastest_growing_ai_repos_this_week/)**

Curated this list of fastest growing AI repos. They are mostly AI coding agents, personal AI, memory, browser automation, Claude Skills and local-first dev tooling: colbymchenry/codegraph (+14.1K stars) Pre-indexed local code knowledge graph for Claude Code, Codex, Cursor, OpenCode, and Hermes Agent. tinyhumansai/openhuman (+17.1K stars) Personal AI / private AI superintelligence. Imbad0202/academic-research-skills (+11.6K stars) Claude Code skills for academic research workflows: research, write, review, revise, finalize. ruvnet/RuView (+6.8K stars) Turns commodity WiFi signals into spatial intelligence, presence detection, and vital sign monitoring. rohitg00/agentmemory (+6.9K stars) Persistent memory for AI coding agents based on real-world benchmarks. supertone-inc/supertonic (+3.6K stars) On-device multilingual TTS running natively via ONNX. CloakHQ/CloakBrowser (+7.0K stars) Stealth Chromium that passes bot detection tests with Playwright compatibility. HKUDS/ViMax (+2.7K stars) Agentic video generation: director, screenwriter, producer, and video generator in one. humanlayer/12-factor-agents (+1.9K stars) Principles for building production-grade LLM-powered software. Varnan-Tech/OpenDirectory (+250 stars) AI Agent Skills built for founders who hate marketing. All links in 1st comment 👇

23h ago

---

**[Small differences in judgment used to be small differences in outcomes.](https://www.reddit.com/r/artificial/comments/1tofmq5/small_differences_in_judgment_used_to_be_small/)**

15m ago

---

**[How to create cinematic typography with Google Flow](https://www.reddit.com/r/artificial/comments/1to81tm/how_to_create_cinematic_typography_with_google/)**

I used Google Flow to create a minimalist “ILLAS CÍES” typography design with ocean textures inside the letters. Basic workflow: Open Google Flow Create a new scene/project Use a typography-focused prompt Describe the textures you want inside the letters Keep the background minimal Generate multiple versions and upscale the best one Example prompt: “Minimalist typography design with the words ‘ILLAS CÍES’, letters filled with realistic turquoise Atlantic ocean water, soft white foam waves, subtle sandy beach gradients, clean white background, modern travel poster aesthetic” Tips: Use short prompts first Add lighting details later Avoid too many effects High contrast text works best The results are surprisingly good for travel-style graphics.

4h ago

---

**[AI solves 80-year-old math conjecture for under $1000](https://www.reddit.com/r/artificial/comments/1to657g/ai_solves_80yearold_math_conjecture_for_under_1000/)**

GPT-next solved an 80-year-old Erdős combinatorics conjecture for under $1,000 in compute. That single fact reframes everything else happening this week. The Erdős unit distance problem resisted human mathematicians since 1946. A frontier model closed it at a cost lower than a mid-tier SaaS subscription, which means the boundary between "AI as tool" and "AI as independent discoverer" is no longer theoretical. Lilian Weng's new deep dive on test-time compute and chain-of-thought reasoning explains the underlying mechanism: reasoning models are not retrieving known proofs, they are generating novel inference chains at scale. The infrastructure layer is pricing this in faster than most observers realize. Railway reports $200K+ monthly coding agent spend and 100K signups per week, and is now building own-metal data centers to absorb the load. Daytona hit 850K daily sandbox runs with 74% month-over-month growth, confirming that isolated compute environments are now a first-class primitive, not a niche DevOps concern. Three specialized infrastructure companies, Exa, Modal, and TurboPuffer, reached unicorn valuations simultaneously this week, covering retrieval, serverless GPU, and vector search. When picks-and-shovels companies price in sustained demand at the same moment, it is not coincidence. Every major lab has now repositioned as an agent lab, not a model lab. ClickUp replacing hundreds of employees with thousands of AI agents is the first established tech company to execute that repositioning at the labor level rather than just the product level. The counterweight is that Salesforce customers remain locked in despite the theoretical ability to rebuild on AI-native stacks cheaply. Data gravity and switching costs are buying incumbents time, but ClickUp's move suggests that time is measured in quarters, not years. The governance conversation caught up this week in an unexpected place. Pope Leo XIV's 42,000-word encyclical names specific failure modes including algorithmic control, surveillance capitalism, and autonomous weapons, and will directly shape EU and Latin American regulatory debates. TechCrunch's read is that the document's real target is the tech elite's capacity to reshape society outside democratic accountability, a framing that lands harder alongside new UK research quantifying data extraction from consumers as equivalent in value to retirement savings. The Vatican and the empiricists arrived at the same diagnosis from opposite directions. Two structural forces will shape AI infrastructure economics over the next 90 days in ways most deployment teams are not modeling. China flooding global markets with DRAM and NAND will compress inference cluster costs faster than US export controls intended. The EU's sovereign cloud setback has paradoxically clarified the build-domestic mandate, accelerating European AI infrastructure investment independent of US hyperscalers. Security remains the open variable: even Google has no established playbook for prompt injection, model supply chain risk, or agentic authorization at production scale. A second Fortune 500 company will publicly attribute a reduction of more than 500 knowledge-worker roles directly to agentic AI systems before Q3 earnings season, making ClickUp's announcement the start of a visible series rather than an isolated case.

5h ago

---

**[AI Infrastructure Has a Physical Weak Spot Nobody Talks About Enough - Copper Supply Shocks](https://www.reddit.com/r/artificial/comments/1to5wz1/ai_infrastructure_has_a_physical_weak_spot_nobody/)**

Something interesting happened this week that barely crossed into mainstream AI discussion. A strong earthquake in Chile disrupted copper ore production and pushed copper prices higher again. Chile matters because it produces roughly 24% of the world’s copper supply, and a huge part of global AI infrastructure indirectly depends on that metal. That connection is becoming impossible to ignore. Everyone talks about GPUs, compute scaling, inference costs, and power demand. But very few people talk about the raw materials underneath the entire AI stack. Copper is everywhere inside AI infrastructure: data center power systems transformers cooling systems switchgear high-voltage cabling backup energy systems grid expansion GPU interconnect infrastructure A single hyperscale AI data center can reportedly consume tens of thousands of tonnes of copper depending on scale and power architecture. At the same time, global copper supply is getting tighter: new mines can take 15-20+ years to develop major deposits are aging permitting remains difficult globally geopolitical risk keeps increasing now even earthquakes are disrupting supply chains This is where the story becomes interesting from an AI perspective. AI demand growth is exponential. Copper supply growth is not. That mismatch is why more people are suddenly watching early-stage copper exploration companies again. One example is NovаRed Mining Inc. and its Wilmac Copper-Gold Project in British Columbia. Not because it is producing copper today - it is not. But because markets are starting to realize future AI infrastructure may require entirely new copper discoveries. Some interesting details about Wіlmac: 16,078 hectares in BC’s Quesnel porphyry belt located near Hudbay’s Copper Mountain Mine soil results up to 1,125 ppm copper interpreted intrusive centers identified recent IP/AMT geophysics added deeper targeting data company also pushing an AI-assisted targeting platform called MetalCore The bigger point is not "this stock goes up." The bigger point is that AI is no longer just a software story. It is becoming a materials story. And every supply disruption - whether geopolitical, regulatory, or seismic - reminds the market that physical infrastructure still matters. The AI boom may eventually depend just as much on copper supply chains as on semiconductor innovation itself. NFA.

5h ago

---

---

## Google News: "ai"

**[To Understand Pope Leo’s Efforts on A.I., Look at the Man Shaking His Hand](https://www.nytimes.com/2026/05/26/us/pope-leo-ai-anthropic.html)**

The New York Times • 9h ago

---

**[Largest study of AI hiring algorithms to date finds 'clear racial disparities' — over 25% of Black applicants tainted by bias](https://fortune.com/2026/05/26/ai-hiring-algorithm-racial-disparities-pymetrics-stanford-study/)**

A Stanford-led study of 4 million job applications reveals AI tools used by Fortune 100 companies systematically reject Black and Asian applicants.

Fortune • 11m ago

---

**[California mom out thousands after scammers use AI to mimic daughter's voice in fake kidnapping; part of growing trend](https://abc7.com/post/california-mom-thousands-scammers-use-ai-mimic-daughters-voice-fake-kidnapping-part-growing-trend/19175361/)**

Thousands of dollars were stolen from a California woman after scammers used artificial intelligence to mimic her daughter's voice in what authorities describe as a growing type of fraud.

ABC7 Los Angeles • 29m ago

---

**[US students on why they booed their pro-AI graduation speakers: ‘They’re not reading the room’](https://www.theguardian.com/technology/2026/may/26/students-boo-pro-ai-graduation-speakers)**

Recent college grads are not very fond of commencement speakers hyping up a technology they see as a threat to their career prospects

The Guardian • 10h ago

---

**[Therapists are using AI to take notes. Is it a useful tool or a breach of trust?](https://www.npr.org/2026/05/26/nx-s1-5826943/talk-therapy-mental-health-ai-artificial-intelligence-privacy-trust)**

New companies are selling artificial intelligence assistance to mental health therapists. The AI tools can help with administration and recordkeeping, but some patients worry about their privacy.

NPR • 9h ago

---

**[How the U.S. military is using AI in warfare](https://www.cbsnews.com/video/how-the-us-military-is-using-ai-in-warfare/)**

CBS News' Chris Livesay gets an inside look at how the U.S. military is using artificial intelligence on the battlefield.

CBS News • 19h ago

---

**[China Expands Travel Curbs to Top AI Talent at Private Firms](https://www.bloomberg.com/news/articles/2026-05-26/china-expands-travel-curbs-to-top-ai-talent-at-private-firms)**

Bloomberg.com • 10h ago

---

**[The House Democrat taking a big risk to land an AI deal](https://www.politico.com/news/2026/05/26/ai-framework-democrats-congress-00935307)**

Politico • 9h ago

---

**[OpenAI's Altman says AI unlikely to lead to 'jobs apocalypse'](https://www.reuters.com/world/asia-pacific/openais-altman-says-ai-unlikely-lead-jobs-apocalypse-2026-05-26/)**

Reuters • 4h ago

---

**[The Despair of the Professor in the Age of A.I.](https://www.newyorker.com/news/fault-lines/the-despair-of-the-professor-in-the-age-of-ai)**

“Was it always the case that half of our students would cheat if it were easy enough?”

The New Yorker • 8h ago

---

---

## HackerNews: "ai"

**[Using AI to write better code more slowly](https://news.ycombinator.com/item?id=48272984)**

⬆️ 1059 • 💬 394 • 19h ago • [nolanlawson.com](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

---

**[Memory has grown to nearly two-thirds of AI chip component costs](https://news.ycombinator.com/item?id=48258684)**

High-bandwidth memory (HBM) accounts for 63% of AI chip component costs, up from 52% in Q1 2024. Epoch AI's breakdown of component cost shifts across major chip designers.

⬆️ 440 • 💬 489 • 2d ago • [Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)

---

**[Pope Leo XIV says AI must serve humanity, not the powerful few](https://news.ycombinator.com/item?id=48266485)**

VATICAN CITY (RNS) — In ‘Magnifica Humanitas,’ Leo's 83-page manifesto on AI, the pope tackles the social, economic and political challenges associated with artificial intelligence.

⬆️ 343 • 💬 67 • 1d ago • [RNS](https://religionnews.com/2026/05/25/in-his-first-encyclical-pope-leo-xiv-says-ai-must-serve-humanity-not-the-powerful-few/)

---

**[Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks](https://news.ycombinator.com/item?id=48266906)**

Authorities in the Netherlands have arrested the co-owners of two related Internet hosting companies for operating IT infrastructure used by Russia to carry out cyberattacks, influence operations and disinformation campaigns inside the European Union. The two men were the focus…

⬆️ 283 • 💬 88 • 1d ago • [krebsonsecurity.com](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)

---

**[A successful Japanese trial of a ramjet engine designed for Mach‑5 aircraft](https://news.ycombinator.com/item?id=48270812)**

A team of engineers from Japan has completed a successful ground combustion trial of a ramjet engine designed for a Mach‑5 hypersonic aircraft.

⬆️ 222 • 💬 166 • 22h ago • [BGR](https://www.bgr.com/2178211/japan-hypersonic-engine-ramjet-2-hour-flights-to-us/)

---

**[Uber president says AI spending is getting 'harder to justify'](https://news.ycombinator.com/item?id=48277485)**

﻿There’s no clear connection between AI usage and productivity.

⬆️ 217 • 💬 111 • 8h ago • [The Verge](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify)

---

**[DeepSeek to Make Permanent 75% Discount on Flagship AI Model](https://news.ycombinator.com/item?id=48257410)**

⬆️ 209 • 💬 2 • 2d ago • [bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model)

---

**['AI washing': firms are scrambling to rebrand themselves as tech-focused](https://news.ycombinator.com/item?id=48257980)**

PR executives say UK companies are forcing them to present ordinary automation as artificial intelligence

⬆️ 179 • 💬 163 • 2d ago • [the Guardian](https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand)

---

**[Pope Leo: opaque AI run by few firms risks "New Forms of Dehumanization"](https://news.ycombinator.com/item?id=48266435)**

Pope Leo issues AI Encyclical warning that 'Opaque Algorithms' controlled by a 'few' companies threaten 'new forms of  dehumanization'

⬆️ 164 • 💬 2 • 1d ago • [Variety](https://variety.com/2026/biz/global/pope-leo-ai-encyclical-algorithms-threaten-dehumanisation-1236758186/)

---

**[Outsourcing plus local AI will soon become more economical vs. frontier labs](https://news.ycombinator.com/item?id=48278610)**

⬆️ 150 • 💬 160 • 6h ago • [signalbloom.ai](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/)

---

---

## YouTube Videos: "ai"

**[OpenAI Founder Admits AI Isn’t Working | Prime Reacts](https://www.youtube.com/watch?v=-vPlLwtVU5g)**

Sources: https://www.youtube.com/watch?v=ZugX7a99dLk https://twitch.tv/ThePrimeagen - I Stream on Twitch ...

📺 ThePrimeagenHighlights

👁️ 180K • 👍 5K • 💬 561 • ⏱️ 20:44 • 1d ago

---

**[Pope Leo issues manifesto warning about AI](https://www.youtube.com/watch?v=RqXXs-ZIDNo)**

Pope Leo XIV says control of artificial intelligence must not remain in the hands “of a few” while warning that technology is fueling ...

📺 CNN

👁️ 126K • 👍 3K • 💬 1K • ⏱️ 11:28 • 1d ago

---

**[How to Make Explainer Videos With AI (Full Guide)](https://www.youtube.com/watch?v=a_qUx3YV8QQ)**

How to Make AI Explainer Videos with AI! Create Your Own Explainer Videos with OpenArt ...

📺 Isa does AI

👁️ 8K • 💬 4 • ⏱️ 15:50 • 6h ago

---

**[DeepMind’s Insane AI Breakthroughs With CEO Demis Hassabis](https://www.youtube.com/watch?v=huAwz_BR8WM)**

Thank you to Google DeepMind for the invite. ❤️ Check out Lambda here and sign up for their GPU Cloud: ...

📺 Two Minute Papers

👁️ 67K • 👍 4K • 💬 452 • ⏱️ 21:28 • 1d ago

---

**[It’s Happening... Anthropic MYTHOS 1 Is Here!](https://www.youtube.com/watch?v=rDDI9gDiNAg)**

Claude Mythos 1 and Anthropic's Claude Security are now at the center of a massive AI cybersecurity story. Project Glasswing ...

📺 AI Revolution

👁️ 61K • 👍 2K • 💬 128 • ⏱️ 14:27 • 1d ago

---

**[Why the AI cyber threat is rising](https://www.youtube.com/watch?v=rlRlhEQDvVA)**

AI is getting much better at hacking and fast. Sky News technology correspondent Rowland Manthorpe examines new evidence ...

📺 Sky News

👁️ 62K • 👍 1K • 💬 203 • ⏱️ 7:33 • 1d ago

---

**[I Replaced Myself With AI Until My Friends Noticed](https://www.youtube.com/watch?v=8AlDjfiBUCs)**

I Replaced Myself With AI Until My Friends Noticed FOLLOW ME: https://www.roblox.com/users/4891355965/profile JOIN MY ...

📺 KAYE

👁️ 372K • 👍 7K • 💬 1K • ⏱️ 15:06 • 2d ago

---

**[Pope Leo warns of the risks of AI](https://www.youtube.com/watch?v=_7MoCJ5tVEM)**

"Artificial intelligence needs to be disarmed." Pope Leo XIV calls for the regulation of AI in a sweeping manifesto and warns it ...

📺 MS NOW

👁️ 64K • 👍 2K • 💬 242 • ⏱️ 0:59 • 1d ago

---

**[Nobody Actually Wants AI Anymore](https://www.youtube.com/watch?v=FQpZdCKgc6w)**

People often compare AI to the internet, but there's one big problem with that comparison: people naturally adopted the internet as ...

📺 Vanessa Wingårdh

👁️ 245K • 👍 16K • 💬 5K • ⏱️ 12:37 • 2d ago

---

**[Richard Feynman is Now A.I. Slop](https://www.youtube.com/watch?v=A2_8199CL1I)**

A.I generated SLOP channels are slowly infecting the Science side of YouTube, it's disturbing and it's a huge problem.

📺 Kyle Hill

👁️ 185K • 👍 18K • 💬 2K • ⏱️ 9:50 • 2d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,908 • ❤️ 851 • 1h ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 9,144 • ❤️ 367 • 6d ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 283 • 15h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 103,033 • ❤️ 371 • 5d ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 2,409 • ❤️ 294 • 14h ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 48,112 • ❤️ 689 • 8d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 1,598,473 • ❤️ 902 • 1mo ago

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

⬇️ 1,376,847 • ❤️ 1,368 • 4d ago

---

**[Qwen3.6-27B-MTP-GGUF](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF)**

*Unsloth AI*

Qwen3.6-27B-MTP-GGUF is a 27B parameter causal language model with vision capabilities, optimized for faster inference via MTP. It excels at agentic coding, reasoning, and handling extended contexts up to 1M tokens, making it suitable for complex development workflows and iterative tasks.

`image-text-to-text` `27.3B`

⬇️ 735,349 • ❤️ 495 • 9h ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 79,711 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 170 • 💬 2 • ⭐ 435 • 4d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 26,259 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://huggingface.co/papers/2605.26115)**

*Weijie Wang, Zimu Li, Jinchuan Shi et al. (8 authors)*

🏢 Zhejiang University

TriSplat is a feed-forward 3D reconstruction network that uses oriented triangle primitives to directly generate simulation-ready meshes from single images, bypassing expensive post-processing steps.

▲ 34 • 💬 1 • ⭐ 91 • 1d ago

[🎓 arXiv](https://arxiv.org/abs/2605.26115) • [💻 code](https://github.com/ziplab/TriSplat) • [🔗 project](https://lhmd.top/trisplat/#interactive)

---

**[Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution](https://huggingface.co/papers/2605.23264)**

*Hongbo Wang, Huaibo Huang, Pin Wang et al. (6 authors)*

🏢 Chinese Academic of Science Institute of Automation

ASASR addresses spectral misalignment in image super-resolution by leveraging Riemannian geometry and adversarial training to improve structural fidelity and reduce artifacts.

▲ 3 • 💬 1 • ⭐ 71 • 4d ago

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

▲ 120 • 💬 10 • ⭐ 10,694 • 22d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 128 • 💬 3 • ⭐ 632 • 7d ago

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

⭐ 2.7k • 🔱 182 • 12h ago

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

⭐ 2.0k • 🔱 139 • 5h ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 1.9k • 🔱 129 • 4h ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.8k • 🔱 220 • 19d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 196 • 35m ago

---

---

*Generated by PeekDeck - A glance is all you need*

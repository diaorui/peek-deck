---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-05-26T23:40:53.079801+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- repositories
- social
- videos
- news
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** May 26, 2026 at 23:40 UTC  
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

**[Anthropic just published how they contain Claude agents, including two security incidents they got wrong](https://www.reddit.com/r/artificial/comments/1tomozc/anthropic_just_published_how_they_contain_claude/)**

Anthropic dropped a solid engineering post this week about containment across claude.ai, Claude Code, and Cowork. One of the more transparent writeups from a major AI lab about what actually broke. The core insight: model-layer defenses are probabilistic and will always have a non-zero miss rate. So the real answer is hard environmental containment, not just safer models. Three patterns they use: -claude.ai: ephemeral gVisor containers, fully server-side -Claude Code: OS-level sandbox with human-in-the-loop approvals (93% get approved anyway, so approval fatigue is real) -Cowork: full local VM, credentials never enter the guest Two incidents they disclosed: A red team phished an employee into running a prompt that exfiltrated AWS credentials. Succeeded 24 out of 25 times. The model had nothing to catch because the user was the one typing it. Only egress controls would have stopped it. A third-party found that Cowork’s egress allowlist passes traffic to api.anthropic.com. An attacker embedded an API key in a file in the user’s workspace, Claude followed hidden instructions, and uploaded files to the attacker’s Anthropic account. Sandbox worked perfectly and still leaked data. Their lesson: an allowlist isn’t a destination filter, it’s a capability grant. Every function reachable through an allowed domain is an attack surface. The section on persistent memory poisoning and multi-agent trust escalation at the end is worth reading too if you’re building anything agentic.

1h ago

---

**[AI is becoming epistemic infrastructure controlled by a handful of private individuals?](https://www.reddit.com/r/artificial/comments/1to0dmn/ai_is_becoming_epistemic_infrastructure/)**

Most people treat AI as a convenient black box. Ask it something, it answers, you move on. But we’re sleepwalking into something bigger. I think Whoever controls the infrastructure of knowledge controls how people perceive reality. The Church held that position for centuries through controlling scripture. The printing press broke that monopoly by distributing interpretive power. AI is doing the opposite recentralizing it into a handful of corporations with no democratic accountability. “AI says X” is structurally identical to “studies show X” you’re invoking an authority you can’t directly access. Except with a study you can theoretically trace the source. With AI the chain is opaque by design. And it delivers wrong answers and right answers with identical confidence. There’s no texture to signal doubt. AI isn’t neutral, it’s being heavily calibrated. In the west, the models are trained to be more “ethical” maybe more liberal and always try to give you a more “balance” take on things. Chinese AI simply doesn’t allow you to access to anything that put the CCP is a bad light. The more you rely on AI in domains where you lack expertise, the less capable you become of evaluating whether to trust it. AI works best for people who already know enough to catch its errors the opposite of how most people use it. Imagine the next generation of people growing up and being shaped by these AI. I can’t help but feel nervous and scared for the future. OpenAI said 10% of our entire population has already started using chatgpt. Regardless of the accuracy of this number, I feel like we are slowly entering into a mass hallucination / blind reliance on these AI models. We’re not just offloading cognitive effort. We’re handing the dial over who shapes how billions of people understand reality to a small group of unelected, largely unregulated private individuals.

15h ago

---

**[Which AI image generator is actually worth the money?](https://www.reddit.com/r/artificial/comments/1to5v3m/which_ai_image_generator_is_actually_worth_the/)**

I've looked at about a dozen different image generators: Nano Banana Flux Midjourney GPT Image 2 Firefly Ideogram Recraft Leonardo Canvas Meta AI They all have their pluses and minuses but they all do a decent job. If I'm looking to spend thousands over a year on an image generator, what would you suggest. This would be mainly for business and a little for art.

10h ago

---

**[Built a tool to save Claude responses (and ChatGPT, Gemini) into one searchable vault - sharing in case it's useful](https://www.reddit.com/r/artificial/comments/1toga8l/built_a_tool_to_save_claude_responses_and_chatgpt/)**

I built this tool because I kept asking Claude for code and explanations and losing them in long chats. Coffer adds a save button to every AI response and stores them locally in a searchable vault. Works on: - claude.ai - chatgpt.com - gemini.google.com You can mix snippets across all three and search them. The Markdown stays formatted, which is very nice for Claude's longer responses with code and tables. Everything is local. Coffer makes zero network calls of its own. Free. Feedback is especially welcome. https://chromewebstore.google.com/detail/nhchbmaobjhjfmeekpnkmhdjajdolcjb?utm_source=item-share-cb

4h ago

---

**[Memory Curator Agent a governance layer for memory in multi-agent systems](https://www.reddit.com/r/artificial/comments/1to9p3u/memory_curator_agent_a_governance_layer_for/)**

I keep seeing the same failure in every multi-agent setup I touch. Memory looks fine on day one. By week three it is half stale facts, half private context that should not have been written publicly, and half decisions that were superseded but never overwritten. Retrieval gets noisier. Users keep repeating context because the right fact ended up in the wrong scope. The recursion limit is not the problem here. The memory store itself is the problem. The thing I changed that helped most was the simplest possible rule. Worker agents are not allowed to write to durable memory. They emit a structured memory event with a proposed scope and evidence, and a separate Memory Curator agent decides whether to write it, where to write it, or to discard it. The four scopes I route into are agent repo memory (durable design rules for one agent), agent team memory (cross-agent procedures, handoff standards, safety rules), project memory (current state, decisions, risks for one engagement), and session scratch (temporary observations that probably should not survive). The mapping I had in mind was to organizational and human memory categories: individual specialist memory, transactive team memory (Ren and Argote), project memory, and short-term working memory. The routing rule is conservative on purpose. If an event is temporary, unsupported, ambiguous, or contains private context, it goes to session scratch or gets discarded outright. Durable memory has to be earned. The schema is JSON with tagged fields for fact, decision, preference, risk, procedure, and hypothesis, plus an evidence reference and a proposed scope that the curator can override. The reason I think this is the right architectural shape is that "what should be remembered, where, and for how long" is a different cognitive task from "do the work." When the same agent does both, the work agent biases toward remembering everything it produced. A dedicated curator whose only job is memory governance ends up much more conservative, and the store stays useful longer.

8h ago

---

**[Uber's COO says it's getting harder to justify the money spent on AI tokenmaxxing](https://www.reddit.com/r/artificial/comments/1tndgv8/ubers_coo_says_its_getting_harder_to_justify_the/)**

Operations chief Andrew Macdonald said he's not seeing proportional productivity gains from increasing AI costs within Uber.

🔗 [Business Insider](https://www.businessinsider.com/uber-coo-andrew-macdonald-ai-token-spending-harder-justify-2026-5) • 1d ago

---

**[Is AI coming for your job? A bigger government can help](https://www.reddit.com/r/artificial/comments/1too4xn/is_ai_coming_for_your_job_a_bigger_government_can/)**

What happens if you lose your job and never find another one? That question is at the heart of the fear AI inspires.

🔗 [The Seattle Times](http://seattletimes.com/opinion/is-ai-coming-for-your-job-a-bigger-government-can-help/?utm_medium=social&utm_campaign=owned_reddit&utm_source=reddit) • 7m ago

---

**[Introducing the Ontology Anchor: A Mechanism that Gives AI a Map of What Matters to You](https://www.reddit.com/r/artificial/comments/1tom195/introducing_the_ontology_anchor_a_mechanism_that/)**

Abstract: Natively, no flagship LLM exists that has the ability to know who you are and what cognitive patterns are important to you. Thus, AI doesn't have a map of your goals, preferences, or tendencies. Without this a model generically drifts and defaults to what you discussed most recently and forgets important details earlier in the thread. And if you want to start a new thread there are re-orientation costs. None of these are fixed by simply adding more context. They require a mechanism that knows what, within the context, matters most to the operator. The Ontology Anchor/Ontology%20Anchor%20(OA)/Ontology%20Anchor%20(OA)) is a mechanism that metaphorically behaves like a knowledge graph. It creates something that acts like nodes, concepts, standards, and edges between them that give those “nodes” their purpose. A node labeled “personal alignment” connects to nodes for “warmth,” “sycophancy risk,” and “governance requirement.” When the model generates content touching any of those nodes, the connected structure remains accessible rather than fading into generic background. The graph is not literally built as a database, as the mechanism is attentional in the standard KV-Cache and not archival, but the functional behavior is graph-like enough to make the metaphor useful. Here is a simpler way to put it. Stock/default AI is a room where everything is equally lit. The Anchor places a bright light on the objects that matter most for the operator’s work. Within the transformer the attention mechanism still operates within the native architecture. But the model now has a clearer set of objects to orient around when it generates answers. Thus, the longer you use the Anchor, the sharper and more tailor-made the models' responses to you become. Memory appears to improve as well. This is a virtuous loop. The Anchor helps the model understand the operator better. This allows the thread to be useful longer, which increases the amount of available contextual information, thus providing even more information for the model to provide even better outputs to the operator further into the thread. The Ontology Anchor (instructions for its use here/Ontology%20Anchor%20(OA)/README)) is a component mechanism to a larger “Epistemic Lattice Tethering” (ELT) framework. ELT is not a collection of separate mechanisms, but a unified architecture for making AI more coherent, faithful, and genuinely more useful over time. Together, ELT allows these interconnected components to operate as a “cognitive exoskeleton,” extending the abilities of the operator and giving the operator both greater agency and capabilities. How does ELT do this? How does ELT extend the useful life of a context window by hundreds of thousands of tokens, while remaining coherent and aligned with the operator’s goals? These questions will be explained, in detail, in another post.

🔗 [Medium](https://medium.com/@socal21st.oc/the-ontology-anchor-giving-ai-a-better-way-to-know-you-4d88923d6d67) • 1h ago

---

**[Built an AI companion architecture with real internal needs — looking for first investor after publishing research paper](https://www.reddit.com/r/artificial/comments/1tokn46/built_an_ai_companion_architecture_with_real/)**

The problem with every AI product right now is that they're all wrappers. Same stateless LLM, different UI. The moment the context window closes, the AI forgets you existed. I built the infrastructure layer that fixes that. PHI // DRIFT gives an AI companion persistent state — seven internal need variables that drift between sessions, memory scored by what emotionally mattered not just what was semantically close, and a real-time telemetry dashboard showing the AI's internal state as it runs. This isn't a product yet. It's a published architecture with a research paper, 18k+ lines of working code, and 10 GitHub stars in the first 24 hours with zero marketing spend. The SaaS opportunity is clear: — Every company building AI companions needs this infrastructure layer — Enterprise AI that actually remembers context across sessions commands premium pricing — Security tooling that maintains reasoning state across bug bounty sessions is immediately monetizable I built this in 5 months on consumer hardware with $0. Imagine what happens with actual help Paper: https://zenodo.org/records/20350249DM

2h ago

---

**[Wiz Integrates with Anthropic's Compliance API](https://www.reddit.com/r/artificial/comments/1tnvmgt/wiz_integrates_with_anthropics_compliance_api/)**

Wiz integrates with Anthropic’s Compliance API. Gain total visibility into Claude usage, configurations, and identity risks within the Wiz platform.

🔗 [wiz.io](https://www.wiz.io/blog/claude-wiz-integration?2) • 19h ago

---

---

## Google News: "ai"

**[To Understand Pope Leo’s Efforts on A.I., Look at the Man Shaking His Hand](https://www.nytimes.com/2026/05/26/us/pope-leo-ai-anthropic.html)**

The New York Times • 14h ago

---

**[Vance Praises Pope Leo’s AI Warnings As ‘Very Profound’](https://www.forbes.com/sites/conormurray/2026/05/26/vance-praises-pope-leos-ai-warnings-as-very-profound/)**

Vice President JD Vance, who previously issued a warning for  Pope Leo XIV over his anti-war comments, praised the pope’s manifesto warning about the risks of AI as “very profound.”

Forbes • 4h ago

---

**[Pope Leo’s AI Encyclical Sparks ’Butlerian Jihad’ Memes](https://www.yahoo.com/news/world/articles/pope-leo-anti-ai-encyclical-221728956.html)**

Pope Leo XIV voiced his concerns about AI in his first encyclical, sparking praise and memes on social media, along with jokes about a ‘Butlerian Jihad.’

Yahoo • 1h ago

---

**[Uber burned through its entire 2026 AI budget in four months. Now its COO is questioning whether it's worth it](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/)**

The rideshare giant's COO says “it’s very hard to draw a line” between rising AI costs and useful features for customers.

Fortune • 5h ago

---

**[Uber COO Says AI Lacks ROI](https://www.theinformation.com/newsletters/applied-ai/uber-coo-says-ai-lacks-roi)**

Many corporate leaders say they’re getting value from AI as their spending on it skyrockets, but hype is outpacing reality in plenty of cases.On a podcast over the weekend, for instance, Uber Chief Operating Officer Andrew Macdonald said the ride-hailing company isn’t seeing a clear increase in ...

The Information • 3h ago

---

**[Uber president says AI spending is getting ‘harder to justify’](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify)**

﻿There’s no clear connection between AI usage and productivity.

The Verge • 13h ago

---

**[Teaching thermodynamic laws to AI unlocks a polymer modeling challenge](https://phys.org/news/2026-05-thermodynamic-laws-ai-polymer.html)**

Phys.org • 20m ago

---

**[Citrus County Commission unanimously approves yearlong freeze on new AI data center rezoning applications](https://www.fox13news.com/news/citrus-county-commission-approves-freeze-ai-data-center-rezoning-applications)**

Citrus County commissioners got an earful from residents who say their backyard is no place for a data center.

FOX 13 Tampa Bay • 55m ago

---

**[N.Y. state senator warns against feds superseding state regulations around AI](https://spectrumlocalnews.com/nys/rochester/politics/2026/05/26/congress-eyes-superseding-state-laws-on-ai)**

State Sen. Andrew Gounardes joined Capital Tonight.

Spectrum News • 10m ago

---

**[Micron tops $1 trillion in market cap as UBS sees company becoming an AI giant](https://finance.yahoo.com/markets/article/micron-tops-1-trillion-in-market-cap-as-ubs-sees-company-becoming-an-ai-giant-134443287.html)**

Micron stock rose after UBS said the AI boom has changed the memory chip market — and tripled its price target to a Street high.

Yahoo Finance • 3h ago

---

---

## HackerNews: "ai"

**[Using AI to write better code more slowly](https://news.ycombinator.com/item?id=48272984)**

⬆️ 1132 • 💬 417 • 1d ago • [nolanlawson.com](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)

---

**[Memory has grown to nearly two-thirds of AI chip component costs](https://news.ycombinator.com/item?id=48258684)**

High-bandwidth memory (HBM) accounts for 63% of AI chip component costs, up from 52% in Q1 2024. Epoch AI's breakdown of component cost shifts across major chip designers.

⬆️ 441 • 💬 490 • 2d ago • [Epoch AI](https://epoch.ai/data-insights/ai-chip-component-cost-shares)

---

**[Pope Leo XIV says AI must serve humanity, not the powerful few](https://news.ycombinator.com/item?id=48266485)**

VATICAN CITY (RNS) — In ‘Magnifica Humanitas,’ Leo's 83-page manifesto on AI, the pope tackles the social, economic and political challenges associated with artificial intelligence.

⬆️ 344 • 💬 67 • 1d ago • [RNS](https://religionnews.com/2026/05/25/in-his-first-encyclical-pope-leo-xiv-says-ai-must-serve-humanity-not-the-powerful-few/)

---

**[Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks](https://news.ycombinator.com/item?id=48266906)**

Authorities in the Netherlands have arrested the co-owners of two related Internet hosting companies for operating IT infrastructure used by Russia to carry out cyberattacks, influence operations and disinformation campaigns inside the European Union. The two men were the focus…

⬆️ 284 • 💬 87 • 1d ago • [krebsonsecurity.com](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)

---

**[Uber president says AI spending is getting 'harder to justify'](https://news.ycombinator.com/item?id=48277485)**

﻿There’s no clear connection between AI usage and productivity.

⬆️ 255 • 💬 132 • 13h ago • [The Verge](https://www.theverge.com/transportation/937116/uber-ai-investment-hard-to-justify)

---

**[Outsourcing plus local AI will soon become more economical vs. frontier labs](https://news.ycombinator.com/item?id=48278610)**

⬆️ 231 • 💬 249 • 11h ago • [signalbloom.ai](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/)

---

**[A successful Japanese trial of a ramjet engine designed for Mach‑5 aircraft](https://news.ycombinator.com/item?id=48270812)**

A team of engineers from Japan has completed a successful ground combustion trial of a ramjet engine designed for a Mach‑5 hypersonic aircraft.

⬆️ 228 • 💬 167 • 1d ago • [BGR](https://www.bgr.com/2178211/japan-hypersonic-engine-ramjet-2-hour-flights-to-us/)

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

---

## YouTube Videos: "ai"

**[THE GOAL OF AI](https://www.youtube.com/watch?v=ZaSqQ9-pFCM)**

Senator Bernie Sanders is the senior senator from Vermont. He is the longest-serving independent in U.S. congressional history ...

📺 Senator Bernie Sanders

👁️ 14K • 👍 2K • 💬 211 • ⏱️ 1:52 • 9h ago

---

**[OpenAI Founder Admits AI Isn’t Working | Prime Reacts](https://www.youtube.com/watch?v=-vPlLwtVU5g)**

Sources: https://www.youtube.com/watch?v=ZugX7a99dLk https://twitch.tv/ThePrimeagen - I Stream on Twitch ...

📺 ThePrimeagenHighlights

👁️ 193K • 👍 5K • 💬 583 • ⏱️ 20:44 • 1d ago

---

**[They’re Building an AI &quot;God&quot;…And Revelation Is Coming Into Focus](https://www.youtube.com/watch?v=NU-zTMgvgQ0)**

In this video, we look at Karen Hao's investigation into OpenAI, the race to build AGI, the language of a “machine god,” the ...

📺 Truth B Told

👁️ 75K • 👍 7K • 💬 1K • ⏱️ 47:00 • 1d ago

---

**[4 FREE and UNLIMITED AI Video Generators That Shouldn’t Exist](https://www.youtube.com/watch?v=r99B1WjyRh8)**

Try Higgsfield Supercomputer and build full AI video workflows in one place ...

📺 Malva AI

👁️ 7K • 👍 395 • 💬 45 • ⏱️ 9:55 • 12h ago

---

**[The ONE Question AI CANNOT ANSWER, Can You?](https://www.youtube.com/watch?v=jRQSo4TRh6Q)**

Did you get the answer right? Comment below.

📺 Tim Pool Show

👁️ 7K • 👍 640 • 💬 149 • ⏱️ 25:56 • 5h ago

---

**[AI Is More Expensive Than Humans](https://www.youtube.com/watch?v=WuhAaMSXD9A)**

AI's cost problem is no longer theoretical. Uber burned through a full year of AI budget in four months and the reason was not the ...

📺 House of El - AI

👁️ 32K • 👍 3K • 💬 660 • ⏱️ 24:08 • 6h ago

---

**[How I build $10,000 AI Websites in 17 mins (Google AI Studio 2.0)](https://www.youtube.com/watch?v=PsE9u37gJjU)**

ALL Systems: https://bit.ly/4kol0y5 firecrawl: https://firecrawl.link/jack-roberts 🎙️ Glaido (voice type): https://bit.ly/42isnim *Build ...

📺 Jack Roberts

👁️ 5K • 👍 245 • 💬 10 • ⏱️ 28:02 • 6h ago

---

**[DeepMind’s Insane AI Breakthroughs With CEO Demis Hassabis](https://www.youtube.com/watch?v=huAwz_BR8WM)**

Thank you to Google DeepMind for the invite. ❤️ Check out Lambda here and sign up for their GPU Cloud: ...

📺 Two Minute Papers

👁️ 75K • 👍 5K • 💬 477 • ⏱️ 21:28 • 1d ago

---

**[Updated Essential AI Skills For 2026](https://www.youtube.com/watch?v=tu4rU4YD1Jk)**

Start building AI apps with Bolt ...

📺 Tina Huang

👁️ 63K • 👍 3K • 💬 127 • ⏱️ 13:45 • 2d ago

---

**[FULL SPEECH: Pope Leo XIV Warns AI “Needs To Be Disarmed” In Explosive Vatican Speech | AK1B](https://www.youtube.com/watch?v=aaYJ_4QcZfE)**

Pope Leo XIV unveiled his first encyclical, Magnifica Humanitas, at the Vatican, warning that artificial intelligence “needs to be ...

📺 DRM News

👁️ 111K • 👍 4K • 💬 582 • ⏱️ 11:16 • 1d ago

---

---

## HuggingFace Models: 🔥 Trending

**[Lance](https://huggingface.co/bytedance-research/Lance)**

*bytedance-research*

Lance is a unified multimodal model supporting image/video understanding, generation, and editing with a 3B parameter architecture. It excels in text-to-video, video editing, and multi-turn consistency editing tasks.

`any-to-any`

⬇️ 1,908 • ❤️ 861 • 6h ago

---

**[Marlin-2B](https://huggingface.co/NemoStation/Marlin-2B)**

*Nemo Station*

Marlin-2B is a compact 2B parameter Video-Language Model (VLM) for extracting structured information from videos. It excels at dense video captioning and natural-language temporal grounding, providing second-precise timestamps for events and resolving queries to specific video spans, making it ideal for efficient video analysis and retrieval on consumer hardware.

`video-text-to-text` `2.2B`

⬇️ 9,144 • ❤️ 375 • 6d ago

---

**[LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)**

*LongCat*

LongCat-Video-Avatar 1.5 is a production-ready framework for audio-driven human video generation, capable of Audio-Text-to-Video (AT2V), Audio-Text-Image-to-Video (ATI2V), and video continuation with stable, commercial-grade avatar synthesis and stylized domain generalization.

⬇️ 0 • ❤️ 297 • 20h ago

---

**[MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B)**

*OpenBMB*

MiniCPM5-1B is a 1B parameter causal language model optimized for on-device deployment, excelling in tool-use, code generation, and reasoning with native long-context support up to 131k tokens.

`text-generation` `1.1B`

⬇️ 2,409 • ❤️ 304 • 19h ago

---

**[HRM-Text-1B](https://huggingface.co/sapientinc/HRM-Text-1B)**

*Sapient AI*

HRM-Text-1B is a 1B-parameter language model utilizing a Hierarchical Reasoning Model (HRM) architecture for enhanced compute depth. It excels at NLP tasks like classification and extraction using few-shot prompting, and can perform reasoning tasks with a 'synth,cot' prefix, though it's a pre-alignment model not a chat assistant.

`text-generation` `1.2B`

⬇️ 103,033 • ❤️ 377 • 5d ago

---

**[supertonic-3](https://huggingface.co/Supertone/supertonic-3)**

*Supertone*

Supertonic 3 is a lightning-fast, on-device text-to-speech model supporting 31 languages with improved stability and speaker similarity. It enables local, cloud-free speech synthesis for applications requiring real-time voice generation.

`text-to-speech`

⬇️ 48,112 • ❤️ 695 • 8d ago

---

**[Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)**

*HauHau*

This is an uncensored, aggressive multimodal (text, image, video) language model based on Qwen3.6-35B-A3B, featuring a Mixture-of-Experts (MoE) architecture with 35B total parameters and 262K context. It is designed for unrestricted text generation and image-text-to-text tasks, offering full content generation without refusals.

`image-text-to-text` `34.7B`

⬇️ 1,598,473 • ❤️ 908 • 1mo ago

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

⬇️ 1,376,847 • ❤️ 1,372 • 4d ago

---

**[DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

*DeepSeek*

DeepSeek-V4-Pro is a 1.6T parameter Mixture-of-Experts language model supporting a 1 million token context length, featuring a hybrid attention architecture for efficient long-context processing. It excels in coding and reasoning tasks, bridging the gap with closed-source models and serving as a top-tier open-source solution for complex agentic workflows and extensive knowledge retrieval.

`text-generation` `861.6B`

⬇️ 5,019,884 • ❤️ 4,309 • 20d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 82 • 💬 3 • ⭐ 79,816 • 17mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://huggingface.co/papers/2605.23904)**

*Yifan Yang, Ziyang Gong, Weiquan Huang et al. (15 authors)*

🏢 Microsoft Research

SkillOpt introduces a systematic text-space optimizer for agent skills that trains skills as external agent state with stable updates and zero deployment inference overhead, achieving superior performance across multiple benchmarks and execution environments.

▲ 170 • 💬 2 • ⭐ 696 • 5d ago

[🎓 arXiv](https://arxiv.org/abs/2605.23904) • [💻 code](https://github.com/microsoft/SkillOpt) • [🔗 project](https://microsoft.github.io/SkillOpt/)

---

**[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**

*Yu Shi, Zongliang Fu, Shuo Chen et al. (7 authors)*

Kronos, a specialized pre-training framework for financial K-line data, outperforms existing models in forecasting and synthetic data generation through a unique tokenizer and autoregressive pre-training on a large dataset.

▲ 35 • 💬 3 • ⭐ 26,445 • 9mo ago

[🎓 arXiv](https://arxiv.org/abs/2508.02739) • [💻 code](https://github.com/shiyu-coder/Kronos)

---

**[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://huggingface.co/papers/2605.26115)**

*Weijie Wang, Zimu Li, Jinchuan Shi et al. (8 authors)*

🏢 Zhejiang University

TriSplat is a feed-forward 3D reconstruction network that uses oriented triangle primitives to directly generate simulation-ready meshes from single images, bypassing expensive post-processing steps.

▲ 34 • 💬 2 • ⭐ 91 • 2d ago

[🎓 arXiv](https://arxiv.org/abs/2605.26115) • [💻 code](https://github.com/ziplab/TriSplat) • [🔗 project](https://lhmd.top/trisplat/#interactive)

---

**[Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution](https://huggingface.co/papers/2605.23264)**

*Hongbo Wang, Huaibo Huang, Pin Wang et al. (6 authors)*

🏢 Chinese Academic of Science Institute of Automation

ASASR addresses spectral misalignment in image super-resolution by leveraging Riemannian geometry and adversarial training to improve structural fidelity and reduce artifacts.

▲ 3 • 💬 2 • ⭐ 71 • 5d ago

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

▲ 120 • 💬 10 • ⭐ 10,738 • 23d ago

[🎓 arXiv](https://arxiv.org/abs/2605.03042) • [💻 code](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) • [🔗 project](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

---

**[Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](https://huggingface.co/papers/2605.19833)**

*Zhifei Xie, Kaiyu Pang, Haobin Zhang et al. (7 authors)*

🏢 National University of Singapore

Mega-ASR framework improves robustness in real-world speech recognition through compound-data construction and progressive acoustic-to-semantic optimization techniques.

▲ 128 • 💬 3 • ⭐ 632 • 8d ago

[🎓 arXiv](https://arxiv.org/abs/2605.19833) • [💻 code](https://github.com/xzf-thu/Mega-ASR) • [🔗 project](https://xzf-thu.github.io/Mega-ASR/)

---

---

## GitHub Repositories: "ai"

**[nexu-io/html-anything](https://github.com/nexu-io/html-anything)**

✨ The agentic HTML editor — your local AI agent writes the HTML, you ship it. 🚀 75 Skills × 9 Surfaces (magazine · deck · poster · XHS / tweet · prototype · data report · Hyperframes) 🛡️ Sandboxed preview · 📤 1-click to WeChat / X / Zhihu / HTML / PNG 🔑 Zero API key — Claude Code / Cursor / Codex / Gemini / Copilot / OpenCode / Qwen / Aider.

`HTML` `agent-skills` `agentic` `ai-agents` `ai-design` `ai-editor`

⭐ 5.1k • 🔱 510 • 4d ago

---

**[willchen96/mike](https://github.com/willchen96/mike)**

OSS AI Legal Platform

`TypeScript`

⭐ 3.5k • 🔱 1.1k • 9d ago

---

**[strukto-ai/mirage](https://github.com/strukto-ai/mirage)**

A Unified Virtual Filesystem For AI Agents

`TypeScript` `agent-sandbox` `agent-tools` `ai-agents` `bash` `claude-code`

⭐ 2.7k • 🔱 182 • 50m ago

---

**[simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)**

A股全栈数据工具包 — 7层架构 · 28端点 · 13数据源 · 零第三方依赖 | Full-stack China A-Share data toolkit for AI coding assistants

⭐ 2.4k • 🔱 528 • 1d ago

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

⭐ 2.0k • 🔱 140 • 10h ago

---

**[opensquilla/opensquilla](https://github.com/opensquilla/opensquilla)**

OpenSquilla — Token-Efficient AI Agent with same budget, higher intelligence density

`Python` `agent` `ai` `ai-agents` `deep-learning` `foundation-models`

⭐ 2.0k • 🔱 131 • 9h ago

---

**[mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding)**

AI coding jargon, explained in plain English.

`TypeScript`

⭐ 1.9k • 🔱 220 • 19d ago

---

**[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)**

A structured, trilingual (繁中 / 简中 / English) learning roadmap for agentic AI — from LLM basics to multi-agent systems. 8 stages · 145+ curated projects · hands-on exercises. 中文 AI agent 學習地圖。

`Python` `agentic-ai` `ai-agents` `awesome-list` `claude-code` `claude-skills`

⭐ 1.7k • 🔱 197 • 5h ago

---

---

*Generated by PeekDeck - A glance is all you need*

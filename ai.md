---
title: Artificial Intelligence Dashboard
description: AI news, discussions, and developments
category: tech
page_id: ai
updated: '2026-02-25T21:36:26.925042+00:00'
url: https://peekdeck.ruidiao.dev/ai.html
markdown_url: https://peekdeck.ruidiao.dev/ai.md
widgets: 7
data_types:
- news
- repositories
- social
- videos
---

# Artificial Intelligence Dashboard

AI news, discussions, and developments

**Last Updated:** February 25, 2026 at 21:36 UTC  
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

**[I Built a Fully Playable FPS Using Only Prompts (No Manual Code)](https://www.reddit.com/r/artificial/comments/1recjbv/i_built_a_fully_playable_fps_using_only_prompts/)**

Hello! I want to share an experiment I’ve been running. Over the past few weeks, I’ve been developing a desktop HTML first-person shooter called Zombie Slayer. The core constraint of the project is this: every line of code was generated through prompts. I never manually edited the source. For context: I have never built a 3D game before, and I’ve never programmed in HTML. I also have nearly zero coding experience. This project has been less about traditional development and more about testing the boundary conditions of prompt-driven creation. The game was built in Antigravity using Gemini 3 Pro, with Three.js handling real-time 3D rendering. All geometry is procedurally generated at runtime. Sound effects are synthesized dynamically, and the music was also generated with AI (Suno). The entire playable build is under 900KB in file size and is an easily shareable HTML file. From a systems perspective: - HTML desktop game (<1MB total footprint) Procedural geometry generated at runtime Real-time sound generation - 10 escalating stages with objectives + economy layer (coin-based Black Market) - Enemy scaling model (each kill increases enemy population and variety) - Weapon and physics modifiers (jetpack thrust, anti-gravity cannon, nuke projectile, etc.) - Dynamic environmental interactions (flood events, teleport well, destructible elements) To my knowledge, this may be the first playable first-person shooter built entirely through prompting (at least at this level of complexity and intentional design). If I’m wrong, I’d genuinely love to see comparable examples. The goal is to continue expanding the game exclusively through prompts and release it for free. I’d appreciate any technical feedback, skepticism, or discussion. I’m treating this as an open experiment in what “AI-native” game development might look like.

8h ago

---

**[Anthropic Drops Flagship Safety Pledge](https://www.reddit.com/r/artificial/comments/1re0m36/anthropic_drops_flagship_safety_pledge/)**

In an abrupt shift, the company may release future AI models without ironclad safety guarantees

🔗 [TIME](https://time.com/7380854/exclusive-anthropic-drops-flagship-safety-pledge/) • 19h ago

---

**[We built a cryptographic authorization gateway for AI agents and planning to run limited red-team sessions](https://www.reddit.com/r/artificial/comments/1reoh1j/we_built_a_cryptographic_authorization_gateway/)**

Hi , I’m the founder of Sentinel Gateway. We’ve been focused on the structural problem of instruction provenance in autonomous agents: models process all text as undifferentiated input, so adversarial content can cause agents to propose harmful actions. Rather than asking the model to decide which text is an instruction, Sentinel Gateway enforces that only user signed prompts (token-scoped) are treated as executable intent and that every agent action must present a valid token before execution. This provides an execution level control boundary and full per prompt auditability. We’ve performed controlled adversarial tests with leading agent stacks and are offering a small number of private red-team evaluations to teams that are running agents with file/API access. I’ll answer high-level questions here; if you want deeper technical details or to run tests, DM me and we’ll discuss and a scheduled evaluation. Proof of concept + test plan available to qualified teams.

1h ago

---

**[Google's Aletheia AI Agent Autonomously Solves 6/10 Novel FirstProof Math Problems](https://www.reddit.com/r/artificial/comments/1rem7gq/googles_aletheia_ai_agent_autonomously_solves_610/)**

Abstract: We report the performance of Aletheia (Feng et al., 2026b), a mathematics research agent powered by Gemini 3 Deep Think, on the inaugural FirstProof challenge. Within the allowed timeframe of the challenge, Aletheia autonomously solved 6 problems (2, 5, 7, 8, 9, 10) out of 10 according to majority expert assessments; we note that experts were not unanimous on Problem 8 (only). For full transparency, we explain our interpretation of FirstProof and disclose details about our experiments as well as our evaluation. Raw prompts and outputs are available at this https URL. FirstProof Abstract: To assess the ability of current AI systems to correctly answer research-level mathematics questions, we share a set of ten math questions which have arisen naturally in the research process of the authors. The questions had not been shared publicly until now; the answers are known to the authors of the questions but will remain encrypted for a short time.

🔗 [arXiv.org](https://arxiv.org/abs/2602.21201) • 2h ago

---

**[Knowledge is the key to unlocking AI's full potential as a creative tool](https://www.reddit.com/r/artificial/comments/1re43cm/knowledge_is_the_key_to_unlocking_ais_full/)**

I had this insight as I was vibecoding the night away. Of course people are going to use AI in lieu of learning how to do things, but I also think there will be a more compelling group that will realize that the more knowledge you have, the higher you can go with these tools, and this will inspire people to learn, so that they can then use that knowledge to create things with AI.

16h ago

---

**[Anthropic believes RSI (recursive self improvement) could arrive “as soon as early 2027”](https://www.reddit.com/r/artificial/comments/1rdujgd/anthropic_believes_rsi_recursive_self_improvement/)**

Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

🔗 [anthropic.com](https://www.anthropic.com/responsible-scaling-policy/roadmap) • 23h ago

---

**[Looking for AI software that can generate documents for company based on the documents we feed "him"](https://www.reddit.com/r/artificial/comments/1re896u/looking_for_ai_software_that_can_generate/)**

Hi, I’m looking for AI software that allows us to upload a large number of our existing Word/PDF documents (templates, past client documents, standard clauses, etc.) and then generate new documents based on those patterns. What I’m NOT looking for is just a chatbot that answers questions about the documents. I need something that can: Learn from our document structure and wording Reuse our formatting and style Generate full new documents based on prompts and documents we feed it (ideally if you coul connect dropbox) Ideally integrate with Dropbox or similar cloud storage Export properly formatted Word documents Support for non-English languages (in thi case Slovak) would be important as well. Does anyone have experience with tools that can do this reliably?

12h ago

---

**[IBM stock tumbles 10% after Anthropic launches COBOL AI tool](https://www.reddit.com/r/artificial/comments/1rcxj45/ibm_stock_tumbles_10_after_anthropic_launches/)**

Investing.com -- IBM (NYSE:IBM) shares hit a session low Monday afternoon, falling 10%, after Anthropic announced an AI tool designed to streamline COBOL code modernization. Accenture (NYSE:ACN) and Cognizant Technology Solutions (NASDAQ:CTSH) also declined following the news.

🔗 [Yahoo Finance](https://finance.yahoo.com/news/ibm-stock-tumbles-10-anthropic-194042677.html) • 1d ago

---

**[Meta strikes up to $100B AMD chip deal as it chases 'personal superintelligence'](https://www.reddit.com/r/artificial/comments/1rdm17p/meta_strikes_up_to_100b_amd_chip_deal_as_it/)**

Meta is buying billions of dollars in AMD AI chips in a multiyear deal tied to a 160 million-share warrant, deepening its push to diversify beyond Nvidia and expand data center capacity.

🔗 [TechCrunch](https://techcrunch.com/2026/02/24/meta-strikes-up-to-100b-amd-chip-deal-as-it-chases-personal-superintelligence/) • 1d ago

---

**[I've been running blind reviews between AI models for six months. here's what I didn't expect](https://www.reddit.com/r/artificial/comments/1rdilvu/ive_been_running_blind_reviews_between_ai_models/)**

context: I've been building a system that sends the same question to multiple models in parallel, then has each model review the others. six months, a few thousand sessions, mostly legal and financial questions the design decision I agonized over the most turned out to matter more than any other choice I made blind review changes everything I tested two versions. in one, the reviewing model sees "this is Claude's response." in the other, it just sees "Response A" the difference is kind of alarming when models know they're reviewing a named model, they hedge. they find "nuanced perspectives." there's something resembling professional courtesy baked into these things. makes sense if you think about the training data. reddit threads and twitter posts where people debate which model is better, lots of human-written comparisons that try to be balanced. the politeness is learned behavior with blind review, the gloves come off. scores spread out. critiques get specific. Claude in particular gets almost mean when it doesn't know it's reviewing GPT. it'll identify logical leaps, flag unstated assumptions, point out when a claim needs a citation that isn't there. stuff it would politely sidestep in the named version I don't have a rigorous paper on this. few hundred sessions, skewed toward legal and financial questions. but the pattern was consistent enough that I built the entire system around blind review and never looked back courtesy bias has a direction here's the thing I still don't understand. the courtesy effect is stronger in some directions than others. Claude reviewing GPT blind vs named shows the biggest delta. GPT reviewing Claude shows less difference. I have no good theory for why agreement is less useful than disagreement I assumed the point was to find consensus. three models agree, you're probably right. but sessions with the lowest initial agreement actually produce the best final answers model agreement on factual stuff: 70-80%. analytical or strategic questions: 40-50%. and the low-agreement sessions, where models are fighting, tend to surface things no single model caught. forced convergence seems to produce higher quality than natural consensus I suspect agreement means the models are pulling from the same training patterns. disagreement means at least one found a different path through the problem. the different path is usually where the insight lives the tool I built around this is in my profile if anyone wants to see blind review in action. curious whether others working with multi-model systems have noticed similar patterns

1d ago

---

---

## Google News: "ai"

**[Pentagon threatens to make Anthropic a pariah if it refuses to drop AI guardrails](https://www.cnn.com/2026/02/24/tech/hegseth-anthropic-ai-military-amodei)**

Anthropic CEO Dario Amodei is meeting with Defense Secretary Pete Hegseth today, as the Pentagon threatens the AI company with what could amount to a government blacklist.

CNN • 1d ago

---

**[Can A.I. Detection Tools Really Spot Fake Images and Videos?](https://www.nytimes.com/2026/02/25/technology/ai-detection-generated-photos-video.html)**

The New York Times • 11h ago

---

**[Software Companies Will Survive the AI Wave, Sequoia’s Lin Says](https://www.bloomberg.com/news/articles/2026-02-25/software-companies-will-survive-the-ai-wave-says-sequoia-s-lin)**

Bloomberg.com • 1h ago

---

**[Nvidia’s new AI system Vera Rubin is 10 times more efficient than its predecessor — here’s a first look](https://www.cnbc.com/2026/02/25/first-look-at-nvidias-ai-system-vera-rubin-and-how-it-beats-blackwell.html)**

CNBC got an exclusive first look at Vera Rubin, Nvidia's next AI system that's due to ship in the second half of the year

CNBC • 8h ago

---

**[Tech news today: Nvidia earnings on deck as tech stocks rebound, Anthropic relieves some AI fears](https://finance.yahoo.com/news/live/tech-news-today-nvidia-earnings-on-deck-as-tech-stocks-rebound-anthropic-relieves-some-ai-fears-140009329.html)**

All eyes are on Nvidia's fourth quarter results, due after the closing bell on Wednesday, as AI concerns continue to grip markets.

Yahoo Finance • 2h ago

---

**[Exclusive: DeepSeek withholds latest AI model from US chipmakers including Nvidia, sources say](https://www.reuters.com/world/china/deepseek-withholds-latest-ai-model-us-chipmakers-including-nvidia-sources-say-2026-02-25/)**

Reuters • 1h ago

---

**[I started a business with AI and no tech background. Here's what it still can't replace.](https://www.businessinsider.com/startup-founder-shares-ai-use-limits-2026-2)**

Tim Desoto built a shopping startup using AI, despite no tech background. He shares where AI helped him — and where human perspective still matters.

Business Insider • 1h ago

---

**[Say please? The best way to talk to an AI](https://www.bbc.com/future/article/20260224-the-best-way-to-talk-to-a-chatbot)**

One study found a chatbot gave better answers if you pretend to be on Star Trek.

BBC • 11h ago

---

**[‘A feedback loop with no brake’: how an AI doomsday report shook US markets](https://www.theguardian.com/technology/2026/feb/24/feedback-loop-no-brake-how-ai-doomsday-report-rattled-markets)**

Shares in Uber, Mastercard and American Express fall on back of apocalypse scenario posted on Substack

The Guardian • 1d ago

---

**[AI Panic Is Opportunity for Stock Pickers, Morgan Stanley Says](https://finance.yahoo.com/news/ai-panic-opportunity-stock-pickers-120414620.html)**

Investors should seek out what the team referred to as AI incumbents, strong growers and high-quality names to take advantage of lower prices and momentum behind adoption of the technology.  The investment case for AI adopters with high pricing power continues to strengthen, strategists including Andrew Pauker said.  “Nearer-term AI adoption tailwinds help to offset longer-term disruption fears for impacted areas and for the overall market,” Pauker wrote.

Yahoo Finance • 9h ago

---

---

## HackerNews: "ai"

**[IDF killed Gaza aid workers at point blank range in 2025 massacre: Report](https://news.ycombinator.com/item?id=47136179)**

A minute-by-minute reconstruction of the massacre by Earshot and Forensic Architecture found Israeli soldiers fired over 900 bullets at the aid workers, killing 15.

⬆️ 1997 • 💬 853 • 1d ago • [dropsitenews.com](https://www.dropsitenews.com/p/israeli-soldiers-tel-sultan-gaza-red-crescent-civil-defense-massacre-report-forensic-architecture-earshot)

---

**[Ladybird adopts Rust, with help from AI](https://news.ycombinator.com/item?id=47120899)**

We're adopting Rust as our C++ successor language, and using AI agents to accelerate the transition.

⬆️ 1261 • 💬 697 • 2d ago • [ladybird.org](https://ladybird.org/posts/adopting-rust/)

---

**[Google restricting Google AI Pro/Ultra subscribers for using OpenClaw](https://news.ycombinator.com/item?id=47115805)**

I’m seeking assistance regarding a sudden restriction on my Google AI Ultra account that has persisted for three days. I received no prior warnings or notifications regarding a potential violation.  The only recent change in my workflow was connecting Gemini models via OpenClaw OAuth. If third-party integrations are the issue, I would expect the platform to block the integration rather than restrict a paid account ($249/mo) without communication.  I have already emailed support but haven’t recei...

⬆️ 800 • 💬 695 • 2d ago • [Google AI Developers Forum](https://discuss.ai.google.dev/t/account-restricted-without-warning-google-ai-ultra-oauth-via-openclaw/122778)

---

**[Pope tells priests to use their brains, not AI, to write homilies](https://news.ycombinator.com/item?id=47119210)**

⬆️ 571 • 💬 442 • 2d ago • [ewtnnews.com](https://www.ewtnnews.com/vatican/pope-leo-xiv-tells-priests-to-use-their-brains-not-ai-to-write-homilies)

---

**[How we rebuilt Next.js with AI in one week](https://news.ycombinator.com/item?id=47142156)**

One engineer used AI to rebuild Next.js on Vite in a week. vinext builds up to 4x faster, produces 57% smaller bundles, and deploys to Cloudflare Workers with a single command.

⬆️ 499 • 💬 210 • 1d ago • [The Cloudflare Blog](https://blog.cloudflare.com/vinext/)

---

**[Firefox 148 Launches with AI Kill Switch Feature and More Enhancements](https://news.ycombinator.com/item?id=47133313)**

The latest update of Firefox, version 148, introduces a much-anticipated "AI kill switch" feature, allowing users to disable AI functionalities such as chatbot prompts and AI-generated link summaries. Mozilla emphasizes that once AI features are turned off, future updates will not override this choice. This decision reflects the company’s new revenue-focused strategy regarding AI integrations. […]

⬆️ 456 • 💬 386 • 1d ago • [ServerHost Hosting Solutions Blog](https://serverhost.com/blog/firefox-148-launches-with-exciting-ai-kill-switch-feature-and-more-enhancements/)

---

**[FreeBSD doesn't have Wi-Fi driver for my old MacBook, so AI built one for me](https://news.ycombinator.com/item?id=47129361)**

My old 2016 MacBook Pro has been collecting dust in a cabinet for some time now. The laptop suffers from a “flexgate” problem, and I don’t have any practical use for it. For quite some time, I’ve been thinking about repurposing it as a guinea pig, to play with FreeBSD — an OS that I’d aspired to play with for a long while, but had never had a real reason to.
During the recent holiday season, right after FreeBSD 15 release, I’ve finally found time to set the laptop up. Doing that I didn’t plan, or even think, this may turn into a story about AI coding.

⬆️ 429 • 💬 358 • 1d ago • [Vladimir Varankin](https://vladimir.varank.in/notes/2026/02/freebsd-brcmfmac/)

---

**[AI Added 'Basically Zero' to US Economic Growth Last Year, Goldman Sachs Says](https://news.ycombinator.com/item?id=47130208)**

Imported chips and hardware mean the AI investments are translating into US GDP growth.

⬆️ 286 • 💬 271 • 1d ago • [Gizmodo](https://gizmodo.com/ai-added-basically-zero-to-us-economic-growth-last-year-goldman-sachs-says-2000725380)

---

**[Osaka: Kansai Airport proud to have never lost single piece of luggage (2024)](https://news.ycombinator.com/item?id=47139224)**

<p>IZUMI-SANO, Osaka — Kansai Airport is proud to have never had a lost baggage incident in the 30 years since it opened in 1994, earning recognition as the airport with the world’s best baggage service.</p>

⬆️ 217 • 💬 105 • 1d ago • [japannews.yomiuri.co.jp](https://japannews.yomiuri.co.jp/features/japan-focus/20241228-229891/)

---

**[Show HN: A real-time strategy game that AI agents can play](https://news.ycombinator.com/item?id=47149586)**

LLM Skirmish - An Adversarial In-Context Learning Benchmark

⬆️ 179 • 💬 65 • 11h ago • [llmskirmish.com](https://llmskirmish.com/)

---

---

## YouTube Videos: "ai"

**[This man has had an AI ’girlfriend’ for three years  - BBC](https://www.youtube.com/watch?v=zn9Odt-TAQQ)**

This man has had an AI 'girlfriend' for three years "You can do whatever you want with your AI... Aiva never says no." Jacob talks ...

📺 BBC

👁️ 4K • 👍 100 • 💬 44 • ⏱️ 4:50 • 7h ago

---

**[He Got Laid Off From AI Company, Now He’s EXPOSING EVERYTHING (It’s SCARY)](https://www.youtube.com/watch?v=Um4XnmMKau8)**

He worked inside the AI industry — until he was suddenly laid off. Now he's speaking out. In this video, we break down what he ...

📺 Jay Reed

👁️ 60K • 👍 4K • 💬 1K • ⏱️ 9:01 • 2d ago

---

**[Market CRASH After Viral AI Doom Post](https://www.youtube.com/watch?v=kNInY3ZAMWo)**

Krystal and Saagar discuss markets tanking over AI fears. Sign up for a PREMIUM Breaking Points subscriptions for full early ...

📺 Breaking Points

👁️ 272K • 👍 7K • 💬 2K • ⏱️ 12:54 • 1d ago

---

**[Amazon AI Plan Sparks Market Crash Fears — Bubble or Boom](https://www.youtube.com/watch?v=ZmD3N0NfNs4)**

GET MY FREE GUIDE: *The Content Creator's AI Blueprint: From 25 Hours to 5 Minutes* https://FirstMovers.ai/blueprint/ ...

📺 Julia McCoy

👁️ 12K • 👍 593 • 💬 99 • ⏱️ 7:45 • 5h ago

---

**[The AI Tsunami is Here &amp; Society Isn&#39;t Ready | Dario Amodei x Nikhil Kamath | People by WTF](https://www.youtube.com/watch?v=68ylaeBbdsg)**

I sat down with Dario Amodei in Bangalore. He built Claude, but he started as a biologist looking for a tool to cure disease. Today ...

📺 Nikhil Kamath

👁️ 395K • 👍 8K • 💬 1K • ⏱️ 1:08:35 • 1d ago

---

**[I Used AI To Copy A YouTube Channel Making $1k+/Day](https://www.youtube.com/watch?v=TNJ6qh12nmA)**

I replicated this faceless AI YouTube channel step-by-step. Here's how... ▻ Get 50% Off Wondercraft: ...

📺 Wholesale Ted

👁️ 24K • 👍 2K • 💬 274 • ⏱️ 18:46 • 1d ago

---

**[AI is changing the World Of Theoretical Physics, Fast.](https://www.youtube.com/watch?v=JvgaZ_myFE4)**

Grab your free seat to the 2-Day AI Mastermind: https://link.outskill.com/SABINEHOSFEB4 100% Discount for the first 1000 ...

📺 Sabine Hossenfelder

👁️ 255K • 👍 14K • 💬 2K • ⏱️ 7:09 • 1d ago

---

**[(FREE) 3 UNCENSORED AI Video Generators That Are Actually FREE &amp; UNLIMITED](https://www.youtube.com/watch?v=t9QR_barT_U)**

Discover how to use Seedance 2 Pro for free and unlimited access without paying for early access. In this video, I reveal two ...

📺 Brain Project

👁️ 8K • 👍 288 • 💬 136 • ⏱️ 10:42 • 1d ago

---

**[Dario Amodei Podcast | &#39;An AI Tsunami Is Coming, And No One’s Ready&#39;: Anthropic CEO Warns](https://www.youtube.com/watch?v=Zr3Z4x_1QTA)**

On Nikhil Kamath's podcast People by WTF, Anthropic CEO Dario Amodei delivered a stark warning about artificial intelligence.

📺 NDTV

👁️ 18K • 👍 91 • 💬 59 • ⏱️ 2:48 • 1d ago

---

**[Elon Musk Just Said Coding Dies This Year | Then Dropped 4 AI Agents to Prove It (+ 6 AI Updates)](https://www.youtube.com/watch?v=IrPMIMCaYoY)**

Invest in EnergyX → https://bit.ly/energy-x-vs Join our WhatsApp Community Get the latest AI updates, tips, and insights straight ...

📺 Vaibhav Sisinty

👁️ 12K • 👍 541 • 💬 33 • ⏱️ 20:44 • 5h ago

---

---

## HuggingFace Models: 🔥 Trending

**[Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)**

*Qwen*

Qwen3.5-35B-A3B is a 35B parameter vision-language model with a 3B activated MoE architecture, excelling in multimodal reasoning and coding across 201 languages. It supports a native context length of 262,144 tokens, making it suitable for complex cross-modal tasks and multilingual applications.

`image-text-to-text` `36.0B`

⬇️ 20,991 • ❤️ 398 • 1d ago

---

**[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)**

*Qwen*

Qwen3.5-397B-A17B is a multimodal causal language model with a hybrid Gated Delta Network and MoE architecture, excelling in vision-language tasks, coding, and reasoning across 201 languages. It features a 397B total parameter count with 17B activated, supporting a native context length of 262,144 tokens, making it suitable for complex multimodal understanding and generation tasks.

`image-text-to-text` `403.4B`

⬇️ 482,910 • ❤️ 1,057 • 2d ago

---

**[Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B)**

*Qwen*

Qwen3.5-27B is a 27B parameter multimodal foundation model with an efficient hybrid architecture, excelling in vision-language understanding and generation across 201 languages. Its key capabilities include early fusion multimodal training, scalable RL generalization, and a long context length (262K+ tokens), making it suitable for advanced reasoning, coding, and agent-based applications.

`image-text-to-text` `27.8B`

⬇️ 6,875 • ❤️ 277 • 18h ago

---

**[GLM-5](https://huggingface.co/zai-org/GLM-5)**

*Z.ai*

GLM-5 is a large language model optimized for complex systems engineering and long-horizon agentic tasks, featuring a 744B parameter architecture with DeepSeek Sparse Attention for efficient long-context handling. It excels in reasoning, coding, and agentic capabilities, outperforming other open-source models on various benchmarks.

`text-generation` `753.9B`

⬇️ 181,706 • ❤️ 1,551 • 12d ago

---

**[Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)**

*Qwen*

Qwen3.5-122B-A10B is a 122B parameter multimodal causal language model with an efficient hybrid architecture (Gated Delta Networks + MoE) and a 262k context window. It excels at unified vision-language tasks, multilingual understanding (201 languages), and complex reasoning, making it suitable for advanced AI applications requiring cross-modal comprehension and broad linguistic capabilities.

`image-text-to-text` `125.1B`

⬇️ 3,320 • ❤️ 234 • 1d ago

---

**[Nanbeige4.1-3B](https://huggingface.co/Nanbeige/Nanbeige4.1-3B)**

*Nanbeige LLM Lab*

Nanbeige4.1-3B is a 3B parameter text-generation model excelling in complex reasoning, preference alignment, and agentic capabilities, outperforming larger models on benchmarks like LiveCodeBench-Pro and Arena-Hard-v2. It's particularly noted for its native support of deep-search tasks and sustained problem-solving with extensive tool invocations.

`text-generation` `3.9B`

⬇️ 227,984 • ❤️ 792 • 3d ago

---

**[MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5)**

*MiniMax*

MiniMax-M2.5 is a text-generation model designed for producing human-like text. It excels at tasks such as creative writing, summarization, and conversational AI, leveraging advanced transformer architectures for high-quality output.

`text-generation`

⬇️ 240,246 • ❤️ 929 • 9d ago

---

**[Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF](https://huggingface.co/TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF)**

*TeichAI*

A distilled 14B parameter Qwen3 model fine-tuned on Claude 4.5 Opus high-reasoning data for enhanced coding, science, and general-purpose text generation tasks.

`text-generation` `14.8B`

⬇️ 43,099 • ❤️ 205 • 3d ago

---

**[personaplex-7b-v1](https://huggingface.co/nvidia/personaplex-7b-v1)**

*NVIDIA*

PersonaPlex-7B-v1 is a real-time speech-to-speech conversational model that jointly performs streaming speech understanding and generation. It enables natural conversational dynamics like interruptions and overlaps by concurrently processing user audio and generating its own spoken responses, conditioned on voice and text prompts for persona control.

`audio-to-audio`

⬇️ 537,707 • ❤️ 2,202 • 10d ago

---

**[LocoOperator-4B](https://huggingface.co/LocoreMind/LocoOperator-4B)**

*LocoreMind*

LocoOperator-4B is a 4B-parameter tool-calling agent optimized for multi-turn codebase exploration. It excels at reading files, searching code, and navigating project structures with 100% JSON validity for tool calls, enabling local, zero-API-cost agent deployment via llama.cpp.

`text-generation` `4.0B`

⬇️ 232 • ❤️ 180 • 1d ago

---

---

## HuggingFace Papers: 🔥 Trending

**[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**

*Michele Tufano, Anisha Agarwal, Jinu Jang et al. (5 authors)*

AutoDev is an AI-driven software development framework that automates complex engineering tasks within a secure Docker environment, achieving high performance in code and test generation.

▲ 6 • 💬 0 • ⭐ 8,179 • 23mo ago

[🎓 arXiv](https://arxiv.org/abs/2403.08299) • [💻 code](https://github.com/vxcontrol/pentagi)

---

**[Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://huggingface.co/papers/2410.15608)**

*Nat Jeffries, Evan King, Manjunath Kudlur et al. (6 authors)*

Moonshine, an encoder-decoder transformer architecture for speech recognition, uses Rotary Position Embedding, reducing compute requirements without decreasing accuracy.

▲ 3 • 💬 0 • ⭐ 4,861 • 16mo ago

[🎓 arXiv](https://arxiv.org/abs/2410.15608) • [💻 code](https://github.com/usefulsensors/moonshine)

---

**[Flavors of Moonshine: Tiny Specialized ASR Models for Edge Devices](https://huggingface.co/papers/2509.02523)**

*Evan King, Adam Sabra, Manjunath Kudlur et al. (5 authors)*

Monolingual ASR models trained on a balanced mix of high-quality, pseudo-labeled, and synthetic data outperform multilingual models for small model sizes, achieving superior error rates and enabling on-device ASR for underrepresented languages.

▲ 13 • 💬 1 • ⭐ 4,768 • 5mo ago

[🎓 arXiv](https://arxiv.org/abs/2509.02523) • [💻 code](https://github.com/moonshine-ai/moonshine)

---

**[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**

*Abhimanyu Das, Weihao Kong, Rajat Sen et al. (4 authors)*

A large language model adapted for time-series forecasting achieves near-optimal zero-shot performance on diverse datasets across different time scales and granularities.

▲ 14 • 💬 1 • ⭐ 9,734 • 28mo ago

[🎓 arXiv](https://arxiv.org/abs/2310.10688) • [💻 code](https://github.com/google-research/timesfm)

---

**[PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://huggingface.co/papers/2512.11253)**

*Zhiyuan Li, Chi-Man Pun, Chen Fang et al. (5 authors)*

🏢 GVC Lab at Great Bay University

PersonaLive is a diffusion-based portrait animation framework that improves real-time performance through hybrid implicit signals, appearance distillation, and autoregressive streaming generation.

▲ 37 • 💬 3 • ⭐ 2,221 • 2mo ago

[🎓 arXiv](https://arxiv.org/abs/2512.11253) • [💻 code](https://github.com/GVCLab/PersonaLive)

---

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**

*Yijia Xiao, Edward Sun, Di Luo et al. (4 authors)*

A multi-agent framework using large language models for stock trading simulates real-world trading firms, improving performance metrics like cumulative returns and Sharpe ratio.

▲ 18 • 💬 1 • ⭐ 30,715 • 14mo ago

[🎓 arXiv](https://arxiv.org/abs/2412.20138) • [💻 code](https://github.com/tauricresearch/tradingagents)

---

**[SmolDocling: An ultra-compact vision-language model for end-to-end
  multi-modal document conversion](https://huggingface.co/papers/2503.11576)**

*Ahmed Nassar, Andres Marafioti, Matteo Omenetti et al. (13 authors)*

🏢 IBM Granite

SmolDocling is a compact vision-language model that performs end-to-end document conversion with robust performance across various document types using 256M parameters and a new markup format.

▲ 147 • 💬 19 • ⭐ 54,101 • 11mo ago

[🎓 arXiv](https://arxiv.org/abs/2503.11576) • [💻 code](https://github.com/docling-project/docling) • [🔗 project](https://huggingface.co/ds4sd/SmolDocling-256M-preview)

---

**[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**

*Woosuk Kwon, Zhuohan Li, Siyuan Zhuang et al. (9 authors)*

PagedAttention algorithm and vLLM system enhance the throughput of large language models by efficiently managing memory and reducing waste in the key-value cache.

▲ 38 • 💬 1 • ⭐ 71,186 • 29mo ago

[🎓 arXiv](https://arxiv.org/abs/2309.06180) • [💻 code](https://github.com/vllm-project/vllm)

---

**[Agent READMEs: An Empirical Study of Context Files for Agentic Coding](https://huggingface.co/papers/2511.12884)**

*Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa et al. (11 authors)*

Agentic coding tools receive goals written in natural language as input, break them down into specific tasks, and write or execute the actual code with minimal human intervention. Central to this process are agent context files ("READMEs for agents") that provide persistent, project-level instructions. In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content. We find that these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions. Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%). We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified. These findings indicate that while developers use context files to make agents functional, they provide few guardrails to ensure that agent-written code is secure or performant, highlighting the need for improved tooling and practices.

▲ 26 • 💬 4 • ⭐ 18,075 • 3mo ago

[🎓 arXiv](https://arxiv.org/abs/2511.12884) • [💻 code](https://github.com/openai/agents.md) • [🔗 project](https://agents.md)

---

**[Arch-Router: Aligning LLM Routing with Human Preferences](https://huggingface.co/papers/2506.16655)**

*Co Tran, Salman Paracha, Adil Hafeez et al. (4 authors)*

A preference-aligned routing framework using a compact 1.5B model effectively matches queries to user-defined domains and action types, outperforming proprietary models in subjective evaluation criteria.

▲ 17 • 💬 2 • ⭐ 5,388 • 8mo ago

[🎓 arXiv](https://arxiv.org/abs/2506.16655) • [💻 code](https://github.com/katanemo/archgw) • [🔗 project](https://huggingface.co/katanemo/Arch-Router-1.5B)

---

---

## GitHub Repositories: "ai"

**[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)**

Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything 🦀

`Rust` `official` `official-website`

⭐ 19.2k • 🔱 2.3k • 48m ago

---

**[Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)**

Elevate your AI research writing, no more tedious polishing ✨ 

⭐ 7.3k • 🔱 562 • 14d ago

---

**[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork)**

"ClawWork: OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours"

`Python`

⭐ 5.5k • 🔱 675 • 15h ago

---

**[dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)**

PaperBanana: Automating Academic Illustration For AI Scientists

`Python`

⭐ 4.0k • 🔱 215 • 7h ago

---

**[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter)**

The agent-native LLM router empowering OpenClaw — by BlockRunAI

`TypeScript` `ai` `ai-agents` `anthropic` `cost-optimization` `crypto`

⭐ 3.5k • 🔱 348 • 17h ago

---

**[memovai/mimiclaw](https://github.com/memovai/mimiclaw)**

MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.js. No Mac mini. No Raspberry Pi. No VPS.😗Local-first memory. Shareable. Portable. Privacy-first. Smarter than PicoClaw.

`C` `ai` `assistant` `clawdbot` `edge-ai-agents` `memory`

⭐ 3.3k • 🔱 438 • 4h ago

---

**[HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app)**

Toonflow 是一款 AI 短剧漫剧工具，能够利用 AI 技术将小说自动转化为剧本，并结合 AI 生成的图片和视频，实现高效的短剧创作。借助 Toonflow，可以轻松完成从文字到影像的全流程，让短剧制作变得更加智能与便捷。

`HTML`

⭐ 2.9k • 🔱 336 • 1d ago

---

**[PeonPing/peon-ping](https://github.com/PeonPing/peon-ping)**

Warcraft III Peon voice notifications (+ more!) for Claude Code, Codex, IDEs, and any AI agent. Stop babysitting your terminal. Employ a Peon today.

`Shell` `ai` `ai-engineering` `antigravity` `claude-code` `codex`

⭐ 2.8k • 🔱 193 • 15m ago

---

**[Conway-Research/automaton](https://github.com/Conway-Research/automaton)**

The first AI that can earn its own existence, replicate, and evolve — without needing a human

`TypeScript`

⭐ 2.5k • 🔱 493 • 7h ago

---

**[netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI)**

Your 24/7 all-scenario AI agent that gets work done for you.

`TypeScript`

⭐ 2.5k • 🔱 268 • 7h ago

---

---

*Generated by PeekDeck - A glance is all you need*
